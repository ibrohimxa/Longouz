"""
LongoUZ WEBSAYT uchun mustaqil ma'lumotlar bazasi qatlami.

MUHIM: Bu bot.py/database.py'dan BUTUNLAY ALOHIDA — botga hech qanday tegishi yo'q.
Websayt o'z bazasida (longouz_web.db) ishlaydi. Ikkala tizim mustaqil.

Jadvallar:
- WebUser        — foydalanuvchi: login ma'lumotlari + onboarding (fan/daraja/sertifikat)
- WebQuizLog     — Claude orqali generatsiya qilingan va yechilgan testlar tarixi
- ChatLog        — Gemini/Claude bilan bo'lgan erkin suhbat tarixi (repetitor rejimi)
"""

from datetime import datetime, date, timedelta
from sqlalchemy import String, Integer, Float, Date, DateTime, Boolean, ForeignKey, Text, LargeBinary, select, func, desc, case
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import insert as sa_insert
from sqlalchemy import text as sa_text
import os
import time
import uuid
import random
import logging

logger = logging.getLogger(__name__)

WEB_DB_PATH = "longouz_web.db"

# ---------------------------------------------------------------------------
# BAZA MANZILI — standart holatda SQLite (hech qanday sozlashsiz, lokal
# rivojlantirish uchun eng oson yo'l). Productionda ko'proq bir vaqtda
# yozuvchi ulanish, kattaroq hajm va backup imkoniyatlari kerak bo'lsa,
# .env fayliga DATABASE_URL qo'shib PostgreSQL'ga o'tish mumkin — kod
# tomonidan HECH QANDAY qo'shimcha o'zgartirish talab qilinmaydi:
#
#   DATABASE_URL=postgresql+asyncpg://foydalanuvchi:parol@host:5432/dbnomi
#
# Qulaylik uchun ko'pchilik hosting/panel'lar (masalan Heroku, Render)
# beradigan "postgres://..." yoki "postgresql://..." (sync drayverga
# mo'ljallangan) manzillar ham avtomatik "postgresql+asyncpg://" ga
# almashtiriladi — .env'ga ularni O'ZGARTIRMASDAN nusxalab qo'yish kifoya.
# ---------------------------------------------------------------------------
_raw_database_url = (os.getenv("DATABASE_URL") or os.getenv("POSTGRES_URL") or os.getenv("NEON_DATABASE_URL") or "").strip()

if _raw_database_url:
    if _raw_database_url.startswith("postgres://"):
        _raw_database_url = _raw_database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif _raw_database_url.startswith("postgresql://"):
        _raw_database_url = _raw_database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    # Neon/Supabase/Vercel Postgres URL'laridagi "sslmode=require" va "channel_binding"
    # asyncpg'ga mos emas — "ssl=require" ga aylantiramiz, ortiqchalarni olib tashlaymiz.
    from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
    _p = urlsplit(_raw_database_url)
    _q = [(k, v) for k, v in parse_qsl(_p.query, keep_blank_values=True) if k not in ("channel_binding", "options")]
    _qd = dict(_q)
    if "sslmode" in _qd:
        _mode = _qd.pop("sslmode")
        if _mode not in ("disable", "allow", "prefer"):
            _qd.setdefault("ssl", "require")
    elif "ssl" not in _qd and _p.hostname and _p.hostname not in ("localhost", "127.0.0.1"):
        _qd["ssl"] = "require"
    _raw_database_url = urlunsplit((_p.scheme, _p.netloc, _p.path, urlencode(_qd), _p.fragment))
    DATABASE_URL = _raw_database_url
    IS_SQLITE = False
    logger.info("Ma'lumotlar bazasi: DATABASE_URL orqali berilgan tashqi baza ishlatilmoqda.")
else:
    import runtime as _rt
    # Vercel'da fayl tizimi faqat o'qish uchun (faqat /tmp yoziladi, u ham doimiy emas) —
    # shu sababli haqiqiy ishlash uchun DATABASE_URL (Postgres) SHART.
    if _rt.IS_VERCEL:
        WEB_DB_PATH = "/tmp/longouz_web.db"
        logger.warning("DIQQAT: DATABASE_URL berilmagan — vaqtinchalik /tmp SQLite ishlatilmoqda (ma'lumotlar yo'qoladi).")
    DATABASE_URL = f"sqlite+aiosqlite:///{WEB_DB_PATH}"
    IS_SQLITE = True

# ---------------------------------------------------------------------------
# ODDIY IN-MEMORY KESH — har so'rovda bazaga yozmaslik/o'qimaslik uchun.
# 20 soniya davomida bir xil foydalanuvchi ma'lumoti keshdan qaytariladi,
# bu bazaga bosimni kamaytiradi va sayt tezroq ishlaydi.
# ---------------------------------------------------------------------------
# Serverless (Vercel)da har instansning o'z xotirasi bor — keshlangan foydalanuvchi boshqa instansda eskirgan bo'lib qoladi
# (onboarding/tarif o'zgargani ko'rinmay, qayta 'kiring/tanlang' deb so'rashiga sabab bo'lardi). Shu sababli u yerda kesh o'chiq.
import runtime as _rt_cache
CACHE_TTL_SECONDS = 0 if _rt_cache.IS_VERCEL else 5
_user_cache: dict[int, tuple[float, "WebUser"]] = {}


def _cache_get(user_id: int):
    entry = _user_cache.get(user_id)
    if entry is None:
        return None
    timestamp, user = entry
    if time.time() - timestamp > CACHE_TTL_SECONDS:
        _user_cache.pop(user_id, None)
        return None
    return user


def _cache_set(user_id: int, user: "WebUser"):
    _user_cache[user_id] = (time.time(), user)


def _cache_invalidate(user_id: int):
    _user_cache.pop(user_id, None)


# ---------------------------------------------------------------------------
# Fanlar va sertifikat turlari — statik ro'yxatlar (frontend ham shulardan foydalanadi)
# ---------------------------------------------------------------------------

SUBJECTS = [
    {"code": "native",    "name": "Ona tili va adabiyot", "icon": "pen"},
    {"code": "math",      "name": "Matematika",               "icon": "ruler"},
    {"code": "english",   "name": "Ingliz tili",               "icon": "globe"},
    {"code": "russian",   "name": "Rus tili",                  "icon": "book"},
    {"code": "history",   "name": "Tarix",                     "icon": "clock"},
    {"code": "chemistry", "name": "Kimyo",                     "icon": "flask"},
    {"code": "biology",   "name": "Biologiya",                 "icon": "leaf"},
    {"code": "physics",   "name": "Fizika",                    "icon": "atom"},
]
SUBJECT_CODES = {s["code"] for s in SUBJECTS}
SUBJECT_NAMES = {s["code"]: s["name"] for s in SUBJECTS}

LEVELS = [
    {"code": "boshlangich", "name": "Boshlang'ich"},
    {"code": "ortacha", "name": "O'rtacha"},
    {"code": "yuqori", "name": "Yuqori"},
]
LEVEL_CODES = {l["code"] for l in LEVELS}
LEVEL_NAMES = {l["code"]: l["name"] for l in LEVELS}

# ---------------------------------------------------------------------------
# TEST REJIMLARI (rejim = "certificate_type" bilan bir xil kod) — fanga
# qarab farqli to'plam ko'rsatiladi:
#   - "english" uchun: DTM, IELTS, CEFR (uchtasi ham alohida bo'lim)
#   - qolgan barcha fanlar uchun: DTM, Sertifikat (umumiy CEFR-uslubidagi
#     mock imtihon, fan nomiga moslashtirilgan)
# Har bir rejim o'z savollar soni, vaqt chegarasi va baholash tizimiga ega
# (qarang: scoring.py). Bu ro'yxat ENDI /quiz sahifasida HAR SAFAR test
# boshlashda ko'rsatiladi — onboarding'dagi certificate_type endi faqat
# "so'nggi ishlatilgan rejim" sifatida standart tanlovni belgilaydi.
# ---------------------------------------------------------------------------
PLAN_NAMES = {"free": "Bepul", "pro": "Pro", "ultra": "Ultra"}

# ---------------------------------------------------------------------------
# TARIFGA BOG'LIQ LIMITLAR — foydalanuvchi so'ragan aniq nisbat bilan:
# Pro = Bepulning ANIQ 2 BARAVARI, Ultra = cheksiz (None = limit yo'q).
# To'liq (mavzusiz, butun fan bo'yicha) MOCK testlar FAQAT Pro/Ultra uchun —
# Bepul foydalanuvchi faqat mavzu bo'yicha (kichikroq, lekin sifatli)
# mashqlarga kira oladi.
# ---------------------------------------------------------------------------
PLAN_LIMITS = {
    # topic_question_count — MAVZU BO'YICHA (mavzusiz emas, to'liq mock ham
    # emas) mashq qilinganda bitta urinishda nechta savol berilishi.
    #
    # ai_window_hours — AI SUHBATI ENDI KUNLIK (yarim tunda) EMAS, SIRPANUVCHI
    # OYNA (sliding window) bilan hisoblanadi: "oxirgi N soat ichida nechta
    # xabar yuborilgan" tekshiriladi. Shu tufayli limit BIRDANIGA (masalan
    # yarim tunda) qaytmaydi — har bir eski xabar aynan N soatdan keyin
    # "eskirib", o'z o'rnini bo'shatadi (aniq so'ralganidek: "soatga qarab
    # orqaga qarab ketaversin").
    #
    # ULTRA = ANIQ PRO'NING 3 BAROBARI (foydalanuvchi qat'iy talabi: "hammasi
    # 3x bo'lsin") — ilgari "cheksiz" edi, endi aniq raqam: 35*3=105 savol/
    # mavzu, 30*3=90 kunlik AI savol. Mavzular soni ham xuddi shunday (pastga,
    # get_topic_unlock_count'ga qarang: 100*3=300).
    "free":  {"ai_daily": 15, "full_mock_access": False, "topic_question_count": 25, "ai_window_hours": 3},
    "pro":   {"ai_daily": 30, "full_mock_access": True, "topic_question_count": 60, "ai_window_hours": 5},
    "ultra": {"ai_daily": 90, "full_mock_access": True, "topic_question_count": 125, "ai_window_hours": 5},
}


def get_plan_limits(plan: str) -> dict:
    """Standart PLAN_LIMITS ustiga admin panelda saqlangan ustama
    (_PLAN_LIMIT_OVERRIDES) bor bo'lsa, o'shani qo'llaydi — shu bilan admin
    kod o'zgartirmasdan, serverni qayta ishga tushirmasdan tariflarni
    o'zgartira oladi."""
    base = dict(PLAN_LIMITS.get(plan, PLAN_LIMITS["free"]))
    override = _PLAN_LIMIT_OVERRIDES.get(plan) if _PLAN_LIMIT_OVERRIDES else None
    if override:
        base.update(override)
    return base


# ---------------------------------------------------------------------------
# MAVZULAR SONI BO'YICHA TARIF CHEGARASI — Free foydalanuvchi bitta fandan
# faqat DASTLABKI N ta mavzuni ko'radi/ocha oladi, Pro esa DASTLABKI M ta
# (qolgani — agar bo'lsa — faqat Ultra'ga ochiq). Mavzular list_topics_db()
# orqali BARQAROR tartibda (birinchi qo'shilgan tartibda) qaytariladi, shuning
# uchun "dastlabki N ta" degani har doim BIR XIL mavzular to'plami bo'ladi,
# tasodifiy emas. Fanlarning aksariyatida hozircha N/M dan kamroq mavzu bor —
# bunday holda hammasi ochiq bo'lib qoladi (Python slice chegaradan oshsa ham
# xato bermaydi), tabiiy ravishda hech kim qulflanmaydi. Fan mavzular banki
# kengaygan sari (Batch 6e — davomli kontent ishi) qulflash o'z-o'zidan
# amalga oshadi, kod o'zgartirishga hojat qolmaydi.
# ---------------------------------------------------------------------------
FREE_TOPIC_VISIBLE_LIMIT = 45
PRO_TOPIC_VISIBLE_LIMIT = 85
# ULTRA = ANIQ PRO'NING 3 BAROBARI (100*3) — foydalanuvchi qat'iy talabi
# bilan "cheksiz" o'rniga aniq raqamga almashtirildi. Amalda hozircha
# barcha fanlarda 300 tagacha mavzu yo'q, shuning uchun bu operatsion
# jihatdan "hammasi ochiq" bilan bir xil natija beradi — lekin fan
# mavzular banki kengaygan sari (Batch 6e) bu chegara haqiqiy ahamiyat kasb
# etadi, "cheksiz" emas, "Pro'ning 3x"ligini saqlab qoladi.
ULTRA_TOPIC_VISIBLE_LIMIT = 150


def get_topic_unlock_count(plan: str) -> int | None:
    """Berilgan tarif uchun nechta (birinchi) mavzu OCHIQ ekanini qaytaradi."""
    if plan == "pro":
        return PRO_TOPIC_VISIBLE_LIMIT
    if plan == "ultra":
        return ULTRA_TOPIC_VISIBLE_LIMIT
    return FREE_TOPIC_VISIBLE_LIMIT


TEST_MODES = [
    {
        "code": "dtm",
        "name": "DTM rejimi",
        "description": "Davlat imtihoni standarti — 30 ta savol, har to'g'ri javob 3.1 ball (maks. 93).",
        "question_count": 30,
        "time_limit_minutes": 30,
        "subjects": None,  # None = barcha fanlarda mavjud
    },
    {
        "code": "certificate",
        "name": "Sertifikat rejimi",
        "description": "Fan bo'yicha qiyinlashtirilgan mock imtihon, milliy sertifikat bahosi (A+ dan C gacha, 100 ballik).",
        "question_count": 20,
        "time_limit_minutes": 40,
        "subjects": None,
        "exclude_subjects": {"english"},  # ingliz tilida buning o'rniga IELTS/CEFR bor
    },
    {
        "code": "ielts",
        "name": "IELTS rejimi",
        "description": "IELTS Academic uslubidagi savollar — Band 1.0–9.0 baholash.",
        "question_count": 20,
        "time_limit_minutes": 40,
        "subjects": {"english"},
    },
    {
        "code": "cefr",
        "name": "CEFR rejimi",
        "description": "CEFR (A1–C2) darajalash mezonlariga mos savollar.",
        "question_count": 20,
        "time_limit_minutes": 35,
        "subjects": {"english"},
    },
]
TEST_MODE_CODES = {m["code"] for m in TEST_MODES}
TEST_MODE_BY_CODE = {m["code"]: m for m in TEST_MODES}

# Eski nom bilan moslik uchun (onboarding.html "certificates" kutadi) —
# CERTIFICATE_TYPES endi TEST_MODES bilan bir xil manbadan olinadi, shunda
# ikkita alohida ro'yxatni sinxronlab yurishga hojat qolmaydi.
CERTIFICATE_TYPES = [{"code": m["code"], "name": m["name"]} for m in TEST_MODES] + [
    {"code": "none", "name": "Sertifikat kerak emas, shunchaki o'rganaman"},
]
CERTIFICATE_CODES = {c["code"] for c in CERTIFICATE_TYPES}


def get_test_modes_for_subject(subject: str) -> list[dict]:
    """
    Berilgan fan uchun mos test rejimlarini qaytaradi:
    - "subjects" belgilangan bo'lsa — faqat o'sha fanlar uchun (masalan IELTS/CEFR faqat ingliz tili)
    - "exclude_subjects" belgilangan bo'lsa — o'sha fanlarda ko'rsatilmaydi (Sertifikat ingliz tilida emas)
    - ikkalasi ham yo'q bo'lsa — barcha fanlarda ko'rinadi (masalan DTM)
    """
    result = []
    for mode in TEST_MODES:
        allowed_subjects = mode.get("subjects")
        excluded_subjects = mode.get("exclude_subjects")
        if allowed_subjects is not None and subject not in allowed_subjects:
            continue
        if excluded_subjects is not None and subject in excluded_subjects:
            continue
        result.append(_mode_with_exam_rules(subject, mode))
    return result


def _mode_with_exam_rules(subject: str, mode: dict) -> dict:
    """Tarix/biologiya uchun rasmiy tuzilmaga mos savol soni, vaqt va tavsifni ko'rsatadi."""
    import exam_rules as ER
    cfg = ER.tiered_config(subject, mode["code"])
    if cfg is None:
        return mode
    m = dict(mode)
    m["question_count"] = cfg["total"]
    m["time_limit_minutes"] = cfg["time"]
    if cfg.get("desc"):
        m["description"] = cfg["desc"]
        return m
    if cfg is ER.HISTORY_CERT:
        m["description"] = ("Milliy sertifikat (UZBMB): 45 ta savol, 90 daqiqa, 100 ball — siyosiy tarix 29, "
                            "ijtimoiy-iqtisodiy 7, moslashtirish 3, madaniyat va me'morchilik 6 ta. "
                            "Daraja: A+ (70+), A, B+, B, C+, C (46+).")
    elif cfg is ER.HISTORY_DTM:
        m["description"] = ("DTM (BMBA) tarix: majburiy blok 10 ta × 1.1 = 11 ball (15 daq) + mutaxassislik bloki "
                            "30 ta × 3.1 = 93 ball (45 daq).")
    elif cfg is ER.BIOLOGY_DTM:
        m["description"] = ("DTM (BMBA) biologiya: 30 ta savol — 24 yopiq, 3 moslashtirish, 3 ochiq. "
                            "1-fan: har biri 3.1 ball (93), 2-fan: 2.1 ball (63).")
    elif cfg is ER.CHEMISTRY_DTM:
        m["description"] = ("DTM (BMBA) kimyo: 30 ta savol — 24 yopiq, 3 moslashtirish, 3 ochiq (hisoblash). "
                            "1-fan: har biri 3.1 ball (93), 2-fan: 2.1 ball (63).")
    return m

# ---------------------------------------------------------------------------
# TASHQI O'QUV/KURS KABINETI (Mohirdev/Udemy uslubida) — statik katalog.
# Har bir kurs bir nechta darsdan iborat; progress `course_progress`
# jadvalida saqlanadi (bitta yakunlangan dars = bitta yozuv).
# ---------------------------------------------------------------------------
COURSES = [
    {
        "code": "python-basics",
        "category": "Dasturlash",
        "title": "Python bilan dasturlashga kirish",
        "description": "O'zgaruvchilardan boshlab, birinchi dasturingizgacha — nol darajadan.",
        "lessons": [
            {"code": "l1", "title": "Python nima va nega o'rganish kerak", "duration_min": 8,
             "content": "Python — o'qish va yozish oson bo'lgan, dunyoda eng ko'p ishlatiladigan dasturlash tillaridan biri. Veb-saytlar, sun'iy intellekt, ma'lumotlar tahlili va avtomatlashtirish — barchasi Python bilan yaratiladi."},
            {"code": "l2", "title": "O'zgaruvchilar va turlari", "duration_min": 12,
             "content": "O'zgaruvchi — dasturda qiymatni saqlab turadigan nom. Python'da o'zgaruvchi e'lon qilish uchun maxsus kalit so'z kerak emas: masalan `ism = \"Aziz\"` yoki `yosh = 20`."},
            {"code": "l3", "title": "Shartli operatorlar (if/else)", "duration_min": 15,
             "content": "Shartli operatorlar dastur qaysi yo'ldan borishini hal qiladi. `if shart:` bloki shart to'g'ri bo'lsagina bajariladi, aks holda `else:` bloki ishga tushadi."},
            {"code": "l4", "title": "Sikllar: for va while", "duration_min": 15,
             "content": "Sikllar bir xil amalni bir necha marta takrorlash uchun ishlatiladi. `for` — ro'yxat yoki diapazon bo'yicha, `while` — shart to'g'ri bo'lgunicha takrorlaydi."},
        ],
    },
    {
        "code": "web-dev-101",
        "category": "IT",
        "title": "Veb-dasturlash asoslari (HTML, CSS)",
        "description": "Birinchi veb-sahifangizni yaratishni shu kursdan boshlang.",
        "lessons": [
            {"code": "l1", "title": "HTML — sahifa skeleti", "duration_min": 10,
             "content": "HTML veb-sahifaning tuzilishini belgilaydi: sarlavhalar, paragraflar, rasmlar va havolalar — barchasi HTML teglari orqali yoziladi."},
            {"code": "l2", "title": "CSS — dizayn va uslub", "duration_min": 14,
             "content": "CSS HTML elementlariga rang, o'lcham, joylashuv va animatsiya beradi. Bir CSS fayli orqali butun saytning ko'rinishini boshqarish mumkin."},
            {"code": "l3", "title": "Flexbox bilan joylashuv", "duration_min": 16,
             "content": "Flexbox — elementlarni qator yoki ustun shaklida, teng yoki moslashuvchan o'lchamda joylashtirish uchun zamonaviy CSS usuli."},
        ],
    },
    {
        "code": "dtm-strategy",
        "category": "Fanlar",
        "title": "DTM'ga tayyorgarlik strategiyasi",
        "description": "Vaqtni to'g'ri taqsimlash, xato ustida ishlash va stressni boshqarish.",
        "lessons": [
            {"code": "l1", "title": "Test topshirishda vaqtni boshqarish", "duration_min": 9,
             "content": "Har bir savolga qancha vaqt ajratish kerakligini oldindan hisoblab qo'ying: umumiy vaqtni savollar soniga bo'ling va murakkab savollarga ko'proq vaqt qoldiring."},
            {"code": "l2", "title": "Xatolar ustida ishlash usuli", "duration_min": 11,
             "content": "Har bir noto'g'ri javobni alohida yozib boring: nima uchun xato qildingiz — bilim yetishmovchiligimi yoki e'tiborsizlikmi? Bu ikkisi butunlay boshqacha yechim talab qiladi."},
        ],
    },
]
COURSE_BY_CODE = {c["code"]: c for c in COURSES}


def get_lesson(course_code: str, lesson_code: str) -> dict | None:
    course = COURSE_BY_CODE.get(course_code)
    if not course:
        return None
    for lesson in course["lessons"]:
        if lesson["code"] == lesson_code:
            return lesson
    return None


class Base(DeclarativeBase):
    pass


class WebUser(Base):
    __tablename__ = "web_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(100), default="")
    plan: Mapped[str] = mapped_column(String(20), default="free")  # free | pro | ultra

    # --- Onboarding (kirishda majburiy tanlanadi) ---
    subject: Mapped[str | None] = mapped_column(String(30), nullable=True)
    level: Mapped[str | None] = mapped_column(String(20), nullable=True)
    certificate_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    onboarding_done: Mapped[bool] = mapped_column(Boolean, default=False)

    joined_at: Mapped[date] = mapped_column(Date, default=date.today)
    streak_days: Mapped[int] = mapped_column(Integer, default=0)
    last_active_date: Mapped[date] = mapped_column(Date, default=date.today)

    # --- Tarifga bog'liq kunlik limitlar (AI repetitor bilan suhbat) ---
    # Har kuni 00:00'da (birinchi so'rov kelganda) avtomatik nolga tushadi —
    # alohida "reset" vazifasi kerak emas, shunchaki sana solishtiriladi.
    ai_messages_today: Mapped[int] = mapped_column(Integer, default=0)
    ai_messages_date: Mapped[date] = mapped_column(Date, default=date.today)

    # --- Shaxsiy sozlamalar (profil sahifasidan tahrirlanadi) ---
    avatar_color: Mapped[str] = mapped_column(String(12), default="")
    daily_goal: Mapped[int] = mapped_column(Integer, default=10)        # kuniga nechta savol
    target_percent: Mapped[int] = mapped_column(Integer, default=90)    # maqsadli o'rtacha natija, %

    # --- Balans (hamyon) — hozircha faqat demo/vizual to'ldirish, haqiqiy
    # to'lov provayderi (Click/Paynet/SQB) ulangandan keyin real bo'ladi ---
    balance_som: Mapped[int] = mapped_column(Integer, default=0)

    # "Qaytib kelgan foydalanuvchi" bildirishnomasi uchun (14+ kun uzilishdan
    # keyin qaytsa) — har muvaffaqiyatli kirishda yangilanadi.
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)


class WebQuizLog(Base):
    """
    Foydalanuvchining har bir yechgan testi — master arxitekturadagi
    `test_attempts` jadvaliga mos keladi: fan, tanlangan rejim (DTM/Sertifikat),
    sarflagan vaqti va natijasi shu yerda saqlanadi.
    """
    __tablename__ = "web_quiz_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    subject: Mapped[str] = mapped_column(String(30))
    level: Mapped[str] = mapped_column(String(20), default="boshlangich")
    topic: Mapped[str] = mapped_column(String(200), default="")
    mode: Mapped[str] = mapped_column(String(20), default="dtm")  # "dtm" | "certificate" | "ielts" | "cefr"
    correct_count: Mapped[int] = mapped_column(Integer, default=0)
    total_count: Mapped[int] = mapped_column(Integer, default=0)
    time_spent_seconds: Mapped[int] = mapped_column(Integer, default=0)
    # DTM rejimida: to'plangan ball (3.1 x to'g'ri javoblar). Sertifikat
    # rejimida: erishilgan Band nomi (masalan "B2"). Ikkalasi ham bitta
    # ustunda matn sifatida saqlanadi — chunki bir vaqtning o'zida faqat
    # bittasi kerak bo'ladi.
    score_label: Mapped[str] = mapped_column(String(40), default="")
    # To'liq savol-javob-izoh JSON matn sifatida saqlanadi, keyin "qayta ko'rish" uchun kerak bo'ladi
    questions_json: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class UserCertificate(Base):
    """
    Muvaffaqiyatli yakunlangan DTM/Sertifikat/IELTS/CEFR testi yoki kurs
    uchun avtomatik generatsiya qilingan rasmiy sertifikat.
    """
    __tablename__ = "user_certificates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    verification_id: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    subject: Mapped[str] = mapped_column(String(30))
    mode: Mapped[str] = mapped_column(String(20), default="dtm")
    score_label: Mapped[str] = mapped_column(String(40), default="")  # "180 ball" | "CEFR B2"
    # PDF sertifikatda "necha to'g'ri / necha savol / necha foiz" ko'rsatish
    # uchun raqamli tafsilotlar ham alohida saqlanadi (faqat matn label
    # yetarli emas — rasmiy sertifikat aniq raqam talab qiladi).
    correct_count: Mapped[int] = mapped_column(Integer, default=0)
    total_count: Mapped[int] = mapped_column(Integer, default=0)
    percent: Mapped[int] = mapped_column(Integer, default=0)
    quiz_log_id: Mapped[int | None] = mapped_column(ForeignKey("web_quiz_log.id"), nullable=True)
    issued_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Announcement(Base):
    """
    Admin tomonidan yuboriladigan, BARCHA foydalanuvchilarga tarqatiladigan
    e'lon — "qo'ng'iroq" (bell) menyusida ko'rinadi.
    """
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), default="")
    body: Mapped[str] = mapped_column(String(1000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Notification(Base):
    """
    SHAXSIY bildirishnomalar — bitta FOYDALANUVCHIGA tegishli hodisalar:
    Yordam xabariga javob kelganda, yangi mavzu qo'shilganda, ro'yxatdan
    o'tganda ("Xush kelibsiz") va uzoq vaqtdan keyin qaytib kelganda
    ("Xush kelibsiz, sog'indik"). `Announcement`dan farqli — bu yerda har
    bir yozuv FAQAT bitta `user_id`ga ko'rinadi (broadcast emas). Qo'ng'iroq
    menyusi ikkalasini (Announcement + Notification) BIRLASHTIRIB ko'rsatadi.
    """
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"), index=True)
    type: Mapped[str] = mapped_column(String(30))  # support_reply | new_topic | welcome | welcome_back
    title: Mapped[str] = mapped_column(String(200), default="")
    body: Mapped[str] = mapped_column(String(1000), default="")
    source_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)


class SupportMessage(Base):
    """
    FOYDALANUVCHIDAN ADMINGA YOZILGAN XABAR ("Yordam" bo'limi). Admin panelda
    "Xabarlar" bo'limida ro'yxat sifatida ko'rinadi, o'qilmaganlar soni
    sidebar'dagi qo'ng'iroq belgisida ko'rsatiladi — admin har doim yangi
    xabar kelganini darhol bilib turishi uchun.
    """
    __tablename__ = "support_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    subject: Mapped[str] = mapped_column(String(200), default="")
    body: Mapped[str] = mapped_column(String(2000))
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    admin_reply: Mapped[str] = mapped_column(String(2000), default="")
    replied_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class BalanceTransaction(Base):
    """
    Balans (hamyon) to'ldirish tarixi — hozircha faqat demo/vizual: haqiqiy
    to'lov provayderi (Click/Paynet/SQB) ulanganda shu jadval real
    tranzaksiyalar uchun ishlatiladi.
    """
    __tablename__ = "balance_transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    amount_som: Mapped[int] = mapped_column(Integer, default=0)
    method: Mapped[str] = mapped_column(String(20), default="click")  # click | paynet | sqb
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class CourseProgress(Base):
    """
    Tashqi O'quv/KURS kabinetidagi (Mohirdev uslubidagi) darslar
    o'zlashtirilishi — har bir yakunlangan dars uchun bitta yozuv.
    """
    __tablename__ = "course_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    course_code: Mapped[str] = mapped_column(String(60))
    lesson_code: Mapped[str] = mapped_column(String(60))
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class ChatLog(Base):
    """
    Foydalanuvchi va AI (Claude yoki Gemini) o'rtasidagi suhbat tarixi.
    ai_provider ustuni qaysi AI javob berganini belgilaydi ("claude" / "gemini").
    """
    __tablename__ = "chat_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    ai_provider: Mapped[str] = mapped_column(String(20))  # "claude" | "gemini"
    question: Mapped[str] = mapped_column(String(1000))
    answer: Mapped[str] = mapped_column(String(4000))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TopicProgress(Base):
    """
    MAVZULASHTIRILGAN TEST TIZIMI (SAT Question Bank uslubida):
    har bir (foydalanuvchi, fan, rejim, mavzu) juftligi uchun bitta yozuv —
    nechta savol ishlangan, nechtasi to'g'ri, va mavzu tugallanganmi.

    "Tugallangan" mavzu — foydalanuvchi shu mavzudagi barcha savollarni
    kamida bir marta TO'G'RI ishlagan degani (quiz_engine.py shu yerga
    qarab, allaqachon to'g'ri ishlangan savollarni boshqa urinishda
    QAYTA BERMAYDI — xato qilingan savol esa keyingi safar QAYTA CHIQADI,
    to'g'ri javob berilguncha).
    """
    __tablename__ = "topic_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    subject: Mapped[str] = mapped_column(String(30))
    mode: Mapped[str] = mapped_column(String(20))
    topic: Mapped[str] = mapped_column(String(200))
    # Shu mavzuda foydalanuvchi TO'G'RI javob bergan savollarning matnlari
    # (yoki barqaror ID'lari) vergul bilan emas, JSON ro'yxat sifatida
    # saqlanadi — shu savollar boshqa urinishda qayta berilmaydi.
    solved_question_keys_json: Mapped[str] = mapped_column(String(4000), default="[]")
    total_questions: Mapped[int] = mapped_column(Integer, default=0)
    solved_count: Mapped[int] = mapped_column(Integer, default=0)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    last_practiced_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class DuplicateQuestionError(Exception):
    """Shu fan va rejimda bir xil matnli savol allaqachon mavjud (admin qo'shish/tahrirlashda)."""


class Question(Base):
    """
    SAVOLLAR BANKI — ENDI BAZADA (avval static_questions.py faylida qattiq
    yozilgan edi). Bu o'zgarish admin panel orqali savollarni qo'shish,
    tahrirlash va o'chirishga imkon beradi — kod o'zgartirmasdan, kodni
    qayta joylashtirmasdan (deploy qilmasdan).

    Birinchi ishga tushirishda (init_web_db) bu jadval bo'sh bo'lsa,
    static_questions.py'dagi barcha eski savollar AVTOMATIK shu yerga
    ko'chiriladi (bir martalik migratsiya) — hech qanday mavjud savol
    yo'qolmaydi.
    """
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(30), index=True)
    mode: Mapped[str] = mapped_column(String(20), index=True)
    topic: Mapped[str] = mapped_column(String(150), default="Umumiy", index=True)
    mock_test: Mapped[str] = mapped_column(String(80), default="")
    question: Mapped[str] = mapped_column(String(2000))
    options_json: Mapped[str] = mapped_column(String(3000))  # JSON: ["variant A", "variant B", ...]
    correct_index: Mapped[int] = mapped_column(Integer)
    explanation: Mapped[str] = mapped_column(String(2000), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)  # False = admin vaqtincha yashirgan
    figure_json: Mapped[str] = mapped_column(Text, default="")  # chizma/shakl: {"q": spec|null, "o": [spec|null x4]} (figure.js formati)
    style_json: Mapped[str] = mapped_column(String(1000), default="")  # admin tahrirlagan ko'rinish (shrift, joylashuv, masofa) — JSON
    is_final_test: Mapped[bool] = mapped_column(Boolean, default=False)  # True = "Yakuniy test" (haftalik yopiq mavzular bo'yicha, har doim TO'LIQ savol soni beriladi — tarifdan qat'iy nazar)
    source_file: Mapped[str] = mapped_column(String(200), default="", index=True)  # import qilingan fayl nomi (bo'sh = qo'lda qo'shilgan)
    source_no: Mapped[int] = mapped_column(Integer, default=0)  # savol shu faylda nechanchi bo'lgan
    # --- v202: rasmiy imtihon tuzilmasi uchun (tarix/biologiya) ---
    grade: Mapped[int] = mapped_column(Integer, default=0)  # sinf (6..11); 0 = belgilanmagan
    difficulty: Mapped[int] = mapped_column(Integer, default=0)  # 1 oson, 2 o'rta, 3 qiyin; 0 = belgilanmagan (o'rta hisoblanadi)
    block: Mapped[str] = mapped_column(String(20), default="")  # siyosiy | ijtimoiy | moslash | madaniyat
    qtype: Mapped[str] = mapped_column(String(10), default="closed")  # closed | open | match
    min_plan: Mapped[int] = mapped_column(Integer, default=0)  # 0 bepul, 1 Pro, 2 Ultra — shu tarifdan boshlab ko'rinadi
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TopicMeta(Base):
    """SINF -> MAVZU -> TARIF tuzilmasi (tarix va biologiya uchun): har bir mavzu qaysi sinfga
    tegishli, tartib raqami va qaysi tarifdan boshlab ochilishi."""
    __tablename__ = "topic_meta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(30), index=True)
    mode: Mapped[str] = mapped_column(String(20), index=True)
    topic: Mapped[str] = mapped_column(String(150))
    code: Mapped[str] = mapped_column(String(20), default="")
    grade: Mapped[int] = mapped_column(Integer, default=0)
    tier: Mapped[str] = mapped_column(String(10), default="free")  # free | pro | ultra
    order_no: Mapped[int] = mapped_column(Integer, default=0)
    block: Mapped[str] = mapped_column(String(20), default="siyosiy")


class Topic(Base):
    """Admin yaratgan mavzu (savollar bo'lmasa ham ro'yxatda ko'rinadi)."""
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(30), index=True)
    mode: Mapped[str] = mapped_column(String(20), index=True)
    name: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class DeletedQuestion(Base):
    """
    O'CHIRILGAN SAVOLLAR "QABRISTONI" (tombstone): admin savolni o'chirganda
    yoki matnini o'zgartirganda eski matn shu yerga yoziladi. Server qayta
    ishga tushganda static_questions.py'dan sinxronlash shu matnlarni QAYTA
    QO'SHMAYDI — shu sababli o'chirilgan savol haqiqatan ham DOIMIY yo'qoladi.
    """
    __tablename__ = "deleted_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(30), index=True)
    mode: Mapped[str] = mapped_column(String(20), index=True)
    question_key: Mapped[str] = mapped_column(String(64), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class AdminLog(Base):
    """
    ADMIN AMALLARI JURNALI — kim, qachon, nima qildi. Ayniqsa foydalanuvchi
    o'chirish kabi QAYTARIB BO'LMAYDIGAN amallar uchun javobgarlik/kuzatuv.
    """
    __tablename__ = "admin_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    admin_username: Mapped[str] = mapped_column(String(60))
    action: Mapped[str] = mapped_column(String(60))
    detail: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class QuestionReport(Base):
    """Foydalanuvchi test paytida yuborgan SHIKOYAT (savol bo'yicha kamchilik / xato). Admin panelda ko'rib chiqiladi,
    Claude tahlil qiladi va (admin tasdiqlasa yoki avto-rejimda) savol tuzatiladi."""
    __tablename__ = "question_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    user_name: Mapped[str] = mapped_column(String(120), default="")
    question_id: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
    subject: Mapped[str] = mapped_column(String(30), default="", index=True)
    mode: Mapped[str] = mapped_column(String(20), default="")
    topic: Mapped[str] = mapped_column(String(150), default="")
    question_text: Mapped[str] = mapped_column(Text, default="")
    options_json: Mapped[str] = mapped_column(Text, default="")
    correct_index: Mapped[int] = mapped_column(Integer, default=-1)
    explanation: Mapped[str] = mapped_column(Text, default="")
    selected_answer: Mapped[str] = mapped_column(String(300), default="")
    category: Mapped[str] = mapped_column(String(40), default="boshqa")
    message: Mapped[str] = mapped_column(Text, default="")
    # new | analyzed | fixed | dismissed
    status: Mapped[str] = mapped_column(String(20), default="new", index=True)
    ai_verdict: Mapped[str] = mapped_column(String(20), default="")      # error | ok | unclear
    ai_confidence: Mapped[int] = mapped_column(Integer, default=0)
    ai_note: Mapped[str] = mapped_column(Text, default="")
    ai_fix_json: Mapped[str] = mapped_column(Text, default="")
    admin_note: Mapped[str] = mapped_column(String(500), default="")
    attempt_token: Mapped[str] = mapped_column(String(64), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)


class SiteSetting(Base):
    """
    ADMIN PANEL ORQALI BOSHQARILADIGAN UMUMIY SOZLAMALAR (key-value).
    Maqsad: admin panel "butun saytni boshqarishi" uchun — tarif limitlari
    (PLAN_LIMITS) va sayt e'loni (announcement banner) kabi narsalarni kod
    o'zgartirmasdan, serverni qayta ishga tushirmasdan, to'g'ridan-to'g'ri
    admin paneldan o'zgartirish mumkin. Qiymat JSON matn sifatida saqlanadi.
    """
    __tablename__ = "site_settings"

    key: Mapped[str] = mapped_column(String(60), primary_key=True)
    value: Mapped[str] = mapped_column(String(4000), default="")
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class AiMessageLog(Base):
    """
    AI suhbat SIRPANUVCHI OYNA (sliding window) limiti uchun — har bir
    ruxsat etilgan AI so'rov shu yerga vaqt belgisi bilan yoziladi.
    Eski "kunlik hisoblagich" (ai_messages_today/ai_messages_date, WebUser
    jadvalida) endi ishlatilmaydi — soat asosidagi aniq oyna kerak edi
    ("limit birdaniga emas, soatga qarab ochilsin" talabiga mos).
    """
    __tablename__ = "ai_message_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)


class SpeakingWritingLog(Base):
    """
    IELTS/Sertifikat Speaking va Writing mashqlari tarixi. "chat ko'rinmasin,
    lekin tarix saqlansin" talabiga mos — foydalanuvchi mashq paytida
    chat oqimini ko'rmaydi, lekin yakunda natija shu jadvalga yoziladi va
    "Tarix" bo'limida ko'rsatiladi.
    """
    __tablename__ = "speaking_writing_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    section: Mapped[str] = mapped_column(String(10))  # "speaking" | "writing"
    topic_id: Mapped[str] = mapped_column(String(60))
    topic_title: Mapped[str] = mapped_column(String(200), default="")
    # Speaking: JSON ro'yxat [{"question": "...", "answer": "..."}]
    # Writing: insho matnining o'zi (JSON emas, oddiy matn)
    content: Mapped[str] = mapped_column(String(8000), default="")
    band_score: Mapped[str] = mapped_column(String(10), default="")
    feedback: Mapped[str] = mapped_column(String(3000), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class MissedQuestion(Base):
    """
    XATO QILINGAN SAVOLLAR BANKI ("Mavzusiz test" / qaytadan ko'rib chiqish
    uchun): foydalanuvchi biror savolga xato javob bersa, shu yerga
    qo'shiladi. To'g'ri javob berilganda shu yerdan olib tashlanadi.
    "Mavzusiz test" bo'limi aynan shu jadvaldan savol tanlaydi — maqsad,
    foydalanuvchi vaqti-vaqti bilan o'zining eski xatolarini takrorlab,
    haqiqatan o'rganib olganini tekshirish.
    """
    __tablename__ = "missed_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("web_users.id"))
    subject: Mapped[str] = mapped_column(String(30))
    mode: Mapped[str] = mapped_column(String(20))
    topic: Mapped[str] = mapped_column(String(200), default="")
    question_key: Mapped[str] = mapped_column(String(64), index=True)
    question_json: Mapped[str] = mapped_column(Text)
    missed_count: Mapped[int] = mapped_column(Integer, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class MockTest(Base):
    """Tayyor mock-variant: admin yaratadi (bankdan yoki hujjatdan), foydalanuvchi bitta bosish bilan yechadi."""
    __tablename__ = "mock_tests"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String(30), index=True)
    mode: Mapped[str] = mapped_column(String(20), index=True)
    name: Mapped[str] = mapped_column(String(120))
    variant_no: Mapped[int] = mapped_column(Integer, default=1)
    question_ids_json: Mapped[str] = mapped_column(Text, default="[]")
    min_plan: Mapped[int] = mapped_column(Integer, default=1)  # 0 bepul, 1 Pro, 2 Ultra
    time_minutes: Mapped[int] = mapped_column(Integer, default=0)  # 0 = fan standarti
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_by: Mapped[str] = mapped_column(String(60), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class QFigure(Base):
    """Admin yuklagan/PDF dan kesilgan chizma rasmlari (Vercel'da disk yo'q — baza ichida saqlanadi)."""
    __tablename__ = "qfigures"
    name: Mapped[str] = mapped_column(String(64), primary_key=True)
    data: Mapped[bytes] = mapped_column(LargeBinary)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


# ---------------- MOCK-VARIANTLAR ----------------
async def create_mock(subject: str, mode: str, name: str, variant_no: int, ids: list[int], min_plan: int,
                      created_by: str = "", time_minutes: int = 0) -> "MockTest":
    import json as _j
    async with async_session() as session:
        m = MockTest(subject=subject, mode=mode, name=name[:120], variant_no=variant_no,
                     question_ids_json=_j.dumps(ids), min_plan=min_plan, time_minutes=time_minutes, created_by=created_by[:60])
        session.add(m)
        await session.commit()
        await session.refresh(m)
        return m


async def list_mocks(subject: str | None = None, mode: str | None = None, active_only: bool = True) -> list["MockTest"]:
    async with async_session() as session:
        q = select(MockTest).order_by(MockTest.subject, MockTest.mode, MockTest.name, MockTest.variant_no)
        if subject:
            q = q.where(MockTest.subject == subject)
        if mode:
            q = q.where(MockTest.mode == mode)
        if active_only:
            q = q.where(MockTest.is_active == True)  # noqa: E712
        return list((await session.execute(q)).scalars().all())


async def get_mock(mock_id: int) -> "MockTest | None":
    async with async_session() as session:
        return await session.get(MockTest, mock_id)


async def delete_mock(mock_id: int) -> bool:
    async with async_session() as session:
        m = await session.get(MockTest, mock_id)
        if m is None:
            return False
        await session.delete(m)
        await session.commit()
        return True


async def set_mock_active(mock_id: int, active: bool) -> bool:
    async with async_session() as session:
        m = await session.get(MockTest, mock_id)
        if m is None:
            return False
        m.is_active = active
        await session.commit()
        return True


async def questions_by_ids(ids: list[int]) -> list[dict]:
    """Savollarni BERILGAN TARTIBDA qaytaradi (faqat faollari)."""
    if not ids:
        return []
    async with async_session() as session:
        rows = (await session.execute(select(Question).where(Question.id.in_(ids), Question.is_active == True))).scalars().all()  # noqa: E712
    by_id = {q.id: q for q in rows}
    return [_question_to_dict(by_id[i]) for i in ids if i in by_id]


async def save_qfigs(items: dict) -> None:
    if not items:
        return
    async with async_session() as session:
        for name, data in items.items():
            if await session.get(QFigure, name) is None:
                session.add(QFigure(name=name, data=data))
        await session.commit()


async def get_qfig(name: str) -> bytes | None:
    async with async_session() as session:
        row = await session.get(QFigure, name)
        return row.data if row is not None else None


# ---------------------------------------------------------------------------
# ULANISH HAVUZI (connection pool) — KO'P FOYDALANUVCHI BIR VAQTDA ISHLAGANDA
# muhim: PostgreSQL'ga o'tilganda (DATABASE_URL berilganda) har bir so'rov
# uchun qayta-qayta yangi ulanish ochish o'rniga, oldindan tayyor ulanishlar
# havuzidan foydalaniladi — bu minglab bir vaqtdagi foydalanuvchida ham
# serverni sekinlashtirmaydi. SQLite'da bu sozlamalar MA'NOSIZ (bitta fayl,
# NullPool ishlatiladi) — shuning uchun faqat PostgreSQL'da qo'llaniladi.
# ---------------------------------------------------------------------------
if IS_SQLITE:
    engine = create_async_engine(DATABASE_URL)
elif os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    # Serverless: har chaqiruv alohida event loop/instans bo'lishi mumkin — havuzsiz (NullPool),
    # Neon'ning "-pooler" manzili bilan birga eng barqaror ishlaydi.
    from sqlalchemy.pool import NullPool
    engine = create_async_engine(DATABASE_URL, poolclass=NullPool, connect_args={"statement_cache_size": 0})
else:
    engine = create_async_engine(
        DATABASE_URL,
        pool_size=20,          # doimiy ochiq ulanishlar soni
        max_overflow=20,       # cho'qqi yuklamada qo'shimcha vaqtinchalik ulanishlar
        pool_timeout=30,       # havuzda bo'sh ulanish kutish chegarasi (soniya)
        pool_recycle=1800,     # 30 daqiqada ulanishni yangilaydi ("stale connection" xatosining oldini oladi)
        pool_pre_ping=True,    # har bir ulanishni ishlatishdan oldin "tirikligini" tekshiradi
    )
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_web_db():
    for _attempt in range(3):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            break
        except Exception as exc:  # noqa: BLE001 — bir vaqtda ikki server nusxasi jadval yaratsa (Vercel)
            if _attempt == 2:
                raise
            logger.warning("Jadvallarni yaratishda to'qnashuv, qayta urinish: %s", type(exc).__name__)
            import asyncio as _aio
            await _aio.sleep(1.5)
    await _migrate_missing_columns()
    await _wipe_legacy_bank_once()
    await _load_plan_limit_overrides()
    await load_env_overrides(force=True)
    try:
        import runtime
        import exam_db
        if runtime.IS_VERCEL and os.getenv("SEED_ON_START", "") != "1":
            # Serverless: katta seeding bitta so'rovga sig'maydi — u BO'LAKLAB, avtomatik bajariladi
            # (main.py: /api/seed-step va birinchi so'rovlardagi fon vazifasi). Bu yerda bloklamaymiz.
            pass
        else:
            await exam_db.seed_exam_content()
    except Exception:  # noqa: BLE001 — seed xatosi serverni to'xtatmasin
        logger.exception("Tayyor savollar bazasini yuklashda xatolik (sayt ishlashda davom etadi).")


# ---------------------------------------------------------------------------
# ADMIN SOZLAMALARI (SiteSetting key-value) — generik yordamchi funksiyalar
# ---------------------------------------------------------------------------
async def get_setting(key: str, default: str = "") -> str:
    async with async_session() as session:
        row = await session.get(SiteSetting, key)
        return row.value if row is not None else default


async def set_setting(key: str, value: str) -> None:
    async with async_session() as session:
        row = await session.get(SiteSetting, key)
        if row is None:
            row = SiteSetting(key=key, value=value, updated_at=datetime.utcnow())
            session.add(row)
        else:
            row.value = value
            row.updated_at = datetime.utcnow()
        await session.commit()


async def claim_lock(name: str, ttl: int = 90) -> bool:
    """Oddiy taqsimlangan qulf (SiteSetting orqali): bir vaqtda bitta instans ishlasin. ttl — soniya (qulf eskirishi)."""
    key = "lock:" + name
    now = int(time.time())
    async with async_session() as session:
        row = await session.get(SiteSetting, key)
        if row is None:
            try:
                session.add(SiteSetting(key=key, value=str(now), updated_at=datetime.utcnow()))
                await session.commit()
                return True
            except Exception:  # noqa: BLE001 — boshqa instans birinchi bo'lib yozdi
                await session.rollback()
                return False
        try:
            last = int(row.value or "0")
        except ValueError:
            last = 0
        if now - last < ttl:
            return False
        res = await session.execute(
            SiteSetting.__table__.update().where(SiteSetting.key == key, SiteSetting.value == row.value)
            .values(value=str(now), updated_at=datetime.utcnow())
        )
        await session.commit()
        return (res.rowcount or 0) > 0


async def release_lock(name: str) -> None:
    await set_setting("lock:" + name, "0")


# --- Kalit/sozlamalar (AI kalitlari, Google, Turnstile) — admin panel orqali bazada saqlanadi.
#     Vercel'da .env yozib bo'lmaydi, shuning uchun qiymatlar SiteSetting'da ("env:NAME") turadi
#     va ishga tushganda os.environ'ga yuklanadi (bazadagi qiymat muhit o'zgaruvchisidan ustun).
ENV_OVERRIDE_NAMES = (
    "ANTHROPIC_API_KEY", "GEMINI_API_KEY", "GEMINI_MODEL", "CLAUDE_MODEL",
    "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "TURNSTILE_SITE_KEY", "TURNSTILE_SECRET_KEY",
    "TURNSTILE_MODE", "TURNSTILE_FALLBACK",
)
# Maxfiy kalitlar bazada SHIFRLANGAN saqlanadi (Fernet, kalit — WEB_SECRET_KEY dan olinadi). Ochiq sozlamalar (rejim, model) oddiy.
_SECRET_OVERRIDES = {"ANTHROPIC_API_KEY", "GEMINI_API_KEY", "GOOGLE_CLIENT_SECRET", "TURNSTILE_SECRET_KEY"}
_env_override_loaded_at = 0.0
# Ishga tushgandagi (muhit/.env dagi) asl qiymatlar — admin panelda "tozalash" bosilganda shunga qaytariladi
_ENV_BASELINE = {n: os.environ.get(n) for n in ENV_OVERRIDE_NAMES}


def _fernet():
    import base64
    import hashlib
    from cryptography.fernet import Fernet
    import auth as _auth
    key = base64.urlsafe_b64encode(hashlib.sha256(b"longouz-keys-v1:" + str(_auth.SECRET_KEY).encode()).digest())
    return Fernet(key)


def _enc(name: str, value: str) -> str:
    if name not in _SECRET_OVERRIDES:
        return value
    try:
        return "enc1:" + _fernet().encrypt(value.encode()).decode()
    except Exception:  # noqa: BLE001
        logger.warning("Kalitni shifrlab bo'lmadi — saqlanmadi.", exc_info=True)
        raise


def _dec(value: str) -> str:
    if not value.startswith("enc1:"):
        return value
    try:
        return _fernet().decrypt(value[5:].encode()).decode()
    except Exception:  # noqa: BLE001
        logger.warning("Bazadagi kalitni ochib bo'lmadi (WEB_SECRET_KEY o'zgargan bo'lishi mumkin) — o'tkazib yuborildi.")
        return ""


async def save_env_override(name: str, value: str) -> None:
    if name in ENV_OVERRIDE_NAMES:
        await set_setting("env:" + name, _enc(name, value))


async def clear_env_override(name: str) -> None:
    if name not in ENV_OVERRIDE_NAMES:
        return
    await set_setting("env:" + name, "")
    base = _ENV_BASELINE.get(name)
    if base:
        os.environ[name] = base
    else:
        os.environ.pop(name, None)


async def env_override_names() -> set[str]:
    """Qaysi kalitlar admin panel orqali (bazada) saqlangan."""
    try:
        async with async_session() as session:
            rows = (await session.execute(select(SiteSetting).where(SiteSetting.key.like("env:%")))).scalars().all()
        return {r.key[4:] for r in rows if (r.value or "").strip()}
    except Exception:  # noqa: BLE001
        return set()


async def load_env_overrides(force: bool = False) -> None:
    global _env_override_loaded_at
    if not force and time.time() - _env_override_loaded_at < 45:
        return
    _env_override_loaded_at = time.time()
    try:
        async with async_session() as session:
            rows = (await session.execute(select(SiteSetting).where(SiteSetting.key.like("env:%")))).scalars().all()
        for row in rows:
            name = row.key[4:]
            if name in ENV_OVERRIDE_NAMES and (row.value or "").strip():
                val = _dec(row.value.strip())
                if val:
                    os.environ[name] = val
            elif name in ENV_OVERRIDE_NAMES:      # admin "tozalash" bosgan — asl (muhit) qiymatga qaytamiz
                base = _ENV_BASELINE.get(name)
                if base:
                    os.environ[name] = base
                else:
                    os.environ.pop(name, None)
    except Exception:  # noqa: BLE001
        logger.debug("env override yuklanmadi", exc_info=True)


# --- Tarif limitlari: admin panel orqali qayta yozilishi mumkin bo'lgan ustama ---
_PLAN_LIMIT_OVERRIDES: dict = {}


async def _load_plan_limit_overrides() -> None:
    """Server ishga tushganda DB'dan saqlangan admin o'zgartirishlarini o'qiydi."""
    import json as _json
    global _PLAN_LIMIT_OVERRIDES
    raw = await get_setting("plan_limits_override", "")
    if raw:
        try:
            _PLAN_LIMIT_OVERRIDES = _json.loads(raw)
        except (ValueError, TypeError):
            logger.warning("plan_limits_override JSON buzilgan, standart qiymatlar ishlatiladi.")
            _PLAN_LIMIT_OVERRIDES = {}


async def admin_update_plan_limits(overrides: dict) -> None:
    """
    Admin panel /admin/settings orqali chaqiriladi. `overrides` shakli:
      {"free": {"ai_daily": 15, "full_mock_access": false}, "pro": {...}, "ultra": {...}}
    ai_daily = None (yoki "unlimited") -> cheksiz. DB'ga yoziladi VA darhol
    xotiradagi qiymatga qo'llanadi — serverni qayta ishga tushirish shart emas.
    """
    global _PLAN_LIMIT_OVERRIDES
    clean: dict = {}
    for plan in ("free", "pro", "ultra"):
        if plan not in overrides:
            continue
        entry = overrides[plan]

        def _parse_optional_int(raw, fallback_key):
            if raw in (None, "", "unlimited", "cheksiz"):
                return None
            try:
                return max(0, int(raw))
            except (ValueError, TypeError):
                return PLAN_LIMITS.get(plan, {}).get(fallback_key)

        ai_window_hours = entry.get("ai_window_hours")
        try:
            ai_window_hours_val = max(1, int(ai_window_hours))
        except (ValueError, TypeError):
            ai_window_hours_val = PLAN_LIMITS.get(plan, {}).get("ai_window_hours", 3)

        clean[plan] = {
            "ai_daily": _parse_optional_int(entry.get("ai_daily"), "ai_daily"),
            "full_mock_access": bool(entry.get("full_mock_access")),
            "topic_question_count": _parse_optional_int(entry.get("topic_question_count"), "topic_question_count"),
            "ai_window_hours": ai_window_hours_val,
        }
    _PLAN_LIMIT_OVERRIDES = clean
    import json as _json
    await set_setting("plan_limits_override", _json.dumps(clean))


# --- Bildirishnomalar tarixi (qo'ng'iroq menyusi) — admin bir nechta e'lonni
# ketma-ket yuboradi va foydalanuvchi ularni ro'yxat sifatida ko'radi. Yagona
# "sayt e'loni" banneri (avval shu yerda edi) olib tashlandi — barcha
# bildirishnomalar endi FAQAT qo'ng'iroq (bell) menyusi orqali ko'rinadi. ---
async def create_announcement(title: str, body: str) -> Announcement:
    async with async_session() as session:
        item = Announcement(title=(title or "").strip()[:200], body=(body or "").strip()[:1000])
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item


async def list_announcements_admin(limit: int = 50) -> list[Announcement]:
    async with async_session() as session:
        result = await session.execute(
            select(Announcement).order_by(Announcement.created_at.desc()).limit(limit)
        )
        return list(result.scalars().all())


async def list_active_announcements(limit: int = 20) -> list[dict]:
    async with async_session() as session:
        result = await session.execute(
            select(Announcement)
            .where(Announcement.is_active == True)  # noqa: E712
            .order_by(Announcement.created_at.desc())
            .limit(limit)
        )
        items = result.scalars().all()
        return [
            {
                "id": a.id,
                "title": a.title,
                "body": a.body,
                "created_at": a.created_at.strftime("%Y-%m-%d %H:%M"),
            }
            for a in items
        ]


async def deactivate_announcement(announcement_id: int) -> None:
    async with async_session() as session:
        item = await session.get(Announcement, announcement_id)
        if item:
            item.is_active = False
            await session.commit()


# ---------------------------------------------------------------------------
# SHAXSIY BILDIRISHNOMALAR (Notification) — qo'ng'iroq menyusi shu yerdan +
# yuqoridagi Announcement'dan BIRLASHTIRIB o'qiydi (get_notifications_for_user).
# ---------------------------------------------------------------------------

NOTIFICATION_TITLES = {
    "support_reply": "Yordam so'roviga javob keldi",
    "new_topic": "Yangi mavzu qo'shildi",
    "welcome": "Xush kelibsiz!",
    "welcome_back": "Sizni sog'indik!",
}


async def create_notification(user_id: int, type: str, body: str, title: str = "", source_id: int | None = None) -> Notification:
    async with async_session() as session:
        item = Notification(
            user_id=user_id, type=type,
            title=(title or NOTIFICATION_TITLES.get(type, "Bildirishnoma"))[:200],
            body=(body or "").strip()[:1000],
            source_id=source_id,
        )
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item


async def get_notifications_for_user(user_id: int, limit: int = 20) -> list[dict]:
    """
    Qo'ng'iroq (bell) menyusi shu yerdan o'qiydi — admin tomonidan BARCHAGA
    yuborilgan e'lonlar (Announcement) va shu foydalanuvchiga shaxsiy tegishli
    hodisalar (Notification) BITTA, vaqt bo'yicha tartiblangan ro'yxatga
    birlashtiriladi. Har bir element uchun "ts" (Unix millisekund) — frontend
    "oxirgi ko'rilgan vaqt"ni shu bo'yicha solishtiradi (localStorage'da).
    """
    async with async_session() as session:
        ann_result = await session.execute(
            select(Announcement).where(Announcement.is_active == True)  # noqa: E712
            .order_by(Announcement.created_at.desc()).limit(limit)
        )
        notif_result = await session.execute(
            select(Notification).where(Notification.user_id == user_id)
            .order_by(Notification.created_at.desc()).limit(limit)
        )
        items = []
        for a in ann_result.scalars().all():
            items.append({
                "id": f"a{a.id}", "type": "announcement",
                "title": a.title or "E'lon", "body": a.body,
                "created_at": a.created_at.strftime("%Y-%m-%d %H:%M"),
                "ts": a.created_at.timestamp() * 1000,
            })
        for n in notif_result.scalars().all():
            items.append({
                "id": f"n{n.id}", "type": n.type,
                "title": n.title, "body": n.body,
                "created_at": n.created_at.strftime("%Y-%m-%d %H:%M"),
                "ts": n.created_at.timestamp() * 1000,
            })
        items.sort(key=lambda x: x["ts"], reverse=True)
        return items[:limit]


async def has_notification_type(user_id: int, type: str) -> bool:
    """"Welcome" bir marta yuborilishini, "welcome_back" bitta qaytish
    davrida takror yuborilmasligini tekshirish uchun."""
    async with async_session() as session:
        result = await session.execute(
            select(func.count()).select_from(Notification)
            .where(Notification.user_id == user_id, Notification.type == type)
        )
        return result.scalar_one() > 0


async def notify_new_topic_once(subject: str, mode: str, topic: str) -> None:
    """
    Yangi mavzu qo'shilganda, shu fandan o'rganayotgan BARCHA foydalanuvchilarga
    (subject mos keladiganlarga) bitta martalik bildirishnoma yuboradi.
    Savol darajasida EMAS — mavzu darajasida (bitta admin bir nechta savol
    qo'shsa ham, bitta xabar yetarli, spam bo'lmasin uchun)."""
    subject_name = SUBJECT_NAMES.get(subject, subject)
    body = f"{subject_name} faniga yangi mavzu qo'shildi: {topic}"
    async with async_session() as session:
        result = await session.execute(select(WebUser.id).where(WebUser.subject == subject))
        user_ids = [row[0] for row in result.all()]
        if not user_ids:
            return
        session.add_all([
            Notification(user_id=uid, type="new_topic", title=NOTIFICATION_TITLES["new_topic"], body=body)
            for uid in user_ids
        ])
        await session.commit()


async def update_last_login_and_check_welcome_back(user_id: int) -> None:
    """
    Har muvaffaqiyatli kirishda chaqiriladi: agar oxirgi kirishdan beri 14+
    kun o'tgan bo'lsa, "Sizni sog'indik" bildirishnomasini yuboradi, so'ng
    last_login_at'ni yangilaydi."""
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return
        now = datetime.utcnow()
        if user.last_login_at and (now - user.last_login_at) >= timedelta(days=14):
            session.add(Notification(
                user_id=user_id, type="welcome_back",
                title=NOTIFICATION_TITLES["welcome_back"],
                body="Sizni ko'rmaganimizga ancha bo'ldi — yangi mavzular va savollar qo'shildi, qaytib kelganingizdan xursandmiz!",
            ))
        user.last_login_at = now
        await session.commit()
    _cache_invalidate(user_id)


# --- Yordam xabarlari (foydalanuvchi -> admin) — admin panel "Xabarlar" bo'limi ---
async def create_support_message(user_id: int, subject: str, body: str) -> SupportMessage:
    async with async_session() as session:
        item = SupportMessage(
            user_id=user_id, subject=(subject or "").strip()[:200], body=(body or "").strip()[:2000],
        )
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item


async def get_user_support_messages(user_id: int, limit: int = 30) -> list[SupportMessage]:
    async with async_session() as session:
        result = await session.execute(
            select(SupportMessage)
            .where(SupportMessage.user_id == user_id)
            .order_by(SupportMessage.created_at.desc())
            .limit(limit)
        )
        return list(result.scalars().all())


async def count_unread_support_messages() -> int:
    async with async_session() as session:
        result = await session.execute(
            select(func.count()).select_from(SupportMessage).where(SupportMessage.is_read == False)  # noqa: E712
        )
        return result.scalar_one()


async def admin_list_support_messages(limit: int = 50, offset: int = 0) -> list[dict]:
    """Har bir xabar bilan birga yuborgan foydalanuvchining email/ismi ham qaytariladi."""
    async with async_session() as session:
        result = await session.execute(
            select(SupportMessage, WebUser.email, WebUser.first_name)
            .join(WebUser, WebUser.id == SupportMessage.user_id)
            .order_by(SupportMessage.is_read.asc(), SupportMessage.created_at.desc())
            .limit(limit).offset(offset)
        )
        rows = result.all()
        return [
            {"msg": msg, "email": email, "first_name": first_name}
            for msg, email, first_name in rows
        ]


async def admin_count_support_messages() -> int:
    async with async_session() as session:
        result = await session.execute(select(func.count()).select_from(SupportMessage))
        return result.scalar_one()


async def admin_get_support_message(message_id: int) -> dict | None:
    async with async_session() as session:
        result = await session.execute(
            select(SupportMessage, WebUser.email, WebUser.first_name)
            .join(WebUser, WebUser.id == SupportMessage.user_id)
            .where(SupportMessage.id == message_id)
        )
        row = result.first()
        if row is None:
            return None
        msg, email, first_name = row
        return {"msg": msg, "email": email, "first_name": first_name}


async def admin_reply_support_message(message_id: int, reply_text: str) -> bool:
    clean_reply = (reply_text or "").strip()[:2000]
    async with async_session() as session:
        item = await session.get(SupportMessage, message_id)
        if item is None:
            return False
        item.admin_reply = clean_reply
        item.replied_at = datetime.utcnow()
        item.is_read = True
        user_id = item.user_id
        await session.commit()
    # Foydalanuvchiga bildirishnoma — endi "Yordam" sahifasiga o'zi qaytib
    # bormasdan, qo'ng'iroq (bell) orqali javob kelganini darhol biladi.
    await create_notification(
        user_id, "support_reply",
        body=clean_reply[:200], source_id=message_id,
    )
    return True


async def mark_support_message_read(message_id: int) -> None:
    async with async_session() as session:
        item = await session.get(SupportMessage, message_id)
        if item is not None and not item.is_read:
            item.is_read = True
            await session.commit()


async def _migrate_missing_columns():
    """
    Base.metadata.create_all FAQAT yangi jadvallarni yaratadi — allaqachon
    mavjud jadvalga (masalan eski longouz_web.db faylida) YANGI USTUN
    qo'shmaydi. Bu yerda web_users jadvaliga keyinroq qo'shilgan ustunlar
    (ai_messages_today, ai_messages_date) bor-yo'qligini tekshirib,
    yo'q bo'lsa ALTER TABLE orqali xavfsiz qo'shamiz — shu bilan eski
    ma'lumotlar bazasi fayli bo'lgan foydalanuvchilarda ham sayt
    "no such column" xatosiz ishlayveradi.

    SQLite va PostgreSQL'da mavjud ustunlarni bilish usuli BOSHQA-BOSHQA
    (PRAGMA table_info — faqat SQLite'da bor buyruq; PostgreSQL'da esa
    information_schema.columns orqali so'raladi) — shuning uchun IS_SQLITE
    bayrog'iga qarab ikkalasini ham qo'llab-quvvatlaymiz.
    """
    from sqlalchemy import text
    async with engine.begin() as conn:
        if IS_SQLITE:
            result = await conn.execute(text("PRAGMA table_info(web_users)"))
            existing_columns = {row[1] for row in result.fetchall()}
        else:
            result = await conn.execute(text(
                "SELECT column_name FROM information_schema.columns WHERE table_name = 'web_users'"
            ))
            existing_columns = {row[0] for row in result.fetchall()}

        if "ai_messages_today" not in existing_columns:
            await conn.execute(text("ALTER TABLE web_users ADD COLUMN ai_messages_today INTEGER DEFAULT 0"))
            logger.info("Migratsiya: web_users.ai_messages_today ustuni qo'shildi.")
        for col_name, ddl in (("avatar_color", "VARCHAR(12) DEFAULT ''"), ("daily_goal", "INTEGER DEFAULT 10"),
                              ("target_percent", "INTEGER DEFAULT 90")):
            if col_name not in existing_columns:
                await conn.execute(text(f"ALTER TABLE web_users ADD COLUMN {col_name} {ddl}"))
                logger.info("Migratsiya: web_users.%s ustuni qo'shildi.", col_name)
        if "ai_messages_date" not in existing_columns:
            await conn.execute(text("ALTER TABLE web_users ADD COLUMN ai_messages_date DATE"))
            logger.info("Migratsiya: web_users.ai_messages_date ustuni qo'shildi.")
        if "last_login_at" not in existing_columns:
            # "Qaytib kelgan foydalanuvchi" bildirishnomasi uchun — oxirgi marta
            # qachon kirganini bilmasak, 14+ kun uzilish bo'lganini aniqlay olmaymiz.
            await conn.execute(text("ALTER TABLE web_users ADD COLUMN last_login_at DATETIME"))
            logger.info("Migratsiya: web_users.last_login_at ustuni qo'shildi.")

        if IS_SQLITE:
            result = await conn.execute(text("PRAGMA table_info(questions)"))
            q_columns = {row[1] for row in result.fetchall()}
        else:
            result = await conn.execute(text(
                "SELECT column_name FROM information_schema.columns WHERE table_name = 'questions'"
            ))
            q_columns = {row[0] for row in result.fetchall()}

        if "is_final_test" not in q_columns:
            await conn.execute(text("ALTER TABLE questions ADD COLUMN is_final_test BOOLEAN DEFAULT FALSE"))
            logger.info("Migratsiya: questions.is_final_test ustuni qo'shildi.")
        if "style_json" not in q_columns:
            await conn.execute(text("ALTER TABLE questions ADD COLUMN style_json VARCHAR(1000) DEFAULT ''"))
            logger.info("Migratsiya: questions.style_json ustuni qo'shildi.")
        if "source_file" not in q_columns:
            await conn.execute(text("ALTER TABLE questions ADD COLUMN source_file VARCHAR(200) DEFAULT ''"))
            logger.info("Migratsiya: questions.source_file ustuni qo'shildi.")
        if "figure_json" not in q_columns:
            await conn.execute(text("ALTER TABLE questions ADD COLUMN figure_json TEXT DEFAULT ''"))
            logger.info("Migratsiya: questions.figure_json ustuni qo'shildi.")
        if "source_no" not in q_columns:
            await conn.execute(text("ALTER TABLE questions ADD COLUMN source_no INTEGER DEFAULT 0"))
            logger.info("Migratsiya: questions.source_no ustuni qo'shildi.")
        for col_name, ddl in (("grade", "INTEGER DEFAULT 0"), ("difficulty", "INTEGER DEFAULT 0"),
                              ("block", "VARCHAR(20) DEFAULT ''"), ("qtype", "VARCHAR(10) DEFAULT 'closed'"),
                              ("min_plan", "INTEGER DEFAULT 0")):
            if col_name not in q_columns:
                await conn.execute(text(f"ALTER TABLE questions ADD COLUMN {col_name} {ddl}"))
                logger.info("Migratsiya: questions.%s ustuni qo'shildi.", col_name)
        if not IS_SQLITE:
            # 45 savollik imtihon JSON'i 8000 belgidan oshadi — PostgreSQL'da ustunni TEXT'ga o'tkazamiz.
            for tbl, col in (("web_quiz_log", "questions_json"), ("missed_questions", "question_json")):
                try:
                    await conn.execute(text(f"ALTER TABLE {tbl} ALTER COLUMN {col} TYPE TEXT"))
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Migratsiya: %s.%s TEXT'ga o'tmadi: %s", tbl, col, exc)


async def _wipe_legacy_bank_once():
    """Bir martalik TO'LIQ tozalash (v138): eski savollar, mavzular, qabriston, xatolar ro'yxati va
    mavzu oyna sozlamalari o'chiriladi. Shundan keyin savollar FAQAT admin panel orqali qo'shiladi
    (static_questions.py bilan avtomatik sinxronlash o'chirilgan)."""
    flag = "bank_wiped_v201"
    if await get_setting(flag, "") == "1":
        return
    async with async_session() as session:
        for table in ("questions", "deleted_questions", "missed_questions", "topic_progress", "topics"):
            await session.execute(sa_text(f"DELETE FROM {table}"))
        await session.execute(sa_text("DELETE FROM site_settings WHERE key LIKE 'ql:%'"))
        await session.commit()
    await set_setting(flag, "1")
    logger.info("Savollar banki va mavzular butunlay tozalandi (v138).")


async def get_user_by_email(email: str) -> WebUser | None:
    async with async_session() as session:
        email = (email or "").strip().lower()
        result = await session.execute(select(WebUser).where(func.lower(WebUser.email) == email).order_by(WebUser.id).limit(1))
        return result.scalars().first()


async def get_user_by_id(user_id: int) -> WebUser | None:
    cached = _cache_get(user_id)
    if cached is not None:
        return cached
    # v229: Supabase ulanishni vaqtincha uzsa ("terminating connection due to administrator command") — bir marta
    # qisqa kutib qayta urinamiz; aks holda o'quvchi bir martalik tarmoq uzilishi uchun 500 xato ko'rardi.
    for _attempt in range(2):
        try:
            async with async_session() as session:
                result = await session.execute(select(WebUser).where(WebUser.id == user_id))
                user = result.scalar_one_or_none()
                if user is not None:
                    _cache_set(user_id, user)
                return user
        except Exception as exc:  # noqa: BLE001
            msg = str(exc).lower()
            transient = any(k in msg for k in ("terminating connection", "connection was closed", "connection reset",
                                                "administrator command", "timeout", "could not connect", "ssl"))
            if _attempt == 0 and transient:
                import asyncio as _aio
                await _aio.sleep(0.4)
                continue
            raise


async def create_user(email: str, password_hash: str, first_name: str = "", plan: str = "free") -> WebUser:
    """Ro'yxatdan o'tgan foydalanuvchi — onboarding hali tugallanmagan holatda yaratiladi."""
    if plan not in ("free", "pro", "ultra"):
        plan = "free"
    user = WebUser(email=email, password_hash=password_hash, first_name=first_name, plan=plan)
    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def complete_onboarding(user_id: int, subject: str, level: str, certificate_type: str):
    """Fan/daraja/sertifikat tanlovi yakunlanganda chaqiriladi."""
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.subject = subject
            user.level = level
            user.certificate_type = certificate_type
            user.onboarding_done = True
            await session.commit()
    _cache_invalidate(user_id)


async def set_user_level(user_id: int, level: str):
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.level = level
            await session.commit()
    _cache_invalidate(user_id)


async def set_user_subject(user_id: int, subject_code: str):
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.subject = subject_code
            await session.commit()
    _cache_invalidate(user_id)


_streak_last_update: dict[int, float] = {}


async def update_streak(user_id: int):
    """
    Bazaga bosimni kamaytirish uchun: bir foydalanuvchi uchun 20 soniyada
    ko'pi bilan bir marta yozadi (masalan sahifa qayta-qayta yuklanganda
    har safar bazaga yozib o'tirmaslik uchun).
    """
    last = _streak_last_update.get(user_id, 0)
    if time.time() - last < CACHE_TTL_SECONDS:
        return
    _streak_last_update[user_id] = time.time()

    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return
        today = date.today()
        if user.streak_days == 0:
            user.streak_days = 1
            user.last_active_date = today
        elif user.last_active_date == today:
            pass
        elif user.last_active_date == today - timedelta(days=1):
            user.streak_days += 1
            user.last_active_date = today
        else:
            user.streak_days = 1
            user.last_active_date = today
        await session.commit()
    _cache_invalidate(user_id)


# ---------------------------------------------------------------------------
# QUIZ VA CHAT TARIXI
# ---------------------------------------------------------------------------

async def log_quiz_result(
    user_id: int, subject: str, topic: str,
    correct_count: int, total_count: int, questions_json: str = "",
    mode: str = "dtm", time_spent_seconds: int = 0, score_label: str = "",
    level: str = "boshlangich",
) -> WebQuizLog:
    log = WebQuizLog(
        user_id=user_id, subject=subject, topic=topic, level=level,
        correct_count=correct_count, total_count=total_count,
        questions_json=questions_json, mode=mode,
        time_spent_seconds=time_spent_seconds, score_label=score_label,
    )
    async with async_session() as session:
        session.add(log)
        await session.commit()
        await session.refresh(log)
        return log


async def get_user_quiz_history(user_id: int, subject: str | None = None) -> list[WebQuizLog]:
    async with async_session() as session:
        query = select(WebQuizLog).where(WebQuizLog.user_id == user_id)
        if subject:
            query = query.where(WebQuizLog.subject == subject)
        result = await session.execute(query.order_by(WebQuizLog.created_at.desc()))
        return list(result.scalars().all())


async def get_quiz_by_id(quiz_id: int, user_id: int) -> WebQuizLog | None:
    """Bitta testni 'qayta ko'rish' uchun — faqat o'ziniki bo'lsa qaytaradi."""
    async with async_session() as session:
        result = await session.execute(
            select(WebQuizLog).where(WebQuizLog.id == quiz_id, WebQuizLog.user_id == user_id)
        )
        return result.scalar_one_or_none()


async def get_quiz_by_id_any(quiz_id: int) -> WebQuizLog | None:
    """Foydalanuvchi tekshiruvisiz — FAQAT sertifikat sahifasida (ochiq,
    login talab qilinmaydigan) javoblar xulosasi (A/B/C/D + to'g'ri/xato)
    grafigini chizish uchun ishlatiladi. Hech qanday maxfiy ma'lumot
    (parol, email va h.k.) qaytarilmaydi — faqat savol-javob tuzilmasi."""
    async with async_session() as session:
        result = await session.execute(
            select(WebQuizLog).where(WebQuizLog.id == quiz_id)
        )
        return result.scalar_one_or_none()


async def log_chat(user_id: int, ai_provider: str, question: str, answer: str):
    async with async_session() as session:
        session.add(ChatLog(
            user_id=user_id, ai_provider=ai_provider,
            question=question, answer=answer,
        ))
        await session.commit()


# ---------------------------------------------------------------------------
# MAVZULASHTIRILGAN TEST TIZIMI — progress va "xato savollar" bankini
# boshqaradi. Asosiy g'oya: har bir savol "question_key" (savol matnidan
# hisoblangan barqaror hash) orqali aniqlanadi:
#   - Foydalanuvchi bir savolni TO'G'RI ishlasa -> TopicProgress'ga
#     qo'shiladi, boshqa MissedQuestion'dan bo'lsa o'chiriladi.
#   - XATO ishlasa -> MissedQuestion'ga qo'shiladi (yoki missed_count++).
# Shu orqali: "xato qilingan savol o'sha mavzuga qayta kelmaydi (chunki
# mavzu savollar to'plami State bilan filtrlanadi), lekin 'Mavzusiz test'
# bo'limida takror-takror chiqadi to'g'ri javob berilguncha" talabi
# bajariladi.
# ---------------------------------------------------------------------------
import hashlib


def make_question_key(question_text: str) -> str:
    """Savol matnidan barqaror, qisqa hash — bir xil savolni qayta tanib olish uchun."""
    return hashlib.sha256(question_text.strip().lower().encode("utf-8")).hexdigest()[:24]


async def get_topic_progress(user_id: int, subject: str, mode: str) -> dict[str, "TopicProgress"]:
    """Shu fan+rejim uchun barcha mavzular progressini {topic: TopicProgress} shaklida qaytaradi."""
    async with async_session() as session:
        result = await session.execute(
            select(TopicProgress).where(
                TopicProgress.user_id == user_id,
                TopicProgress.subject == subject,
                TopicProgress.mode == mode,
            )
        )
        return {row.topic: row for row in result.scalars().all()}


async def record_topic_answer(
    user_id: int, subject: str, mode: str, topic: str,
    question_text: str, question_json: str, is_correct: bool,
):
    """
    Bitta savolga berilgan javobni qayd etadi:
    - to'g'ri bo'lsa -> TopicProgress.solved ga qo'shiladi, MissedQuestion'dan olib tashlanadi
    - xato bo'lsa -> MissedQuestion'ga qo'shiladi/missed_count oshiriladi
    """
    import json as _json

    key = make_question_key(question_text)

    async with async_session() as session:
        # --- Mavzu progressi ---
        result = await session.execute(
            select(TopicProgress).where(
                TopicProgress.user_id == user_id,
                TopicProgress.subject == subject,
                TopicProgress.mode == mode,
                TopicProgress.topic == topic,
            )
        )
        progress = result.scalar_one_or_none()
        if progress is None:
            progress = TopicProgress(
                user_id=user_id, subject=subject, mode=mode, topic=topic,
                solved_question_keys_json="[]", total_questions=0, solved_count=0,
            )
            session.add(progress)

        try:
            solved_keys = set(_json.loads(progress.solved_question_keys_json or "[]"))
        except _json.JSONDecodeError:
            solved_keys = set()

        if is_correct:
            solved_keys.add(key)
            progress.solved_question_keys_json = _json.dumps(list(solved_keys))
            progress.solved_count = len(solved_keys)
        progress.last_practiced_at = datetime.utcnow()
        if progress.total_questions and progress.solved_count >= progress.total_questions:
            progress.completed = True

        # --- Xato savollar banki ("Mavzusiz test" uchun) ---
        missed_result = await session.execute(
            select(MissedQuestion).where(
                MissedQuestion.user_id == user_id,
                MissedQuestion.question_key == key,
            )
        )
        missed = missed_result.scalar_one_or_none()

        if is_correct:
            if missed is not None:
                await session.delete(missed)
        else:
            if missed is not None:
                missed.missed_count += 1
                missed.created_at = datetime.utcnow()
            else:
                session.add(MissedQuestion(
                    user_id=user_id, subject=subject, mode=mode, topic=topic,
                    question_key=key, question_json=question_json, missed_count=1,
                ))

        await session.commit()


async def set_topic_total_questions(user_id: int, subject: str, mode: str, topic: str, total: int):
    """Mavzudagi umumiy savollar sonini qayd etadi (progress-bar uchun, masalan '3/6')."""
    async with async_session() as session:
        result = await session.execute(
            select(TopicProgress).where(
                TopicProgress.user_id == user_id,
                TopicProgress.subject == subject,
                TopicProgress.mode == mode,
                TopicProgress.topic == topic,
            )
        )
        progress = result.scalar_one_or_none()
        if progress is None:
            progress = TopicProgress(
                user_id=user_id, subject=subject, mode=mode, topic=topic,
                solved_question_keys_json="[]", total_questions=total, solved_count=0,
            )
            session.add(progress)
        else:
            progress.total_questions = max(progress.total_questions, total)
        await session.commit()


async def get_missed_questions(user_id: int, subject: str | None = None, limit: int = 30) -> list[dict]:
    """
    "Mavzusiz test" bo'limi uchun — foydalanuvchining xato qilgan barcha
    savollarini qaytaradi (eng ko'p xato qilinganlar birinchi).
    """
    import json as _json

    async with async_session() as session:
        query = select(MissedQuestion).where(MissedQuestion.user_id == user_id)
        if subject:
            query = query.where(MissedQuestion.subject == subject)
        query = query.order_by(MissedQuestion.missed_count.desc(), MissedQuestion.created_at.desc()).limit(limit)
        result = await session.execute(query)
        rows = result.scalars().all()

    questions = []
    for row in rows:
        try:
            q = _json.loads(row.question_json)
            q["_missed_subject"] = row.subject
            q["_missed_topic"] = row.topic
            questions.append(q)
        except _json.JSONDecodeError:
            continue
    return questions


async def get_recent_chat(user_id: int, limit: int = 20) -> list[ChatLog]:
    """Eng oxirgi N ta xabarni eskidan-yangiga tartibda qaytaradi (chatni tiklash uchun)."""
    async with async_session() as session:
        result = await session.execute(
            select(ChatLog)
            .where(ChatLog.user_id == user_id)
            .order_by(ChatLog.created_at.desc())
            .limit(limit)
        )
        rows = list(result.scalars().all())
        return list(reversed(rows))


async def get_user_stats(user_id: int) -> dict:
    async with async_session() as session:
        user_result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = user_result.scalar_one_or_none()
        if not user:
            return {}

        quiz_result = await session.execute(
            select(WebQuizLog).where(WebQuizLog.user_id == user_id).order_by(WebQuizLog.created_at)
        )
        quizzes = list(quiz_result.scalars().all())
        total_correct = sum(q.correct_count for q in quizzes)
        total_questions = sum(q.total_count for q in quizzes)
        accuracy = round((total_correct / total_questions) * 100) if total_questions else 0

        # Fan bo'yicha taqsimot (diagramma uchun) — MUHIM: ENDI BARCHA fanlar
        # ro'yxatda bo'ladi (hali birorta test yechilmagan fanlar uchun ham),
        # 0% bilan — foydalanuvchi birinchi marta kirganida barcha ustunlar
        # 0 dan boshlanadi, keyin har bir yechilgan test bo'yicha real
        # ko'rsatkichga (ortishi HAM, pastga tushishi HAM mumkin) o'zgaradi.
        by_subject: dict[str, dict] = {
            s["code"]: {"correct": 0, "total": 0, "count": 0} for s in SUBJECTS
        }
        for q in quizzes:
            entry = by_subject.setdefault(q.subject, {"correct": 0, "total": 0, "count": 0})
            entry["correct"] += q.correct_count
            entry["total"] += q.total_count
            entry["count"] += 1

        # So'nggi 10 ta test natijasi (trend chizig'i uchun)
        recent_scores = [
            {
                "topic": q.topic,
                "subject": q.subject,
                "score": round((q.correct_count / q.total_count) * 100) if q.total_count else 0,
                "date": q.created_at.strftime("%Y-%m-%d"),
            }
            for q in quizzes[-10:]
        ]

        return {
            "streak_days": user.streak_days,
            "level": user.level,
            "subject": user.subject,
            "certificate_type": user.certificate_type,
            "total_quizzes": len(quizzes),
            "total_correct": total_correct,
            "total_questions": total_questions,
            "accuracy": accuracy,
            "by_subject": by_subject,
            "recent_scores": recent_scores,
        }


async def update_user_subject_level(user_id: int, subject: str | None = None, level: str | None = None):
    """Foydalanuvchi shaxsiy kabinetida istalgan vaqtda fan/darajasini o'zgartirishi uchun."""
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            if subject and subject in SUBJECT_CODES:
                user.subject = subject
            if level and level in LEVEL_CODES:
                user.level = level
            await session.commit()
    _cache_invalidate(user_id)


# ---------------------------------------------------------------------------
# 10-SONIYALIK KESH VA BATCH YOZUV (server performance / DB crash protection)
# -----------------------------------------------------------------------------
# Test yechish jarayonida har bir bosilgan javobni darhol bazaga yozish
# o'rniga, avval shu jarayon uchun ajratilgan xotiradagi keshga to'planadi.
# Klient (frontend) har 10 soniyada shu keshni /api/quiz/autosave orqali
# yangilab turadi — bu ODDIY xotira yozuvi, DB'ga hech narsa yozilmaydi.
# Test yakunlanganda (yoki foydalanuvchi sahifani qayta ochganda tiklash
# uchun) FAQAT BITTA yakuniy /api/quiz/submit so'rovi bazaga yoziladi.
# Natijada: bosilgan har bir javob emas, butun test uchun bitta DB yozuvi —
# DB yuklamasi ~90% kamayadi.
# -----------------------------------------------------------------------------
_autosave_cache: dict[str, dict] = {}
AUTOSAVE_TTL_SECONDS = 10

# ---------------------------------------------------------------------------
# XAVFSIZ TEST SESSIYASI (anti-tamper) — muammoning tafsiloti:
# Ilgari test yakunlanganda BROWSER (client) o'zi "necha ta to'g'ri javob
# berdim" deb hisoblab, shu raqamni serverga yuborardi. Bu — jiddiy zaif
# tomon: har qanday foydalanuvchi brauzer konsolida bitta so'rovni o'zgartirib,
# "correct_count": 30 deb yuborib, har doim 100% natija va soxta sertifikat
# olishi mumkin edi. Endi test generatsiya qilinganda ASL savol-javoblar
# (to'g'ri javoblar bilan) shu yerda, SERVERDA, attempt_token bo'yicha
# saqlanadi. Yakunlashda esa faqat foydalanuvchi TANLAGAN variantlar
# qabul qilinadi — necha ta to'g'ri ekanini SERVERNING O'ZI hisoblaydi.
# Client tomonidan yuborilgan "correct_count" ga endi umuman ishonilmaydi.
# ---------------------------------------------------------------------------
_quiz_session_cache: dict[str, dict] = {}
QUIZ_SESSION_TTL_SECONDS = 60 * 60 * 2  # 2 soat — test yechish uchun yetarli


class QuizSessionRow(Base):
    """Test sessiyasi (to'g'ri javoblar bilan) + autosave. Serverless (Vercel) da bir nechta instans bo'lgani uchun
    xotira o'rniga BAZADA saqlanadi (xotira keshi faqat tezlashtirish uchun)."""
    __tablename__ = "quiz_sessions"
    token: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    payload: Mapped[str] = mapped_column(Text)
    autosave: Mapped[str] = mapped_column(Text, default="")
    ts: Mapped[float] = mapped_column(Float, default=0.0, index=True)


async def store_quiz_session(
    attempt_token: str, user_id: int, subject: str, mode: str, questions: list[dict],
    topic: str = "", level: str = "boshlangich", meta: dict | None = None,
):
    """Test generatsiya qilingandan so'ng, asl (to'g'ri javobli) savollarni serverda saqlaydi."""
    import json as _j
    entry = {
        "user_id": user_id, "subject": subject, "mode": mode, "questions": questions,
        "topic": topic, "level": level, "meta": meta or {}, "ts": time.time(),
    }
    _quiz_session_cache[attempt_token] = entry
    if len(_quiz_session_cache) > 300:  # xotirani cheklaymiz
        for k in sorted(_quiz_session_cache, key=lambda k: _quiz_session_cache[k]["ts"])[:100]:
            _quiz_session_cache.pop(k, None)
    payload = _j.dumps(entry, ensure_ascii=False, default=str)
    async with async_session() as session:
        row = await session.get(QuizSessionRow, attempt_token)
        if row is None:
            session.add(QuizSessionRow(token=attempt_token, user_id=user_id, payload=payload, ts=entry["ts"]))
        else:
            row.user_id, row.payload, row.ts = user_id, payload, entry["ts"]
        # eski (2 soatdan oshgan) sessiyalarni vaqti-vaqti bilan tozalash
        if random.random() < 0.05:
            await session.execute(QuizSessionRow.__table__.delete().where(QuizSessionRow.ts < time.time() - QUIZ_SESSION_TTL_SECONDS))
        await session.commit()


async def get_quiz_session(attempt_token: str, user_id: int) -> dict | None:
    """Faqat SHU foydalanuvchiga tegishli va muddati o'tmagan sessiyani qaytaradi."""
    import json as _j
    entry = _quiz_session_cache.get(attempt_token)
    if entry is None:
        async with async_session() as session:
            row = await session.get(QuizSessionRow, attempt_token)
        if row is None:
            return None
        try:
            entry = _j.loads(row.payload)
        except ValueError:
            return None
        _quiz_session_cache[attempt_token] = entry
    if entry["user_id"] != user_id:
        return None  # boshqa foydalanuvchining testiga urinish — rad etiladi
    if time.time() - entry["ts"] > QUIZ_SESSION_TTL_SECONDS:
        _quiz_session_cache.pop(attempt_token, None)
        return None
    return entry


async def clear_quiz_session(attempt_token: str):
    _quiz_session_cache.pop(attempt_token, None)
    async with async_session() as session:
        await session.execute(QuizSessionRow.__table__.delete().where(QuizSessionRow.token == attempt_token))
        await session.commit()


async def autosave_progress(attempt_token: str, payload: dict, user_id: int | None = None):
    """Test jarayonini bazadagi sessiya qatoriga yozadi (serverless uchun)."""
    import json as _j
    _autosave_cache[attempt_token] = {"ts": time.time(), "data": payload}
    async with async_session() as session:
        row = await session.get(QuizSessionRow, attempt_token)
        if row is not None:
            row.autosave = _j.dumps(payload, ensure_ascii=False, default=str)
            await session.commit()


async def get_autosaved_progress(attempt_token: str) -> dict | None:
    import json as _j
    entry = _autosave_cache.get(attempt_token)
    if entry is not None and time.time() - entry["ts"] <= 3600:
        return entry["data"]
    async with async_session() as session:
        row = await session.get(QuizSessionRow, attempt_token)
    if row is None or not row.autosave:
        return None
    try:
        return _j.loads(row.autosave)
    except ValueError:
        return None


async def clear_autosaved_progress(attempt_token: str):
    _autosave_cache.pop(attempt_token, None)  # qator clear_quiz_session bilan o'chiriladi


# ---------------------------------------------------------------------------
# SERTIFIKATLAR
# ---------------------------------------------------------------------------

async def create_certificate(
    user_id: int, subject: str, mode: str, score_label: str, quiz_log_id: int | None = None,
    correct_count: int = 0, total_count: int = 0, percent: int = 0,
) -> UserCertificate:
    verification_id = uuid.uuid4().hex[:12].upper()
    cert = UserCertificate(
        user_id=user_id, verification_id=verification_id, subject=subject,
        mode=mode, score_label=score_label, quiz_log_id=quiz_log_id,
        correct_count=correct_count, total_count=total_count, percent=percent,
    )
    async with async_session() as session:
        session.add(cert)
        await session.commit()
        await session.refresh(cert)
        return cert


async def get_certificates_for_user(user_id: int) -> list[UserCertificate]:
    async with async_session() as session:
        result = await session.execute(
            select(UserCertificate).where(UserCertificate.user_id == user_id)
            .order_by(UserCertificate.issued_at.desc())
        )
        return list(result.scalars().all())


async def get_certificate_by_quiz_log_id(quiz_log_id: int) -> UserCertificate | None:
    """Berilgan test natijasiga (quiz_log) tegishli sertifikat bo'lsa qaytaradi —
    natijalarni ko'rish sahifasida (quiz_review) "Sertifikatni ko'rish" tugmasini
    faqat sertifikat HAQIQATDA mavjud bo'lsa ko'rsatish uchun kerak."""
    async with async_session() as session:
        result = await session.execute(
            select(UserCertificate).where(UserCertificate.quiz_log_id == quiz_log_id)
        )
        return result.scalar_one_or_none()


async def get_certificate_by_verification_id(verification_id: str) -> UserCertificate | None:
    async with async_session() as session:
        result = await session.execute(
            select(UserCertificate).where(UserCertificate.verification_id == verification_id)
        )
        return result.scalar_one_or_none()


# ---------------------------------------------------------------------------
# KURS PROGRESSI
# ---------------------------------------------------------------------------

async def mark_lesson_complete(user_id: int, course_code: str, lesson_code: str):
    async with async_session() as session:
        existing = await session.execute(
            select(CourseProgress).where(
                CourseProgress.user_id == user_id,
                CourseProgress.course_code == course_code,
                CourseProgress.lesson_code == lesson_code,
            )
        )
        if existing.scalar_one_or_none():
            return  # allaqachon belgilangan
        session.add(CourseProgress(user_id=user_id, course_code=course_code, lesson_code=lesson_code))
        await session.commit()


async def get_completed_lessons(user_id: int, course_code: str | None = None) -> set[tuple[str, str]]:
    async with async_session() as session:
        query = select(CourseProgress).where(CourseProgress.user_id == user_id)
        if course_code:
            query = query.where(CourseProgress.course_code == course_code)
        result = await session.execute(query)
        return {(row.course_code, row.lesson_code) for row in result.scalars().all()}


def course_progress_percent(course_code: str, completed: set[tuple[str, str]]) -> int:
    course = COURSE_BY_CODE.get(course_code)
    if not course or not course["lessons"]:
        return 0
    done = sum(1 for lesson in course["lessons"] if (course_code, lesson["code"]) in completed)
    return round(done / len(course["lessons"]) * 100)


# ---------------------------------------------------------------------------
# BALANS (hamyon) — hozircha faqat demo/vizual to'ldirish.
# ---------------------------------------------------------------------------

async def add_demo_balance(user_id: int, amount_som: int, method: str = "click") -> int:
    """
    Balansga demo summasini qo'shadi va tranzaksiyani tarixga yozadi.
    MUHIM: bu haqiqiy to'lov EMAS — Click/Paynet/SQB hali ulanmagan,
    shuning uchun bu yerda hech qanday real pul harakati yo'q, faqat
    ko'rgazma/vizual balans yangilanadi. Qaytaradi: yangi balans (so'mda).
    """
    async with async_session() as session:
        result = await session.execute(select(WebUser).where(WebUser.id == user_id))
        user = result.scalar_one_or_none()
        if user is None:
            return 0
        user.balance_som = (user.balance_som or 0) + amount_som
        session.add(BalanceTransaction(user_id=user_id, amount_som=amount_som, method=method))
        await session.commit()
        return user.balance_som


async def get_balance_history(user_id: int, limit: int = 20) -> list[dict]:
    async with async_session() as session:
        result = await session.execute(
            select(BalanceTransaction)
            .where(BalanceTransaction.user_id == user_id)
            .order_by(BalanceTransaction.created_at.desc())
            .limit(limit)
        )
        return [
            {
                "amount_som": row.amount_som,
                "method": row.method,
                "created_at": row.created_at.strftime("%d.%m.%Y %H:%M"),
            }
            for row in result.scalars().all()
        ]


# =============================================================================
# ADMIN PANEL — faqat admin.py orqali, admin autentifikatsiyasidan o'tgan
# so'ngina chaqiriladigan yordamchi funksiyalar. Oddiy foydalanuvchi
# so'rovlarida bular HECH QACHON ishlatilmaydi.
# =============================================================================

async def get_platform_stats() -> dict:
    """Admin bosh sahifasi uchun umumiy ko'rsatkichlar."""
    async with async_session() as session:
        total_users = (await session.execute(select(func.count(WebUser.id)))).scalar_one()
        total_quizzes = (await session.execute(select(func.count(WebQuizLog.id)))).scalar_one()
        total_certs = (await session.execute(select(func.count(UserCertificate.id)))).scalar_one()
        pro_users = (
            await session.execute(select(func.count(WebUser.id)).where(WebUser.plan == "pro"))
        ).scalar_one()
        ultra_users = (
            await session.execute(select(func.count(WebUser.id)).where(WebUser.plan == "ultra"))
        ).scalar_one()
        today = date.today()
        signups_today = (
            await session.execute(select(func.count(WebUser.id)).where(WebUser.joined_at == today))
        ).scalar_one()
        quizzes_today = (
            await session.execute(
                select(func.count(WebQuizLog.id)).where(func.date(WebQuizLog.created_at) == today)
            )
        ).scalar_one()
        ai_messages_today = (
            await session.execute(
                select(func.coalesce(func.sum(WebUser.ai_messages_today), 0)).where(
                    WebUser.ai_messages_date == today
                )
            )
        ).scalar_one()
        total_questions = (await session.execute(select(func.count(Question.id)))).scalar_one()
        active_questions = (
            await session.execute(select(func.count(Question.id)).where(Question.is_active.is_(True)))
        ).scalar_one()
        return {
            "total_users": total_users,
            "total_quizzes": total_quizzes,
            "total_certs": total_certs,
            "pro_users": pro_users,
            "ultra_users": ultra_users,
            "signups_today": signups_today,
            "quizzes_today": quizzes_today,
            "ai_messages_today": ai_messages_today,
            "total_questions": total_questions,
            "active_questions": active_questions,
        }


async def admin_subject_breakdown() -> list[dict]:
    """Admin monitoring uchun: har bir fan bo'yicha nechta faol savol bor,
    nechta noyob mavzu bor — qaysi fanlar 'kam savol' bilan qolganini
    tezda ko'rish uchun (foydalanuvchi ~3000/fan maqsad qilgan)."""
    async with async_session() as session:
        rows = (
            await session.execute(
                select(
                    Question.subject,
                    func.count(Question.id),
                    func.count(func.distinct(Question.topic)),
                )
                .where(Question.is_active.is_(True))
                .group_by(Question.subject)
                .order_by(Question.subject)
            )
        ).all()
        return [
            {"subject": r[0], "question_count": r[1], "topic_count": r[2]}
            for r in rows
        ]


async def admin_recent_signups(limit: int = 8) -> list[WebUser]:
    async with async_session() as session:
        result = await session.execute(select(WebUser).order_by(desc(WebUser.id)).limit(limit))
        return list(result.scalars().all())


# ---------------------------------------------------------------------------
# IELTS/Sertifikat SPEAKING va WRITING — natijalarni saqlash va tarixni o'qish
# ---------------------------------------------------------------------------

async def save_speaking_writing_log(
    user_id: int, section: str, topic_id: str, topic_title: str,
    content: str, band_score: str, feedback: str,
) -> int:
    async with async_session() as session:
        row = SpeakingWritingLog(
            user_id=user_id, section=section, topic_id=topic_id, topic_title=topic_title,
            content=content[:8000], band_score=band_score[:10], feedback=feedback[:3000],
        )
        session.add(row)
        await session.commit()
        await session.refresh(row)
        return row.id


async def get_speaking_writing_history(user_id: int, section: str = "", limit: int = 30) -> list[SpeakingWritingLog]:
    async with async_session() as session:
        query = select(SpeakingWritingLog).where(SpeakingWritingLog.user_id == user_id)
        if section:
            query = query.where(SpeakingWritingLog.section == section)
        query = query.order_by(desc(SpeakingWritingLog.id)).limit(limit)
        result = await session.execute(query)
        return list(result.scalars().all())


def _user_filter(query, search: str = "", plan: str = ""):
    if search:
        like = f"%{search.strip()}%"
        query = query.where((WebUser.email.ilike(like)) | (WebUser.first_name.ilike(like)))
    if plan in ("free", "pro", "ultra"):
        query = query.where(WebUser.plan == plan)
    return query


async def get_all_users(limit: int = 100, offset: int = 0, search: str = "", plan: str = "") -> list[WebUser]:
    """Admin panel uchun foydalanuvchilar ro'yxati — eng yangi ro'yxatdan
    o'tganlar birinchi. `search` ism/email, `plan` tarif bo'yicha filtrlaydi."""
    async with async_session() as session:
        query = _user_filter(select(WebUser), search, plan).order_by(desc(WebUser.id)).limit(limit).offset(offset)
        return list((await session.execute(query)).scalars().all())


async def count_users(search: str = "", plan: str = "") -> int:
    async with async_session() as session:
        query = _user_filter(select(func.count(WebUser.id)), search, plan)
        return (await session.execute(query)).scalar_one()


async def users_quiz_stats(user_ids: list[int]) -> dict[int, dict]:
    """Har bir foydalanuvchi uchun testlar soni, o'rtacha natija va oxirgi faollik."""
    if not user_ids:
        return {}
    async with async_session() as session:
        rows = (await session.execute(
            select(
                WebQuizLog.user_id, func.count(WebQuizLog.id),
                func.sum(WebQuizLog.correct_count), func.sum(WebQuizLog.total_count),
                func.max(WebQuizLog.created_at),
            ).where(WebQuizLog.user_id.in_(user_ids)).group_by(WebQuizLog.user_id)
        )).all()
    out: dict[int, dict] = {}
    for uid, n, corr, tot, last in rows:
        out[uid] = {"tests": n, "percent": round((corr or 0) * 100 / tot) if tot else 0, "last": last}
    return out


async def admin_user_detail(user_id: int) -> dict | None:
    async with async_session() as session:
        user = await session.get(WebUser, user_id)
        if user is None:
            return None
        logs = (await session.execute(
            select(WebQuizLog).where(WebQuizLog.user_id == user_id)
            .order_by(desc(WebQuizLog.id)).limit(30)
        )).scalars().all()
    stats = (await users_quiz_stats([user_id])).get(user_id, {"tests": 0, "percent": 0, "last": None})
    return {"user": user, "logs": list(logs), "stats": stats}


async def admin_set_user_plan(user_id: int, plan: str) -> bool:
    """Admin foydalanuvchiga qo'lda Pro/Ultra tarif beradi (masalan to'lov
    tashqarida, naqd yoki bank o'tkazmasi orqali qilingan bo'lsa)."""
    if plan not in ("free", "pro", "ultra"):
        return False
    async with async_session() as session:
        user = await session.get(WebUser, user_id)
        if user is None:
            return False
        user.plan = plan
        await session.commit()
        _cache_invalidate(user_id)  # MUHIM: aks holda eski tarif 20 soniyagacha "yopishib qoladi"
        return True


async def admin_delete_user(user_id: int) -> bool:
    """Foydalanuvchi va unga tegishli BARCHA yozuvlarni o'chiradi. QAYTARIB BO'LMAYDI — admin tomonida
    tasdiqlashsiz chaqirilmasligi kerak.
    v229: web_users ga bog'langan hamma jadvallar (bildirishnomalar, yordam xabarlari, balans, AI/chat jurnali,
    test tarixi, sertifikatlar, progress...) avtomatik topiladi — yangi jadval qo'shilsa ham o'chirish buzilmaydi
    (avval bildirishnomalar qolib ketib, "foreign key" xatosi bilan o'chirish ishlamas edi)."""
    async with async_session() as session:
        user = await session.get(WebUser, user_id)
        if user is None:
            return False
        deps = []
        for t in Base.metadata.sorted_tables:
            for fk in t.foreign_keys:
                if fk.column.table.name == WebUser.__tablename__:
                    deps.append((t, fk.parent))
        # sorted_tables: avval "ota" jadvallar — teskari tartibda o'chiramiz (sertifikat test tarixidan oldin)
        for t, col in reversed(deps):
            await session.execute(t.delete().where(col == user_id))
        await session.delete(user)
        await session.commit()
        _cache_invalidate(user_id)  # o'chirilgan foydalanuvchi keshda "tirik" qolib ketmasin
        return True


async def admin_get_question(question_id: int) -> "Question | None":
    """Admin tahrirlash sahifasi uchun bitta savol (v229: yetishmayotgan funksiya qo'shildi)."""
    async with async_session() as session:
        return await session.get(Question, question_id)


# =============================================================================
# SAVOLLAR BANKI — so'rovlar (oddiy foydalanuvchi test yechishda ishlatadi)
# =============================================================================

def _question_to_dict(q: "Question") -> dict:
    import json as _json
    if (q.qtype or "closed") == "open":
        accept = [str(a) for a in _json.loads(q.options_json or "[]")]
        return {
            "id": q.id, "mock_test": q.mock_test, "topic": q.topic, "question": q.question,
            "options": [], "accept": accept, "answer_text": accept[0] if accept else "", "correct_index": -1,
            "explanation": q.explanation, "style": _parse_style(q.style_json), "figure": _parse_figures(q.figure_json),
            "difficulty": q.difficulty or 0, "block": q.block or "", "qtype": "open", "grade": q.grade or 0,
        }
    return {
        "id": q.id,
        "mock_test": q.mock_test,
        "topic": q.topic,
        "question": q.question,
        "options": _json.loads(q.options_json),
        "correct_index": q.correct_index,
        "explanation": q.explanation,
        "style": _parse_style(q.style_json),
        "figure": _parse_figures(q.figure_json),
        "difficulty": q.difficulty or 0,
        "block": q.block or "",
        "qtype": q.qtype or "closed",
        "grade": q.grade or 0,
    }


def _parse_figures(raw: str) -> dict:
    import figures
    return figures.parse_figures(raw or "")


def _parse_style(raw: str) -> dict:
    import json as _json
    if not raw:
        return {}
    try:
        val = _json.loads(raw)
    except ValueError:
        return {}
    return val if isinstance(val, dict) else {}


async def list_topics_db(subject: str, mode: str) -> list[str]:
    """Shu fan+rejim uchun mavjud mavzular ro'yxati, birinchi uchragan
    tartibida (barqaror bo'lishi uchun id bo'yicha saralanadi)."""
    async with async_session() as session:
        result = await session.execute(
            select(Question.topic)
            .where(Question.subject == subject, Question.mode == mode, Question.is_active == True)  # noqa: E712
            .order_by(Question.id)
        )
        seen = []
        for (topic,) in result.all():
            if topic and topic not in seen:
                seen.append(topic)
        return seen


async def count_questions_by_topic(subject: str, mode: str) -> dict[str, int]:
    async with async_session() as session:
        result = await session.execute(
            select(Question.topic, func.count(Question.id))
            .where(Question.subject == subject, Question.mode == mode, Question.is_active == True)  # noqa: E712
            .group_by(Question.topic)
        )
        return {topic: cnt for topic, cnt in result.all()}


async def topic_is_final_test(subject: str, mode: str, topic: str) -> bool:
    """
    Shu mavzu "Yakuniy test" (haftalik/oylik yopiq mavzular bo'yicha
    umumlashtiruvchi tekshiruv) sifatida belgilanganmi — shunday bo'lsa,
    /api/quiz/generate BUTUN savol to'plamini (tarifdan qat'iy nazar, 25
    tagacha) beradi, oddiy mavzular kabi tarif bo'yicha kesilmaydi.
    """
    async with async_session() as session:
        result = await session.execute(
            select(Question.id)
            .where(
                Question.subject == subject, Question.mode == mode,
                Question.topic == topic, Question.is_final_test == True,  # noqa: E712
            )
            .limit(1)
        )
        return result.scalar_one_or_none() is not None


MIN_TOPIC_TEST = 20


def _norm_text(text: str) -> str:
    return " ".join(str(text or "").lower().split())


def _unique_by_text(rows):
    seen: set[str] = set()
    out = []
    for q in rows:
        key = _norm_text(q.question)
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


async def get_questions_db_multi_topic(
    subject: str, mode: str, topics: list[str], count: int = 10,
) -> list[dict]:
    """5-MAVZULIK ARALASH AMALIY SINOV uchun: bir nechta mavzudan birgalikda
    savol tanlaydi (get_questions_db'ga o'xshash, lekin bitta emas, bir
    nechta mavzu ro'yxatidan). Mavzular orasida imkon qadar teng taqsimlab,
    keyin aralashtirib beradi."""
    if not topics:
        return []
    async with async_session() as session:
        result = await session.execute(
            select(Question).where(
                Question.subject == subject, Question.mode == mode,
                Question.is_active == True, Question.topic.in_(topics),  # noqa: E712
            )
        )
        rows = list(result.scalars().all())
        if not rows:
            return []
        random.shuffle(rows)
        return [_question_to_dict(q) for q in _unique_by_text(rows)[:count]]


async def get_questions_db(
    subject: str, count: int = 5, mode: str = "dtm",
    topic: str | None = None, exclude_keys: set[str] | None = None,
) -> list[dict]:
    """DB'dan savollarni qaytaradi — static_questions.get_static_questions
    bilan bir xil xulq-atvor va qaytish formati (eski kod bilan to'liq mos):
    mavzu berilsa faqat o'sha mavzudan, exclude_keys berilsa iloji boricha
    ulardan qochiladi, va HECH QACHON bitta test ichida savol takrorlanmaydi
    (so'ralgan sondan kam bo'lsa ham, faqat noyob savollar qaytariladi)."""
    async with async_session() as session:
        query = select(Question).where(
            Question.subject == subject, Question.mode == mode, Question.is_active == True,  # noqa: E712
        )
        if topic:
            query_with_topic = query.where(Question.topic == topic)
            result = await session.execute(query_with_topic)
            rows = result.scalars().all()
            if not rows:  # mavzu topilmasa, umumiy bankdan foydalanamiz
                result = await session.execute(query)
                rows = result.scalars().all()
        else:
            result = await session.execute(query)
            rows = result.scalars().all()

        if not rows:
            return []

        rows = list(rows)
        random.shuffle(rows)

        if exclude_keys:
            fresh = [q for q in rows if make_question_key(q.question) not in exclude_keys]
            if len(fresh) >= min(count, len(rows)):
                rows = fresh

        picked = _unique_by_text(rows)[:count]

        random.shuffle(picked)

        return [_question_to_dict(q) for q in picked]


# =============================================================================
# ADMIN — savollar bankini boshqarish (CRUD)
# =============================================================================

ADMIN_QUESTIONS_PAGE_SIZE = 30


def _q_filters(query, subject="", mode="", topic="", search="", status="", source=""):
    if subject:
        query = query.where(Question.subject == subject)
    if mode:
        query = query.where(Question.mode == mode)
    if topic:
        query = query.where(Question.topic == topic)
    if search:
        query = query.where(Question.question.ilike(f"%{search.strip()}%"))
    if status == "published":
        query = query.where(Question.is_active.is_(True))
    elif status == "private":
        query = query.where(Question.is_active.is_(False))
    if source == "__manual__":
        query = query.where(Question.source_file == "")
    elif source:
        query = query.where(Question.source_file == source)
    return query


async def admin_list_questions(
    subject: str = "", mode: str = "", topic: str = "", search: str = "",
    limit: int = ADMIN_QUESTIONS_PAGE_SIZE, offset: int = 0, status: str = "", source: str = "",
) -> list["Question"]:
    async with async_session() as session:
        query = _q_filters(select(Question), subject, mode, topic, search, status, source)
        query = query.order_by(desc(Question.id)).limit(limit).offset(offset)
        return list((await session.execute(query)).scalars().all())


async def admin_count_questions(subject: str = "", mode: str = "", topic: str = "", search: str = "", status: str = "", source: str = "") -> int:
    async with async_session() as session:
        query = _q_filters(select(func.count(Question.id)), subject, mode, topic, search, status, source)
        return (await session.execute(query)).scalar_one()


async def admin_import_sources() -> list[dict]:
    """Import qilingan fayllar: nomi, savollar soni, nechtasi private, birinchi qo'shilgan sana."""
    async with async_session() as session:
        rows = (await session.execute(
            select(Question.source_file, func.count(Question.id), func.min(Question.created_at),
                   func.sum(case((Question.is_active.is_(False), 1), else_=0)))
            .where(Question.source_file != "").group_by(Question.source_file)
            .order_by(desc(func.min(Question.created_at))).limit(200)
        )).all()
    return [{"name": r[0], "count": r[1], "date": r[2], "private": int(r[3] or 0)} for r in rows]


async def admin_question_key_index() -> dict[str, dict]:
    """Bazadagi BARCHA savollar: normallashtirilgan matn -> {id, subject, mode, topic, date, src, no}.
    Import vaqtida takrorlarni aniqlash uchun (fan/rejimdan qat'i nazar)."""
    from question_import import norm_key
    idx: dict[str, dict] = {}
    async with async_session() as session:
        rows = (await session.execute(
            select(Question.id, Question.subject, Question.mode, Question.topic, Question.question,
                   Question.created_at, Question.source_file, Question.source_no).order_by(Question.id)
        )).all()
    for r in rows:
        key = norm_key(r[4])
        if key and key not in idx:
            idx[key] = {"id": r[0], "subject": r[1], "mode": r[2], "topic": r[3], "date": r[5], "src": r[6] or "", "no": r[7] or 0}
    return idx


async def admin_delete_questions_bulk(question_ids: list[int]) -> int:
    n = 0
    for qid in question_ids:
        if await admin_delete_question(qid):
            n += 1
    return n


async def admin_delete_source(source: str) -> int:
    async with async_session() as session:
        ids = [r[0] for r in (await session.execute(select(Question.id).where(Question.source_file == source))).all()]
    return await admin_delete_questions_bulk(ids)


async def admin_set_source_active(source: str, active: bool) -> int:
    from sqlalchemy import update as sa_update
    async with async_session() as session:
        res = await session.execute(sa_update(Question).where(Question.source_file == source).values(is_active=active))
        await session.commit()
        return res.rowcount or 0


async def _question_text_exists(session, subject: str, mode: str, text: str, exclude_id: int | None = None) -> bool:
    query = select(Question.id).where(
        Question.subject == subject, Question.mode == mode,
        func.lower(Question.question) == text.strip().lower(),
    ).limit(1)
    if exclude_id is not None:
        query = query.where(Question.id != exclude_id)
    return (await session.execute(query)).scalar_one_or_none() is not None


async def _add_tombstone(session, subject: str, mode: str, text: str) -> None:
    key = make_question_key(text)
    found = (await session.execute(
        select(DeletedQuestion.id).where(
            DeletedQuestion.subject == subject, DeletedQuestion.mode == mode,
            DeletedQuestion.question_key == key,
        ).limit(1)
    )).scalar_one_or_none()
    if found is None:
        session.add(DeletedQuestion(subject=subject, mode=mode, question_key=key))


async def _remove_tombstone(session, subject: str, mode: str, text: str) -> None:
    from sqlalchemy import delete as sa_delete
    await session.execute(
        sa_delete(DeletedQuestion).where(
            DeletedQuestion.subject == subject, DeletedQuestion.mode == mode,
            DeletedQuestion.question_key == make_question_key(text),
        )
    )


async def _purge_missed_for_question(session, text: str) -> None:
    """Savol o'chirilganda/almashtirilganda foydalanuvchilarning "xato qilingan
    savollar" ro'yxatidan ham olib tashlanadi — hech qayerda qolmasin."""
    from sqlalchemy import delete as sa_delete
    await session.execute(sa_delete(MissedQuestion).where(MissedQuestion.question_key == make_question_key(text)))


async def admin_create_question(
    subject: str, mode: str, topic: str, question: str,
    options: list[str], correct_index: int, explanation: str = "", mock_test: str = "",
    is_final_test: bool = False, style_json: str = "", figure_json: str = "",
) -> "Question":
    import json as _json
    question = question.strip()
    q = Question(
        subject=subject, mode=mode, topic=(topic or "Umumiy").strip(),
        mock_test=mock_test, question=question,
        options_json=_json.dumps(options, ensure_ascii=False),
        correct_index=correct_index, explanation=explanation, is_active=True,
        is_final_test=is_final_test, style_json=style_json, figure_json=figure_json,
    )
    async with async_session() as session:
        if not figure_json and await _question_text_exists(session, subject, mode, question):
            raise DuplicateQuestionError(question[:80])
        await _remove_tombstone(session, subject, mode, question)
        session.add(q)
        await session.commit()
        await session.refresh(q)
        return q


async def admin_bulk_create_questions(items: list[dict], mock_test: str = "Admin import", is_active: bool = True) -> dict:
    """Ko'p savolni bir tranzaksiyada qo'shadi. items: subject, mode, topic,
    question, options[4], correct_index, explanation. Takrorlar o'tkazib yuboriladi.
    Natija: {"added": [..items..], "skipped": n}."""
    import json as _json
    from sqlalchemy import delete as sa_delete
    added, skipped = [], 0
    async with async_session() as session:
        batch_seen: set[tuple[str, str, str]] = set()
        for it in items:
            text = it["question"].strip()
            k = (it["subject"], it["mode"], text.lower())
            if not it.get("force") and not it.get("figure_json") and (k in batch_seen or await _question_text_exists(session, it["subject"], it["mode"], text)):
                skipped += 1
                continue
            batch_seen.add(k)
            await _remove_tombstone(session, it["subject"], it["mode"], text)
            session.add(Question(
                subject=it["subject"], mode=it["mode"], topic=(it.get("topic") or "Umumiy").strip(),
                mock_test=it.get("mock_test") or mock_test, question=text,
                options_json=_json.dumps(it["options"], ensure_ascii=False),
                correct_index=int(it["correct_index"]), explanation=(it.get("explanation") or ""),
                is_active=is_active, is_final_test=False, figure_json=(it.get("figure_json") or ""),
                source_file=(it.get("src") or "")[:200], source_no=int(it.get("no") or 0),
            ))
            added.append(it)
        await session.commit()
    return {"added": added, "skipped": skipped}


async def admin_update_question(
    question_id: int, subject: str, mode: str, topic: str, question: str,
    options: list[str], correct_index: int, explanation: str = "", mock_test: str = "",
    is_active: bool = True, is_final_test: bool = False, style_json: str | None = None,
    figure_json: str | None = None,
) -> bool:
    import json as _json
    question = question.strip()
    async with async_session() as session:
        q = await session.get(Question, question_id)
        if q is None:
            return False
        old_subject, old_mode, old_text = q.subject, q.mode, q.question
        has_figure = bool(figure_json if figure_json is not None else q.figure_json)
        if not has_figure and await _question_text_exists(session, subject, mode, question, exclude_id=question_id):
            raise DuplicateQuestionError(question[:80])
        if (old_subject, old_mode, old_text.strip().lower()) != (subject, mode, question.lower()):
            # Eski matn/joy endi mavjud emas — static bankdan qayta tiklanmasin
            await _add_tombstone(session, old_subject, old_mode, old_text)
            await _purge_missed_for_question(session, old_text)
            await _remove_tombstone(session, subject, mode, question)
        q.subject = subject
        q.mode = mode
        q.topic = (topic or "Umumiy").strip()
        q.mock_test = mock_test
        q.question = question
        q.options_json = _json.dumps(options, ensure_ascii=False)
        q.correct_index = correct_index
        q.explanation = explanation
        q.is_active = is_active
        q.is_final_test = is_final_test
        if style_json is not None:
            q.style_json = style_json
        if figure_json is not None:
            q.figure_json = figure_json
        await session.commit()
        return True


async def admin_delete_question(question_id: int) -> "Question | None":
    """Savolni bazadan va foydalanuvchilarning xatolar ro'yxatidan DOIMIY o'chiradi
    va qabristonga yozadi (qayta ishga tushganda tiklanmaydi). O'chirilgan
    savol ma'lumotini qaytaradi (bildirishnoma uchun) yoki None."""
    async with async_session() as session:
        q = await session.get(Question, question_id)
        if q is None:
            return None
        await _add_tombstone(session, q.subject, q.mode, q.question)
        await _purge_missed_for_question(session, q.question)
        snapshot = Question(subject=q.subject, mode=q.mode, topic=q.topic, question=q.question,
                            options_json=q.options_json, correct_index=q.correct_index)
        await session.delete(q)
        await session.commit()
        return snapshot


async def admin_quick_set_correct(question_id: int, index: int) -> bool:
    import json as _json
    async with async_session() as session:
        q = await session.get(Question, question_id)
        if q is None:
            return False
        try:
            n = len(_json.loads(q.options_json or "[]"))
        except ValueError:
            return False
        if not 0 <= index < n:
            return False
        q.correct_index = index
        await session.commit()
        return True


async def admin_move_questions(question_ids: list[int], subject: str = "", mode: str = "", topic: str = "") -> int:
    """Tanlangan savollarni boshqa fan/rejim/mavzuga ko'chiradi (bo'sh maydon o'zgarmaydi)."""
    from sqlalchemy import update as sa_update
    values = {k: v.strip() for k, v in (("subject", subject), ("mode", mode), ("topic", topic)) if v and v.strip()}
    if not question_ids or not values:
        return 0
    async with async_session() as session:
        res = await session.execute(sa_update(Question).where(Question.id.in_(question_ids)).values(**values))
        await session.commit()
        return res.rowcount or 0


def _mixed_script(text: str) -> bool:
    import re as _re
    return any(_re.search(r"[A-Za-z]", w) and _re.search(r"[\u0400-\u04FF]", w) for w in _re.findall(r"\w+", text or ""))


async def admin_audit_questions(subject: str = "", mode: str = "", limit: int = 400) -> dict:
    """Bazani avtomatik tekshiradi: noto'g'ri kalit, takror variantlar, bo'sh variant,
    aralash harf, takror savol. Har bir muammo uchun savol ID si va sabab qaytaradi."""
    import json as _json
    issues: list[dict] = []
    seen: dict[tuple, int] = {}
    counts = {"checked": 0}
    async with async_session() as session:
        query = select(Question.id, Question.subject, Question.mode, Question.topic, Question.question,
                       Question.options_json, Question.correct_index, Question.is_active)
        if subject:
            query = query.where(Question.subject == subject)
        if mode:
            query = query.where(Question.mode == mode)
        rows = (await session.execute(query.order_by(Question.id))).all()
    kinds: dict[str, int] = {}

    def add(row, kind, detail):
        kinds[kind] = kinds.get(kind, 0) + 1
        if len(issues) < limit:
            issues.append({"id": row[0], "subject": row[1], "mode": row[2], "topic": row[3],
                           "question": (row[4] or "")[:140], "kind": kind, "detail": detail})

    for row in rows:
        counts["checked"] += 1
        try:
            opts = _json.loads(row[5] or "[]")
        except ValueError:
            add(row, "Buzilgan variantlar", "options_json o'qilmadi")
            continue
        text = (row[4] or "").strip()
        if len(text) < 8:
            add(row, "Juda qisqa savol", text)
        if len(opts) < 2:
            add(row, "Variantlar yetarli emas", f"{len(opts)} ta")
        elif len(opts) != 4 and row[2] != "ielts":
            add(row, "Variantlar soni 4 emas", f"{len(opts)} ta")
        if not isinstance(row[6], int) or not 0 <= row[6] < len(opts):
            add(row, "Javob kaliti diapazondan tashqari", f"correct_index={row[6]}")
        norm = [str(o).strip() for o in opts]
        if any(not o for o in norm):
            add(row, "Bo'sh variant", "")
        if len(set(norm)) != len(norm):
            add(row, "Takror variantlar", " | ".join(norm)[:120])
        if _mixed_script(text) or any(_mixed_script(o) for o in norm):
            add(row, "Lotin/kirill aralash so'z", "")
        key = (row[1], row[2], " ".join(text.lower().split()))
        if key in seen:
            add(row, "Takror savol", f"#{seen[key]} bilan bir xil")
        else:
            seen[key] = row[0]
    return {"issues": issues, "kinds": kinds, "checked": counts["checked"], "total_issues": sum(kinds.values())}


async def admin_set_questions_active(question_ids: list[int], active: bool) -> int:
    from sqlalchemy import update as sa_update
    if not question_ids:
        return 0
    async with async_session() as session:
        res = await session.execute(sa_update(Question).where(Question.id.in_(question_ids)).values(is_active=active))
        await session.commit()
        return res.rowcount or 0


async def topic_counts_all(subject: str, mode: str) -> dict[str, int]:
    """Faol savollar soni mavzular bo'yicha — import vaqtida kam mavzularni topish uchun."""
    return await count_questions_by_topic(subject, mode)


async def sample_questions_for_matching(subject: str, mode: str, per_topic: int = 40) -> dict[str, list[str]]:
    """Mavzuni avtomatik aniqlash uchun har mavzudan namunaviy savol matnlari."""
    async with async_session() as session:
        result = await session.execute(
            select(Question.topic, Question.question)
            .where(Question.subject == subject, Question.mode == mode, Question.is_active == True)  # noqa: E712
        )
        out: dict[str, list[str]] = {}
        for topic, text in result.all():
            lst = out.setdefault(topic, [])
            if len(lst) < per_topic:
                lst.append(text)
        return out


NOTIFICATION_TITLES.update({
    "questions_added": "Yangi savollar qo'shildi",
    "questions_updated": "Savollar yangilandi",
    "questions_deleted": "Savollar o'chirildi",
})


async def notify_question_change(subject: str, mode: str, kind: str, topics: list[str], count: int = 1) -> int:
    """Admin savollar bankini o'zgartirganda (qo'shish/tahrirlash/o'chirish) shu fandan
    o'qiyotgan BARCHA foydalanuvchiga bildirishnoma yuboradi. Qaytaradi: foydalanuvchilar soni."""
    verbs = {
        "questions_added": "yangi savol qo'shildi",
        "questions_updated": "savol yangilandi",
        "questions_deleted": "savol o'chirildi",
    }
    if kind not in verbs:
        return 0
    mode_name = {"dtm": "DTM", "certificate": "Sertifikat", "ielts": "IELTS", "cefr": "CEFR"}.get(mode, mode)
    topic_list = ", ".join(dict.fromkeys(t for t in topics if t))[:300]
    body = f"{SUBJECT_NAMES.get(subject, subject)} ({mode_name}): {count} ta {verbs[kind]}"
    if topic_list:
        body += f" — mavzu: {topic_list}"
    async with async_session() as session:
        ids = [r[0] for r in (await session.execute(select(WebUser.id).where(WebUser.subject == subject))).all()]
        if not ids:
            return 0
        session.add_all([
            Notification(user_id=uid, type=kind, title=NOTIFICATION_TITLES[kind], body=body[:1000]) for uid in ids
        ])
        await session.commit()
        return len(ids)


async def admin_question_bank_summary() -> list[dict]:
    """Har bir fan+rejim uchun nechta savol borligi — admin bosh sahifasida
    "qaysi fan/rejimda savol kam" ko'rinishi uchun."""
    async with async_session() as session:
        result = await session.execute(
            select(Question.subject, Question.mode, func.count(Question.id))
            .where(Question.is_active == True)  # noqa: E712
            .group_by(Question.subject, Question.mode)
        )
        return [{"subject": s, "mode": m, "count": c} for s, m, c in result.all()]


async def log_admin_action(admin_username: str, action: str, detail: str = ""):
    entry = AdminLog(admin_username=admin_username, action=action, detail=detail)
    async with async_session() as session:
        session.add(entry)
        await session.commit()


async def get_admin_log(limit: int = 100) -> list["AdminLog"]:
    async with async_session() as session:
        result = await session.execute(select(AdminLog).order_by(desc(AdminLog.id)).limit(limit))
        return list(result.scalars().all())


# =============================================================================
# ADMIN — berilgan sertifikatlar (kuzatuv)
# =============================================================================

async def admin_list_certificates(search: str = "", limit: int = 30, offset: int = 0) -> list[dict]:
    async with async_session() as session:
        query = (
            select(UserCertificate, WebUser.email, WebUser.first_name)
            .join(WebUser, WebUser.id == UserCertificate.user_id)
            .order_by(desc(UserCertificate.id))
            .limit(limit).offset(offset)
        )
        if search:
            like = f"%{search.strip()}%"
            query = query.where((WebUser.email.ilike(like)) | (WebUser.first_name.ilike(like)) | (UserCertificate.verification_id.ilike(like)))
        result = await session.execute(query)
        return [
            {"cert": cert, "email": email, "first_name": first_name}
            for cert, email, first_name in result.all()
        ]


async def admin_count_certificates(search: str = "") -> int:
    async with async_session() as session:
        query = select(func.count(UserCertificate.id)).select_from(UserCertificate).join(WebUser, WebUser.id == UserCertificate.user_id)
        if search:
            like = f"%{search.strip()}%"
            query = query.where((WebUser.email.ilike(like)) | (WebUser.first_name.ilike(like)) | (UserCertificate.verification_id.ilike(like)))
        return (await session.execute(query)).scalar_one()


# =============================================================================
# TARIF LIMITLARI — AI repetitor kunlik xabar soni
# =============================================================================

async def _ai_window_usage(session, user_id: int, window_hours: int) -> tuple[int, datetime | None]:
    """Oxirgi `window_hours` soat ichida yuborilgan AI xabarlar soni va shu
    oyna ichidagi ENG ESKI xabar vaqtini qaytaradi (ikkinchisi — "qachon
    birinchi bo'sh o'rin ochiladi" ni hisoblash uchun kerak)."""
    cutoff = datetime.utcnow() - timedelta(hours=window_hours)
    result = await session.execute(
        select(AiMessageLog.created_at)
        .where(AiMessageLog.user_id == user_id, AiMessageLog.created_at >= cutoff)
        .order_by(AiMessageLog.created_at)
    )
    rows = [r[0] for r in result.all()]
    oldest = rows[0] if rows else None
    return len(rows), oldest


async def check_and_use_ai_message(user_id: int) -> dict:
    """
    Foydalanuvchi AI repetitorga savol yubormoqchi bo'lganda ChAQIRILADI —
    limitni tekshiradi VA (ruxsat bo'lsa) darhol yozadi.

    MUHIM — SIRPANUVCHI OYNA (sliding window), KUNLIK EMAS: limit yarim
    tunda BIRDANIGA qaytmaydi — "oxirgi N soat ichida nechta xabar
    yuborilgan" tekshiriladi (N = tarifga bog'liq: Bepul 3 soat, Pro/Ultra
    5 soat). Har bir eski xabar aynan N soatdan keyin oynadan "chiqib
    ketadi" va o'z o'rnini avtomatik bo'shatadi — aniq so'ralganidek,
    "soatga qarab orqaga qarab ketaveradi", bitta joyda birdaniga ochilmaydi.

    Qaytaradi: {"allowed": bool, "used": int, "limit": int|None, "plan": str,
                "window_hours": int, "retry_after_seconds": int|None}
    limit=None — cheksiz (Ultra) degani. retry_after_seconds — limit tugagan
    bo'lsa, keyingi bo'sh o'rin necha soniyadan keyin ochilishini bildiradi
    (frontendda "X daqiqadan keyin yana yozishingiz mumkin" ko'rsatish uchun).
    """
    async with async_session() as session:
        user = await session.get(WebUser, user_id)
        if user is None:
            return {"allowed": False, "used": 0, "limit": 0, "plan": "free", "window_hours": 3, "retry_after_seconds": None}

        limits = get_plan_limits(user.plan)
        limit = limits["ai_daily"]
        window_hours = limits.get("ai_window_hours", 3)

        used, oldest = await _ai_window_usage(session, user_id, window_hours)

        if limit is not None and used >= limit:
            retry_after = None
            if oldest is not None:
                free_at = oldest + timedelta(hours=window_hours)
                retry_after = max(0, int((free_at - datetime.utcnow()).total_seconds()))
            return {
                "allowed": False, "used": used, "limit": limit, "plan": user.plan,
                "window_hours": window_hours, "retry_after_seconds": retry_after,
            }

        session.add(AiMessageLog(user_id=user_id, created_at=datetime.utcnow()))
        await session.commit()
        _cache_invalidate(user_id)
        return {
            "allowed": True, "used": used + 1, "limit": limit, "plan": user.plan,
            "window_hours": window_hours, "retry_after_seconds": None,
        }


async def get_ai_usage_status(user_id: int) -> dict:
    """Faqat KO'RSATISH uchun (masalan Settings/limit ko'rsatkichi uchun) —
    hisoblagichni O'ZGARTIRMAYDI, faqat joriy sirpanuvchi oyna holatini
    qaytaradi."""
    async with async_session() as session:
        user = await session.get(WebUser, user_id)
        if user is None:
            return {"used": 0, "limit": 0, "plan": "free", "window_hours": 3, "retry_after_seconds": None}
        limits = get_plan_limits(user.plan)
        limit = limits["ai_daily"]
        window_hours = limits.get("ai_window_hours", 3)
        used, oldest = await _ai_window_usage(session, user_id, window_hours)
        retry_after = None
        if limit is not None and used >= limit and oldest is not None:
            free_at = oldest + timedelta(hours=window_hours)
            retry_after = max(0, int((free_at - datetime.utcnow()).total_seconds()))
        return {
            "used": used, "limit": limit, "plan": user.plan,
            "window_hours": window_hours, "retry_after_seconds": retry_after,
        }


# ============================================================================
# DASHBOARD — barcha ko'rsatkichlar REAL natijalardan hisoblanadi
# ============================================================================
WEEKLY_QUESTION_GOAL = 100
DAILY_QUESTION_GOAL = 10  # standart; foydalanuvchi profilda o'zgartiradi (WebUser.daily_goal)
_SKIP_TOPICS = {"", "Mavzusiz test"}


def _pct(correct: int, total: int) -> int:
    return round(correct * 100 / total) if total else 0


def _display_name(first_name: str, email: str) -> str:
    name = (first_name or "").strip()
    return name[:20] if name else (email.split("@")[0][:12] if email else "Foydalanuvchi")


async def get_leaderboard(period: str = "all", limit: int = 10, me_id: int | None = None) -> dict:
    """Ball = to'g'ri javoblar soni. period: 'week' | 'all'."""
    since = datetime.utcnow() - timedelta(days=7) if period == "week" else None
    async with async_session() as session:
        q = (
            select(
                WebQuizLog.user_id,
                func.sum(WebQuizLog.correct_count).label("pts"),
                func.sum(WebQuizLog.total_count).label("tot"),
                func.count(WebQuizLog.id).label("n"),
            )
            .group_by(WebQuizLog.user_id)
            .having(func.sum(WebQuizLog.total_count) > 0)
        )
        if since:
            q = q.where(WebQuizLog.created_at >= since)
        rows = (await session.execute(q)).all()
        rows.sort(key=lambda r: (-(r.pts or 0), -_pct(r.pts or 0, r.tot or 0), r.user_id))
        ids = [r.user_id for r in rows[:limit]]
        if me_id is not None and me_id not in ids and any(r.user_id == me_id for r in rows):
            ids.append(me_id)
        users = {}
        if ids:
            ures = await session.execute(select(WebUser).where(WebUser.id.in_(ids)))
            users = {u.id: u for u in ures.scalars().all()}
    entries = []
    for pos, r in enumerate(rows, start=1):
        if r.user_id not in ids:
            continue
        u = users.get(r.user_id)
        entries.append({
            "rank": pos, "name": _display_name(u.first_name if u else "", u.email if u else ""),
            "points": int(r.pts or 0), "accuracy": _pct(r.pts or 0, r.tot or 0), "quizzes": int(r.n),
            "is_me": r.user_id == me_id, "plan": (u.plan if u else "free"),
        })
    return {"entries": entries, "total": len(rows)}


async def get_dashboard_data(user: "WebUser") -> dict:
    now = datetime.utcnow()
    today = now.date()
    async with async_session() as session:
        logs = list((await session.execute(
            select(WebQuizLog).where(WebQuizLog.user_id == user.id).order_by(WebQuizLog.created_at)
        )).scalars().all())
        cert_count = (await session.execute(
            select(func.count(UserCertificate.id)).where(UserCertificate.user_id == user.id)
        )).scalar() or 0
        chat_today = (await session.execute(
            select(func.count(ChatLog.id)).where(
                ChatLog.user_id == user.id, ChatLog.created_at >= datetime.combine(today, datetime.min.time()))
        )).scalar() or 0
        missed_count = (await session.execute(
            select(func.count(MissedQuestion.id)).where(MissedQuestion.user_id == user.id)
        )).scalar() or 0

    total_q = sum(l.total_count for l in logs)
    total_c = sum(l.correct_count for l in logs)
    scores = [_pct(l.correct_count, l.total_count) for l in logs if l.total_count]
    week_ago = now - timedelta(days=7)
    two_weeks_ago = now - timedelta(days=14)
    week_logs = [l for l in logs if l.created_at >= week_ago]
    prev_week_logs = [l for l in logs if two_weeks_ago <= l.created_at < week_ago]
    today_logs = [l for l in logs if l.created_at.date() == today]
    week_q = sum(l.total_count for l in week_logs)
    today_q = sum(l.total_count for l in today_logs)

    def avg(ls):
        vals = [_pct(l.correct_count, l.total_count) for l in ls if l.total_count]
        return round(sum(vals) / len(vals)) if vals else 0

    avg_all, avg_week, avg_prev = avg(logs), avg(week_logs), avg(prev_week_logs)

    # --- Mavzu o'zlashtirish (halqalar) va zaif mavzular: foydalanuvchining joriy fani bo'yicha ---
    by_topic: dict[str, dict] = {}
    for l in logs:
        if l.subject != user.subject or (l.topic or "") in _SKIP_TOPICS:
            continue
        e = by_topic.setdefault(l.topic, {"c": 0, "t": 0, "n": 0, "last": l.created_at})
        e["c"] += l.correct_count
        e["t"] += l.total_count
        e["n"] += 1
        e["last"] = max(e["last"], l.created_at)
    practiced = [
        {"topic": t, "percent": _pct(e["c"], e["t"]), "attempts": e["n"], "questions": e["t"]}
        for t, e in by_topic.items() if e["t"] > 0
    ]
    mastery = sorted(practiced, key=lambda x: (-x["attempts"], -x["questions"]))[:4]
    weak = sorted(practiced, key=lambda x: (x["percent"], -x["questions"]))[:4]
    weak = [w for w in weak if w["percent"] < 80]
    if len(mastery) < 4 and user.subject:
        try:
            names = await list_topics_db(user.subject, user.certificate_type or "dtm")
        except Exception:
            names = []
        have = {m["topic"] for m in mastery}
        for n in names:
            if len(mastery) >= 4:
                break
            if n not in have:
                mastery.append({"topic": n, "percent": 0, "attempts": 0, "questions": 0})

    # --- Tarix grafigi: so'nggi 80 natija (davr tanlash brauzerda) ---
    history = [
        {"percent": _pct(l.correct_count, l.total_count), "topic": l.topic or "Mavzusiz",
         "date": l.created_at.strftime("%d.%m"), "iso": l.created_at.strftime("%Y-%m-%d"),
         "subject": SUBJECT_NAMES.get(l.subject, l.subject)}
        for l in logs[-80:]
    ]

    # --- Bugungi reja ---
    goal_q = max(1, min(200, getattr(user, "daily_goal", None) or DAILY_QUESTION_GOAL))
    weak_topic = weak[0]["topic"] if weak else None
    plan_items = [
        {"text": "Bugun kamida 1 ta test yeching", "done": len(today_logs) >= 1, "href": "/quiz"},
        {"text": f"Bugun {goal_q} ta savolga javob bering", "done": today_q >= goal_q,
         "href": "/quiz", "meta": f"{min(today_q, goal_q)}/{goal_q}"},
        {"text": f"Zaif mavzu: {weak_topic}" if weak_topic else "Xato qilingan savollarni takrorlang",
         "done": bool(weak_topic and any(l.topic == weak_topic for l in today_logs)) or (not weak_topic and missed_count == 0 and bool(logs)),
         "href": "/quiz", "meta": (f"{missed_count} ta xato" if missed_count else "")},
        {"text": "AI repetitorga savol bering", "done": chat_today > 0, "href": "/repetitor"},
    ]

    streak = user.streak_days or 0
    achievements = [
        {"key": "first", "title": "Birinchi qadam", "desc": "1-testni yeching", "done": len(logs) >= 1, "icon": "flag"},
        {"key": "five", "title": "Faol o'quvchi", "desc": "5 ta test", "done": len(logs) >= 5, "icon": "book"},
        {"key": "ace", "title": "A'lochi", "desc": "Testda 90%+", "done": any(s >= 90 for s in scores), "icon": "star"},
        {"key": "perfect", "title": "Mukammal", "desc": "100% natija", "done": any(s == 100 for s in scores), "icon": "trophy"},
        {"key": "streak3", "title": "3 kunlik seriya", "desc": "Ketma-ket 3 kun", "done": streak >= 3, "icon": "flame"},
        {"key": "streak7", "title": "Haftalik seriya", "desc": "Ketma-ket 7 kun", "done": streak >= 7, "icon": "flame"},
        {"key": "q100", "title": "100 savol", "desc": "100 ta savol yeching", "done": total_q >= 100, "icon": "target"},
        {"key": "cert", "title": "Sertifikat egasi", "desc": "Sertifikat oling", "done": cert_count > 0, "icon": "award"},
    ]

    xp = total_c * 10
    level_no = 1 + xp // 500
    board_all = await get_leaderboard("all", 10, user.id)
    board_week = await get_leaderboard("week", 10, user.id)
    my_rank = next((e["rank"] for e in board_all["entries"] if e["is_me"]), None)

    return {
        "total_quizzes": len(logs), "total_questions": total_q, "total_correct": total_c,
        "accuracy": _pct(total_c, total_q), "avg_score": avg_all,
        "best_score": max(scores) if scores else 0,
        "week_questions": week_q, "week_goal": WEEKLY_QUESTION_GOAL,
        "week_percent": min(100, _pct(week_q, WEEKLY_QUESTION_GOAL)),
        "week_quizzes": len(week_logs),
        "trend": (avg_week - avg_prev) if (week_logs and prev_week_logs) else None,
        "time_spent_min": round(sum(l.time_spent_seconds for l in logs) / 60),
        "today_questions": today_q, "streak": streak,
        "xp": xp, "level_no": level_no, "level_progress": (xp % 500) * 100 // 500, "xp_to_next": 500 - xp % 500,
        "mastery": mastery, "weak": weak, "history": history, "plan": plan_items,
        "plan_done": sum(1 for p in plan_items if p["done"]), "achievements": achievements,
        "achievements_done": sum(1 for a in achievements if a["done"]),
        "board_all": board_all, "board_week": board_week, "my_rank": my_rank,
        "last_percent": scores[-1] if scores else 0,
        "delta_last": (scores[-1] - scores[-2]) if len(scores) >= 2 else None,
        "subject_avg": avg([l for l in logs if l.subject == user.subject]),
        "subject_quizzes": sum(1 for l in logs if l.subject == user.subject),
        "last_quiz": ({"topic": logs[-1].topic or "Mavzusiz", "percent": _pct(logs[-1].correct_count, logs[-1].total_count),
                       "id": logs[-1].id} if logs else None),
    }


# ============================================================================
# ADMIN — mavzular markazi va mavzu tahrirlagichi
# ============================================================================
import hashlib as _hashlib
import json as _json_style

STYLE_LIMITS = {  # kalit: (min, max)
    "fs": (0.9, 2.6), "fw": (400, 800), "lh": (1.1, 2.2), "mt": (0, 80), "mb": (0, 80),
    "pd": (8, 56), "og": (4, 32), "ox": (-120, 120), "oy": (-60, 120),
}
STYLE_CHOICES = {"al": {"left", "center", "right"}}
LAYOUT_LIMITS = {"timerSize": (0.8, 2.4), "cardW": (480, 960)}
LAYOUT_CHOICES = {
    "timer": {"show", "hide"}, "timerPos": {"left", "center", "right"}, "header": {"show", "hide"},
    "progress": {"show", "hide"}, "nav": {"between", "center", "right"},
}


def sanitize_style(raw: dict | None) -> dict:
    """Admin yuborgan ko'rinish sozlamalarini tekshiradi: faqat ruxsat etilgan kalitlar va chegaralar."""
    out: dict = {}
    if not isinstance(raw, dict):
        return out
    for k, (lo, hi) in STYLE_LIMITS.items():
        if k in raw:
            try:
                out[k] = round(min(hi, max(lo, float(raw[k]))), 2)
            except (TypeError, ValueError):
                pass
    for k, allowed in STYLE_CHOICES.items():
        if raw.get(k) in allowed:
            out[k] = raw[k]
    col = raw.get("col")
    if isinstance(col, str) and len(col) == 7 and col.startswith("#") and all(c in "0123456789abcdefABCDEF" for c in col[1:]):
        out["col"] = col.lower()
    return out


def sanitize_layout(raw: dict | None) -> dict:
    out: dict = {}
    if not isinstance(raw, dict):
        return out
    for k, (lo, hi) in LAYOUT_LIMITS.items():
        if k in raw:
            try:
                out[k] = round(min(hi, max(lo, float(raw[k]))), 2)
            except (TypeError, ValueError):
                pass
    for k, allowed in LAYOUT_CHOICES.items():
        if raw.get(k) in allowed:
            out[k] = raw[k]
    return out


def _layout_key(subject: str, mode: str, topic: str) -> str:
    return "ql:" + _hashlib.sha1(f"{subject}|{mode}|{topic}".encode("utf-8")).hexdigest()[:24]


async def get_topic_layout(subject: str, mode: str, topic: str) -> dict:
    if not topic:
        return {}
    raw = await get_setting(_layout_key(subject, mode, topic), "")
    if not raw:
        return {}
    try:
        return sanitize_layout(_json_style.loads(raw))
    except ValueError:
        return {}


async def set_topic_layout(subject: str, mode: str, topic: str, layout: dict) -> None:
    await set_setting(_layout_key(subject, mode, topic), _json_style.dumps(sanitize_layout(layout), ensure_ascii=False))


async def admin_topic_overview(subject: str = "", mode: str = "", search: str = "") -> list[dict]:
    """Har bir (fan, rejim, mavzu) uchun: savollar soni, faol/yashirin, yakuniy test, mock testlar, oxirgi qo'shilgan."""
    from sqlalchemy import case
    async with async_session() as session:
        q = (
            select(
                Question.subject, Question.mode, Question.topic,
                func.count(Question.id).label("total"),
                func.sum(case((Question.is_active == True, 1), else_=0)).label("active"),  # noqa: E712
                func.sum(case((Question.is_final_test == True, 1), else_=0)).label("final"),  # noqa: E712
                func.sum(case((func.coalesce(Question.style_json, "") != "", 1), else_=0)).label("styled"),
                func.count(func.distinct(Question.mock_test)).label("mocks"),
                func.max(Question.id).label("last_id"),
            )
            .group_by(Question.subject, Question.mode, Question.topic)
        )
        if subject:
            q = q.where(Question.subject == subject)
        if mode:
            q = q.where(Question.mode == mode)
        if search:
            q = q.where(Question.topic.ilike(f"%{search.strip()}%"))
        rows = (await session.execute(q)).all()
    items = [
        {"subject": r.subject, "mode": r.mode, "topic": r.topic, "total": int(r.total), "active": int(r.active or 0),
         "hidden": int(r.total) - int(r.active or 0), "final": int(r.final or 0), "styled": int(r.styled or 0),
         "mocks": int(r.mocks or 0), "last_id": int(r.last_id or 0)}
        for r in rows
    ]
    async with async_session() as session:
        topic_rows = (await session.execute(select(Topic.subject, Topic.mode, Topic.name))).all()
    have = {(i["subject"], i["mode"], i["topic"]) for i in items}
    needle = search.strip().lower()
    for subj, md, name in topic_rows:
        if (subj, md, name) in have or (subject and subj != subject) or (mode and md != mode):
            continue
        if needle and needle not in name.lower():
            continue
        items.append({"subject": subj, "mode": md, "topic": name, "total": 0, "active": 0, "hidden": 0,
                      "final": 0, "styled": 0, "mocks": 0, "last_id": 0})
    items.sort(key=lambda x: (x["subject"], x["mode"], x["topic"].lower()))
    return items


async def admin_create_topic(subject: str, mode: str, name: str) -> bool:
    name = " ".join(name.split())[:150]
    if not name:
        return False
    async with async_session() as session:
        exists_t = (await session.execute(select(Topic.id).where(Topic.subject == subject, Topic.mode == mode, Topic.name == name))).first()
        exists_q = (await session.execute(select(Question.id).where(Question.subject == subject, Question.mode == mode, Question.topic == name).limit(1))).first()
        if exists_t or exists_q:
            return False
        session.add(Topic(subject=subject, mode=mode, name=name))
        await session.commit()
        return True


async def admin_delete_topic(subject: str, mode: str, topic: str) -> int:
    """Mavzuni va undagi barcha savollarni o'chiradi. O'chirilgan savollar soni qaytadi."""
    from sqlalchemy import delete as sa_delete
    async with async_session() as session:
        rows = (await session.execute(select(Question.id).where(Question.subject == subject, Question.mode == mode, Question.topic == topic))).all()
    for (qid,) in rows:
        await admin_delete_question(qid)
    async with async_session() as session:
        await session.execute(sa_delete(Topic).where(Topic.subject == subject, Topic.mode == mode, Topic.name == topic))
        await session.commit()
    return len(rows)


async def admin_rename_topic(subject: str, mode: str, old: str, new: str) -> bool:
    from sqlalchemy import update as sa_update
    new = " ".join(new.split())[:150]
    if not new or new == old:
        return False
    async with async_session() as session:
        clash = (await session.execute(select(Question.id).where(Question.subject == subject, Question.mode == mode, Question.topic == new).limit(1))).first()
        clash_t = (await session.execute(select(Topic.id).where(Topic.subject == subject, Topic.mode == mode, Topic.name == new))).first()
        if clash or clash_t:
            return False
        await session.execute(sa_update(Question).where(Question.subject == subject, Question.mode == mode, Question.topic == old).values(topic=new))
        await session.execute(sa_update(Topic).where(Topic.subject == subject, Topic.mode == mode, Topic.name == old).values(name=new))
        await session.commit()
        return True


async def admin_topic_questions(subject: str, mode: str, topic: str) -> list["Question"]:
    async with async_session() as session:
        res = await session.execute(
            select(Question).where(Question.subject == subject, Question.mode == mode, Question.topic == topic)
            .order_by(Question.id)
        )
        return list(res.scalars().all())


# ---------------------------------------------------------------------------
# PROFIL: tahrirlash, parol, ma'lumotlarni yuklab olish va akkauntni o'chirish
# ---------------------------------------------------------------------------
AVATAR_COLORS = ("#2FBF83", "#4A9EFF", "#FFA726", "#B388FF", "#FF6B8A", "#26C6DA", "#9CCC65", "#FF7043")


async def update_user_profile(user_id: int, first_name: str | None = None, daily_goal: int | None = None,
                              target_percent: int | None = None, avatar_color: str | None = None) -> None:
    async with async_session() as session:
        user = (await session.execute(select(WebUser).where(WebUser.id == user_id))).scalar_one_or_none()
        if user is None:
            return
        if first_name is not None:
            user.first_name = first_name.strip()[:60]
        if daily_goal is not None:
            user.daily_goal = max(1, min(200, int(daily_goal)))
        if target_percent is not None:
            user.target_percent = max(10, min(100, int(target_percent)))
        if avatar_color is not None and (avatar_color in AVATAR_COLORS or avatar_color == ""):
            user.avatar_color = avatar_color
        await session.commit()
    _cache_invalidate(user_id)


async def set_user_password_hash(user_id: int, password_hash: str) -> None:
    async with async_session() as session:
        user = (await session.execute(select(WebUser).where(WebUser.id == user_id))).scalar_one_or_none()
        if user is not None:
            user.password_hash = password_hash
            await session.commit()
    _cache_invalidate(user_id)


def _user_owned_tables():
    return [t for t in Base.metadata.sorted_tables if "user_id" in t.c and t.name != "web_users"]


async def export_user_data(user_id: int) -> dict:
    """Foydalanuvchining barcha shaxsiy ma'lumotlari (parol xeshisiz) — yuklab olish uchun."""
    out: dict = {}
    async with async_session() as session:
        user = (await session.execute(select(WebUser).where(WebUser.id == user_id))).scalar_one_or_none()
        if user is None:
            return out
        out["profil"] = {
            "email": user.email, "ism": user.first_name, "tarif": user.plan, "fan": user.subject,
            "daraja": user.level, "imtihon": user.certificate_type, "qoshilgan": str(user.joined_at),
            "streak": user.streak_days, "kunlik_maqsad": user.daily_goal, "maqsadli_foiz": user.target_percent,
        }
        for table in _user_owned_tables():
            rows = (await session.execute(select(table).where(table.c.user_id == user_id))).mappings().all()
            out[table.name] = [{k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in dict(r).items()} for r in rows]
    return out


async def delete_user_account(user_id: int) -> None:
    """Foydalanuvchi va unga bog'langan barcha yozuvlarni qaytarib bo'lmaydigan tarzda o'chiradi."""
    from sqlalchemy import delete as sa_delete
    async with async_session() as session:
        for table in _user_owned_tables():
            await session.execute(sa_delete(table).where(table.c.user_id == user_id))
        await session.execute(sa_delete(WebUser).where(WebUser.id == user_id))
        await session.commit()
    _cache_invalidate(user_id)


# ---------------------------------------------------------------------------
# ADMIN BOSH SAHIFA — haqiqiy ma'lumotlar bo'yicha umumiy ko'rinish
# ---------------------------------------------------------------------------
BANK_TARGET_PER_SUBJECT = 3000


async def admin_overview() -> dict:
    """Admin boshqaruv markazi uchun: 14 kunlik faollik, tariflar ulushi, oxirgi harakatlar, zaif mavzular, bank to'liqligi."""
    from datetime import time as _time
    today = date.today()
    days = [today - timedelta(days=i) for i in range(13, -1, -1)]
    since = datetime.combine(days[0], _time.min)
    async with async_session() as session:
        quiz_rows = (await session.execute(
            select(WebQuizLog.created_at).where(WebQuizLog.created_at >= since)
        )).scalars().all()
        signup_rows = (await session.execute(
            select(WebUser.joined_at).where(WebUser.joined_at >= days[0])
        )).scalars().all()
        quiz_by_day = {d: 0 for d in days}
        for ts in quiz_rows:
            d = ts.date() if hasattr(ts, "date") else ts
            if d in quiz_by_day:
                quiz_by_day[d] += 1
        signup_by_day = {d: 0 for d in days}
        for d in signup_rows:
            if d in signup_by_day:
                signup_by_day[d] += 1

        plan_rows = (await session.execute(select(WebUser.plan, func.count(WebUser.id)).group_by(WebUser.plan))).all()
        plans = {"free": 0, "pro": 0, "ultra": 0}
        for plan, cnt in plan_rows:
            plans[plan if plan in plans else "free"] += cnt

        recent_users = [
            {"id": u.id, "name": u.first_name or "—", "email": u.email, "plan": u.plan, "subject": SUBJECT_NAMES.get(u.subject, u.subject or "—"), "joined": u.joined_at.strftime("%d.%m.%Y")}
            for u in (await session.execute(select(WebUser).order_by(desc(WebUser.id)).limit(6))).scalars().all()
        ]
        recent_quizzes = []
        for log, name in (await session.execute(
            select(WebQuizLog, WebUser.first_name).join(WebUser, WebUser.id == WebQuizLog.user_id).order_by(desc(WebQuizLog.id)).limit(8)
        )).all():
            pct = round(log.correct_count * 100 / log.total_count) if log.total_count else 0
            recent_quizzes.append({"name": name or "—", "subject": SUBJECT_NAMES.get(log.subject, log.subject), "topic": log.topic or "Mavzusiz",
                                   "percent": pct, "when": log.created_at.strftime("%d.%m %H:%M")})

        weak_rows = (await session.execute(
            select(WebQuizLog.subject, WebQuizLog.topic, func.sum(WebQuizLog.correct_count), func.sum(WebQuizLog.total_count), func.count(WebQuizLog.id))
            .where(WebQuizLog.topic != "").group_by(WebQuizLog.subject, WebQuizLog.topic)
        )).all()
        weak = sorted(
            [{"subject": SUBJECT_NAMES.get(s, s), "topic": t, "percent": round(c * 100 / n) if n else 0, "attempts": a}
             for s, t, c, n, a in weak_rows if n and a >= 2],
            key=lambda r: r["percent"])[:6]

        bank_rows = (await session.execute(
            select(Question.subject, func.count(Question.id), func.count(func.distinct(Question.topic)))
            .where(Question.is_active.is_(True)).group_by(Question.subject)
        )).all()
        subject_breakdown = sorted(
            [{"subject": s, "name": SUBJECT_NAMES.get(s, s), "question_count": q, "topic_count": t,
              "percent": min(100, round(q * 100 / BANK_TARGET_PER_SUBJECT))} for s, q, t in bank_rows],
            key=lambda r: -r["question_count"])
        unread = (await session.execute(select(func.count(SupportMessage.id)).where(SupportMessage.is_read.is_(False)))).scalar_one()
    return {
        "days": [d.strftime("%d.%m") for d in days],
        "signups": [signup_by_day[d] for d in days], "quizzes": [quiz_by_day[d] for d in days],
        "plans": plans, "recent_users": recent_users, "recent_quizzes": recent_quizzes, "weak": weak,
        "subject_breakdown": subject_breakdown, "unread_messages": unread, "bank_target": BANK_TARGET_PER_SUBJECT,
        "db_engine": "PostgreSQL" if "postgres" in DATABASE_URL else "SQLite",
    }
