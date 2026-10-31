"""
LongoUZ websayt uchun AI router.
Ikkita AI provayderni (Gemini, Claude) BITTA joydan boshqaradi — main.py faqat
shu moduldagi funksiyalarni chaqiradi, qaysi AI ishlatilishini bilishi shart emas.

MUHIM — AVTOMATIK ZAXIRA ZANJIRI (fallback chain):
Claude API'da doimiy bepul tarif yo'q (faqat yangi hisoblar uchun bir martalik
sinov krediti) — shuning uchun kredit tugasa yoki kalit sozlanmagan bo'lsa,
sayt "buzilib" qolmasligi kerak. Shu sabab har bir funksiya quyidagi zanjir
bo'yicha ishlaydi:

  1. Claude   — eng sifatli javob (agar sozlangan va kredit yetarli bo'lsa)
  2. Gemini   — Google AI Studio'ning DOIMIY bepul tarifi (karta kerak emas:
                https://ai.google.dev), Claude ishlamasa avtomatik ishga tushadi
  3. Statik bank (faqat test generatsiyasi uchun, static_questions.py) —
                hech qanday kalit kerak emas, ENG OXIRGI zaxira

Foydalanuvchi qaysi provayder javob berganini SEZMAYDI — faqat "javob keldi"
yoki "test tayyor" ko'radi. `provider` maydoni faqat ichki log/statistika uchun.

MUHIM — QATTIQ VAQT CHEGARASI (timeout):
Anthropic SDK'ning standart kutish vaqti 10 daqiqagacha (!), Gemini esa
o'zi ichida bir necha marta qayta urinishi mumkin ("high demand" xatolarida).
Agar shularga ishonib qo'ya qolsak, bitta AI "sekinlashib qolsa" ham
foydalanuvchi bir necha daqiqa hech narsa ko'rmay kutib qoladi — bu esa
"test darhol chiqishi kerak" degan asosiy talabga zid. Shu sababli HAR BIR
chaqiruv o'zimizning qattiq vaqt chegaramiz bilan o'raladi (asyncio.wait_for):
muddat tugasa, o'sha provayder shunchaki "ishlamadi" deb hisoblanadi va
zanjir keyingisiga (yoki statik bankka) DARHOL o'tadi.
"""

import asyncio
import logging

import ai_diagnostics
import ai_gemini as gemini
import ai_claude as claude
import static_questions
import database as db
from ai_config import GEMINI_LEVELS

logger = logging.getLogger(__name__)

# DIQQAT — 2026-09-30: production loglarida Gemini so'rovlari DOIM (har bir
# chaqiruvda) 12 soniyalik chegarada "vaqt tugadi" bo'lib chiqdi, lekin
# ai_gemini.py'ning o'zidagi xato logi (`Gemini javob bermadi...`) HECH QACHON
# ko'rinmadi — bu shuni bildiradi: so'rov Google serveridan tezkor xato (masalan
# noto'g'ri model nomi — bu HAR DOIM tez, bir necha soniyada 404/400 qaytaradi)
# bilan emas, balki tarmoq darajasida "osilib qolib" (javob ham, xato ham
# kelmay) ishlamayapti. Bu ko'proq server-Google API orasidagi tarmoq/latency
# muammosiga o'xshaydi, nazariy jihatdan noto'g'ri model nomiga emas — shuning
# uchun GEMINI_MODEL qiymati bu yerda "taxmin bilan" o'zgartirilmadi. Chegara
# 12s dan 18s ga oshirildi — qayta urinish (retry) zanjiri (ai_gemini.py,
# _RETRY_DELAYS_SECONDS) o'zi ham ~3s kutish qo'shishi mumkinligini hisobga
# olib, haqiqatan sekin (lekin ishlaydigan) javobga ko'proq imkon berish uchun.
ASK_TIMEOUT_SECONDS = 25
# Claude birinchi navbatda — u sekin bo'lsa zaxira (Gemini)ga tezroq o'tamiz:
# foydalanuvchi ovozli suhbatda 36 soniya kutib qolmasin.
CLAUDE_ASK_TIMEOUT_SECONDS = 24
# Test generatsiyasi (ayniqsa DTM'ning 30 savoli) ko'proq token yozadi,
# lekin baribir bu chegaradan oshsa — foydalanuvchi kutishi shart emas,
# statik bank baribir tayyor turibdi. Claude va Gemini alohida cheklanadi
# (ikkalasi ketma-ket ishlamay qolsa ham, umumiy kutish ~18s dan oshmasin —
# avvalgi holatda ikkalasi 20s+20s=40s gacha kutib, foydalanuvchini
# charchatib qo'yardi).
QUIZ_TIMEOUT_CLAUDE_SECONDS = 8
QUIZ_TIMEOUT_GEMINI_SECONDS = 8
EVALUATE_TIMEOUT_SECONDS = 9


async def _with_timeout(coro, seconds: float, label: str):
    """
    Har qanday AI chaqiruvini belgilangan soniyada "kesib qo'yadi". Agar
    shu vaqt ichida javob kelmasa (SDK o'zi ichida sekinlashib/qayta urinib
    turgan bo'lishi mumkin), None qaytariladi — chaqiruvchi funksiya buni
    oddiy "ishlamadi" holati sifatida qabul qilib, keyingi provayderga o'tadi.
    """
    import time
    started = time.monotonic()
    try:
        return await asyncio.wait_for(coro, timeout=seconds)
    except asyncio.TimeoutError:
        elapsed = time.monotonic() - started
        ai_diagnostics.record_error("gemini" if "Gemini" in label else "claude", "timeout")
        logger.warning(
            f"{label}: {seconds}s ichida javob kelmadi (aslida {elapsed:.1f}s kutildi) — "
            f"keyingisiga o'tiladi. Agar bu doimo takrorlansa va ai_gemini.py/ai_claude.py'da "
            f"hech qanday xato logi ko'rinmasa — server bilan AI provayder orasida tarmoq "
            f"muammosi bo'lishi mumkin (SDK hech qanday javob/xatoni qaytarmay 'osilib qolgan')."
        )
        return None


import re as _re

_MD_STRIP = _re.compile(r"(\*\*|__|`+|^#{1,6}\s*|^\s*[-*•]\s+)", _re.MULTILINE)
_EMOJI = _re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]")


def _clean_spoken(text: str) -> str:
    """Ovoz chiqarib o'qiladigan javobdan markdown/emoji/LaTeX belgilarini olib tashlaydi."""
    text = _MD_STRIP.sub("", text)
    text = _EMOJI.sub("", text)
    text = text.replace("\\(", "").replace("\\)", "").replace("\\[", "").replace("\\]", "").replace("$", "")
    text = _re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", text)
    text = _re.sub(r"\\(frac|cdot|times|sqrt|le|ge|neq|pi)\b", lambda m: {"frac": "", "cdot": "*", "times": "*", "sqrt": "sqrt", "le": "<=", "ge": ">=", "neq": "!=", "pi": "pi"}[m.group(1)], text)
    return _re.sub(r"[ \t]+\n", "\n", text).strip()


async def ask_tutor(
    question: str, subject: str, level: str, certificate_type: str | None = None,
    effort: str = "normal", source: str = "widget",
    history: list[dict] | None = None, lang: str | None = None,
) -> tuple[str, str]:
    """
    Repetitor javobi: (matn, provider). TARTIB: Gemini (tez, suhbat tarixi bilan) -> Claude (zaxira).
    Ikkalasi ham bir xil "ustoz" promptidan foydalanadi (ai_tutor_prompt.py). Hech biri ishlamasa,
    sababi (kalit/kredit/limit/tarmoq) tushunarli xabar bilan qaytariladi.
    """
    label_suffix = "repetitor" if source == "repetitor" else "widget"
    hist = history

    async def _try_gemini():
        if not gemini.is_gemini_configured():
            return None
        a = await _with_timeout(
            gemini.ask_gemini(question, subject, effort, level, certificate_type, hist, lang),
            ASK_TIMEOUT_SECONDS, f"Gemini (ask, {label_suffix})",
        )
        return (_clean_spoken(a), "gemini") if a else None

    async def _try_claude():
        if not claude.is_claude_configured():
            return None
        a = await _with_timeout(
            claude.ask_claude(question, subject, level, certificate_type, effort, hist, lang),
            CLAUDE_ASK_TIMEOUT_SECONDS, f"Claude (ask, {label_suffix})",
        )
        return (_clean_spoken(a), "claude") if a else None

    # To'liq AI repetitor (aniqlik muhim, ayniqsa matematika/fizika/kimyo) — avval Claude; tezkor suzuvchi chat — avval Gemini.
    # Admin paneldan "ai_primary_repetitor" = claude | gemini bilan almashtirish mumkin (db sozlamasi).
    prefer = (await db.get_setting("ai_primary_repetitor", "claude")) if source == "repetitor" else "gemini"
    chain = (_try_claude, _try_gemini) if prefer == "claude" else (_try_gemini, _try_claude)
    for attempt in chain:
        res = await attempt()
        if res:
            return res

    if not gemini.is_gemini_configured() and not claude.is_claude_configured():
        return (
            "AI repetitor uchun kalit hali sozlanmagan. Administrator GEMINI_API_KEY "
            "(zaxira sifatida ANTHROPIC_API_KEY) qiymatini serverning .env fayliga qo'yishi kerak.",
            "none",
        )

    reason = ai_diagnostics.failure_hint()
    return (
        "AI repetitor hozir javob bera olmadi. "
        + (f"Sabab: {reason} " if reason else "Server band yoki internet sekin bo'lishi mumkin. ")
        + "Savolni birozdan so'ng qayta yuboring.",
        "none",
    )


async def generate_quiz(
    subject: str, level: str, topic: str | None = None, count: int = 5,
    certificate_type: str | None = None, mode: str = "dtm",
    exclude_keys: set[str] | None = None,
) -> list[dict] | None:
    """
    Test generatsiyasi. MUHIM, YANGI TARTIB (foydalanuvchi qarori bilan
    belgilangan): MAVZULASHTIRILGAN testlar uchun ENDI static_questions.py
    (dasturning o'z bazasi — qo'lda tuzilgan, haqiqiy, kitobdagidek savollar)
    ASOSIY manba hisoblanadi. Bu ikkita sabab bilan to'g'ri:
      1. Tezkor — hech qanday API chaqiruvi, kredit sarflanmaydi, foydalanuvchi
         kutmaydi.
      2. Barqaror sifat — AI har safar boshqacha (ba'zan noto'g'ri/tasodifiy)
         savol chiqarishi mumkin, static bank esa qo'lda tekshirilgan.

    AI (Claude -> Gemini) faqat quyidagi holatlarda ZAXIRA sifatida ishga
    tushadi:
      - so'ralgan mavzu static bankda UMUMAN topilmasa (masalan foydalanuvchi
        o'zi erkin mavzu nomi kiritsa)
      - "Mavzusiz test" (aralash, mavzudan tashqari erkin mashq) so'ralganda —
        bu holatda topic=None va explicit erkin so'rov beriladi
      - static bank shu fan uchun umuman bo'sh bo'lib chiqsa

    exclude_keys: foydalanuvchi shu mavzuda ALLAQACHON TO'G'RI ishlagan
    savollarning hash-kalitlari — static bank shularni iloji boricha
    chetlab o'tadi (bir xil savol qayta-qayta chiqavermasligi uchun).
    """
    # --- 1-USTUVORLIK: bazadagi savollar banki (agar mavzu berilgan yoki fan mavjud bo'lsa) ---
    static_pool_has_topic = True
    if topic:
        available_topics = await db.list_topics_db(subject, mode)
        static_pool_has_topic = topic in available_topics

    if static_pool_has_topic:
        static_result = await db.get_questions_db(
            subject, count, mode, topic=topic, exclude_keys=exclude_keys,
        )
        if static_result:
            return static_result

    # --- 2-USTUVORLIK: AI zaxirasi (faqat static bankda topilmagan holatda) ---
    logger.info(
        f"Static bankda mos savol topilmadi (subject={subject}, topic={topic}) — AI zaxirasiga o'tildi."
    )
    questions = await _with_timeout(
        claude.generate_quiz(subject, level, topic, count, certificate_type, mode),
        QUIZ_TIMEOUT_CLAUDE_SECONDS, "Claude (test)",
    )
    if questions:
        return questions

    questions = await _with_timeout(
        gemini.generate_quiz(subject, level, topic, count, certificate_type, mode),
        QUIZ_TIMEOUT_GEMINI_SECONDS, "Gemini (test)",
    )
    if questions:
        return questions

    # --- 3-USTUVORLIK: AI ham ishlamasa, baribir bazadan (mavzusiz) beramiz ---
    logger.info(f"AI ham ishlamadi (subject={subject}) — umumiy bazaga o'tildi.")
    return await db.get_questions_db(subject, count, mode)


async def evaluate_free_answer(question: str, user_answer: str, subject: str, level: str) -> dict | None:
    """Erkin javobni baholash — avval Claude, ishlamasa (yoki kechiksa) Gemini."""
    result = await _with_timeout(
        claude.evaluate_free_answer(question, user_answer, subject, level),
        EVALUATE_TIMEOUT_SECONDS, "Claude (baholash)",
    )
    if result:
        return result
    return await _with_timeout(
        gemini.evaluate_free_answer(question, user_answer, subject, level),
        EVALUATE_TIMEOUT_SECONDS, "Gemini (baholash)",
    )


async def evaluate_speaking(topic_title: str, qa_pairs: list[dict], level: str = "ortacha") -> dict | None:
    """IELTS Speaking transkriptini baholaydi — avval Claude, ishlamasa Gemini."""
    result = await _with_timeout(
        claude.evaluate_speaking(topic_title, qa_pairs, level), EVALUATE_TIMEOUT_SECONDS, "Claude (speaking)",
    )
    if result:
        return result
    return await _with_timeout(
        gemini.evaluate_speaking(topic_title, qa_pairs, level), EVALUATE_TIMEOUT_SECONDS, "Gemini (speaking)",
    )


async def evaluate_writing(topic_title: str, prompt_en: str, essay_text: str) -> dict | None:
    """IELTS Writing inshosini baholaydi — avval Claude, ishlamasa Gemini."""
    result = await _with_timeout(
        claude.evaluate_writing(topic_title, prompt_en, essay_text), EVALUATE_TIMEOUT_SECONDS, "Claude (writing)",
    )
    if result:
        return result
    return await _with_timeout(
        gemini.evaluate_writing(topic_title, prompt_en, essay_text), EVALUATE_TIMEOUT_SECONDS, "Gemini (writing)",
    )


async def judge_open_answers(items: list[dict], subject: str) -> dict[int, bool]:
    """Qoida hal qila olmagan ochiq javoblar: [{i, question, accepted, user}] -> {i: to'g'rimi}.
    Avval Claude, ishlamasa Gemini; ikkalasi ham ishlamasa — bo'sh natija (javoblar noto'g'ri deb qoladi)."""
    if not items:
        return {}
    items = items[:15]
    import ai_diagnostics as _diag
    # v229: kreditsiz/kalitsiz provayder chaqirilmaydi va kutish qisqa — natija o'quvchiga tez chiqsin
    if claude.is_claude_configured() and not _diag.blocked("claude"):
        res = await _with_timeout(claude.judge_answers(items, subject), 6, "Claude (hakamlik)")
        if res:
            return res
    if gemini.is_gemini_configured() and not _diag.blocked("gemini"):
        res = await _with_timeout(gemini.judge_answers(items, subject), 7, "Gemini (hakamlik)")
        if res:
            return res
    return {}


def is_any_ai_configured() -> bool:
    return gemini.is_gemini_configured() or claude.is_claude_configured()
