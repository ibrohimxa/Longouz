"""
LongoUZ — DTM, Sertifikat, IELTS va CEFR rejimlari uchun baholash mantiqi.

Barcha rejimlar bitta test natijasidan (to'g'ri javoblar soni / jami savol
soni) boshlanadi, lekin natija rejimga qarab butunlay boshqacha ko'rsatiladi:

  - DTM rejimi:         har bir to'g'ri javob uchun 3.1 ball (davlat
                         standartidagi asosiy fan balliga mos).
  - Sertifikat rejimi:  foizga qarab CEFR Band (A2 / B1 / B2 / C1) beriladi
                         (ingliz tilidan boshqa barcha fanlar uchun umumiy
                         mock-imtihon natijasi sifatida ishlatiladi).
  - IELTS rejimi:       foiz taxminiy IELTS Band Score (1.0-9.0) ga
                         aylantiriladi — faqat ingliz tili uchun.
  - CEFR rejimi:        IELTS bilan bir xil A1-C2 mezonlariga asoslanadi,
                         lekin faqat ingliz tili "CEFR" rejimida ishlatiladi
                         (Sertifikat rejimidan farqli — CEFR mustaqil bo'lim).

main.py shu modulni chaqirib, foydalanuvchi tanlagan rejimga qarab to'g'ri
natija tuzilmasini quradi.
"""

import exam_rules as ER

# Rasmiy DTM blok-test: asosiy (1-chi) fan 30 savol x 3.1 = 93 ball (umumiy 189 ball:
# 93 + 2-fan 30 x 2.1 = 63 + majburiy fanlar 30 x 1.1 = 33). Mashq testida savollar
# soni har xil bo'lgani uchun natija 93 ballik shkalaga proporsional keltiriladi
# (30 savolda aynan 3.1 ball/savol).
DTM_BALL_PER_QUESTION = 3.1
DTM_MAIN_SUBJECT_MAX = 93.0

# Milliy sertifikat (fan bo'yicha, 100 ballik shkala) rasmiy darajalari.
NATIONAL_CERT_LEVELS = [
    (70.0, "A+"), (65.0, "A"), (60.0, "B+"), (55.0, "B"), (50.0, "C+"), (46.0, "C"),
]
NATIONAL_CERT_MIN = 46.0

CEFR_BANDS = [
    (90, "C2"),
    (75, "C1"),
    (60, "B2"),
    (40, "B1"),
    (20, "A2"),
    (0, "A1"),
]

# IELTS Band Score — foizni taxminiy IELTS shkalasiga (1.0-9.0) aylantirish.
# Bu RASMIY IELTS konvertatsiya jadvali emas (chunki haqiqiy IELTS bali
# faqat rasmiy imtihonda, alohida metodika bilan aniqlanadi) — bu shunchaki
# LongoUZ ichidagi mashq-testlari uchun mo'ljallangan, foydalanuvchiga
# taxminiy yo'nalish beruvchi shkala. Sertifikatda ham shu narsa aniq
# ko'rsatiladi ("taxminiy Band", rasmiy IELTS sertifikati emas).
IELTS_BANDS = [
    (95, 9.0), (90, 8.5), (85, 8.0), (80, 7.5), (70, 7.0),
    (60, 6.5), (50, 6.0), (40, 5.5), (30, 5.0), (20, 4.5), (0, 4.0),
]


def _percent(correct: int, total: int) -> int:
    return round((correct / total) * 100) if total else 0


def score_dtm(correct: int, total: int) -> dict:
    ball = round(correct / total * DTM_MAIN_SUBJECT_MAX, 1) if total else 0.0
    percent = _percent(correct, total)
    return {
        "mode": "dtm",
        "correct": correct,
        "total": total,
        "percent": percent,
        "ball": ball,
        "max_ball": DTM_MAIN_SUBJECT_MAX,
        "label": f"{ball} / {DTM_MAIN_SUBJECT_MAX} ball",
    }


def national_level(ball: float) -> str:
    for threshold, name in NATIONAL_CERT_LEVELS:
        if ball >= threshold:
            return name
    return ""


def score_certificate(correct: int, total: int) -> dict:
    """Milliy sertifikat: 100 ballik shkala, A+ (70+), A (65), B+ (60), B (55), C+ (50), C (46)."""
    percent = _percent(correct, total)
    ball = round(correct / total * 100, 1) if total else 0.0
    level = national_level(ball)
    if level:
        label = f"{level} daraja · {ball} / 100 ball"
    else:
        label = f"{ball} / 100 ball · daraja yo'q"
    return {
        "mode": "certificate",
        "correct": correct,
        "total": total,
        "percent": percent,
        "ball": ball,
        "max_ball": 100,
        "band": level or "Daraja yo'q",
        "label": label,
    }


def score_cefr(correct: int, total: int) -> dict:
    """CEFR rejimi — Sertifikat bilan bir xil A1-C2 mezoni, lekin ingliz
    tiliga xos, mustaqil bo'lim sifatida alohida saqlanadi."""
    percent = _percent(correct, total)
    band = "A1"
    for threshold, name in CEFR_BANDS:
        if percent >= threshold:
            band = name
            break
    return {
        "mode": "cefr",
        "correct": correct,
        "total": total,
        "percent": percent,
        "band": band,
        "label": f"CEFR {band}",
    }


def score_ielts(correct: int, total: int) -> dict:
    percent = _percent(correct, total)
    band_score = 4.0
    for threshold, score in IELTS_BANDS:
        if percent >= threshold:
            band_score = score
            break
    return {
        "mode": "ielts",
        "correct": correct,
        "total": total,
        "percent": percent,
        "band_score": band_score,
        "label": f"IELTS Band {band_score}",
    }


def score_result(mode: str, correct: int, total: int) -> dict:
    if mode == "certificate":
        return score_certificate(correct, total)
    if mode == "cefr":
        return score_cefr(correct, total)
    if mode == "ielts":
        return score_ielts(correct, total)
    return score_dtm(correct, total)


_ANSWER_LETTERS = ["A", "B", "C", "D", "E", "F"]


def build_topic_breakdown(questions_with_answers: list[dict]) -> list[dict]:
    """
    Har bir mavzu (topic) bo'yicha to'g'ri/jami sonini hisoblaydi — rasmiy
    sertifikatdagi "Bo'limlar bo'yicha natijalari" qatoriga o'xshab
    ko'rsatish uchun (masalan "Algebra: 8/10", "Geometriya: 6/8").
    Mavzu tartibda, birinchi uchragan tartibida qaytariladi.
    """
    breakdown: dict[str, dict] = {}
    for q in questions_with_answers:
        topic = q.get("topic") or "Umumiy"
        entry = breakdown.setdefault(topic, {"topic": topic, "correct": 0, "total": 0})
        entry["total"] += 1
        ok = q["is_correct"] if "is_correct" in q else (isinstance(q.get("user_index"), int) and q["user_index"] == q.get("correct_index"))
        if ok:
            entry["correct"] += 1
    return list(breakdown.values())


def build_answer_grid(questions_with_answers: list[dict]) -> list[dict]:
    """
    Har bir savol uchun {"num", "letter", "is_correct"} tuzilmasini qaytaradi —
    rasmiy DTM javob varag'iga o'xshab (masalan "1. A ✓", "2. C ✗") sertifikatda
    va natijalarni ko'rish sahifasida ko'rsatish uchun ishlatiladi. Foydalanuvchi
    javob bermagan savol uchun harf o'rniga "—" qo'yiladi.
    """
    grid = []
    for i, q in enumerate(questions_with_answers):
        user_idx = q.get("user_index")
        correct_idx = q.get("correct_index")
        if q.get("qtype") == "open":
            letter = "Y" if q.get("user_text") else "—"
            ok = bool(q.get("is_correct"))
        else:
            letter = _ANSWER_LETTERS[user_idx] if isinstance(user_idx, int) and 0 <= user_idx < len(_ANSWER_LETTERS) else "—"
            ok = isinstance(user_idx, int) and user_idx == correct_idx
        grid.append({"num": i + 1, "letter": letter, "is_correct": ok})
    return grid


# ---------------------------------------------------------------------------
# RASMIY BAHOLASH (tarix: milliy sertifikat va DTM; biologiya: DTM) — har bir
# savolning o'z qiyinlik/blok bali bo'yicha. Hisob FAQAT serverda bajariladi.
# ---------------------------------------------------------------------------

def _diff(q: dict) -> int:
    d = q.get("difficulty")
    return d if d in (1, 2, 3) else 2


def _blocks_summary(items: list[dict], ball_of) -> list[dict]:
    order: list[str] = []
    agg: dict[str, dict] = {}
    for q in items:
        b = q.get("block") or q.get("section") or ""
        if b not in agg:
            order.append(b)
            agg[b] = {"block": b, "name": ER.BLOCK_NAMES.get(b, b or "Umumiy"), "correct": 0, "total": 0, "ball": 0.0, "max": 0.0}
        e = agg[b]
        e["total"] += 1
        e["max"] += ball_of(q)
        if q["is_correct"]:
            e["correct"] += 1
            e["ball"] += ball_of(q)
    out = []
    for b in order:
        e = agg[b]
        e["ball"] = round(e["ball"], 1)
        e["max"] = round(e["max"], 1)
        out.append(e)
    return out


def _difficulty_summary(items: list[dict]) -> list[dict]:
    res = []
    for d in (1, 2, 3):
        tot = [q for q in items if _diff(q) == d]
        if tot:
            res.append({"difficulty": d, "name": ER.DIFFICULTY_NAMES[d], "correct": sum(1 for q in tot if q["is_correct"]), "total": len(tot)})
    return res


def score_session(subject: str, mode: str, items: list[dict], meta: dict | None = None) -> dict | None:
    """
    items: har bir savol uchun {"is_correct": bool, "difficulty": 1..3, "block": str, "section": str}.
    meta:  {"full_mock": bool, "variant": "main"|"second"}.
    Tuzilma rasmiy bo'lmagan fan/rejimlar uchun None qaytaradi (eski score_result ishlatiladi).
    """
    cfg = ER.tiered_config(subject, mode)
    if cfg is None or not items:
        return None
    meta = meta or {}
    full = bool(meta.get("full_mock"))
    total = len(items)
    correct = sum(1 for q in items if q["is_correct"])
    percent = _percent(correct, total)
    base = {"correct": correct, "total": total, "percent": percent, "full_mock": full, "official": True,
            "by_difficulty": _difficulty_summary(items)}

    if cfg.get("kind") == "raw68" and mode == "certificate":
        pts = cfg["points"]
        kind_of = lambda q: {"closed": "c", "match": "m", "open": "o"}.get(q.get("qtype") or "closed", "c")
        earned = sum(pts[kind_of(q)] for q in items if q["is_correct"])
        possible = sum(pts[kind_of(q)] for q in items)
        if full:
            ball = round(earned / cfg["max_raw"] * 100, 1)
        else:
            ball = round(earned / possible * 100, 1) if possible else 0.0
        level = ""
        for thr, name in cfg["levels"]:
            if ball >= thr:
                level = name
                break
        label = f"{level} daraja · {ball} / 100 ball" if level else f"{ball} / 100 ball · daraja yo'q"
        benefit = next((r["specialty"] for r in cfg["benefits"] if r["level"] == (level or "—")), "")
        names = {"c": "Yopiq testlar (+1)", "m": "Moslashtirish (+2)", "o": "Ochiq format (+3)"}
        blocks = []
        for k in ("c", "m", "o"):
            sub = [q for q in items if kind_of(q) == k]
            if sub:
                blocks.append({"block": k, "name": names[k], "correct": sum(1 for q in sub if q["is_correct"]), "total": len(sub),
                               "ball": float(sum(pts[k] for q in sub if q["is_correct"])), "max": float(pts[k] * len(sub))})
        base.update({
            "mode": "certificate", "ball": ball, "max_ball": 100, "raw_ball": earned, "raw_max": possible,
            "band": level or "Daraja yo'q", "label": label, "benefit": benefit, "mandatory_note": "",
            "blocks": blocks,
        })
        return base

    if subject == "history" and mode == "certificate":
        per = ER.HISTORY_CERT["ball_by_difficulty"]
        earned = sum(per[_diff(q)] for q in items if q["is_correct"])
        possible = sum(per[_diff(q)] for q in items)
        ball = round(earned, 1) if full else (round(earned / possible * 100, 1) if possible else 0.0)
        level = ER.national_level(ball)
        label = (f"{level} daraja · {ball} / 100 ball" if level else f"{ball} / 100 ball · daraja yo'q")
        base.update({
            "mode": "certificate", "ball": ball, "max_ball": 100,
            "raw_ball": round(earned, 1), "raw_max": round(possible, 1),
            "band": level or "Daraja yo'q", "label": label,
            "benefit": ER.cert_benefit_text(level) if level else ER.cert_benefit_text("—"),
            "mandatory_note": ER.CERT_MANDATORY_NOTE if level else "",
            "blocks": _blocks_summary(items, lambda q: per[_diff(q)]),
        })
        return base

    if subject == "history" and mode == "dtm":
        if full:
            per_q = {b["code"]: b["per_question"] for b in ER.HISTORY_DTM["blocks"]}
            sect = lambda q: q.get("section") or q.get("block") or "mutaxassislik"
            ball = round(sum(per_q.get(sect(q), 3.1) for q in items if q["is_correct"]), 1)
            mx = round(sum(per_q.get(sect(q), 3.1) for q in items), 1)
            base.update({
                "mode": "dtm", "ball": ball, "max_ball": mx, "label": f"{ball} / {mx} ball",
                "blocks": _blocks_summary([{**q, "block": sect(q)} for q in items], lambda q: per_q.get(q["block"], 3.1)),
            })
            return base
        ball = round(correct / total * ER.HISTORY_DTM["blocks"][1]["max"], 1)
        base.update({"mode": "dtm", "ball": ball, "max_ball": 93.0, "label": f"{ball} / 93.0 ball"})
        return base

    if subject in ER.VARIANT_SUBJECTS and mode == "dtm":
        variant = meta.get("variant") if meta.get("variant") in ("main", "second") else "main"
        per_q = cfg["per_question"][variant]
        mx_full = cfg["max_ball"][variant]
        ball = round(correct * per_q, 1) if full else round(correct / total * mx_full, 1)
        mx = round(total * per_q, 1) if full else mx_full
        base.update({
            "mode": "dtm", "ball": ball, "max_ball": mx, "variant": variant,
            "label": f"{ball} / {mx} ball",
            "blocks": [{"block": "", "name": "1-mutaxassislik fani (3.1 ball)" if variant == "main" else "2-mutaxassislik fani (2.1 ball)",
                        "correct": correct, "total": total, "ball": ball, "max": mx}],
        })
        return base
    return None


def certificate_eligible(result: dict) -> bool:
    """
    MUHIM, YANGI QOIDA: haqiqiy DTM/rasmiy sertifikatlar natija past bo'lsa
    ham beriladi (rasmiy DTM javob varag'ida past ball bilan ham "Umumiy
    ball" rasmiy hujjat sifatida beriladi — past natija sertifikatni
    "soxta" qilmaydi, faqat haqiqiy natijani ko'rsatadi). Shu sababli endi
    foiz/band bo'yicha chegara YO'Q — faqat test yetarlicha uzun bo'lishi
    kerak (juda qisqa, 5 tadan kam savolli "mashq" rasmiy hujjat sifatida
    hisoblanmaydi).
    """
    if result.get("official") and not result.get("full_mock"):
        return False  # rasmiy tuzilmali fanlarda faqat TO'LIQ imtihon sertifikat beradi
    return result["total"] >= 5
