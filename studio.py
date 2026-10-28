"""LongoUZ STUDIO — admin uchun AI yordamida ishlaydigan vositalar.

  1) Hujjat -> savollar: istalgan PDF / Word / Excel / JSON / CSV / matn / rasm; chizmalar saqlanadi (yoki AI qayta chizadi);
  2) Mock yaratish: bankdan yoki hujjatdan 1-3 ta o'zaro farqli variant (rasmiy tuzilma bo'yicha);
  3) Baza ko'rinishi: fan/rejim/tarif kesimida statistika, kam savolli mavzular, bazani yangilash, o'zgarishlar tarixi;
  4) Claude yordamchi: bazani o'qiydi, tahlil qiladi, o'zgartirishlarni TAKLIF qiladi — admin tasdiqlagandan keyin bajariladi.
Barcha endpointlar admin sessiyasi va `x-requested-with: fetch` bilan himoyalangan.
"""
from __future__ import annotations

import asyncio
import base64
import json
import logging
import os
import re
import time

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

import ai_keys
import database as db
import exam_db
import exam_rules
import figures as figures_mod
import question_import as qimport
from content._dsl import _build_match

logger = logging.getLogger("longouz.studio")

CHUNK_CHARS = 9000
MAX_DOC_BYTES = 25 * 1024 * 1024
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------------------
# Umumiy: AI'dan JSON olish (Claude -> Gemini)
# --------------------------------------------------------------------------------------


def _json_from_text(raw: str):
    txt = (raw or "").strip()
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\s*|\s*```$", "", txt).strip()
    for cand in (txt, ):
        try:
            return json.loads(cand)
        except ValueError:
            pass
    m = re.search(r"(\[.*\]|\{.*\})", txt, re.S)
    if m:
        try:
            return json.loads(m.group(1))
        except ValueError:
            return None
    return None


async def ai_json(system: str, user: str | list, max_tokens: int = 6000, timeout: float = 50.0):
    """Claude (asosiy) -> Gemini (zaxira). JSON obyektini qaytaradi yoki None. user — matn yoki Claude content bloklari."""
    import ai_claude
    import ai_gemini
    client = ai_claude._get_client()
    if client is not None:
        try:
            async def run():
                async with client.messages.stream(
                    model=ai_keys.get("CLAUDE_MODEL", "claude-sonnet-5-5"), max_tokens=max_tokens, system=system,
                    messages=[{"role": "user", "content": user}],
                ) as stream:
                    return await stream.get_final_message()
            msg = await asyncio.wait_for(run(), timeout=timeout)
            data = _json_from_text(msg.content[0].text)
            if data is not None:
                return data
        except Exception as exc:  # noqa: BLE001
            logger.warning("Claude JSON so'rovi ishlamadi: %s", exc)
    if ai_gemini.is_gemini_configured() and isinstance(user, str):
        try:
            resp = await asyncio.wait_for(ai_gemini._call_gemini_with_retry(
                model=ai_keys.get("GEMINI_MODEL", "gemini-3.6-flash"), contents=user,
                config={"system_instruction": system, "max_output_tokens": max_tokens,
                        "automatic_function_calling": ai_gemini._NO_AFC_CONFIG}), timeout=timeout)
            return _json_from_text(resp.text or "")
        except Exception as exc:  # noqa: BLE001
            logger.warning("Gemini JSON so'rovi ishlamadi: %s", exc)
    return None


# --------------------------------------------------------------------------------------
# 1) HUJJAT -> SAVOLLAR
# --------------------------------------------------------------------------------------

PARSE_SYSTEM = (
    "Siz imtihon savollarini hujjatdan ajratib oladigan aniq va ehtiyotkor yordamchisiz. Matn PDF/Word/Excel dan olingan (xatolar, "
    "sahifa raqamlari, sarlavhalar bo'lishi mumkin). Faqat HAQIQIY test savollarini oling. Savol matnini ASL HOLATIDA saqlang "
    "(faqat aniq OCR/format xatolarini to'g'rilang, formulalarni oddiy matn/yunikodda yozing: x^2 -> x², 10^-3 -> 10⁻³). "
    "Har bir savol uchun JSON obyekt: "
    '{"no": hujjatdagi tartib raqami yoki null, "type": "closed"|"open"|"match", "question": "...", '
    '"options": ["A variant","B variant","C variant","D variant"] (faqat closed; variant harflari/belgilarini olib tashlang), '
    '"answer": closed uchun to\'g\'ri variant harfi (A-D) yoki indeksi (0-3); open uchun qabul qilinadigan javoblar ro\'yxati [..] (raqamli bo\'lsa faqat son/ifoda), '
    '"pairs": [["chap1","o\'ng1"],["chap2","o\'ng2"],["chap3","o\'ng3"]] (faqat match), '
    '"explanation": "qisqa izoh (bo\'lsa; bo\'lmasa bo\'sh)", "topic": "eng mos mavzu nomi (berilgan ro\'yxatdan, mos kelmasa yangi qisqa nom)", '
    '"difficulty": 1|2|3, "solved": true agar javob hujjatda YO\'Q bo\'lib, siz o\'zingiz yechib topgan bo\'lsangiz (aks holda false), '
    '"figure_note": chizma/jadval/grafik KERAK bo\'lsa-yu matnda ko\'rinmasa nima tasvirlanishi kerakligi (aks holda null), '
    '"svg": agar savol sodda chizmaga (geometriya, grafik, elektr sxemasi, hujayra, molekula...) muhtoj bo\'lsa — OQ FONLI, aniq, '
    'ranglar bilan, viewBox "0 0 340 215" bo\'lgan toza <svg> kodi (yo\'qsa null)}. '
    "QOIDALAR: javob kaliti hujjatning boshqa joyida (oxirida 'Javoblar: 1-A ...') bo'lsa, shu matnda bo'lsa foydalaning; yo'q bo'lsa o'zingiz "
    "diqqat bilan yechib, solved=true qo'ying — taxmin qilmang, ishonchingiz komil bo'lmasa savolni tashlab keting. Variantlar soni aniq 4 bo'lsin "
    "(5 ta bo'lsa eng ishonchsizini olib tashlamang — savolni tashlab keting). Matnda [[IMG:xxxxxxxxxxxxxxxx]] belgilari bo'lsa, ularni savol/variant matnida AYNAN saqlang. "
    "Hujjatda bo'lmagan savol uydirmang. Natija FAQAT JSON massiv (boshqa matnsiz)."
)


def _norm_ai_item(raw: dict, default_topic: str = "") -> dict | None:
    if not isinstance(raw, dict):
        return None
    q = qimport._clean(str(raw.get("question") or ""))
    if len(q) < 8:
        return None
    t = str(raw.get("type") or "closed").lower()
    t = t if t in ("closed", "open", "match") else "closed"
    out = {
        "no": raw.get("no") if isinstance(raw.get("no"), int) else 0,
        "qtype": t, "question": q[:1900], "explanation": str(raw.get("explanation") or "")[:1900],
        "topic": (str(raw.get("topic") or default_topic or "Umumiy").strip() or "Umumiy")[:150],
        "difficulty": raw.get("difficulty") if raw.get("difficulty") in (1, 2, 3) else 2,
        "solved": bool(raw.get("solved")), "figure_note": raw.get("figure_note") or None,
    }
    if t == "closed":
        opts = [qimport._clean(str(o)) for o in (raw.get("options") or [])]
        opts = [re.sub(r"^\(?[A-Da-d][\).:]\s+", "", o) for o in opts]
        if len(opts) != 4 or any(not o for o in opts) or len({o.lower() for o in opts}) != 4:
            return None
        a = raw.get("answer")
        ci = None
        if isinstance(a, int) and 0 <= a <= 3:
            ci = a
        elif isinstance(a, str):
            a = a.strip()
            if a.upper()[:1] in "ABCD" and len(a) <= 2:
                ci = "ABCD".index(a.upper()[:1])
            elif a.isdigit() and 0 <= int(a) <= 3:
                ci = int(a)
            else:
                for i, o in enumerate(opts):
                    if o.lower() == a.lower():
                        ci = i
        if ci is None:
            return None
        out.update({"options": opts, "correct_index": ci})
    elif t == "open":
        acc = raw.get("answer")
        acc = [acc] if isinstance(acc, (str, int, float)) else (acc or [])
        acc = [str(a).strip() for a in acc if str(a).strip()][:8]
        if not acc:
            return None
        out.update({"options": acc, "correct_index": 0})
    else:  # match
        pairs = [(str(p[0]).strip(), str(p[1]).strip()) for p in (raw.get("pairs") or []) if isinstance(p, (list, tuple)) and len(p) == 2]
        if len(pairs) < 3 or len({l for l, _ in pairs}) != len(pairs):
            return None
        pairs = pairs[:4]
        text, correct, wrong = _build_match({"pairs": pairs})
        opts = [correct] + wrong
        import random
        r = random.Random(text)
        order = list(range(len(opts)))
        r.shuffle(order)
        out.update({"question": text, "options": [opts[i] for i in order], "correct_index": order.index(0)})
    svg = raw.get("svg")
    if isinstance(svg, str) and svg.strip().startswith("<svg"):
        clean = figures_mod.sanitize_svg(svg)
        if clean:
            out["figure"] = {"q": {"type": "svg", "svg": clean}, "o": [None] * 4}
            out["ai_figure"] = True
    return out


def _doc_chunks(text: str) -> list[str]:
    text = re.sub(r"[ \t]+", " ", text)
    chunks, cur = [], ""
    for para in re.split(r"\n{1,}", text):
        if len(cur) + len(para) + 1 > CHUNK_CHARS and cur:
            chunks.append(cur)
            cur = ""
        cur += para + "\n"
    if cur.strip():
        chunks.append(cur)
    return chunks


def _extract_doc(name: str, data: bytes) -> dict:
    """Bitta fayldan: matn bo'laklari, qoida bo'yicha topilgan savollar, chizmalar xaritasi (sync, thread ichida)."""
    low = name.lower()
    info = {"name": name, "kind": "text", "chunks": [], "regex_items": [], "figures": {}, "warn": "", "pages": 0, "visual": False}
    if len(data) > MAX_DOC_BYTES:
        info["warn"] = "Fayl juda katta (25 MB dan oshmasin)."
        return info
    try:
        if low.endswith(".pdf"):
            info["kind"] = "pdf"
            from pypdf import PdfReader
            import io
            reader = PdfReader(io.BytesIO(data))
            info["pages"] = len(reader.pages)
            pages = []
            for p in reader.pages[:300]:
                try:
                    pages.append(p.extract_text() or "")
                except Exception:  # noqa: BLE001
                    pages.append("")
            text = "\n".join(pages)
            if len(text.strip()) < 80:
                info["visual"] = True
                info["warn"] = "Matn topilmadi (skaner/rasm) — AI ko'rish rejimi ishlatiladi."
            else:
                info["chunks"] = _doc_chunks(text)
                try:
                    import question_figures
                    found = question_figures.pdf_question_figures(data)
                    info["figures"] = {str(n): f for n, f in found if f}
                except Exception:  # noqa: BLE001
                    pass
        elif low.endswith(".docx"):
            info["kind"] = "docx"
            from docx import Document
            import io
            import question_figures
            from docx.table import Table
            from docx.text.paragraph import Paragraph
            doc = Document(io.BytesIO(data))
            lines = []
            for child in doc.element.body.iterchildren():
                tag = child.tag.rsplit("}", 1)[-1]
                if tag == "p":
                    para = Paragraph(child, doc)
                    if child.xpath(".//a:blip"):
                        lines.append("".join(r.text + " " + question_figures.docx_marker_text(r._r, doc.part) + " " for r in para.runs))
                    else:
                        lines.append(para.text)
                elif tag == "tbl":
                    for row in Table(child, doc).rows:
                        cells = []
                        for c in row.cells:
                            t = c.text.strip()
                            if t and (not cells or cells[-1] != t):
                                cells.append(t)
                        lines.append("  ".join(cells))
            info["chunks"] = _doc_chunks("\n".join(lines))
        elif low.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
            info["kind"], info["visual"] = "image", True
        elif low.endswith((".xlsx", ".csv", ".tsv", ".json")):
            info["kind"] = "table"
            items, w = qimport._parse_single(name, data)
            info["regex_items"] = items
            info["warn"] = w
        else:
            text = qimport._decode(data)
            if low.endswith((".html", ".htm")):
                text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
                text = re.sub(r"<[^>]+>", " ", text)
            info["chunks"] = _doc_chunks(text)
        if info["chunks"]:
            items = qimport.parse_plain_text("\n".join(info["chunks"]))
            info["regex_items"] = items[:2500]
    except Exception as exc:  # noqa: BLE001
        logger.exception("Hujjatni o'qishda xato: %s", name)
        info["warn"] = f"O'qib bo'lmadi: {exc}"
    return info


def _dup_info(items: list[dict], db_index: dict) -> None:
    seen = set()
    for it in items:
        key = qimport.norm_key(it["question"])
        info = db_index.get(key)
        it["dup"] = ({"id": info["id"], "topic": info["topic"]} if info else ("file" if key in seen else None))
        seen.add(key)


async def _bank_snapshot(subject_hint: str, mode: str) -> dict:
    """AI mavzu tanlashi uchun: fan -> mavzular ro'yxati."""
    out = {}
    for s in db.SUBJECTS:
        if subject_hint not in ("auto", "", s["code"]):
            continue
        cnt = await db.count_questions_by_topic(s["code"], mode)
        out[s["code"]] = sorted(cnt.keys())[:120]
    return out


GEN_SYSTEM = (
    "Siz O'zbekiston DTM va milliy sertifikat imtihonlari uchun test tuzuvchi tajribali metodistsiz. Berilgan fan va MAVZU bo'yicha aniq, "
    "bir ma'noli, faktik jihatdan TO'G'RI savollar yarating (maktab darsligi va rasmiy dastur doirasida). Qoidalar: "
    "(1) har savol faqat shu mavzuga oid; (2) closed savolda aynan 4 ta variant, bittasi aniq to'g'ri, qolganlari ishonarli lekin aniq xato; "
    "(3) hisoblash savollarida javobni o'zingiz bosqichma-bosqich tekshiring va izohda qisqa yechim yozing; (4) sana/ism/formulani faqat ishonchingiz komil bo'lsa yozing — "
    "shubhali savolni tashlab keting; (5) qiyinlik aralash (1 oson, 2 o'rta, 3 qiyin) va ochiq (type=open, qisqa javobli) savollarning 20% atrofida bo'lsin; "
    "fizika/matematika/kimyo/biologiyada mos joyda sodda chizma kerak bo'lsa 'svg' maydonida (oq fon, viewBox 0 0 340 215, aniq rangli) bering; "
    "(6) bazada allaqachon bor savollarni takrorlamang; (7) fanga mos qisqa kontekst kiriting: tarix/adabiyot/ona tili/til fanlarida savol matnidan oldin 2–4 gaplik "
    "qisqa PARCHA (manba, matn, jumla) bering va savolni shu parchaga bog'lang; fizika/kimyo/biologiya/matematikada shart (berilgan kattaliklar) savol matnida aniq bo'lsin. Chiqish — FAQAT JSON massiv, har element: "
    '{"type":"closed"|"open","question":"..","options":[4 ta] (closed),"answer":"A-D harfi" (closed) yoki [qabul qilinadigan javoblar] (open),'
    '"explanation":"..","difficulty":1|2|3,"svg":null yoki "<svg..>"}.'
)


async def ai_generate(subject: str, mode: str, topic: str, count: int, existing: list[str]) -> list[dict]:
    count = max(1, min(12, count))
    user = (f"Fan: {db.SUBJECT_NAMES.get(subject, subject)}. Rejim: {mode}. MAVZU: {topic}.\n{count} ta savol yarating.\n"
            f"Mavjud savollar (takrorlamang): " + " | ".join(e[:70] for e in existing[:25]))
    data = await ai_json(GEN_SYSTEM, user, max_tokens=7000, timeout=55)
    if data is None:
        raise HTTPException(status_code=502, detail="AI javob bermadi (kalit/kredit/tarmoq).")
    if isinstance(data, dict):
        data = data.get("questions") or []
    out = []
    for raw in data:
        it = _norm_ai_item(raw, topic)
        if it:
            it["topic"] = topic
            it["ai_generated"] = True
            out.append(it)
    return out


# --------------------------------------------------------------------------------------
# COMMIT: tahrirlangan savollarni bazaga yozish
# --------------------------------------------------------------------------------------

def _plan_for(difficulty: int, n_in_topic: dict, topic: str, forced) -> int:
    if forced in (0, 1, 2):
        return int(forced)
    n_in_topic[(topic, difficulty)] = n_in_topic.get((topic, difficulty), 0) + 1
    n = n_in_topic[(topic, difficulty)]
    if difficulty == 1:
        return 0
    if difficulty == 2:
        return 0 if n <= 3 else 1
    return 1 if n <= 2 else 2


async def commit_items(subject: str, mode: str, items: list[dict], publish: bool = True, mock_name: str = "AI import",
                       default_tier: str = "free", admin: str = "") -> dict:
    from sqlalchemy import func, select
    added_ids, skipped_dup, skipped_bad = [], 0, 0
    topics_new: dict[str, int] = {}
    n_in_topic: dict = {}
    tiered = exam_rules.is_tiered(subject, mode)
    async with db.async_session() as session:
        existing = {str(t).strip().lower() for (t,) in (await session.execute(
            select(db.Question.question).where(db.Question.subject == subject, db.Question.mode == mode))).all()}
        have_meta = {t for (t,) in (await session.execute(
            select(db.TopicMeta.topic).where(db.TopicMeta.subject == subject, db.TopicMeta.mode == mode))).all()}
        max_order = (await session.execute(select(func.max(db.TopicMeta.order_no)).where(
            db.TopicMeta.subject == subject, db.TopicMeta.mode == mode))).scalar() or 0
        for it in items:
            text = str(it.get("question") or "").strip()
            qt = it.get("qtype") or "closed"
            opts = [str(o).strip() for o in (it.get("options") or [])]
            ci = it.get("correct_index", 0)
            if not text or len(text) > 2000 or qt not in ("closed", "open", "match"):
                skipped_bad += 1
                continue
            if qt == "open":
                if not opts:
                    skipped_bad += 1
                    continue
                ci = 0
            else:
                if len(opts) != 4 or any(not o for o in opts) or len({o.lower() for o in opts}) != 4 or not isinstance(ci, int) or not 0 <= ci < 4:
                    skipped_bad += 1
                    continue
            if text.lower() in existing and not it.get("force"):
                skipped_dup += 1
                continue
            existing.add(text.lower())
            topic = (str(it.get("topic") or "Umumiy").strip() or "Umumiy")[:150]
            d = it.get("difficulty") if it.get("difficulty") in (1, 2, 3) else 2
            fig = it.get("figure")
            fig_json = figures_mod.figures_to_json(fig) if fig else ""
            if len(json.dumps(opts, ensure_ascii=False)) > 2900:
                skipped_bad += 1
                continue
            if tiered and topic not in have_meta:
                max_order += 1
                tier = it.get("tier") if it.get("tier") in ("free", "pro", "ultra") else default_tier
                session.add(db.TopicMeta(subject=subject, mode=mode, topic=topic, code=f"X{max_order}", grade=int(it.get("grade") or 0),
                                         tier=tier, order_no=max_order, block=""))
                have_meta.add(topic)
                topics_new[topic] = 0
            q = db.Question(
                subject=subject, mode=mode, topic=topic, mock_test=(mock_name or "AI import")[:80], question=text,
                options_json=json.dumps(opts, ensure_ascii=False), correct_index=ci, explanation=str(it.get("explanation") or "")[:1900],
                is_active=bool(publish), figure_json=fig_json, source_file=str(it.get("src") or "")[:200], source_no=int(it.get("no") or 0),
                grade=int(it.get("grade") or 0), difficulty=d, block=("moslash" if qt == "match" else str(it.get("block") or "")[:20]),
                qtype=qt, min_plan=_plan_for(d, n_in_topic, topic, it.get("min_plan")),
            )
            session.add(q)
            await session.flush()
            added_ids.append(q.id)
            if topic in topics_new:
                topics_new[topic] += 1
        await session.commit()
    if admin:
        await db.log_admin_action(admin, "studio_commit", f"{subject}/{mode}: +{len(added_ids)}, takror {skipped_dup}, yaroqsiz {skipped_bad}")
    return {"added": len(added_ids), "ids": added_ids, "dup": skipped_dup, "bad": skipped_bad, "new_topics": topics_new}


# --------------------------------------------------------------------------------------
# 2) MOCK
# --------------------------------------------------------------------------------------

async def build_mocks(subject: str, mode: str, name: str, variants: int, topics: list[str] | None, min_plan: int,
                      admin: str, time_minutes: int = 0) -> list[dict]:
    variants = max(1, min(3, variants))
    used: set[int] = set()
    out = []
    for v in range(1, variants + 1):
        if exam_rules.is_tiered(subject, mode):
            qs = await exam_db.assemble_exam(subject, mode, "ultra", "main", exclude_ids=used, topics=topics or None)
        else:
            qs = await db.get_questions_db(subject, 30, mode)
        ids = [q["id"] for q in qs if q.get("id")]
        if not ids:
            raise HTTPException(status_code=404, detail="Bu fan/rejim uchun savollar yetarli emas.")
        used.update(ids)
        m = await db.create_mock(subject, mode, name, v, ids, min_plan, admin, time_minutes)
        out.append({"id": m.id, "variant": v, "total": len(ids)})
    await db.log_admin_action(admin, "mock_create", f"{subject}/{mode} '{name}' x{variants}")
    return out


# --------------------------------------------------------------------------------------
# 3) BAZA KO'RINISHI
# --------------------------------------------------------------------------------------

async def bank_overview() -> dict:
    from sqlalchemy import case, func, select
    Q = db.Question
    async with db.async_session() as session:
        rows = (await session.execute(
            select(Q.subject, Q.mode, func.count(Q.id),
                   func.sum(case((Q.min_plan == 0, 1), else_=0)), func.sum(case((Q.min_plan == 1, 1), else_=0)),
                   func.sum(case((Q.min_plan == 2, 1), else_=0)),
                   func.sum(case((Q.qtype == "open", 1), else_=0)), func.sum(case((Q.qtype == "match", 1), else_=0)),
                   func.sum(case((Q.figure_json != "", 1), else_=0)), func.sum(case((Q.is_active == False, 1), else_=0)),  # noqa: E712
                   func.count(func.distinct(Q.topic)))
            .group_by(Q.subject, Q.mode).order_by(Q.subject, Q.mode))).all()
        meta = (await session.execute(
            select(db.TopicMeta.subject, db.TopicMeta.mode, db.TopicMeta.tier, func.count(db.TopicMeta.id))
            .group_by(db.TopicMeta.subject, db.TopicMeta.mode, db.TopicMeta.tier))).all()
    tiers: dict = {}
    for s, m, t, c in meta:
        tiers.setdefault(f"{s}/{m}", {})[t] = c
    table = []
    for s, m, total, free, pro, ultra, op, mt, fg, inactive, ntop in rows:
        table.append({
            "subject": s, "subject_name": db.SUBJECT_NAMES.get(s, s), "mode": m, "total": total, "free": int(free or 0), "pro": int(pro or 0),
            "ultra": int(ultra or 0), "open": int(op or 0), "match": int(mt or 0), "figures": int(fg or 0), "inactive": int(inactive or 0),
            "topics": ntop, "topic_tiers": tiers.get(f"{s}/{m}", {}),
        })
    return {"table": table, "version": open(os.path.join(BASE_DIR, "VERSION")).read().strip() if os.path.exists(os.path.join(BASE_DIR, "VERSION")) else "?"}


async def topic_report(subject: str, mode: str) -> list[dict]:
    """Mavzu kesimi: nechta savol, tarif bo'yicha taqsimot, ochiq/moslashtirish/chizma soni, 50 dan kam bo'lganlar belgilanadi."""
    from sqlalchemy import case, func, select
    Q = db.Question
    async with db.async_session() as session:
        rows = (await session.execute(
            select(Q.topic, func.count(Q.id), func.sum(case((Q.min_plan == 0, 1), else_=0)), func.sum(case((Q.min_plan <= 1, 1), else_=0)),
                   func.sum(case((Q.qtype == "open", 1), else_=0)), func.sum(case((Q.qtype == "match", 1), else_=0)),
                   func.sum(case((Q.figure_json != "", 1), else_=0)))
            .where(Q.subject == subject, Q.mode == mode, Q.is_active == True).group_by(Q.topic))).all()  # noqa: E712
        meta = {t: (g, tier, code) for t, g, tier, code in (await session.execute(
            select(db.TopicMeta.topic, db.TopicMeta.grade, db.TopicMeta.tier, db.TopicMeta.code)
            .where(db.TopicMeta.subject == subject, db.TopicMeta.mode == mode))).all()}
    out = []
    for t, n, free, pro_cum, op, mt, fg in rows:
        g, tier, code = meta.get(t, (0, "", ""))
        out.append({"topic": t, "code": code, "grade": g, "tier": tier, "total": n, "free_q": int(free or 0), "pro_q": int(pro_cum or 0),
                    "open": int(op or 0), "match": int(mt or 0), "figures": int(fg or 0)})
    out.sort(key=lambda r: (r["grade"], r["code"], r["topic"]))
    return out


async def seed_step(step: int) -> dict:
    """Bazani yangilash — har chaqiruvda BITTA (fan, rejim) paketi (Vercel 60 soniya chegarasiga sig'adi)."""
    import content
    packs = content.load_packs()
    plan = [(p["subject"], mode, p) for p in packs for mode in p["modes"]]
    if step >= len(plan):
        await db.set_setting(f"seed_exam_content_{exam_db.CONTENT_VERSION}", "1")
        return {"done": True, "total_steps": len(plan), "step": step}
    subject, mode, pack = plan[step]
    added = await exam_db._seed_pack(subject, mode, pack["topics"], pack["questions"], exam_db.pack_keep_keys(packs)[(subject, mode)])
    return {"done": False, "step": step, "total_steps": len(plan), "subject": subject, "mode": mode, "added": added}


# --------------------------------------------------------------------------------------
# 4) CLAUDE YORDAMCHI (tool-use; o'zgartirishlar admin tasdig'ini kutadi)
# --------------------------------------------------------------------------------------

ASSISTANT_SYSTEM = (
    "Siz LongoUZ admin yordamchisisiz (xavfsiz, aniq, o'zbek tilida). Sizda bazani O'QISH vositalari bor (bank_stats, topic_report, find_questions, get_question, "
    "list_mocks) va o'zgartirish TAKLIF qilish vositalari (propose_*). Taklif qilingan o'zgartirishlar darhol bajarilmaydi — admin ko'rib chiqib 'Qo'llash' tugmasini bosadi. "
    "Ishlash tartibi: avval o'qing va tekshiring (savol to'g'riligi: javob, hisob, sana; mavzuga mosligi; variantlar takrori; tarif/qiyinlik muvozanati), "
    "keyin aniq, kichik, asoslangan taklif bering (reason maydonini to'ldiring). Hech qachon uydirmang: bilmasangiz yoki ishonchingiz komil bo'lmasa, buni ayting. "
    "Matematika/fizika/kimyo javoblarini bosqichma-bosqich o'zingiz qayta hisoblab tekshiring. Javobingiz qisqa va tushunarli bo'lsin: nima topildi, nima taklif qilindi. "
    "Foydalanuvchi hujjat/mavzu haqida so'rasa, bazadagi holatni vosita bilan tekshirib, nimalar yetishmasligini (kam savolli mavzu, ochiq/moslashtirish/chizma yo'qligi) ayting."
)

_TOOLS = [
    {"name": "bank_stats", "description": "Butun baza statistikasi: fan/rejim kesimida savol, mavzu, tarif, ochiq/moslashtirish/chizma soni.",
     "input_schema": {"type": "object", "properties": {}}},
    {"name": "topic_report", "description": "Bitta fan+rejim bo'yicha har bir mavzuning savol soni (tarif, tur, chizma kesimida).",
     "input_schema": {"type": "object", "properties": {"subject": {"type": "string"}, "mode": {"type": "string"}}, "required": ["subject", "mode"]}},
    {"name": "find_questions", "description": "Savollarni qidirish (matn bo'yicha yoki mavzu bo'yicha). Eng ko'pi 15 ta qaytaradi.",
     "input_schema": {"type": "object", "properties": {"subject": {"type": "string"}, "mode": {"type": "string"}, "topic": {"type": "string"},
                                                          "text": {"type": "string"}, "offset": {"type": "integer"}}, "required": ["subject", "mode"]}},
    {"name": "get_question", "description": "Savolning to'liq ma'lumoti (variantlar, javob, izoh, tarif).",
     "input_schema": {"type": "object", "properties": {"id": {"type": "integer"}}, "required": ["id"]}},
    {"name": "list_mocks", "description": "Yaratilgan mock-variantlar.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "propose_update_question", "description": "Savolni TUZATISH taklifi. fields: question, options[4], correct_index(0-3), accept[] (ochiq), explanation, topic, difficulty(1-3), min_plan(0-2), is_active.",
     "input_schema": {"type": "object", "properties": {"id": {"type": "integer"}, "fields": {"type": "object"}, "reason": {"type": "string"}}, "required": ["id", "fields", "reason"]}},
    {"name": "propose_delete_question", "description": "Savolni O'CHIRISH taklifi (xato/takror/yaroqsiz).",
     "input_schema": {"type": "object", "properties": {"id": {"type": "integer"}, "reason": {"type": "string"}}, "required": ["id", "reason"]}},
    {"name": "propose_create_questions", "description": "Yangi savollar qo'shish taklifi. Har savol: question, qtype(closed|open|match), options[4] yoki accept[], correct_index, explanation, difficulty, topic.",
     "input_schema": {"type": "object", "properties": {"subject": {"type": "string"}, "mode": {"type": "string"}, "topic": {"type": "string"},
                                                          "questions": {"type": "array", "items": {"type": "object"}}, "reason": {"type": "string"}},
                      "required": ["subject", "mode", "topic", "questions", "reason"]}},
]


async def _tool_find(args: dict) -> list[dict]:
    from sqlalchemy import select
    Q = db.Question
    async with db.async_session() as session:
        stmt = select(Q).where(Q.subject == args.get("subject"), Q.mode == args.get("mode")).order_by(Q.id)
        if args.get("topic"):
            stmt = stmt.where(Q.topic == args["topic"])
        if args.get("text"):
            stmt = stmt.where(Q.question.ilike(f"%{str(args['text'])[:80]}%"))
        stmt = stmt.offset(int(args.get("offset") or 0)).limit(15)
        rows = (await session.execute(stmt)).scalars().all()
    return [{"id": q.id, "topic": q.topic, "type": q.qtype, "difficulty": q.difficulty, "min_plan": q.min_plan, "active": q.is_active,
             "figure": bool(q.figure_json), "question": q.question[:220]} for q in rows]


async def _tool_get(qid: int) -> dict:
    async with db.async_session() as session:
        q = await session.get(db.Question, qid)
    if q is None:
        return {"error": "topilmadi"}
    return {"id": q.id, "subject": q.subject, "mode": q.mode, "topic": q.topic, "type": q.qtype, "question": q.question,
            "options": json.loads(q.options_json or "[]"), "correct_index": q.correct_index, "explanation": q.explanation,
            "difficulty": q.difficulty, "min_plan": q.min_plan, "active": q.is_active, "has_figure": bool(q.figure_json), "grade": q.grade}


async def run_assistant(messages: list[dict]) -> dict:
    import ai_claude
    client = ai_claude._get_client()
    if client is None:
        return {"reply": "Claude kaliti sozlanmagan. Admin → AI holati sahifasida ANTHROPIC_API_KEY ni kiriting.", "actions": []}
    msgs = [{"role": "assistant" if m.get("role") == "assistant" else "user", "content": str(m.get("text", ""))[:4000]} for m in messages[-12:] if str(m.get("text", "")).strip()]
    if not msgs or msgs[-1]["role"] != "user":
        return {"reply": "Savol yozing.", "actions": []}
    actions: list[dict] = []
    started = time.monotonic()
    reply = ""
    for _ in range(8):
        if time.monotonic() - started > 48:
            reply = reply or "Vaqt tugadi — savolni qisqaroq/aniqroq bering."
            break
        try:
            resp = await asyncio.wait_for(client.messages.create(
                model=ai_keys.get("CLAUDE_MODEL", "claude-sonnet-5-5"), max_tokens=2500, system=ASSISTANT_SYSTEM, tools=_TOOLS, messages=msgs), timeout=40)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Yordamchi xatosi: %s", exc)
            reply = reply or "AI hozir javob bera olmadi. Birozdan so'ng qayta urinib ko'ring."
            break
        text_parts = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
        if text_parts:
            reply = "\n".join(text_parts)
        uses = [b for b in resp.content if getattr(b, "type", "") == "tool_use"]
        if not uses:
            break
        msgs.append({"role": "assistant", "content": [b.model_dump() if hasattr(b, "model_dump") else b for b in resp.content]})
        results = []
        for u in uses:
            a = u.input or {}
            try:
                if u.name == "bank_stats":
                    out = (await bank_overview())["table"]
                elif u.name == "topic_report":
                    out = await topic_report(str(a.get("subject")), str(a.get("mode")))
                elif u.name == "find_questions":
                    out = await _tool_find(a)
                elif u.name == "get_question":
                    out = await _tool_get(int(a.get("id")))
                elif u.name == "list_mocks":
                    out = [{"id": m.id, "subject": m.subject, "mode": m.mode, "name": m.name, "variant": m.variant_no, "active": m.is_active} for m in await db.list_mocks(active_only=False)]
                elif u.name.startswith("propose_"):
                    act = {"id": f"a{len(actions) + 1}", "type": u.name[len("propose_"):], "payload": a, "reason": str(a.get("reason", ""))[:400]}
                    actions.append(act)
                    out = {"ok": True, "staged": act["id"], "note": "Admin tasdig'ini kutmoqda"}
                else:
                    out = {"error": "noma'lum vosita"}
            except Exception as exc:  # noqa: BLE001
                out = {"error": str(exc)[:200]}
            results.append({"type": "tool_result", "tool_use_id": u.id, "content": json.dumps(out, ensure_ascii=False)[:12000]})
        msgs.append({"role": "user", "content": results})
    return {"reply": reply.strip() or "Tayyor.", "actions": actions}


async def apply_action(act: dict, admin: str) -> dict:
    t, p = act.get("type"), act.get("payload") or {}
    if t == "update_question":
        qid = int(p.get("id"))
        f = p.get("fields") or {}
        async with db.async_session() as session:
            q = await session.get(db.Question, qid)
            if q is None:
                raise HTTPException(status_code=404, detail="Savol topilmadi.")
            if "question" in f and str(f["question"]).strip():
                q.question = str(f["question"]).strip()[:2000]
            if "options" in f and isinstance(f["options"], list):
                opts = [str(o).strip() for o in f["options"]]
                if q.qtype != "open" and (len(opts) != 4 or len({o.lower() for o in opts}) != 4 or any(not o for o in opts)):
                    raise HTTPException(status_code=422, detail="4 ta turli variant kerak.")
                q.options_json = json.dumps(opts, ensure_ascii=False)
            if "accept" in f and q.qtype == "open" and isinstance(f["accept"], list):
                q.options_json = json.dumps([str(a).strip() for a in f["accept"] if str(a).strip()], ensure_ascii=False)
            if "correct_index" in f and q.qtype != "open":
                ci = int(f["correct_index"])
                if not 0 <= ci <= 3:
                    raise HTTPException(status_code=422, detail="correct_index 0-3 bo'lsin.")
                q.correct_index = ci
            for k, attr in (("explanation", "explanation"), ("topic", "topic")):
                if k in f:
                    setattr(q, attr, str(f[k])[:2000 if k == "explanation" else 150])
            if f.get("difficulty") in (1, 2, 3):
                q.difficulty = f["difficulty"]
            if f.get("min_plan") in (0, 1, 2):
                q.min_plan = f["min_plan"]
            if "is_active" in f:
                q.is_active = bool(f["is_active"])
            await session.commit()
        await db.log_admin_action(admin, "ai_update_question", f"#{qid}: {act.get('reason', '')[:120]}")
        return {"ok": True}
    if t == "delete_question":
        ok = await db.admin_delete_question(int(p.get("id")))
        await db.log_admin_action(admin, "ai_delete_question", f"#{p.get('id')}: {act.get('reason', '')[:120]}")
        return {"ok": bool(ok)}
    if t == "create_questions":
        subject, mode = str(p.get("subject")), str(p.get("mode"))
        if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE:
            raise HTTPException(status_code=422, detail="Fan/rejim noto'g'ri.")
        items = []
        for raw in p.get("questions") or []:
            qt = raw.get("qtype", "closed")
            r = {"type": qt, "question": raw.get("question"), "options": raw.get("options"), "answer": raw.get("correct_index") if qt == "closed" else raw.get("accept"),
                 "pairs": raw.get("pairs"), "explanation": raw.get("explanation"), "difficulty": raw.get("difficulty", 2), "topic": raw.get("topic") or p.get("topic")}
            it = _norm_ai_item(r, str(p.get("topic") or ""))
            if it:
                items.append(it)
        res = await commit_items(subject, mode, items, True, "AI yordamchi", admin=admin)
        return {"ok": True, **res}
    raise HTTPException(status_code=422, detail="Noma'lum amal.")


# --------------------------------------------------------------------------------------
# ROUTE'LAR
# --------------------------------------------------------------------------------------

def register(app, prefix: str, require_admin, current_admin_username, templates, import_modes) -> None:
    def guard(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")

    @app.get(f"{prefix}/studio", response_class=HTMLResponse)
    async def studio_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        changelog = ""
        p = os.path.join(BASE_DIR, "CHANGELOG.md")
        if os.path.exists(p):
            changelog = open(p, encoding="utf-8").read()[:14000]
        return templates.TemplateResponse(request, "admin_studio.html", {
            "active_tab": "studio", "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "changelog": changelog,
            "ai_ready": bool(ai_keys.get("ANTHROPIC_API_KEY") or ai_keys.get("GEMINI_API_KEY")),
            "claude_ready": bool(ai_keys.get("ANTHROPIC_API_KEY")),
        })

    @app.post(f"{prefix}/api/studio/extract")
    async def studio_extract(request: Request):
        guard(request)
        form = await request.form(max_files=40)
        ups = [u for u in form.getlist("file") if getattr(u, "filename", "")]
        if not ups:
            raise HTTPException(status_code=422, detail="Fayl tanlang.")
        docs = []
        for up in ups[:20]:
            data = await up.read()
            name = (up.filename or "fayl").replace("\\", "/").split("/")[-1][:120]
            if name.lower().endswith(".zip"):
                for n, blob, w in qimport.expand_zip(data, name):
                    if blob:
                        docs.append(await asyncio.to_thread(_extract_doc, n.split("/")[-1][:120], blob))
                continue
            docs.append(await asyncio.to_thread(_extract_doc, name, data))
        db_index = await db.admin_question_key_index()
        for d in docs:
            for it in d["regex_items"]:
                it["src"] = d["name"]
                it.setdefault("qtype", "closed")
                if it.get("difficulty") not in (1, 2, 3):
                    it["difficulty"] = 2
                it["topic"] = it.get("topic") or "Umumiy"
            _dup_info(d["regex_items"], db_index)
            # rasm (chizma) biriktirish: PDF chizmalari savol raqami bo'yicha
            if d["figures"]:
                for it in d["regex_items"]:
                    f = d["figures"].get(str(it.get("no")))
                    if f and not it.get("figure"):
                        it["figure"] = {"q": f, "o": [None] * 4}
            d["n_regex"] = len(d["regex_items"])
        return JSONResponse({"docs": docs})

    @app.post(f"{prefix}/api/studio/ai-parse")
    async def studio_ai_parse(request: Request):
        guard(request)
        body = await request.json()
        subject, mode = str(body.get("subject", "auto")), str(body.get("mode", "dtm"))
        text = str(body.get("text", ""))[:CHUNK_CHARS + 2000]
        if not text.strip():
            raise HTTPException(status_code=422, detail="Matn bo'sh.")
        snap = await _bank_snapshot(subject, mode)
        topics_note = "; ".join(f"{s}: {', '.join(t[:60])}" for s, t in snap.items() if t)[:3500]
        hint = str(body.get("hint", ""))[:300]
        user = (f"Fan: {db.SUBJECT_NAMES.get(subject, 'avtomatik aniqlang (fan kodi: ' + ', '.join(db.SUBJECT_CODES) + ')')}. Rejim: {mode}.\n"
                f"Mavjud mavzular ({'fan: mavzular'}): {topics_note}\nQo'shimcha ko'rsatma: {hint or '-'}\n"
                f"Agar fan 'avtomatik' bo'lsa, har savolga \"subject\" kodini ham qo'shing.\n\nHUJJAT MATNI:\n{text}")
        data = await ai_json(PARSE_SYSTEM, user, max_tokens=7000, timeout=52)
        if data is None:
            raise HTTPException(status_code=502, detail="AI javob bermadi (kalit/kredit/tarmoq). Qoida bo'yicha natijadan foydalaning.")
        if isinstance(data, dict):
            data = data.get("questions") or data.get("items") or []
        items = []
        for raw in data:
            it = _norm_ai_item(raw)
            if it:
                if isinstance(raw, dict) and raw.get("subject") in db.SUBJECT_CODES:
                    it["subject"] = raw["subject"]
                items.append(it)
        if any("[[IMG:" in (it["question"] + "".join(it.get("options", []))) for it in items):
            import question_figures
            question_figures.resolve_markers([it for it in items if it["qtype"] == "closed"])
        return JSONResponse({"items": items, "raw_count": len(data)})

    @app.post(f"{prefix}/api/studio/ai-vision")
    async def studio_ai_vision(request: Request):
        guard(request)
        form = await request.form()
        up = form.get("file")
        if up is None or not getattr(up, "filename", ""):
            raise HTTPException(status_code=422, detail="Fayl tanlang.")
        data = await up.read()
        if len(data) > 20 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="Fayl 20 MB dan oshmasin.")
        name = up.filename.lower()
        if name.endswith(".pdf"):
            block = {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": base64.b64encode(data).decode()}}
        else:
            mt = "image/png" if name.endswith(".png") else "image/webp" if name.endswith(".webp") else "image/gif" if name.endswith(".gif") else "image/jpeg"
            block = {"type": "image", "source": {"type": "base64", "media_type": mt, "data": base64.b64encode(data).decode()}}
        subject, mode = str(form.get("subject", "auto")), str(form.get("mode", "dtm"))
        snap = await _bank_snapshot(subject, mode)
        topics_note = "; ".join(f"{s}: {', '.join(t[:60])}" for s, t in snap.items() if t)[:3000]
        txt = {"type": "text", "text": f"Fan: {subject}. Rejim: {mode}. Mavjud mavzular: {topics_note}\nShu hujjat/rasmdagi barcha test savollarini ajrating. "
                                      f"Chizma/grafik/sxema bo'lsa, uni 'svg' maydonida OQ FONLI toza SVG qilib qayta chizing."}
        data_j = await ai_json(PARSE_SYSTEM, [block, txt], max_tokens=8000, timeout=55)
        if data_j is None:
            raise HTTPException(status_code=502, detail="AI ko'rish rejimi ishlamadi (Claude kaliti kerak; skaner PDF/rasm uchun).")
        if isinstance(data_j, dict):
            data_j = data_j.get("questions") or []
        items = [it for it in (_norm_ai_item(r) for r in data_j) if it]
        for it in items:
            it["src"] = up.filename[:150]
        return JSONResponse({"items": items})

    @app.post(f"{prefix}/api/studio/ai-generate")
    async def studio_ai_generate(request: Request):
        guard(request)
        body = await request.json()
        subject, mode, topic = str(body.get("subject", "")), str(body.get("mode", "")), str(body.get("topic", "")).strip()
        if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE or not topic:
            raise HTTPException(status_code=422, detail="Fan, rejim va mavzu kerak.")
        have = await _tool_find({"subject": subject, "mode": mode, "topic": topic})
        items = await ai_generate(subject, mode, topic, int(body.get("count", 8)), [h["question"] for h in have])
        db_index = await db.admin_question_key_index()
        _dup_info(items, db_index)
        return JSONResponse({"items": items})

    @app.post(f"{prefix}/api/studio/commit")
    async def studio_commit(request: Request):
        guard(request)
        body = await request.json()
        subject, mode = str(body.get("subject", "")), str(body.get("mode", ""))
        if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE:
            raise HTTPException(status_code=422, detail="Fan yoki rejim noto'g'ri.")
        items = body.get("items") or []
        if not isinstance(items, list) or len(items) > 800:
            raise HTTPException(status_code=422, detail="Savollar ro'yxati noto'g'ri (800 tagacha).")
        res = await commit_items(subject, mode, items, bool(body.get("publish", True)), str(body.get("mock_name") or "AI import"),
                                 str(body.get("tier") or "free"), current_admin_username(request))
        return JSONResponse(res)

    @app.get(f"{prefix}/api/studio/bank")
    async def studio_bank(request: Request):
        guard(request)
        return JSONResponse(await bank_overview())

    @app.get(f"{prefix}/api/studio/topics")
    async def studio_topics(request: Request, subject: str, mode: str):
        guard(request)
        if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE:
            raise HTTPException(status_code=422, detail="Noto'g'ri.")
        return JSONResponse({"topics": await topic_report(subject, mode)})

    @app.post(f"{prefix}/api/studio/seed")
    async def studio_seed(request: Request):
        guard(request)
        body = await request.json()
        res = await seed_step(int(body.get("step", 0)))
        if res.get("done"):
            await db.log_admin_action(current_admin_username(request), "seed", "Bazani yangilash tugadi")
        return JSONResponse(res)

    @app.get(f"{prefix}/api/studio/mocks")
    async def studio_mocks(request: Request):
        guard(request)
        ms = await db.list_mocks(active_only=False)
        return JSONResponse({"mocks": [{"id": m.id, "subject": db.SUBJECT_NAMES.get(m.subject, m.subject), "mode": m.mode, "name": m.name, "variant": m.variant_no,
                                        "total": len(json.loads(m.question_ids_json or "[]")), "min_plan": m.min_plan, "active": m.is_active,
                                        "date": m.created_at.strftime("%Y-%m-%d")} for m in ms]})

    @app.post(f"{prefix}/api/studio/mock/create")
    async def studio_mock_create(request: Request):
        guard(request)
        body = await request.json()
        subject, mode = str(body.get("subject", "")), str(body.get("mode", ""))
        if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE:
            raise HTTPException(status_code=422, detail="Fan yoki rejim noto'g'ri.")
        name = str(body.get("name") or "").strip()[:100] or f"{db.SUBJECT_NAMES.get(subject, subject)} mock"
        out = await build_mocks(subject, mode, name, int(body.get("variants", 2)), body.get("topics") or None,
                                int(body.get("min_plan", 1)), current_admin_username(request), int(body.get("time_minutes", 0)))
        return JSONResponse({"ok": True, "mocks": out})

    @app.post(f"{prefix}/api/studio/mock/{{mock_id}}/toggle")
    async def studio_mock_toggle(request: Request, mock_id: int):
        guard(request)
        body = await request.json()
        return JSONResponse({"ok": await db.set_mock_active(mock_id, bool(body.get("active")))})

    @app.post(f"{prefix}/api/studio/mock/{{mock_id}}/delete")
    async def studio_mock_delete(request: Request, mock_id: int):
        guard(request)
        ok = await db.delete_mock(mock_id)
        await db.log_admin_action(current_admin_username(request), "mock_delete", f"#{mock_id}")
        return JSONResponse({"ok": ok})

    @app.post(f"{prefix}/api/studio/assistant")
    async def studio_assistant(request: Request):
        guard(request)
        body = await request.json()
        return JSONResponse(await run_assistant(body.get("messages") or []))

    @app.post(f"{prefix}/api/studio/assistant/apply")
    async def studio_assistant_apply(request: Request):
        guard(request)
        body = await request.json()
        res = await apply_action(body.get("action") or {}, current_admin_username(request))
        return JSONResponse(res)
