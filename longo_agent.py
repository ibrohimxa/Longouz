"""LongoUZ — «LongoAI» avtonom yordamchisi (v243, faqat Gemini).

1) SHIKOYATLAR: o'quvchi savolga shikoyat qilsa — LongoAI savolni o'zi yechadi, kerak bo'lsa Google'dan faktni tekshiradi;
   xato aniq bo'lsa savolni O'ZI tuzatadi (natijalar qayta baholanadi) va o'quvchiga tushuntirish yozadi;
   savol to'g'ri bo'lsa — nega to'g'ri ekanini tushuntirib javob beradi; ishonchi yetmasa — adminga qoldiradi.
2) YORDAM xabarlari: o'quvchi «Yordam» bo'limiga yozsa — LongoAI odamdek, iliq va aniq javob beradi (hisobini, testlarini,
   savollar bazasini ko'rib); to'lov/hisob kabi admin qarori kerak bo'lsa — javob beradi va xabarni adminga belgilab qo'yadi.
3) ADMIN YORDAMCHI: admin panelda — butun savollar bazasi, shikoyatlar, xabarlar, statistika, internet qidiruv va xotira
   vositalari bilan ishlaydi; o'zgartirishlarni taklif qiladi (admin «Qo'llash» bosadi).

Ishlar navbati (agent_jobs jadvali) — Vercel fon vazifalarini muzlatgani uchun ish keyingi so'rov ichida bajariladi:
o'quvchi sahifasi /api/agent/kick ni chaqiradi, admin panel esa har 30 soniyada qolganini bajaradi.
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timedelta

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy import DateTime, Integer, String, Text, desc, func, or_, select
from sqlalchemy.orm import Mapped, mapped_column

import database as db
import gemini_agent as ga
from gemini_agent import Tool

logger = logging.getLogger("longouz.longoai")

AI_NAME = "LongoAI"
FACT_SUBJECTS = {"history", "geography", "biology", "native", "english", "russian", "chemistry", "law", "literature"}


class AgentJob(db.Base):
    __tablename__ = "agent_jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kind: Mapped[str] = mapped_column(String(20), index=True)          # report | support
    ref_id: Mapped[int] = mapped_column(Integer, index=True)
    user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
    status: Mapped[str] = mapped_column(String(16), default="pending", index=True)   # pending|running|done|admin|error
    attempts: Mapped[int] = mapped_column(Integer, default=0)
    result: Mapped[str] = mapped_column(Text, default="")
    steps: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    done_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)


_ready = False


async def _ensure() -> None:
    global _ready
    if _ready:
        return
    async with db.engine.begin() as conn:
        await conn.run_sync(lambda c: db.Base.metadata.create_all(c, tables=[AgentJob.__table__]))
    _ready = True


async def enqueue(kind: str, ref_id: int, user_id: int | None) -> int:
    await _ensure()
    async with db.async_session() as s:
        prev = (await s.execute(select(AgentJob).where(AgentJob.kind == kind, AgentJob.ref_id == ref_id,
                                                       AgentJob.status.in_(("pending", "running"))))).scalar_one_or_none()
        if prev is not None:
            return prev.id
        job = AgentJob(kind=kind, ref_id=ref_id, user_id=user_id)
        s.add(job)
        await s.commit()
        await s.refresh(job)
        return job.id


async def _claim(job_id: int) -> AgentJob | None:
    """Ishni band qilish (ikki instans bir ishni qilmasin). 3 daqiqadan oshib «running» qolgan ish qayta olinadi."""
    async with db.async_session() as s:
        job = await s.get(AgentJob, job_id)
        if job is None:
            return None
        stale = job.status == "running" and job.done_at is not None and datetime.utcnow() - job.done_at > timedelta(minutes=3)
        if job.status != "pending" and not stale:
            return None
        if job.attempts >= 3:
            job.status = "error"
            await s.commit()
            return None
        job.status, job.attempts, job.done_at = "running", (job.attempts or 0) + 1, datetime.utcnow()
        await s.commit()
        return job


async def _finish(job_id: int, status: str, result: str, steps: list | None = None) -> None:
    async with db.async_session() as s:
        job = await s.get(AgentJob, job_id)
        if job is not None:
            job.status, job.result, job.done_at = status, result[:4000], datetime.utcnow()
            if steps is not None:
                job.steps = json.dumps(steps, ensure_ascii=False)[:8000]
            await s.commit()


async def _memory_log(text: str) -> None:
    try:
        import insights
        await insights.add_memory_log(text, who=AI_NAME)
    except Exception:  # noqa: BLE001
        logger.debug("xotira jurnali", exc_info=True)


# =========================================================================== umumiy vositalar
async def _t_find_questions(a: dict) -> dict:
    Q = db.Question
    text = str(a.get("text") or "").strip()[:120]
    limit = max(1, min(int(a.get("limit") or 12), 25))
    async with db.async_session() as s:
        stmt = select(Q)
        if a.get("subject"):
            stmt = stmt.where(Q.subject == str(a["subject"]))
        if a.get("mode"):
            stmt = stmt.where(Q.mode == str(a["mode"]))
        if a.get("topic"):
            stmt = stmt.where(Q.topic.ilike(f"%{str(a['topic'])[:80]}%"))
        if text:
            words = [w for w in text.split() if len(w) > 2][:4] or [text]
            stmt = stmt.where(*[or_(Q.question.ilike(f"%{w}%"), Q.options_json.ilike(f"%{w}%")) for w in words])
        if a.get("only_inactive"):
            stmt = stmt.where(Q.is_active == False)  # noqa: E712
        stmt = stmt.order_by(Q.id).offset(max(0, int(a.get("offset") or 0))).limit(limit)
        rows = (await s.execute(stmt)).scalars().all()
    return {"count": len(rows), "items": [{"id": q.id, "subject": q.subject, "mode": q.mode, "topic": q.topic, "type": q.qtype,
                                            "active": q.is_active, "question": (q.question or "")[:260]} for q in rows]}


async def _t_get_question(a: dict) -> dict:
    import studio
    return await studio._tool_get(int(a.get("id")))


async def _t_web_search(a: dict) -> dict:
    return await ga.web_search(str(a.get("query") or ""), str(a.get("context") or ""))


FIND_TOOL = Tool("find_questions", "Savollar bazasidan qidirish: matn (so'zlar), fan kodi, rejim, mavzu bo'yicha. Eng ko'pi 25 ta.",
                 {"type": "object", "properties": {
                     "text": {"type": "string", "description": "savol matnidagi so'zlar"},
                     "subject": {"type": "string", "description": "math, physics, chemistry, biology, history, geography, native, english, russian ..."},
                     "mode": {"type": "string", "description": "dtm, certificate, ielts ..."},
                     "topic": {"type": "string"}, "offset": {"type": "integer"}, "limit": {"type": "integer"},
                     "only_inactive": {"type": "boolean"}}},
                 _t_find_questions, "Savollar bazasidan qidirilmoqda")
GET_TOOL = Tool("get_question", "Bitta savolning to'liq ma'lumoti: variantlar, to'g'ri javob, izoh, mavzu, faolligi.",
                {"type": "object", "properties": {"id": {"type": "integer"}}, "required": ["id"]}, _t_get_question, "Savol ochilmoqda")
WEB_TOOL = Tool("web_search", "Internetdan (Google) qidirish — sana, fakt, ta'rif, qoida yoki yangilikni tekshirish uchun. Natija: qisqa xulosa va manbalar.",
                {"type": "object", "properties": {"query": {"type": "string"}, "context": {"type": "string"}}, "required": ["query"]},
                _t_web_search, "Google'da qidirilmoqda")


# =========================================================================== 1) SHIKOYATLAR
async def handle_report(report_id: int) -> tuple[str, str, list]:
    import reports
    cfg = await reports.get_cfg()
    async with db.async_session() as s:
        rep = await s.get(db.QuestionReport, report_id)
        if rep is None:
            return "done", "shikoyat topilmadi", []
        if rep.status not in ("new", "analyzed"):
            return "done", "allaqachon ko'rib chiqilgan", []
        subject, question, uid = rep.subject, rep.question_text, rep.user_id
        try:
            opts = json.loads(rep.options_json or "[]")
        except ValueError:
            opts = []
    steps: list = []
    facts = ""
    if cfg.get("web_search", True) and (subject in FACT_SUBJECTS or any(w in (question or "").lower() for w in ("yil", "asr", "kim ", "qachon", "qayerda"))):
        t0 = time.monotonic()
        q = question[:300] + ((" Variantlar: " + "; ".join(str(o) for o in opts[:4])) if opts else "")
        found = await ga.web_search(q, f"{db.SUBJECT_NAMES.get(subject, subject)} fanidan test savoli to'g'ri javobini aniqlash")
        if found.get("text"):
            facts = found["text"] + ("\nManbalar: " + ", ".join(x["url"] for x in found.get("sources", [])[:4]) if found.get("sources") else "")
        steps.append({"tool": "web_search", "label": "Google'da tekshirildi", "ok": bool(found.get("text")), "ms": int((time.monotonic() - t0) * 1000)})
    res = await reports.analyze_report(report_id, apply_if_confident=bool(cfg.get("auto_fix")), admin=AI_NAME, facts=facts)
    steps.append({"tool": "analyze", "label": "Savol yechib tekshirildi", "ok": True})
    verdict, conf, note = res.get("verdict"), int(res.get("confidence") or 0), str(res.get("note") or "")
    min_conf = int(cfg.get("min_conf", 90))
    reporters = await _reporters(report_id)
    short_note = note.replace("\n\n", " ").strip()[:600]
    if res.get("applied"):
        for u in reporters:
            await db.create_notification(u, "report", title=f"{AI_NAME}: savol tuzatildi",
                                         body=f"Shikoyatingizni tekshirdim — haqiqatan xato bor ekan va tuzatdim. {short_note} Rahmat, siz platformani yaxshilayapsiz!")
        await _memory_log(f"Shikoyat #{report_id}: savol tuzatildi (ishonch {conf}%). {short_note[:300]}")
        return "done", f"Tuzatildi ({conf}%): {short_note}", steps
    if verdict == "ok" and conf >= min_conf and cfg.get("auto_reply", True):
        await reports.dismiss(report_id, f"{AI_NAME}: savol to'g'ri ({conf}%). {short_note}"[:500], AI_NAME)
        for u in reporters:
            await db.create_notification(u, "report", title=f"{AI_NAME}: shikoyatingiz tekshirildi",
                                         body=f"Savolni qayta yechib ko'rdim — bazadagi javob to'g'ri ekan. {short_note} Yana savol bo'lsa, bemalol yozing!")
        await _memory_log(f"Shikoyat #{report_id}: savol to'g'ri deb topildi ({conf}%).")
        return "done", f"Savol to'g'ri ({conf}%): {short_note}", steps
    for u in reporters:
        await db.create_notification(u, "report", title="Shikoyatingiz qabul qilindi",
                                     body="Rahmat! Savolni tekshiryapmiz — mutaxassis ko'rib chiqqach natijasini shu yerda ko'rasiz.")
    return "admin", f"Adminga qoldirildi: {verdict} ({conf}%). {short_note}", steps


async def _reporters(report_id: int) -> set[int]:
    async with db.async_session() as s:
        rep = await s.get(db.QuestionReport, report_id)
        if rep is None:
            return set()
        if rep.question_id is None:
            return {rep.user_id}
        rows = (await s.execute(select(db.QuestionReport.user_id).where(
            db.QuestionReport.question_id == rep.question_id,
            db.QuestionReport.created_at >= datetime.utcnow() - timedelta(days=30)))).scalars().all()
        return set(rows) | {rep.user_id}


# =========================================================================== 2) YORDAM XABARLARI
SUPPORT_SYSTEM = (
    f"Siz {AI_NAME} — LongoUZ (O'zbekistondagi DTM, milliy sertifikat, IELTS/CEFR tayyorlov platformasi) yordam xizmatining xodimisiz. "
    "Odamdek, iliq va samimiy, lekin qisqa va aniq yozasiz: salom bilan boshlang, o'quvchini ismi bilan chaqiring (bo'lsa), "
    "muammoni hal qiladigan aniq qadamlarni ayting. O'zbek tilida (lotin) yozing; o'quvchi ruscha yozsa — ruscha. Emoji ishlatmang. "
    "«Men sun'iy intellektman», «men o'zbek tilida gapiraman» kabi gaplarni AYTMANG.\n"
    "VOSITALAR: my_account (o'quvchining tarifi, testlari, natijalari), find_questions / get_question (savollar bazasi), "
    "my_reports (shikoyatlari holati), web_search (internetdan fakt tekshirish), site_info (sayt bo'limlari va qoidalar). "
    "Javob berishdan oldin kerakli vositani chaqiring — taxmin qilmang.\n"
    "QOIDALAR: pul qaytarish, tarifni yoqish, hisobni o'chirish, parolni almashtirishni O'ZINGIZ va'da qilmang — buni admin hal qiladi "
    "(bunday holda needs_admin=true). Agar savol test savolidagi xato haqida bo'lsa — savolni bazadan topib o'zingiz yeching va natijani ayting "
    "(xato bo'lsa needs_admin=true). Bilmasangiz — halol ayting va adminga uzating.\n"
    'YAKUNIY JAVOB (FAQAT JSON): {"reply": "o\'quvchiga javob matni (3-8 gap)", "needs_admin": true|false, "summary": "admin uchun bir gapda xulosa"}'
)

SITE_INFO = (
    "LongoUZ bo'limlari: /dashboard — shaxsiy kabinet (natijalar, maqsad, statistika); /tests — fan bo'yicha testlar, mavzular, mock (to'liq imtihon) "
    "variantlari, DTM blok-test (/block-test); /tutor — AI repetitor (ovozli ham), faqat Pro va Ultra tarifda; /analytics — natijalar tahlili; "
    "/profile — ism, fan, maqsad, parol, sertifikatlar; /plans — Bepul, Pro (25 000 so'm/oy, yillik 2% chegirma — 294 000 so'm/yil), Ultra (40 000 so'm/oy, yillik 5% chegirma — 456 000 so'm/yil); /support — adminga xabar; "
    "/guide — yo'riqnoma; /verify — sertifikatni QR/ID bilan tekshirish. Testlar va mavzular bepul. "
    "TO'LOV: tarif oynasida karta raqami va amal muddati kiritilsa tarif darhol ochiladi. "
    "Test paytida savol xato bo'lsa — savol yonidagi «Shikoyat» tugmasi; LongoAI uni tekshirib javob beradi. "
    "Google bilan kirish mavjud. Parolni unutgan bo'lsa — /support orqali email bilan yozsin, admin yordam beradi. "
    "Natija qayta hisoblansa (savol tuzatilganda) ball faqat oshadi, kamaymaydi."
)


async def handle_support(msg_id: int) -> tuple[str, str, list]:
    async with db.async_session() as s:
        m = await s.get(db.SupportMessage, msg_id)
        if m is None:
            return "done", "xabar topilmadi", []
        if m.admin_reply:
            return "done", "allaqachon javob berilgan", []
        user = await s.get(db.WebUser, m.user_id)
        subj, body, uid = m.subject, m.body, m.user_id
    if user is None:
        return "done", "foydalanuvchi topilmadi", []

    async def my_account(_a: dict) -> dict:
        stats = await db.get_user_stats(uid)
        hist = (await db.get_user_quiz_history(uid))[:6]
        return {"ism": user.first_name, "email": user.email, "tarif": user.plan, "fan": db.SUBJECT_NAMES.get(user.subject or "", user.subject),
                "ro'yxatdan_o'tgan": str(user.joined_at), "streak": user.streak_days,
                "statistika": {k: v for k, v in (stats or {}).items() if isinstance(v, (int, float, str))},
                "oxirgi_testlar": [{"id": h.id, "fan": h.subject, "mavzu": h.topic, "natija": f"{h.correct_count}/{h.total_count}",
                                    "baho": h.score_label, "sana": h.created_at.strftime("%Y-%m-%d %H:%M") if h.created_at else ""} for h in hist]}

    async def my_reports(_a: dict) -> dict:
        async with db.async_session() as s2:
            rows = (await s2.execute(select(db.QuestionReport).where(db.QuestionReport.user_id == uid)
                                     .order_by(desc(db.QuestionReport.id)).limit(8))).scalars().all()
        return {"items": [{"id": r.id, "savol": (r.question_text or "")[:160], "holat": r.status, "ai_xulosa": (r.ai_note or "")[:300]} for r in rows]}

    async def site_info(_a: dict) -> dict:
        return {"info": SITE_INFO}

    tools = [
        Tool("my_account", "Shu o'quvchining hisobi: tarif, fan, statistika, oxirgi testlari.", {"type": "object", "properties": {}}, my_account, "Hisob ko'rilmoqda"),
        Tool("my_reports", "Shu o'quvchining savollarga yuborgan shikoyatlari va ularning holati.", {"type": "object", "properties": {}}, my_reports, "Shikoyatlar ko'rilmoqda"),
        Tool("site_info", "LongoUZ sayt bo'limlari, tariflar, to'lov va qoidalar haqida ma'lumot.", {"type": "object", "properties": {}}, site_info, "Sayt ma'lumoti"),
        FIND_TOOL, GET_TOOL, WEB_TOOL,
    ]
    prompt = f"O'quvchi: {user.first_name or ''} (tarif: {user.plan}).\nXabar turi/mavzu: {subj}\nXabar:\n{body}"
    r = await ga.run_agent(SUPPORT_SYSTEM, [{"role": "user", "text": prompt}], tools, deadline=55, max_steps=6, json_final=True)
    data = ga.parse_json(r.text) or ({"reply": r.text, "needs_admin": True, "summary": "JSON emas"} if r.ok else None)
    if not data or not str(data.get("reply") or "").strip():
        return "pending", "Gemini javob bermadi (keyinroq qayta uriniladi)", r.steps
    reply = str(data["reply"]).strip()[:1900]
    await db.admin_reply_support_message(msg_id, reply)
    needs_admin = bool(data.get("needs_admin"))
    if needs_admin:
        async with db.async_session() as s:
            m = await s.get(db.SupportMessage, msg_id)
            if m is not None:
                m.is_read = False   # admin ham ko'rsin
                await s.commit()
    await _memory_log(f"Yordam #{msg_id} ({user.first_name or user.email}): {str(data.get('summary') or '')[:200]}"
                      + (" — ADMIN KERAK" if needs_admin else ""))
    return ("admin" if needs_admin else "done"), str(data.get("summary") or reply[:200]), r.steps


# =========================================================================== ishlarni bajarish
async def process_job(job_id: int) -> dict:
    job = await _claim(job_id)
    if job is None:
        return {"id": job_id, "skipped": True}
    try:
        if job.kind == "report":
            status, text, steps = await handle_report(job.ref_id)
        elif job.kind == "support":
            status, text, steps = await handle_support(job.ref_id)
        else:
            status, text, steps = "error", "noma'lum ish", []
    except HTTPException as exc:
        status, text, steps = ("pending" if exc.status_code == 502 else "error"), str(exc.detail), []
    except Exception as exc:  # noqa: BLE001
        logger.exception("LongoAI ishi #%s xatosi", job_id)
        status, text, steps = "pending", f"xato: {str(exc)[:200]}", []
    await _finish(job_id, status, text, steps)
    return {"id": job_id, "status": status, "result": text}


async def process_pending(limit: int = 1, user_id: int | None = None, budget: float = 50.0) -> list[dict]:
    await _ensure()
    t0 = time.monotonic()
    async with db.async_session() as s:
        stmt = select(AgentJob.id).where(or_(AgentJob.status == "pending",
                                             (AgentJob.status == "running") & (AgentJob.done_at < datetime.utcnow() - timedelta(minutes=3))))
        if user_id is not None:
            stmt = stmt.where(AgentJob.user_id == user_id)
        ids = (await s.execute(stmt.order_by(AgentJob.id).limit(limit))).scalars().all()
    out = []
    for jid in ids:
        if time.monotonic() - t0 > budget:
            break
        out.append(await process_job(jid))
    return out


async def pending_count() -> int:
    await _ensure()
    async with db.async_session() as s:
        return int((await s.execute(select(func.count()).select_from(AgentJob).where(AgentJob.status == "pending"))).scalar() or 0)


# =========================================================================== 3) ADMIN YORDAMCHI
ADMIN_SYSTEM = (
    f"Siz {AI_NAME} — LongoUZ admin panelidagi kuchli yordamchisiz. O'zbek tilida, odamdek, aniq va qisqa gapirasiz. "
    "Sizda VOSITALAR bor: butun savollar bazasi (find_questions, get_question, bank_stats, topic_report), shikoyatlar (list_reports, get_report), "
    "yordam xabarlari (list_support), sayt statistikasi (site_stats), internet qidiruv (web_search), xotira (remember / recall) va "
    "o'zgartirish TAKLIFLARI (propose_update_question, propose_delete_question, propose_create_questions, propose_support_reply). "
    "Takliflar darhol bajarilmaydi — admin «Qo'llash» tugmasini bosadi.\n"
    "ISH USLUBI: avval vositalar bilan ma'lumot yig'ing, keyin xulosa qiling. Savol to'g'riligini tekshirganda O'ZINGIZ bosqichma-bosqich yeching; "
    "tarix/biologiya/til kabi faktlarni web_search bilan tasdiqlang. Hech qachon uydirmang. Muhim yangi narsa o'rgansangiz (admin qarori, qoida, "
    "takrorlanuvchi muammo) — remember bilan xotiraga yozing. Javobni markdown bilan chiroyli yozing: qisqa sarlavha, ro'yxat, **qalin** muhim joylar; "
    "savol ID'larini #123 ko'rinishida yozing. Taklif bergan bo'lsangiz — nima taklif qilinganini 1-2 gapda ayting."
)


def admin_tools(staged: list) -> list[Tool]:
    import reports
    import studio

    async def bank_stats(_a):
        return {"table": (await studio.bank_overview())["table"]}

    async def topic_report(a):
        return {"topics": (await studio.topic_report(str(a.get("subject")), str(a.get("mode") or "dtm")))[:150]}

    async def list_reports(a):
        data = await reports.list_reports(str(a.get("status") or "open"), str(a.get("subject") or ""), 1, 20)
        return {"total": data["total"], "counts": data["counts"], "items": [
            {k: it[k] for k in ("id", "question_id", "subject", "topic", "category_name", "message", "status", "verdict", "confidence", "same", "created")}
            for it in data["items"]]}

    async def get_report(a):
        data = await reports.list_reports("all", "", 1, 200)
        for it in data["items"]:
            if it["id"] == int(a.get("id")):
                return it
        return {"error": "topilmadi"}

    async def list_support(a):
        items = await db.admin_list_support_messages(limit=min(int(a.get("limit") or 15), 30))
        out = []
        for x in items:
            m = x["msg"]
            if a.get("unanswered_only") and m.admin_reply:
                continue
            out.append({"id": m.id, "kimdan": x["first_name"] or x["email"], "mavzu": m.subject, "matn": m.body[:400],
                        "javob": (m.admin_reply or "")[:300], "o'qilgan": m.is_read, "sana": m.created_at.strftime("%Y-%m-%d %H:%M")})
        return {"items": out}

    async def site_stats(_a):
        import insights
        import traffic
        return {"hozir": await traffic.public_numbers(), "kunlik": await traffic.daily_series(14), "hisoblar": await insights._counts()}

    async def remember(a):
        txt = str(a.get("note") or "").strip()[:1500]
        if not txt:
            return {"ok": False}
        import insights
        m = await insights.get_memory()
        m["notes"] = (m["notes"] + "\n- " + txt).strip()[-20000:]
        await db.set_setting(insights.MEMORY_KEY, json.dumps(m, ensure_ascii=False))
        await db.set_setting("admin_memory", (m["notes"] + "\n\nREJALAR:\n" + m["plans"])[-6000:])
        await _memory_log("Eslab qoldim: " + txt[:300])
        return {"ok": True}

    async def recall(_a):
        import insights
        m = await insights.get_memory()
        return {"eslatmalar": m["notes"][-6000:], "rejalar": m["plans"][-3000:], "oxirgi_ishlar": m["log"][-25:]}

    def proposer(kind):
        async def _p(a):
            act = {"id": f"a{len(staged) + 1}", "type": kind, "payload": a.get("payload") if isinstance(a.get("payload"), dict) else
                   {k: v for k, v in a.items() if k != "reason"}, "reason": str(a.get("reason") or "")[:400]}
            staged.append(act)
            return {"ok": True, "staged": act["id"], "note": "admin tasdig'ini kutmoqda"}
        return _p

    obj = {"type": "object"}
    return [
        FIND_TOOL, GET_TOOL, WEB_TOOL,
        Tool("bank_stats", "Butun baza statistikasi: fan/rejim kesimida savol, mavzu, tarif, ochiq/chizma soni.", {"type": "object", "properties": {}}, bank_stats, "Baza statistikasi"),
        Tool("topic_report", "Bitta fan+rejim bo'yicha har mavzudagi savollar soni.", {"type": "object", "properties": {"subject": {"type": "string"}, "mode": {"type": "string"}}, "required": ["subject"]}, topic_report, "Mavzular hisoboti"),
        Tool("list_reports", "Savollarga shikoyatlar ro'yxati. status: open|new|analyzed|fixed|dismissed|all.", {"type": "object", "properties": {"status": {"type": "string"}, "subject": {"type": "string"}}}, list_reports, "Shikoyatlar ko'rilmoqda"),
        Tool("get_report", "Bitta shikoyatning to'liq ma'lumoti (AI xulosasi, taklif qilingan tuzatish).", {"type": "object", "properties": {"id": {"type": "integer"}}, "required": ["id"]}, get_report, "Shikoyat ochilmoqda"),
        Tool("list_support", "O'quvchilardan kelgan «Yordam» xabarlari.", {"type": "object", "properties": {"limit": {"type": "integer"}, "unanswered_only": {"type": "boolean"}}}, list_support, "Xabarlar ko'rilmoqda"),
        Tool("site_stats", "Sayt statistikasi: tashriflar, odamlar, onlayn, testlar boshlandi/tugadi, ro'yxatdan o'tganlar (14 kun).", {"type": "object", "properties": {}}, site_stats, "Statistika"),
        Tool("remember", "Muhim narsani doimiy xotiraga yozish (admin qarori, qoida, takrorlanuvchi muammo).", {"type": "object", "properties": {"note": {"type": "string"}}, "required": ["note"]}, remember, "Xotiraga yozildi"),
        Tool("recall", "Xotiradagi eslatmalar, rejalar va oxirgi AI ishlari.", {"type": "object", "properties": {}}, recall, "Xotira o'qilmoqda"),
        Tool("propose_update_question", "Savolni tuzatish TAKLIFI. fields: question, options[4], correct_index(0-3), accept[] (ochiq savol), explanation, topic, difficulty(1-3), min_plan(0-2), is_active.",
             {"type": "object", "properties": {"id": {"type": "integer"}, "fields": obj, "reason": {"type": "string"}}, "required": ["id", "fields", "reason"]},
             proposer("update_question"), "Tuzatish taklifi"),
        Tool("propose_delete_question", "Savolni o'chirish TAKLIFI (xato/takror/yaroqsiz).", {"type": "object", "properties": {"id": {"type": "integer"}, "reason": {"type": "string"}}, "required": ["id", "reason"]},
             proposer("delete_question"), "O'chirish taklifi"),
        Tool("propose_create_questions", "Yangi savollar qo'shish TAKLIFI. questions: [{question, qtype(closed|open), options[4], correct_index, accept[], explanation, difficulty, topic}].",
             {"type": "object", "properties": {"subject": {"type": "string"}, "mode": {"type": "string"}, "topic": {"type": "string"},
                                               "questions": {"type": "array", "items": obj}, "reason": {"type": "string"}}, "required": ["subject", "mode", "topic", "questions", "reason"]},
             proposer("create_questions"), "Yangi savollar taklifi"),
        Tool("propose_support_reply", "O'quvchi xabariga javob TAKLIFI.", {"type": "object", "properties": {"id": {"type": "integer"}, "text": {"type": "string"}, "reason": {"type": "string"}}, "required": ["id", "text"]},
             proposer("support_reply"), "Javob taklifi"),
    ]


async def admin_assistant(messages: list[dict], on_step=None) -> dict | None:
    """Admin suhbati. None — agent ishlamadi (chaqiruvchi eski usulga o'tadi)."""
    hist = [{"role": "assistant" if m.get("role") == "assistant" else "user", "text": str(m.get("text", ""))[:4000]}
            for m in messages[-14:] if str(m.get("text", "")).strip()]
    if not hist or hist[-1]["role"] != "user":
        return {"reply": "Savol yozing.", "actions": [], "steps": []}
    staged: list = []
    try:
        import insights
        mem = await insights.get_memory()
        mem_txt = (mem["notes"][-2500:] + ("\nREJALAR: " + mem["plans"][-1200:] if mem["plans"] else "")).strip()
    except Exception:  # noqa: BLE001
        mem_txt = ""
    system = ADMIN_SYSTEM + (f"\n\nXOTIRA (avvalgi eslatmalar):\n{mem_txt}" if mem_txt else "") + \
        f"\n\nBugun: {datetime.utcnow().strftime('%Y-%m-%d')}. Fan kodlari: {', '.join(db.SUBJECT_CODES)}."
    r = await ga.run_agent(system, hist, admin_tools(staged), deadline=55, max_steps=8, max_tokens=7000, on_step=on_step)
    if not r.ok and not staged:
        return None
    return {"reply": r.text or "Tayyor.", "actions": staged[:10], "steps": r.steps, "provider": "gemini", "model": r.model}


async def apply_support_reply(payload: dict, admin: str) -> dict:
    mid, text = int(payload.get("id")), str(payload.get("text") or "").strip()
    if not text:
        raise HTTPException(status_code=422, detail="Javob matni bo'sh.")
    ok = await db.admin_reply_support_message(mid, text)
    await db.log_admin_action(admin, "support_reply_ai", f"#{mid}")
    return {"ok": ok}


# =========================================================================== route'lar
def register(app, prefix: str, require_admin, get_current_user, limiter, templates=None) -> None:
    from fastapi.responses import HTMLResponse, RedirectResponse

    @app.get(f"{prefix}/longoai", response_class=HTMLResponse)
    async def longoai_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        import ai_gemini
        import reports
        return templates.TemplateResponse(request, "admin_longoai.html", {
            "active_tab": "longoai", "ai_ready": ai_gemini.is_gemini_configured(), "cfg": await reports.get_cfg(),
            "support_auto": (await db.get_setting("longoai_support_auto", "1")) != "0", "pending": await pending_count(),
            "audit_autofix": (await db.get_setting("ai_audit_autofix", "1")) != "0",
        })

    @app.post(f"{prefix}/api/agent/settings")
    async def agent_settings(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401)
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400)
        import reports
        body = await request.json()
        patch = {k: bool(body[k]) for k in ("auto_analyze", "auto_fix", "auto_reply", "web_search") if k in body}
        if "min_conf" in body:
            patch["min_conf"] = body["min_conf"]
        cfg = await reports.set_cfg(patch) if patch else await reports.get_cfg()
        if "support_auto" in body:
            await db.set_setting("longoai_support_auto", "1" if body["support_auto"] else "0")
        if "audit_autofix" in body:
            await db.set_setting("ai_audit_autofix", "1" if body["audit_autofix"] else "0")
        return JSONResponse({"ok": True, "cfg": cfg, "support_auto": (await db.get_setting("longoai_support_auto", "1")) != "0"})

    @app.post("/api/agent/kick")
    @limiter.limit("12/minute")
    async def agent_kick(request: Request):
        """O'quvchi sahifasi shikoyat/xabar yuborgach chaqiradi — shu odamning navbatdagi ishi darhol bajariladi."""
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401)
        done = await process_pending(limit=2, user_id=user.id, budget=55)
        return JSONResponse({"done": done})

    @app.get("/api/support/thread")
    async def support_thread(request: Request):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401)
        msgs = await db.get_user_support_messages(user.id, limit=10)
        await _ensure()
        async with db.async_session() as s:
            pend = int((await s.execute(select(func.count()).select_from(AgentJob).where(
                AgentJob.user_id == user.id, AgentJob.kind == "support", AgentJob.status.in_(("pending", "running"))))).scalar() or 0)
        return JSONResponse({"pending": pend, "items": [{"id": m.id, "reply": m.admin_reply, "replied": bool(m.replied_at)} for m in msgs]})

    @app.post(f"{prefix}/api/longoai/stream")
    async def longoai_stream(request: Request):
        """v246: admin yordamchi — ish bosqichlari jonli (SSE), yakuniy javob keyin keladi."""
        import asyncio
        from fastapi.responses import StreamingResponse
        if not require_admin(request):
            raise HTTPException(status_code=401)
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400)
        body = await request.json()
        msgs = body.get("messages") or []
        q: asyncio.Queue = asyncio.Queue()

        async def on_step(st: dict) -> None:
            await q.put({"step": st})

        async def worker():
            t0 = time.monotonic()
            try:
                out = await admin_assistant(msgs, on_step=on_step)
                if out is None:
                    import studio
                    out = await studio.run_assistant(msgs)
                out["ms"] = int((time.monotonic() - t0) * 1000)
                await q.put({"done": out})
            except Exception as exc:  # noqa: BLE001
                logger.exception("LongoAI stream")
                await q.put({"error": str(exc)[:300]})

        async def gen():
            task = asyncio.create_task(worker())
            yield b": ok\n\n"
            while True:
                try:
                    item = await asyncio.wait_for(q.get(), timeout=10)
                except asyncio.TimeoutError:
                    yield b": ping\n\n"
                    if task.done() and q.empty():
                        break
                    continue
                yield ("data: " + json.dumps(item, ensure_ascii=False, default=str) + "\n\n").encode()
                if "done" in item or "error" in item:
                    break

        return StreamingResponse(gen(), media_type="text/event-stream", headers={"Cache-Control": "no-store", "X-Accel-Buffering": "no"})

    @app.get(f"{prefix}/api/agent/jobs")
    async def agent_jobs(request: Request, limit: int = 40):
        if not require_admin(request):
            raise HTTPException(status_code=401)
        await _ensure()
        async with db.async_session() as s:
            rows = (await s.execute(select(AgentJob).order_by(desc(AgentJob.id)).limit(max(1, min(limit, 100))))).scalars().all()
            counts = dict((await s.execute(select(AgentJob.status, func.count()).group_by(AgentJob.status))).all())
        return JSONResponse({"counts": counts, "items": [{
            "id": j.id, "kind": j.kind, "ref": j.ref_id, "status": j.status, "result": j.result, "attempts": j.attempts,
            "steps": json.loads(j.steps) if j.steps else [], "created": j.created_at.strftime("%Y-%m-%d %H:%M") if j.created_at else "",
            "done": j.done_at.strftime("%H:%M") if j.done_at else ""} for j in rows]})

    @app.post(f"{prefix}/api/agent/run")
    async def agent_run(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401)
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400)
        done = await process_pending(limit=3, budget=50)
        return JSONResponse({"done": done, "left": await pending_count()})
