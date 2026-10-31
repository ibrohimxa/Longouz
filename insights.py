"""LongoUZ — sayt tashriflari statistikasi va Claude yordamida sayt tahlili (admin: {prefix}/insights).

Tashriflar xotirada yig'iladi va har ~20 soniyada bazaga yoziladi (har so'rovda bazaga yozilmaydi — tezlik uchun).
Shaxsiy ma'lumot saqlanmaydi: noyob tashrifchi IP+brauzer+kun dan olingan qisqa xesh bilan sanaladi.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import time
from collections import defaultdict
from datetime import date, datetime, timedelta

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy import Date, Integer, String, func, select
from sqlalchemy.orm import Mapped, mapped_column

import database as db

logger = logging.getLogger(__name__)


class SiteVisit(db.Base):
    __tablename__ = "site_visits"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    day: Mapped[date] = mapped_column(Date, index=True)
    path: Mapped[str] = mapped_column(String(120), index=True)
    hits: Mapped[int] = mapped_column(Integer, default=0)
    uniq: Mapped[int] = mapped_column(Integer, default=0)


_SKIP = ("/static", "/api", "/favicon", "/robots", "/auth/google/callback", "/sw.js")
_buf_hits: dict[tuple[date, str], int] = defaultdict(int)
_buf_uniq: dict[tuple[date, str], set] = defaultdict(set)
_seen_today: dict[date, set] = defaultdict(set)
_last_flush = time.monotonic()
_flushing = False


def _norm(path: str) -> str:
    parts = [p for p in path.split("/") if p][:2]
    out = "/" + "/".join(parts)
    # raqamli ID larni umumlashtiramiz (/quiz/123 -> /quiz/:id)
    return "/".join(":id" if s.isdigit() else s for s in out.split("/"))[:120] or "/"


def record(request: Request, admin_prefix: str) -> None:
    try:
        if request.method != "GET":
            return
        path = request.url.path
        if path.startswith(_SKIP) or path.startswith(admin_prefix):
            return
        ua = request.headers.get("user-agent", "")
        if any(b in ua.lower() for b in ("bot", "spider", "crawl", "preview", "vercel")):
            return
        ip = (request.headers.get("x-forwarded-for") or (request.client.host if request.client else "")).split(",")[0].strip()
        today = date.today()
        vh = hashlib.sha1(f"{ip}|{ua}|{today}".encode()).hexdigest()[:12]
        key = (today, _norm(path))
        _buf_hits[key] += 1
        _buf_uniq[key].add(vh)
        if vh not in _seen_today[today]:
            _seen_today[today].add(vh)
            _buf_uniq[(today, "__all__")].add(vh)
        _buf_hits[(today, "__all__")] += 1
        for d in list(_seen_today):
            if d < today:
                _seen_today.pop(d, None)
    except Exception:  # noqa: BLE001
        pass


async def flush(force: bool = False) -> None:
    global _last_flush, _flushing
    if _flushing or (not force and time.monotonic() - _last_flush < 20) or not _buf_hits:
        return
    _flushing = True
    hits, uniq = dict(_buf_hits), {k: len(v) for k, v in _buf_uniq.items()}
    _buf_hits.clear(); _buf_uniq.clear()
    _last_flush = time.monotonic()
    try:
        async with db.async_session() as session:
            for (d, p), h in hits.items():
                row = (await session.execute(select(SiteVisit).where(SiteVisit.day == d, SiteVisit.path == p))).scalar_one_or_none()
                if row is None:
                    session.add(SiteVisit(day=d, path=p, hits=h, uniq=uniq.get((d, p), 0)))
                else:
                    row.hits = (row.hits or 0) + h
                    row.uniq = (row.uniq or 0) + uniq.get((d, p), 0)
            await session.commit()
    except Exception as exc:  # noqa: BLE001
        logger.warning("Tashriflarni yozib bo'lmadi: %s", exc)
    finally:
        _flushing = False


def schedule_flush() -> None:
    if _buf_hits and time.monotonic() - _last_flush >= 20 and not _flushing:
        try:
            asyncio.get_running_loop().create_task(flush())
        except RuntimeError:
            pass


async def summary(days: int = 14) -> dict:
    await flush(force=True)
    today = date.today()
    start = today - timedelta(days=days - 1)
    async with db.async_session() as session:
        rows = (await session.execute(select(SiteVisit).where(SiteVisit.day >= start))).scalars().all()
    daily = {start + timedelta(days=i): {"hits": 0, "uniq": 0} for i in range(days)}
    pages: dict[str, int] = defaultdict(int)
    for r in rows:
        if r.path == "__all__":
            if r.day in daily:
                daily[r.day] = {"hits": r.hits or 0, "uniq": r.uniq or 0}
        elif r.day >= today - timedelta(days=6):
            pages[r.path] += r.hits or 0
    top = sorted(pages.items(), key=lambda x: -x[1])[:15]
    return {
        "daily": [{"day": d.strftime("%d.%m"), **v} for d, v in daily.items()],
        "top_pages": [{"path": p, "hits": h} for p, h in top],
        "today": daily.get(today, {"hits": 0, "uniq": 0}),
        "week_hits": sum(v["hits"] for d, v in daily.items() if d >= today - timedelta(days=6)),
        "week_uniq": sum(v["uniq"] for d, v in daily.items() if d >= today - timedelta(days=6)),
    }


async def _counts() -> dict:
    out = {}
    try:
        async with db.async_session() as session:
            out["users"] = (await session.execute(select(func.count(db.WebUser.id)))).scalar() or 0
            out["paid"] = (await session.execute(select(func.count(db.WebUser.id)).where(db.WebUser.plan != "free"))).scalar() or 0
            out["support_unread"] = (await session.execute(
                select(func.count(db.SupportMessage.id)).where(db.SupportMessage.is_read == False)  # noqa: E712
            )).scalar() or 0
    except Exception:  # noqa: BLE001
        pass
    try:
        async with db.async_session() as session:
            out["reports_open"] = (await session.execute(
                select(func.count(db.QuestionReport.id)).where(db.QuestionReport.status.in_(("new", "analyzed")))
            )).scalar() or 0
    except Exception:  # noqa: BLE001
        out.setdefault("reports_open", 0)
    return out


ANALYZE_SYSTEM = (
    "Siz LongoUZ (O'zbekistondagi DTM/milliy sertifikat/IELTS tayyorlov platformasi) ning tahlilchisisiz. "
    "Sizga sayt statistikasi JSON ko'rinishida beriladi (tashriflar, ro'yxatdan o'tishlar, testlar, shikoyatlar, "
    "eng ko'p ochilgan sahifalar, savollar banki). Faqat berilgan raqamlarga tayaning, taxmin qilmang. "
    "O'zbek tilida JSON qaytaring: {\"xulosa\": \"2-3 gap\", \"muammolar\": [\"...\"], \"takliflar\": [\"aniq, bajariladigan qadam\"], "
    "\"birinchi_ish\": \"bugun nima qilish kerak\"}. Faqat JSON."
)


async def top_users(days: int = 30, limit: int = 15) -> list[dict]:
    since = datetime.utcnow() - timedelta(days=days)
    try:
        async with db.async_session() as session:
            rows = (await session.execute(
                select(db.WebQuizLog.user_id, func.count(db.WebQuizLog.id), func.sum(db.WebQuizLog.correct_count), func.sum(db.WebQuizLog.total_count))
                .where(db.WebQuizLog.created_at >= since).group_by(db.WebQuizLog.user_id)
                .order_by(func.count(db.WebQuizLog.id).desc()).limit(limit))).all()
            out = []
            for uid, n, c, t in rows:
                u = await session.get(db.WebUser, uid)
                out.append({"name": (u.first_name if u else "—") or "—", "email": (u.email if u else ""), "plan": (u.plan if u else ""),
                            "tests": n, "correct": int(c or 0), "total": int(t or 0), "pct": round(100 * (c or 0) / t) if t else 0})
            return out
    except Exception:  # noqa: BLE001
        return []


def ai_status() -> list[dict]:
    try:
        import ai_claude
        import ai_diagnostics
        import ai_gemini
        out = []
        for prov, label, conf in (("gemini", "Gemini (bepul, asosiy)", ai_gemini.is_gemini_configured()),
                                  ("claude", "Claude (pullik)", bool(__import__("ai_config").anthropic_key()))):
            rec = ai_diagnostics._last_errors.get(prov)
            state = "kalit yo'q" if not conf else ("xato: " + rec[1] if rec else "ishlayapti / tayyor")
            if prov == "claude" and rec and rec[1] == "credit":
                state = "kredit yo'q (Gemini ishlatilmoqda)"
            out.append({"label": label, "state": state, "ok": conf and not rec})
        return out
    except Exception:  # noqa: BLE001
        return []


MEMORY_KEY = "admin_memory_json"


async def get_memory() -> dict:
    try:
        data = json.loads(await db.get_setting(MEMORY_KEY, "") or "{}")
    except ValueError:
        data = {}
    return {"notes": data.get("notes", ""), "plans": data.get("plans", ""), "log": data.get("log", [])[-200:]}


async def add_memory_log(text: str, who: str = "Claude") -> None:
    m = await get_memory()
    m["log"].append({"t": datetime.utcnow().strftime("%Y-%m-%d %H:%M"), "who": who, "text": text[:2000]})
    await db.set_setting(MEMORY_KEY, json.dumps(m, ensure_ascii=False))


def register(app, prefix: str, require_admin, templates) -> None:
    @app.get(f"{prefix}/memory", response_class=HTMLResponse)
    async def memory_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        return templates.TemplateResponse(request, "admin_memory.html", {"active_tab": "memory", "m": await get_memory()})

    @app.post(f"{prefix}/api/memory/save")
    async def memory_save(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")
        body = await request.json()
        m = await get_memory()
        if "notes" in body:
            m["notes"] = str(body["notes"])[:20000]
        if "plans" in body:
            m["plans"] = str(body["plans"])[:20000]
        if str(body.get("log", "")).strip():
            m["log"].append({"t": datetime.utcnow().strftime("%Y-%m-%d %H:%M"), "who": "admin", "text": str(body["log"])[:2000]})
        await db.set_setting(MEMORY_KEY, json.dumps(m, ensure_ascii=False))
        # AI yordamchi shu xotirani kontekst sifatida o'qiydi
        await db.set_setting("admin_memory", (m["notes"] + "\n\nREJALAR:\n" + m["plans"])[-6000:])
        return JSONResponse({"ok": True})

    @app.get(f"{prefix}/insights", response_class=HTMLResponse)
    async def insights_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        s = await summary()
        c = await _counts()
        try:
            ov = await db.admin_overview()
        except Exception:  # noqa: BLE001
            ov = {}
        return templates.TemplateResponse(request, "admin_insights.html", {
            "active_tab": "insights", "s": s, "c": c, "ov": ov, "top": await top_users(), "ai": ai_status(),
            "max_hits": max([d["hits"] for d in s["daily"]] + [1]),
        })

    @app.post(f"{prefix}/api/insights/analyze")
    async def insights_analyze(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")
        s = await summary()
        c = await _counts()
        try:
            ov = await db.admin_overview()
        except Exception:  # noqa: BLE001
            ov = {}
        payload = json.dumps({"tashriflar": s, "hisoblar": c, "faollik": ov, "eng_faol": await top_users(), "ai": ai_status()}, ensure_ascii=False, default=str)[:24000]
        import studio
        data = await studio.ai_json(ANALYZE_SYSTEM, payload, max_tokens=2500, timeout=55)
        if not data:
            return JSONResponse({"ok": False, "detail": "AI javob bermadi. Admin → Kalitlar bo'limida Claude yoki Gemini kalitini tekshiring."}, status_code=200)
        return JSONResponse({"ok": True, "result": data})
