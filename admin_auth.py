"""
LongoUZ — Admin panel autentifikatsiyasi. Oddiy foydalanuvchi autentifikatsiyasi
(auth.py)dan BUTUNLAY ALOHIDA — boshqa cookie nomi, boshqa token tuzilmasi.
Admin bo'lish O'ZI bilan sayt foydalanuvchisi bo'lishni anglatmaydi va aksincha.

MARKAZLASHTIRILGAN PAROL (siz so'raganidek — "bitta joy bo'lsin, shuni
o'zgartirsam hammasi o'zgarsin"):
  Admin paroli FAQAT bitta joydan — ADMIN_PASSWORD muhit o'zgaruvchisidan
  (.env fayl) o'qiladi. Kodning boshqa HECH BIR joyida parol yozilmagan yoki
  takrorlanmagan. Parolni o'zgartirish uchun FAQAT .env fayldagi
  ADMIN_PASSWORD qatorini o'zgartiring va serverni qayta ishga tushiring —
  butun tizimda (login tekshiruvi ham) avtomatik yangi parol ishlaydi.

XAVFSIZLIK HAQIDA HALOL ESLATMA: parol .env faylda ochiq matn sifatida
saqlanadi (hash emas) — bu bitta-admin, kichik loyiha uchun oddiy va real
yechim, lekin bu degani: .env faylni HECH KIMGA ko'rsatmang va GitHub'ga
yuklamang (.gitignore'da allaqachon istisno qilingan). Solishtirish
`secrets.compare_digest` orqali VAQT HUJUMLARIGA (timing attack) qarshi
xavfsiz tarzda amalga oshiriladi.
"""

import os
import secrets
import logging
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError

import auth as user_auth  # SECRET_KEY va ALGORITHM'ni QAYTA ISHLATAMIZ (bitta manba)

logger = logging.getLogger(__name__)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "NEO")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")  # kodda standart parol YO'Q — faqat .env / Vercel Environment Variables

if not ADMIN_PASSWORD:
    logger.warning(
        "ADMIN_PASSWORD muhit o'zgaruvchisi berilmagan — admin panelga HECH KIM "
        "kira olmaydi (bu ataylab shunday: standart/taxmin qilinadigan parol "
        "bilan admin panel ochiq qolishi xavfli). .env fayldagi ADMIN_PASSWORD "
        "qatorini to'ldiring."
    )

if ADMIN_PASSWORD in ("xamroyevi10", "xamroyevi", "xamroyevi6"):
    raise RuntimeError(
        "XAVFSIZLIK TO'XTATUVI: ADMIN_PASSWORD hali ham ilgari oshkor bo'lgan "
        "qiymatlardan biri (\"xamroyevi10\" yoki \"xamroyevi6\") da turibdi — bu "
        "qiymatlar kod nusxalarida ochiq matn sifatida ko'rilgan. .env faylda "
        "ADMIN_PASSWORD ni YANGI, boshqa hech qayerda ishlatilmagan, hech kimga "
        "aytilmagan/ko'rsatilmagan parolga o'zgartiring. ESLATMA: parolni HECH "
        "QACHON shu faylga (admin_auth.py) yoki boshqa .py fayliga yozib "
        "qo'ymang — FAQAT .env fayliga, va .env faylni hech kimga (shu jumladan "
        "AI yordamchiga ham) yuklamang/ko'rsatmang."
    )

ADMIN_COOKIE_NAME = "longouz_admin_session"
ADMIN_TOKEN_EXPIRE_HOURS = 12  # foydalanuvchi sessiyasidan (30 kun) ANCHA qisqa — admin huquqi xavfliroq

# --- Admin panelga kiradigan manzil (URL) ---
# "/admin" so'zi taxmin qilish oson (har qanday bot/hujumchi birinchi shuni
# sinaydi), shuning uchun standart bo'yicha boshqa, kamroq ko'zga
# tashlanadigan yo'l ishlatiladi. Buni istalgan boshqa so'zga (masalan
# "/boshqaruv-7x9") .env fayldagi ADMIN_URL_PREFIX orqali o'zgartirishingiz
# mumkin — kodga qaytib kirish shart emas. Qiymat "/" bilan boshlanishi va
# oxirida "/" bo'lmasligi kerak.
ADMIN_URL_PREFIX = os.getenv("ADMIN_URL_PREFIX", "/neo").strip()
if not ADMIN_URL_PREFIX.startswith("/"):
    ADMIN_URL_PREFIX = "/" + ADMIN_URL_PREFIX
ADMIN_URL_PREFIX = ADMIN_URL_PREFIX.rstrip("/") or "/neo"


def verify_admin_credentials(username: str, password: str) -> bool:
    """Vaqt hujumlariga chidamli solishtirish — parol noto'g'ri bo'lganda
    ham javob VAQTI bir xil bo'lishi kerak, aks holda parolni harf-harflab
    "sinab ko'rish" mumkin bo'lib qoladi."""
    if not ADMIN_PASSWORD:
        return False
    username_ok = secrets.compare_digest(username.strip(), ADMIN_USERNAME)
    password_ok = secrets.compare_digest(password, ADMIN_PASSWORD)
    return username_ok and password_ok


def create_admin_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=ADMIN_TOKEN_EXPIRE_HOURS)
    payload = {"admin": True, "username": username, "exp": expire}
    return jwt.encode(payload, user_auth.SECRET_KEY, algorithm=user_auth.ALGORITHM)


def verify_admin_token(token: str) -> bool:
    """Token haqiqiy va muddati o'tmagan bo'lsa va aniq admin={"admin": True}
    da'vosiga ega bo'lsagina True qaytaradi — oddiy foydalanuvchi token
    (sub={user_id}) bu yerdan HECH QACHON o'tolmaydi, chunki unda "admin"
    da'vosi yo'q."""
    try:
        payload = jwt.decode(token, user_auth.SECRET_KEY, algorithms=[user_auth.ALGORITHM])
    except JWTError:
        return False
    return payload.get("admin") is True


def get_admin_username(token: str) -> str:
    """Admin jurnaliga yozish uchun — token ichidagi username'ni qaytaradi
    (admin_log.py yozuvlarida "kim qildi" ko'rsatish uchun)."""
    try:
        payload = jwt.decode(token, user_auth.SECRET_KEY, algorithms=[user_auth.ALGORITHM])
        return payload.get("username", "admin")
    except JWTError:
        return "admin"
