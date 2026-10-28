"""
LongoUZ — Cloudflare Turnstile (bot-himoya vidjeti) tekshiruvi.

SOZLASH: dash.cloudflare.com/?to=/:account/turnstile sahifasida yangi
"Widget" yarating (domenni ko'rsating, masalan 127.0.0.1 lokal test uchun
yoki haqiqiy domeningiz). Sizga ikkita kalit beriladi:
  - Site Key  (ochiq, frontend'da ko'rinadi) -> TURNSTILE_SITE_KEY
  - Secret Key (maxfiy, faqat serverda)      -> TURNSTILE_SECRET_KEY
Ikkalasini ham .env fayliga qo'ying. Bo'sh qoldirsangiz, vidjet saytda
ko'rinmaydi va ro'yxatdan o'tish/kirish oddiy (tekshiruvsiz) ishlayveradi —
sayt buzilmaydi, faqat bot-himoya bo'lmaydi.
"""

import os
import logging
import ipaddress

import aiohttp

logger = logging.getLogger(__name__)

import ai_keys


def site_key() -> str:
    return ai_keys.get("TURNSTILE_SITE_KEY")


def secret_key() -> str:
    return ai_keys.get("TURNSTILE_SECRET_KEY")


def is_enabled() -> bool:
    return bool(site_key() and secret_key())


def __getattr__(name):  # eski kod uchun
    if name == "TURNSTILE_SITE_KEY":
        return site_key()
    if name == "TURNSTILE_SECRET_KEY":
        return secret_key()
    if name == "TURNSTILE_ENABLED":
        return is_enabled()
    raise AttributeError(name)

# Cloudflare Turnstile kaliti faqat ro'yxatdan o'tgan DOMENLARDA ishlaydi.
# Lokal tarmoq (localhost, 127.0.0.1, 192.168.x.x, 10.x.x.x) manzillarida
# vidjet "domen ruxsat etilmagan" xatosi beradi va ro'yxatdan o'tishni
# butunlay to'sib qo'yadi. Shu sababli bunday manzillarda Turnstile
# avtomatik o'chiriladi (haqiqiy domenda — yoqiladi). Majburan yoqish:
# .env da TURNSTILE_ENFORCE_LOCAL=true.
TURNSTILE_ENFORCE_LOCAL = os.getenv("TURNSTILE_ENFORCE_LOCAL", "false").strip().lower() == "true"


def _is_local_host(host_header: str) -> bool:
    host = (host_header or "").split(",")[0].strip().lower()
    if host.startswith("["):
        host = host[1:host.find("]")]
    elif host.count(":") == 1:
        host = host.rsplit(":", 1)[0]
    if host in ("", "localhost") or host.endswith((".local", ".lan", ".internal")):
        return True
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False
    return ip.is_private or ip.is_loopback or ip.is_link_local


def is_active_for_request(request) -> bool:
    if not is_enabled():
        return False
    if TURNSTILE_ENFORCE_LOCAL:
        return True
    return not _is_local_host(request.headers.get("x-forwarded-host") or request.headers.get("host", ""))


def client_ip(request) -> str:
    forwarded = request.headers.get("cf-connecting-ip") or request.headers.get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else ""


_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


# Cloudflare javobidagi SOZLAMA xatolari (kalit noto'g'ri/yo'q) — bunda foydalanuvchi aybdor emas,
# shuning uchun uni bloklamaymiz (admin panelda ogohlantirish chiqadi). Faqat haqiqiy "robot"
# yoki eskirgan/ishlatilgan token rad etiladi.
_CONFIG_ERRORS = {"missing-input-secret", "invalid-input-secret", "bad-request", "internal-error"}
LAST_ERROR: dict = {"codes": [], "at": 0.0}


async def verify_turnstile(token: str, remote_ip: str = "", widget_unavailable: bool = False) -> bool:
    """True = o'tkazish. widget_unavailable=True: brauzerda vidjet umuman yuklanmadi/xato berdi
    (Cloudflare bloklangan, domen ruxsatsiz, tarmoq) — foydalanuvchi bloklab qo'yilmaydi,
    lekin so'rov rate-limit (10/daq) ostida qoladi."""
    import time as _t
    if not is_enabled():
        return True
    if not token:
        if widget_unavailable:
            logger.warning("Turnstile vidjeti brauzerda ishlamadi — foydalanuvchi o'tkazildi (rate-limit ostida).")
            LAST_ERROR.update(codes=["widget-unavailable"], at=_t.time())
            return True
        return False

    payload = {"secret": secret_key(), "response": token}
    if remote_ip:
        payload["remoteip"] = remote_ip

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(_VERIFY_URL, data=payload, timeout=aiohttp.ClientTimeout(total=8)) as resp:
                data = await resp.json()
                if data.get("success"):
                    return True
                codes = data.get("error-codes") or []
                logger.warning(f"Turnstile rad etdi: {codes}")
                LAST_ERROR.update(codes=codes, at=_t.time())
                return bool(set(codes) & _CONFIG_ERRORS)
    except Exception as e:
        logger.warning(f"Turnstile tekshiruvi ishlamadi (tarmoq muammosi bo'lishi mumkin): {e}")
        return True
