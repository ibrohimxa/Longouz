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

ADMIN_USERNAME = (os.getenv("ADMIN_USERNAME") or "neo").strip()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")  # v221: koddagi standart parol olib tashlandi (repo ochiq)

if not ADMIN_PASSWORD:
    logger.warning(
        "ADMIN_PASSWORD muhit o'zgaruvchisi berilmagan — admin panelga HECH KIM "
        "kira olmaydi (bu ataylab shunday: standart/taxmin qilinadigan parol "
        "bilan admin panel ochiq qolishi xavfli). .env fayldagi ADMIN_PASSWORD "
        "qatorini to'ldiring."
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
# v250: standart yo'l KODDA YOZILMAGAN — repo ochiq bo'lgani uchun. Aniq manzil Vercel/.env dagi
# ADMIN_URL_PREFIX da turadi; u yo'q bo'lsa, maxfiy kalitdan hosil bo'ladigan taxmin qilib bo'lmaydigan yo'l olinadi.
def _default_prefix() -> str:
    import hashlib
    return "/ctl-" + hashlib.sha256(("lz-admin-path|" + str(user_auth.SECRET_KEY)).encode()).hexdigest()[:10]


ADMIN_URL_PREFIX = (os.getenv("ADMIN_URL_PREFIX") or "").strip() or _default_prefix()
if not ADMIN_URL_PREFIX.startswith("/"):
    ADMIN_URL_PREFIX = "/" + ADMIN_URL_PREFIX
ADMIN_URL_PREFIX = ADMIN_URL_PREFIX.rstrip("/") or _default_prefix()


import hashlib as _hashlib


def admin_password_problem() -> str:
    """Admin paroli o'rnatilmagan bo'lsa — sababi (bo'sh satr = hammasi joyida)."""
    return "" if ADMIN_PASSWORD else "ADMIN_PASSWORD o'rnatilmagan."


def _password_fingerprint() -> str:
    """Parol o'zgarsa — eski admin sessiyalari avtomatik bekor bo'ladi."""
    return _hashlib.sha256(("lz-admin|" + (ADMIN_PASSWORD or "")).encode()).hexdigest()[:16]


def verify_admin_credentials(username: str, password: str) -> bool:
    """Vaqt hujumlariga chidamli solishtirish — parol noto'g'ri bo'lganda
    ham javob VAQTI bir xil bo'lishi kerak, aks holda parolni harf-harflab
    "sinab ko'rish" mumkin bo'lib qoladi."""
    if not ADMIN_PASSWORD or admin_password_problem():
        return False
    username_ok = secrets.compare_digest(username.strip().lower(), ADMIN_USERNAME.lower())  # katta-kichik harf farqsiz
    password_ok = secrets.compare_digest(password, ADMIN_PASSWORD)
    return username_ok and password_ok


def create_admin_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(hours=ADMIN_TOKEN_EXPIRE_HOURS)
    payload = {"admin": True, "username": username, "exp": expire, "pv": _password_fingerprint()}
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
    if admin_password_problem():
        return False
    return payload.get("admin") is True and secrets.compare_digest(str(payload.get("pv", "")), _password_fingerprint())


def get_admin_username(token: str) -> str:
    """Admin jurnaliga yozish uchun — token ichidagi username'ni qaytaradi
    (admin_log.py yozuvlarida "kim qildi" ko'rsatish uchun)."""
    try:
        payload = jwt.decode(token, user_auth.SECRET_KEY, algorithms=[user_auth.ALGORITHM])
        return payload.get("username", "admin")
    except JWTError:
        return "admin"
