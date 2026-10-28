"""
LongoUZ websayt uchun Gemini moduli.
Vazifasi: TEZKOR va ODDIY repetitor javoblari — asosan "boshlangich" darajadagi
foydalanuvchilarning erkin savollariga javob berish uchun.

SHAXSIYAT: xuddi ai_claude.py'dagidek — bu "AI" emas, fan bo'yicha o'qituvchi.
Javoblar tabiiy, qisqa, emojisiz, savolga to'g'ridan-to'g'ri javob beradi.

Murakkab tushuntirish, test generatsiyasi va baholash uchun ai_claude.py ishlatiladi
(qarang: web/ai_claude.py va web/ai_router.py).

Muhim: agar ai_config.py'da GEMINI_API_KEY bo'sh bo'lsa, bu modul xato bermaydi -
shunchaki "AI hali sozlanmagan" degan xabar qaytaradi (botdagi ai_tutor.py bilan
bir xil graceful-fallback tamoyili).
"""

import ai_diagnostics
import logging

from google import genai
from google.genai import errors as genai_errors

from ai_config import GEMINI_MODEL, GEMINI_MAX_TOKENS, gemini_key
import ai_keys
from prompt_safety import wrap_user_content

logger = logging.getLogger(__name__)

# google-genai kutubxonasi har bir chaqiruvda "Direct use of automatic
# function calling..." degan ZARARSIZ eslatishni chiqarib turadi. Buni
# shunchaki jimga o'tkazish o'rniga, muammoning ILDIZINI tuzatamiz: har bir
# so'rovga quyidagi konfiguratsiyani qo'shib, AFC'ni SDK hujjatlarida
# tavsiya etilgan usulda butunlay o'chiramiz (biz hech qachon tool/function
# calling ishlatmaymiz, shuning uchun bu bizga umuman kerak emas).
_NO_AFC_CONFIG = {"disable": True}

_client: genai.Client | None = None
_client_key: str = ""


def _get_client() -> genai.Client | None:
    """Kalit har safar tekshiriladi — .env keyin o'zgarsa ham qayta ishga tushirish shart emas."""
    global _client, _client_key
    key = gemini_key()
    if not key:
        _client, _client_key = None, ""
        return None
    if _client is None or key != _client_key:
        _client, _client_key = genai.Client(api_key=key), key
    return _client


def is_gemini_configured() -> bool:
    return _get_client() is not None


# Vaqtincha "band" (503 UNAVAILABLE / 429) xatolarda darhol taslim bo'lish
# o'rniga, 1-2 marta qisqa kutib qayta urinamiz — ko'pincha ikkinchi
# urinishda muvaffaqiyatli bo'ladi. ai_router.py'dagi umumiy vaqt chegarasi
# ICHIDA qolishi uchun juda qisqa kutamiz.
_RETRY_DELAYS_SECONDS = [1.0, 2.0]


async def _call_gemini_with_retry(**kwargs):
    """generate_content'ni chaqiradi, 503/429 kabi vaqtinchalik xatolarda
    qisqa backoff bilan 1-2 marta qayta urinadi."""
    import asyncio

    last_error = None
    for attempt, delay in enumerate([0.0] + _RETRY_DELAYS_SECONDS):
        if delay:
            await asyncio.sleep(delay)
        try:
            return await _get_client().aio.models.generate_content(**kwargs)
        except genai_errors.APIError as e:
            last_error = e
            is_retryable = getattr(e, "code", None) in (503, 429) or "UNAVAILABLE" in str(e)
            if not is_retryable:
                raise
            logger.info(f"Gemini vaqtincha band (urinish {attempt + 1}) — qayta urinilmoqda...")
    raise last_error


BASE_PERSONA_RULES = (
    "Muhim qoidalar:\n"
    "- JAVOBNI HAR DOIM FAQAT O'ZBEK TILIDA YOZING — savol qaysi tilda "
    "berilgan bo'lishidan (masalan inglizcha so'z yoki gap bo'lsa ham) qat'iy "
    "nazar. Faqat chet tili darsida (masalan ingliz/rus tili fanida) o'sha "
    "tilning o'z misollari, so'zlari yoki gaplari keltirilishi mumkin — lekin "
    "tushuntirishning o'zi baribir o'zbek tilida bo'lishi SHART.\n"
    "- O'zingizni sun'iy intellekt yoki AI deb atamang. Siz — o'qituvchi.\n"
    "- Emoji, yulduzcha (**), ortiqcha undov belgisi ishlatmang.\n"
    "- Sodda so'zlar va qisqa gaplar bilan tushuntiring — o'quvchi boshlang'ich darajada.\n"
    "- Javobni salomlashuv bilan boshlamang, to'g'ridan-to'g'ri savolga javob bering.\n"
)

SUBJECT_PERSONAS = {
    "english": (
        "Siz LongoUZ platformasida ishlaydigan ingliz tili o'qituvchisisiz. "
        "O'zbek tilida tushuntirasiz, oddiy ingliz misollarini ko'rsatasiz."
    ),
    "russian": (
        "Siz LongoUZ platformasida ishlaydigan rus tili o'qituvchisisiz. "
        "O'zbek tilida tushuntirasiz, oddiy ruscha misollarini ko'rsatasiz."
    ),
    "math": "Siz LongoUZ platformasida ishlaydigan matematika o'qituvchisisiz. Sodda tilda tushuntirasiz.",
    "history": "Siz LongoUZ platformasida ishlaydigan tarix o'qituvchisisiz. Sodda tilda tushuntirasiz.",
    "geography": "Siz LongoUZ platformasida ishlaydigan geografiya o'qituvchisisiz. Sodda tilda tushuntirasiz.",
    "native": "Siz LongoUZ platformasida ishlaydigan ona tili o'qituvchisisiz. Sodda tilda tushuntirasiz.",
}

DEFAULT_PERSONA = "Siz LongoUZ platformasida ishlaydigan fan o'qituvchisisiz. O'zbek tilida tushuntirasiz."


# "Fikrlash darajasi" — ai_claude.py'dagi bilan bir xil tamoyil, Gemini
# tarafida ham qo'llaniladi (bu ikkalasi bir xil narsani qilishi kerak,
# chunki foydalanuvchi qaysi provayder javob berayotganini bilmaydi).
EFFORT_MAX_TOKENS = {
    "low": 350,
    "normal": GEMINI_MAX_TOKENS,
    "high": 2200,
    "max": 3200,
}

EFFORT_INSTRUCTIONS = {
    "low": "FIKRLASH DARAJASI: Past. Javobni JUDA QISQA bering — 2-4 gap, ortiqcha misolsiz.",
    "normal": "FIKRLASH DARAJASI: Odatiy. Javobni o'rtacha uzunlikda, tushunarli bering.",
    "high": (
        "FIKRLASH DARAJASI: Yuqori. Javobni BATAFSIL, bosqichma-bosqich "
        "tushuntiring va kamida bitta aniq misol keltiring."
    ),
    "max": (
        "FIKRLASH DARAJASI: Maksimal. Savolni har tomonlama, chuqur tahlil "
        "qiling — bir nechta misol bilan, bosqichma-bosqich yoritib bering."
    ),
}


def _build_system_prompt(subject: str, effort: str = "normal") -> str:
    persona = SUBJECT_PERSONAS.get(subject, DEFAULT_PERSONA)
    effort_note = EFFORT_INSTRUCTIONS.get(effort, EFFORT_INSTRUCTIONS["normal"])
    return persona + "\n\n" + BASE_PERSONA_RULES + "\n\n" + effort_note


_FALLBACK_MODELS = ("gemini-flash-latest", "gemini-2.5-flash")
_MATHY = __import__("re").compile(r"[0-9=+*/^<>%]|masala|hisobla|yech|formula|tenglama|isbot|nechta|necha")


def _thinking_level(question: str, effort: str, history_len: int) -> str:
    """Tezlik va to'g'rilik muvozanati: oddiy suhbat — minimal/low, hisob-kitob va chuqur savol — medium."""
    if effort in ("high", "max"):
        return "medium" if effort == "high" else "high"
    if _MATHY.search(question.lower()) or len(question) > 220:
        return "medium"
    if len(question) < 40 and history_len:
        return "minimal"
    return "low"


def _to_contents(question: str, history: list[dict] | None):
    contents = []
    for h in history or []:
        role = "model" if h["role"] == "assistant" else "user"
        text = wrap_user_content(h["text"]) if role == "user" else h["text"]
        contents.append({"role": role, "parts": [{"text": text}]})
    contents.append({"role": "user", "parts": [{"text": wrap_user_content(question)}]})
    return contents


async def ask_gemini(
    question: str, subject: str, effort: str = "normal", level: str | None = None,
    certificate_type: str | None = None, history: list[dict] | None = None, lang: str | None = None,
) -> str | None:
    """Tez, suhbatni eslab turuvchi javob. None — kalit yo'q yoki xato (router keyingi provayderga o'tadi)."""
    if not is_gemini_configured():
        return None

    from ai_tutor_prompt import build_system_prompt, normalize_history

    hist = normalize_history(history)
    system_prompt = build_system_prompt(subject, level, certificate_type, effort, lang, spoken=True)
    # Gemini 3'da "o'ylash" tokenlari ham max_output_tokens ichiga kiradi — shuning uchun chegara keng.
    max_tokens = {"low": 1500, "normal": 2500, "high": 4000, "max": 6000}.get(effort, 2500)
    level_name = _thinking_level(question, effort, len(hist))
    contents = _to_contents(question, hist)

    def make_config(with_thinking: bool) -> dict:
        cfg = {"system_instruction": system_prompt, "max_output_tokens": max_tokens,
               "automatic_function_calling": _NO_AFC_CONFIG}
        if with_thinking:
            cfg["thinking_config"] = {"thinking_level": level_name}
        return cfg

    attempts = [(GEMINI_MODEL, True), (GEMINI_MODEL, False)]
    for fallback in _FALLBACK_MODELS:
        if fallback != GEMINI_MODEL:
            attempts.append((fallback, False))

    for model, with_thinking in attempts:
        try:
            response = await _call_gemini_with_retry(model=model, contents=contents, config=make_config(with_thinking))
            text = (response.text or "").strip()
            if text:
                ai_diagnostics.clear_error("gemini")
                return text
            logger.warning("Gemini bo'sh javob qaytardi (model=%s, thinking=%s) — keyingi urinish.", model, with_thinking)
        except genai_errors.APIError as e:
            msg = str(e).lower()
            # thinking_level qo'llab-quvvatlanmasa yoki model topilmasa — keyingi variantga o'tamiz
            if getattr(e, "code", None) in (400, 404) or "thinking" in msg or "not_found" in msg:
                logger.info("Gemini %s (thinking=%s) rad etdi: %s — boshqa variant sinab ko'riladi.", model, with_thinking, str(e)[:160])
                ai_diagnostics.record_error("gemini", e)
                continue
            ai_diagnostics.record_error("gemini", e)
            logger.warning("Gemini javob bermadi: %s", e)
            return None
        except Exception as e:
            ai_diagnostics.record_error("gemini", e)
            logger.exception("Kutilmagan Gemini xatosi: %s", e)
            return None
    return None


# ---------------------------------------------------------------------------
# TEST GENERATSIYASI VA BAHOLASH — Claude kredit tugaganda yoki sozlanmaganda
# bepul zaxira sifatida ishlatiladi (Google AI Studio'dagi kalit doimiy
# bepul tarifga ega, karta talab qilinmaydi: https://ai.google.dev).
# ---------------------------------------------------------------------------

def _strip_json_fence(raw_text: str) -> str:
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    return text


def _extract_questions(raw_text: str) -> list[dict]:
    """
    Gemini ba'zan JSON atrofiga qo'shimcha gap qo'shib yuboradi, yoki javob
    token chegarasiga urilib o'rtada kesilib qoladi. Oddiy json.loads bunday
    holatlarda butunlay muvaffaqiyatsiz bo'lib, hammasi (hatto to'liq kelgan
    savollar ham) yo'qolardi. Shu funksiya avval to'g'ridan-to'g'ri parse
    qilishga urinadi, so'ng — muvaffaqiyatsiz bo'lsa — matn ichidan har bir
    to'liq "{...}" savol blokini alohida topib, faqat buzilmagan
    savollarni saqlab qoladi (qisman javob ham foydali bo'lishi mumkin).
    """
    import json
    import re

    text = _strip_json_fence(raw_text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Zaxira: har bir "{...}" blokni alohida ajratib, birma-bir parse qilamiz
    questions = []
    depth = 0
    start = None
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                chunk = text[start:i + 1]
                try:
                    questions.append(json.loads(chunk))
                except json.JSONDecodeError:
                    pass  # kesilib qolgan oxirgi blok — tashlab yuboramiz
                start = None
    return questions


async def generate_quiz(
    subject: str, level: str, topic: str | None = None, count: int = 5,
    certificate_type: str | None = None, mode: str = "dtm",
) -> list[dict] | None:
    if not is_gemini_configured():
        return None

    if not topic:
        topic = "umumiy bilim"

    subject_name = subject
    mode_hint = (
        " Savollar DTM andozasiga mos, standart qiyinlikda bo'lsin."
        if mode != "certificate" else
        " Savollar Sertifikat (CEFR/IELTS) andozasiga mos, qiyinroq bo'lsin."
    )

    prompt = (
        f"{subject_name} fanidan, '{topic}' mavzusida, {level} darajadagi o'quvchi uchun "
        f"{count} ta test savoli tuzing.{mode_hint} Har bir savol uchun 4 ta variant va faqat bitta "
        f"to'g'ri javob bo'lsin. Javobni FAQAT quyidagi JSON formatida qaytaring, "
        f"boshqa hech qanday matn qo'shmang:\n\n"
        f'[{{"question": "savol matni", "options": ["A", "B", "C", "D"], '
        f'"correct_index": 0, "explanation": "qisqa izoh"}}]\n\n'
        f"correct_index - to'g'ri javobning options ro'yxatidagi indeksi (0 dan boshlab)."
    )

    try:
        response = await _call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", GEMINI_MODEL),
            contents=prompt,
            config={
                "system_instruction": "Siz test tuzuvchi o'qituvchisiz. Faqat so'ralgan JSON formatida javob bering.",
                # Har bir savol (savol matni + 4 variant + izoh) taxminan
                # 250-350 token oladi — kesilib qolmasligi uchun kenroq zaxira
                # bilan hisoblaymiz.
                "max_output_tokens": max(2500, count * 380),
                "automatic_function_calling": _NO_AFC_CONFIG,
            },
        )
        raw_text = (response.text or "").strip()
        questions = _extract_questions(raw_text)

        valid_questions = [
            q for q in questions
            if isinstance(q, dict) and "question" in q and "options" in q
            and len(q["options"]) == 4 and "correct_index" in q and 0 <= q["correct_index"] <= 3
        ]
        if valid_questions:
            if len(valid_questions) < count:
                logger.info(
                    f"Gemini {count} tadan faqat {len(valid_questions)} ta yaroqli savol qaytardi "
                    f"(qisman javob yoki kesilish) — mavjudlari ishlatiladi."
                )
            return valid_questions
        return None
    except Exception as e:
        logger.warning(f"Gemini test generatsiyasi ishlamadi — statik bankka o'tiladi: {e}")
        return None


async def evaluate_free_answer(question: str, user_answer: str, subject: str, level: str) -> dict | None:
    if not is_gemini_configured():
        return None

    import json

    prompt = (
        f"{subject} fani, {level} daraja. Savol: {question}\nO'quvchi javobi: {wrap_user_content(user_answer)}\n\n"
        f'Baholang va FAQAT JSON qaytaring: {{"score": 0-100, "is_correct": true/false, "feedback": "qisqa izoh"}}'
    )

    try:
        response = await _call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", GEMINI_MODEL),
            contents=prompt,
            config={
                "system_instruction": "Siz adolatli o'qituvchisiz. Faqat JSON qaytaring.",
                "max_output_tokens": 400,
                "automatic_function_calling": _NO_AFC_CONFIG,
            },
        )
        raw_text = (response.text or "").strip()
        result = json.loads(_strip_json_fence(raw_text))
        if isinstance(result, dict) and "score" in result and "is_correct" in result and "feedback" in result:
            return result
        return None
    except Exception as e:
        logger.warning(f"Gemini baholashi ishlamadi: {e}")
        return None


async def evaluate_speaking(topic_title: str, qa_pairs: list[dict], level: str = "ortacha") -> dict | None:
    if not is_gemini_configured():
        return None
    import json

    transcript = "\n\n".join(
        f"Savol: {qa.get('question', '')}\nJavob: {wrap_user_content(qa.get('answer', ''))}"
        for qa in qa_pairs
    )
    prompt = (
        f"IELTS Speaking mashqi, mavzu: {topic_title}.\n\n{transcript}\n\n"
        "Yuqoridagi ingliz tilidagi javoblarni IELTS Speaking mezonlari asosida baholang. "
        "FAQAT JSON qaytaring: "
        '{"band": "masalan 6.5", "feedback": "o\'zbek tilida qisqa izoh", '
        '"strengths": ["kuchli tomon"], "improvements": ["yaxshilash kerak bo\'lgan narsa"]}'
    )
    try:
        response = await _call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", GEMINI_MODEL),
            contents=prompt,
            config={
                "system_instruction": "Siz IELTS Speaking baholovchisisiz. Faqat JSON qaytaring, o'zbek tilida.",
                "max_output_tokens": 700,
                "automatic_function_calling": _NO_AFC_CONFIG,
            },
        )
        raw_text = (response.text or "").strip()
        result = json.loads(_strip_json_fence(raw_text))
        if isinstance(result, dict) and "band" in result and "feedback" in result:
            return result
        return None
    except Exception as e:
        logger.warning(f"Gemini Speaking baholashi ishlamadi: {e}")
        return None


async def evaluate_writing(topic_title: str, prompt_en: str, essay_text: str) -> dict | None:
    if not is_gemini_configured():
        return None
    import json

    prompt = (
        f"IELTS Writing Task 2 mashqi, mavzu: {topic_title}.\nTopshiriq: {prompt_en}\n\n"
        f"O'quvchi inshosi:\n{wrap_user_content(essay_text)}\n\n"
        "Yuqoridagi inshoni IELTS Writing Task 2 mezonlari asosida baholang. FAQAT JSON qaytaring: "
        '{"band": "masalan 6.0", "feedback": "o\'zbek tilida qisqa izoh", '
        '"strengths": ["kuchli tomon"], "improvements": ["yaxshilash kerak bo\'lgan narsa"]}'
    )
    try:
        response = await _call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", GEMINI_MODEL),
            contents=prompt,
            config={
                "system_instruction": "Siz IELTS Writing baholovchisisiz. Faqat JSON qaytaring, o'zbek tilida.",
                "max_output_tokens": 700,
                "automatic_function_calling": _NO_AFC_CONFIG,
            },
        )
        raw_text = (response.text or "").strip()
        result = json.loads(_strip_json_fence(raw_text))
        if isinstance(result, dict) and "band" in result and "feedback" in result:
            return result
        return None
    except Exception as e:
        logger.warning(f"Gemini Writing baholashi ishlamadi: {e}")
        return None


async def judge_answers(items: list[dict], subject: str) -> dict[int, bool] | None:
    """Ochiq javoblarni hakamlik qilish (Claude zaxirasi). Qoidalar ai_claude.JUDGE_SYSTEM da."""
    if not is_gemini_configured() or not items:
        return None
    import ai_claude
    try:
        response = await _call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", GEMINI_MODEL),
            contents=ai_claude._judge_payload(items, subject),
            config={"system_instruction": ai_claude.JUDGE_SYSTEM, "max_output_tokens": 600,
                    "automatic_function_calling": _NO_AFC_CONFIG},
        )
        return ai_claude.parse_judge_json(response.text or "") or None
    except Exception as e:  # noqa: BLE001
        logger.warning("Gemini hakamligi ishlamadi: %s", e)
        return None
