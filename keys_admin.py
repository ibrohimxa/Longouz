"""LongoUZ — ADMIN: KALITLAR (Claude, Gemini, Cloudflare Turnstile, Google).

Maqsad: kalitlarni kod ichiga yoki GitHub'ga YOZMASDAN, admin paneldan kiritish.
  * kalit saqlanishdan OLDIN tekshiriladi (format + imkon bo'lsa jonli so'rov) — xato kalit saqlanmaydi, sababi aytiladi;
  * Vercel'da (fayl tizimi yopiq) bazada SHIFRLANGAN holda saqlanadi, mahalliyda esa .env ga (u .gitignore da);
  * sahifada kalit HECH QACHON to'liq ko'rsatilmaydi (faqat boshi/oxiri), tozalash va qayta tekshirish mumkin.
"""
from __future__ import annotations

import asyncio
import logging
import os
import re

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

import ai_keys
import database as db

logger = logging.getLogger(__name__)

KEYS = [
    # (name, label, group, secret?, help)
    ("ANTHROPIC_API_KEY", "Claude (Anthropic) kaliti", "AI", True, "PULLIK (ixtiyoriy): console.anthropic.com → API Keys, 'sk-ant-' bilan boshlanadi. Ishlashi uchun Billing'da kredit kerak; kredit bo'lmasa sayt Gemini'dan foydalanadi."),
    ("GEMINI_API_KEY", "Gemini (Google AI) kaliti", "AI", True, "BEPUL: aistudio.google.com/app/apikey → Create API key. 'AQ.' yoki 'AIza' bilan boshlanadi. Sayt AI'si asosan shu orqali ishlaydi."),
    ("TURNSTILE_SITE_KEY", "Turnstile — Site key", "Cloudflare Turnstile", False, "Cloudflare → Turnstile → widget → Site Key ('0x4…')."),
    ("TURNSTILE_SECRET_KEY", "Turnstile — Secret key", "Cloudflare Turnstile", True, "Cloudflare → Turnstile → widget → Secret Key. Faqat serverda ishlatiladi."),
    ("GOOGLE_CLIENT_ID", "Google — Client ID", "Google bilan kirish", False, "Google Cloud Console → Credentials → OAuth client. '….apps.googleusercontent.com'."),
    ("GOOGLE_CLIENT_SECRET", "Google — Client Secret", "Google bilan kirish", True, "Odatda 'GOCSPX-' bilan boshlanadi."),
]
_INFO = {k[0]: k for k in KEYS}

_FORMAT = {
    "ANTHROPIC_API_KEY": (re.compile(r"^sk-ant-[A-Za-z0-9_\-]{20,}$"), "Claude kaliti 'sk-ant-' bilan boshlanadigan uzun matn bo'lishi kerak. Boshqa joydan nusxalangan bo'lishi mumkin."),
    "GEMINI_API_KEY": (re.compile(r"^(AIza[0-9A-Za-z_\-]{30,}|AQ\.[0-9A-Za-z_\-\.]{20,})$"), "Gemini kaliti 'AIza…' yoki 'AQ.…' bilan boshlanadi (aistudio.google.com/app/apikey dan nusxalang)."),
    "TURNSTILE_SITE_KEY": (re.compile(r"^0x[0-9A-Za-z_\-]{10,}$"), "Turnstile Site key '0x' bilan boshlanadi. Secret key'ni noto'g'ri joyga qo'ymadingizmi?"),
    "TURNSTILE_SECRET_KEY": (re.compile(r"^0x[0-9A-Za-z_\-]{10,}$"), "Turnstile Secret key '0x' bilan boshlanadi."),
    "GOOGLE_CLIENT_ID": (re.compile(r"^[0-9]+-[0-9a-z]+\.apps\.googleusercontent\.com$"), "Google Client ID '123…-abc….apps.googleusercontent.com' ko'rinishida bo'lishi kerak."),
    "GOOGLE_CLIENT_SECRET": (re.compile(r"^[A-Za-z0-9_\-]{16,}$"), "Google Client Secret juda qisqa yoki noto'g'ri belgilar bor."),
}


class _TempEnv:
    """Kalitni vaqtincha muhitga qo'yib sinaydi; muvaffaqiyatsiz bo'lsa eskisini qaytaradi."""
    def __init__(self, name, value):
        self.name, self.value, self.old = name, value, os.environ.get(name)

    def __enter__(self):
        os.environ[self.name] = self.value

    def restore(self):
        if self.old is None:
            os.environ.pop(self.name, None)
        else:
            os.environ[self.name] = self.old


async def _probe_ai(name: str, value: str) -> tuple[str, str]:
    """('ok'|'bad'|'warn', xabar)"""
    import ai_claude
    import ai_diagnostics
    import ai_gemini
    provider = "claude" if name == "ANTHROPIC_API_KEY" else "gemini"
    tmp = _TempEnv(name, value)
    tmp.__enter__()
    ai_diagnostics.clear_error(provider)
    probe = "Faqat bitta so'z bilan javob ber: salom"
    try:
        if provider == "claude":
            res = await asyncio.wait_for(ai_claude.ask_claude(probe, "math", "ortacha", None, "normal"), timeout=25)
        else:
            res = await asyncio.wait_for(ai_gemini.ask_gemini(probe, "math", "normal"), timeout=25)
    except asyncio.TimeoutError:
        tmp.restore()
        return "warn", "Kalit tekshirilmadi: javob 25 soniyada kelmadi (tarmoq yoki provayder sekin)."
    except Exception as exc:  # noqa: BLE001
        res = None
        ai_diagnostics.record_error(provider, exc)
    if res:
        return "ok", "Kalit ishlaydi (jonli so'rov muvaffaqiyatli)."
    kind = (ai_diagnostics._last_errors.get(provider) or (0, "unknown", ""))[1]
    tmp.restore()
    if kind == "auth":
        return "bad", "Provayder bu kalitni QABUL QILMADI (noto'g'ri yoki o'chirilgan kalit). Qaytadan nusxalang."
    if kind == "credit":
        return "warn", ("Kalit to'g'ri va saqlandi, lekin Anthropic hisobida kredit yo'q — Claude API pullik (bepul tarifi yo'q). "
                        "console.anthropic.com → Billing'da hisob to'ldirilgach o'zi ishlaydi. Shu vaqtgacha sayt BEPUL Gemini orqali ishlaydi.")
    if kind == "quota":
        return "warn", "Kalit to'g'ri ko'rinadi, lekin so'rovlar limiti tugagan/band."
    if kind == "model":
        return "warn", "Kalit qabul qilindi, lekin model nomi topilmadi (CLAUDE_MODEL / GEMINI_MODEL)."
    return "warn", "Kalitni jonli tekshirib bo'lmadi (tarmoq yoki noma'lum xato) — format to'g'ri, saqlandi."


async def _probe_turnstile_secret(value: str) -> tuple[str, str]:
    import turnstile
    ok, codes, state = await turnstile.verify_detail("lz-key-check", "", secret=value)
    if state == "network":
        return "warn", "Secret key'ni Cloudflare orqali tekshirib bo'lmadi (tarmoq) — format to'g'ri, saqlandi."
    if "invalid-input-secret" in codes or "missing-input-secret" in codes:
        return "bad", "Cloudflare bu Secret key'ni QABUL QILMADI. Widget sahifasidagi 'Secret Key' ni nusxalang (Site Key emas)."
    return "ok", "Secret key to'g'ri (Cloudflare tasdiqladi)."


async def check_value(name: str, value: str) -> tuple[str, str]:
    """Saqlashdan oldingi tekshiruv. ('ok'|'warn'|'bad', xabar)."""
    rx = _FORMAT.get(name)
    if rx and not rx[0].match(value):
        return "bad", rx[1]
    if name in ("ANTHROPIC_API_KEY", "GEMINI_API_KEY"):
        return await _probe_ai(name, value)
    if name == "TURNSTILE_SECRET_KEY":
        return await _probe_turnstile_secret(value)
    return "ok", "Format to'g'ri."


async def save_key(name: str, raw: str) -> dict:
    if name not in _INFO and name not in ("GEMINI_MODEL", "CLAUDE_MODEL"):
        return {"ok": False, "msg": "Noma'lum kalit nomi."}
    value = ai_keys._clean(raw)
    if not value:
        return {"ok": False, "msg": "Qiymat bo'sh."}
    if len(value) > 300 or "\n" in value or "\r" in value:
        return {"ok": False, "msg": "Qiymat noto'g'ri (juda uzun yoki bir nechta qator)."}
    state, msg = ("ok", "Saqlandi.") if name in ("GEMINI_MODEL", "CLAUDE_MODEL") else await check_value(name, value)
    if state == "bad":
        return {"ok": False, "msg": msg}
    try:
        ai_keys.save(name, value)           # mahalliyda .env ga; Vercel'da yozilmaydi (jim)
        await db.save_env_override(name, value)
        if name == "ANTHROPIC_API_KEY":
            # Kredit bo'lmasa AI repetitor avval bepul Gemini'ni ishlatsin; Claude ishlasa — avval Claude
            await db.set_setting("ai_primary_repetitor", "gemini" if state == "warn" else "claude")
    except Exception:  # noqa: BLE001
        logger.exception("Kalitni saqlab bo'lmadi")
        return {"ok": False, "msg": "Saqlashda xato (baza). Server logiga qarang."}
    return {"ok": True, "warn": state == "warn", "msg": msg, "mask": ai_keys.mask(ai_keys.get(name))}


def _status_rows(overrides: set[str]) -> list[dict]:
    rows = []
    for name, label, group, secret, help_ in KEYS:
        val = ai_keys.get(name)
        src = "admin panel" if name in overrides else (".env / muhit" if val else "—")
        rows.append({"name": name, "label": label, "group": group, "secret": secret, "help": help_,
                     "set": bool(val), "mask": (ai_keys.mask(val) if secret else (val or "—")), "source": src})
    return rows


def register(app, prefix: str, require_admin, current_admin_username, templates) -> None:
    def guard(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")

    @app.get(f"{prefix}/keys", response_class=HTMLResponse)
    async def keys_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        import oauth_google
        import turnstile
        host = (request.headers.get("x-forwarded-host") or request.headers.get("host") or "").split(",")[0].strip()
        try:
            redirect_uri = oauth_google.redirect_uri_for(request)
        except Exception:  # noqa: BLE001
            redirect_uri = ""
        return templates.TemplateResponse(request, "admin_keys.html", {
            "active_tab": "keys", "rows": _status_rows(await db.env_override_names()),
            "host": host, "redirect_uri": redirect_uri,
            "ts_mode": turnstile.mode(), "ts_fallback": turnstile.fallback_allowed(),
            "ts_active_here": turnstile.is_active_for_request(request),
        })

    @app.post(f"{prefix}/api/keys/save")
    async def keys_save(request: Request):
        guard(request)
        body = await request.json()
        res = await save_key(str(body.get("name", "")), str(body.get("value", "")))
        if res.get("ok"):
            await db.log_admin_action(current_admin_username(request), "key_saved", str(body.get("name")))
        return JSONResponse(res, status_code=200)

    @app.post(f"{prefix}/api/keys/clear")
    async def keys_clear(request: Request):
        guard(request)
        name = str((await request.json()).get("name", ""))
        if name not in _INFO:
            return JSONResponse({"ok": False, "msg": "Noma'lum kalit."})
        try:
            ai_keys.save(name, "")
        except Exception:  # noqa: BLE001
            pass
        await db.clear_env_override(name)
        await db.log_admin_action(current_admin_username(request), "key_cleared", name)
        return JSONResponse({"ok": True, "msg": "Tozalandi.", "mask": ai_keys.mask(ai_keys.get(name))})

    @app.post(f"{prefix}/api/keys/test")
    async def keys_test(request: Request):
        guard(request)
        name = str((await request.json()).get("name", ""))
        if name not in _INFO:
            return JSONResponse({"ok": False, "msg": "Noma'lum kalit."})
        val = ai_keys.get(name)
        if not val:
            return JSONResponse({"ok": False, "msg": "Kalit kiritilmagan."})
        state, msg = await check_value(name, val)
        return JSONResponse({"ok": state != "bad", "warn": state == "warn", "msg": msg})

    @app.post(f"{prefix}/api/keys/option")
    async def keys_option(request: Request):
        guard(request)
        body = await request.json()
        name, value = str(body.get("name", "")), str(body.get("value", "")).strip().lower()
        allowed = {"TURNSTILE_MODE": {"auto", "off"}, "TURNSTILE_FALLBACK": {"on", "off"}}
        if name not in allowed or value not in allowed[name]:
            return JSONResponse({"ok": False, "msg": "Noto'g'ri qiymat."})
        try:
            ai_keys.save(name, value)
        except Exception:  # noqa: BLE001
            os.environ[name] = value
        await db.save_env_override(name, value)
        await db.log_admin_action(current_admin_username(request), "key_option", f"{name}={value}")
        return JSONResponse({"ok": True, "msg": "Saqlandi."})
