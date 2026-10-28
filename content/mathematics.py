"""Matematika (DTM/BMBA va Milliy sertifikat): 8–11-sinf bo'yicha mavzular va tayyor savollar.

Tuzilma:
  math_a.py — 8-sinf (M8.*) va 9-sinf (M9.*): algebra, sonlar, progressiyalar, kombinatorika, ehtimollik
  math_b.py — 10-sinf (M10.*): trigonometriya, logarifm, vektorlar, stereometriya
              11-sinf (M11.*): hosila, integral, limit, funksiya tadqiqi, DTM masalalari
  math_fig.py — barcha sinflar (MF.*): chizmalı geometriya (alohida modul, o'ziga yuklanadi)

DTM (BMBA): majburiy blok 10·1.1 + mutaxassislik 30·3.1 = 104 ball
Milliy sertifikat: 45 savol, raw68 tizimi (yopiq·1 + moslash·2 + ochiq·3 → IRT/100)
"""
from . import math_a, math_b, math_c
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

# ─────────────────── MAVZULAR RO'YXATI ───────────────────
# (kod, sinf, nom, tarif)  |  tarif: free/pro/ultra
TOPICS = [
    # ── 8-SINF ──
    ("M8.1", 8, "Kvadrat ildiz va haqiqiy sonlar", "free"),
    ("M8.2", 8, "Kvadrat tenglama va diskriminant", "free"),
    ("M8.3", 8, "Algebraik kasrlar va soddalashtirish", "free"),
    ("M8.4", 8, "Nisbat, proporsiya va foiz masalalari", "free"),
    ("M8.5", 8, "Chiziqli tengsizliklar va modul", "pro"),
    ("M8.6", 8, "Funksiyalar: chiziqli va kvadrat funksiya", "free"),
    ("M8.7", 8, "Ko'p hadlar va algebraik identikliklar", "pro"),
    ("M8.8", 8, "EKB, EKU va bo'linuvchanlik belgilari", "pro"),
    # ── 9-SINF ──
    ("M9.1", 9, "Kvadrat funksiya: uch, diskriminant, parametr", "free"),
    ("M9.2", 9, "Ikkinchi darajali tengsizliklar tizimi", "pro"),
    ("M9.3", 9, "Arifmetik va geometrik progressiyalar", "free"),
    ("M9.4", 9, "Kombinatorika: faktorial, kombinatsiya, joylashtirma", "pro"),
    ("M9.5", 9, "Ehtimollik asoslari va klassik formula", "free"),
    ("M9.6", 9, "Statistika: o'rtacha, mediana, moda", "pro"),
    # ── 10-SINF ──
    ("M10.1", 10, "Trigonometrik funksiyalar va asosiy formulalar", "free"),
    ("M10.2", 10, "Trigonometrik tenglamalar", "pro"),
    ("M10.3", 10, "Logarifm va ko'rsatkichli funksiyalar", "free"),
    ("M10.4", 10, "Ko'rsatkichli va logarifmik tenglamalar", "pro"),
    ("M10.5", 10, "Vektorlar va koordinatali geometriya tekislikda", "pro"),
    ("M10.6", 10, "Stereometriya asoslari: hajm va sirt", "pro"),
    # ── 11-SINF ──
    ("M11.1", 11, "Hosila va differentsial hisoblash qoidalari", "free"),
    ("M11.2", 11, "Integral va aniqlangan integral", "pro"),
    ("M11.3", 11, "Koordinatali geometriya: to'g'ri chiziq va aylana", "pro"),
    ("M11.4", 11, "Limit asoslari va ajoyib limitlar", "ultra"),
    ("M11.5", 11, "Funksiya tadqiqi: ekstremum va burilish nuqtasi", "pro"),
    ("M11.6", 11, "Murakkab kombinatsion va analitik masalalar", "ultra"),
    ("M11.7", 11, "DTM darajasidagi murakkab masalalar (11-sinf)", "ultra"),
]

_MORE = [
    ("M8.9", 8, "Daraja va uning xossalari", "free"), ("M8.10", 8, "Foizlar va foiz masalalari", "free"),
    ("M8.11", 8, "Harakat masalalari", "pro"), ("M8.12", 8, "Ish va birgalikda ishlash masalalari", "pro"),
    ("M8.13", 8, "Aralashma va qotishma masalalari", "pro"), ("M8.14", 8, "Chiziqli tenglamalar tizimi", "free"),
    ("M8.15", 8, "Modulli tenglama va tengsizliklar", "pro"), ("M8.16", 8, "Ko'paytuvchilarga ajratish", "free"),
    ("M8.17", 8, "Planimetriya: uchburchak xossalari", "free"), ("M8.18", 8, "To'rtburchaklar va ularning yuzalari", "free"),
    ("M8.19", 8, "Aylana va doira: uzunlik va yuza", "free"), ("M8.20", 8, "Pifagor teoremasi va o'xshashlik", "pro"),
    ("M9.7", 9, "Vyet teoremasi", "pro"), ("M9.8", 9, "Irratsional tenglamalar", "pro"),
    ("M9.9", 9, "Intervallar usuli", "pro"), ("M9.10", 9, "Funksiya xossalari: aniqlanish sohasi, juft-toqlik", "free"),
    ("M9.11", 9, "Ketma-ketliklar va yig'indilar", "pro"), ("M9.12", 9, "Parametrli tenglamalar", "pro"),
    ("M10.7", 10, "Trigonometrik ayniyatlar va keltirish formulalari", "pro"), ("M10.8", 10, "Logarifmik tengsizliklar", "pro"),
    ("M10.9", 10, "Prizma va piramida", "pro"), ("M10.10", 10, "Silindr, konus va shar", "pro"),
    ("M10.11", 10, "Ko'pburchaklar va ichki burchaklar", "free"),
    ("M11.8", 11, "Hosilaning geometrik va fizik ma'nosi", "pro"), ("M11.9", 11, "Boshlang'ich funksiya va integral yuzasi", "pro"),
    ("M11.10", 11, "Ehtimollik: klassik va ko'p bosqichli", "pro"), ("M11.11", 11, "Kombinatsiya, Nyuton binomi va masalalar", "ultra"),
]
TOPICS = sorted(TOPICS + _MORE, key=lambda t: t[1])

# Barcha savol banklarini birlashtirish
_BANKS: dict = {}
_BANKS.update(math_a.Q)
_BANKS.update(math_b.Q)
_BANKS.update(math_c.Q)


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning(
            "Matematika bankida %s ta muammo: %s", len(problems), problems[:5]
        )
    return {
        "subject": "math",
        "modes": ["dtm", "certificate"],
        "topics": topics,
        "questions": questions,
    }
