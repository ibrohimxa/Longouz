"""
LongoUZ — RASMIY imtihon qoidalari (Milliy sertifikat, DTM/BMBA) va tarif cheklovlari.

Bu modul faqat konfiguratsiya va toza (DB'siz) hisob-kitob funksiyalarini saqlaydi,
shuning uchun scoring.py, database.py va main.py bir xil manbadan foydalanadi.

TARIX — MILLIY SERTIFIKAT (UZBMB, 100 ball, 45 savol, 90 daqiqa):
  Blok                              savol  ball    qiyinlik tarkibi (oson/o'rta/qiyin)
  Siyosiy tarix                      29    70.2    4 / 15 / 10   (20 yopiq + 9 ochiq)
  Ijtimoiy-iqtisodiy tarix            7    12.7    3 / 4  / 0    (6 yopiq + 1 ochiq)
  Moslashtirish                       3     6.6    0 / 3  / 0
  Mamlakatlar madaniyati/me'morchilik 6    10.5    3 / 3  / 0
  Jami                               45   100.0   10 / 25 / 10
  Savol bali: oson 1.3, o'rta 2.2, qiyin 3.2 (1.3*10 + 2.2*25 + 3.2*10 = 100).

TARIX — DTM (BMBA): majburiy blok 10 x 1.1 = 11.0 (15 daq), mutaxassislik 30 x 3.1 = 93.0 (45 daq).
KIMYO — DTM: biologiya bilan bir xil tuzilma (30 savol, 3.1 / 2.1 ball).
FIZIKA, ONA TILI VA ADABIYOT — sertifikat (UzBMB): 45 savol; №1–32 yopiq (+1), №33–35 moslashtirish (+2),
  №36–45 ochiq (+3) => 68 xom ball, 100 ballik shkalaga o'tkaziladi; DTM — biologiyadagi kabi (30 savol, 3.1 / 2.1).
BIOLOGIYA — DTM: 1-fan 30 x 3.1 = 93.0, 2-fan 30 x 2.1 = 63.0; 9 oson / 15 o'rta / 6 qiyin;
  24 yopiq + 3 moslashtirish + 3 ochiq.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# TARIF DARAJALARI
# ---------------------------------------------------------------------------
PLAN_RANK = {"free": 0, "pro": 1, "ultra": 2}
TIER_NAMES = {"free": "Bepul", "pro": "Pro", "ultra": "Ultra"}

# Har bir tarifda ochiq mavzular soni (jami, barcha sinflar bo'yicha).
TIER_TOPIC_TOTALS = {"free": 45, "pro": 85, "ultra": 150}

# Mavzu bo'yicha mashqda bitta urinishdagi savollar soni va ko'rinadigan qiyinlik.
TIER_PRACTICE = {
    "free":  {"count": 10, "max_difficulty": 2},
    "pro":   {"count": 16, "max_difficulty": 3},
    "ultra": {"count": 40, "max_difficulty": 3},
}

# Mashq/nazorat testlari uchun (mavzu bo'yicha) savol-narx
NAZORAT_EVERY = 10          # har 10 mavzudan keyin xatolar ustida ishlash testi
NAZORAT_COUNT = 20

DIFFICULTY_NAMES = {1: "Oson", 2: "O'rta", 3: "Qiyin"}

BLOCK_NAMES = {
    "siyosiy": "Siyosiy tarix",
    "ijtimoiy": "Ijtimoiy-iqtisodiy tarix",
    "moslash": "Moslashtirish",
    "madaniyat": "Mamlakatlar madaniyati va me'morchiligi",
    "majburiy": "Majburiy blok",
    "mutaxassislik": "Mutaxassislik bloki",
}

# ---------------------------------------------------------------------------
# IMTIHON TUZILMALARI
# cells: (blok, qiyinlik, tur, soni); tur: c = yopiq (A-D), o = ochiq, m = moslashtirish
# ---------------------------------------------------------------------------
HISTORY_CERT = {
    "key": "history_cert",
    "name": "Milliy sertifikat — Tarix",
    "total": 45,
    "time": 90,
    "max_ball": 100.0,
    "ball_by_difficulty": {1: 1.3, 2: 2.2, 3: 3.2},
    "blocks": [
        {"code": "siyosiy", "count": 29, "max": 70.2, "note": "20 ta yopiq + 9 ta ochiq"},
        {"code": "ijtimoiy", "count": 7, "max": 12.7, "note": "6 ta yopiq + 1 ta ochiq"},
        {"code": "moslash", "count": 3, "max": 6.6, "note": "faqat juftlik hosil qilish"},
        {"code": "madaniyat", "count": 6, "max": 10.5, "note": "faqat yopiq test"},
    ],
    "cells": [
        ("siyosiy", 1, "c", 4), ("siyosiy", 2, "c", 15), ("siyosiy", 3, "o", 9), ("siyosiy", 3, "c", 1),
        ("ijtimoiy", 1, "c", 3), ("ijtimoiy", 2, "c", 3), ("ijtimoiy", 2, "o", 1),
        ("moslash", 2, "m", 3),
        ("madaniyat", 1, "c", 3), ("madaniyat", 2, "c", 3),
    ],
}

HISTORY_DTM = {
    "key": "history_dtm",
    "name": "DTM (BMBA) — Tarix",
    "total": 40,
    "time": 60,
    "blocks": [
        {"code": "majburiy", "count": 10, "per_question": 1.1, "max": 11.0, "minutes": 15},
        {"code": "mutaxassislik", "count": 30, "per_question": 3.1, "max": 93.0, "minutes": 45},
    ],
    "max_ball": 104.0,
    "cells": [
        ("majburiy", 1, "c", 5), ("majburiy", 2, "c", 5),
        ("mutaxassislik", 1, "c", 8), ("mutaxassislik", 2, "c", 12), ("mutaxassislik", 2, "m", 3),
        ("mutaxassislik", 3, "c", 4), ("mutaxassislik", 3, "o", 3),
    ],
}

BIOLOGY_DTM = {
    "key": "biology_dtm",
    "name": "DTM (BMBA) — Biologiya",
    "total": 30,
    "time": 60,
    "per_question": {"main": 3.1, "second": 2.1},
    "max_ball": {"main": 93.0, "second": 63.0},
    "cells": [
        ("", 1, "c", 9), ("", 2, "c", 12), ("", 2, "m", 3), ("", 3, "c", 3), ("", 3, "o", 3),
    ],
}

CHEMISTRY_DTM = {
    "key": "chemistry_dtm",
    "name": "DTM (BMBA) — Kimyo",
    "total": 30,
    "time": 60,
    "per_question": {"main": 3.1, "second": 2.1},
    "max_ball": {"main": 93.0, "second": 63.0},
    "cells": [
        ("", 1, "c", 9), ("", 2, "c", 12), ("", 2, "m", 3), ("", 3, "c", 3), ("", 3, "o", 3),
    ],
}


# ---------------------------------------------------------------------------
# FIZIKA va ONA TILI VA ADABIYOT — sertifikat (xom ball 68 => 100 ball) va DTM
# ---------------------------------------------------------------------------
RAW68_POINTS = {"c": 1, "m": 2, "o": 3}      # yopiq / moslashtirish / ochiq
RAW68_LEVELS = [(86.0, "A+"), (76.0, "A"), (66.0, "B"), (56.0, "C"), (46.0, "D")]
RAW68_BENEFITS = [
    {"level": "A+", "range": "86.0 — 100", "specialty": "OTMga kirishda fandan maksimal ball, imtihondan ozod (o'qituvchiga 50% ustama)"},
    {"level": "A", "range": "76.0 — 85.9", "specialty": "OTMga kirishda fandan maksimal ball, imtihondan ozod (o'qituvchiga 50% ustama)"},
    {"level": "B", "range": "66.0 — 75.9", "specialty": "Proporsional ball (o'qituvchiga 20% ustama)"},
    {"level": "C", "range": "56.0 — 65.9", "specialty": "Imtiyoz yo'q, to'plangan real foiz hisobga olinadi"},
    {"level": "D", "range": "46.0 — 55.9", "specialty": "Sertifikat beriladi, imtiyoz kuchi yo'q (eng quyi o'tish chegarasi)"},
    {"level": "—", "range": "46.0 dan past", "specialty": "Sertifikat berilmaydi"},
]
_RAW68_CELLS = [
    ("", 1, "c", 8), ("", 2, "c", 16), ("", 3, "c", 8),
    ("", 2, "m", 3),
    ("", 2, "o", 3), ("", 3, "o", 7),
]


def _raw68(key, name, time_min, closed_note, open_note):
    return {
        "key": key, "name": name, "kind": "raw68", "total": 45, "time": time_min,
        "points": RAW68_POINTS, "max_raw": 68, "max_ball": 100.0,
        "levels": RAW68_LEVELS, "benefits": RAW68_BENEFITS,
        "cells": _RAW68_CELLS,
        "info": {
            "kind": key, "max_ball": 100,
            "blocks": [
                {"name": "Yopiq test (№1–32)", "count": 32, "max": 32, "note": closed_note},
                {"name": "Moslashtirish (№33–35)", "count": 3, "max": 6, "note": "3 juftlikni to'liq topsangiz +2 ball"},
                {"name": "Ochiq format (№36–45)", "count": 10, "max": 30, "note": open_note},
            ],
            "ball_by_difficulty": [
                {"name": "Yopiq testning har biri (xom ball)", "ball": 1},
                {"name": "Moslashtirishning har biri (xom ball)", "ball": 2},
                {"name": "Ochiq savolning har biri (xom ball)", "ball": 3},
            ],
            "levels": [{"level": r["level"], "range": r["range"], "benefit": r["specialty"]} for r in RAW68_BENEFITS],
            "mandatory_note": ("Maksimal xom ball 68. Haqiqiy imtihonda xom ball respublika natijalari asosida IRT (Rash) modeli bilan "
                               "100 ballik shkalaga o'tkaziladi; bu yerda ball xom ballning 100 ballik proporsional ko'rinishi (taxminiy)."),
        },
        "desc": (f"Milliy sertifikat (UzBMB): 45 ta savol, {time_min} daqiqa — №1–32 yopiq (+1), №33–35 moslashtirish (+2), "
                 "№36–45 ochiq format (+3); xom ball 68 => 100 ball. Daraja: A+ (86+), A, B, C, D (46+)."),
    }


PHYSICS_CERT = _raw68("physics_cert", "Milliy sertifikat — Fizika", 150,
                      "4 ta variantli (A–D), har biri +1 xom ball", "variantsiz, faqat raqamli javob, har biri +3 xom ball")
NATIVE_CERT = _raw68("native_cert", "Milliy sertifikat — Ona tili va adabiyot", 90,
                     "4 ta variantli (A–D): matn tahlili, imlo, asarlar g'oyasi", "variantsiz: imlo xatosini to'g'rilash, gap turi, qahramon ismi")


def _variant_dtm(key, name, desc_name, diff_texts, typology):
    return {
        "key": key, "name": name, "kind": "variant_dtm", "total": 30, "time": 60,
        "per_question": {"main": 3.1, "second": 2.1},
        "max_ball": {"main": 93.0, "second": 63.0},
        "cells": [("", 1, "c", 9), ("", 2, "c", 12), ("", 2, "m", 3), ("", 3, "c", 3), ("", 3, "o", 3)],
        "info": {
            "kind": key, "max_ball": {"main": 93.0, "second": 63.0},
            "blocks": [
                {"name": "1-mutaxassislik fani", "count": 30, "max": 93.0, "note": "har biri 3.1 ball (№1–30)"},
                {"name": "2-mutaxassislik fani", "count": 30, "max": 63.0, "note": "har biri 2.1 ball (№31–60)"},
            ],
            "difficulty": [{"name": t, "count": c} for t, c in diff_texts],
            "typology": typology,
        },
        "desc": f"DTM (BMBA) {desc_name}: 30 ta savol — 24 yopiq, 3 moslashtirish, 3 ochiq. 1-fan: har biri 3.1 ball (93), 2-fan: 2.1 ball (63).",
    }


PHYSICS_DTM = _variant_dtm(
    "physics_dtm", "DTM (BMBA) — Fizika", "fizika",
    [("I daraja (oson) — ta'rif, formula va birliklar", 9),
     ("II daraja (o'rta) — grafik, chizma va moslashtirish masalalari", 15),
     ("III daraja (qiyin) — murakkab hisoblash masalalari", 6)],
    "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (son yozing)")
NATIVE_DTM = _variant_dtm(
    "native_dtm", "DTM (BMBA) — Ona tili va adabiyot", "ona tili va adabiyot",
    [("I daraja (oson) — ta'rif, atamalar, asar muallifi", 9),
     ("II daraja (o'rta) — tahlil, moslashtirish, imlo va punktuatsiya", 15),
     ("III daraja (qiyin) — murakkab sintaktik va poetik tahlil", 6)],
    "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (so'z/ism yozing)")

# 1-/2-mutaxassislik fani varianti bor (3.1 / 2.1 ball) DTM fanlari
# ─────────────────────────────────────────────────────────
# MATEMATIKA — DTM va Milliy sertifikat
# ─────────────────────────────────────────────────────────
MATH_DTM = _variant_dtm(
    "math_dtm", "DTM (BMBA) — Matematika", "matematika",
    [("I daraja (oson) — ta'rif, formula va hisoblash", 9),
     ("II daraja (o'rta) — tenglamalar, tengsizliklar, grafik", 15),
     ("III daraja (qiyin) — murakkab masalalar, trigonometriya, integral", 6)],
    "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (son yozing)")

MATH_CERT = _raw68("math_cert", "Milliy sertifikat — Matematika", 120,
                   "4 ta variantli (A–D): algebra, geometriya, trigonometriya, sonlar",
                   "variantsiz: aniq hisob, kvadrat tenglama, integral, hosila javobi")

ENGLISH_DTM = _variant_dtm(
    "english_dtm", "DTM (BMBA) — Ingliz tili", "ingliz tili",
    [("I daraja (oson) — asosiy grammatika va lug'at", 9),
     ("II daraja (o'rta) — zamonlar, shartli gaplar, o'qish", 15),
     ("III daraja (qiyin) — murakkab grammatika, inversiya, idioma", 6)],
    "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (so'z yoki ibora yozing)")
RUSSIAN_DTM = _variant_dtm(
    "russian_dtm", "DTM (BMBA) — Rus tili", "rus tili",
    [("I daraja (oson) — fonetika, orfografiya asoslari", 9),
     ("II daraja (o'rta) — morfologiya va sintaksis", 15),
     ("III daraja (qiyin) — tinish belgilari, murakkab gaplar, adabiyot", 6)],
    "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (so'z yozing)")
RUSSIAN_CERT = _raw68("russian_cert", "Milliy sertifikat — Rus tili", 90,
                      "4 ta variantli (A–D): imlo, grammatika, matn tahlili", "variantsiz: so'z shaklini yoki imloni yozing")

VARIANT_SUBJECTS = {"biology": BIOLOGY_DTM, "chemistry": CHEMISTRY_DTM, "physics": PHYSICS_DTM, "native": NATIVE_DTM, "math": MATH_DTM,
                    "english": ENGLISH_DTM, "russian": RUSSIAN_DTM}

NATIONAL_CERT_LEVELS = [(70.0, "A+"), (65.0, "A"), (60.0, "B+"), (55.0, "B"), (50.0, "C+"), (46.0, "C")]
NATIONAL_CERT_MIN = 46.0

# Milliy sertifikat OTMga kirishda bergan imtiyozi (foydalanuvchi bergan rasmiy jadval)
CERT_BENEFITS = [
    {"level": "A+", "range": "70.0 va undan yuqori", "specialty": "Maksimal ball (imtihonsiz 100% — 93.0 ball)"},
    {"level": "A", "range": "65.0 — 69.9", "specialty": "Maksimal ball (imtihonsiz 100% — 93.0 ball)"},
    {"level": "B+", "range": "60.0 — 64.9", "specialty": "Proporsional (tabaqalashtirilgan) ball"},
    {"level": "B", "range": "55.0 — 59.9", "specialty": "Proporsional (tabaqalashtirilgan) ball"},
    {"level": "C+", "range": "50.0 — 54.9", "specialty": "Proporsional (tabaqalashtirilgan) ball"},
    {"level": "C", "range": "46.0 — 49.9", "specialty": "Proporsional (tabaqalashtirilgan) ball"},
    {"level": "—", "range": "46.0 dan past", "specialty": "Sertifikat berilmaydi (imtiyoz yo'q)"},
]
CERT_MANDATORY_NOTE = (
    "Milliy sertifikatga ega abituriyentga (A+, A, B+, B, C+, C — daraja qat'iy nazar) "
    "majburiy blokdagi 10 ta tarix savoli uchun to'liq 11 ball avtomatik beriladi."
)


def tiered_config(subject: str, mode: str) -> dict | None:
    """Shu fan+rejim uchun rasmiy tuzilma bo'lsa qaytaradi, aks holda None."""
    if subject == "history" and mode == "certificate":
        return HISTORY_CERT
    if subject == "history" and mode == "dtm":
        return HISTORY_DTM
    if subject == "biology" and mode == "dtm":
        return BIOLOGY_DTM
    if subject == "chemistry" and mode == "dtm":
        return CHEMISTRY_DTM
    if subject == "physics":
        return PHYSICS_CERT if mode == "certificate" else (PHYSICS_DTM if mode == "dtm" else None)
    if subject == "native":
        return NATIVE_CERT if mode == "certificate" else (NATIVE_DTM if mode == "dtm" else None)
    if subject == "math":
        return MATH_CERT if mode == "certificate" else (MATH_DTM if mode == "dtm" else None)
    if subject == "english":
        return ENGLISH_DTM if mode == "dtm" else None
    if subject == "russian":
        return RUSSIAN_CERT if mode == "certificate" else (RUSSIAN_DTM if mode == "dtm" else None)
    return None


def is_tiered(subject: str, mode: str) -> bool:
    """Sinf -> mavzu -> tarif tizimi ishlaydigan fan/rejimlar."""
    return tiered_config(subject, mode) is not None


def plan_rank(plan: str) -> int:
    return PLAN_RANK.get(plan, 0)


def tier_allows(plan: str, tier: str) -> bool:
    return plan_rank(plan) >= PLAN_RANK.get(tier, 0)


def national_level(ball: float) -> str:
    for threshold, name in NATIONAL_CERT_LEVELS:
        if ball >= threshold:
            return name
    return ""


def cert_benefit_text(level: str) -> str:
    for row in CERT_BENEFITS:
        if row["level"] == level:
            return row["specialty"]
    return CERT_BENEFITS[-1]["specialty"]


# ---------------------------------------------------------------------------
# OCHIQ (yozma) JAVOBNI TEKSHIRISH
# ---------------------------------------------------------------------------
_APOS = "'`´ʻʼ’‘ʹ"


def normalize_answer(text: str) -> str:
    """Yozma javobni solishtirish uchun yagona ko'rinishga keltiradi:
    kichik harf, apostrof turlari bir xil, ortiqcha belgi/bo'shliq olib tashlanadi."""
    s = str(text or "").strip().lower()
    for ch in _APOS:
        s = s.replace(ch, "'")
    s = s.replace("‑", "-").replace("–", "-").replace("—", "-")
    s = re.sub(r"[\"“”«».,;:!?()\[\]]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _loose(s: str) -> str:
    """Yil/asr qo'shimchalaridan tozalangan yengil ko'rinish: '1398-yil' == '1398', 'XV asr' == 'xv'."""
    s = normalize_answer(s)
    s = re.sub(r"(?<=[\d\s-])(yil|yilda|yilgi|yillar|asr|asrda|asrning)\b", "", s)
    s = re.sub(r"(?<=\d)[-\s]*(chi|nchi|inchi)\b", "", s)
    return re.sub(r"[\s\-']+", "", s)


_NUM_RE = re.compile(r"^[-+]?(?:\d+(?:[.,]\d+)?|[.,]\d+)(?:\s*[eE][-+]?\d+)?$")


def _as_number(text) -> float | None:
    """'2,5' / '2.5' / '1e-3' / '3 · 10^5' kabi yozuvlarni songa aylantiradi (aks holda None)."""
    s = str(text or "").strip().replace("−", "-").replace("–", "-").replace("\u00a0", " ")
    s = s.replace("×", "*").replace("·", "*")
    m = re.match(r"^([-+]?[\d.,]+)\s*\*\s*10\s*\^?\s*\(?([-+]?\d+)\)?$", s)
    try:
        if m:
            return float(m.group(1).replace(",", ".")) * 10 ** int(m.group(2))
        if _NUM_RE.match(s):
            return float(s.replace(",", ".").replace(" ", ""))
    except ValueError:
        return None
    return None


def check_open_answer(user_answer, accepted: list[str]) -> bool:
    """Ochiq javobni tekshirish: birlik, yaxlitlash, chala yozuv, imlo — answer_check.py (qoidaviy qism)."""
    import answer_check
    return answer_check.check_open_answer(user_answer, accepted)
    ua = str(user_answer)
    if not ua.strip():
        return False
    na, la = normalize_answer(ua), _loose(ua)
    un = _as_number(ua)
    for acc in accepted or []:
        if na == normalize_answer(acc) or (la and la == _loose(acc)):
            return True
        if un is not None:
            an = _as_number(acc)
            if an is not None and abs(un - an) <= 1e-9 + 1e-6 * abs(an):
                return True
    return False
