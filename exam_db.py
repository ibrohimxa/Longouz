"""
LongoUZ — rasmiy imtihon tuzilmasi uchun ma'lumotlar bazasi so'rovlari:
sinf -> mavzu -> tarif, imtihonni (45 savollik sertifikat / DTM) bloklar va qiyinlik bo'yicha yig'ish,
10 mavzudan keyingi "xatolar ustida ishlash" testi va maxsus (qiyin / blok) mashqlar.
Shuningdek, tayyor savollar bazasini (content/ papkasi) bazaga bir martalik yuklaydi.
"""
from __future__ import annotations

import json
import logging
import random
import time

from sqlalchemy import select, func, delete as sa_delete

import database as db
import exam_rules as ER

logger = logging.getLogger(__name__)

# Tayyor kontent versiyasi: oshirilsa yangi savollar/mavzular qo'shiladi (mavjudlari qayta yozilmaydi).
CONTENT_VERSION = "v230q"

_KIND_OF = {"closed": "c", "open": "o", "match": "m"}


# ---------------------------------------------------------------------------
# MAVZU META (sinf / tarif)
# ---------------------------------------------------------------------------

async def get_topic_meta(subject: str, mode: str) -> list[dict]:
    async with db.async_session() as session:
        rows = (await session.execute(
            select(db.TopicMeta).where(db.TopicMeta.subject == subject, db.TopicMeta.mode == mode)
            .order_by(db.TopicMeta.order_no, db.TopicMeta.id)
        )).scalars().all()
    return [{"topic": r.topic, "code": r.code, "grade": r.grade, "tier": r.tier, "order": r.order_no, "block": r.block}
            for r in rows]


async def get_topic_tier(subject: str, mode: str, topic: str) -> str | None:
    async with db.async_session() as session:
        row = (await session.execute(
            select(db.TopicMeta.tier).where(db.TopicMeta.subject == subject, db.TopicMeta.mode == mode,
                                            db.TopicMeta.topic == topic).limit(1)
        )).scalar_one_or_none()
    return row


async def count_visible_by_topic(subject: str, mode: str, plan: str) -> dict[str, int]:
    """Foydalanuvchi tarifi ko'ra oladigan savollar soni (mavzu bo'yicha)."""
    rank = ER.plan_rank(plan)
    max_diff = ER.TIER_PRACTICE.get(plan, ER.TIER_PRACTICE["free"])["max_difficulty"]
    async with db.async_session() as session:
        res = await session.execute(
            select(db.Question.topic, func.count(db.Question.id))
            .where(db.Question.subject == subject, db.Question.mode == mode, db.Question.is_active == True,  # noqa: E712
                   db.Question.min_plan <= rank, db.Question.difficulty <= max_diff)
            .group_by(db.Question.topic)
        )
        return {t: c for t, c in res.all()}


# ---------------------------------------------------------------------------
# SAVOL TANLASH YORDAMCHILARI
# ---------------------------------------------------------------------------

def _unique(rows):
    seen: set[str] = set()
    out = []
    for q in rows:
        k = db._norm_text(q.question)
        if k in seen:
            continue
        seen.add(k)
        out.append(q)
    return out


def _balanced_pick(rows: list, count: int) -> list:
    """Qiyinlik bo'yicha muvozanatli tanlash: oson / o'rta / qiyin navbatma-navbat, so'ng oson -> qiyin tartibida."""
    groups: dict[int, list] = {1: [], 2: [], 3: []}
    for q in rows:
        groups[q.difficulty if q.difficulty in (1, 2, 3) else 2].append(q)
    for g in groups.values():
        random.shuffle(g)
    picked: list = []
    order = [1, 2, 3, 2]
    i = 0
    while len(picked) < count and any(groups.values()):
        g = groups[order[i % len(order)]]
        if g:
            picked.append(g.pop())
        i += 1
    picked.sort(key=lambda q: (q.difficulty if q.difficulty in (1, 2, 3) else 2))
    return picked


async def _fetch(subject: str, mode: str, plan: str, topics: list[str] | None = None, extra=None) -> list:
    rank = ER.plan_rank(plan)
    q = select(db.Question).where(
        db.Question.subject == subject, db.Question.mode == mode, db.Question.is_active == True,  # noqa: E712
        db.Question.min_plan <= rank,
    )
    if topics:
        q = q.where(db.Question.topic.in_(topics))
    if extra is not None:
        q = q.where(extra)
    async with db.async_session() as session:
        return list((await session.execute(q)).scalars().all())


async def topic_practice_questions(
    subject: str, mode: str, topic: str, plan: str, count: int, exclude_keys: set[str] | None = None,
) -> tuple[list[dict], int]:
    """Mavzu bo'yicha mashq. Tarifga qarab qiyinlik chegarasi: Bepul — oson/o'rta; Pro/Ultra — barchasi.
    Qaytadi: (savollar, tarifga ko'rinadigan jami savollar soni)."""
    max_diff = ER.TIER_PRACTICE.get(plan, ER.TIER_PRACTICE["free"])["max_difficulty"]
    rows = await _fetch(subject, mode, plan, [topic], db.Question.difficulty <= max_diff)
    rows = _unique(rows)
    pool_total = len(rows)
    if exclude_keys:
        fresh = [q for q in rows if db.make_question_key(q.question) not in exclude_keys]
        if len(fresh) >= min(count, len(rows)):
            rows = fresh
        elif fresh:
            # yangi savollar yetmasa — yangilarini birinchi, qolganini eskilardan to'ldiramiz
            old = [q for q in rows if q not in fresh]
            random.shuffle(old)
            rows = fresh + old
    picked = _balanced_pick(rows, count)
    return [db._question_to_dict(q) for q in picked], pool_total


# ---------------------------------------------------------------------------
# TO'LIQ IMTIHON (45 savollik sertifikat, 40 savollik DTM tarix, 30 savollik biologiya)
# ---------------------------------------------------------------------------

def _cell_predicate(use_db_block: bool, block: str, diff: int, kind: str):
    def pred(q) -> bool:
        k = _KIND_OF.get(q.qtype or "closed", "c")
        if kind == "m":
            if k != "m":
                return False
        elif k != kind:
            return False
        d = q.difficulty if q.difficulty in (1, 2, 3) else 2
        if d != diff:
            return False
        if use_db_block:
            return (q.block or "siyosiy") == block
        return (q.block or "siyosiy") != "moslash" or kind == "m"
    return pred


def _fallbacks(use_db_block: bool, block: str, diff: int, kind: str):
    """Aniq katak yetmaganda yumshatilgan qoidalar (ball baribir savolning o'z qiyinligi bo'yicha hisoblanadi)."""
    yield _cell_predicate(use_db_block, block, diff, kind)
    # shu blok, qo'shni qiyinlik, shu tur
    for d2 in (2, 1, 3):
        if d2 != diff:
            yield _cell_predicate(use_db_block, block, d2, kind)
    # shu qiyinlik, boshqa blok
    yield _cell_predicate(False, block, diff, kind)
    for d2 in (2, 1, 3):
        yield _cell_predicate(False, block, d2, kind)
    if kind != "c":
        yield _cell_predicate(False, block, diff, "c")
        yield _cell_predicate(False, block, 2, "c")


async def assemble_exam(subject: str, mode: str, plan: str, variant: str = "main",
                        exclude_ids: set[int] | None = None, topics: list[str] | None = None) -> list[dict]:
    """Rasmiy tuzilma bo'yicha to'liq imtihon yig'adi (ExamRules.cells). Har bir savolga 'section' belgisi qo'shiladi.
    exclude_ids — mock-variantlar bir-birini takrorlamasligi uchun; topics — faqat shu mavzulardan."""
    cfg = ER.tiered_config(subject, mode)
    if cfg is None:
        return []
    rows = _unique(await _fetch(subject, mode, plan, topics) if topics else await _fetch(subject, mode, plan))
    if exclude_ids:
        fresh = [q for q in rows if q.id not in exclude_ids]
        rows = fresh + [q for q in rows if q.id in exclude_ids]  # yetmasa, oxirida takrorlangani ham ishlatiladi
    random.shuffle(rows)
    if exclude_ids:
        rows.sort(key=lambda q: q.id in exclude_ids)  # barqaror: yangilari oldinda
    use_db_block = cfg is ER.HISTORY_CERT
    used: set[int] = set()
    out: list[dict] = []
    for block, diff, kind, n in cfg["cells"]:
        got: list = []
        for pred in _fallbacks(use_db_block, block, diff, kind):
            for q in rows:
                if len(got) >= n:
                    break
                if q.id in used or not pred(q):
                    continue
                used.add(q.id)
                got.append(q)
            if len(got) >= n:
                break
        for q in got:
            d = db._question_to_dict(q)
            d["section"] = block
            out.append(d)
    # Yetishmagan bo'lsa (bank hali kichik) — qolgan savollar bilan umumiy sonni to'ldiramiz
    total = cfg["total"]
    if len(out) < total:
        rest = [q for q in rows if q.id not in used]
        for q in rest[: total - len(out)]:
            d = db._question_to_dict(q)
            d["section"] = cfg["cells"][-1][0]
            out.append(d)
    # blok tartibini saqlab, blok ichida oson -> qiyin
    order = {}
    for i, (b, *_rest) in enumerate(cfg["cells"]):
        order.setdefault(b, i)
    if len(order) == 1 and "" in order:
        # blok yo'q (biologiya, kimyo, fizika, ona tili): avval yopiq, so'ng moslashtirish, so'ng ochiq; ichida oson -> qiyin
        rank = {"closed": 0, "match": 1, "open": 2}
        out.sort(key=lambda d: (rank.get(d.get("qtype") or "closed", 0), d.get("difficulty") or 2))
    else:
        out.sort(key=lambda d: (order.get(d["section"], 99), d.get("difficulty") or 2))
    return out


# ---------------------------------------------------------------------------
# NAZORAT TESTI (har 10 mavzudan keyin: o'zi xato qilgan savollar)
# ---------------------------------------------------------------------------

async def checkpoint_questions(user_id: int, subject: str, mode: str, topics: list[str], plan: str,
                               count: int = ER.NAZORAT_COUNT) -> tuple[list[dict], int]:
    """Foydalanuvchi shu mavzularda sayt ichida xato qilgan savollarni birinchi beradi; yetmasa shu mavzulardan
    yangi savollar bilan to'ldiradi. Qaytadi: (savollar, xato savollar soni)."""
    rank = ER.plan_rank(plan)
    missed: list[dict] = []
    async with db.async_session() as session:
        rows = (await session.execute(
            select(db.MissedQuestion).where(
                db.MissedQuestion.user_id == user_id, db.MissedQuestion.subject == subject,
                db.MissedQuestion.mode == mode, db.MissedQuestion.topic.in_(topics),
            ).order_by(db.MissedQuestion.missed_count.desc(), db.MissedQuestion.created_at.desc()).limit(count)
        )).scalars().all()
    for r in rows:
        try:
            q = json.loads(r.question_json)
        except ValueError:
            continue
        if (q.get("min_plan") or 0) > rank:
            continue
        q["_missed_topic"] = r.topic
        q.setdefault("topic", r.topic)
        missed.append(q)
    out = missed[:count]
    if len(out) < count:
        have = {db._norm_text(q.get("question", "")) for q in out}
        pool = [q for q in _unique(await _fetch(subject, mode, plan, topics,
                                                db.Question.difficulty <= ER.TIER_PRACTICE.get(plan, ER.TIER_PRACTICE["free"])["max_difficulty"]))
                if db._norm_text(q.question) not in have]
        for q in _balanced_pick(pool, count - len(out)):
            out.append(db._question_to_dict(q))
    return out, len(missed)


# ---------------------------------------------------------------------------
# MAXSUS MASHQLAR (Qiyin savollar — Ultra; Blok bo'yicha — Pro/Ultra)
# ---------------------------------------------------------------------------

async def drill_questions(subject: str, mode: str, plan: str, kind: str, topics: list[str] | None = None,
                          count: int = 25) -> list[dict]:
    """Maxsus mashq: faqat foydalanuvchi uchun OCHIQ mavzulardan (topics) tanlanadi."""
    if not topics:
        return []
    if kind == "hard":
        rows = await _fetch(subject, mode, plan, topics, db.Question.difficulty == 3)
    elif kind.startswith("block:"):
        rows = await _fetch(subject, mode, plan, topics, db.Question.block == kind.split(":", 1)[1])
    elif kind == "open":
        rows = await _fetch(subject, mode, plan, topics, db.Question.qtype == "open")
    else:
        return []
    rows = _unique(rows)
    random.shuffle(rows)
    return [db._question_to_dict(q) for q in rows[:count]]


# ---------------------------------------------------------------------------
# TAYYOR KONTENTNI BIR MARTALIK YUKLASH
# ---------------------------------------------------------------------------

def pack_keep_keys(packs: list[dict]) -> dict:
    """(fan, rejim) -> shu juftlikka tegishli BARCHA paketlardagi savol matnlari (bir fan bir nechta paketdan iborat bo'lishi mumkin)."""
    keep: dict = {}
    for pack in packs:
        for mode in pack["modes"]:
            keep.setdefault((pack["subject"], mode), set()).update(q["question"].strip().lower() for q in pack["questions"])
    return keep


async def seed_exam_content() -> None:
    flag = f"seed_exam_content_{CONTENT_VERSION}"
    if await db.get_setting(flag, "") == "1":
        return
    try:
        import content
    except ImportError:
        logger.warning("content/ paketi topilmadi — tayyor savollar yuklanmadi.")
        return
    packs = content.load_packs()
    keep = pack_keep_keys(packs)
    added_total = 0
    for pack in packs:
        subject = pack["subject"]
        for mode in pack["modes"]:
            added_total += await _seed_pack(subject, mode, pack["topics"], pack["questions"], keep[(subject, mode)])
    await db.set_setting(flag, "1")
    logger.info("Tayyor savollar bazasi yuklandi: %s ta yangi savol.", added_total)


async def seed_step(budget: float = 40.0) -> dict:
    """Serverless (Vercel) uchun BO'LAKLAB yuklash: har chaqiruv vaqt byudjeti ichida bir nechta paketni yuklaydi,
    qolganini keyingi chaqiruv davom ettiradi. Natija: {"done": bool, "left": N, "added": N}."""
    ver = CONTENT_VERSION
    flag = f"seed_exam_content_{ver}"
    if await db.get_setting(flag, "") == "1":
        return {"done": True, "left": 0, "added": 0}
    try:
        import content
    except ImportError:
        return {"done": True, "left": 0, "added": 0}
    if not await db.claim_lock("seed_lock", ttl=70):
        return {"done": False, "left": -1, "added": 0, "busy": True}
    started = time.monotonic()
    packs = content.load_packs()
    keep = pack_keep_keys(packs)
    added_total = 0
    left = 0
    try:
        for idx, pack in enumerate(packs):
            subject = pack["subject"]
            for mode in pack["modes"]:
                key = f"seedpack_{ver}_{idx}_{subject}_{mode}"
                if await db.get_setting(key, "") == "1":
                    continue
                if time.monotonic() - started > budget:
                    left += 1
                    continue
                added_total += await _seed_pack(subject, mode, pack["topics"], pack["questions"], keep[(subject, mode)])
                await db.set_setting(key, "1")
        if left == 0:
            await db.set_setting(flag, "1")
            logger.info("Tayyor savollar bazasi bo'laklab yuklandi (+%s).", added_total)
    finally:
        await db.release_lock("seed_lock")
    return {"done": left == 0, "left": left, "added": added_total}


async def _seed_pack(subject: str, mode: str, topics: list[dict], questions: list[dict], keep_keys: set | None = None) -> int:
    async with db.async_session() as session:
        existing_rows = {}
        for row in (await session.execute(
                select(db.Question).where(db.Question.subject == subject, db.Question.mode == mode))).scalars().all():
            existing_rows.setdefault(str(row.question).strip().lower(), row)
        existing_texts = set(existing_rows)
        tomb = {k for (k,) in (await session.execute(
            select(db.DeletedQuestion.question_key).where(db.DeletedQuestion.subject == subject,
                                                          db.DeletedQuestion.mode == mode)
        )).all()}
        have_meta = {t for (t,) in (await session.execute(
            select(db.TopicMeta.topic).where(db.TopicMeta.subject == subject, db.TopicMeta.mode == mode)
        )).all()}
        for i, t in enumerate(topics, start=1):
            if t["name"] in have_meta:
                await session.execute(
                    db.TopicMeta.__table__.update().where(
                        db.TopicMeta.subject == subject, db.TopicMeta.mode == mode, db.TopicMeta.topic == t["name"]
                    ).values(code=t["code"], grade=t["grade"], tier=t["tier"], order_no=i, block=t.get("block", "siyosiy"))
                )
            else:
                session.add(db.TopicMeta(subject=subject, mode=mode, topic=t["name"], code=t["code"], grade=t["grade"],
                                         tier=t["tier"], order_no=i, block=t.get("block", "siyosiy")))
        added = 0
        pack_keys = set()
        synced = 0
        for q in questions:
            text = q["question"].strip()
            pack_keys.add(text.lower())
            row = existing_rows.get(text.lower())
            if row is not None:
                # Tayyor bank qatori: mavzu / tarif / javob / chizma yangi versiyaga moslanadi (eski xato biriktirishlar tuzaladi)
                if row.source_file == "longouz-bank":
                    new_opts = json.dumps(q["options"], ensure_ascii=False)
                    new_vals = dict(topic=q["topic"], grade=q.get("grade", 0), difficulty=q.get("difficulty", 2), block=q.get("block", ""),
                                    qtype=q.get("qtype", "closed"), min_plan=q.get("min_plan", 0), options_json=new_opts,
                                    correct_index=q["correct_index"], explanation=q.get("explanation", ""),
                                    figure_json=q.get("figure_json", ""))
                    changed = False
                    for k, v in new_vals.items():
                        if getattr(row, k) != v:
                            setattr(row, k, v)
                            changed = True
                    if not row.is_active and db.make_question_key(text) not in tomb:
                        row.is_active = True
                        changed = True
                    synced += changed
                continue
            if db.make_question_key(text) in tomb:
                continue
            existing_texts.add(text.lower())
            session.add(db.Question(
                subject=subject, mode=mode, topic=q["topic"], mock_test="LongoUZ bazasi", question=text,
                options_json=json.dumps(q["options"], ensure_ascii=False), correct_index=q["correct_index"],
                explanation=q.get("explanation", ""), is_active=True, grade=q.get("grade", 0),
                difficulty=q.get("difficulty", 2), block=q.get("block", ""), qtype=q.get("qtype", "closed"),
                min_plan=q.get("min_plan", 0), figure_json=q.get("figure_json", ""), source_file="longouz-bank",
            ))
            added += 1
        # Paketdan olib tashlangan (eski/xato) tayyor-bank savollari nofaol qilinadi — faqat paket to'liq yuklangan bo'lsa
        keep = keep_keys if keep_keys is not None else pack_keys
        if len(keep) >= 20:
            for key, row in existing_rows.items():
                if row.source_file == "longouz-bank" and key not in keep and row.is_active:
                    row.is_active = False
                    synced += 1
        await session.commit()
    if synced:
        logger.info("Tayyor bank yangilandi (%s/%s): %s ta savol moslashtirildi.", subject, mode, synced)
    return added
