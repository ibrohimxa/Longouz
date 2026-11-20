"""LongoUZ — HAQIQIY tashrif statistikasi (v243).

Muammo (v242 gacha): har bir sahifa ochilishi "ko'rish" deb sanalardi — sahifani yangilasangiz (F5) raqam oshib ketardi,
Vercel'ning har bir instansi noyob tashrifchilarni alohida sanagani uchun «kishi» soni ham ko'payib ketardi.

Endi:
  * har brauzerga bir marta tasodifiy `lz_vid` cookie beriladi (shaxsiy ma'lumot emas, 1 yil);
  * «tashrif» = sessiya: odam 30 daqiqadan ko'proq tanaffusdan keyin qaytsa — yangi tashrif. Yangilash (F5) sanalmaydi;
  * «odam» = bugun saytga kirgan noyob brauzer (bazada (kun, vid) juftligi bilan bir marta sanaladi — barcha instanslar uchun);
  * «onlayn» = oxirgi 5 daqiqada faol bo'lganlar;
  * hodisalar: test boshlandi / test tugadi (natija chiqdi) / AI savol / shikoyat / ro'yxatdan o'tish — kunlik hisoblagichlar.
"""
from __future__ import annotations

import json
import logging
import secrets
import time
from datetime import date, datetime, timedelta

from sqlalchemy import Date, DateTime, Integer, String, UniqueConstraint, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped, mapped_column

import database as db

logger = logging.getLogger("longouz.traffic")

VID_COOKIE = "lz_vid"
SESSION_GAP = timedelta(minutes=30)
ONLINE_WINDOW = timedelta(minutes=5)
_BOT_WORDS = ("bot", "spider", "crawl", "preview", "vercel", "headless", "python-requests", "curl", "wget", "monitor",
              "lighthouse", "facebookexternalhit", "telegram", "whatsapp", "slurp", "httpx", "go-http", "uptime")
_SKIP = ("/static", "/api", "/favicon", "/robots", "/auth/google", "/sw.js", "/news/img", "/certificate", "/verify")


class SiteVisitor(db.Base):
    __tablename__ = "site_visitors"
    vid: Mapped[str] = mapped_column(String(40), primary_key=True)
    first_seen: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_seen: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    visits: Mapped[int] = mapped_column(Integer, default=1)
    pages: Mapped[int] = mapped_column(Integer, default=1)
    user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
    device: Mapped[str] = mapped_column(String(12), default="")


class SiteVisitorDay(db.Base):
    __tablename__ = "site_visitor_days"
    __table_args__ = (UniqueConstraint("day", "vid", name="uq_visitor_day"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    day: Mapped[date] = mapped_column(Date, index=True)
    vid: Mapped[str] = mapped_column(String(40))


class SiteDaily(db.Base):
    __tablename__ = "site_daily"
    __table_args__ = (UniqueConstraint("day", "key", name="uq_site_daily"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    day: Mapped[date] = mapped_column(Date, index=True)
    key: Mapped[str] = mapped_column(String(40), index=True)
    n: Mapped[int] = mapped_column(Integer, default=0)


EVENT_NAMES = {
    "visits": "Tashriflar", "visitors": "Odamlar (noyob)", "new_visitors": "Yangi odamlar", "pageviews": "Sahifa ochilishi",
    "quiz_start": "Test boshlandi", "quiz_finish": "Test tugadi (natija chiqdi)", "ai_ask": "AI savollari",
    "report": "Shikoyatlar", "signup": "Ro'yxatdan o'tish", "support": "Yordam xabarlari",
}

_tables_ready = False
_recent: dict[str, float] = {}      # vid -> oxirgi bazaga yozilgan vaqt (shu instans ichida)
_marked_day: dict[str, date] = {}   # vid -> bugun sanalganmi


async def _ensure_tables() -> None:
    global _tables_ready
    if _tables_ready:
        return
    try:
        async with db.engine.begin() as conn:
            await conn.run_sync(lambda c: db.Base.metadata.create_all(
                c, tables=[SiteVisitor.__table__, SiteVisitorDay.__table__, SiteDaily.__table__]))
        _tables_ready = True
    except Exception:  # noqa: BLE001
        logger.exception("traffic jadvallarini yaratib bo'lmadi")


async def bump(key: str, n: int = 1, day: date | None = None) -> None:
    """Kunlik hisoblagichni oshiradi (barcha instanslar uchun bitta bazada)."""
    if n <= 0:
        return
    await _ensure_tables()
    d = day or date.today()
    try:
        async with db.async_session() as session:
            res = await session.execute(update(SiteDaily).where(SiteDaily.day == d, SiteDaily.key == key).values(n=SiteDaily.n + n))
            if res.rowcount == 0:
                session.add(SiteDaily(day=d, key=key, n=n))
                try:
                    await session.commit()
                    return
                except IntegrityError:
                    await session.rollback()
                    await session.execute(update(SiteDaily).where(SiteDaily.day == d, SiteDaily.key == key).values(n=SiteDaily.n + n))
            await session.commit()
    except Exception:  # noqa: BLE001
        logger.warning("hisoblagich %s yozilmadi", key, exc_info=True)


def _is_bot(ua: str) -> bool:
    low = (ua or "").lower()
    return not low or any(w in low for w in _BOT_WORDS)


def _device(ua: str) -> str:
    low = (ua or "").lower()
    if "ipad" in low or "tablet" in low:
        return "planshet"
    if "mobi" in low or "android" in low or "iphone" in low:
        return "telefon"
    return "kompyuter"


def should_track(request, admin_prefix: str) -> bool:
    if request.method != "GET":
        return False
    path = request.url.path
    if path.startswith(_SKIP) or path.startswith(admin_prefix):
        return False
    if request.headers.get("purpose") == "prefetch" or request.headers.get("sec-purpose", "").startswith("prefetch"):
        return False
    return not _is_bot(request.headers.get("user-agent", ""))


async def track(request, response, admin_prefix: str, user_id: int | None = None) -> None:
    """HTML sahifa javobidan keyin chaqiriladi. Yangilash (F5) tashrif sonini OSHIRMAYDI."""
    if not should_track(request, admin_prefix):
        return
    vid = request.cookies.get(VID_COOKIE, "")
    is_new_cookie = not (vid and 16 <= len(vid) <= 40 and vid.replace("-", "").replace("_", "").isalnum())
    if is_new_cookie:
        vid = secrets.token_urlsafe(18)
        try:
            import auth as _auth
            response.set_cookie(VID_COOKIE, vid, max_age=60 * 60 * 24 * 365, httponly=True, samesite="lax",
                                secure=bool(_auth.COOKIE_SECURE), path="/")
        except Exception:  # noqa: BLE001
            pass
    now_m = time.monotonic()
    today = date.today()
    # shu instansda shu brauzer 60 soniya ichida yozilgan bo'lsa — bazaga tegmaymiz (F5 bosib turish ham hech narsa qo'shmaydi)
    if not is_new_cookie and now_m - _recent.get(vid, -1e9) < 60 and _marked_day.get(vid) == today:
        return
    _recent[vid] = now_m
    if len(_recent) > 5000:
        for k in sorted(_recent, key=_recent.get)[:2500]:
            _recent.pop(k, None)
            _marked_day.pop(k, None)
    await _ensure_tables()
    now = datetime.utcnow()
    new_visit = new_person = False
    try:
        async with db.async_session() as session:
            row = await session.get(SiteVisitor, vid)
            if row is None:
                session.add(SiteVisitor(vid=vid, first_seen=now, last_seen=now, visits=1, pages=1, user_id=user_id,
                                        device=_device(request.headers.get("user-agent", ""))))
                new_visit = new_person = True
            else:
                if row.last_seen is None or now - row.last_seen > SESSION_GAP:
                    row.visits = (row.visits or 0) + 1
                    new_visit = True
                row.last_seen = now
                row.pages = (row.pages or 0) + 1
                if user_id and row.user_id != user_id:
                    row.user_id = user_id
            try:
                await session.commit()
            except IntegrityError:          # ikki instans bir vaqtda yaratdi
                await session.rollback()
                new_visit = new_person = False
        if _marked_day.get(vid) != today:
            async with db.async_session() as session:
                session.add(SiteVisitorDay(day=today, vid=vid))
                try:
                    await session.commit()
                    await bump("visitors")
                    if not new_visit:
                        new_visit = True   # bugungi birinchi kirish — har doim tashrif
                        async with db.async_session() as s2:
                            await s2.execute(update(SiteVisitor).where(SiteVisitor.vid == vid).values(visits=SiteVisitor.visits + 1))
                            await s2.commit()
                except IntegrityError:
                    await session.rollback()
            _marked_day[vid] = today
        if new_visit:
            await bump("visits")
        if new_person:
            await bump("new_visitors")
    except Exception:  # noqa: BLE001
        logger.warning("tashrifni yozib bo'lmadi", exc_info=True)


# --------------------------------------------------------------------------- o'qish
async def _sum(session, key: str, since: date | None = None, day: date | None = None) -> int:
    stmt = select(func.coalesce(func.sum(SiteDaily.n), 0)).where(SiteDaily.key == key)
    if since is not None:
        stmt = stmt.where(SiteDaily.day >= since)
    if day is not None:
        stmt = stmt.where(SiteDaily.day == day)
    return int((await session.execute(stmt)).scalar() or 0)


async def _baseline() -> dict:
    """v242 gacha yig'ilgan raqamlar yo'qolmasin: eski jadvaldagi (site_visits) ko'rsatkichlar bir marta qotiriladi."""
    raw = await db.get_setting("traffic_baseline_v243", "")
    if raw:
        try:
            return json.loads(raw)
        except ValueError:
            pass
    base = {"views": 0, "visitors": 0, "cutover": date.today().isoformat()}
    try:
        import insights
        async with db.async_session() as session:
            v = (await session.execute(select(func.coalesce(func.sum(insights.SiteVisit.hits), 0),
                                              func.coalesce(func.sum(insights.SiteVisit.uniq), 0))
                                       .where(insights.SiteVisit.path == "__all__", insights.SiteVisit.day < date.today()))).one()
            # eski «ko'rishlar» F5 bilan oshib ketgan — tashrif sifatida noyob kunlik tashrifchilar yig'indisi olinadi
            base["views"], base["visitors"] = int(v[1] or 0), int(v[1] or 0)
    except Exception:  # noqa: BLE001
        logger.debug("baseline", exc_info=True)
    await db.set_setting("traffic_baseline_v243", json.dumps(base))
    return base


_CACHE = {"t": 0.0, "d": None}


async def public_numbers() -> dict:
    """Kabinet va admin kartalari uchun (15 soniya kesh)."""
    if _CACHE["d"] and time.monotonic() - _CACHE["t"] < 15:
        return dict(_CACHE["d"])
    await _ensure_tables()
    today = date.today()
    base = await _baseline()
    out = {"views": 0, "visitors": 0, "today_views": 0, "today_visitors": 0, "online": 0, "users": 0, "new_users_today": 0,
           "tests": 0, "tests_today": 0, "tests_started": 0, "tests_started_today": 0, "finish_rate": 0, "accuracy": 0,
           "today_accuracy": 0, "ai_today": 0}
    try:
        async with db.async_session() as session:
            out["views"] = base.get("views", 0) + await _sum(session, "visits")
            out["visitors"] = base.get("visitors", 0) + await _sum(session, "visitors")
            out["today_views"] = await _sum(session, "visits", day=today)
            out["today_visitors"] = await _sum(session, "visitors", day=today)
            out["online"] = int((await session.execute(select(func.count()).select_from(SiteVisitor)
                                                       .where(SiteVisitor.last_seen >= datetime.utcnow() - ONLINE_WINDOW))).scalar() or 0)
            out["users"] = int((await session.execute(select(func.count(db.WebUser.id)))).scalar() or 0)
            out["new_users_today"] = int((await session.execute(select(func.count(db.WebUser.id)).where(db.WebUser.joined_at >= today))).scalar() or 0)
            q = (await session.execute(select(func.count(db.WebQuizLog.id), func.coalesce(func.sum(db.WebQuizLog.correct_count), 0),
                                              func.coalesce(func.sum(db.WebQuizLog.total_count), 0)))).one()
            out["tests"] = int(q[0] or 0)
            out["accuracy"] = round(100 * int(q[1] or 0) / int(q[2])) if q[2] else 0
            start = datetime.combine(today, datetime.min.time())
            qt = (await session.execute(select(func.count(db.WebQuizLog.id), func.coalesce(func.sum(db.WebQuizLog.correct_count), 0),
                                               func.coalesce(func.sum(db.WebQuizLog.total_count), 0)).where(db.WebQuizLog.created_at >= start))).one()
            out["tests_today"] = int(qt[0] or 0)
            out["today_accuracy"] = round(100 * int(qt[1] or 0) / int(qt[2])) if qt[2] else 0
            out["tests_started"] = max(await _sum(session, "quiz_start"), 0)
            out["tests_started_today"] = await _sum(session, "quiz_start", day=today)
            fin_since = await _sum(session, "quiz_finish")
            out["finish_rate"] = min(100, round(100 * fin_since / out["tests_started"])) if out["tests_started"] else 0
            out["ai_today"] = await _sum(session, "ai_ask", day=today)
    except Exception:  # noqa: BLE001
        logger.warning("public_numbers", exc_info=True)
    _CACHE.update(t=time.monotonic(), d=dict(out))
    return out


async def daily_series(days: int = 14) -> list[dict]:
    """Admin grafik: har kun uchun tashrif, odam, yangi odam, test boshlandi/tugadi, AI, ro'yxatdan o'tish."""
    await _ensure_tables()
    today = date.today()
    start = today - timedelta(days=days - 1)
    series = {start + timedelta(days=i): {k: 0 for k in EVENT_NAMES} for i in range(days)}
    try:
        async with db.async_session() as session:
            rows = (await session.execute(select(SiteDaily).where(SiteDaily.day >= start))).scalars().all()
            for r in rows:
                if r.day in series and r.key in series[r.day]:
                    series[r.day][r.key] = r.n or 0
            q = (await session.execute(select(func.date(db.WebQuizLog.created_at), func.count(db.WebQuizLog.id))
                                       .where(db.WebQuizLog.created_at >= datetime.combine(start, datetime.min.time()))
                                       .group_by(func.date(db.WebQuizLog.created_at)))).all()
            for d, n in q:
                dd = d if isinstance(d, date) else date.fromisoformat(str(d)[:10])
                if dd in series:
                    series[dd]["quiz_finish"] = max(series[dd]["quiz_finish"], int(n or 0))
            u = (await session.execute(select(db.WebUser.joined_at, func.count(db.WebUser.id)).where(db.WebUser.joined_at >= start)
                                       .group_by(db.WebUser.joined_at))).all()
            for d, n in u:
                if d in series:
                    series[d]["signup"] = int(n or 0)
    except Exception:  # noqa: BLE001
        logger.warning("daily_series", exc_info=True)
    return [{"day": d.strftime("%d.%m"), **v} for d, v in series.items()]


async def devices() -> dict:
    await _ensure_tables()
    try:
        async with db.async_session() as session:
            rows = (await session.execute(select(SiteVisitor.device, func.count()).where(
                SiteVisitor.last_seen >= datetime.utcnow() - timedelta(days=30)).group_by(SiteVisitor.device))).all()
        return {d or "?": int(n) for d, n in rows}
    except Exception:  # noqa: BLE001
        return {}


async def returning_share() -> int:
    """Oxirgi 30 kunda bir martadan ko'p kelganlar ulushi, %."""
    await _ensure_tables()
    try:
        async with db.async_session() as session:
            since = datetime.utcnow() - timedelta(days=30)
            tot = (await session.execute(select(func.count()).select_from(SiteVisitor).where(SiteVisitor.last_seen >= since))).scalar() or 0
            ret = (await session.execute(select(func.count()).select_from(SiteVisitor).where(SiteVisitor.last_seen >= since, SiteVisitor.visits > 1))).scalar() or 0
        return round(100 * ret / tot) if tot else 0
    except Exception:  # noqa: BLE001
        return 0
