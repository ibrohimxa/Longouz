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
