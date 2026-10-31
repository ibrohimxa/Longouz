"""LongoUZ — SAVOL BO'YICHA SHIKOYATLAR.

Foydalanuvchi test paytida "Shikoyat" tugmasini bosadi, o'ng tomondagi oynada savol bo'yicha nima xato ekanini yozadi.
Shikoyat admin panelga (/neo/reports) tushadi. U yerda:
  * Claude shikoyatni TAHLIL qiladi: savolni o'zi yechadi, haqiqatan xato bormi-yo'qmi aytadi va tuzatilgan variantni taklif qiladi;
  * admin "Tuzatishni qo'llash" tugmasi bilan savolni yangilaydi (yoki avto-rejimda yuqori ishonchli tuzatishlar o'zi qo'llanadi);
  * foydalanuvchiga bildirishnoma boradi.
Token tejash: AI faqat admin bosganda (yoki avto-rejim yoqilgan bo'lsa) ishlaydi, va bir savolga kelgan shikoyatlar bitta tahlilga jamlanadi.
"""
from __future__ import annotations

import json
import logging
from datetime import datetime

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy import select, func, desc

import database as db

logger = logging.getLogger("longouz.reports")

CATEGORIES = {
    "wrong_answer": "To'g'ri javob noto'g'ri belgilangan",
    "question_text": "Savol matnida xato / tushunarsiz",
    "options": "Variantlar noto'g'ri yoki takrorlangan",
    "no_correct": "To'g'ri javob variantlar orasida yo'q",
    "figure": "Chizma / rasm xato yoki ko'rinmayapti",
    "topic": "Savol bu mavzuga/faniga tegishli emas",
    "explanation": "Izoh (yechim) noto'g'ri",
    "typo": "Imlo / yozuv xatosi",
    "duplicate": "Savol takrorlanyapti",
    "other": "Boshqa",
}
STATUS_NAMES = {"new": "Yangi", "analyzed": "Tahlil qilingan", "fixed": "Tuzatilgan", "dismissed": "Rad etilgan"}

TRIAGE_SYSTEM = (
    "Siz O'zbekiston DTM/milliy sertifikat imtihon savollarini tekshiradigan ehtiyotkor mutaxassis-redaktorsiz. "
    "Sizga bitta test savoli, uning variantlari, bazada BELGILANGAN to'g'ri javob va foydalanuvchilarning shikoyatlari beriladi. "
    "VAZIFA: avval savolni O'ZINGIZ mustaqil yeching (hisob-kitobni qadamma-qadam tekshiring), keyin bazadagi javob bilan solishtiring. "
    "Foydalanuvchi shikoyati noto'g'ri bo'lishi mumkin — savol to'g'ri bo'lsa, buni ochiq ayting. "
    "FAQAT JSON obyekt qaytaring: "
    '{"verdict": "error" | "ok" | "unclear", "confidence": 0-100 (o\'z xulosangizga ishonchingiz), '
    '"problem": "bir-ikki gapda asosiy muammo (yoki nima uchun savol to\'g\'ri)", '
    '"solution": "qisqa yechim/asoslash", '
    '"fix": null yoki {"question": "tuzatilgan savol matni", "options": ["A","B","C","D"], "correct_index": 0-3, "explanation": "qisqa izoh"} '
    '(ochiq savol bo\'lsa options o\'rniga "accept": ["qabul qilinadigan javob", ...]), '
    '"action": "update" (savolni tuzatish) | "deactivate" (tuzatib bo\'lmaydi, yashirish kerak) | "none" (o\'zgarish kerak emas)}. '
    "QOIDALAR: fix faqat verdict=error va aniq ishonchli bo'lsa to'ldiriladi. Variantlar aniq 4 ta va turlicha bo'lsin. "
    "Formulalarni oddiy matn/yunikodda yozing (x², 10⁻³, H₂SO₄). Savol matnining ma'nosi va uslubini keraksiz o'zgartirmang — faqat xatoni tuzating. "
    "Ishonchingiz komil bo'lmasa verdict='unclear' va fix=null qo'ying — taxmin qilmang."
)


# ------------------------------------------------------------------ sozlamalar
async def get_cfg() -> dict:
    raw = await db.get_setting("reports_cfg", "")
    cfg = {"auto_analyze": False, "auto_fix": False, "min_conf": 92}
    try:
        cfg.update(json.loads(raw) if raw else {})
    except ValueError:
        pass
    return cfg


async def set_cfg(patch: dict) -> dict:
    cfg = await get_cfg()
    if "auto_analyze" in patch:
        cfg["auto_analyze"] = bool(patch["auto_analyze"])
    if "auto_fix" in patch:
        cfg["auto_fix"] = bool(patch["auto_fix"])
    if "min_conf" in patch:
        try:
            cfg["min_conf"] = max(70, min(100, int(patch["min_conf"])))
        except (TypeError, ValueError):
            pass
    await db.set_setting("reports_cfg", json.dumps(cfg))
    return cfg


# ------------------------------------------------------------------ yaratish
async def create_report(user, session_entry: dict, index: int, category: str, message: str, selected: str) -> dict:
    qs = session_entry.get("questions") or []
    if not 0 <= index < len(qs):
        raise HTTPException(status_code=422, detail="Savol topilmadi.")
    q = qs[index]
    category = category if category in CATEGORIES else "other"
    message = (message or "").strip()[:1500]
    if not message and category == "other":
        raise HTTPException(status_code=422, detail="Iltimos, nima xato ekanini yozing.")
    qid = q.get("id") if isinstance(q.get("id"), int) else None
    opts = q.get("options") or q.get("accept") or []
    async with db.async_session() as session:
        # bir foydalanuvchi bir savolga ochiq shikoyatni takrorlamasin — yangilanadi
        if qid is not None:
            prev = (await session.execute(
                select(db.QuestionReport).where(db.QuestionReport.user_id == user.id, db.QuestionReport.question_id == qid,
                                                db.QuestionReport.status.in_(("new", "analyzed")))
                .order_by(desc(db.QuestionReport.id)).limit(1))).scalar_one_or_none()
            if prev is not None:
                prev.category, prev.message, prev.selected_answer = category, message or prev.message, selected[:300]
                prev.created_at = datetime.utcnow()
                await session.commit()
                return {"id": prev.id, "updated": True}
        rep = db.QuestionReport(
            user_id=user.id, user_name=(user.first_name or user.email or "")[:120], question_id=qid,
            subject=session_entry.get("subject", ""), mode=session_entry.get("mode", ""), topic=str(q.get("topic") or session_entry.get("topic") or "")[:150],
            question_text=str(q.get("question") or ""), options_json=json.dumps(opts, ensure_ascii=False),
            correct_index=int(q.get("correct_index", -1)) if isinstance(q.get("correct_index"), int) else -1,
            explanation=str(q.get("explanation") or "")[:2000], selected_answer=selected[:300], category=category, message=message,
            attempt_token=str(session_entry.get("token", ""))[:64],
        )
        session.add(rep)
        await session.commit()
        await session.refresh(rep)
        return {"id": rep.id, "updated": False}


# ------------------------------------------------------------------ AI tahlil
def _fmt_question(row_or_q: dict) -> str:
    opts = row_or_q.get("options") or []
    lines = [f"Savol: {row_or_q.get('question')}"]
    if opts:
        for i, o in enumerate(opts):
            lines.append(f"  {'ABCD'[i] if i < 4 else i}) {o}")
        ci = row_or_q.get("correct_index")
        if isinstance(ci, int) and 0 <= ci < len(opts):
            lines.append(f"Bazada belgilangan to'g'ri javob: {'ABCD'[ci]}) {opts[ci]}")
    else:
        lines.append(f"Bazada qabul qilinadigan javob(lar): {row_or_q.get('accept')}")
    if row_or_q.get("explanation"):
        lines.append(f"Izoh: {row_or_q.get('explanation')}")
    return "\n".join(lines)


async def _live_question(qid: int | None) -> dict | None:
    if qid is None:
        return None
    async with db.async_session() as session:
        q = await session.get(db.Question, qid)
        if q is None:
            return None
        return db._question_to_dict(q) | {"subject": q.subject, "mode": q.mode, "is_active": q.is_active}


async def analyze_report(report_id: int, apply_if_confident: bool = False, admin: str = "AI") -> dict:
    import studio  # kech import: studio katta modul
    async with db.async_session() as session:
        rep = await session.get(db.QuestionReport, report_id)
        if rep is None:
            raise HTTPException(status_code=404, detail="Shikoyat topilmadi.")
        siblings = (await session.execute(
            select(db.QuestionReport).where(db.QuestionReport.question_id == rep.question_id, db.QuestionReport.status.in_(("new", "analyzed")))
            if rep.question_id is not None else select(db.QuestionReport).where(db.QuestionReport.id == rep.id)
        )).scalars().all()
        sib_ids = [s.id for s in siblings] or [rep.id]
        complaints = [f"- [{CATEGORIES.get(s.category, s.category)}] {s.message or '(izohsiz)'}" + (f" (foydalanuvchi tanlagan javob: {s.selected_answer})" if s.selected_answer else "")
                      for s in siblings][:12]
        live = await _live_question(rep.question_id)
        if live is None:
            try:
                opts = json.loads(rep.options_json or "[]")
            except ValueError:
                opts = []
            live = {"question": rep.question_text, "options": opts, "correct_index": rep.correct_index, "explanation": rep.explanation}
        head = f"Fan: {db.SUBJECT_NAMES.get(rep.subject, rep.subject)}; rejim: {rep.mode}; mavzu: {rep.topic}\n"
        user_msg = head + _fmt_question(live) + "\n\nFoydalanuvchi shikoyatlari:\n" + "\n".join(complaints)
    data = await studio.ai_json(TRIAGE_SYSTEM, user_msg, max_tokens=2500, timeout=55)
    if not isinstance(data, dict):
        raise HTTPException(status_code=502, detail="AI javob bermadi (kalit/kredit/tarmoq). Keyinroq urinib ko'ring.")
    verdict = data.get("verdict") if data.get("verdict") in ("error", "ok", "unclear") else "unclear"
    try:
        conf = max(0, min(100, int(data.get("confidence", 0))))
    except (TypeError, ValueError):
        conf = 0
    fix = data.get("fix") if isinstance(data.get("fix"), dict) else None
    if verdict != "error" or data.get("action") == "none":
        fix = None if verdict != "error" else fix
    note = (str(data.get("problem") or "") + ("\n\nYechim: " + str(data.get("solution")) if data.get("solution") else ""))[:2400]
    action = data.get("action") if data.get("action") in ("update", "deactivate", "none") else ("update" if fix else "none")
    payload = {"fix": fix, "action": action}
    async with db.async_session() as session:
        for sid in sib_ids:
            r = await session.get(db.QuestionReport, sid)
            if r is not None and r.status in ("new", "analyzed"):
                r.status, r.ai_verdict, r.ai_confidence, r.ai_note = "analyzed", verdict, conf, note
                r.ai_fix_json = json.dumps(payload, ensure_ascii=False)
        await session.commit()
    result = {"id": report_id, "verdict": verdict, "confidence": conf, "note": note, "fix": fix, "action": action, "applied": False}
    cfg = await get_cfg()
    if apply_if_confident and cfg.get("auto_fix") and verdict == "error" and conf >= cfg.get("min_conf", 92) and (fix or action == "deactivate"):
        try:
            await apply_fix(report_id, admin=admin + " (avto)")
            result["applied"] = True
        except HTTPException as exc:
            logger.info("Avto-tuzatish bajarilmadi: %s", exc.detail)
    return result


# ------------------------------------------------------------------ tuzatishni qo'llash
async def apply_fix(report_id: int, admin: str, override: dict | None = None) -> dict:
    import studio
    async with db.async_session() as session:
        rep = await session.get(db.QuestionReport, report_id)
        if rep is None:
            raise HTTPException(status_code=404, detail="Shikoyat topilmadi.")
        try:
            payload = json.loads(rep.ai_fix_json or "{}")
        except ValueError:
            payload = {}
        qid = rep.question_id
    if qid is None:
        raise HTTPException(status_code=422, detail="Bu shikoyat bazadagi aniq savolga bog'lanmagan (AI generatsiya qilingan savol).")
    fix = override if isinstance(override, dict) and override else payload.get("fix")
    action = "update" if override else payload.get("action")
    async with db.async_session() as session:
        q = await session.get(db.Question, qid)
        if q is None:
            raise HTTPException(status_code=404, detail="Savol bazada topilmadi (allaqachon o'chirilgan).")
        old_text, subj, mode, was_bank = q.question, q.subject, q.mode, q.source_file == "longouz-bank"
    if action == "deactivate" and not fix:
        res = await studio.apply_action({"type": "update_question", "payload": {"id": qid, "fields": {"is_active": False}}, "reason": f"shikoyat #{report_id}"}, admin)
    elif fix:
        fields: dict = {}
        if fix.get("question"):
            fields["question"] = fix["question"]
        if isinstance(fix.get("options"), list):
            fields["options"] = fix["options"]
        if isinstance(fix.get("accept"), list):
            fields["accept"] = fix["accept"]
        if isinstance(fix.get("correct_index"), int):
            fields["correct_index"] = fix["correct_index"]
        if fix.get("explanation") is not None:
            fields["explanation"] = fix["explanation"]
        if not fields:
            raise HTTPException(status_code=422, detail="Tuzatish ma'lumoti bo'sh.")
        res = await studio.apply_action({"type": "update_question", "payload": {"id": qid, "fields": fields}, "reason": f"shikoyat #{report_id}"}, admin)
        if was_bank:
            # tayyor bank qatori: keyingi versiya yangilanishida admin tuzatishi ustidan yozilib ketmasin
            async with db.async_session() as session:
                q = await session.get(db.Question, qid)
                if q is not None:
                    q.source_file = "longouz-fixed"
                    if q.question != old_text:
                        await db._add_tombstone(session, subj, mode, old_text)
                    await session.commit()
    else:
        raise HTTPException(status_code=422, detail="Qo'llash uchun tuzatish yo'q. Avval tahlil qiling yoki qo'lda tahrirlang.")
    now = datetime.utcnow()
    async with db.async_session() as session:
        rows = (await session.execute(select(db.QuestionReport).where(db.QuestionReport.question_id == qid,
                                                                      db.QuestionReport.status.in_(("new", "analyzed"))))).scalars().all()
        reporters = set()
        for r in rows:
            r.status, r.resolved_at = "fixed", now
            reporters.add(r.user_id)
        await session.commit()
    for uid in reporters:
        try:
            await db.create_notification(uid, "report", body="Siz yuborgan shikoyat ko'rib chiqildi va savol tuzatildi. Rahmat — bu platformani yaxshilaydi!", title="Shikoyatingiz ko'rib chiqildi")
        except Exception:  # noqa: BLE001
            logger.debug("bildirishnoma yuborilmadi", exc_info=True)
    regr = {"logs": 0, "users": 0}
    try:
        regr = await regrade_question(qid)
    except Exception:  # noqa: BLE001
        logger.exception("Qayta baholashda xato")
    await db.log_admin_action(admin, "report_fix", f"shikoyat #{report_id} -> savol #{qid}; qayta baholandi: {regr['logs']} ta natija, {regr['users']} o'quvchi")
    return {"ok": True, "question_id": qid, "resolved": len(reporters), "regraded": regr}


async def regrade_question(qid: int) -> dict:
    """Savol tuzatilgandan keyin: shu savol tushgan barcha test natijalarini qayta tekshiradi.
    Yangi to'g'ri javobga mos javob bergan o'quvchining bali OSHADI (kamaytirilmaydi) va unga xabar boradi."""
    import exam_rules
    async with db.async_session() as session:
        q = await session.get(db.Question, qid)
        if q is None:
            return {"logs": 0, "users": 0}
        new_ci = q.correct_index
        try:
            opts = json.loads(q.options_json or "[]")
        except ValueError:
            opts = []
        new_accept = opts if (q.qtype or "") == "open" else []
        new_correct_text = (str(opts[new_ci]).strip().lower() if (q.qtype or "") != "open" and isinstance(new_ci, int) and 0 <= new_ci < len(opts) else "")
        rows = (await session.execute(select(db.WebQuizLog).where(db.WebQuizLog.questions_json.like(f'%"id": {qid}%')))).scalars().all()
        changed_users: dict[int, int] = {}
        n_logs = 0
        for log in rows:
            try:
                items = json.loads(log.questions_json or "[]")
            except ValueError:
                continue
            gained = 0
            for it in items:
                if not isinstance(it, dict) or it.get("id") != qid or it.get("is_correct"):
                    continue
                ok = False
                if (it.get("qtype") or "closed") == "open":
                    ut = (it.get("user_text") or "").strip()
                    ok = bool(ut) and exam_rules.check_open_answer(ut, new_accept or it.get("accept") or [])
                else:
                    ui, iopts = it.get("user_index"), it.get("options") or []
                    # variantlar testda aralashtirilgan — raqam emas, tanlangan variant MATNI solishtiriladi
                    chosen = str(iopts[ui]).strip().lower() if isinstance(ui, int) and 0 <= ui < len(iopts) else ""
                    ok = bool(chosen) and bool(new_correct_text) and chosen == new_correct_text
                    if ok:
                        it["correct_index"] = ui
                if ok:
                    it["is_correct"] = True
                    it["regraded"] = True
                    gained += 1
            if gained:
                old_label = log.score_label or ""
                old_items = json.loads(log.questions_json or "[]")
                log.correct_count = min(log.total_count or 0, (log.correct_count or 0) + gained) or (log.correct_count or 0) + gained
                log.questions_json = json.dumps(items, ensure_ascii=False)
                new_label = _relabel(log, old_items, items, old_label)
                if new_label:
                    log.score_label = new_label
                # shu natija bo'yicha berilgan sertifikat ham yangilanadi (QR tekshiruv sahifasida yangi ball chiqadi)
                try:
                    certs = (await session.execute(select(db.UserCertificate).where(db.UserCertificate.quiz_log_id == log.id))).scalars().all()
                    for c in certs:
                        c.correct_count = log.correct_count
                        c.percent = round(100 * log.correct_count / log.total_count) if log.total_count else c.percent
                        if new_label:
                            c.score_label = new_label[:40]
                except Exception:  # noqa: BLE001
                    logger.debug("sertifikat yangilanmadi", exc_info=True)
                n_logs += 1
                prev = changed_users.get(log.user_id, (0, ""))
                changed_users[log.user_id] = (prev[0] + gained, new_label or prev[1])
        await session.commit()
    for uid, (g, lbl) in changed_users.items():
        try:
            extra = f" Yangi natija: {lbl}." if lbl else ""
            await db.create_notification(uid, "report", title="Natijangiz qayta hisoblandi — ball oshdi",
                                         body=f"Testdagi bir savol tekshirilib tuzatildi. Sizning javobingiz to'g'ri deb qabul qilindi: natijangizga +{g} ta to'g'ri javob qo'shildi.{extra} Reytingdagi o'rningiz ham yangilandi.")
        except Exception:  # noqa: BLE001
            logger.debug("bildirishnoma yuborilmadi", exc_info=True)
    return {"logs": n_logs, "users": len(changed_users)}


def _graded_from(items: list) -> list[dict]:
    return [{"is_correct": bool(it.get("is_correct")), "difficulty": it.get("difficulty"), "block": it.get("block"),
             "section": it.get("section"), "qtype": it.get("qtype") or "closed", "subject": it.get("_subject"),
             "coef": it.get("_coef"), "role": it.get("_role")} for it in items if isinstance(it, dict)]


def _relabel(log, old_items: list, new_items: list, old_label: str) -> str:
    """Qayta baholangandan keyingi natija yozuvi (masalan "62.3 / 93.0 ball" yoki "B2").
    Rasmiy tuzilmali (tiered) testlarda qaysi hisoblash usuli ishlatilganini eski yozuvni qayta hosil qilib aniqlaymiz;
    aniqlab bo'lmasa — yozuv o'zgartirilmaydi (noto'g'ri ball ko'rsatgandan ko'ra, eskisini qoldirish xavfsizroq)."""
    import scoring
    import exam_rules
    try:
        if exam_rules.is_tiered(log.subject, log.mode):
            for meta in ({"full_mock": False}, {"full_mock": True}, {"full_mock": True, "variant": "second"}):
                before = scoring.score_session(log.subject, log.mode, _graded_from(old_items), meta)
                if before and before.get("label") == old_label:
                    after = scoring.score_session(log.subject, log.mode, _graded_from(new_items), meta)
                    return (after or {}).get("label", "") or ""
            return ""
        old_correct = sum(1 for it in old_items if isinstance(it, dict) and it.get("is_correct"))
        before = scoring.score_result(log.mode, old_correct, log.total_count or 0)
        if before and before.get("label") == old_label:
            after = scoring.score_result(log.mode, log.correct_count or 0, log.total_count or 0)
            return (after or {}).get("label", "") or ""
        return ""
    except Exception:  # noqa: BLE001
        logger.debug("natija yozuvi qayta hisoblanmadi", exc_info=True)
        return ""


async def dismiss(report_id: int, note: str, admin: str) -> None:
    async with db.async_session() as session:
        rep = await session.get(db.QuestionReport, report_id)
        if rep is None:
            raise HTTPException(status_code=404, detail="Shikoyat topilmadi.")
        targets = [rep]
        if rep.question_id is not None:
            targets = (await session.execute(select(db.QuestionReport).where(db.QuestionReport.question_id == rep.question_id,
                                                                            db.QuestionReport.status.in_(("new", "analyzed"))))).scalars().all()
        for r in targets:
            r.status, r.admin_note, r.resolved_at = "dismissed", (note or "")[:500], datetime.utcnow()
        await session.commit()
    await db.log_admin_action(admin, "report_dismiss", f"#{report_id}")


# ------------------------------------------------------------------ ro'yxat
def _row(r: "db.QuestionReport", n_same: int = 1) -> dict:
    try:
        opts = json.loads(r.options_json or "[]")
    except ValueError:
        opts = []
    try:
        fixp = json.loads(r.ai_fix_json) if r.ai_fix_json else {}
    except ValueError:
        fixp = {}
    return {
        "id": r.id, "user": r.user_name, "question_id": r.question_id, "subject": r.subject, "subject_name": db.SUBJECT_NAMES.get(r.subject, r.subject),
        "mode": r.mode, "topic": r.topic, "question": r.question_text, "options": opts, "correct_index": r.correct_index,
        "explanation": r.explanation, "selected": r.selected_answer, "category": r.category, "category_name": CATEGORIES.get(r.category, r.category),
        "message": r.message, "status": r.status, "status_name": STATUS_NAMES.get(r.status, r.status), "verdict": r.ai_verdict, "confidence": r.ai_confidence,
        "ai_note": r.ai_note, "fix": fixp.get("fix"), "action": fixp.get("action"), "admin_note": r.admin_note, "same": n_same,
        "created": r.created_at.strftime("%Y-%m-%d %H:%M") if r.created_at else "",
    }


async def list_reports(status: str = "open", subject: str = "", page: int = 1, per: int = 30) -> dict:
    async with db.async_session() as session:
        cond = []
        if status == "open":
            cond.append(db.QuestionReport.status.in_(("new", "analyzed")))
        elif status in STATUS_NAMES:
            cond.append(db.QuestionReport.status == status)
        if subject:
            cond.append(db.QuestionReport.subject == subject)
        total = (await session.execute(select(func.count()).select_from(db.QuestionReport).where(*cond))).scalar() or 0
        rows = (await session.execute(select(db.QuestionReport).where(*cond).order_by(desc(db.QuestionReport.created_at))
                                      .offset((page - 1) * per).limit(per))).scalars().all()
        counts = dict((await session.execute(select(db.QuestionReport.status, func.count()).group_by(db.QuestionReport.status))).all())
        same: dict = {}
        qids = [r.question_id for r in rows if r.question_id is not None]
        if qids:
            same = dict((await session.execute(select(db.QuestionReport.question_id, func.count()).where(
                db.QuestionReport.question_id.in_(qids), db.QuestionReport.status.in_(("new", "analyzed"))).group_by(db.QuestionReport.question_id))).all())
        by_cat = dict((await session.execute(select(db.QuestionReport.category, func.count()).where(
            db.QuestionReport.status.in_(("new", "analyzed"))).group_by(db.QuestionReport.category))).all())
        by_subj = dict((await session.execute(select(db.QuestionReport.subject, func.count()).where(
            db.QuestionReport.status.in_(("new", "analyzed"))).group_by(db.QuestionReport.subject))).all())
    return {"total": total, "page": page, "per": per, "counts": counts, "by_category": by_cat, "by_subject": by_subj,
            "items": [_row(r, same.get(r.question_id, 1)) for r in rows]}


async def open_count() -> int:
    async with db.async_session() as session:
        return (await session.execute(select(func.count()).select_from(db.QuestionReport).where(db.QuestionReport.status == "new"))).scalar() or 0


# ------------------------------------------------------------------ route'lar
def register(app, prefix: str, require_admin, current_admin_username, templates, limiter, get_current_user) -> None:
    def guard(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")

    # ---------- foydalanuvchi tomoni ----------
    @app.get("/api/report-categories")
    async def report_categories():
        return JSONResponse({"categories": [{"code": k, "name": v} for k, v in CATEGORIES.items()]})

    @app.post("/api/report-question")
    @limiter.limit("20/minute")
    async def report_question(request: Request):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
        body = await request.json()
        token = str(body.get("attempt_token", ""))
        try:
            index = int(body.get("index"))
        except (TypeError, ValueError):
            raise HTTPException(status_code=422, detail="Savol raqami noto'g'ri.")
        entry = await db.get_quiz_session(token, user.id)
        if entry is None:
            raise HTTPException(status_code=404, detail="Test sessiyasi topilmadi yoki muddati o'tgan.")
        entry = dict(entry)
        entry["token"] = token
        res = await create_report(user, entry, index, str(body.get("category", "other")), str(body.get("message", "")), str(body.get("selected", "")))
        cfg = await get_cfg()
        if cfg.get("auto_analyze") and not res.get("updated"):
            import asyncio

            async def _bg():
                try:
                    await analyze_report(res["id"], apply_if_confident=True)
                except Exception:  # noqa: BLE001
                    logger.info("Avto-tahlil bajarilmadi", exc_info=True)
            asyncio.create_task(_bg())
        return JSONResponse({"ok": True, **res})

    # ---------- admin tomoni ----------
    @app.get(f"{prefix}/reports", response_class=HTMLResponse)
    async def reports_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        return templates.TemplateResponse(request, "admin_reports.html", {
            "active_tab": "reports", "subjects": db.SUBJECTS, "categories": CATEGORIES, "cfg": await get_cfg(),
            "ai_ready": bool(__import__("ai_keys").get("ANTHROPIC_API_KEY") or __import__("ai_keys").get("GEMINI_API_KEY")),
        })

    @app.get(f"{prefix}/api/reports")
    async def reports_list(request: Request, status: str = "open", subject: str = "", page: int = 1):
        guard(request)
        return JSONResponse(await list_reports(status, subject, max(1, page)))

    @app.get(f"{prefix}/api/reports/count")
    async def reports_count(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        return JSONResponse({"count": await open_count()})

    @app.post(f"{prefix}/api/reports/{{report_id}}/analyze")
    async def reports_analyze(request: Request, report_id: int):
        guard(request)
        return JSONResponse(await analyze_report(report_id))

    @app.post(f"{prefix}/api/reports/analyze-batch")
    async def reports_analyze_batch(request: Request):
        guard(request)
        body = await request.json()
        limit = max(1, min(int(body.get("limit", 5)), 8))
        auto_apply = bool(body.get("apply"))
        async with db.async_session() as session:
            rows = (await session.execute(select(db.QuestionReport).where(db.QuestionReport.status == "new").order_by(db.QuestionReport.id))).scalars().all()
        seen, ids = set(), []
        for r in rows:       # bir savolga bitta tahlil
            key = r.question_id if r.question_id is not None else ("r", r.id)
            if key in seen:
                continue
            seen.add(key)
            ids.append(r.id)
            if len(ids) >= limit:
                break
        out = []
        for rid in ids:
            try:
                out.append(await analyze_report(rid, apply_if_confident=auto_apply, admin=current_admin_username(request)))
            except HTTPException as exc:
                out.append({"id": rid, "error": exc.detail})
                if exc.status_code == 502:
                    break
        return JSONResponse({"done": len(out), "results": out, "left": max(0, len(rows) - len(ids))})

    @app.post(f"{prefix}/api/reports/{{report_id}}/apply")
    async def reports_apply(request: Request, report_id: int):
        guard(request)
        override = None
        try:
            body = await request.json()
            override = body.get("fix") if isinstance(body, dict) else None
        except ValueError:
            pass
        return JSONResponse(await apply_fix(report_id, current_admin_username(request), override))

    @app.post(f"{prefix}/api/reports/{{report_id}}/dismiss")
    async def reports_dismiss(request: Request, report_id: int):
        guard(request)
        try:
            body = await request.json()
        except ValueError:
            body = {}
        await dismiss(report_id, str(body.get("note", "")), current_admin_username(request))
        return JSONResponse({"ok": True})

    @app.post(f"{prefix}/api/reports/{{report_id}}/hide-question")
    async def reports_hide(request: Request, report_id: int):
        guard(request)
        import studio
        async with db.async_session() as session:
            rep = await session.get(db.QuestionReport, report_id)
            if rep is None or rep.question_id is None:
                raise HTTPException(status_code=404, detail="Savol topilmadi.")
            qid = rep.question_id
        await studio.apply_action({"type": "update_question", "payload": {"id": qid, "fields": {"is_active": False}}, "reason": f"shikoyat #{report_id}"},
                                  current_admin_username(request))
        await dismiss(report_id, "Savol yashirildi", current_admin_username(request))
        return JSONResponse({"ok": True})

    @app.post(f"{prefix}/api/reports/settings")
    async def reports_settings(request: Request):
        guard(request)
        return JSONResponse(await set_cfg(await request.json()))
