"""
LongoUZ websayt uchun autentifikatsiya moduli.
- Parolni bcrypt bilan hash qilish/tekshirish
- JWT token yaratish/tekshirish (cookie orqali saqlanadi)

XAVFSIZLIK — MUHIM:
Ilgari SECRET_KEY uchun kodning ICHIDA yozilgan ("vaqtinchalik-maxfiy-kalit-
ALMASHTIRING" kabi) ochiq matnli standart qiymat bor edi. Bu — jiddiy zaif
tomon: kim bu kodni ko'rsa (masalan GitHub'da ochiq repo bo'lsa), xuddi shu
maxfiy kalit bilan ISTALGAN foydalanuvchi nomidan haqiqiy JWT token yasab,
uning hisobiga kirib olishi mumkin edi. Endi:
  - Agar WEB_SECRET_KEY muhit o'zgaruvchisi berilgan bo'lsa — shu ishlatiladi
    (productionda, ayniqsa bir nechta server/worker ishlatilganda, ALBATTA
    shunday qiling — pastdagi fayl-asosidagi zaxira faqat BITTA mashinada
    ishlaydi).
  - Berilmagan bo'lsa — ILGARI har safar TASODIFIY yangi kalit yaratilardi,
    bu esa "--reload" bilan ishlaganda (yoki har safar serverni qayta
    ishga tushirganda) BARCHA foydalanuvchilarni, jumladan SIZNI, tizimdan
    chiqarib yuborardi — aynan shuning uchun "kirganimni eslab qolmayapti"
    muammosi paydo bo'lgan bo'lishi katta ehtimol. Endi bunday holatda kalit
    FAYLGA saqlanadi (.web_secret_key.local) va keyingi ishga tushirishlarda
    O'SHA saqlangan kalit qayta ishlatiladi — shu mashinada sessiyalar endi
    qayta ishga tushirishlar orasida saqlanib qoladi, hatto .env sozlanmagan
    bo'lsa ham.
"""

import os
import secrets
import logging
from pathlib import Path
from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt, JWTError

logger = logging.getLogger(__name__)

_LOCAL_SECRET_FILE = Path(__file__).parent / ".web_secret_key.local"


def _load_or_create_local_secret() -> str:
    """
    .env orqali WEB_SECRET_KEY berilmagan hollarda ishlatiladigan ZAXIRA
    mexanizm — kalitni FAYLGA yozib, keyingi ishga tushirishlarda o'sha
    faylni o'qiydi (shu bilan qayta ishga tushirish/--reload sessiyalarni
    bekor qilmaydi). Bu faqat BITTA server/mashina uchun mo'ljallangan
    qulaylik — bir nechta worker/server ishlatadigan haqiqiy productionda
    baribir WEB_SECRET_KEY muhit o'zgaruvchisini o'zingiz belgilashingiz
    kerak (barcha workerlar BITTA kalitni bilishi shart).
    """
    try:
        if _LOCAL_SECRET_FILE.exists():
            existing = _LOCAL_SECRET_FILE.read_text(encoding="utf-8").strip()
            if existing:
                return existing
    except OSError:
        pass

    new_key = secrets.token_hex(32)
    try:
        _LOCAL_SECRET_FILE.write_text(new_key, encoding="utf-8")
    except OSError:
        # Faylga yoza olmasak (masalan ruxsat yo'q) — baribir ishlashda
        # davom etamiz, faqat bu safar chindan ham vaqtinchalik bo'ladi.
        logger.warning(f"{_LOCAL_SECRET_FILE} fayliga yoza olmadik — kalit faqat shu jarayon uchun vaqtinchalik.")
    return new_key


_env_secret = os.getenv("WEB_SECRET_KEY", "")
if _env_secret:
    SECRET_KEY = _env_secret
elif os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    # Serverless: fayl yozib bo'lmaydi va har instans alohida — barqaror kalit DATABASE_URL/ADMIN_PASSWORD'dan hosil qilinadi
    import runtime as _rt
    SECRET_KEY = _rt.stable_secret_seed()
    logger.warning("WEB_SECRET_KEY berilmagan — barqaror zaxira kalit ishlatilmoqda. Vercel'da WEB_SECRET_KEY'ni qo'shing.")
else:
    SECRET_KEY = _load_or_create_local_secret()
    logger.warning(
        "WEB_SECRET_KEY muhit o'zgaruvchisi berilmagan — .web_secret_key.local "
        "fayldagi (yoki yangi yaratilgan) kalit ishlatilmoqda. Bu shu mashinada "
        "qayta ishga tushirishlar orasida sessiyalarni saqlab turadi, lekin "
        "productionda (ayniqsa bir nechta serverda) baribir WEB_SECRET_KEY'ni "
        "o'zingiz .env orqali belgilang: "
        "python -c \"import secrets; print(secrets.token_hex(32))\""
    )

ALGORITHM = "HS256"
TOKEN_EXPIRE_DAYS = 30

COOKIE_NAME = "longouz_session"

# Cookie'ning "secure" bayrog'i — faqat HTTPS orqali yuborilishini
# ta'minlaydi. Productionda (https bilan) albatta yoqilishi kerak, lekin
# lokal http://127.0.0.1 orqali test qilishda yoqilgan bo'lsa, brauzer
# cookie'ni umuman yubormaydi va tizimga kirish ishlamay qoladi — shuning
# uchun standart holatda o'chirilgan, productionda quyidagicha yoqiladi:
#   $env:WEB_COOKIE_SECURE="true"
COOKIE_SECURE = (os.getenv("WEB_COOKIE_SECURE", "false").strip().lower() == "true"
                 or bool(os.getenv("VERCEL")))  # Vercel doim HTTPS
COOKIE_SAMESITE = "lax"


def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), password_hash.encode("utf-8"))
    except (ValueError, TypeError):
        return False


def create_access_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=TOKEN_EXPIRE_DAYS)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> int | None:
    """Token to'g'ri bo'lsa user_id qaytaradi, aks holda None."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        return int(user_id) if user_id is not None else None
    except (JWTError, ValueError, TypeError):
        return None


def set_session_cookie(response, token: str):
    """Sessiya cookie'sini xavfsiz sozlamalar bilan o'rnatadi — barcha
    joyda BIR XIL bayroqlar ishlatilishini kafolatlaydi."""
    response.set_cookie(
        COOKIE_NAME, token,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite=COOKIE_SAMESITE,
        max_age=60 * 60 * 24 * TOKEN_EXPIRE_DAYS,
    )
