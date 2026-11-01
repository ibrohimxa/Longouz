"""
LongoUZ — repetitorning javobini OVOZGA aylantiruvchi modul (Text-to-Speech).

Microsoft Edge'ning bepul, onlayn neyron ovoz xizmatidan (edge-tts kutubxonasi
orqali) foydalanadi. MUHIM: bu xizmat HAQIQIY, tabiiy talaffuzli O'ZBEKCHA
neyron ovozga ega ("uz-UZ-SardorNeural" — erkak, "uz-UZ-MadinaNeural" — ayol),
gTTS (Google Translate TTS) esa bunga ega emas edi — shuning uchun avvalgi
"turkcha bilan yaqinlashtirish" yechimi endi kerak emas: ovoz endi HAQIQIY
o'zbekcha, aniq va tiniq talaffuz bilan chiqadi.

Eslatma: bu server INTERNETGA ulanган bo'lishi kerak (Microsoft'ning ochiq
TTS xizmatiga so'rov yuboradi, hech qanday API kalit yoki to'lov shart emas).
Agar server internetga ulanolmasa yoki xizmat vaqtincha javob bermasa,
`synthesize_speech` None qaytaradi va frontend avtomatik ravishda brauzerning
o'z (zaxira, past sifatli) ovoziga o'tadi — sayt hech qachon "soqov" qolib
ketmaydi.
"""

import asyncio
import io
import logging

try:
    import edge_tts
except ImportError:  # kutubxona o'rnatilmagan — brauzer ovoziga o'tiladi
    edge_tts = None

logger = logging.getLogger(__name__)

# Erkak, o'zbekcha neyron ovoz — aniq talab qilingani: "erkak", "tiniq".
TTS_VOICE = "uz-UZ-SardorNeural"

# IELTS Speaking savollari INGLIZ TILIDA o'qilishi kerak (haqiqiy imtihonni
# simulyatsiya qilish uchun) — shu uchun alohida, tabiiy ingliz neyron ovoz.
# O'zbekcha AI fikr-mulohaza (feedback) esa baribir yuqoridagi TTS_VOICE bilan.
TTS_VOICE_EN = "en-US-AndrewNeural"

# (til, jins) -> neyron ovoz. O'zbekcha va ruscha ham haqiqiy mahalliy ovozlar.
VOICES = {
    ("uz", "male"): "uz-UZ-SardorNeural", ("uz", "female"): "uz-UZ-MadinaNeural",
    ("ru", "male"): "ru-RU-DmitryNeural", ("ru", "female"): "ru-RU-SvetlanaNeural",
    ("en", "male"): "en-US-AndrewNeural", ("en", "female"): "en-US-AvaNeural",
}

MAX_TTS_TEXT_LENGTH = 800  # bitta javobni ovozga aylantirish uchun yetarli, ammo cheklangan

# v235: ASOSIY ovoz — Gemini TTS (tabiiy, jonli inson ovozi). Erkak: "Charon" (chuqur, xotirjam —
# "Jarvis"ga o'xshash), ayol: "Sulafat" (iliq, tabiiy). Admin ovozni GEMINI_TTS_VOICE_MALE/FEMALE bilan
# almashtirishi mumkin. Gemini ishlamasa — avvalgidek Microsoft neyron ovozi (edge-tts) zaxira.
GEMINI_TTS_MODELS = ("gemini-3.8-flash-tts", "gemini-3.8-flash-lite-tts", "gemini-2.5-flash-preview-tts")
GEMINI_VOICES = {"male": "Charon", "female": "Sulafat"}
_TTS_STYLE = {
    "uz": "O'zbek tilida, tabiiy, iliq va xotirjam o'qituvchi ovozida, ravon va aniq talaffuz bilan o'qing:",
    "ru": "Прочитай по-русски естественным, тёплым и спокойным голосом учителя:",
    "en": "Read in a natural, warm, calm and clear teacher voice:",
}
_TTS_BAD_MODEL: dict = {}


def _pcm_to_wav(pcm: bytes, rate: int = 24000) -> bytes:
    import struct
    n = len(pcm)
    return (b"RIFF" + struct.pack("<I", 36 + n) + b"WAVEfmt " + struct.pack("<IHHIIHH", 16, 1, 1, rate, rate * 2, 2, 16)
            + b"data" + struct.pack("<I", n) + pcm)


async def synthesize_gemini(text: str, lang: str = "uz", voice_gender: str = "male") -> bytes | None:
    """Gemini TTS: WAV bayt yoki None."""
    import os
    import time
    try:
        import ai_gemini
        import ai_keys
        client = ai_gemini._get_client()
    except Exception:  # noqa: BLE001
        return None
    if client is None:
        return None
    voice = (ai_keys.get("GEMINI_TTS_VOICE_" + voice_gender.upper()) or GEMINI_VOICES.get(voice_gender, "Charon")).strip()
    prompt = f"{_TTS_STYLE.get(lang, _TTS_STYLE['uz'])}\n{text}"
    models = [m for m in ((os.getenv("GEMINI_TTS_MODEL") or "").strip(),) + GEMINI_TTS_MODELS if m]
    for model in dict.fromkeys(models):
        if _TTS_BAD_MODEL.get(model, 0) > time.time():
            continue
        try:
            resp = await asyncio.wait_for(client.aio.models.generate_content(
                model=model, contents=prompt,
                config={"response_modalities": ["AUDIO"],
                        "speech_config": {"voice_config": {"prebuilt_voice_config": {"voice_name": voice}}}}), timeout=20)
            for part in (resp.candidates[0].content.parts if resp.candidates else []):
                inline = getattr(part, "inline_data", None)
                if inline and inline.data:
                    data = inline.data
                    mime = (inline.mime_type or "").lower()
                    if "wav" in mime or data[:4] == b"RIFF":
                        return data
                    rate = 24000
                    if "rate=" in mime:
                        try:
                            rate = int(mime.split("rate=")[1].split(";")[0])
                        except ValueError:
                            pass
                    return _pcm_to_wav(data, rate)
        except Exception as e:  # noqa: BLE001
            msg = str(e).lower()
            logger.warning("Gemini TTS (%s) ishlamadi: %s", model, str(e)[:200])
            if "not_found" in msg or "404" in msg or "not supported" in msg:
                _TTS_BAD_MODEL[model] = time.time() + 3600
            elif "429" in msg or "resource_exhausted" in msg:
                _TTS_BAD_MODEL[model] = time.time() + 300
    return None


async def synthesize_any(text: str, lang: str = "uz", voice_gender: str = "male", rate: str = "+0%") -> tuple[bytes, str] | None:
    """Avval Gemini (tabiiy ovoz), bo'lmasa Microsoft neyron ovozi. (bayt, mime) yoki None."""
    if not text or not text.strip():
        return None
    clean = text.strip()[:MAX_TTS_TEXT_LENGTH]
    wav = await synthesize_gemini(clean, lang, voice_gender)
    if wav:
        return wav, "audio/wav"
    mp3 = await synthesize_speech(clean, lang, voice_gender, rate)
    return (mp3, "audio/mpeg") if mp3 else None


async def synthesize_speech(text: str, lang: str = "uz", voice_gender: str = "male", rate: str = "+0%") -> bytes | None:
    """
    Berilgan matnni MP3 bayt sifatida qaytaradi. Internet aloqasi yo'q yoki
    Microsoft'ning TTS xizmati vaqtincha ishlamasa — None qaytaradi (chaqiruvchi
    tomon bunda brauzerning o'z (zaxira) ovoziga o'tishi kerak).
    lang="en" — IELTS Speaking savollari uchun tabiiy ingliz ovozi.
    """
    if not text or not text.strip() or edge_tts is None:
        return None

    clean_text = text.strip()[:MAX_TTS_TEXT_LENGTH]
    voice = VOICES.get((lang, voice_gender), TTS_VOICE)

    # MUHIM: edge-tts vaqti-vaqti bilan (tarmoq/xizmat tomonidan) bitta
    # so'rovni rad etishi mumkin — bunday holatda darhol brauzer zaxirasiga
    # (past sifatli, ba'zan "turkcha aralash" eshitiladigan ovozga) o'tib
    # ketishdan oldin, BIR MARTA qayta urinib ko'ramiz. Bu haqiqiy, sifatli
    # o'zbekcha ovozning ko'proq hollarda ishlatilishini ta'minlaydi.
    last_error: Exception | None = None
    for attempt in range(2):
        try:
            communicate = edge_tts.Communicate(clean_text, voice=voice, rate=rate)
            buf = io.BytesIO()
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    buf.write(chunk["data"])
            audio_bytes = buf.getvalue()
            if audio_bytes:
                return audio_bytes
        except Exception as e:
            last_error = e
            if attempt == 0:
                await asyncio.sleep(0.6)

    logger.warning(
        f"TTS generatsiya qilinmadi (edge-tts xizmati muammosi, 2 urinishdan keyin ham) — "
        f"server internetdan Microsoft TTS xizmatiga (Azure Speech) chiqa olmayotgan bo'lishi "
        f"ham mumkin: {last_error}"
    )
    return None
