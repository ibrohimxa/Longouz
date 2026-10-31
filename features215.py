"""LongoUZ v215: DTM blok mock, AI-adaptiv test, chuqur analitika va ball prognozi, imtihon yo'riqnomasi.

main.py oxirida `features215.register(app, ...)` bilan ulanadi.
"""
from __future__ import annotations

import json
import logging
import random
import uuid
from collections import defaultdict
from datetime import datetime, timedelta

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel, Field
from sqlalchemy import select

import database as db
import exam_db
import exam_rules

logger = logging.getLogger(__name__)

# Rasmiy DTM (2025/2026): 180 daqiqa; 30 ta majburiy (ona tili, matematika, tarix — 10 tadan, har biri 1,1 ball),
# 1-ixtisoslik fani 30 ta (3,1 ball), 2-ixtisoslik fani 30 ta (2,1 ball). Maksimal ball 189.
MANDATORY = [("native", 10), ("math", 10), ("history", 10)]
COEF_MANDATORY, COEF_SPEC1, COEF_SPEC2 = 1.1, 3.1, 2.1
BLOCK_TOTAL = 90
BLOCK_MINUTES = 180
MAX_BALL = round(30 * COEF_MANDATORY + 30 * COEF_SPEC1 + 30 * COEF_SPEC2, 1)  # 189.0
SUBJECT_ORDER = ["native", "math", "history", "english", "russian", "physics", "chemistry", "biology"]


def _name(code: str) -> str:
    return db.SUBJECT_NAMES.get(code, code)


# ---------------------------------------------------------------- BLOK MOCK
def _hardness(q) -> float:
    """Savol qiyinligi bahosi: belgilangan qiyinlik + hisob-kitob/matn murakkabligi."""
    d = q.difficulty if q.difficulty in (1, 2, 3) else 2
    text = q.question or ""
    score = d * 100.0
    score += min(len(text), 260) / 13.0                      # uzun shart — ko'p bosqichli masala
    score += 6 if any(ch.isdigit() for ch in text) else 0     # hisoblash
    score += 5 if (q.figure_json or "") else 0                # chizma/jadval
    score += 4 if any(w in text.lower() for w in ("noto'g'ri", "barcha", "qaysi biri emas", "ketma-ketlik", "juftlik", "mos keladi")) else 0
    return score + random.random() * 8                        # bir xil variant chiqmasligi uchun


async def _seen_block_ids(user_id: int | None) -> set[int]:
    """Foydalanuvchining oldingi blok mocklarida tushgan savollar — yangi mockda oxiriga suriladi."""
    if not user_id:
        return set()
    seen: set[int] = set()
    try:
        async with db.async_session() as session:
            rows = (await session.execute(
                select(db.WebQuizLog.questions_json).where(db.WebQuizLog.user_id == user_id,
                                                           db.WebQuizLog.topic.like("DTM blok mock%"))
                .order_by(db.WebQuizLog.id.desc()).limit(6)
            )).all()
        for (qj,) in rows:
            for q in json.loads(qj or "[]"):
                if isinstance(q, dict) and isinstance(q.get("id"), int):
                    seen.add(q["id"])
    except Exception:  # noqa: BLE001 — tarix bo'lmasa ham mock ishlayveradi
        logger.debug("blok mock tarixi o'qilmadi", exc_info=True)
    return seen


def _pick_hard(rows: list, n: int, seen: set[int]) -> list:
    """Eng qiyin savollar: avval qiyinlik 3, so'ng 2 (1 — faqat yetmasa). Mavzular bo'yicha tarqatiladi."""
    closed = [q for q in rows if (q.qtype or "closed") == "closed"]
    pool = closed if len(closed) >= n else closed + [q for q in rows if (q.qtype or "closed") != "closed"]
    scored = sorted(pool, key=lambda q: (q.id in seen, -_hardness(q)))
    topics = {q.topic for q in scored}
    per_topic_cap = max(1, -(-n // max(1, len(topics))) + 1)
    got, per = [], defaultdict(int)
    for strict in (True, False):
        for q in scored:
            if len(got) >= n:
                break
            if q in got:
                continue
            if strict and (per[q.topic] >= per_topic_cap or (q.difficulty or 2) < 2):
                continue
            got.append(q)
            per[q.topic] += 1
    # blok ichida: o'rta -> qiyin (haqiqiy imtihondagi kabi qiyinlik oshib boradi)
    got.sort(key=lambda q: _hardness(q))
    return got


async def block_questions(plan: str, spec1: str, spec2: str, user_id: int | None = None) -> list[dict]:
    """Majburiy 3 fandan 10 tadan + 2 ixtisoslik fanidan 30 tadan (jami 90). Har fandan ENG QIYIN savollar olinadi."""
    plan_cells = [(s, n, COEF_MANDATORY, "majburiy") for s, n in MANDATORY]
    plan_cells += [(spec1, 30, COEF_SPEC1, "1-ixtisoslik"), (spec2, 30, COEF_SPEC2, "2-ixtisoslik")]
    seen = await _seen_block_ids(user_id)
    used: set[int] = set()
    out: list[dict] = []
    for subject, n, coef, role in plan_cells:
        # Blok mock — to'liq imtihon simulyatsiyasi: tarifdan qat'i nazar butun bankdan (eng qiyinlari) olinadi
        rows = [q for q in exam_db._unique(await exam_db._fetch(subject, "dtm", "ultra")) if q.id not in used]
        got = _pick_hard(rows, n, seen)
        used.update(q.id for q in got)
        for q in got:
            d = db._question_to_dict(q)
            d["section"] = f"{_name(subject)} · {role} (×{coef})".replace(".", ",")
            d["_subject"] = subject
            d["_coef"] = coef
            d["_role"] = role
            out.append(d)
    return out


def score_block(graded: list[dict], specs: list[str]) -> dict:
    """graded: [{is_correct, subject, coef, role}] -> rasmiy DTM ball (maks. 189)."""
    per: dict[tuple, dict] = {}
    order: list[tuple] = []
    for g in graded:
        key = (g.get("subject"), g.get("role"))
        if key not in per:
            per[key] = {"correct": 0, "total": 0, "coef": g.get("coef") or 1.0}
            order.append(key)
        per[key]["total"] += 1
        per[key]["correct"] += 1 if g.get("is_correct") else 0
    blocks, ball, correct, total = [], 0.0, 0, 0
    for key in order:
        p = per[key]
        subj, role = key
        b = round(p["correct"] * p["coef"], 1)
        mx = round({"majburiy": 10, "1-ixtisoslik": 30, "2-ixtisoslik": 30}.get(role, p["total"]) * p["coef"], 1)
        blocks.append({"name": f"{_name(subj)} ({role})", "correct": p["correct"], "total": p["total"], "ball": b, "max": mx})
        ball += b
        correct += p["correct"]
        total += p["total"]
    ball = round(ball, 1)
    return {
        "mode": "dtm", "official": True, "full_mock": True, "block_mock": True,
        "correct": correct, "total": total, "percent": round(correct / total * 100, 1) if total else 0.0,
        "ball": ball, "max_ball": MAX_BALL, "label": f"{ball} / {MAX_BALL:g} ball", "blocks": blocks,
    }


# ---------------------------------------------------------------- ANALITIKA
def _pct(c: int, t: int) -> float:
    return round(c / t * 100, 1) if t else 0.0


async def user_analytics(user_id: int) -> dict:
    async with db.async_session() as session:
        logs = list((await session.execute(
            select(db.WebQuizLog).where(db.WebQuizLog.user_id == user_id).order_by(db.WebQuizLog.created_at.desc()).limit(400)
        )).scalars().all())
        progress = list((await session.execute(
            select(db.TopicProgress).where(db.TopicProgress.user_id == user_id)
        )).scalars().all())
    logs_sorted = sorted(logs, key=lambda l: l.created_at)
    by_subject: dict[str, dict] = {}

    def _parts(l):
        """Oddiy test — bitta qism; blok mock — har bir fan alohida hisoblanadi (aks holda 90 savol bitta fanga yozilib qoladi)."""
        if (l.topic or "").startswith("DTM blok mock") and l.questions_json:
            try:
                agg: dict[str, list] = {}
                for q in json.loads(l.questions_json):
                    a = agg.setdefault(q.get("_subject") or l.subject, [0, 0])
                    a[1] += 1
                    a[0] += 1 if q.get("is_correct") else 0
                return [(sub, c, t, 0) for sub, (c, t) in agg.items()]
            except (ValueError, TypeError):
                pass
        return [(l.subject, l.correct_count or 0, l.total_count or 0, l.time_spent_seconds or 0)]

    for l in logs_sorted:
        for sub, c, t, secs in _parts(l):
            if t < 3:
                continue
            s = by_subject.setdefault(sub, {"attempts": 0, "correct": 0, "total": 0, "recent": [], "seconds": 0})
            s["attempts"] += 1
            s["correct"] += c
            s["total"] += t
            s["seconds"] += secs
            s["recent"].append(_pct(c, t))
    subjects = []
    for code in SUBJECT_ORDER:
        s = by_subject.get(code)
        if not s:
            subjects.append({"code": code, "name": _name(code), "attempts": 0, "total": 0, "correct": 0, "percent": 0.0,
                             "forecast": None, "trend": 0.0})
            continue
        rec = s["recent"][-5:]
        weights = list(range(1, len(rec) + 1))
        forecast = round(sum(r * w for r, w in zip(rec, weights)) / sum(weights), 1) if rec else None
        older = s["recent"][-10:-5]
        trend = round((sum(rec) / len(rec)) - (sum(older) / len(older)), 1) if rec and older else 0.0
        subjects.append({"code": code, "name": _name(code), "attempts": s["attempts"], "total": s["total"], "correct": s["correct"],
                         "percent": _pct(s["correct"], s["total"]), "forecast": forecast, "trend": trend,
                         "minutes": round(s["seconds"] / 60)})
    # haftalik progress (oxirgi 7 kun)
    today = datetime.utcnow().date()
    days = {today - timedelta(days=i): {"c": 0, "t": 0} for i in range(6, -1, -1)}
    for l in logs:
        d = l.created_at.date() if l.created_at else None
        if d in days:
            days[d]["c"] += l.correct_count or 0
            days[d]["t"] += l.total_count or 0
    weekday_names = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
    weekly = [{"day": weekday_names[d.weekday()], "date": d.isoformat(), "total": v["t"], "percent": _pct(v["c"], v["t"])} for d, v in days.items()]
    this_week = sum(w["total"] for w in weekly)
    # kuchsiz mavzular: mavzu bo'yicha oxirgi urinishlar
    topic_stats: dict[tuple, dict] = {}
    for l in logs_sorted:
        t = (l.topic or "").strip()
        if not t or t.startswith("__") or (l.total_count or 0) < 3 or t.startswith(("DTM", "Mock", "Nazorat", "Adaptiv")):
            continue
        k = (l.subject, t)
        e = topic_stats.setdefault(k, {"c": 0, "t": 0, "n": 0})
        e["c"] += l.correct_count or 0
        e["t"] += l.total_count or 0
        e["n"] += 1
    weak = sorted(
        [{"subject": s, "subject_name": _name(s), "topic": t, "percent": _pct(e["c"], e["t"]), "total": e["t"], "attempts": e["n"]}
         for (s, t), e in topic_stats.items() if e["t"] >= 5],
        key=lambda x: (x["percent"], -x["total"]))[:8]
    strong = sorted(
        [{"subject": s, "subject_name": _name(s), "topic": t, "percent": _pct(e["c"], e["t"]), "total": e["t"]}
         for (s, t), e in topic_stats.items() if e["t"] >= 5], key=lambda x: (-x["percent"], -x["total"]))[:5]
    completed = sum(1 for p in progress if p.completed)
    total_q = sum(l.total_count or 0 for l in logs)
    total_c = sum(l.correct_count or 0 for l in logs)
    return {
        "overview": {"attempts": len(logs), "questions": total_q, "accuracy": _pct(total_c, total_q), "this_week": this_week,
                     "topics_done": completed, "minutes": round(sum(l.time_spent_seconds or 0 for l in logs) / 60)},
        "subjects": subjects, "weekly": weekly, "weak": weak, "strong": strong,
        "weights": {"mandatory": {"coef": COEF_MANDATORY, "count": 10}, "spec1": {"coef": COEF_SPEC1, "count": 30},
                    "spec2": {"coef": COEF_SPEC2, "count": 30}, "max": MAX_BALL},
        "mandatory": [s for s, _ in MANDATORY],
    }


# ---------------------------------------------------------------- YO'RIQNOMA
GUIDE_SUBJECTS = ["native", "math", "history", "english", "russian", "physics", "chemistry", "biology"]


async def guide_data() -> list[dict]:
    out = []
    for code in GUIDE_SUBJECTS:
        modes = []
        for mode in ("dtm", "certificate"):
            try:
                meta = await exam_db.get_topic_meta(code, mode)
            except Exception:  # noqa: BLE001
                meta = []
            if not meta:
                continue
            cfg = exam_rules.tiered_config(code, mode)
            by_grade: dict[int, list] = defaultdict(list)
            for m in meta:
                by_grade[int(m.get("grade") or 0)].append(m["topic"])
            modes.append({
                "mode": mode, "mode_name": "DTM" if mode == "dtm" else "Milliy sertifikat",
                "format": (cfg or {}).get("name", ""), "total": (cfg or {}).get("total"), "time": (cfg or {}).get("time"),
                "topics_total": len(meta),
                "grades": [{"grade": g, "count": len(v), "topics": v} for g, v in sorted(by_grade.items())],
            })
        out.append({"code": code, "name": _name(code), "modes": modes})
    return out


# ---------------------------------------------------------------- ADAPTIV
def _level_pick(pool: dict[int, list[int]], used: set[int], level: int) -> int | None:
    for lv in sorted((1, 2, 3), key=lambda x: (abs(x - level), x)):
        cand = [i for i in pool.get(lv, []) if i not in used]
        if cand:
            return random.choice(cand)
    return None


class BlockRequest(BaseModel):
    specs: list[str] = Field(..., min_length=2, max_length=2)
    attempt_token: str = Field(..., min_length=8, max_length=64)


class AdaptiveStart(BaseModel):
    subject: str
    mode: str = "dtm"
    topic: str | None = None
    total: int = Field(20, ge=5, le=40)
    attempt_token: str = Field(..., min_length=8, max_length=64)


class AdaptiveNext(BaseModel):
    attempt_token: str = Field(..., min_length=8, max_length=64)
    index: int = Field(..., ge=0, le=100)
    answer: int | str | None = None



async def bank_status():
    """Har fan/rejim/mavzu bo'yicha savollar soni va kvotadan (25/60/125) kamchilik."""
    from sqlalchemy import select, func
    import database as _db
    async with _db.async_session() as session:
        rows = (await session.execute(
            select(_db.Question.subject, _db.Question.mode, _db.Question.topic, _db.Question.min_plan, func.count(_db.Question.id))
            .where(_db.Question.is_active == True).group_by(_db.Question.subject, _db.Question.mode, _db.Question.topic, _db.Question.min_plan)  # noqa: E712
        )).all()
    agg = {}
    for subj, mode, topic, mp, c in rows:
        d = agg.setdefault((subj, mode, topic), [0, 0, 0])
        d[min(int(mp or 0), 2)] += c
    # Bir mavzu bir nechta rejimda (dtm + sertifikat) bir xil savollar bilan turadi — ikki marta sanalmasin
    merged: dict = {}
    for (subj, mode, topic), vals in agg.items():
        cur = merged.get((subj, topic))
        if cur is None:
            merged[(subj, topic)] = [mode, vals]
        else:
            cur[0] = cur[0] + "/" + mode if mode not in cur[0].split("/") else cur[0]
            if sum(vals) > sum(cur[1]):
                cur[1] = vals
    agg = {(subj, m, topic): v for (subj, topic), (m, v) in merged.items()}
    subjects = {}
    for (subj, mode, topic), (f, p_, u) in agg.items():
        tot = f + p_ + u
        sd = subjects.setdefault(subj, {"subject": subj, "topics": 0, "total": 0, "need": 0, "short": 0, "rows": []})
        sd["topics"] += 1
        sd["total"] += tot
        need = max(0, 125 - tot)
        sd["need"] += need
        if need:
            sd["short"] += 1
        sd["rows"].append({"mode": mode, "topic": topic, "free": f, "pro": p_, "ultra": u, "total": tot, "need": need})
    for sd in subjects.values():
        sd["rows"].sort(key=lambda r: (-r["need"], r["topic"]))
    return {"targets": {"free": 25, "pro": 60, "ultra": 125}, "subjects": sorted(subjects.values(), key=lambda x: -x["need"])}


def register(app, get_current_user, templates, limiter, shuffle_question_options, public_question):
    def _login_redirect(request: Request):
        q = f"?{request.url.query}" if request.url.query else ""
        return RedirectResponse(f"/login?next={request.url.path}{q}", status_code=302)

    # ---------- sahifalar
    @app.get("/dtm-blok", response_class=HTMLResponse)
    async def block_page(request: Request):
        user = await get_current_user(request)
        if user is None:
            return _login_redirect(request)
        return templates.TemplateResponse(request, "block_mock.html", {
            "user": user, "subjects": [{"code": c, "name": _name(c)} for c in SUBJECT_ORDER],
            "full_access": db.get_plan_limits(user.plan)["full_mock_access"], "max_ball": MAX_BALL,
        })

    @app.get("/analytics", response_class=HTMLResponse)
    async def analytics_page(request: Request):
        user = await get_current_user(request)
        if user is None:
            return _login_redirect(request)
        return templates.TemplateResponse(request, "analytics.html", {"user": user})

    @app.get("/guide", response_class=HTMLResponse)
    async def guide_page(request: Request):
        user = await get_current_user(request)
        if user is None:
            return _login_redirect(request)
        return templates.TemplateResponse(request, "guide.html", {
            "user": user, "subjects": await guide_data(), "max_ball": MAX_BALL,
            "cert_levels": exam_rules.NATIONAL_CERT_LEVELS,
        })

    @app.get("/api/analytics")
    @limiter.limit("30/minute")
    async def api_analytics(request: Request):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
        return JSONResponse(await user_analytics(user.id))

    # ---------- blok mock
    @app.post("/api/block/generate")
    @limiter.limit("6/minute")
    async def api_block_generate(request: Request, body: BlockRequest):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
        s1, s2 = body.specs
        if s1 == s2 or s1 not in db.SUBJECT_CODES or s2 not in db.SUBJECT_CODES:
            raise HTTPException(status_code=400, detail="Ikki xil ixtisoslik fanini tanlang.")
        if not db.get_plan_limits(user.plan)["full_mock_access"]:
            raise HTTPException(status_code=402, detail="DTM blok mock faqat Pro yoki Ultra tarifda mavjud.")
        questions = await block_questions(user.plan, s1, s2, user.id)
        if len(questions) < 30:
            raise HTTPException(status_code=404, detail="Blok uchun savollar hali yetarli emas.")
        questions = [shuffle_question_options(q) for q in questions]
        meta = {"block_mock": True, "specs": [s1, s2], "full_mock": True, "label": f"DTM blok mock: {_name(s1)} + {_name(s2)}"}
        await db.store_quiz_session(body.attempt_token, user.id, s1, "dtm", questions, topic="__block__",
                                    level=user.level or "ortacha", meta=meta)
        return JSONResponse({"topic": meta["label"], "questions": [public_question(q) for q in questions], "mode": "dtm",
                             "time_limit_minutes": BLOCK_MINUTES, "layout": {}, "full_mock": True})

    # ---------- adaptiv
    @app.post("/api/adaptive/start")
    @limiter.limit("10/minute")
    async def api_adaptive_start(request: Request, body: AdaptiveStart):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
        if body.subject not in db.SUBJECT_CODES:
            raise HTTPException(status_code=400, detail="Noto'g'ri fan.")
        mode = body.mode if body.mode in {m["code"] for m in db.get_test_modes_for_subject(body.subject)} else "dtm"
        if not db.get_plan_limits(user.plan)["full_mock_access"] and not body.topic:
            raise HTTPException(status_code=402, detail="Butun fan bo'yicha adaptiv test Pro yoki Ultra tarifda. Mavzu bo'yicha bepul.")
        rows = exam_db._unique(await exam_db._fetch(body.subject, mode, user.plan, [body.topic] if body.topic else None))
        closed = [q for q in rows if (q.qtype or "closed") != "match"]
        if len(closed) < 5:
            raise HTTPException(status_code=404, detail="Adaptiv test uchun savollar yetarli emas.")
        pool: dict[int, list[int]] = {1: [], 2: [], 3: []}
        for q in closed:
            pool[min(3, max(1, q.difficulty or 2))].append(q.id)
        total = min(body.total, len(closed))
        used: set[int] = set()
        first_id = _level_pick(pool, used, 2)
        used.add(first_id)
        first = await db.questions_by_ids([first_id])
        if not first:
            raise HTTPException(status_code=404, detail="Savol topilmadi.")
        q0 = shuffle_question_options(first[0])
        q0["section"] = "Qiyinlik: o'rta"
        meta = {"adaptive": True, "ad_pool": {str(k): v for k, v in pool.items()}, "ad_total": total, "ad_level": 2,
                "ad_used": sorted(used), "pool_total": len(closed), "label": "Adaptiv test" + (f": {body.topic}" if body.topic else "")}
        await db.store_quiz_session(body.attempt_token, user.id, body.subject, mode, [q0],
                                    topic=body.topic or "__checkpoint__", level=user.level or "ortacha", meta=meta)
        return JSONResponse({"topic": meta["label"], "questions": [public_question(q0)], "mode": mode, "adaptive": True,
                             "total": total, "time_limit_minutes": max(10, round(total * 1.5)), "layout": {}, "full_mock": False})

    @app.post("/api/adaptive/next")
    @limiter.limit("120/minute")
    async def api_adaptive_next(request: Request, body: AdaptiveNext):
        user = await get_current_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
        sess = await db.get_quiz_session(body.attempt_token, user.id)
        if sess is None or not (sess.get("meta") or {}).get("adaptive"):
            raise HTTPException(status_code=409, detail="Adaptiv sessiya topilmadi.")
        meta, questions = sess["meta"], sess["questions"]
        if body.index != len(questions) - 1:
            raise HTTPException(status_code=409, detail="Savol tartibi mos emas.")
        cur = questions[body.index]
        if cur.get("qtype") == "open":
            ok = isinstance(body.answer, str) and exam_rules.check_open_answer(body.answer.strip(), cur.get("accept") or [])
        else:
            ok = isinstance(body.answer, int) and not isinstance(body.answer, bool) and body.answer == cur.get("correct_index")
        level = int(meta.get("ad_level", 2))
        level = min(3, level + 1) if ok else max(1, level - 1)
        total = int(meta["ad_total"])
        if len(questions) >= total:
            return JSONResponse({"done": True})
        pool = {int(k): v for k, v in meta["ad_pool"].items()}
        used = set(meta.get("ad_used") or [])
        nid = _level_pick(pool, used, level)
        if nid is None:
            return JSONResponse({"done": True})
        got = await db.questions_by_ids([nid])
        if not got:
            return JSONResponse({"done": True})
        used.add(nid)
        nq = shuffle_question_options(got[0])
        nq["section"] = "Qiyinlik: " + {1: "oson", 2: "o'rta", 3: "qiyin"}[level]
        questions.append(nq)
        meta["ad_level"], meta["ad_used"] = level, sorted(used)
        await db.store_quiz_session(body.attempt_token, user.id, sess["subject"], sess["mode"], questions,
                                    topic=sess.get("topic") or "", level=sess.get("level") or "ortacha", meta=meta)
        return JSONResponse({"done": False, "question": public_question(nq), "level": level, "correct": bool(ok)})
