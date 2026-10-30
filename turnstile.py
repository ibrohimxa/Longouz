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


def mode() -> str:
    """TURNSTILE_MODE: 'off' — admin paneldan butunlay o'chirilgan; boshqa qiymat (yoki bo'sh) — kalit bo'lsa yoqiladi."""
    return (ai_keys.get("TURNSTILE_MODE") or "auto").strip().lower()


def is_enabled() -> bool:
    return mode() != "off" and bool(site_key() and secret_key())


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
# Kalit/sozlamadagi xato (foydalanuvchi aybi emas) — bunda foydalanuvchini bloklamaymiz
_CONFIG_ERRORS = {"missing-input-secret", "invalid-input-secret", "bad-request", "internal-error"}


async def verify_detail(token: str, remote_ip: str = "", secret: str | None = None) -> tuple[bool, list[str], str]:
    """Qaytadi: (muvaffaqiyat, xato kodlari, holat). holat: ok | rejected | network."""
    payload = {"secret": secret if secret is not None else secret_key(), "response": token or ""}
    if remote_ip:
        payload["remoteip"] = remote_ip
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(_VERIFY_URL, data=payload, timeout=aiohttp.ClientTimeout(total=8)) as resp:
                data = await resp.json(content_type=None)
    except Exception as e:  # noqa: BLE001
        logger.warning("Turnstile tekshiruvi ishlamadi (tarmoq): %s", e)
        return False, [], "network"
    codes = [str(c) for c in (data.get("error-codes") or [])]
    if data.get("success"):
        return True, codes, "ok"
    logger.warning("Turnstile rad etdi: %s", codes)
    return False, codes, "rejected"


async def verify_turnstile(token: str, remote_ip: str = "") -> bool:
    """Eski interfeys: True = o'tkazish mumkin."""
    if not is_enabled():
        return True
    if not token:
        return False
    ok, codes, state = await verify_detail(token, remote_ip)
    if ok:
        return True
    if state == "network":
        return True          # Cloudflare vaqtincha ishlamasa foydalanuvchini bloklamaymiz
    if set(codes) & _CONFIG_ERRORS:
        logger.error("Turnstile SECRET KEY noto'g'ri sozlangan (%s) — tekshiruv o'tkazib yuborildi. Admin → Kalitlar.", codes)
        return True
    return False


# --- Zaxira yo'l: vidjet brauzerda yuklanmasa (reklama-bloker, tarmoq, domen sozlamasi) foydalanuvchi qulflanib qolmasin.
#     Bunda tekshiruv o'rniga IP bo'yicha qattiq cheklov qo'llanadi (10 daqiqada 4 ta urinish).
_FALLBACK_HITS: dict[str, list[float]] = {}


def fallback_allowed() -> bool:
    return (ai_keys.get("TURNSTILE_FALLBACK") or "on").strip().lower() != "off"


def _fallback_rate_ok(ip: str, limit: int = 4, window: int = 600) -> bool:
    import time
    now = time.time()
    hits = [t for t in _FALLBACK_HITS.get(ip, []) if now - t < window]
    if len(hits) >= limit:
        _FALLBACK_HITS[ip] = hits
        return False
    hits.append(now)
    _FALLBACK_HITS[ip] = hits
    if len(_FALLBACK_HITS) > 5000:
        _FALLBACK_HITS.clear()
    return True


async def check(request, token: str, fallback_flag: str = "") -> bool:
    """Formalar uchun yagona tekshiruv. True — davom etish mumkin."""
    if not is_active_for_request(request):
        return True
    ip = client_ip(request)
    if token:
        return await verify_turnstile(token, ip)
    if fallback_flag and fallback_allowed():
        ok = _fallback_rate_ok(ip or "?")
        if not ok:
            logger.warning("Turnstile zaxira yo'li: IP %s uchun urinishlar chegarasi oshdi.", ip)
        return ok
    return False
