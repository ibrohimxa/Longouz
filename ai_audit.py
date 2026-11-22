"""LongoUZ — AI TEKSHIRUV (v242): Gemini butun savollar bankini bo'laklab ko'rib chiqadi.

Nima qiladi:
  * Bank ko'rinishi: har fan bo'yicha nechta savol (takrorlanmas), mavzu va mock borligini ko'rsatadi.
  * AI tekshiruv: har bir takrorlanmas savolni Gemini mustaqil yechib ko'radi va faqat ANIQ muammolarni belgilaydi
    (javob kaliti xato, bir nechta to'g'ri variant, to'g'ri variant yo'q, tushunarsiz savol, jiddiy imlo, izoh javobga zid).
  * Admin har bir topilmani ko'radi: AI taklif qilgan javobni qo'llaydi, savolni yashiradi, tahrirlaydi yoki "to'g'ri ekan" deb yopadi.

Vercel (serverless) uzoq fon vazifasini bajara olmaydi, shuning uchun tekshiruv BO'LAKLAB ishlaydi: admin sahifasi
`/api/ai-audit/step` ni ketma-ket chaqiradi, har chaqiruv bir bo'lak savolni tekshiradi va joyini bazaga yozadi —
sahifa yopilsa yoki AI limiti tugasa, keyin aynan o'sha joydan davom etadi.
Barcha endpointlar admin sessiyasi va `x-requested-with: fetch` bilan himoyalangan.
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel, Field
from sqlalchemy import delete as sa_delete, func, select, update as sa_update

import database as db

logger = logging.getLogger("longouz.ai_audit")

BATCH = 16          # bitta AI so'rovida tekshiriladigan savollar soni
SCAN = 80           # bir o'qishda bazadan olinadigan qatorlar
STATE_KEY = "ai_audit_state"
KINDS = {
    "wrong_key": "Javob kaliti xato",
    "multi_correct": "Bir nechta to'g'ri variant",
    "no_correct": "To'g'ri variant yo'q",
    "unclear": "Savol tushunarsiz / shart yetishmaydi",
    "typo": "Imlo yoki format xatosi",
    "explanation": "Izoh javobga zid",
    "other": "Boshqa",
}

SYSTEM = (
    "Siz O'zbekiston DTM va milliy sertifikat imtihonlari bo'yicha savollar sifat nazoratchisisiz: matematika, fizika, kimyo, "
    "biologiya, tarix, ona tili va adabiyot, ingliz va rus tili bo'yicha tajribali metodist. Sizga JSON ro'yxat beriladi; har bir "
    "elementda: id, subject, topic, type (closed | open | match), q (savol), options (variantlar; indeks 0 dan), key (hozir TO'G'RI deb "
    "belgilangan variant indeksi), expl (izoh), has_figure (savolda chizma bor, siz uni ko'rmaysiz).\n"
    "VAZIFA: har bir savolni O'ZINGIZ mustaqil yeching (hisob-kitobni oxirigacha bajaring, faktni eslang), so'ng belgilangan kalit "
    "bilan solishtiring. FAQAT aniq muammosi bor savollarni qaytaring. Muammo turlari (kind):\n"
    "- wrong_key: belgilangan kalit noto'g'ri va boshqa variant aniq to'g'ri -> correct_index ga to'g'ri variant indeksini yozing;\n"
    "- multi_correct: ikki yoki undan ortiq variant to'g'ri;\n"
    "- no_correct: variantlar orasida to'g'risi yo'q;\n"
    "- unclear: savol tushunarsiz, shart yetishmaydi yoki ikki xil tushuniladi (has_figure=true bo'lsa, chizma yo'qligi muammo EMAS);\n"
    "- typo: ma'noni buzadigan imlo, formula yoki format xatosi (mayda uslubiy kamchilik emas);\n"
    "- explanation: izoh to'g'ri javobga zid yoki xato.\n"
    "QOIDALAR: ishonchingiz komil bo'lmasa, savolni QAYTARMANG (yolg'on signal zararli). type=open da options — qabul qilinadigan "
    "javoblar ro'yxati (kalit ahamiyatsiz): faqat qabul qilinadigan javobning o'zi xato bo'lsa belgilang. type=match da variantlar — "
    "'1-A, 2-C, 3-B' ko'rinishidagi moslik; savol matnidagi juftlarga qarab tekshiring. Maktab dasturi va DTM an'anasidagi qiymatlarni "
    "to'g'ri deb oling (g = 10 m/s^2, Cl = 35,5, Cu = 64, pi = 3,14 va h.k.). Rus va ingliz tilidagi savollarni o'sha til qoidalari "
    "bo'yicha tekshiring. note — o'zbek tilida, 1-2 gap: nima xato va to'g'risi qanday.\n"
    'NATIJA — faqat JSON: {"issues": [{"id": 123, "kind": "wrong_key", "severity": 3, "note": "...", "correct_index": 2, "fix": null}]}. '
    "severity: 3 — o'quvchi noto'g'ri baholanadi (kalit/variant xato), 2 — savol chalg'itadi, 1 — mayda. Muammo bo'lmasa: {\"issues\": []}.\n"
    "TUZATISH (fix): no_correct, multi_correct, unclear, typo, explanation turlarida savol muallifi NIMA DEMOQCHI bo'lganini aniqlang va "
    "TO'LIQ tuzatilgan savolni bering: \"fix\": {\"question\": \"...\", \"options\": [4 ta variant], \"correct_index\": 0-3, "
    "\"explanation\": \"qisqa to'g'ri izoh\"}. Savol mazmuni va mavzusini saqlang, faqat xatoni tuzating; aynan bitta variant to'g'ri "
    "bo'lsin. type=open yoki match bo'lsa yoki aniq tuzata olmasangiz — \"fix\": null."
)


# --------------------------------------------------------------------------------------
# Holat (SiteSetting ichida JSON)
# --------------------------------------------------------------------------------------

async def _load_state() -> dict:
    try:
        st = json.loads(await db.get_setting(STATE_KEY, "") or "{}")
    except ValueError:
        st = {}
    return st if isinstance(st, dict) else {}


async def _save_state(st: dict) -> None:
    st["updated_at"] = datetime.utcnow().isoformat(timespec="seconds")
    await db.set_setting(STATE_KEY, json.dumps(st, ensure_ascii=False))


async def _total_unique(subject: str = "") -> int:
    async with db.async_session() as session:
        q = select(db.Question.subject, db.Question.question).where(db.Question.is_active == True)  # noqa: E712
        if subject:
            q = q.where(db.Question.subject == subject)
        sub = q.distinct().subquery()
        return int((await session.execute(select(func.count()).select_from(sub))).scalar() or 0)


# --------------------------------------------------------------------------------------
# Bank ko'rinishi
# --------------------------------------------------------------------------------------

async def overview() -> dict:
    """Fanlar kesimida: qatorlar, takrorlanmas savollar, mavzular, mocklar + ochiq AI topilmalari."""
    async with db.async_session() as session:
        Q = db.Question
        rows = (await session.execute(
            select(Q.subject, Q.mode, func.count(Q.id), func.count(func.distinct(Q.topic)))
            .where(Q.is_active == True).group_by(Q.subject, Q.mode))).all()  # noqa: E712
        uniq_sub = select(Q.subject, Q.question).where(Q.is_active == True).distinct().subquery()  # noqa: E712
        uniq = dict((await session.execute(select(uniq_sub.c.subject, func.count()).group_by(uniq_sub.c.subject))).all())
        topic_sub = select(Q.subject, Q.topic).where(Q.is_active == True).distinct().subquery()  # noqa: E712
        topics = dict((await session.execute(select(topic_sub.c.subject, func.count()).group_by(topic_sub.c.subject))).all())
        hidden = int((await session.execute(select(func.count(Q.id)).where(Q.is_active == False))).scalar() or 0)  # noqa: E712
        mocks = dict((await session.execute(
            select(db.MockTest.subject, func.count(db.MockTest.id)).where(db.MockTest.is_active == True)  # noqa: E712
            .group_by(db.MockTest.subject))).all())
        F = db.AiAuditFinding
        open_by = dict((await session.execute(
            select(F.subject, func.count(F.id)).where(F.status == "open").group_by(F.subject))).all())
        sev3 = int((await session.execute(select(func.count(F.id)).where(F.status == "open", F.severity >= 3))).scalar() or 0)
        fixed = int((await session.execute(select(func.count(F.id)).where(F.status.in_(("fixed", "hidden"))))).scalar() or 0)
    subjects: dict[str, dict] = {}
    for subject, mode, n, _t in rows:
        d = subjects.setdefault(subject, {"subject": subject, "name": db.SUBJECT_NAMES.get(subject, subject), "rows": 0, "modes": {}})
        d["rows"] += n
        d["modes"][mode] = n
    out = []
    for subject, d in subjects.items():
        d.update(unique=int(uniq.get(subject, 0)), topics=int(topics.get(subject, 0)), mocks=int(mocks.get(subject, 0)),
                 open=int(open_by.get(subject, 0)))
        out.append(d)
    out.sort(key=lambda x: -x["unique"])
    return {
        "subjects": out,
        "total_rows": sum(d["rows"] for d in out), "total_unique": sum(d["unique"] for d in out),
        "total_topics": sum(d["topics"] for d in out), "total_mocks": sum(d["mocks"] for d in out),
        "hidden": hidden, "open": sum(d["open"] for d in out), "open_severe": sev3, "fixed": fixed,
    }


# --------------------------------------------------------------------------------------
# Bitta qadam
# --------------------------------------------------------------------------------------

def _payload(row) -> dict:
    try:
        opts = json.loads(row.options_json or "[]")
    except ValueError:
        opts = []
    return {
        "id": row.id, "subject": db.SUBJECT_NAMES.get(row.subject, row.subject), "topic": row.topic,
        "type": row.qtype or "closed", "q": (row.question or "")[:1500], "options": [str(o)[:300] for o in opts][:8],
        "key": row.correct_index, "expl": (row.explanation or "")[:400], "has_figure": bool((row.figure_json or "").strip()),
    }


async def _next_batch(cursor: int, subject: str) -> tuple[list, int, bool]:
    """Keyingi BATCH ta TAKRORLANMAS savol (bir xil matn DTM va sertifikat rejimida bo'lsa — bir marta tekshiriladi).
    Qaytaradi: (qatorlar, yangi kursor, tugadimi)."""
    Q = db.Question
    batch: list = []
    finished = False
    async with db.async_session() as session:
        for _ in range(6):
            q = select(Q).where(Q.id > cursor, Q.is_active == True)  # noqa: E712
            if subject:
                q = q.where(Q.subject == subject)
            rows = (await session.execute(q.order_by(Q.id).limit(SCAN))).scalars().all()
            if not rows:
                finished = True
                break
            texts = list({r.question for r in rows})
            first = {(s, t): i for s, t, i in (await session.execute(
                select(Q.subject, Q.question, func.min(Q.id)).where(Q.question.in_(texts), Q.is_active == True)  # noqa: E712
                .group_by(Q.subject, Q.question))).all()}
            for r in rows:
                cursor = r.id
                if first.get((r.subject, r.question), r.id) == r.id:
                    batch.append(r)
                    if len(batch) >= BATCH:
                        break
            if len(batch) >= BATCH:
                break
            if len(rows) < SCAN:
                finished = True
                break
    return batch, cursor, finished


def _clean_issues(data, batch: list) -> list[dict]:
    items = data.get("issues") if isinstance(data, dict) else data
    if not isinstance(items, list):
        return []
    by_id = {r.id: r for r in batch}
    out = []
    for it in items:
        if not isinstance(it, dict):
            continue
        try:
            qid = int(it.get("id"))
        except (TypeError, ValueError):
            continue
        row = by_id.get(qid)
        if row is None:
            continue
        kind = str(it.get("kind") or "other").strip().lower()
        if kind not in KINDS:
            kind = "other"
        try:
            n_opts = len(json.loads(row.options_json or "[]"))
        except ValueError:
            n_opts = 0
        idx = it.get("correct_index")
        idx = idx if isinstance(idx, int) and not isinstance(idx, bool) and 0 <= idx < n_opts else -1
        if kind == "wrong_key":
            if (row.qtype or "closed") == "open" or idx < 0 or idx == row.correct_index:
                continue  # taklif yo'q yoki hozirgi kalit bilan bir xil — signal emas
        else:
            idx = -1
        note = " ".join(str(it.get("note") or "").split())[:680]
        if not note:
            continue
        try:
            sev = max(1, min(3, int(it.get("severity") or 2)))
        except (TypeError, ValueError):
            sev = 2
        if kind in ("wrong_key", "no_correct", "multi_correct"):
            sev = 3
        fix = it.get("fix") if isinstance(it.get("fix"), dict) else None
        if fix is not None:
            try:
                fq = " ".join(str(fix.get("question") or "").split())[:1900]
                fo = [" ".join(str(o).split())[:600] for o in (fix.get("options") or [])]
                fci = int(fix.get("correct_index"))
                fe = " ".join(str(fix.get("explanation") or "").split())[:1500]
                ok = ((row.qtype or "closed") == "closed" and fq and len(fo) == 4 and all(fo) and len(set(o.lower() for o in fo)) == 4
                      and 0 <= fci < 4)
                fix = {"question": fq, "options": fo, "correct_index": fci, "explanation": fe} if ok else None
            except (TypeError, ValueError):
                fix = None
        out.append({"row": row, "kind": kind, "severity": sev, "note": note, "idx": idx, "fix": fix})
    return out


async def _auto_fix(session, row, it: dict) -> str:
    """v246: aniq xatoni AI o'zi tuzatadi (barcha rejimdagi nusxalarida). Natija: 'fixed' yoki 'open'."""
    targets = await _twins(session, row)
    if it["kind"] == "wrong_key" and it["idx"] >= 0:
        try:
            want = json.loads(row.options_json or "[]")[it["idx"]]
        except (ValueError, IndexError):
            return "open"
        n = 0
        for t in targets:
            try:
                opts = json.loads(t.options_json or "[]")
            except ValueError:
                continue
            if want in opts:
                t.correct_index = opts.index(want)
                n += 1
        if n:
            for t in targets:
                if t.source_file == "longouz-bank":
                    t.source_file = "longouz-fixed"
            return "fixed"
        return "open"
    fix = it.get("fix")
    if not fix:
        return "open"
    # matni o'zgargan savol boshqa savolning nusxasiga aylanib qolmasin
    dup = (await session.execute(select(db.Question.id).where(db.Question.question == fix["question"], db.Question.subject == row.subject,
                                                              db.Question.id.notin_([t.id for t in targets])).limit(1))).scalar()
    if dup:
        return "open"
    for t in targets:
        t.question = fix["question"]
        t.options_json = json.dumps(fix["options"], ensure_ascii=False)
        t.correct_index = fix["correct_index"]
        if fix.get("explanation"):
            t.explanation = fix["explanation"]
        t.source_file = "longouz-fixed" if t.source_file in ("longouz-bank", "") else t.source_file
    return "fixed"


async def step(subject: str = "", restart: bool = False) -> dict:
    import studio
    import ai_gemini
    st = await _load_state()
    if restart or st.get("subject", "") != subject or not st:
        st = {"subject": subject, "cursor": 0, "checked": 0, "flagged": 0, "done": False,
              "total": await _total_unique(subject), "started_at": datetime.utcnow().isoformat(timespec="seconds")}
    if st.get("done"):
        return {"ok": True, **st}
    if not ai_gemini.is_gemini_configured():
        return {"ok": False, "fatal": True, "detail": "Gemini kaliti sozlanmagan. «Kalitlar» bo'limida GEMINI_API_KEY ni kiriting.", **st}

    batch, new_cursor, finished = await _next_batch(int(st.get("cursor", 0)), subject)
    if not batch:
        st.update(cursor=new_cursor, done=True)
        await _save_state(st)
        return {"ok": True, **st}

    started = time.monotonic()
    user = json.dumps([_payload(r) for r in batch], ensure_ascii=False)
    data = await studio.ai_json(SYSTEM, user, max_tokens=3500, timeout=48)
    took = round(time.monotonic() - started, 1)
    if data is None:
        import ai_diagnostics
        hint = ai_diagnostics.failure_hint() or "Gemini hozir band yoki bepul limit vaqtincha tugagan."
        return {"ok": False, "retry_after": 25, "detail": hint, "took": took, **st}

    issues = _clean_issues(data, batch)
    ids = [r.id for r in batch]
    async with db.async_session() as session:
        # qayta tekshirilgan savolning eski OCHIQ topilmasi yangisi bilan almashtiriladi
        await session.execute(sa_delete(db.AiAuditFinding).where(db.AiAuditFinding.question_id.in_(ids),
                                                                 db.AiAuditFinding.status == "open"))
        auto = (await db.get_setting("ai_audit_autofix", "1")) != "0"
        fixed_now = 0
        for it in issues:
            r = it["row"]
            status = "open"
            if auto:
                status = await _auto_fix(session, r, it)
                if status == "fixed":
                    fixed_now += 1
            session.add(db.AiAuditFinding(question_id=r.id, subject=r.subject, mode=r.mode, topic=r.topic, kind=it["kind"],
                                          severity=it["severity"], suggested_index=it["idx"], status=status,
                                          note=(it["note"] + (" — LongoAI o'zi tuzatdi." if status == "fixed" else ""))[:700]))
        await session.commit()
        st["autofixed"] = int(st.get("autofixed", 0)) + fixed_now
    st.update(cursor=new_cursor, checked=int(st.get("checked", 0)) + len(batch),
              flagged=int(st.get("flagged", 0)) + len(issues), done=bool(finished))
    await _save_state(st)
    return {"ok": True, "batch": len(batch), "found": len(issues), "took": took, **st}


# --------------------------------------------------------------------------------------
# Topilmalar
# --------------------------------------------------------------------------------------

async def list_findings(status: str = "open", subject: str = "", kind: str = "", page: int = 1, per: int = 25) -> dict:
    F, Q = db.AiAuditFinding, db.Question
    async with db.async_session() as session:
        cond = [F.status == status] if status in ("open", "fixed", "hidden", "dismissed") else []
        if subject:
            cond.append(F.subject == subject)
        if kind in KINDS:
            cond.append(F.kind == kind)
        total = int((await session.execute(select(func.count(F.id)).where(*cond))).scalar() or 0)
        rows = (await session.execute(
            select(F, Q).join(Q, Q.id == F.question_id, isouter=True).where(*cond)
            .order_by(F.severity.desc(), F.id.desc()).offset(max(0, page - 1) * per).limit(per))).all()
    items = []
    for f, q in rows:
        try:
            opts = json.loads(q.options_json or "[]") if q is not None else []
        except ValueError:
            opts = []
        items.append({
            "id": f.id, "question_id": f.question_id, "subject": db.SUBJECT_NAMES.get(f.subject, f.subject), "mode": f.mode,
            "topic": f.topic, "kind": f.kind, "kind_label": KINDS.get(f.kind, f.kind), "severity": f.severity, "note": f.note,
            "suggested_index": f.suggested_index, "status": f.status,
            "question": (q.question if q is not None else "(savol o'chirilgan)"), "options": opts,
            "correct_index": (q.correct_index if q is not None else -1), "qtype": (q.qtype if q is not None else "closed"),
            "explanation": (q.explanation if q is not None else ""), "exists": q is not None,
            "has_figure": bool(q is not None and (q.figure_json or "").strip()),
        })
    return {"items": items, "total": total, "page": page, "per": per}


async def _twins(session, q) -> list:
    """Shu savolning barcha nusxalari (DTM va sertifikat rejimida bir xil matn)."""
    return (await session.execute(select(db.Question).where(db.Question.subject == q.subject,
                                                            db.Question.question == q.question))).scalars().all()


async def resolve(finding_id: int, action: str, admin: str) -> dict:
    """action: apply (AI taklif qilgan kalitni qo'llash) | hide (savolni yashirish) | dismiss (to'g'ri ekan)."""
    async with db.async_session() as session:
        f = await session.get(db.AiAuditFinding, finding_id)
        if f is None:
            raise HTTPException(status_code=404, detail="Topilma topilmadi.")
        q = await session.get(db.Question, f.question_id)
        changed = 0
        if action == "dismiss" or q is None:
            f.status = "dismissed"
        elif action == "apply":
            if f.suggested_index < 0:
                raise HTTPException(status_code=422, detail="Bu topilmada AI aniq javob taklif qilmagan — savolni qo'lda tahrirlang.")
            want = None
            try:
                want = json.loads(q.options_json or "[]")[f.suggested_index]
            except (ValueError, IndexError):
                raise HTTPException(status_code=422, detail="Taklif qilingan variant topilmadi.")
            for t in await _twins(session, q):
                try:
                    opts = json.loads(t.options_json or "[]")
                except ValueError:
                    continue
                if want in opts:  # variantlar har rejimda bir xil tartibda bo'lmasligi mumkin — matn bo'yicha topamiz
                    t.correct_index = opts.index(want)
                    if t.source_file == "longouz-bank":
                        t.source_file = "longouz-fixed"  # keyingi baza yangilanishida tuzatish ustidan yozilmasin
                    changed += 1
            f.status = "fixed"
        elif action == "hide":
            for t in await _twins(session, q):
                t.is_active = False
                if t.source_file == "longouz-bank":
                    t.source_file = "longouz-fixed"
                changed += 1
            f.status = "hidden"
        else:
            raise HTTPException(status_code=422, detail="Noma'lum amal.")
        qid = f.question_id
        await session.commit()
    await db.log_admin_action(admin, f"ai_audit_{action}", f"topilma #{finding_id}, savol #{qid}, {changed} ta nusxa")
    return {"ok": True, "status": action, "changed": changed}


# --------------------------------------------------------------------------------------
# Yo'llar
# --------------------------------------------------------------------------------------

class StepBody(BaseModel):
    subject: str = Field("", max_length=30)
    restart: bool = False


class ResolveBody(BaseModel):
    action: str = Field(..., max_length=12)


class BulkBody(BaseModel):
    subject: str = Field("", max_length=30)
    max_severity: int = Field(1, ge=1, le=3)


def register(app, prefix: str, require_admin, current_admin_username, templates) -> None:
    def guard(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")

    @app.get(f"{prefix}/ai-audit", response_class=HTMLResponse)
    async def ai_audit_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        return templates.TemplateResponse(request, "admin_ai_audit.html", {
            "active_tab": "ai_audit", "subjects": db.SUBJECTS, "kinds": KINDS, "batch": BATCH,
        })

    @app.get(f"{prefix}/api/ai-audit/overview")
    async def ai_audit_overview(request: Request):
        guard(request)
        import ai_gemini
        st = await _load_state()
        return JSONResponse({"ok": True, "overview": await overview(), "state": st, "ai_ready": ai_gemini.is_gemini_configured()})

    @app.get(f"{prefix}/api/ai-audit/structure")
    async def ai_audit_structure(request: Request):
        """Tuzilma tekshiruvi (AI'siz, bir zumda): buzilgan variantlar, takrorlar, diapazondan tashqari kalit."""
        guard(request)
        rep = await db.admin_audit_questions(limit=1)
        return JSONResponse({"ok": True, "checked": rep["checked"], "total_issues": rep["total_issues"], "kinds": rep["kinds"]})

    @app.post(f"{prefix}/api/ai-audit/step")
    async def ai_audit_step(request: Request, body: StepBody):
        guard(request)
        subject = body.subject if body.subject in db.SUBJECT_CODES else ""
        try:
            return JSONResponse(await step(subject, body.restart))
        except HTTPException:
            raise
        except Exception:  # noqa: BLE001
            logger.exception("AI tekshiruv qadami xatosi")
            return JSONResponse({"ok": False, "retry_after": 20, "detail": "Server xatosi — qayta urinilmoqda."})

    @app.get(f"{prefix}/api/ai-audit/findings")
    async def ai_audit_findings(request: Request, status: str = "open", subject: str = "", kind: str = "", page: int = 1):
        guard(request)
        return JSONResponse({"ok": True, **await list_findings(status, subject if subject in db.SUBJECT_CODES else "", kind, max(1, page))})

    @app.post(f"{prefix}/api/ai-audit/finding/{{finding_id}}")
    async def ai_audit_resolve(request: Request, finding_id: int, body: ResolveBody):
        guard(request)
        return JSONResponse(await resolve(finding_id, body.action, current_admin_username(request)))

    @app.post(f"{prefix}/api/ai-audit/dismiss-minor")
    async def ai_audit_dismiss_minor(request: Request, body: BulkBody):
        """Mayda (severity <= N) ochiq topilmalarni bir bosishda yopadi."""
        guard(request)
        F = db.AiAuditFinding
        async with db.async_session() as session:
            cond = [F.status == "open", F.severity <= body.max_severity]
            if body.subject in db.SUBJECT_CODES:
                cond.append(F.subject == body.subject)
            res = await session.execute(sa_update(F).where(*cond).values(status="dismissed"))
            await session.commit()
        await db.log_admin_action(current_admin_username(request), "ai_audit_dismiss_minor", f"{res.rowcount or 0} ta")
        return JSONResponse({"ok": True, "count": res.rowcount or 0})
