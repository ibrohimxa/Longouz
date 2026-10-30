"""
LongoUZ — Google orqali ro'yxatdan o'tish/kirish (OAuth 2.0, Authorization
Code Flow). Hech qanday qo'shimcha og'ir kutubxona (masalan authlib) talab
qilinmaydi — protokolning o'zi standart bo'lgani uchun to'g'ridan-to'g'ri
aiohttp orqali amalga oshirilgan, shunda nima sodir bo'layotgani har bir
qadamda aniq ko'rinadi.

SOZLASH: Google Cloud Console'da (console.cloud.google.com/apis/credentials)
"OAuth 2.0 Client ID" (Web application turi) yarating:
  - Authorized redirect URI: <SITE_BASE_URL>/auth/google/callback
    (masalan http://127.0.0.1:8000/auth/google/callback lokal test uchun,
    productionda https://sizning-domeningiz.uz/auth/google/callback)
Olingan Client ID va Client Secret'ni .env fayldagi GOOGLE_CLIENT_ID va
GOOGLE_CLIENT_SECRET'ga qo'ying. Bular bo'sh bo'lsa, "Google bilan kirish"
tugmasi saytda UMUMAN ko'rinmaydi (xato bermaydi, shunchaki yashirin turadi).
"""

import os
import hmac
import time
import hashlib
import secrets
import logging
import ipaddress
from urllib.parse import urlencode, urlparse

import aiohttp

logger = logging.getLogger(__name__)

import ai_keys
import runtime


def client_id() -> str:
    return ai_keys.get("GOOGLE_CLIENT_ID")


def client_secret() -> str:
    return ai_keys.get("GOOGLE_CLIENT_SECRET")


def is_enabled() -> bool:
    """Kalitlar HAR chaqiruvda o'qiladi (admin paneldan o'zgarsa darhol kuchga kiradi)."""
    return bool(client_id() and client_secret())


def __getattr__(name):  # eski kod uchun: oauth_google.GOOGLE_ENABLED va h.k.
    if name == "GOOGLE_ENABLED":
        return is_enabled()
    if name == "GOOGLE_CLIENT_ID":
        return client_id()
    if name == "GOOGLE_CLIENT_SECRET":
        return client_secret()
    if name == "SITE_BASE_URL":
        return runtime.site_base_url()
    raise AttributeError(name)

_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
_TOKEN_URL = "https://oauth2.googleapis.com/token"
_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

STATE_COOKIE_NAME = "longouz_oauth_state"


def _host_only(host: str) -> str:
    host = (host or "").strip().lower()
    if host.startswith("["):
        return host[1:host.find("]")]
    return host.rsplit(":", 1)[0] if host.count(":") == 1 else host


def _is_private_host(host: str) -> bool:
    h = _host_only(host)
    try:
        ip = ipaddress.ip_address(h)
        return ip.is_private and not ip.is_loopback
    except ValueError:
        return h.endswith((".local", ".lan", ".internal"))


def base_url_for(request) -> str:
    """Brauzer ochgan manzil (localhost / 127.0.0.1 / haqiqiy domen / HTTPS) bo'yicha
    redirect bazasi. Google LAN IP (192.168.x.x) ni qabul qilmaydi — bunda
    .env dagi SITE_BASE_URL ishlatiladi."""
    configured = runtime.site_base_url().rstrip("/")
    if request is None:
        return configured
    host = (request.headers.get("x-forwarded-host") or request.headers.get("host", "")).split(",")[0].strip()
    if not host:
        return configured
    if _is_private_host(host):
        # Google LAN IP (192.168.x.x) ni redirect sifatida QABUL QILMAYDI. Sozlangan manzil ham lokal IP bo'lsa,
        # eng ishonchli variant — localhost (Google uni ruxsat beradi, brauzer shu kompyuterda ochilgan bo'lishi kerak).
        if _is_private_host(configured.split("://", 1)[-1].split("/")[0]):
            port = host.rsplit(":", 1)[1] if host.count(":") == 1 else ""
            return f"http://localhost{(':' + port) if port else ''}"
        return configured
    scheme = request.headers.get("x-forwarded-proto") or request.url.scheme
    return f"{scheme.split(',')[0].strip()}://{host.split(',')[0].strip()}"


def redirect_uri_for(request) -> str:
    return f"{base_url_for(request)}/auth/google/callback"


def _sign(payload: str, secret: str) -> str:
    return hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()[:32]


def make_state(secret: str) -> str:
    """Imzolangan, cookie'siz state: hostlar (localhost <-> 127.0.0.1) almashsa ham ishlaydi."""
    nonce = secrets.token_urlsafe(12)
    ts = str(int(time.time()))
    body = f"{nonce}.{ts}"
    return f"{body}.{_sign(body, secret)}"


def verify_state(state: str, secret: str, max_age: int = 900) -> bool:
    try:
        nonce, ts, sig = (state or "").split(".")
        if not hmac.compare_digest(sig, _sign(f"{nonce}.{ts}", secret)):
            return False
        return 0 <= time.time() - int(ts) <= max_age
    except (ValueError, TypeError):
        return False


def build_authorize_url(redirect_uri: str, state: str) -> str:
    params = {
        "client_id": client_id(),
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "prompt": "select_account",
    }
    return f"{_AUTH_URL}?{urlencode(params)}"


async def exchange_code_for_userinfo(code: str, redirect_uri: str) -> tuple[dict | None, str]:
    """(userinfo, xato_kodi). Xato bo'lsa userinfo=None va kod sababni bildiradi:
    redirect_uri_mismatch / invalid_client / invalid_grant / network / email_unverified."""
    token_payload = {
        "code": code,
        "client_id": client_id(),
        "client_secret": client_secret(),
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(_TOKEN_URL, data=token_payload, timeout=aiohttp.ClientTimeout(total=12)) as resp:
                if resp.status != 200:
                    body = await resp.text()
                    logger.warning(f"Google token almashinuvi muvaffaqiyatsiz: {resp.status} {body} (redirect_uri={redirect_uri})")
                    if "redirect_uri_mismatch" in body:
                        return None, "redirect_uri_mismatch"
                    if "invalid_client" in body:
                        return None, "invalid_client"
                    return None, "invalid_grant"
                token_data = await resp.json()

            access_token = token_data.get("access_token")
            if not access_token:
                return None, "invalid_grant"

            headers = {"Authorization": f"Bearer {access_token}"}
            async with session.get(_USERINFO_URL, headers=headers, timeout=aiohttp.ClientTimeout(total=12)) as resp:
                if resp.status != 200:
                    return None, "network"
                userinfo = await resp.json()

        email = userinfo.get("email")
        if not email:
            return None, "no_email"
        if userinfo.get("email_verified") is False:
            return None, "email_unverified"

        return {
            "email": email.strip().lower(),
            "name": userinfo.get("name") or userinfo.get("given_name") or "",
        }, ""
    except Exception as e:
        logger.warning(f"Google OAuth xatosi: {e}")
        return None, "network"
