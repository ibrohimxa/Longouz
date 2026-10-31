"""
LongoUZ websayt — FastAPI asosiy ilova.
Ishga tushirish:  python main.py   (yoki start_server.bat)
Server 0.0.0.0:6060 (HTTP) va :6600 (HTTPS) da ishlaydi — shu kompyuterda http://localhost:6060,
boshqa qurilmalarda http://<kompyuter-IP>:6060 orqali ochiladi.

Hozircha mavjud: /register, /login, /logout, /dashboard
Keyingi qadamlarda qo'shiladi: Gemini/Claude AI, testlar, baholash.
"""

import os
import uuid
import secrets
import random
import re
import logging
from datetime import datetime, date, timedelta

# XAVFSIZLIK: .env fayldagi muhit o'zgaruvchilarini (API kalitlar, maxfiy
# kalit va h.k.) ENG BIRINCHI bo'lib yuklaymiz — pastdagi `import ai_config`
# va boshqa modullar `os.getenv(...)` chaqirganda bu qiymatlar allaqachon
# joyida bo'lishi kerak. .env fayl topilmasa (masalan production'da haqiqiy
# muhit o'zgaruvchilari to'g'ridan-to'g'ri serverga o'rnatilgan bo'lsa),
# bu chaqiruv shunchaki hech narsa qilmaydi — xato bermaydi.
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel, Field

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import runtime
import database as db
import ai_router as ai
import scoring
import exam_rules
import exam_db
import certificate_gen
import prompt_safety
import figures as figures_mod
import tts as tts_module
import admin_auth

# Admin panel manzili — "/admin" o'rniga taxmin qilish qiyinroq bo'lgan yo'l
# (standart: /neo, .env'dagi ADMIN_URL_PREFIX orqali o'zgartiriladi).
ADMIN_PREFIX = admin_auth.ADMIN_URL_PREFIX
import oauth_google
import turnstile
import ielts_topics
from auth import (
    hash_password, verify_password, create_access_token, decode_access_token,
    COOKIE_NAME, set_session_cookie, SECRET_KEY,
)

logger = logging.getLogger(__name__)

_EXPOSE_DOCS = os.getenv("EXPOSE_API_DOCS", "false").strip().lower() == "true"
app = FastAPI(
    title="LongoUZ",
    docs_url="/docs" if _EXPOSE_DOCS else None,
    redoc_url=None,
    openapi_url="/openapi.json" if _EXPOSE_DOCS else None,
)

# ---------------------------------------------------------------------------
# RATE LIMITING — IP bo'yicha so'rovlar sonini cheklaydi. Bunga ehtiyoj bor,
# chunki /api/quiz/generate va /api/ask kabi AI chaqiruvlari PULGA tushadi
# (token sarflaydi) — himoyasiz qoldirilsa, kimdir avtomatik skript bilan
# ming marta so'rov yuborib, hisobingizdagi AI kreditini bir zumda
# tugatishi yoki serverni DoS bilan cho'ktirishi mumkin.
# ---------------------------------------------------------------------------
def _client_key(request: Request) -> str:
    """Vercel/Cloudflare proksi ortida haqiqiy foydalanuvchi IP'si (aks holda hamma bitta IP bo'lib qoladi)."""
    fwd = request.headers.get("cf-connecting-ip") or request.headers.get("x-real-ip") or request.headers.get("x-forwarded-for", "")
    return fwd.split(",")[0].strip() if fwd else get_remote_address(request)


limiter = Limiter(key_func=_client_key)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# ---------------------------------------------------------------------------
# XAVFSIZLIK SARLAVHALARI (security headers) — har bir javobga qo'shiladi.
# Maqsad: clickjacking (X-Frame-Options), MIME-sniffing orqali hujum
# (X-Content-Type-Options), va begona saytlarga URL orqali maxfiy ma'lumot
# "sizib chiqishi" (Referrer-Policy) kabi keng tarqalgan hujum turlarining
# oldini olish — bular server buzib kirishning O'ZINI to'xtatmaydi, lekin
# muvaffaqiyatli bo'lgan taqdirda zararni sezilarli kamaytiradi.
#
# Content-Security-Policy — sayt FAQAT o'zi ishlatadigan tashqi manbalarga
# ruxsat beradi (Google Fonts, Cloudflare Turnstile, Google OAuth) — boshqa
# hech qanday tashqi skript/frame yuklanmaydi, hatto sayt kodiga kimdir
# zararli <script> qo'shib qo'ysa ham brauzer uni bloklaydi.
# ---------------------------------------------------------------------------
_CSP_POLICY = (
    "default-src 'self'; "
    "script-src 'self' https://challenges.cloudflare.com 'unsafe-inline'; "
    "style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; "
    "font-src 'self' https://fonts.gstatic.com; "
    "img-src 'self' data: https:; "
    "media-src 'self' blob:; "
    "connect-src 'self' https://challenges.cloudflare.com; "
    "frame-src https://challenges.cloudflare.com https://accounts.google.com; "
    "child-src https://challenges.cloudflare.com blob:; "
    "worker-src 'self' blob:; "
    "frame-ancestors 'none'; "
    "object-src 'none'; "
    "base-uri 'self';"
)


# v219: HTML/JSON javoblar siqiladi (sekin mobil internetda sahifa ancha tez ochiladi)
from starlette.middleware.gzip import GZipMiddleware as _GZip
app.add_middleware(_GZip, minimum_size=1200, compresslevel=5)

# v223: yagona manzil — eski *.vercel.app manzillari (longouz-v1xf..., longo-uz) asosiy manzilga yo'naltiriladi.
# Asosiy manzil SITE_BASE_URL dan olinadi (masalan https://longouz.vercel.app). Faqat production'da ishlaydi.
def _canonical_host() -> str:
    from urllib.parse import urlsplit
    u = (os.getenv("SITE_BASE_URL") or "").strip()
    return (urlsplit(u).hostname or "").lower() if u.startswith("http") else ""


@app.middleware("http")
async def canonical_host_middleware(request: Request, call_next):
    if runtime.IS_VERCEL and os.getenv("VERCEL_ENV", "production") == "production":
        canon = _canonical_host()
        host = (request.headers.get("host") or "").split(":")[0].lower()
        if canon and canon.endswith(".vercel.app") and host and host != canon and host.endswith(".vercel.app"):
            target = f"https://{canon}{request.url.path}"
            if request.url.query:
                target += "?" + request.url.query
            return RedirectResponse(target, status_code=308)
    return await call_next(request)


@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    if runtime.IS_VERCEL:
        await _ensure_db_ready()
        await db.load_env_overrides()  # 45 soniyada bir marta: boshqa instansda saqlangan kalitlar
        _kick_seed(request)
    response = await call_next(request)
    try:
        import question_figures as _qf
        if _qf.PENDING:
            pending = dict(_qf.PENDING)
            _qf.PENDING.clear()
            await db.save_qfigs(pending)
    except Exception:  # noqa: BLE001
        logger.exception("Chizma rasmlarini bazaga yozib bo'lmadi")
    try:
        if response.status_code == 200 and "text/html" in response.headers.get("content-type", ""):
            import insights as _ins
            _ins.record(request, ADMIN_PREFIX)
            if runtime.IS_VERCEL:
                await _ins.flush(force=True)  # Vercel fon vazifasini muzlatadi — darhol yozamiz
            else:
                _ins.schedule_flush()
    except Exception:  # noqa: BLE001
        pass
    if getattr(request.state, "drop_session", False):
        response.delete_cookie(COOKIE_NAME)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), camera=(), payment=()"
    response.headers["Content-Security-Policy"] = _CSP_POLICY
    # HSTS faqat HAQIQIY HTTPS ulanishida ma'noga ega (brauzer HTTP orqali
    # kelgan HSTS sarlavhasini e'tiborsiz qoldiradi, lekin lokal http://
    # rivojlantirishda chalkashtirmaslik uchun shart bo'lganda qo'shamiz).
    if request.url.path.startswith("/static/") and "Cache-Control" not in response.headers:
        response.headers["Cache-Control"] = "public, max-age=300, stale-while-revalidate=604800"
    if request.url.scheme == "https":
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
    return response


# ---------------------------------------------------------------------------
# GLOBAL XATOLIK USHLAGICH — xavfsizlik uchun MUHIM: kutilmagan xato
# (masalan dasturdagi bug, DB uzilishi) yuz bersa, foydalanuvchiga Python
# Traceback (fayl yo'llari, kod qatorlari, ichki struktura) HECH QACHON
# ko'rsatilmaydi — faqat umumiy, xavfsiz xabar qaytariladi. Haqiqiy xato
# esa serverning o'z logiga to'liq yoziladi (admin ko'rishi uchun).
# ---------------------------------------------------------------------------
@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Kutilmagan server xatosi: {request.method} {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Serverda kutilmagan xatolik yuz berdi. Iltimos, birozdan so'ng qayta urinib ko'ring."},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    # HTTPException'lar (401, 404, va h.k.) — bu bizning o'zimiz ataylab
    # qaytaradigan, xavfsiz xabarlar, shuning uchun o'zgarishsiz qaytariladi.
    if exc.status_code in (301, 302, 303, 307, 308) and exc.headers and exc.headers.get("Location"):
        return RedirectResponse(exc.headers["Location"], status_code=302)
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail}, headers=exc.headers or None)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Pydantic validatsiya xatolari — ichki struktura tafsilotlarini
    # (masalan fayl yo'li) fosh qilmasdan, faqat qaysi maydon xato ekanini
    # qaytaramiz.
    errors = [{"field": ".".join(str(p) for p in e["loc"]), "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"detail": "Yuborilgan ma'lumot noto'g'ri.", "errors": errors})

# BASE_DIR — bu fayl (main.py) joylashgan papka, ya'ni web/.
# Bu orqali templates/static yo'llari SERVER QAYERDAN ISHGA TUSHIRILISHIDAN
# QAT'IY NAZAR to'g'ri topiladi (ildizdan ham, web/ ichidan ham).
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
# admin_prefix — barcha shablonlarda {{ admin_prefix }} orqali ishlatiladi,
# har bir render() chaqiruviga alohida qo'shish shart emas (global).
templates.env.globals["admin_prefix"] = ADMIN_PREFIX
# Google tugmasi barcha login/register sahifalarida (xato holatlarida ham)
# ko'rinishi/yashirinishi uchun — har bir route'da alohida uzatish o'rniga
# global sifatida bir marta qo'shildi.
templates.env.globals["google_enabled"] = oauth_google.is_enabled
templates.env.globals["turnstile_active"] = turnstile.is_active_for_request
templates.env.globals["turnstile_site_key"] = turnstile.site_key
@app.get("/static/qfig/{name}")
async def serve_qfig(name: str):
    """Admin yuklagan chizmalar: avval baza, keyin (lokal) disk."""
    import re as _re0
    if not _re0.fullmatch(r"[A-Za-z0-9_.-]{6,80}", name):
        raise HTTPException(status_code=404)
    data = await db.get_qfig(name)
    if data is None:
        p = os.path.join(BASE_DIR, "static", "qfig", name)
        if os.path.isfile(p):
            with open(p, "rb") as fh:
                data = fh.read()
    if data is None:
        raise HTTPException(status_code=404)
    return Response(data, media_type="image/png", headers={"Cache-Control": "public, max-age=31536000, immutable"})


app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")


_DB_READY = False
_SEED_DONE = False
_SEED_TASK = None


def _kick_seed(request: Request):
    """Vercel: tayyor savollar bazasi hali to'liq yuklanmagan bo'lsa, fon vazifasi sifatida davom ettiradi.
    (Fon vazifa instans muzlatilsa to'xtashi mumkin — shuning uchun sahifalar /api/seed-step ni ham chaqiradi.)"""
    global _SEED_TASK
    # v224: Vercel javob qaytgach fon vazifasini muzlatadi va u qulfni 100 s band qilib qo'yardi.
    # Endi yuklash faqat /api/seed-step so'rovlari ichida bajariladi (sahifalar uni o'zi chaqiradi).
    return
    if _SEED_DONE or request.url.path.startswith(("/static", "/api/seed-step")):
        return
    if _SEED_TASK is not None and not _SEED_TASK.done():
        return

    async def _run():
        global _SEED_DONE
        try:
            res = await exam_db.seed_step(budget=12)  # v219: instansni uzoq band qilmasin
            if res.get("done"):
                _SEED_DONE = True
        except Exception:  # noqa: BLE001
            logger.exception("Fon rejimida savollarni yuklashda xato")

    import asyncio as _asyncio
    _SEED_TASK = _asyncio.create_task(_run())


@app.get("/api/health")
async def api_health():
    """Holat: baza turi va ulanish (maxfiy ma'lumot chiqarilmaydi)."""
    info = {"db": "sqlite" if db.IS_SQLITE else "postgres", "ok": False}
    try:
        from sqlalchemy import text as _t
        async with db.async_session() as session:
            await session.execute(_t("select 1"))
            info["users"] = (await session.execute(_t("select count(*) from web_users"))).scalar()
        info["ok"] = True
    except Exception as exc:  # noqa: BLE001
        info["error"] = type(exc).__name__ + ": " + str(exc)[:160].replace(os.getenv("DATABASE_URL", "") or "\x00", "***")
    return JSONResponse(info)


@app.get("/api/seed-step")
@limiter.limit("30/minute")
async def api_seed_step(request: Request):
    """Savollar bazasini bo'laklab yuklaydi (Vercel). Sahifadagi kichik skript tugaguncha takror chaqiradi."""
    global _SEED_DONE
    if _SEED_DONE:
        return JSONResponse({"done": True})
    try:
        res = await exam_db.seed_step(budget=40)
    except Exception:  # noqa: BLE001
        logger.exception("seed-step xatosi")
        return JSONResponse({"done": False, "error": True})
    if res.get("done"):
        _SEED_DONE = True
    return JSONResponse(res)


@app.on_event("startup")
async def on_startup():
    global _DB_READY
    await db.init_web_db()
    _DB_READY = True


async def _ensure_db_ready():
    """Serverless (Vercel) da lifespan ishonchsiz — birinchi so'rovda bazani tayyorlaymiz."""
    global _DB_READY
    if not _DB_READY:
        _DB_READY = True
        try:
            await db.init_web_db()
        except Exception:  # noqa: BLE001
            _DB_READY = False
            raise


# ---------------------------------------------------------------------------
# Joriy foydalanuvchini cookie'dagi JWT orqali aniqlash
# ---------------------------------------------------------------------------

async def get_current_user(request: Request) -> db.WebUser | None:
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        return None
    user_id = decode_access_token(token)
    if user_id is None:
        request.state.drop_session = True  # v224: yaroqsiz token — cookie tozalanadi (header "Chiqish" ko'rsatmasin)
        return None
    user = await db.get_user_by_id(user_id)
    if user is None:
        request.state.drop_session = True
    return user


async def require_user(request: Request) -> db.WebUser:
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=307, headers={"Location": "/login"})
    return user


# ---------------------------------------------------------------------------
# Bosh sahifa
# ---------------------------------------------------------------------------

_QCOUNT_CACHE = {"t": 0.0, "n": 0}


async def _question_total() -> int:
    """Bazadagi HAQIQIY (takrorlanmas) savollar soni — bir savol bir nechta rejimda bo'lsa ham bir marta sanaladi.
    10 daqiqa keshlanadi — bosh sahifa tez ochilsin."""
    import time as _t
    if _QCOUNT_CACHE["n"] and _t.time() - _QCOUNT_CACHE["t"] < 600:
        return _QCOUNT_CACHE["n"]
    try:
        from sqlalchemy import select as _sel, func as _fn
        async with db.async_session() as _s:
            n = (await _s.execute(
                _sel(_fn.count(_fn.distinct(db.Question.question))).where(db.Question.is_active == True)  # noqa: E712
            )).scalar() or 0
        _QCOUNT_CACHE.update(t=_t.time(), n=int(n))
    except Exception:
        logger.exception("savollar sonini hisoblab bo'lmadi")
    return _QCOUNT_CACHE["n"]


def _question_total_label(n: int) -> str:
    if n >= 1000:
        return f"{(n // 500) * 500:,}".replace(",", " ") + "+"
    return f"{n}+" if n else "Minglab"


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = await get_current_user(request)
    if user:
        return RedirectResponse("/dashboard", status_code=302)
    qn = await _question_total()
    return templates.TemplateResponse(request, "home.html", {"q_total_label": _question_total_label(qn)})



# ---------------------------------------------------------------------------
# FAN TANLOVI (bosh sahifadan): foydalanuvchi bosh sahifada fanni bosgan bo'lsa,
# ro'yxatdan o'tgach onboarding'da fan/darajani QAYTA so'ramaymiz.
# ---------------------------------------------------------------------------
SUBJECT_COOKIE = "lz_subject"
DEFAULT_LEVEL = "ortacha"


def _valid_subject(code: str | None) -> str:
    code = (code or "").strip()
    return code if code in db.SUBJECT_CODES else ""


def _remember_subject(response, code: str):
    if code:
        response.set_cookie(SUBJECT_COOKIE, code, max_age=60 * 60 * 24, httponly=True, samesite="lax")


async def _auto_onboard(request: Request, user, form_subject: str = ""):
    """Fan avval tanlangan bo'lsa (forma yoki cookie) — onboarding'ni o'tkazib yuboradi. Qaytaradi: user."""
    if user.onboarding_done:
        return user
    code = _valid_subject(form_subject) or _valid_subject(request.cookies.get(SUBJECT_COOKIE))
    if code:
        await db.complete_onboarding(user.id, code, DEFAULT_LEVEL, "dtm")
        refreshed = await db.get_user_by_id(user.id)
        return refreshed or user
    return user


AFTER_ONBOARD_COOKIE = "lz_after_onboard"


def _safe_next(next_url: str) -> str:
    next_url = (next_url or "").strip()
    return next_url if next_url.startswith("/") and not next_url.startswith("//") else ""


def _remember_after_onboard(response, user, next_url: str = ""):
    """Yangi o'quvchi fan tanlash (onboarding) sahifasiga yuborilsa, tanlab bo'lgach asl maqsadiga
    (masalan, tarif sotib olish oynasi) qaytishi uchun eslab qolamiz."""
    nxt = _safe_next(next_url)
    if nxt and not user.onboarding_done and not nxt.startswith("/onboarding"):
        response.set_cookie(AFTER_ONBOARD_COOKIE, nxt[:200], max_age=60 * 60, httponly=True, samesite="lax")
    return response


def _after_auth_destination(user, next_url: str = "") -> str:
    if next_url and next_url.startswith("/") and not next_url.startswith("//"):
        return next_url if user.onboarding_done or next_url.startswith("/onboarding") else "/onboarding"
    return "/dashboard" if user.onboarding_done else "/onboarding"

# ---------------------------------------------------------------------------
# Ro'yxatdan o'tish
# ---------------------------------------------------------------------------

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    user = await get_current_user(request)
    if user:
        return RedirectResponse("/dashboard" if user.onboarding_done else "/onboarding", status_code=302)
    plan = request.query_params.get("plan", "free")
    if plan not in ("free", "pro", "ultra"):
        plan = "free"
    subject = _valid_subject(request.query_params.get("subject")) or _valid_subject(request.cookies.get(SUBJECT_COOKIE))
    resp = templates.TemplateResponse(request, "register.html", {
        "error": GOOGLE_ERROR_TEXT.get(request.query_params.get("error", "")), "plan": plan,
        "subject": subject, "subject_name": db.SUBJECT_NAMES.get(subject, ""),
        "email": (request.query_params.get("email") or "")[:120],
    })
    _remember_subject(resp, _valid_subject(request.query_params.get("subject")))
    return resp


@app.post("/register", response_class=HTMLResponse)
@limiter.limit("10/minute")
async def register_submit(
    request: Request,
    first_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    password_confirm: str = Form(...),
    plan: str = Form("free"),
    subject: str = Form(""),
    cf_turnstile_response: str = Form("", alias="cf-turnstile-response"),
    cf_fallback: str = Form("", alias="cf-turnstile-fallback"),
):
    email = email.strip().lower()
    _keep = {"plan": plan, "subject": _valid_subject(subject), "subject_name": db.SUBJECT_NAMES.get(_valid_subject(subject), ""),
             "first_name": first_name.strip(), "email": email}

    if turnstile.is_active_for_request(request):
        turnstile_ok = await turnstile.check(request, cf_turnstile_response, cf_fallback)
        if not turnstile_ok:
            return templates.TemplateResponse(request, "register.html", {
                "error": "Juda ko'p urinish bo'ldi. 10 daqiqadan so'ng qayta urinib ko'ring yoki «Google bilan davom etish»ni bosing.", **_keep,
            })

    if not _EMAIL_RE.match(email):
        return templates.TemplateResponse(request, "register.html", {"error": "Email manzil noto'g'ri yozilgan (masalan: ism@gmail.com).", **_keep})
    if password != password_confirm:
        return templates.TemplateResponse(request, "register.html", {"error": "Parollar bir xil emas.", **_keep})
    if len(password) < 6:
        return templates.TemplateResponse(request, "register.html", {"error": "Parol kamida 6 belgidan iborat bo'lishi kerak.", **_keep})

    existing = await db.get_user_by_email(email)
    if existing:
        # Hisob allaqachon bor: parol to'g'ri bo'lsa — shunchaki kiritamiz (ro'yxatdan o'tish ham, kirish ham bir xil ishlaydi)
        if verify_password(password, existing.password_hash):
            await db.update_streak(existing.id)
            existing = await _auto_onboard(request, existing, subject)
            resp = RedirectResponse(_after_auth_destination(existing), status_code=302)
            set_session_cookie(resp, create_access_token(existing.id))
            return resp
        return templates.TemplateResponse(request, "register.html", {
            "error": "Bu email bilan hisob allaqachon bor — parol mos kelmadi. To'g'ri parolni kiriting (avtomatik kirasiz) yoki hisob Google orqali ochilgan bo'lsa «Google bilan davom etish»ni bosing.",
            **_keep, "account_exists": True,
        })

    password_hash = hash_password(password)
    # MUHIM: hisob HAR DOIM "free" tarifda yaratiladi — pulli (pro/ultra)
    # tarif faqat to'lov (checkout) bosqichidan o'tgandan keyin beriladi.
    # Aks holda foydalanuvchi "/register?plan=pro" havolasi orqali hech
    # qanday to'lovsiz Pro/Ultra tarifni bepul olib qo'yishi mumkin edi.
    user = await db.create_user(email=email, password_hash=password_hash, first_name=first_name.strip(), plan="free")
    await db.create_notification(user.id, "welcome", body="LongoUZ platformasiga xush kelibsiz! O'rganishni hoziroq boshlang.")

    user = await _auto_onboard(request, user, subject)
    token = create_access_token(user.id)
    if plan in ("pro", "ultra"):
        response = RedirectResponse(f"/upgrade?plan={plan}&auto=1", status_code=302) if user.onboarding_done else RedirectResponse("/onboarding", status_code=302)
    else:
        response = RedirectResponse(_after_auth_destination(user), status_code=302)
    set_session_cookie(response, token)
    response.delete_cookie(SUBJECT_COOKIE)
    if plan in ("pro", "ultra") and not user.onboarding_done:
        # Onboarding tugagach shu tarif uchun karta kiritish oynasi avtomatik
        # ochilishi uchun eslatib turamiz (qisqa muddatli, faqat shu oqim uchun).
        response.set_cookie(
            "intended_plan", plan,
            httponly=True,
            secure=os.getenv("WEB_COOKIE_SECURE", "false").strip().lower() == "true",
            samesite="lax",
            max_age=60 * 30,
        )
    return response


# ---------------------------------------------------------------------------
# BOSH SAHIFADAGI "DARHOL KARTA OYNASI" OQIMI — foydalanuvchi qat'iy talabi:
# bosh sahifada pullik (Pro/Ultra) tarifni bosganda avval ro'yxatdan o'tish
# sahifasiga EMAS, darhol karta kiritish oynasiga o'tsin. Bu ALOHIDA endpoint
# (yuqoridagi oddiy /register'dan farqli) — chunki bu yerga faqat home.html'dagi
# haqiqiy checkout darchasidan kelinadi, shuning uchun bu yerda hisob
# YARATILISHI BILAN BIRGA tarif ham DARHOL faollashtiriladi (haqiqiy to'lov
# ulanganda, aynan shu joy kartadan pul yechish logikasi bilan almashtiriladi).
# Oddiy "/register?plan=pro" havolasi orqali BEPUL "loophole" ochilmasligi
# uchun ESKI /register endpoint hech qachon to'g'ridan-to'g'ri pullik tarif
# bermaydi — faqat shu maxsus checkout yo'li beradi.
# ---------------------------------------------------------------------------

@app.post("/checkout/register", response_class=HTMLResponse)
@limiter.limit("10/minute")
async def checkout_register_submit(
    request: Request,
    first_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    password_confirm: str = Form(...),
    plan: str = Form(...),
    cf_turnstile_response: str = Form("", alias="cf-turnstile-response"),
    cf_fallback: str = Form("", alias="cf-turnstile-fallback"),
):
    email = email.strip().lower()
    if plan not in ("pro", "ultra"):
        plan = "pro"

    if turnstile.is_active_for_request(request):
        turnstile_ok = await turnstile.check(request, cf_turnstile_response, cf_fallback)
        if not turnstile_ok:
            return templates.TemplateResponse(request, "register.html", {
                "error": "Juda ko'p urinish bo'ldi. 10 daqiqadan so'ng qayta urinib ko'ring yoki «Google bilan davom etish»ni bosing.",
                "plan": plan, "first_name": first_name.strip(), "email": email,
            })

    if not _EMAIL_RE.match(email):
        return templates.TemplateResponse(request, "register.html", {"error": "Email manzil noto'g'ri yozilgan (masalan: ism@gmail.com).", "plan": plan, "first_name": first_name.strip(), "email": email})
    if password != password_confirm:
        return templates.TemplateResponse(request, "register.html", {"error": "Parollar bir xil emas.", "plan": plan, "first_name": first_name.strip(), "email": email})
    if len(password) < 6:
        return templates.TemplateResponse(request, "register.html", {"error": "Parol kamida 6 belgidan iborat bo'lishi kerak.", "plan": plan, "first_name": first_name.strip(), "email": email})

    existing = await db.get_user_by_email(email)
    if existing:
        # Hisob oldin ro'yxatdan o'tgan bo'lsa: parol to'g'ri bo'lsa — kiritib, tanlangan tarifni faollashtiramiz
        # (ilgari "email band" xatosi chiqardi va foydalanuvchi ro'yxatdan o'tgani hisobga olinmagandek tuyulardi).
        if verify_password(password, existing.password_hash):
            await db.admin_set_user_plan(existing.id, plan)
            await db.update_streak(existing.id)
            existing = await _auto_onboard(request, existing)
            response = RedirectResponse(_after_auth_destination(existing, "/profile?upgraded=1"), status_code=302)
            _remember_after_onboard(response, existing, "/profile?upgraded=1")
            set_session_cookie(response, create_access_token(existing.id))
            response.delete_cookie(SUBJECT_COOKIE)
            return response
        return templates.TemplateResponse(request, "login.html", {
            "error": "Bu email bilan hisob allaqachon bor, lekin parol mos kelmadi. Shu hisobga kiring — tarif oynasi o'zi ochiladi.",
            "next": f"/upgrade?plan={plan}&auto=1", "email": email,
        })

    password_hash = hash_password(password)
    # Bu yerda — oddiy /register'dan farqli — hisob TO'G'RIDAN-TO'G'RI
    # tanlangan pullik tarifda yaratiladi, chunki bu yo'lga faqat haqiqiy
    # checkout (karta) darchasidan kelinadi.
    user = await db.create_user(email=email, password_hash=password_hash, first_name=first_name.strip(), plan=plan)
    await db.create_notification(user.id, "welcome", body=f"LongoUZ platformasiga xush kelibsiz! {plan.upper()} tarifingiz faollashtirildi.")

    # Fan bosh sahifada tanlangan bo'lsa (cookie) — onboarding o'tkazib yuboriladi; aks holda faqat fan so'raladi.
    user = await _auto_onboard(request, user)
    token = create_access_token(user.id)
    response = RedirectResponse(_after_auth_destination(user), status_code=302)
    set_session_cookie(response, token)
    response.delete_cookie(SUBJECT_COOKIE)
    return response


_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
_EMAIL_TYPOS = {"gmial.com": "gmail.com", "gmai.com": "gmail.com", "gmal.com": "gmail.com", "gmail.co": "gmail.com",
                "gmail.con": "gmail.com", "gmail.cm": "gmail.com", "gamil.com": "gmail.com", "gmail.ru": "gmail.com",
                "gmali.com": "gmail.com", "gnail.com": "gmail.com", "mail.ri": "mail.ru", "yandex.r": "yandex.ru",
                "yahoo.co": "yahoo.com", "icloud.co": "icloud.com", "outlok.com": "outlook.com"}


@app.get("/api/auth/email-check")
@limiter.limit("40/minute")
async def auth_email_check(request: Request, email: str = ""):
    """Ro'yxatdan o'tish / kirish formasi uchun: email to'g'ri yozilganmi va bunday hisob bormi."""
    email = (email or "").strip().lower()
    if not _EMAIL_RE.match(email):
        return {"valid": False, "exists": False}
    domain = email.rsplit("@", 1)[1]
    suggest = email.rsplit("@", 1)[0] + "@" + _EMAIL_TYPOS[domain] if domain in _EMAIL_TYPOS else ""
    try:
        exists = bool(await db.get_user_by_email(email))
    except Exception:  # noqa: BLE001
        logger.exception("email-check")
        return {"valid": True, "exists": None, "suggest": suggest}
    return {"valid": True, "exists": exists, "suggest": suggest}


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    user = await get_current_user(request)
    if user:
        return RedirectResponse("/dashboard" if user.onboarding_done else "/onboarding", status_code=302)
    next_url = request.query_params.get("next", "")
    resp = templates.TemplateResponse(request, "login.html", {
        "error": GOOGLE_ERROR_TEXT.get(request.query_params.get("error", "")),
        "next": next_url, "email": (request.query_params.get("email") or "")[:120],
    })
    # next= ni cookie ga ham yozamiz — form login va Google OAuth ikkalasi uchun
    if next_url and next_url.startswith("/") and not next_url.startswith("//"):
        resp.set_cookie("lz_oauth_next", next_url[:200], max_age=600, httponly=True, samesite="lax")
    return resp


@app.post("/login", response_class=HTMLResponse)
@limiter.limit("10/minute")
async def login_submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    cf_turnstile_response: str = Form("", alias="cf-turnstile-response"),
    cf_fallback: str = Form("", alias="cf-turnstile-fallback"),
):
    email = email.strip().lower()

    if turnstile.is_active_for_request(request):
        if not await turnstile.check(request, cf_turnstile_response, cf_fallback):
            return templates.TemplateResponse(request, "login.html", {
                "error": "Bot tekshiruvi o'tmadi (yoki muddati tugadi). Sahifani yangilab, qayta urinib ko'ring.",
            })

    user = await db.get_user_by_email(email)
    form_next = ((await request.form()).get("next") or "").strip()

    if not user:
        return templates.TemplateResponse(request, "login.html", {
            "error": "Bu email bilan hisob topilmadi. Emailni tekshiring yoki «Ro'yxatdan o'tish»ni bosing.",
            "email": email, "next": form_next, "no_account": True,
        })
    if not verify_password(password, user.password_hash):
        return templates.TemplateResponse(request, "login.html", {
            "error": "Parol noto'g'ri. Agar hisobni Google orqali ochgan bo'lsangiz, «Google bilan davom etish»ni bosing.",
            "email": email, "next": form_next,
        })

    await db.update_streak(user.id)
    await db.update_last_login_and_check_welcome_back(user.id)
    user = await _auto_onboard(request, user)

    token = create_access_token(user.id)
    # next URL: avval form hidden input dan, keyin cookie dan olamiz
    next_url = (form_next or request.cookies.get("lz_oauth_next", "") or "").strip()
    response = RedirectResponse(_after_auth_destination(user, next_url), status_code=302)
    _remember_after_onboard(response, user, next_url)
    set_session_cookie(response, token)
    response.delete_cookie("lz_oauth_next")
    response.delete_cookie(SUBJECT_COOKIE)
    return response


@app.get("/logout")
async def logout():
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie(COOKIE_NAME)
    return response


# ---------------------------------------------------------------------------
# Google bilan kirish (OAuth 2.0) — GOOGLE_CLIENT_ID/SECRET sozlanmagan
# bo'lsa, bu routelar chaqirilganda ham xushmuomalalik bilan /login'ga
# qaytaradi (sayt buzilmaydi, faqat tugma ishlamaydi).
# ---------------------------------------------------------------------------

GOOGLE_ERROR_TEXT = {
    "google_not_configured": "Google bilan kirish sozlanmagan (.env da GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET yo'q).",
    "google_cancelled": "Google bilan kirish bekor qilindi yoki Google xato qaytardi. Qayta urinib ko'ring.",
    "google_state_mismatch": "Xavfsizlik tekshiruvi (state) muddati tugagan. Qaytadan \"Google bilan kirish\" ni bosing.",
    "google_failed": "Google bilan kirib bo'lmadi. Qayta urinib ko'ring.",
    "google_redirect_uri_mismatch": "Google Cloud Console'dagi 'Authorized redirect URI' ro'yxatida bu sayt manzili yo'q. Admin panelda (/neo → Tizim holati) aynan qo'shilishi kerak bo'lgan manzil ko'rsatilgan.",
    "google_invalid_client": "Google Client ID yoki Client Secret noto'g'ri (.env ni tekshiring).",
    "google_invalid_grant": "Google kodi eskirgan yoki bir marta ishlatilgan. Qaytadan urinib ko'ring.",
    "google_network": "Server Google bilan bog'lana olmadi (tarmoq). Birozdan so'ng urinib ko'ring.",
    "google_email_unverified": "Google hisobingizdagi email tasdiqlanmagan.",
    "google_no_email": "Google hisobidan email olinmadi.",
}


@app.get("/auth/google/login")
async def google_login(request: Request):
    if not oauth_google.is_enabled():
        return RedirectResponse("/login?error=google_not_configured", status_code=302)
    state = oauth_google.make_state(SECRET_KEY)
    # next= parametrini cookie ga yozamiz — callback da shu yerga qaytamiz
    next_url = request.query_params.get("next", "")
    response = RedirectResponse(
        oauth_google.build_authorize_url(oauth_google.redirect_uri_for(request), state), status_code=302,
    )
    _remember_subject(response, _valid_subject(request.query_params.get("subject")))
    if next_url and next_url.startswith("/") and not next_url.startswith("//"):
        response.set_cookie("lz_oauth_next", next_url[:200], max_age=600, httponly=True, samesite="lax")
    return response


@app.get("/auth/google/callback")
async def google_callback(request: Request, code: str = "", state: str = "", error: str = ""):
    if not oauth_google.is_enabled():
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )

    if error or not code:
        return RedirectResponse("/login?error=google_cancelled", status_code=302)

    if not oauth_google.verify_state(state, SECRET_KEY):
        logger.warning("Google OAuth: state noto'g'ri yoki eskirgan.")
        return RedirectResponse("/login?error=google_state_mismatch", status_code=302)

    userinfo, g_err = await oauth_google.exchange_code_for_userinfo(code, oauth_google.redirect_uri_for(request))
    if userinfo is None:
        return RedirectResponse(f"/login?error=google_{g_err or 'failed'}", status_code=302)

    email = userinfo["email"]
    user = await db.get_user_by_email(email)
    is_new_user = user is None
    if user is None:
        # Yangi foydalanuvchi — Google orqali birinchi marta kirmoqda.
        # Parol hech qachon ishlatilmaydi (foydalanuvchi doim Google orqali
        # kiradi), shuning uchun tasodifiy, kuchli, hech kimga ma'lum
        # bo'lmagan parol generatsiya qilib, hash'ini saqlaymiz — DB
        # sxemasini o'zgartirmasdan (password_hash NOT NULL) ishlaydi.
        random_password_hash = hash_password(secrets.token_urlsafe(32))
        user = await db.create_user(
            email=email, password_hash=random_password_hash,
            first_name=(userinfo["name"] or email.split("@")[0])[:60], plan="free",
        )

    await db.update_streak(user.id)
    if is_new_user:
        await db.create_notification(user.id, "welcome", body="LongoUZ platformasiga xush kelibsiz! O'rganishni hoziroq boshlang.")
    else:
        await db.update_last_login_and_check_welcome_back(user.id)
    # Ro'yxatdan o'tish ham, kirish ham BIR XIL: hisob bo'lsa kiradi, bo'lmasa yaratiladi.
    # Fan bosh sahifada tanlangan bo'lsa — onboarding o'tkazib yuboriladi.
    user = await _auto_onboard(request, user)
    token = create_access_token(user.id)
    # next URL faqat cookie'dan olinadi (callback GET so'rov — forma yo'q)
    next_url = (request.cookies.get("lz_oauth_next", "") or "").strip()
    response = RedirectResponse(_after_auth_destination(user, next_url), status_code=302)
    _remember_after_onboard(response, user, next_url)
    set_session_cookie(response, token)
    response.delete_cookie("lz_oauth_next")
    response.delete_cookie(SUBJECT_COOKIE)
    return response


# ---------------------------------------------------------------------------
# ADMIN PANEL — sayt foydalanuvchilari autentifikatsiyasidan (yuqoridagi
# COOKIE_NAME) BUTUNLAY ALOHIDA. Parol FAQAT .env fayldagi ADMIN_PASSWORD
# o'zgaruvchisidan olinadi (admin_auth.py) — kodning boshqa hech bir joyida
# takrorlanmaydi.
# ---------------------------------------------------------------------------

def require_admin(request: Request) -> bool:
    """Admin sahifalari uchun qo'riqchi — token yo'q yoki yaroqsiz bo'lsa
    None qaytaradi, chaqiruvchi buni /admin/login'ga redirect sifatida
    ishlatadi."""
    token = request.cookies.get(admin_auth.ADMIN_COOKIE_NAME)
    if not token:
        return False
    return admin_auth.verify_admin_token(token)


def current_admin_username(request: Request) -> str:
    """Admin jurnaliga yozish uchun — joriy admin sessiyasining nomini
    qaytaradi (require_admin allaqachon True qaytargandan keyin chaqiriladi)."""
    token = request.cookies.get(admin_auth.ADMIN_COOKIE_NAME, "")
    return admin_auth.get_admin_username(token)


@app.get(f"{ADMIN_PREFIX}/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    if require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}", status_code=302)
    return templates.TemplateResponse(request, "admin_login.html", {})


@app.post(f"{ADMIN_PREFIX}/login", response_class=HTMLResponse)
@limiter.limit("5/minute")  # brute-force'ga qarshi — oddiy login (10/daq)dan ham qattiqroq
async def admin_login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    if not admin_auth.verify_admin_credentials(username, password):
        logger.warning(f"Admin panelga noto'g'ri urinish: username={username!r}, IP={get_remote_address(request)}")
        return templates.TemplateResponse(request, "admin_login.html", {"error": "Login yoki parol noto'g'ri."})

    token = admin_auth.create_admin_token(username.strip())
    response = RedirectResponse(f"{ADMIN_PREFIX}", status_code=302)
    response.set_cookie(
        admin_auth.ADMIN_COOKIE_NAME, token,
        httponly=True,
        secure=os.getenv("WEB_COOKIE_SECURE", "false").strip().lower() == "true",
        samesite="lax",
        max_age=60 * 60 * admin_auth.ADMIN_TOKEN_EXPIRE_HOURS,
    )
    return response


@app.get(f"{ADMIN_PREFIX}/logout")
async def admin_logout():
    response = RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    response.delete_cookie(admin_auth.ADMIN_COOKIE_NAME)
    return response


@app.post(f"{ADMIN_PREFIX}/api/diagnose-auth")
async def admin_diagnose_auth(request: Request):
    """Cloudflare Turnstile va Google OAuth kalitlarini HAQIQIY so'rov bilan tekshiradi
    (soxta token/kod yuboriladi — javob kodi kalit to'g'riligini bildiradi)."""
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin kerak.")
    import aiohttp
    out: dict = {"redirect_uri": oauth_google.redirect_uri_for(request)}
    timeout = aiohttp.ClientTimeout(total=12)
    async with aiohttp.ClientSession() as http:
        if turnstile.is_enabled():
            try:
                async with http.post("https://challenges.cloudflare.com/turnstile/v0/siteverify",
                                     data={"secret": turnstile.secret_key(), "response": "diagnostic"}, timeout=timeout) as r:
                    codes = (await r.json()).get("error-codes", [])
                if "invalid-input-secret" in codes or "missing-input-secret" in codes:
                    out["turnstile"] = {"ok": False, "msg": "Secret key Cloudflare'da topilmadi — noto'g'ri kalit."}
                else:
                    out["turnstile"] = {"ok": True, "msg": "Cloudflare akkaunti secret key'ni qabul qildi (kalit haqiqiy). Site key domeni: dash.cloudflare.com → Turnstile → Hostname Management'da saytingiz domeni bo'lishi kerak."}
            except Exception as exc:
                out["turnstile"] = {"ok": False, "msg": f"Cloudflare'ga ulanib bo'lmadi: {exc}"}
        else:
            out["turnstile"] = {"ok": False, "msg": "TURNSTILE_SITE_KEY / TURNSTILE_SECRET_KEY .env da yo'q."}
        if oauth_google.is_enabled():
            try:
                async with http.post("https://oauth2.googleapis.com/token", data={
                    "code": "diagnostic", "client_id": oauth_google.client_id(),
                    "client_secret": oauth_google.client_secret(),
                    "redirect_uri": out["redirect_uri"], "grant_type": "authorization_code"}, timeout=timeout) as r:
                    body = await r.json()
                err = body.get("error", "")
                if err == "invalid_client":
                    out["google"] = {"ok": False, "msg": "Client ID yoki Client Secret noto'g'ri."}
                else:
                    out["google"] = {"ok": True, "msg": "Client ID/Secret to'g'ri. Endi Google Cloud Console → Credentials → Authorized redirect URIs ga aynan shu manzilni qo'shing: " + out["redirect_uri"]}
            except Exception as exc:
                out["google"] = {"ok": False, "msg": f"Google'ga ulanib bo'lmadi: {exc}"}
        else:
            out["google"] = {"ok": False, "msg": "GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET .env da yo'q."}
    return JSONResponse(out)


@app.get(f"{ADMIN_PREFIX}", response_class=HTMLResponse)
async def admin_dashboard_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    import ai_claude
    import ai_gemini
    stats = await db.get_platform_stats()
    bank_summary = await db.admin_question_bank_summary()
    overview = await db.admin_overview()
    status = [
        {"name": "Gemini (asosiy AI)", "ok": ai_gemini.is_gemini_configured(), "hint": "kalit sozlangan" if ai_gemini.is_gemini_configured() else "kalit yo'q"},
        {"name": "Claude (zaxira AI)", "ok": ai_claude.is_claude_configured(), "hint": "kalit sozlangan" if ai_claude.is_claude_configured() else "kalit yo'q"},
        {"name": "Google bilan kirish", "ok": oauth_google.is_enabled(), "hint": ("Google Cloud'da 'Authorized redirect URI' ga qo'shing: " + oauth_google.redirect_uri_for(request)) if oauth_google.is_enabled() else "sozlanmagan"},
        {"name": "Cloudflare Turnstile", "ok": turnstile.is_enabled(), "hint": (("shu manzilda FAOL" if turnstile.is_active_for_request(request) else "kalitlar bor, lekin lokal manzilda o'chirilgan (haqiqiy domenda yoqiladi)")) if turnstile.is_enabled() else "sozlanmagan"},
        {"name": "Ma'lumotlar bazasi", "ok": True, "hint": overview["db_engine"]},
    ]
    return templates.TemplateResponse(request, "admin_dashboard.html", {
        "stats": stats, "bank_summary": bank_summary, "ov": overview, "status": status,
        "subject_breakdown": overview["subject_breakdown"],
        "subject_names": db.SUBJECT_NAMES, "mode_names": {m["code"]: m["name"] for m in db.TEST_MODES},
        "active_tab": "dashboard",
    })


ADMIN_USERS_PAGE_SIZE = 25


@app.get(f"{ADMIN_PREFIX}/users", response_class=HTMLResponse)
async def admin_users_page(request: Request, page: int = 1, q: str = "", plan: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    page = max(1, page)
    search = q.strip()[:100]
    plan = plan if plan in ("free", "pro", "ultra") else ""
    total = await db.count_users(search, plan)
    total_pages = max(1, -(-total // ADMIN_USERS_PAGE_SIZE))  # ceil division
    page = min(page, total_pages)
    offset = (page - 1) * ADMIN_USERS_PAGE_SIZE

    users = await db.get_all_users(limit=ADMIN_USERS_PAGE_SIZE, offset=offset, search=search, plan=plan)
    stats = await db.users_quiz_stats([u.id for u in users])

    return templates.TemplateResponse(request, "admin_users.html", {
        "users": users,
        "stats": stats,
        "total": total,
        "total_pages": total_pages,
        "page": page,
        "search": search,
        "plan_filter": plan,
        "subject_names": db.SUBJECT_NAMES,
        "message": request.query_params.get("message", ""),
        "active_tab": "users",
    })


@app.get(f"{ADMIN_PREFIX}/users/export.csv")
async def admin_users_export(request: Request, q: str = "", plan: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    import csv, io
    plan = plan if plan in ("free", "pro", "ultra") else ""
    users = await db.get_all_users(limit=50000, offset=0, search=q.strip()[:100], plan=plan)
    stats = await db.users_quiz_stats([u.id for u in users])
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "ism", "email", "fan", "tarif", "royxatdan_otgan", "testlar", "ortacha_%"])

    def safe(v: str) -> str:  # CSV/Excel formula injection himoyasi
        v = str(v or "")
        return "'" + v if v[:1] in ("=", "+", "-", "@") else v

    for u in users:
        st = stats.get(u.id, {})
        w.writerow([u.id, safe(u.first_name), safe(u.email), u.subject or "", u.plan,
                    u.joined_at.isoformat() if u.joined_at else "", st.get("tests", 0), st.get("percent", 0)])
    await db.log_admin_action(current_admin_username(request), "users_export", f"{len(users)} ta")
    return Response("\ufeff" + buf.getvalue(), media_type="text/csv; charset=utf-8",
                    headers={"Content-Disposition": "attachment; filename=longouz_users.csv"})


@app.get(f"{ADMIN_PREFIX}/users/{{user_id}}", response_class=HTMLResponse)
async def admin_user_detail_page(request: Request, user_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    detail = await db.admin_user_detail(user_id)
    if detail is None:
        return RedirectResponse(f"{ADMIN_PREFIX}/users?message=Foydalanuvchi topilmadi.", status_code=302)
    return templates.TemplateResponse(request, "admin_user_detail.html", {
        **detail, "subject_names": db.SUBJECT_NAMES, "active_tab": "users",
    })


@app.post(f"{ADMIN_PREFIX}/users/{{user_id}}/plan")
async def admin_set_user_plan_route(request: Request, user_id: int, plan: str = Form(...)):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    ok = await db.admin_set_user_plan(user_id, plan)
    message = "Tarif yangilandi." if ok else "Foydalanuvchi topilmadi yoki tarif noto'g'ri."
    admin_name = current_admin_username(request)
    logger.info(f"ADMIN: user #{user_id} plan -> {plan} ({'OK' if ok else 'FAILED'})")
    if ok:
        await db.log_admin_action(admin_name, "plan_change", f"user #{user_id} -> {plan}")
    return RedirectResponse(f"{ADMIN_PREFIX}/users?message={message}", status_code=302)


@app.post(f"{ADMIN_PREFIX}/users/{{user_id}}/delete")
async def admin_delete_user_route(request: Request, user_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    ok = await db.admin_delete_user(user_id)
    message = "Foydalanuvchi o'chirildi." if ok else "Foydalanuvchi topilmadi."
    admin_name = current_admin_username(request)
    logger.warning(f"ADMIN: user #{user_id} delete -> {'OK' if ok else 'FAILED'}")
    if ok:
        await db.log_admin_action(admin_name, "user_delete", f"user #{user_id}")
    return RedirectResponse(f"{ADMIN_PREFIX}/users?message={message}", status_code=302)


# ---------------------------------------------------------------------------
# ADMIN — savollar banki (to'liq CRUD, "to'liq nazorat" so'ralganidek)
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/questions", response_class=HTMLResponse)
async def admin_questions_page(request: Request, page: int = 1, subject: str = "", mode: str = "", q: str = "", topic: str = "", status: str = "", source: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    page = max(1, page)
    search = q.strip()
    status = status if status in ("published", "private") else ""
    total = await db.admin_count_questions(subject=subject, mode=mode, topic=topic, search=search, status=status, source=source)
    total_pages = max(1, -(-total // db.ADMIN_QUESTIONS_PAGE_SIZE))
    page = min(page, total_pages)
    offset = (page - 1) * db.ADMIN_QUESTIONS_PAGE_SIZE

    questions = await db.admin_list_questions(subject=subject, mode=mode, topic=topic, search=search, limit=db.ADMIN_QUESTIONS_PAGE_SIZE, offset=offset, status=status, source=source)

    import json as _json
    opts_map = {}
    for _q in questions:
        try:
            opts_map[_q.id] = _json.loads(_q.options_json or "[]")
        except ValueError:
            opts_map[_q.id] = []
    return templates.TemplateResponse(request, "admin_questions.html", {
        "questions": questions, "opts_map": opts_map,
        "total": total,
        "total_pages": total_pages,
        "page": page,
        "subject": subject,
        "mode": mode,
        "search": search, "topic": topic, "status": status, "source": source,
        "sources": await db.admin_import_sources(),
        "subjects": db.SUBJECTS,
        "modes": db.TEST_MODES,
        "subject_names": db.SUBJECT_NAMES,
        "message": request.query_params.get("message", ""),
        "active_tab": "questions", "qtab": "list",
    })


def _parse_question_form(form) -> dict:
    options = [form.get(f"option_{i}", "").strip() for i in range(4)]
    return {
        "subject": form.get("subject", "").strip(),
        "mode": form.get("mode", "").strip(),
        "topic": form.get("topic", "").strip(),
        "mock_test": form.get("mock_test", "").strip(),
        "question": form.get("question_text", "").strip(),
        "options": options,
        "correct_index": int(form.get("correct_index", 0)),
        "explanation": form.get("explanation", "").strip(),
        "is_active": form.get("is_active") == "on",
        "is_final_test": form.get("is_final_test") == "on",
    }


@app.get(f"{ADMIN_PREFIX}/questions/new", response_class=HTMLResponse)
async def admin_question_new_page(request: Request, subject: str = "", mode: str = "", topic: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    return templates.TemplateResponse(request, "admin_question_form.html", {
        "pf": {"subject": subject, "mode": mode, "topic": topic},
        "question": None, "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "active_tab": "questions",
    })


@app.post(f"{ADMIN_PREFIX}/questions/new", response_class=HTMLResponse)
async def admin_question_create(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    form = await request.form()
    data = _parse_question_form(form)

    if data["subject"] not in db.SUBJECT_CODES or not data["question"] or any(not o for o in data["options"]):
        return templates.TemplateResponse(request, "admin_question_form.html", {
            "question": None, "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "active_tab": "questions",
            "error": "Barcha maydonlarni (fan, savol, 4 ta variant) to'ldiring.",
        })

    existing_topics = await db.list_topics_db(data["subject"], data["mode"])
    is_new_topic = bool(data["topic"]) and data["topic"] not in existing_topics

    try:
        q = await db.admin_create_question(
            subject=data["subject"], mode=data["mode"], topic=data["topic"],
            question=data["question"], options=data["options"],
            correct_index=data["correct_index"], explanation=data["explanation"],
            mock_test=data["mock_test"], is_final_test=data["is_final_test"],
        )
    except db.DuplicateQuestionError:
        return templates.TemplateResponse(request, "admin_question_form.html", {
            "question": None, "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "active_tab": "questions",
            "error": "Bu savol shu fan va rejimda allaqachon mavjud.",
        })
    await db.log_admin_action(current_admin_username(request), "question_create", f"#{q.id} ({data['subject']}/{data['mode']})")
    if form.get("notify") == "on":
        if is_new_topic:
            await db.notify_new_topic_once(data["subject"], data["mode"], data["topic"])
        await db.notify_question_change(data["subject"], data["mode"], "questions_added", [data["topic"]], 1)
    return RedirectResponse(f"{ADMIN_PREFIX}/questions?message=Savol qo'shildi.", status_code=302)


@app.get(f"{ADMIN_PREFIX}/questions/{{question_id}}/edit", response_class=HTMLResponse)
async def admin_question_edit_page(request: Request, question_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    q = await db.admin_get_question(question_id)
    if q is None:
        return RedirectResponse(f"{ADMIN_PREFIX}/questions?message=Savol topilmadi.", status_code=302)
    import json as _json
    return templates.TemplateResponse(request, "admin_question_form.html", {
        "question": q, "question_options": _json.loads(q.options_json),
        "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "active_tab": "questions",
        "error": "Bu savol matni shu fan va rejimda allaqachon mavjud." if request.query_params.get("error") == "duplicate" else "",
    })


@app.post(f"{ADMIN_PREFIX}/questions/{{question_id}}/edit", response_class=HTMLResponse)
async def admin_question_update(request: Request, question_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    form = await request.form()
    data = _parse_question_form(form)

    try:
        ok = await db.admin_update_question(
            question_id, subject=data["subject"], mode=data["mode"], topic=data["topic"],
            question=data["question"], options=data["options"],
            correct_index=data["correct_index"], explanation=data["explanation"],
            mock_test=data["mock_test"], is_active=data["is_active"], is_final_test=data["is_final_test"],
        )
    except db.DuplicateQuestionError:
        return RedirectResponse(f"{ADMIN_PREFIX}/questions/{question_id}/edit?error=duplicate", status_code=302)
    message = "Savol yangilandi." if ok else "Savol topilmadi."
    if ok:
        await db.log_admin_action(current_admin_username(request), "question_edit", f"#{question_id}")
        # Tahrirlash o'quvchilarga bildirishnoma YUBORMAYDI (faqat yangi test, xabar, yangilik).
    return RedirectResponse(f"{ADMIN_PREFIX}/questions?message={message}", status_code=302)


@app.post(f"{ADMIN_PREFIX}/questions/{{question_id}}/delete")
async def admin_question_delete(request: Request, question_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form()
    removed = await db.admin_delete_question(question_id)
    message = "Savol butunlay o'chirildi." if removed else "Savol topilmadi."
    if removed:
        await db.log_admin_action(current_admin_username(request), "question_delete", f"#{question_id}")
        # O'chirish o'quvchilarga bildirishnoma YUBORMAYDI.
    return RedirectResponse(f"{ADMIN_PREFIX}/questions?message={message}", status_code=302)


# ---------------------------------------------------------------------------
# ADMIN — MAVZULAR MARKAZI va MAVZU TAHRIRLAGICHI
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/questions/audit", response_class=HTMLResponse)
async def admin_questions_audit(request: Request, subject: str = "", mode: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    report = await db.admin_audit_questions(subject=subject, mode=mode)
    return templates.TemplateResponse(request, "admin_question_audit.html", {
        "report": report, "subject": subject, "mode": mode,
        "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "subject_names": db.SUBJECT_NAMES,
        "active_tab": "questions", "qtab": "audit",
    })


class QuickCorrectBody(BaseModel):
    index: int = Field(..., ge=0, le=9)


@app.post(f"{ADMIN_PREFIX}/api/questions/{{question_id}}/correct")
async def admin_question_quick_correct(request: Request, question_id: int, body: QuickCorrectBody):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin kerak.")
    ok = await db.admin_quick_set_correct(question_id, body.index)
    if not ok:
        raise HTTPException(status_code=404, detail="Savol yoki variant topilmadi.")
    await db.log_admin_action(current_admin_username(request), "question_set_correct", f"#{question_id} -> {'ABCDEF'[body.index]}")
    return JSONResponse({"ok": True, "index": body.index})


@app.get(f"{ADMIN_PREFIX}/topics", response_class=HTMLResponse)
async def admin_topics_page(request: Request, subject: str = "", mode: str = "", q: str = "", page: int = 1):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    all_topics = await db.admin_topic_overview(subject=subject, mode=mode, search=q.strip())
    totals = {
        "topics": len(all_topics), "questions": sum(t["total"] for t in all_topics),
        "active": sum(t["active"] for t in all_topics), "hidden": sum(t["hidden"] for t in all_topics),
    }
    per_page = 20
    total_pages = max(1, -(-len(all_topics) // per_page))
    page = min(max(1, page), total_pages)
    topics = all_topics[(page - 1) * per_page: page * per_page]
    return templates.TemplateResponse(request, "admin_topics.html", {
        "topics": topics, "totals": totals, "page": page, "total_pages": total_pages, "subject": subject, "mode": mode, "search": q.strip(),
        "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "subject_names": db.SUBJECT_NAMES,
        "mode_names": {m["code"]: m["name"] for m in db.TEST_MODES},
        "message": request.query_params.get("message", ""), "active_tab": "questions", "qtab": "topics",
    })


@app.get(f"{ADMIN_PREFIX}/topics/edit", response_class=HTMLResponse)
async def admin_topic_editor_page(request: Request, subject: str, mode: str, topic: str, start: int = 1):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    rows = await db.admin_topic_questions(subject, mode, topic)
    layout = await db.get_topic_layout(subject, mode, topic)
    import json as _json
    payload = {
        "subject": subject, "mode": mode, "topic": topic, "layout": layout,
        "subject_name": db.SUBJECT_NAMES.get(subject, subject),
        "mode_name": db.TEST_MODE_BY_CODE.get(mode, {}).get("name", mode),
        "time_limit_minutes": db.TEST_MODE_BY_CODE.get(mode, {}).get("time_limit_minutes", 30),
        "start": max(1, start), "prefix": ADMIN_PREFIX,
        "questions": [
            {"id": q.id, "question": q.question, "options": _json.loads(q.options_json),
             "correct_index": q.correct_index, "explanation": q.explanation or "",
             "is_active": bool(q.is_active), "style": db._parse_style(q.style_json),
             "figure": db._parse_figures(q.figure_json)}
            for q in rows
        ],
    }
    return templates.TemplateResponse(request, "admin_topic_editor.html", {
        "payload": payload, "subject": subject, "mode": mode, "topic": topic, "active_tab": "questions",
    })


@app.post(f"{ADMIN_PREFIX}/api/topic/save")
async def admin_topic_save(request: Request):
    """Mavzu tahrirlagichidan "Saqlash": o'zgargan savollar + o'chirilganlar + test oynasi sozlamalari.
    O'quvchilarga bildirishnoma YUBORILMAYDI."""
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
    if request.headers.get("x-requested-with") != "fetch":
        raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")
    import json as _json
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="JSON noto'g'ri.")
    subject, mode, topic = str(body.get("subject", "")), str(body.get("mode", "")), str(body.get("topic", "")).strip()
    if subject not in db.SUBJECT_CODES or mode not in db.TEST_MODE_BY_CODE or not topic:
        raise HTTPException(status_code=400, detail="Fan, rejim yoki mavzu noto'g'ri.")

    admin_name = current_admin_username(request)
    saved, created, deleted, errors = 0, 0, 0, []
    id_map: dict[str, int] = {}
    ok_keys: list[str] = []
    failed_keys: list[str] = []

    for qid in body.get("deletes", []) or []:
        try:
            if await db.admin_delete_question(int(qid)):
                deleted += 1
        except (TypeError, ValueError):
            continue

    for item in body.get("changes", []) or []:
        text_q = str(item.get("question", "")).strip()
        options = [str(o).strip() for o in (item.get("options") or [])][:4]
        try:
            ci = int(item.get("correct_index", 0))
        except (TypeError, ValueError):
            ci = 0
        label = item.get("label") or item.get("id") or "?"
        key = str(item.get("key", ""))
        if not text_q or len(options) != 4 or any(not o for o in options) or not (0 <= ci < 4):
            errors.append(f"{label}: savol va 4 ta variant to'ldirilishi shart")
            failed_keys.append(key)
            continue
        if len(text_q) > 2000 or any(len(o) > 700 for o in options):
            errors.append(f"{label}: matn juda uzun")
            failed_keys.append(key)
            continue
        style_json = _json.dumps(db.sanitize_style(item.get("style")), ensure_ascii=False)
        if len(style_json) > 1000:
            style_json = ""
        figure_json = figures_mod.figures_to_json(item.get("figure"))
        explanation = str(item.get("explanation", ""))[:2000]
        try:
            if item.get("id"):
                ok = await db.admin_update_question(
                    int(item["id"]), subject=subject, mode=mode, topic=topic, question=text_q, options=options,
                    correct_index=ci, explanation=explanation, mock_test=str(item.get("mock_test", "")),
                    is_active=bool(item.get("is_active", True)), is_final_test=bool(item.get("is_final_test", False)),
                    style_json=style_json, figure_json=figure_json,
                )
                if ok:
                    saved += 1
                    ok_keys.append(key)
                else:
                    errors.append(f"{label}: savol topilmadi (allaqachon o'chirilgan)")
                    failed_keys.append(key)
            else:
                q = await db.admin_create_question(
                    subject=subject, mode=mode, topic=topic, question=text_q, options=options,
                    correct_index=ci, explanation=explanation, style_json=style_json, figure_json=figure_json,
                )
                if not item.get("is_active", True):
                    await db.admin_set_questions_active([q.id], False)
                created += 1
                ok_keys.append(key)
                id_map[key] = q.id
        except db.DuplicateQuestionError:
            errors.append(f"{label}: bunday savol matni allaqachon mavjud")
            failed_keys.append(key)

    if "layout" in body:
        await db.set_topic_layout(subject, mode, topic, body.get("layout") or {})

    await db.log_admin_action(admin_name, "topic_edit", f"{subject}/{mode}/{topic}: {saved} tahrir, {created} yangi, {deleted} o'chirildi")
    return JSONResponse({"ok": not errors, "saved": saved, "created": created, "deleted": deleted,
                         "errors": errors, "id_map": id_map, "ok_keys": ok_keys, "failed_keys": failed_keys})


# ---------------------------------------------------------------------------
# ADMIN — savollarni ommaviy import qilish (JSON / CSV / TXT / PDF)
# ---------------------------------------------------------------------------

import json as _json_mod  # noqa: E402
import question_import as qimport  # noqa: E402

MAX_IMPORT_UPLOAD_BYTES = qimport.MAX_FILE_BYTES
MAX_IMPORT_TOTAL_BYTES = 120 * 1024 * 1024
IMPORT_MODES = ("dtm", "certificate", "ielts", "cefr")


import studio as _studio  # noqa: E402
_studio.register(app, ADMIN_PREFIX, require_admin, current_admin_username, templates, IMPORT_MODES)
import reports as _reports  # noqa: E402
import features215 as _f215  # noqa: E402
_reports.register(app, ADMIN_PREFIX, require_admin, current_admin_username, templates, limiter, get_current_user)
import keys_admin as _keys_admin  # noqa: E402
_keys_admin.register(app, ADMIN_PREFIX, require_admin, current_admin_username, templates)
import insights as _insights  # noqa: E402
_insights.register(app, ADMIN_PREFIX, require_admin, templates)
import news as _news  # noqa: E402
_news.register(app, ADMIN_PREFIX, require_admin, templates)


@app.get(f"{ADMIN_PREFIX}/import", response_class=HTMLResponse)
async def admin_import_page(request: Request, mode: str = "dtm"):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    mode = mode if mode in IMPORT_MODES else "dtm"
    thin = await qimport.thin_topics(mode, 15)
    return templates.TemplateResponse(request, "admin_import.html", {
        "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "mode": mode, "thin": thin[:60],
        "thin_total": len(thin), "active_tab": "import", "preview": None,
        "sources": await db.admin_import_sources(),
        "message": request.query_params.get("message", ""),
    })


# ---------------------------------------------------------------------------
# ADMIN — mavzu yaratish, "Test qo'shish", savollar ro'yxati, chizmalar, JSON/fayl import
# ---------------------------------------------------------------------------

def _admin_api_guard(request: Request) -> None:
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
    if request.headers.get("x-requested-with") != "fetch":
        raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")


def _valid_scope(subject: str, mode: str) -> bool:
    return subject in db.SUBJECT_CODES and mode in db.TEST_MODE_BY_CODE


@app.post(f"{ADMIN_PREFIX}/topics/new")
async def admin_topic_create(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form()
    subject, mode, name = form.get("subject", ""), form.get("mode", ""), (form.get("name") or "").strip()
    if not _valid_scope(subject, mode) or not name:
        return RedirectResponse(f"{ADMIN_PREFIX}/topics?message=Fan, rejim va mavzu nomini kiriting.", status_code=302)
    ok = await db.admin_create_topic(subject, mode, name)
    if not ok:
        return RedirectResponse(f"{ADMIN_PREFIX}/topics?subject={subject}&mode={mode}&message=Bu nomdagi mavzu allaqachon bor.", status_code=302)
    await db.log_admin_action(current_admin_username(request), "topic_create", f"{subject}/{mode}/{name}")
    from urllib.parse import quote
    return RedirectResponse(f"{ADMIN_PREFIX}/topics/add?subject={subject}&mode={mode}&topic={quote(' '.join(name.split()))}&created=1", status_code=302)


@app.post(f"{ADMIN_PREFIX}/topics/delete")
async def admin_topic_delete(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form()
    subject, mode, topic = form.get("subject", ""), form.get("mode", ""), (form.get("topic") or "").strip()
    if not _valid_scope(subject, mode) or not topic:
        return RedirectResponse(f"{ADMIN_PREFIX}/topics?message=Noto'g'ri so'rov.", status_code=302)
    n = await db.admin_delete_topic(subject, mode, topic)
    await db.log_admin_action(current_admin_username(request), "topic_delete", f"{subject}/{mode}/{topic} ({n} savol)")
    return RedirectResponse(f"{ADMIN_PREFIX}/topics?message=Mavzu va {n} ta savol o'chirildi.", status_code=302)


@app.post(f"{ADMIN_PREFIX}/topics/rename")
async def admin_topic_rename(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form()
    subject, mode = form.get("subject", ""), form.get("mode", "")
    old, new = (form.get("topic") or "").strip(), (form.get("new_name") or "").strip()
    if not _valid_scope(subject, mode) or not old or not new:
        return RedirectResponse(f"{ADMIN_PREFIX}/topics?message=Noto'g'ri so'rov.", status_code=302)
    ok = await db.admin_rename_topic(subject, mode, old, new)
    if ok:
        await db.log_admin_action(current_admin_username(request), "topic_rename", f"{subject}/{mode}: {old} -> {new}")
    return RedirectResponse(f"{ADMIN_PREFIX}/topics?message={'Mavzu nomi o`zgartirildi.' if ok else 'Nomni o`zgartirib bo`lmadi (bunday nom bor yoki bo`sh).'}", status_code=302)


@app.get(f"{ADMIN_PREFIX}/topics/add", response_class=HTMLResponse)
async def admin_topic_add_page(request: Request, subject: str, mode: str, topic: str, created: int = 0, tab: str = "manual"):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    if not _valid_scope(subject, mode):
        return RedirectResponse(f"{ADMIN_PREFIX}/topics", status_code=302)
    return templates.TemplateResponse(request, "admin_topic_add.html", {
        "subject": subject, "mode": mode, "topic": topic, "created": bool(created), "tab": tab,
        "subject_name": db.SUBJECT_NAMES.get(subject, subject),
        "mode_name": db.TEST_MODE_BY_CODE.get(mode, {}).get("name", mode), "active_tab": "questions",
    })


@app.get(f"{ADMIN_PREFIX}/topics/questions", response_class=HTMLResponse)
async def admin_topic_questions_page(request: Request, subject: str, mode: str, topic: str):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    if not _valid_scope(subject, mode):
        return RedirectResponse(f"{ADMIN_PREFIX}/topics", status_code=302)
    rows = await db.admin_topic_questions(subject, mode, topic)
    import json as _json
    payload = {
        "subject": subject, "mode": mode, "topic": topic, "prefix": ADMIN_PREFIX,
        "questions": [
            {"id": q.id, "n": i + 1, "question": q.question, "options": _json.loads(q.options_json),
             "correct_index": q.correct_index, "is_active": bool(q.is_active), "has_figure": bool(q.figure_json)}
            for i, q in enumerate(rows)
        ],
    }
    return templates.TemplateResponse(request, "admin_topic_questions.html", {
        "payload": payload, "subject": subject, "mode": mode, "topic": topic,
        "subject_name": db.SUBJECT_NAMES.get(subject, subject),
        "mode_name": db.TEST_MODE_BY_CODE.get(mode, {}).get("name", mode), "active_tab": "questions",
    })


def _clean_question_payload(item: dict) -> tuple[dict | None, str]:
    """Bitta savol JSON'ini tekshiradi -> (tayyor dict, xato matni)."""
    text_q = str(item.get("question", "")).strip()
    options = [str(o).strip() for o in (item.get("options") or [])][:4]
    try:
        ci = int(item.get("correct_index"))
    except (TypeError, ValueError):
        return None, "to'g'ri javob ko'rsatilmagan"
    fig_json = figures_mod.figures_to_json(item.get("figure"))
    has_opt_fig = bool(fig_json and any(figures_mod.parse_figures(fig_json).get("o", [])))
    if not text_q and not fig_json:
        return None, "savol matni yoki chizma kerak"
    if not text_q:
        text_q = "Rasmga qarab savolga javob bering."
    if len(options) != 4 or not 0 <= ci < 4:
        return None, "4 ta variant va to'g'ri javob kerak"
    if any(not o for o in options):
        figs_o = figures_mod.parse_figures(fig_json).get("o", []) if fig_json else []
        options = [o or (f"{'ABCD'[i]} variant" if has_opt_fig and i < len(figs_o) and figs_o[i] else "") for i, o in enumerate(options)]
        if any(not o for o in options):
            return None, "barcha variantlarni to'ldiring"
    if len(text_q) > 2000 or any(len(o) > 700 for o in options):
        return None, "matn juda uzun"
    return {"question": text_q, "options": options, "correct_index": ci, "figure_json": fig_json,
            "explanation": str(item.get("explanation", ""))[:2000], "is_active": bool(item.get("is_active", True))}, ""


@app.post(f"{ADMIN_PREFIX}/api/question/create")
async def admin_api_question_create(request: Request):
    """Bitta savol (chizma bilan yoki chizmasiz) qo'shish."""
    _admin_api_guard(request)
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="JSON noto'g'ri.")
    subject, mode, topic = str(body.get("subject", "")), str(body.get("mode", "")), str(body.get("topic", "")).strip()
    if not _valid_scope(subject, mode) or not topic:
        raise HTTPException(status_code=400, detail="Fan, rejim yoki mavzu noto'g'ri.")
    clean, err = _clean_question_payload(body)
    if clean is None:
        raise HTTPException(status_code=422, detail=err)
    try:
        q = await db.admin_create_question(
            subject=subject, mode=mode, topic=topic, question=clean["question"], options=clean["options"],
            correct_index=clean["correct_index"], explanation=clean["explanation"], figure_json=clean["figure_json"],
        )
    except db.DuplicateQuestionError:
        raise HTTPException(status_code=409, detail="Bunday savol matni shu fan va rejimda allaqachon mavjud.")
    if not clean["is_active"]:
        await db.admin_set_questions_active([q.id], False)
    await db.log_admin_action(current_admin_username(request), "question_create", f"#{q.id} ({subject}/{mode}/{topic})")
    return JSONResponse({"ok": True, "id": q.id})


@app.post(f"{ADMIN_PREFIX}/api/topic/import-json")
async def admin_api_topic_import_json(request: Request):
    """JSON (matn yoki tayyor ro'yxat) -> mavzuga savollar. Chizmalar ham JSON ichida bo'lishi mumkin."""
    _admin_api_guard(request)
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="So'rov JSON emas.")
    subject, mode, topic = str(body.get("subject", "")), str(body.get("mode", "")), str(body.get("topic", "")).strip()
    if not _valid_scope(subject, mode) or not topic:
        raise HTTPException(status_code=400, detail="Fan, rejim yoki mavzu noto'g'ri.")
    publish = bool(body.get("publish", True))
    raw_items = body.get("items")
    if raw_items is None:
        text = str(body.get("text", "")).strip()
        if not text:
            raise HTTPException(status_code=422, detail="JSON matni bo'sh.")
        try:
            data = _json_mod.loads(text)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=f"JSON xato: {exc}")
        if isinstance(data, dict):
            for key in ("questions", "savollar", "items", "data"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
            else:
                data = [data]
        raw_items = data
    if not isinstance(raw_items, list) or not raw_items:
        raise HTTPException(status_code=422, detail="Savollar ro'yxati topilmadi.")
    raw_items = raw_items[:qimport.MAX_ITEMS]

    ready, errors = [], []
    for i, raw in enumerate(raw_items, 1):
        if not isinstance(raw, dict):
            errors.append(f"№{i}: obyekt emas")
            continue
        norm = qimport.normalize_item(raw)
        if norm is None:
            errors.append(f"№{i}: savol yoki 4 ta turli variant noto'g'ri")
            continue
        figure = raw.get("figure") if isinstance(raw.get("figure"), dict) else norm.get("figure")
        item = {"question": norm["question"], "options": norm["options"], "correct_index": norm["correct_index"],
                "explanation": norm["explanation"], "figure": figure}
        clean, err = _clean_question_payload(item)
        if clean is None:
            errors.append(f"№{i}: {err}")
            continue
        ready.append({"subject": subject, "mode": mode, "topic": topic, "question": clean["question"],
                      "options": clean["options"], "correct_index": clean["correct_index"],
                      "explanation": clean["explanation"], "figure_json": clean["figure_json"],
                      "src": str(raw.get("src") or "JSON")[:200], "no": int(raw.get("no") or i)})
    result = await db.admin_bulk_create_questions(ready, mock_test="Import", is_active=publish)
    await db.log_admin_action(current_admin_username(request), "question_import", f"{subject}/{mode}/{topic}: +{len(result['added'])}")
    return JSONResponse({"ok": True, "added": len(result["added"]), "skipped": result["skipped"], "errors": errors[:40],
                         "failed": len(errors)})


@app.post(f"{ADMIN_PREFIX}/api/topic/import-file")
async def admin_api_topic_import_file(request: Request):
    """Fayl(lar) — PDF, DOCX, XLSX, CSV, TXT, JSON, rasm, ZIP — o'qiladi; chizmalar ajratib olinadi.
    Natija: ko'rib chiqish uchun savollar ro'yxati (hali saqlanmaydi)."""
    _admin_api_guard(request)
    import asyncio
    form = await request.form(max_files=60)
    uploads = [u for u in form.getlist("file") if getattr(u, "filename", "")]
    if not uploads:
        raise HTTPException(status_code=422, detail="Fayl tanlang.")
    pairs, warns, total = [], [], 0
    for up in uploads:
        data = await up.read()
        total += len(data)
        if len(data) > MAX_IMPORT_UPLOAD_BYTES:
            warns.append(f"{up.filename}: fayl juda katta (25 MB dan oshmasin).")
            continue
        if total > MAX_IMPORT_TOTAL_BYTES:
            warns.append("Umumiy hajm 120 MB dan oshdi — qolgan fayllar olinmadi.")
            break
        pairs.append((up.filename, data))
    items, more = await asyncio.to_thread(qimport.parse_files, pairs)
    warns.extend(more)
    out = []
    for it in items:
        doc = figures_mod.sanitize_figures_doc(it.get("figure")) if it.get("figure") else {}
        out.append({"question": it["question"], "options": it["options"], "correct_index": it.get("correct_index"),
                    "explanation": it.get("explanation", ""), "figure": doc or None, "src": it.get("src", ""), "no": it.get("no", 0)})
    return JSONResponse({"ok": True, "items": out, "warnings": warns[:30],
                         "with_figures": sum(1 for o in out if o["figure"]),
                         "no_answer": sum(1 for o in out if o["correct_index"] is None)})


@app.post(f"{ADMIN_PREFIX}/api/figure/upload")
async def admin_api_figure_upload(request: Request):
    """Admin yuklagan rasm -> xavfsiz PNG -> chizma spetsifikatsiyasi."""
    _admin_api_guard(request)
    import asyncio
    import question_figures
    form = await request.form()
    up = form.get("file")
    if up is None or not getattr(up, "filename", ""):
        raise HTTPException(status_code=422, detail="Rasm tanlang.")
    data = await up.read()
    if len(data) > 8 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Rasm 8 MB dan oshmasin.")
    if up.filename.lower().endswith(".svg"):
        svg = figures_mod.sanitize_svg(data.decode("utf-8", "ignore"))
        if not svg:
            raise HTTPException(status_code=422, detail="SVG yaroqsiz yoki ruxsat etilmagan elementlar bor.")
        return JSONResponse({"ok": True, "figure": {"type": "svg", "svg": svg}})
    src = await asyncio.to_thread(question_figures.save_image_bytes, data)
    if not src:
        raise HTTPException(status_code=422, detail="Rasm formati yaroqsiz (PNG, JPG, WEBP, GIF yoki SVG).")
    return JSONResponse({"ok": True, "figure": {"type": "image", "src": src, "alt": ""}})


@app.post(f"{ADMIN_PREFIX}/api/question/{{question_id}}/active")
async def admin_api_question_active(request: Request, question_id: int):
    _admin_api_guard(request)
    body = await request.json()
    active = bool(body.get("active"))
    n = await db.admin_set_questions_active([question_id], active)
    if not n:
        raise HTTPException(status_code=404, detail="Savol topilmadi.")
    await db.log_admin_action(current_admin_username(request), "question_publish" if active else "question_unpublish", f"#{question_id}")
    return JSONResponse({"ok": True, "active": active})


@app.post(f"{ADMIN_PREFIX}/api/question/{{question_id}}/delete")
async def admin_api_question_delete(request: Request, question_id: int):
    _admin_api_guard(request)
    removed = await db.admin_delete_question(question_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Savol topilmadi.")
    await db.log_admin_action(current_admin_username(request), "question_delete", f"#{question_id}")
    return JSONResponse({"ok": True})



def _fmt_date(d) -> str:
    return d.strftime("%d.%m.%Y %H:%M") if d else ""


@app.post(f"{ADMIN_PREFIX}/import/preview", response_class=HTMLResponse)
async def admin_import_preview(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    import asyncio
    form = await request.form(max_files=60)
    mode = form.get("mode", "dtm")
    subject = form.get("subject", "auto")
    topic = (form.get("topic") or "").strip()
    pasted = (form.get("pasted") or "").strip()
    uploads = [u for u in form.getlist("file") if getattr(u, "filename", "")]

    items: list[dict] = []
    warns: list[str] = []
    if uploads:
        pairs, total = [], 0
        for up in uploads:
            data = await up.read()
            total += len(data)
            if len(data) > MAX_IMPORT_UPLOAD_BYTES:
                warns.append(f"{up.filename}: fayl juda katta (25 MB dan oshmasin).")
                continue
            if total > MAX_IMPORT_TOTAL_BYTES:
                warns.append("Umumiy hajm 120 MB dan oshdi — qolgan fayllar olinmadi.")
                break
            pairs.append((up.filename, data))
        if pairs:
            items, more = await asyncio.to_thread(qimport.parse_files, pairs)
            warns.extend(more)
    elif pasted:
        name = "joylashtirilgan.json" if pasted[:1] in "[{" else "joylashtirilgan.txt"
        items, more = await asyncio.to_thread(qimport.parse_files, [(name, pasted.encode("utf-8"))])
        warns.extend(more)
    else:
        warns.append("Fayl tanlang yoki matnni joylashtiring.")

    if mode not in IMPORT_MODES or (subject != "auto" and subject not in db.SUBJECT_CODES):
        items, warns = [], ["Fan yoki rejim noto'g'ri."]

    # --- Takrorlarni aniqlash: bazadagi barcha savollar + shu yuklashning o'zi ---
    db_index = await db.admin_question_key_index()
    seen: dict[str, dict] = {}
    for it in items:
        key = qimport.norm_key(it["question"])
        it["dup"] = None
        if key in db_index:
            info = db_index[key]
            it["dup"] = {"type": "db", "id": info["id"], "subject": db.SUBJECT_NAMES.get(info["subject"], info["subject"]),
                         "mode": info["mode"], "topic": info["topic"], "date": _fmt_date(info["date"]),
                         "src": info["src"], "no": info["no"]}
        elif key in seen:
            first = seen[key]
            it["dup"] = {"type": "file", "src": first["src"], "no": first["no"]}
        else:
            seen[key] = {"src": it.get("src", ""), "no": it.get("no", 0)}

    topics_by_subject: dict[str, list[str]] = {}
    thin = await qimport.thin_topics(mode, 15)
    fresh = [it for it in items if not it["dup"]]
    if fresh:
        matcher = await qimport.build_matcher(mode, None if subject == "auto" else [subject])
        qimport.auto_assign(fresh, matcher, subject, topic or None)
    for it in items:
        if it["dup"]:
            it.setdefault("subject", "" if subject == "auto" else subject)
            it.setdefault("topic", topic or "Umumiy")
    for sc in {it.get("subject") for it in items if it.get("subject")}:
        topics_by_subject[sc] = sorted((await db.count_questions_by_topic(sc, mode)).keys())

    stats = {
        "total": len(items),
        "new": sum(1 for it in items if not it["dup"]),
        "dup_db": sum(1 for it in items if it["dup"] and it["dup"]["type"] == "db"),
        "dup_file": sum(1 for it in items if it["dup"] and it["dup"]["type"] == "file"),
        "no_answer": sum(1 for it in items if not it["dup"] and it.get("correct_index") is None),
        "files": len({it.get("src") for it in items}),
    }
    return templates.TemplateResponse(request, "admin_import.html", {
        "subjects": db.SUBJECTS, "modes": db.TEST_MODES, "mode": mode, "thin": thin[:60], "thin_total": len(thin),
        "active_tab": "import", "preview": items, "warns": warns, "subject_sel": subject, "stats": stats,
        "topics_by_subject": topics_by_subject, "subject_names": db.SUBJECT_NAMES,
        "sources": await db.admin_import_sources(),
    })


@app.post(f"{ADMIN_PREFIX}/import/commit")
async def admin_import_commit(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form(max_fields=80000, max_files=5)
    mode = form.get("mode", "dtm")
    if mode not in IMPORT_MODES:
        mode = "dtm"
    publish = form.get("status", "published") != "private"
    try:
        count = min(int(form.get("count", 0)), qimport.MAX_ITEMS)
    except ValueError:
        count = 0
    db_index = await db.admin_question_key_index()
    ready, skipped_bad, skipped_dup = [], 0, 0
    batch_keys: set[str] = set()
    for i in range(count):
        if form.get(f"inc_{i}") != "on":
            continue
        options = [(form.get(f"opt_{i}_{k}") or "").strip() for k in range(4)]
        subj = form.get(f"subject_{i}", "")
        qtext = (form.get(f"q_{i}") or "").strip()
        try:
            ci = int(form.get(f"correct_{i}", ""))
        except ValueError:
            skipped_bad += 1
            continue
        if subj not in db.SUBJECT_CODES or not qtext or any(not o for o in options) or not 0 <= ci <= 3:
            skipped_bad += 1
            continue
        force = form.get(f"force_{i}") == "on"
        key = qimport.norm_key(qtext)
        if not force and (key in db_index or key in batch_keys):
            skipped_dup += 1
            continue
        batch_keys.add(key)
        try:
            src_no = int(form.get(f"no_{i}") or 0)
        except ValueError:
            src_no = 0
        ready.append({
            "subject": subj, "mode": mode, "topic": (form.get(f"topic_{i}") or "Umumiy").strip()[:150],
            "question": qtext[:2000], "options": options, "correct_index": ci,
            "explanation": (form.get(f"exp_{i}") or "").strip()[:2000],
            "src": (form.get(f"src_{i}") or "").strip()[:200], "no": src_no, "force": force,
        })
    result = await db.admin_bulk_create_questions(ready, mock_test="Import", is_active=publish)
    await db.log_admin_action(current_admin_username(request), "question_import",
                              f"+{len(result['added'])} ({'nashr' if publish else 'private'}), takror {skipped_dup + result['skipped']}")
    if publish and form.get("notify") == "on" and result["added"]:
        groups: dict[str, list[str]] = {}
        for it in result["added"]:
            groups.setdefault(it["subject"], []).append(it["topic"])
        for sc, topics in groups.items():
            await db.notify_question_change(sc, mode, "questions_added", topics, len(topics))
    state = "nashr qilindi" if publish else "private (qoralama) holatda saqlandi"
    msg = (f"Qo'shildi: {len(result['added'])} ({state}). Takror: {skipped_dup + result['skipped']}, "
           f"javobsiz/yaroqsiz: {skipped_bad}.")
    return RedirectResponse(f"{ADMIN_PREFIX}/import?mode={mode}&message={msg}", status_code=302)


def _safe_admin_next(value: str, fallback: str) -> str:
    return value if value.startswith(f"{ADMIN_PREFIX}/") and "//" not in value[1:] else fallback


@app.post(f"{ADMIN_PREFIX}/questions/bulk")
async def admin_questions_bulk(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form(max_fields=5000)
    action = form.get("action", "")
    ids = []
    for v in form.getlist("ids"):
        if str(v).isdigit():
            ids.append(int(v))
    nxt = _safe_admin_next(form.get("next", ""), f"{ADMIN_PREFIX}/questions")
    sep = "&" if "?" in nxt else "?"
    if not ids or action not in ("publish", "private", "delete", "move"):
        return RedirectResponse(f"{nxt}{sep}message=Savollar tanlanmadi.", status_code=302)
    if action == "move":
        n = await db.admin_move_questions(ids, str(form.get("subject_to", "")), str(form.get("mode_to", "")), str(form.get("topic_to", "")))
        await db.log_admin_action(current_admin_username(request), "question_bulk_move", f"{n} ta")
        return RedirectResponse(f"{nxt}{sep}message={n} ta savol ko'chirildi.", status_code=302)
    if action == "delete":
        n = await db.admin_delete_questions_bulk(ids)
        msg = f"{n} ta savol o'chirildi."
    else:
        n = await db.admin_set_questions_active(ids, action == "publish")
        msg = f"{n} ta savol {'nashr qilindi' if action == 'publish' else 'private qilindi'}."
    await db.log_admin_action(current_admin_username(request), f"question_bulk_{action}", f"{n} ta")
    return RedirectResponse(f"{nxt}{sep}message={msg}", status_code=302)


@app.post(f"{ADMIN_PREFIX}/questions/source-action")
async def admin_questions_source_action(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    form = await request.form()
    source = (form.get("source") or "").strip()
    action = form.get("action", "")
    if not source or action not in ("publish", "private", "delete"):
        return RedirectResponse(f"{ADMIN_PREFIX}/import?message=Noto'g'ri so'rov.", status_code=302)
    if action == "delete":
        n = await db.admin_delete_source(source)
        msg = f"«{source}» faylidan kelgan {n} ta savol o'chirildi."
    else:
        n = await db.admin_set_source_active(source, action == "publish")
        msg = f"«{source}»: {n} ta savol {'nashr qilindi' if action == 'publish' else 'private qilindi'}."
    await db.log_admin_action(current_admin_username(request), f"source_{action}", f"{source} ({n})")
    return RedirectResponse(f"{ADMIN_PREFIX}/import?message={msg}", status_code=302)


# ---------------------------------------------------------------------------
# ADMIN — berilgan sertifikatlar ro'yxati (kuzatuv/nazorat uchun)
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/certificates", response_class=HTMLResponse)
async def admin_certificates_page(request: Request, page: int = 1, q: str = ""):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    page = max(1, page)
    search = q.strip()
    total = await db.admin_count_certificates(search=search)
    total_pages = max(1, -(-total // db.ADMIN_QUESTIONS_PAGE_SIZE))
    page = min(page, total_pages)
    offset = (page - 1) * db.ADMIN_QUESTIONS_PAGE_SIZE

    certs = await db.admin_list_certificates(search=search, limit=db.ADMIN_QUESTIONS_PAGE_SIZE, offset=offset)

    return templates.TemplateResponse(request, "admin_certificates.html", {
        "certs": certs, "total": total, "total_pages": total_pages, "page": page, "search": search,
        "subject_names": db.SUBJECT_NAMES, "active_tab": "certificates",
    })


# ---------------------------------------------------------------------------
# ADMIN — amallar jurnali
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/log", response_class=HTMLResponse)
async def admin_log_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    entries = await db.get_admin_log(limit=150)
    return templates.TemplateResponse(request, "admin_log.html", {"entries": entries, "active_tab": "log"})


# ---------------------------------------------------------------------------
# ADMIN — sayt sozlamalari: tarif limitlari va sayt e'loni (announcement).
# Bu yerda o'zgartirilgan har bir narsa DARHOL, serverni qayta ishga
# tushirmasdan amal qiladi ("admin butun saytni boshqarsin" so'raganidek).
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/settings", response_class=HTMLResponse)
async def admin_settings_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    plan_limits = {p: db.get_plan_limits(p) for p in ("free", "pro", "ultra")}
    subject_breakdown = await db.admin_subject_breakdown()
    return templates.TemplateResponse(request, "admin_settings.html", {
        "plan_limits": plan_limits,
        "plan_names": db.PLAN_NAMES,
        "subject_breakdown": subject_breakdown,
        "subject_names": db.SUBJECT_NAMES,
        "admin_username": os.getenv("ADMIN_USERNAME", "admin"),
        "message": request.query_params.get("message", ""),
        "active_tab": "settings",
    })


@app.post(f"{ADMIN_PREFIX}/settings/plans")
async def admin_settings_plans_submit(
    request: Request,
    free_ai_daily: str = Form(""),
    free_full_mock: str = Form(""),
    free_topic_question_count: str = Form(""),
    free_ai_window_hours: str = Form("3"),
    pro_ai_daily: str = Form(""),
    pro_full_mock: str = Form(""),
    pro_topic_question_count: str = Form(""),
    pro_ai_window_hours: str = Form("5"),
    ultra_ai_daily: str = Form(""),
    ultra_full_mock: str = Form(""),
    ultra_topic_question_count: str = Form(""),
    ultra_ai_window_hours: str = Form("5"),
):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    overrides = {
        "free": {
            "ai_daily": free_ai_daily.strip(), "full_mock_access": free_full_mock == "on",
            "topic_question_count": free_topic_question_count.strip(), "ai_window_hours": free_ai_window_hours.strip(),
        },
        "pro": {
            "ai_daily": pro_ai_daily.strip(), "full_mock_access": pro_full_mock == "on",
            "topic_question_count": pro_topic_question_count.strip(), "ai_window_hours": pro_ai_window_hours.strip(),
        },
        "ultra": {
            "ai_daily": ultra_ai_daily.strip(), "full_mock_access": ultra_full_mock == "on",
            "topic_question_count": ultra_topic_question_count.strip(), "ai_window_hours": ultra_ai_window_hours.strip(),
        },
    }
    await db.admin_update_plan_limits(overrides)
    admin_name = current_admin_username(request)
    await db.log_admin_action(admin_name, "plan_limits_update", str(overrides))
    logger.info(f"ADMIN: tarif limitlari yangilandi -> {overrides}")
    return RedirectResponse(f"{ADMIN_PREFIX}/settings?message=Tarif+limitlari+yangilandi.", status_code=302)


# ---------------------------------------------------------------------------
# ADMIN — AI holati: kalitlar sozlanganmi, oxirgi xato nima, "Tekshirish" tugmasi
# haqiqiy so'rov yuborib har bir provayderni (Claude, Gemini, ovoz) sinaydi.
# ---------------------------------------------------------------------------

async def _probe_ai_providers() -> list[dict]:
    import asyncio
    import time

    import ai_claude
    import ai_config
    import ai_diagnostics
    import ai_gemini

    async def run(label: str, configured: bool, model: str, key: str, coro_factory, kind: str) -> dict:
        row = {"label": label, "configured": configured, "model": model, "ok": False, "detail": "", "ms": None}
        if not configured:
            row["detail"] = "Kalit .env faylida sozlanmagan."
            return row
        ai_diagnostics.clear_error(key)
        started = time.monotonic()
        try:
            result = await asyncio.wait_for(coro_factory(), timeout=20)
        except asyncio.TimeoutError:
            row["detail"] = "20 soniyada javob kelmadi (tarmoq/firewall/proxy yoki provayder sekin)."
            return row
        except Exception as exc:  # noqa: BLE001 — diagnostika uchun har qanday xatoni ko'rsatamiz
            row["detail"] = f"Xato: {exc}"
            return row
        row["ms"] = int((time.monotonic() - started) * 1000)
        if result:
            row["ok"] = True
            row["detail"] = (f"Ovoz tayyor ({len(result)} bayt)" if kind == "tts" else f"Javob: {str(result)[:80]}")
        else:
            hint = ai_diagnostics.failure_hint()
            row["detail"] = hint or "Javob bo'sh qaytdi (server logiga qarang)."
        return row

    probe = "Faqat bitta so'z bilan javob ber: salom"
    return [
        await run("Claude (Anthropic)", ai_claude.is_claude_configured(), ai_config.CLAUDE_MODEL, "claude",
                  lambda: ai_claude.ask_claude(probe, "math", "ortacha", None, "normal"), "text"),
        await run("Gemini (Google)", ai_gemini.is_gemini_configured(), ai_config.GEMINI_MODEL, "gemini",
                  lambda: ai_gemini.ask_gemini(probe, "math", "normal"), "text"),
        await run("Ovoz (edge-tts)", True, tts_module.TTS_VOICE, "tts",
                  lambda: tts_module.synthesize_speech("Salom"), "tts"),
    ]


@app.get(f"{ADMIN_PREFIX}/ai", response_class=HTMLResponse)
async def admin_ai_status_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    import ai_claude
    import ai_config
    import ai_diagnostics
    import ai_gemini
    return templates.TemplateResponse(request, "admin_ai.html", {
        "active_tab": "ai",
        "providers": [
            {"label": "Claude (Anthropic)", "configured": ai_claude.is_claude_configured(), "model": ai_config.CLAUDE_MODEL},
            {"label": "Gemini (Google)", "configured": ai_gemini.is_gemini_configured(), "model": ai_config.GEMINI_MODEL},
        ],
        "recent_hint": ai_diagnostics.failure_hint(),
        "results": None,
        "key_masks": _key_masks(),
    })


_ALLOWED_KEY_NAMES = set(db.ENV_OVERRIDE_NAMES)


def _key_masks() -> dict:
    import ai_keys
    return {n: ai_keys.mask(ai_keys.get(n)) for n in ("GEMINI_API_KEY", "ANTHROPIC_API_KEY")} | {
        "GEMINI_MODEL": ai_keys.get("GEMINI_MODEL", "gemini-flash-latest"), "CLAUDE_MODEL": ai_keys.get("CLAUDE_MODEL", "claude-sonnet-5-5")}


@app.post(f"{ADMIN_PREFIX}/api/ai/keys")
async def admin_ai_save_keys(request: Request):
    """AI kalit/modelini .env ga yozadi va darhol kuchga kiritadi (serverni qayta ishga tushirish shart emas)."""
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
    if request.headers.get("x-requested-with") != "fetch":
        raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="JSON noto'g'ri.")
    import keys_admin
    saved, notes, errors = [], [], []
    for name, value in (body or {}).items():
        if name not in _ALLOWED_KEY_NAMES or not isinstance(value, str) or not value.strip():
            continue
        res = await keys_admin.save_key(name, value)
        if res.get("ok"):
            saved.append(name)
            if res.get("warn"):
                notes.append(f"{name}: {res.get('msg')}")
        else:
            errors.append(f"{name}: {res.get('msg')}")
    await db.log_admin_action(current_admin_username(request), "ai_keys", ", ".join(saved) or "-")
    if errors and not saved:
        raise HTTPException(status_code=400, detail=" | ".join(errors))
    return {"ok": True, "saved": saved, "notes": notes, "errors": errors}


@app.post(f"{ADMIN_PREFIX}/ai/test", response_class=HTMLResponse)
async def admin_ai_test(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    import ai_claude
    import ai_config
    import ai_diagnostics
    import ai_gemini
    results = await _probe_ai_providers()
    await db.log_admin_action(current_admin_username(request), "ai_test", "; ".join(f"{r['label']}={'ok' if r['ok'] else 'fail'}" for r in results))
    return templates.TemplateResponse(request, "admin_ai.html", {
        "active_tab": "ai",
        "providers": [
            {"label": "Claude (Anthropic)", "configured": ai_claude.is_claude_configured(), "model": ai_config.CLAUDE_MODEL},
            {"label": "Gemini (Google)", "configured": ai_gemini.is_gemini_configured(), "model": ai_config.GEMINI_MODEL},
        ],
        "recent_hint": ai_diagnostics.failure_hint(),
        "results": results,
        "key_masks": _key_masks(),
    })


# ---------------------------------------------------------------------------
# ADMIN — bildirishnomalar tarixi (qo'ng'iroq menyusi). Yuqoridagi bitta
# banner'dan farqli: bu yerda admin xohlagancha e'lon yuboradi, har biri
# alohida saqlanadi, foydalanuvchi ularni ro'yxat sifatida ko'radi.
# ---------------------------------------------------------------------------

@app.get(f"{ADMIN_PREFIX}/announcements", response_class=HTMLResponse)
async def admin_announcements_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    items = await db.list_announcements_admin()
    return templates.TemplateResponse(request, "admin_announcements.html", {
        "items": items,
        "message": request.query_params.get("message", ""),
        "active_tab": "announcements",
    })


@app.post(f"{ADMIN_PREFIX}/announcements")
async def admin_announcements_create(
    request: Request, title: str = Form(""), body: str = Form(...),
):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    if not body.strip():
        return RedirectResponse(f"{ADMIN_PREFIX}/announcements?message=Matn+bo'sh+bo'lishi+mumkin+emas.", status_code=302)
    await db.create_announcement(title=title, body=body)
    admin_name = current_admin_username(request)
    await db.log_admin_action(admin_name, "announcement_created", body[:100])
    return RedirectResponse(f"{ADMIN_PREFIX}/announcements?message=Bildirishnoma+yuborildi.", status_code=302)


@app.post(f"{ADMIN_PREFIX}/announcements/{{announcement_id}}/deactivate")
async def admin_announcements_deactivate(request: Request, announcement_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    await db.deactivate_announcement(announcement_id)
    admin_name = current_admin_username(request)
    await db.log_admin_action(admin_name, "announcement_deactivated", str(announcement_id))
    return RedirectResponse(f"{ADMIN_PREFIX}/announcements?message=O'chirildi.", status_code=302)


@app.get("/api/notifications")
async def api_notifications(request: Request):
    """Qo'ng'iroq (bell) menyusi shu yerdan o'qiydi — admin BARCHAGA yuborgan
    e'lonlar VA shu foydalanuvchiga shaxsiy tegishli hodisalar (Yordam
    javobi, yangi mavzu, xush kelibsiz) BIR ro'yxatga birlashtirilgan."""
    user = await get_current_user(request)
    if user is None:
        return {"items": []}
    return {"items": await db.get_notifications_for_user(user.id)}


# ---------------------------------------------------------------------------
# YORDAM (Support) — foydalanuvchi admin'ga xabar yozadi, admin panelda
# "Xabarlar" bo'limida bildirishnoma (o'qilmaganlar soni) bilan ko'rinadi.
# ---------------------------------------------------------------------------

@app.get("/support", response_class=HTMLResponse)
async def support_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    messages = await db.get_user_support_messages(user.id)
    return templates.TemplateResponse(request, "support.html", {
        "user": user, "messages": messages,
        "sent": request.query_params.get("sent", ""),
    })


@app.post("/support", response_class=HTMLResponse)
@limiter.limit("10/minute")
async def support_submit(request: Request, subject: str = Form(""), body: str = Form(...), kind: str = Form("Savol")):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )

    clean_body = prompt_safety.sanitize_user_text(body, 2000)
    if not clean_body.strip():
        messages = await db.get_user_support_messages(user.id)
        return templates.TemplateResponse(request, "support.html", {
            "user": user, "messages": messages, "sent": "", "error": "Xabar matni bo'sh bo'lishi mumkin emas.",
        })

    kind = kind if kind in ("Savol", "Shikoyat", "Texnik xato", "To'lov", "Taklif") else "Savol"
    await db.create_support_message(user.id, f"[{kind}] " + subject.strip()[:180], clean_body)
    return RedirectResponse("/support?sent=1", status_code=302)


# ---------------------------------------------------------------------------
# ADMIN — foydalanuvchi xabarlari (Yordam bo'limidan kelgan). Har bir yangi
# xabar "o'qilmagan" holatda keladi va sidebar'dagi belgida ko'rinadi.
# ---------------------------------------------------------------------------

ADMIN_MESSAGES_PAGE_SIZE = 25


@app.get(f"{ADMIN_PREFIX}/messages", response_class=HTMLResponse)
async def admin_messages_page(request: Request, page: int = 1):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    page = max(1, page)
    total = await db.admin_count_support_messages()
    total_pages = max(1, -(-total // ADMIN_MESSAGES_PAGE_SIZE))
    page = min(page, total_pages)
    offset = (page - 1) * ADMIN_MESSAGES_PAGE_SIZE

    items = await db.admin_list_support_messages(limit=ADMIN_MESSAGES_PAGE_SIZE, offset=offset)

    return templates.TemplateResponse(request, "admin_messages.html", {
        "items": items, "total": total, "total_pages": total_pages, "page": page,
        "active_tab": "messages",
    })


@app.get(f"{ADMIN_PREFIX}/messages/{{message_id}}", response_class=HTMLResponse)
async def admin_message_detail_page(request: Request, message_id: int):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    item = await db.admin_get_support_message(message_id)
    if item is None:
        return RedirectResponse(f"{ADMIN_PREFIX}/messages", status_code=302)

    await db.mark_support_message_read(message_id)

    return templates.TemplateResponse(request, "admin_message_detail.html", {
        "item": item, "active_tab": "messages",
    })


@app.post(f"{ADMIN_PREFIX}/messages/{{message_id}}/reply")
async def admin_message_reply_submit(request: Request, message_id: int, reply: str = Form(...)):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)

    ok = await db.admin_reply_support_message(message_id, reply)
    if ok:
        admin_name = current_admin_username(request)
        await db.log_admin_action(admin_name, "message_reply", f"#{message_id}")
    return RedirectResponse(f"{ADMIN_PREFIX}/messages/{message_id}", status_code=302)


@app.get(f"{ADMIN_PREFIX}/api/messages/unread-count")
async def admin_api_messages_unread_count(request: Request):
    if not require_admin(request):
        raise HTTPException(status_code=401, detail="Admin sessiyasi topilmadi.")
    return {"count": await db.count_unread_support_messages()}


# ---------------------------------------------------------------------------
# Onboarding — fan, daraja, sertifikat turini majburiy tanlash
# ---------------------------------------------------------------------------

@app.get("/onboarding", response_class=HTMLResponse)
async def onboarding_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if user.onboarding_done:
        return RedirectResponse("/dashboard", status_code=302)
    # Fan bosh sahifada allaqachon tanlangan bo'lsa — qayta so'ramaymiz
    user = await _auto_onboard(request, user, request.query_params.get("subject", ""))
    if user.onboarding_done:
        resp = RedirectResponse("/dashboard", status_code=302)
        resp.delete_cookie(SUBJECT_COOKIE)
        return resp

    return templates.TemplateResponse(request, "onboarding.html", {
        "user": user,
        "subjects": db.SUBJECTS,
        "levels": db.LEVELS,
        "certificates": db.CERTIFICATE_TYPES,
        "error": None,
    })


@app.post("/onboarding", response_class=HTMLResponse)
async def onboarding_submit(
    request: Request,
    subject: str = Form(...),
    level: str = Form(DEFAULT_LEVEL),
    certificate_type: str = Form("dtm"),
):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )

    if subject not in db.SUBJECT_CODES or level not in db.LEVEL_CODES or certificate_type not in db.CERTIFICATE_CODES:
        return templates.TemplateResponse(request, "onboarding.html", {
            "user": user,
            "subjects": db.SUBJECTS,
            "levels": db.LEVELS,
            "certificates": db.CERTIFICATE_TYPES,
            "error": "Iltimos, barcha bosqichlarni to'g'ri tanlang.",
        })

    await db.complete_onboarding(user.id, subject, level, certificate_type)

    after = _safe_next(request.cookies.get(AFTER_ONBOARD_COOKIE, ""))
    if after:
        response = RedirectResponse(after, status_code=302)
        response.delete_cookie(AFTER_ONBOARD_COOKIE)
        return response
    intended_plan = request.cookies.get("intended_plan")
    if intended_plan in ("pro", "ultra"):
        response = RedirectResponse(f"/upgrade?plan={intended_plan}&auto=1", status_code=302)
        response.delete_cookie("intended_plan")
        return response

    return RedirectResponse("/dashboard", status_code=302)


# ---------------------------------------------------------------------------
# Dashboard (login + onboarding talab qilinadi)
# ---------------------------------------------------------------------------

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if not user.onboarding_done:
        return RedirectResponse("/onboarding", status_code=302)

    stats = await db.get_user_stats(user.id)
    try:
        dash = await db.get_dashboard_data(user)
    except Exception:
        logger.exception("dashboard ma'lumotlarini hisoblashda xato")
        dash = None
    hour = (datetime.utcnow() + timedelta(hours=5)).hour
    greeting = "Xayrli tong" if 5 <= hour < 12 else "Xayrli kun" if 12 <= hour < 18 else "Xayrli kech"
    quotes = [
        "Har kuni oz-ozdan — katta natija shundan boshlanadi.",
        "Xato — o'rganishning eng tez yo'li. Uni takrorlang va yeching.",
        "Bugungi 10 ta savol, ertangi 10 ball.",
        "Muvaffaqiyat — har kuni takrorlanadigan kichik ishlar yig'indisi.",
        "Eng yaxshi vaqt — hozir. Bitta testdan boshlang.",
        "Mavzuni tushunish yodlashdan kuchliroq.",
        "Zaif mavzuni yenggan kishi imtihonni yengadi.",
    ]
    return templates.TemplateResponse(request, "dashboard.html", {
        "user": user,
        "stats": stats,
        "d": dash,
        "greeting": greeting,
        "quote": quotes[date.today().toordinal() % len(quotes)],
        "subject_name": db.SUBJECT_NAMES.get(user.subject, user.subject),
    })


# ---------------------------------------------------------------------------
# TEST BOSHLASH — rejim tanlash (DTM / Sertifikat) va test yechish sahifasi
# ---------------------------------------------------------------------------

@app.get("/quiz", response_class=HTMLResponse)
async def quiz_select_page(request: Request):
    """
    TEST BOSHLASH — endi har safar TO'LIQ tanlov: Fan -> Daraja -> Rejim
    (DTM/Sertifikat, yoki ingliz tili uchun DTM/IELTS/CEFR). Standart
    tanlangan qiymatlar foydalanuvchining profilidagi (onboarding'dan
    qolgan yoki oxirgi ishlatgan) subject/level bo'ladi — lekin bu yerda
    ISTALGAN narsani o'zgartirish mumkin, faqat shu bitta testga tegishli
    bo'ladi (profilni butunlay o'zgartirmaydi).
    """
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if not user.onboarding_done:
        return RedirectResponse("/onboarding", status_code=302)

    # Har bir fan uchun mos rejimlar ro'yxatini oldindan hisoblab beramiz —
    # frontend JS shu jadvaldan foydalanib, fan almashganda rejimlar
    # ro'yxatini serverga qayta so'rov yubormasdan yangilaydi. MUHIM: bu
    # yerda faqat JSON-mos (set BO'LMAGAN) maydonlarni yuboramiz — TEST_MODES
    # ichidagi "subjects"/"exclude_subjects" Python set() bo'lib, ular
    # to'g'ridan-to'g'ri JSON'ga aylanmaydi.
    modes_by_subject = {
        s["code"]: [
            {
                "code": m["code"], "name": m["name"], "description": m["description"],
                "question_count": m["question_count"], "time_limit_minutes": m["time_limit_minutes"],
            }
            for m in db.get_test_modes_for_subject(s["code"])
        ]
        for s in db.SUBJECTS
    }

    return templates.TemplateResponse(request, "quiz_select.html", {
        "user": user,
        "subjects": db.SUBJECTS,
        "levels": db.LEVELS,
        "modes_by_subject": modes_by_subject,
        "default_subject": user.subject or db.SUBJECTS[0]["code"],
        "default_level": user.level or "boshlangich",
        "default_level_name": db.LEVEL_NAMES.get(user.level, "O'rtacha"),
        "full_mock_access": db.get_plan_limits(user.plan)["full_mock_access"],
    })


@app.get("/quiz/take", response_class=HTMLResponse)
async def quiz_take_page(request: Request):
    """
    Testning o'zi shu yerda o'tkaziladi — savollar JS orqali
    /api/quiz/generate'dan yuklanadi. Fan/daraja/rejim endi HAR BIR TEST
    uchun query-parametr orqali keladi (/quiz sahifasidagi tanlovdan) —
    foydalanuvchining doimiy profiliga yozilmaydi, faqat shu bitta
    urinishga tegishli bo'ladi.
    """
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if not user.onboarding_done:
        return RedirectResponse("/onboarding", status_code=302)

    subject = request.query_params.get("subject", user.subject or "english")
    if subject not in db.SUBJECT_CODES:
        subject = user.subject or "english"

    level = request.query_params.get("level", user.level or "boshlangich")
    if level not in db.LEVEL_CODES:
        level = user.level or "boshlangich"

    # Rejim shu fan uchun ruxsat etilganlar ro'yxatidan tanlanadi (masalan
    # "ielts" faqat ingliz tilida bo'ladi) — aks holda shu fan uchun mos
    # birinchi rejim (odatda "dtm") standart qilinadi.
    allowed_modes = db.get_test_modes_for_subject(subject)
    allowed_mode_codes = {m["code"] for m in allowed_modes}
    mode = request.query_params.get("mode", "dtm")
    if mode not in allowed_mode_codes:
        mode = allowed_modes[0]["code"] if allowed_modes else "dtm"
    mode_info = db.TEST_MODE_BY_CODE[mode]

    # Mavzu tanlangan bo'lsa ("mavzulashtirilgan" ro'yxatdan bosilgan
    # bo'lsa) shuni ishlatamiz, aks holda AI/statik bank o'zi mavzu tanlaydi.
    topic = request.query_params.get("topic", "") or None
    # Maxsus: "__missed__" — bu "Mavzusiz test" (xato qilingan savollarni
    # qaytadan ko'rib chiqish) rejimini bildiradi.
    missed_mode = topic == "__missed__"

    # 5-MAVZULIK ARALASH AMALIY SINOV: quiz_select.html'dan "topics=A,B,C,D,E"
    # ko'rinishida keladi — bir nechta mavzudan birgalikda savol so'raladi.
    topics_param = request.query_params.get("topics", "")
    _sep = "|" if "|" in topics_param else ","
    topics_list = [t.strip() for t in topics_param.split(_sep) if t.strip()] if topics_param else []
    practice_group = request.query_params.get("practice_group", "")
    variant = request.query_params.get("variant", "main")
    if variant not in ("main", "second"):
        variant = "main"
    checkpoint = request.query_params.get("checkpoint", "") == "1"
    drill = request.query_params.get("drill", "")[:40]
    if exam_rules.is_tiered(subject, mode):
        mode_info = db._mode_with_exam_rules(subject, mode_info)
    # v215: DTM blok mock (?block=physics,chemistry) va adaptiv test (?adaptive=1)
    block_specs = [c for c in request.query_params.get("block", "").split(",") if c in db.SUBJECT_CODES]
    block_specs = block_specs[:2] if len(block_specs) == 2 and block_specs[0] != block_specs[1] else []
    adaptive = request.query_params.get("adaptive", "") == "1" and not block_specs
    if block_specs:
        subject, mode = block_specs[0], "dtm"
        mode_info = {**db.TEST_MODE_BY_CODE["dtm"], "question_count": _f215.BLOCK_TOTAL, "time_limit_minutes": _f215.BLOCK_MINUTES}
    elif adaptive:
        mode_info = {**mode_info, "question_count": int(request.query_params.get("n", "20") or 20) if (request.query_params.get("n", "20") or "20").isdigit() else 20}

    return templates.TemplateResponse(request, "quiz_take.html", {
        "block_specs": ",".join(block_specs),
        "adaptive": adaptive,
        "user": user,
        "subject": subject,
        "subject_name": "DTM blok mock" if block_specs else db.SUBJECT_NAMES.get(subject, subject),
        "level": level,
        "mode": mode,
        "mode_info": mode_info,
        "topic": topic if not missed_mode else None,
        "topics_list": topics_list,
        "practice_group": practice_group,
        "missed_mode": missed_mode,
        "variant": variant,
        "checkpoint": checkpoint,
        "drill": drill,
        # Har bir test-urinish uchun unikal token — 10 soniyalik xotira keshi
        # va autosave shu token orqali bog'lanadi.
        "attempt_token": uuid.uuid4().hex,
    })


# ---------------------------------------------------------------------------
# Profil — statistika, diagrammalar, testlarni qayta ko'rish
# ---------------------------------------------------------------------------

@app.get("/repetitor", response_class=HTMLResponse)
async def repetitor_page(request: Request):
    """
    AI repetitor uchun ALOHIDA, TO'LIQ sahifa (kichik suzuvchi chat oynasi
    o'rniga) — katta animatsion "ovoz orbi" bilan, sahifa ochilishi bilan
    HECH NARSA so'ramasdan avtomatik suhbatni boshlaydi.

    FAQAT Pro/Ultra — AI repetitor endi Bepul tarifda mavjud emas (avval
    Bepulda ham cheklangan miqdorda ishlar edi; endi butunlay Pro/Ultra
    imtiyozi). Bepul foydalanuvchi shu sahifaga kirsa, to'g'ridan-to'g'ri
    /upgrade'ga yo'naltiriladi — bo'sh chatni ko'rsatib, keyin har bir
    xabarda bloklashdan ko'ra yaxshiroq tajriba.
    """
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if not user.onboarding_done:
        return RedirectResponse("/onboarding", status_code=302)
    if user.plan == "free":
        return RedirectResponse("/upgrade?locked=repetitor", status_code=302)

    return templates.TemplateResponse(request, "repetitor.html", {
        "user": user,
        "subject_name": db.SUBJECT_NAMES.get(user.subject, user.subject),
    })


# ---------------------------------------------------------------------------
# O'Z-O'ZIGA XIZMAT KO'RSATISH TARIQASIDA TARIFNI O'ZGARTIRISH
# ---------------------------------------------------------------------------
# MUHIM: hozircha to'lov tizimi ulanmagan ("pul so'rash yo'q" — aniq talab
# qilingan), shuning uchun "Pro/Ultra'ga o'tish" tugmasi bosilganda darhol
# tarif faollashadi (kelajakda bu yerga to'lov tekshiruvi qo'shilishi mumkin).
# Buning zarurati: ilgari "Pro'ga o'tish" havolalari doim /register?plan=...
# ga olib borar, allaqachon ro'yxatdan o'tgan (tizimga kirgan) foydalanuvchi
# uchun bu HECH NARSA qilmasdi (register sahifasi darhol /dashboard'ga
# qaytarib yuborar edi) — ya'ni "reklama" tugmasi bosilganda hech qanday
# ta'sir qilmasdi. Endi tizimga kirgan foydalanuvchi shu route orqali
# haqiqatda Pro/Ultra'ga o'tadi.
# ---------------------------------------------------------------------------
# Free foydalanuvchi biror Pro/Ultra-only sahifaga kirmoqchi bo'lib, shu
# yerga "?locked=..." bilan yo'naltirilganda ko'rsatiladigan tushuntirish
# matnlari — aks holda foydalanuvchi nega bu yerga tushib qolganini
# tushunmay qoladi (sabab ko'rsatilmasdan "tarif tanlang" sahifasiga otilib
# ketish — chalkashtiruvchi UX).
LOCKED_REASON_MESSAGES = {
    "repetitor": "AI repetitor endi faqat Pro va Ultra tarifda mavjud — davom etish uchun tarifni yangilang.",
    "mock": "To'liq (mavzusiz) mock test faqat Pro yoki Ultra tarifda mavjud.",
    "topic_pro": "Bu mavzu Pro tarifida ochiladi — davom etish uchun Pro'ga o'ting.",
    "topic_ultra": "Bu mavzu Ultra tarifida ochiladi — davom etish uchun Ultra'ga o'ting.",
    "drill_hard": "«Qiyin savollar» mashqi faqat Ultra tarifda mavjud.",
}


@app.get("/upgrade", response_class=HTMLResponse)
async def upgrade_page(request: Request, locked: str | None = None, plan: str | None = None, auto: str | None = None):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/register?plan=pro", status_code=302)
    plan_limits = {p: db.get_plan_limits(p) for p in ("free", "pro", "ultra")}
    # Ro'yxatdan o'tishda Pro/Ultra tanlangan bo'lsa, onboarding tugagach shu
    # yerga "auto=1" bilan tushadi — karta kiritish oynasi darhol ochiladi.
    auto_open_plan = plan if (auto == "1" and plan in ("pro", "ultra") and user.plan != plan) else None
    return templates.TemplateResponse(request, "upgrade.html", {
        "user": user,
        "plan_limits": plan_limits,
        "locked_message": LOCKED_REASON_MESSAGES.get(locked or ""),
        "auto_open_plan": auto_open_plan,
    })


@app.post("/upgrade", response_class=HTMLResponse)
@limiter.limit("10/minute")
async def upgrade_submit(
    request: Request,
    plan: str = Form(...),
    cf_turnstile_response: str = Form("", alias="cf-turnstile-response"),
    cf_fallback: str = Form("", alias="cf-turnstile-fallback"),
):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if turnstile.is_active_for_request(request):
        if not await turnstile.check(request, cf_turnstile_response, cf_fallback):
            return RedirectResponse(f"/upgrade?plan={plan}&auto=1&error=bot", status_code=302)
    if plan not in ("free", "pro", "ultra"):
        raise HTTPException(status_code=400, detail="Noto'g'ri tarif.")
    await db.admin_set_user_plan(user.id, plan)
    return RedirectResponse("/profile?upgraded=1", status_code=302)


@app.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    if not user.onboarding_done:
        return RedirectResponse("/onboarding", status_code=302)

    stats = await db.get_user_stats(user.id)
    history = await db.get_user_quiz_history(user.id)
    certificates = await db.get_certificates_for_user(user.id)
    usage = await db.get_ai_usage_status(user.id)
    plan_limits = {p: db.get_plan_limits(p) for p in ("free", "pro", "ultra")}

    return templates.TemplateResponse(request, "profile.html", {
        "user": user,
        "stats": stats,
        "history": history,
        "certificates": certificates,
        "usage": usage,
        "plan_limits": plan_limits,
        "subject_name": db.SUBJECT_NAMES.get(user.subject, user.subject),
        "subject_names": db.SUBJECT_NAMES,
        "subjects": db.SUBJECTS,
        "levels": db.LEVELS,
        "avatar_colors": db.AVATAR_COLORS,
    })


class ProfileUpdateRequest(BaseModel):
    first_name: str | None = Field(None, max_length=60)
    daily_goal: int | None = Field(None, ge=1, le=200)
    target_percent: int | None = Field(None, ge=10, le=100)
    avatar_color: str | None = Field(None, max_length=12)


class PasswordChangeRequest(BaseModel):
    current_password: str = Field("", max_length=128)
    new_password: str = Field(..., min_length=8, max_length=72)


class AccountDeleteRequest(BaseModel):
    password: str = Field("", max_length=128)
    confirm: str = Field(..., max_length=20)


def _require_fetch_header(request: Request) -> None:
    if request.headers.get("x-requested-with") != "fetch":
        raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")


@app.post("/api/profile/update")
@limiter.limit("30/minute")
async def api_profile_update(request: Request, body: ProfileUpdateRequest):
    user = await require_user(request)
    _require_fetch_header(request)
    if body.avatar_color is not None and body.avatar_color not in db.AVATAR_COLORS and body.avatar_color != "":
        raise HTTPException(status_code=400, detail="Noto'g'ri rang.")
    name = prompt_safety.sanitize_user_text(body.first_name, 60) if body.first_name is not None else None
    if name is not None and not name.strip():
        raise HTTPException(status_code=400, detail="Ism bo'sh bo'lmasligi kerak.")
    await db.update_user_profile(user.id, first_name=name, daily_goal=body.daily_goal,
                                 target_percent=body.target_percent, avatar_color=body.avatar_color)
    return {"ok": True}


@app.post("/api/profile/password")
@limiter.limit("5/minute")
async def api_profile_password(request: Request, body: PasswordChangeRequest):
    user = await require_user(request)
    _require_fetch_header(request)
    if not verify_password(body.current_password, user.password_hash):
        raise HTTPException(status_code=400, detail="Joriy parol noto'g'ri.")
    if body.new_password == body.current_password:
        raise HTTPException(status_code=400, detail="Yangi parol eskisidan farq qilishi kerak.")
    await db.set_user_password_hash(user.id, hash_password(body.new_password))
    return {"ok": True}


@app.get("/api/profile/export")
@limiter.limit("5/minute")
async def api_profile_export(request: Request):
    user = await require_user(request)
    data = await db.export_user_data(user.id)
    import json as _json
    return Response(
        content=_json.dumps(data, ensure_ascii=False, indent=2, default=str),
        media_type="application/json",
        headers={"Content-Disposition": 'attachment; filename="longouz_malumotlarim.json"'},
    )


@app.post("/api/profile/delete")
@limiter.limit("3/minute")
async def api_profile_delete(request: Request, body: AccountDeleteRequest):
    user = await require_user(request)
    _require_fetch_header(request)
    if body.confirm != "O'CHIRISH":
        raise HTTPException(status_code=400, detail="Tasdiqlash so'zini to'g'ri yozing.")
    if not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Parol noto'g'ri.")
    await db.delete_user_account(user.id)
    response = JSONResponse({"ok": True})
    response.delete_cookie(COOKIE_NAME)
    return response


@app.post("/profile/subject", response_class=HTMLResponse)
async def profile_change_subject(
    request: Request,
    subject: str = Form(""),
    level: str = Form(""),
):
    """Foydalanuvchi istalgan vaqtda shaxsiy kabinetida fan/darajasini o'zgartiradi."""
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )

    await db.update_user_subject_level(user.id, subject=subject or None, level=level or None)
    return RedirectResponse("/profile", status_code=302)


@app.get("/quiz/{quiz_id}/review", response_class=HTMLResponse)
async def quiz_review_page(request: Request, quiz_id: int):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )

    quiz = await db.get_quiz_by_id(quiz_id, user.id)
    if quiz is None:
        return RedirectResponse("/profile", status_code=302)

    import json as _json
    try:
        questions = _json.loads(quiz.questions_json) if quiz.questions_json else []
    except _json.JSONDecodeError:
        questions = []

    certificate = await db.get_certificate_by_quiz_log_id(quiz.id)

    return templates.TemplateResponse(request, "quiz_review.html", {
        "user": user,
        "quiz": quiz,
        "questions": questions,
        "subject_name": db.SUBJECT_NAMES.get(quiz.subject, quiz.subject),
        "certificate": certificate,
    })


def format_retry_after(seconds: int | None) -> str:
    """Sirpanuvchi oyna limiti tugaganda, keyingi bo'sh o'rin qachon
    ochilishini o'zbekcha o'qiladigan matnga aylantiradi."""
    if seconds is None:
        return "Birozdan so'ng yana urinib ko'ring."
    if seconds <= 0:
        return "Hozir qayta urinib ko'ring."
    minutes = seconds // 60
    if minutes < 1:
        return "1 daqiqadan kam vaqtdan keyin yana yozishingiz mumkin bo'ladi."
    if minutes < 60:
        return f"{minutes} daqiqadan keyin yana yozishingiz mumkin bo'ladi."
    hours = minutes // 60
    rem_minutes = minutes % 60
    if rem_minutes:
        return f"{hours} soat {rem_minutes} daqiqadan keyin yana yozishingiz mumkin bo'ladi."
    return f"{hours} soatdan keyin yana yozishingiz mumkin bo'ladi."


@app.get("/api/usage")
async def api_usage(request: Request):
    """Kabinet sahifalaridagi limit ko'rsatkichi (chat ustidagi progress-bar
    va h.k.) shu yerdan o'qiydi — hisoblagichni o'zgartirmaydi."""
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
    usage = await db.get_ai_usage_status(user.id)
    return JSONResponse(usage)


# ---------------------------------------------------------------------------
# AI repetitor — /ask (erkin savol-javob, Gemini yoki Claude'ga yo'naltiriladi)
# ---------------------------------------------------------------------------

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    # "Fikrlash darajasi" — Claude'ning o'z UI'sidagi kabi, foydalanuvchi
    # javobning chuqurligini tanlaydi. "max" faqat Pro/Ultar uchun — bepul
    # tarifda so'ralsa, pastda avtomatik "high"ga tushiriladi (xato
    # qaytarilmaydi, shunchaki jimgina cheklanadi).
    effort: str = Field("normal", pattern="^(low|normal|high|max)$")
    # "source" — bitta /api/ask endpoint IKKI TURLI suhbat sirtini
    # xizmat qiladi: "repetitor" (/repetitor sahifasidagi to'liq AI
    # repetitor, ovoz bilan) va "widget" (boshqa sahifalardagi suzuvchi
    # tezkor chat). Foydalanuvchi qat'iy talabi: ikkalasi ALOHIDA AI
    # provayderga bog'lanishi kerak — Claude FAQAT repetitorda ishlaydi,
    # widget esa doim Gemini'da qolaveradi (frontend'da owl-chat.js shuni
    # avtomatik aniqlab yuboradi).
    source: str = Field("widget", pattern="^(widget|repetitor)$")
    # Suhbat tarixi (oxirgi xabarlar) va gapirish tili — ustoz oldingi gaplarni eslab javob beradi.
    history: list[dict] = Field(default_factory=list, max_length=12)
    lang: str = Field("uz-UZ", pattern="^(uz|ru|en)-[A-Z]{2}$")
    # Repetitor sahifasida o'quvchi fanni o'zi almashtira oladi; "ielts" — IELTS speaking examiner rejimi.
    subject: str | None = Field(None, max_length=20)
    mode: str = Field("chat", pattern="^(chat|ielts)$")


@app.post("/api/ask")
@limiter.limit("20/minute")
async def api_ask(request: Request, body: AskRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    # AI REPETITOR — FAQAT Pro/Ultra. Sahifa darajasida (/repetitor) allaqachon
    # Bepul foydalanuvchini /upgrade'ga yo'naltiramiz, lekin API endpointni
    # ham alohida himoyalaymiz — to'g'ridan-to'g'ri so'rov yuborilsa ham
    # (masalan brauzer konsolidan) ishlamasligi kerak.
    if user.plan == "free":
        return JSONResponse(
            {
                "limit_reached": True,
                "used": 0, "limit": 0, "plan": "free", "window_hours": 0,
                "retry_after_seconds": None,
                "message": "AI repetitor — Pro va Ultra tarif imtiyozi. Testlar va mavzular bepul qolaveradi.",
            },
            status_code=402,
        )

    # --- TARIF LIMITI: sirpanuvchi oyna (Pro/Ultra=5 soat ichida N ta xabar) ---
    usage = await db.check_and_use_ai_message(user.id)
    if not usage["allowed"]:
        # 402 Payment Required — frontend shu holatni "limit tugadi, Pro/Ultra
        # taklif qil" ekranini ko'rsatish uchun ishlatadi (oddiy AI javobi
        # o'rniga). AI provayderlarga umuman so'rov yuborilmaydi — bu
        # kredit ham tejaydi.
        return JSONResponse(
            {
                "limit_reached": True,
                "used": usage["used"],
                "limit": usage["limit"],
                "plan": usage["plan"],
                "window_hours": usage["window_hours"],
                "retry_after_seconds": usage["retry_after_seconds"],
                "message": (
                    f"So'nggi {usage['window_hours']} soat ichidagi AI suhbat limitingiz "
                    f"({usage['limit']} ta savol) tugadi. {format_retry_after(usage['retry_after_seconds'])}"
                ),
            },
            status_code=402,
        )

    question = prompt_safety.sanitize_user_text(body.question, prompt_safety.MAX_QUESTION_LENGTH)
    if not question:
        raise HTTPException(status_code=400, detail="Savol bo'sh bo'lishi mumkin emas.")

    # "Maksimal" fikrlash darajasi faqat Pro/Ultra uchun — bepul tarif
    # buni so'rasa, jimgina "Yuqori"ga tushiriladi (frontend baribir buni
    # tugma holatida oldindan qulflab qo'yadi, lekin server ham tekshiradi).
    effort = body.effort
    if effort == "max" and user.plan == "free":
        effort = "high"

    # XAVFSIZLIK — Prompt Injection: agar savol "ko'rsatmani almashtirish"
    # urinishiga o'xshasa, buni AI'ga umuman yubormasdan, xushmuomala javob
    # qaytaramiz. Bu 100% himoya emas (izoh uchun prompt_safety.py'ga
    # qarang), lekin eng oddiy va eng ko'p uchraydigan urinishlarni ushlaydi.
    if prompt_safety.looks_like_injection(question):
        answer = (
            "Men faqat o'quv fani bo'yicha savollaringizga javob bera olaman. "
            "Iltimos, darsga oid savol bering."
        )
        await db.log_chat(user.id, "none", question, answer)
        return JSONResponse({"answer": answer, "provider": "none"})

    subject = body.subject if body.subject in db.SUBJECT_CODES else user.subject
    certificate_type, lang = user.certificate_type, body.lang
    if body.mode == "ielts":
        subject, certificate_type, lang = "english", "ielts", "en-US"
    answer, provider = await ai.ask_tutor(
        question, subject, user.level, certificate_type, effort, source=body.source,
        history=[{"role": str(h.get("role", "user"))[:12], "text": str(h.get("text", ""))[:700]} for h in body.history[-10:]],
        lang=lang,
    )
    await db.log_chat(user.id, provider, question, answer)

    return JSONResponse({"answer": answer, "provider": provider, "usage": usage, "effort": effort})


# ---------------------------------------------------------------------------
# AI test — /quiz (Claude orqali generatsiya qilinadi)
# ---------------------------------------------------------------------------

class QuizRequest(BaseModel):
    subject: str = Field(..., min_length=1, max_length=30)
    level: str = Field(..., min_length=1, max_length=20)
    topic: str | None = Field(None, max_length=200)
    topics: list[str] | None = Field(None, max_length=12)  # aralash amaliy sinov / nazorat testi mavzulari
    variant: str = "main"  # biologiya DTM: "main" (1-fan, 3.1 ball) | "second" (2-fan, 2.1 ball)
    checkpoint: bool = False  # har 10 mavzudan keyingi "xatolar ustida ishlash" testi
    drill: str = ""  # "hard" (Ultra) | "block:<kod>" | "open" (Pro/Ultra)
    count: int = Field(5, ge=1, le=50)
    mode: str = "dtm"  # "dtm" | "certificate" | "ielts" | "cefr"
    missed_mode: bool = False  # true bo'lsa — "Mavzusiz test" (xato savollar banki)
    # Har bir test-urinishni serverdagi xavfsiz sessiyaga bog'laydi (pastga
    # qarang — anti-tamper tushuntirishi uchun).
    mock_id: int = Field(0, ge=0)  # admin yaratgan MOCK variant
    attempt_token: str = Field(..., min_length=8, max_length=64)


@app.get("/api/topics")
@limiter.limit("30/minute")
async def api_topics(request: Request, subject: str, mode: str = "dtm"):
    """
    MAVZULASHTIRILGAN TEST RO'YXATI (SAT Question Bank uslubida): shu
    fan+rejim uchun barcha mavzularni, har birining progress holati bilan
    birga qaytaradi. Frontend (/quiz sahifasi) shu ro'yxatni progress-bar
    bilan ko'rsatadi va foydalanuvchi kunlik reja tartibida (1, 2, 3...)
    mavzularni tanlab boradi.
    """
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    if subject not in db.SUBJECT_CODES:
        raise HTTPException(status_code=400, detail="Noto'g'ri fan kodi.")

    allowed_modes = {m["code"] for m in db.get_test_modes_for_subject(subject)}
    if mode not in allowed_modes:
        raise HTTPException(status_code=400, detail="Bu fan uchun bunday rejim mavjud emas.")

    if exam_rules.is_tiered(subject, mode):
        return JSONResponse(await _tiered_topics_payload(user, subject, mode))

    topics = await db.list_topics_db(subject, mode)
    topic_counts = await db.count_questions_by_topic(subject, mode)
    progress_map = await db.get_topic_progress(user.id, subject, mode)
    missed_count = len(await db.get_missed_questions(user.id, subject=subject, limit=999))

    # Tarifga qarab NECHTA (birinchi) mavzu OCHIQ — qolgani "qulflangan"
    # ko'rinishda qaytariladi (frontend qulf belgisi bilan ko'rsatadi,
    # bosilsa /upgrade'ga yo'naltiradi). None = cheksiz (Ultra).
    unlock_count = db.get_topic_unlock_count(user.plan)

    topic_list = []
    for i, topic in enumerate(topics, start=1):
        pool_size = topic_counts.get(topic, 0)
        progress = progress_map.get(topic)
        solved = progress.solved_count if progress else 0
        total = max(pool_size, 1)
        topic_list.append({
            "order": i,
            "topic": topic,
            "solved": min(solved, total),
            "total": total,
            "percent": round(min(solved, total) / total * 100) if total else 0,
            "completed": bool(progress and progress.completed),
            "locked": bool(unlock_count is not None and i > unlock_count),
        })

    # 5-mavzulik aralash "amaliy sinov" kartasida nechta savol borligini
    # frontend oldindan bilishi uchun — asosiy generatsiya logikasi bilan
    # bir xil hisoblash (main.py'dagi /api/quiz/generate'ning `body.topics`
    # bo'limiga qarang).
    topic_cap = db.get_plan_limits(user.plan)["topic_question_count"]
    practice_question_count = topic_cap if topic_cap is not None else 25

    return JSONResponse({
        "subject": subject, "mode": mode,
        "topics": topic_list,
        "missed_count": missed_count,
        "practice_question_count": practice_question_count,
    })



async def _tiered_topics_payload(user, subject: str, mode: str) -> dict:
    """Sinf -> mavzu -> tarif ro'yxati (tarix va biologiya): har bir mavzu qulf holati va progressi bilan."""
    meta = await exam_db.get_topic_meta(subject, mode)
    visible = await exam_db.count_visible_by_topic(subject, mode, user.plan)
    all_counts = await db.count_questions_by_topic(subject, mode)
    progress_map = await db.get_topic_progress(user.id, subject, mode)
    missed_count = len(await db.get_missed_questions(user.id, subject=subject, limit=999))

    grades: dict[int, dict] = {}
    topics = []
    for m in meta:
        g = m["grade"]
        info = grades.setdefault(g, {"grade": g, "name": f"{g}-sinf", "total": 0, "open": 0, "topics": []})
        locked = not exam_rules.tier_allows(user.plan, m["tier"])
        info["total"] += 1
        if not locked:
            info["open"] += 1
        pool = visible.get(m["topic"], 0)
        prog = progress_map.get(m["topic"])
        solved = min(prog.solved_count if prog else 0, max(pool, 1))
        total = max(pool, 1)
        item = {
            "order": m["order"], "topic": m["topic"], "code": m["code"], "grade": g, "tier": m["tier"],
            "locked": locked, "tier_name": exam_rules.TIER_NAMES.get(m["tier"], m["tier"]),
            "solved": solved, "total": total, "bank_total": all_counts.get(m["topic"], 0),
            "percent": round(solved / total * 100) if total else 0,
            "completed": bool(prog and prog.completed and not locked),
        }
        info["topics"].append(item)
        topics.append(item)
    # har 10 mavzudan keyin (sinf ichida) nazorat testi; sinf oxirida >=5 mavzu qolsa — shu yerda ham
    for g, info in grades.items():
        lst = info["topics"]
        n = len(lst)
        marks = list(range(10, n + 1, 10))
        if n % 10 >= 5:
            marks.append(n)
        for k, end in enumerate(marks, start=1):
            group = lst[max(0, end - 10 if end % 10 == 0 else (end // 10) * 10):end]
            if not any(not t["locked"] for t in group):
                continue
            lst[end - 1]["checkpoint"] = {
                "n": k, "from": group[0]["order"], "to": group[-1]["order"],
                "topics": [t["topic"] for t in group if not t["locked"]],
                "label": f"{k}-nazorat testi: xatolar ustida ishlash",
            }
    limits = db.get_plan_limits(user.plan)
    cfg = exam_rules.tiered_config(subject, mode)
    return {
        "subject": subject, "mode": mode, "tiered": True, "plan": user.plan,
        "plan_name": exam_rules.TIER_NAMES.get(user.plan, user.plan),
        "grades": sorted(grades.values(), key=lambda x: x["grade"]),
        "topics": topics, "missed_count": missed_count,
        "full_mock_access": bool(limits["full_mock_access"]),
        "can_hard_drill": user.plan == "ultra",
        "tier_totals": exam_rules.TIER_TOPIC_TOTALS,
        "open_topics": sum(1 for t in topics if not t["locked"]),
        "total_topics": len(topics),
        "mock": {"total": cfg["total"], "time": cfg["time"]},
    }


def _public_question(q: dict) -> dict:
    """Brauzerga FAQAT savol, variantlar va ko'rinish ma'lumotlari yuboriladi (to'g'ri javobsiz)."""
    return {
        "question": q["question"], "options": q.get("options") or [], "style": q.get("style") or {},
        "figure": q.get("figure") or {}, "type": q.get("qtype") or "closed", "section": q.get("section") or "",
    }


@app.get("/api/exam-info")
@limiter.limit("60/minute")
async def api_exam_info(request: Request, subject: str, mode: str = "dtm"):
    """Rasmiy imtihon tuzilmasi va baholash jadvali (frontend "Imtihon haqida" panelida ko'rsatadi)."""
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
    cfg = exam_rules.tiered_config(subject, mode)
    if cfg is None:
        return JSONResponse({"tiered": False})
    data: dict = {"tiered": True, "name": cfg["name"], "total": cfg["total"], "time": cfg["time"]}
    if cfg.get("info"):
        data.update(cfg["info"])
        return JSONResponse(data)
    if cfg is exam_rules.HISTORY_CERT:
        data.update({
            "kind": "history_cert", "max_ball": 100,
            "blocks": [{"name": exam_rules.BLOCK_NAMES[b["code"]], "count": b["count"], "max": b["max"], "note": b["note"]}
                       for b in cfg["blocks"]],
            "ball_by_difficulty": [
                {"name": "Oson (faktga oid yopiq testlar)", "ball": 1.3},
                {"name": "O'rtacha (xronologiya va atamalar)", "ball": 2.2},
                {"name": "Qiyin (ochiq yoziladigan va me'moriy tahlillar)", "ball": 3.2},
            ],
            "levels": [{"level": r["level"], "range": r["range"], "benefit": r["specialty"]} for r in exam_rules.CERT_BENEFITS],
            "mandatory_note": exam_rules.CERT_MANDATORY_NOTE,
        })
    elif cfg is exam_rules.HISTORY_DTM:
        data.update({
            "kind": "history_dtm", "max_ball": cfg["max_ball"],
            "blocks": [{"name": exam_rules.BLOCK_NAMES[b["code"]], "count": b["count"], "max": b["max"],
                        "note": f"har biri {b['per_question']} ball · {b['minutes']} daqiqa"} for b in cfg["blocks"]],
            "levels": [{"level": r["level"], "range": r["range"], "benefit": r["specialty"]} for r in exam_rules.CERT_BENEFITS],
            "mandatory_note": exam_rules.CERT_MANDATORY_NOTE,
        })
    elif cfg is exam_rules.CHEMISTRY_DTM:
        data.update({
            "kind": "chemistry_dtm", "max_ball": cfg["max_ball"],
            "blocks": [
                {"name": "1-mutaxassislik fani", "count": 30, "max": 93.0, "note": "har biri 3.1 ball (№1–30)"},
                {"name": "2-mutaxassislik fani", "count": 30, "max": 63.0, "note": "har biri 2.1 ball (№31–60)"},
            ],
            "difficulty": [
                {"name": "I daraja (oson) — ta'rif, formula, reaksiya mahsulotlari", "count": 9},
                {"name": "II daraja (o'rta) — reaksiya tenglamalari, moslashtirish, ketma-ket o'zgarishlar", "count": 15},
                {"name": "III daraja (qiyin) — hisoblash masalalari, aralashma va eritma masalalari", "count": 6},
            ],
            "typology": "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi moslashtirish, 3 tasi ochiq (hisoblash natijasini yozish)",
        })
    else:
        data.update({
            "kind": "biology_dtm", "max_ball": cfg["max_ball"],
            "blocks": [
                {"name": "1-mutaxassislik fani", "count": 30, "max": 93.0, "note": "har biri 3.1 ball (№1–30)"},
                {"name": "2-mutaxassislik fani", "count": 30, "max": 63.0, "note": "har biri 2.1 ball (№31–60)"},
            ],
            "difficulty": [
                {"name": "I daraja (oson) — faktik ma'lumot va ta'riflar", "count": 9},
                {"name": "II daraja (o'rta) — muvofiqlashtirish, sxemalar, ko'p javobli", "count": 15},
                {"name": "III daraja (qiyin) — genetik, biokimyoviy, ekologik masalalar", "count": 6},
            ],
            "typology": "30 ta savoldan 24 tasi yopiq (A–D), 3 tasi muvofiqlashtirish, 3 tasi ochiq/mantiqiy masala",
        })
    return JSONResponse(data)


async def _tiered_generate(user, body, subject: str, level: str, mode: str, mode_info: dict, tcfg: dict):
    """Rasmiy tuzilmali fanlar (tarix, biologiya): mavzu / nazorat / maxsus mashq / to'liq imtihon."""
    plan = user.plan
    limits = db.get_plan_limits(plan)
    variant = body.variant if body.variant in ("main", "second") else "main"
    meta = {"variant": variant, "full_mock": False}
    meta_rows = await exam_db.get_topic_meta(subject, mode)
    tier_of = {m["topic"]: m["tier"] for m in meta_rows}
    allowed = [m["topic"] for m in meta_rows if exam_rules.tier_allows(plan, m["tier"])]
    topic_for_session = ""
    label = ""
    layout: dict = {}
    questions: list[dict] = []

    if body.drill:
        kind = body.drill
        if kind == "hard":
            if plan != "ultra":
                raise HTTPException(status_code=402, detail="Qiyin savollar mashqi faqat Ultra tarifda mavjud.")
            label = "Qiyin savollar mashqi"
        elif kind == "open":
            if not limits["full_mock_access"]:
                raise HTTPException(status_code=402, detail="Ochiq (yozma) savollar mashqi Pro yoki Ultra tarifda mavjud.")
            label = "Ochiq (yozma javobli) savollar mashqi"
        elif kind.startswith("block:") and kind.split(":", 1)[1] in exam_rules.BLOCK_NAMES:
            if not limits["full_mock_access"]:
                raise HTTPException(status_code=402, detail="Blok bo'yicha mashq Pro yoki Ultra tarifda mavjud.")
            label = f"Blok mashqi: {exam_rules.BLOCK_NAMES[kind.split(':', 1)[1]]}"
        else:
            raise HTTPException(status_code=400, detail="Noto'g'ri mashq turi.")
        questions = await exam_db.drill_questions(subject, mode, plan, kind, allowed, 25)
        topic_for_session = "__drill__"
    elif body.checkpoint:
        topics = [t for t in (body.topics or []) if t in allowed][:12]
        if not topics:
            raise HTTPException(status_code=404, detail="Bu oraliqda siz uchun ochiq mavzu yo'q.")
        questions, missed_n = await exam_db.checkpoint_questions(user.id, subject, mode, topics, plan)
        label = "Nazorat testi: xatolar ustida ishlash"
        meta["missed_in_test"] = missed_n
        topic_for_session = "__checkpoint__"
    elif body.topic:
        tier = tier_of.get(body.topic)
        if tier and not exam_rules.tier_allows(plan, tier):
            raise HTTPException(
                status_code=402,
                detail=f"Bu mavzu {exam_rules.TIER_NAMES.get(tier, tier)} tarifida ochiladi. Tarifni yangilang.",
            )
        count = limits["topic_question_count"] or 40
        exclude_keys = None
        progress = (await db.get_topic_progress(user.id, subject, mode)).get(body.topic)
        if progress:
            import json as _json
            try:
                exclude_keys = set(_json.loads(progress.solved_question_keys_json or "[]"))
            except _json.JSONDecodeError:
                exclude_keys = None
        questions, pool_total = await exam_db.topic_practice_questions(subject, mode, body.topic, plan, count, exclude_keys)
        meta["pool_total"] = pool_total
        topic_for_session = body.topic
        layout = await db.get_topic_layout(subject, mode, body.topic)
    else:
        if not limits["full_mock_access"]:
            raise HTTPException(
                status_code=402,
                detail="To'liq imtihon faqat Pro yoki Ultra tarifda mavjud. Mavzu bo'yicha mashqlar bepul davom etadi.",
            )
        questions = await exam_db.assemble_exam(subject, mode, plan, variant)
        meta["full_mock"] = True
        label = tcfg["name"]

    if not questions:
        raise HTTPException(status_code=404, detail="Bu bo'lim uchun savollar hali tayyorlanmagan.")

    questions = [shuffle_question_options(q) for q in questions]
    meta["label"] = label
    time_limit = mode_info["time_limit_minutes"]
    if not meta["full_mock"]:
        time_limit = max(10, round(len(questions) * 1.5))
    await db.store_quiz_session(body.attempt_token, user.id, subject, mode, questions,
                          topic=topic_for_session, level=level, meta=meta)
    return JSONResponse({
        "topic": label or body.topic, "questions": [_public_question(q) for q in questions], "mode": mode,
        "time_limit_minutes": time_limit, "layout": layout, "full_mock": meta["full_mock"],
    })


_PLAN_RANK = {"free": 0, "pro": 1, "ultra": 2}


async def _mock_generate(user, body, subject: str, level: str, mode: str, mode_info: dict):
    m = await db.get_mock(body.mock_id)
    if m is None or not m.is_active or m.subject != subject or m.mode != mode:
        raise HTTPException(status_code=404, detail="Mock topilmadi.")
    if _PLAN_RANK.get(user.plan, 0) < m.min_plan:
        raise HTTPException(status_code=402, detail="Bu mock yuqoriroq tarifda ochiladi.")
    import json as _json
    questions = await db.questions_by_ids(_json.loads(m.question_ids_json or "[]"))
    if not questions:
        raise HTTPException(status_code=404, detail="Mock savollari topilmadi.")
    questions = [shuffle_question_options(q) for q in questions]
    label = f"{m.name} — {m.variant_no}-variant"
    time_limit = m.time_minutes or db._mode_with_exam_rules(subject, mode_info).get("time_limit_minutes") or max(10, round(len(questions) * 1.5))
    await db.store_quiz_session(body.attempt_token, user.id, subject, mode, questions,
                                topic="__mock__", level=level, meta={"variant": "main", "full_mock": True, "label": label})
    return JSONResponse({"topic": label, "questions": [_public_question(q) for q in questions], "mode": mode,
                         "time_limit_minutes": time_limit, "layout": {}, "full_mock": True})


@app.get("/api/mocks")
async def api_mocks(request: Request, subject: str, mode: str):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
    import json as _json
    rank = _PLAN_RANK.get(user.plan, 0)
    return {"mocks": [{"id": m.id, "name": m.name, "variant": m.variant_no, "total": len(_json.loads(m.question_ids_json or "[]")),
                       "minutes": m.time_minutes, "locked": rank < m.min_plan, "plan": ["Free", "Pro", "Ultra"][m.min_plan]}
                      for m in await db.list_mocks(subject, mode)]}


_POSITIONAL_OPTION_RE = re.compile(
    r"(?:(?<![\w'])[A-D]\s*(?:va|и|and|,|\+|&)\s*[A-D](?![\w'])"
    r"|(?i:\b(?:hammasi|barchasi|hech\s+biri|yuqoridagi(?:lar)?|barcha\s+javob\w*|"
    r"всё\s+вышеперечисленное|все\s+вышеперечисленные|ничего\s+из\s+перечисленного|"
    r"all\s+of\s+the\s+above|none\s+of\s+the\s+above)\b))"
)


def shuffle_question_options(q: dict) -> dict:
    """
    Savol variantlarining tartibini ARALASHTIRADI va `correct_index`ni shu
    yangi tartibga mos ravishda YANGILAYDI — natijada bir xil savol har safar
    (yoki turli foydalanuvchilarda) to'g'ri javob doim bir xil pozitsiyada
    (masalan har doim "B") chiqavermaydi. Asl savol lug'ati o'zgartirilmaydi —
    yangi dict qaytariladi. To'g'ri javob matni tarkibi o'zgarmaydi, faqat
    variantlar ro'yxatidagi o'rni ixtiyoriy bo'ladi.
    """
    options = list(q.get("options") or [])
    correct_index = q.get("correct_index", 0)
    if not isinstance(correct_index, int) or not options or not (0 <= correct_index < len(options)):
        return q
    if q.get("figure") and any((q["figure"].get("o") or [])):
        return q  # chizmali variantlar tartibi o'zgarmaydi
    if any(_POSITIONAL_OPTION_RE.search(str(o)) for o in options):
        return q  # "A va B", "hammasi to'g'ri" kabi variantlar o'rniga bog'liq
    order = list(range(len(options)))
    random.shuffle(order)
    shuffled_options = [options[i] for i in order]
    new_correct_index = order.index(correct_index)
    new_q = dict(q)
    new_q["options"] = shuffled_options
    new_q["correct_index"] = new_correct_index
    return new_q


@app.post("/api/quiz/generate")
@limiter.limit("10/minute")
async def api_quiz_generate(request: Request, body: QuizRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    subject = body.subject if body.subject in db.SUBJECT_CODES else (user.subject or "english")
    level = body.level if body.level in db.LEVEL_CODES else (user.level or "boshlangich")

    allowed_modes = db.get_test_modes_for_subject(subject)
    allowed_mode_codes = {m["code"] for m in allowed_modes}
    mode = body.mode if body.mode in allowed_mode_codes else (allowed_modes[0]["code"] if allowed_modes else "dtm")
    mode_info = db.TEST_MODE_BY_CODE[mode]

    if body.mock_id:
        return await _mock_generate(user, body, subject, level, mode, mode_info)

    # --- RASMIY TUZILMALI FANLAR (tarix: sertifikat/DTM; biologiya: DTM) — alohida mantiq ---
    _tcfg = exam_rules.tiered_config(subject, mode)
    if _tcfg is not None and not body.missed_mode:
        return await _tiered_generate(user, body, subject, level, mode, db._mode_with_exam_rules(subject, mode_info), _tcfg)

    # --- TARIF CHEKLOVI: to'liq (mavzusiz, butun fan bo'yicha) MOCK test
    #     faqat Pro/Ultra uchun. "Mavzusiz test (xatolarni takrorlash)"
    #     bunga kirmaydi — u alohida, har doim BEPUL imkoniyat (pastda,
    #     missed_mode shart bilan tekshiriladi). Frontendda tugma allaqachon
    #     yashiringan/qulflangan, lekin bu yerda ham albatta tekshiramiz —
    #     to'g'ridan-to'g'ri API so'rovi bilan chetlab o'tib bo'lmasin.
    if not body.topic and not body.topics and not body.missed_mode:
        if not db.get_plan_limits(user.plan)["full_mock_access"]:
            raise HTTPException(
                status_code=402,
                detail="To'liq mock test faqat Pro yoki Ultra tarifda mavjud. Mavzu bo'yicha mashqlar bepul davom etadi.",
            )

    # --- TARIF CHEKLOVI: MAVZULAR SONI. Frontendda qulflangan mavzu allaqachon
    #     bosilmaydigan qilib ko'rsatiladi, lekin bu yerda ham albatta
    #     tekshiramiz — to'g'ridan-to'g'ri API so'rovi bilan chetlab o'tib
    #     bo'lmasin (masalan brauzer konsolidan). ---
    if body.topic and not body.missed_mode:
        unlock_count = db.get_topic_unlock_count(user.plan)
        if unlock_count is not None:
            available_topics = await db.list_topics_db(subject, mode)
            if body.topic in available_topics and available_topics.index(body.topic) >= unlock_count:
                raise HTTPException(
                    status_code=402,
                    detail="Bu mavzu yuqori tarifda ochiladi. Tarifni yangilang.",
                )

    # --- 5-MAVZULIK ARALASH AMALIY SINOV: bir nechta mavzudan aralash savol
    #     (to'liq mock EMAS — hamma tarifda BEPUL, chunki bu shunchaki
    #     o'tilgan mavzularni o'zini-o'zi sinash imkoniyati). ---
    if body.topics:
        topic_cap = db.get_plan_limits(user.plan)["topic_question_count"]
        practice_count = topic_cap if topic_cap is not None else 25
        questions = await db.get_questions_db_multi_topic(subject, mode, body.topics[:5], practice_count)
        if not questions:
            raise HTTPException(status_code=404, detail="Bu mavzular uchun savollar hali tayyorlanmagan.")
        questions = [shuffle_question_options(q) for q in questions]
        await db.store_quiz_session(
            body.attempt_token, user.id, subject, mode, questions,
            topic="Amaliy sinov (aralash mavzular)", level=level,
        )
        public_questions = [_public_question(q) for q in questions]
        return JSONResponse({
            "topic": "Amaliy sinov (aralash mavzular)", "questions": public_questions, "mode": mode,
            "time_limit_minutes": mode_info["time_limit_minutes"],
        })

    # --- "MAVZUSIZ TEST" (xato qilingan savollarni qaytadan ko'rib chiqish) ---
    if body.missed_mode:
        missed = await db.get_missed_questions(user.id, subject=subject, limit=mode_info["question_count"])
        if not missed:
            raise HTTPException(
                status_code=404,
                detail="Hozircha xato qilingan savollaringiz yo'q — ajoyib natija!",
            )
        missed = [shuffle_question_options(q) for q in missed]
        await db.store_quiz_session(body.attempt_token, user.id, subject, mode, missed, topic="__missed__", level=level)
        public_questions = [_public_question(q) for q in missed]
        return JSONResponse({
            "topic": "Mavzusiz test (xatolaringiz)", "questions": public_questions, "mode": mode,
            "time_limit_minutes": mode_info["time_limit_minutes"],
        })

    # DTM/Sertifikat rejimlari o'zining standart savollar soniga ega —
    # foydalanuvchi kamroq so'ragan bo'lsa ham, rejim standartidan oshib
    # ketmaydi (backend nazorat qiladi, faqat frontendga ishonilmaydi).
    count = max(1, min(body.count or mode_info["question_count"], mode_info["question_count"]))

    # --- TARIF FARQI: MAVZU BO'YICHA mashqda (to'liq mock EMAS) bitta
    #     urinishdagi savollar soni tarifga qarab farqlanadi — aniq
    #     so'ralganidek: Bepul kamida 10 ta, Pro kamida 20 ta (Bepulning
    #     2 baravari), Ultra — cheksiz (mavzuda mavjud BARCHA savollar).
    #     To'liq mock test (topic=None) bunga kirmaydi — u alohida,
    #     yuqorida full_mock_access orqali allaqachon nazorat qilinadi.
    if body.topic and not body.missed_mode:
        topic_cap = db.get_plan_limits(user.plan)["topic_question_count"]
        # topic_cap=None -> Ultra, cheksiz (mavzuda nechta savol bo'lsa,
        # shunchasi beriladi — xavfsizlik uchun yuqori chegara 100).
        count = topic_cap if topic_cap is not None else 100

        # "YAKUNIY TEST" — haftalik/oylik yopiq mavzular bo'yicha umumiy
        # tekshiruv — ODDIY mavzu emas, shuning uchun tarif bo'yicha
        # kesilmaydi: qaysi tarifda bo'lishidan qat'iy nazar, to'plamdagi
        # BARCHA savol (odatda 25 tagacha) beriladi.
        if await db.topic_is_final_test(subject, mode, body.topic):
            count = 25

    # Foydalanuvchi shu mavzuda ALLAQACHON TO'G'RI ishlagan savollarni
    # aniqlaymiz — static bank shularni imkon qadar chetlab o'tadi, shunda
    # bir xil savol charchatib takrorlanavermaydi (lekin agar mavzuda savol
    # kam bo'lsa, baribir to'liq to'plamdan foydalaniladi — testni bo'sh
    # qoldirmaslik ustunroq).
    exclude_keys = None
    if body.topic:
        progress_map = await db.get_topic_progress(user.id, subject, mode)
        progress = progress_map.get(body.topic)
        if progress:
            import json as _json
            try:
                exclude_keys = set(_json.loads(progress.solved_question_keys_json or "[]"))
            except _json.JSONDecodeError:
                exclude_keys = None

    questions = await ai.generate_quiz(
        subject, level, body.topic, count, user.certificate_type, mode=mode,
        exclude_keys=exclude_keys,
    )

    if questions is None:
        raise HTTPException(
            status_code=503,
            detail="AI test hozircha sozlanmagan yoki vaqtinchalik ishlamayapti.",
        )

    # Variantlar tartibini har chiqishda ARALASHTIRAMIZ — bir xil savol
    # boshqa foydalanuvchida (yoki qayta chiqqanda) to'g'ri javob doim bir xil
    # pozitsiyada bo'lib qolmasin (masalan doim "B" bo'lib ko'rinib, o'yin
    # pozitsiyasi bo'yicha "yodlab" yechilib qolmasligi uchun).
    questions = [shuffle_question_options(q) for q in questions]

    # XAVFSIZLIK: to'g'ri javoblar bilan asl savollarni SERVERDA saqlaymiz —
    # client (brauzer) esa faqat savol+variantlarni ko'radi. Shu tufayli
    # javob yuborilganda hisoblash serverning o'zida bo'ladi, client
    # "men hammasini to'g'ri topdim" deb yolg'on ayta olmaydi.
    await db.store_quiz_session(body.attempt_token, user.id, subject, mode, questions, topic=body.topic or "", level=level)

    # Brauzerga FAQAT savol va variantlar yuboriladi — to'g'ri javob va
    # izoh (correct_index/explanation) client tomonga umuman chiqarilmaydi.
    # Aks holda foydalanuvchi brauzer konsolida tarmoq javobini ochib,
    # javoblarni oldindan bilib olishi mumkin edi.
    public_questions = [_public_question(q) for q in questions]
    layout = await db.get_topic_layout(subject, mode, body.topic) if body.topic else {}

    return JSONResponse({
        "topic": body.topic, "questions": public_questions, "mode": mode,
        "time_limit_minutes": mode_info["time_limit_minutes"], "layout": layout,
    })


# ---------------------------------------------------------------------------
# 10-SONIYALIK AVTO-SAQLASH — test davomidagi javoblar shu yerda XOTIRAGA
# yoziladi (DB'ga EMAS). Frontend har 10 soniyada shu endpoint'ni chaqiradi.
# Sahifa tasodifan yopilib qolsa, keyingi ochilishda progress shu keshdan
# tiklanishi mumkin. Yakuniy /api/quiz/submit chaqirilganda kesh tozalanadi.
# ---------------------------------------------------------------------------

class QuizAutosaveRequest(BaseModel):
    attempt_token: str
    answers: dict[str, int] = {}
    current_index: int = 0
    remaining_seconds: int | None = None


@app.post("/api/quiz/autosave")
@limiter.limit("30/minute")
async def api_quiz_autosave(request: Request, body: QuizAutosaveRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    # DIQQAT: bu yerda HECH QANDAY DB yozuvi yo'q — faqat xotiradagi kesh.
    await db.autosave_progress(body.attempt_token, {
        "user_id": user.id,
        "answers": body.answers,
        "current_index": body.current_index,
        "remaining_seconds": body.remaining_seconds,
    })
    return JSONResponse({"status": "keshlandi", "ttl_seconds": db.AUTOSAVE_TTL_SECONDS})


@app.get("/api/quiz/autosave/{attempt_token}")
async def api_quiz_autosave_get(request: Request, attempt_token: str):
    """Sahifa qayta ochilganda oldingi progressni tiklash uchun."""
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    data = await db.get_autosaved_progress(attempt_token)
    if data is None or data.get("user_id") != user.id:
        return JSONResponse({"found": False})
    return JSONResponse({"found": True, **data})


class QuizSubmitRequest(BaseModel):
    topic: str | None = None
    attempt_token: str = Field(..., min_length=8, max_length=64)
    answers: dict[str, int | str] = {}
    time_spent_seconds: int = Field(0, ge=0, le=60 * 60 * 4)  # 4 soatdan oshmasin


@app.post("/api/quiz/submit")
@limiter.limit("15/minute")
async def api_quiz_submit(request: Request, body: QuizSubmitRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    # XAVFSIZLIK — ANTI-TAMPER: natija endi HECH QACHON client'dan
    # to'g'ridan-to'g'ri qabul qilinmaydi. /api/quiz/generate paytida
    # SERVERDA saqlangan asl savol-javoblar shu yerdan qayta olinadi va
    # foizlar/ball SERVERNING O'ZI hisoblaydi. Agar sessiya topilmasa
    # (masalan muddati o'tgan, yoki boshqa foydalanuvchining tokeni bilan
    # urinilgan bo'lsa), so'rov rad etiladi — soxta natija yoki sertifikat
    # olish imkoni yo'q.
    session = await db.get_quiz_session(body.attempt_token, user.id)
    if session is None:
        raise HTTPException(
            status_code=409,
            detail="Test sessiyasi topilmadi yoki muddati o'tgan. Iltimos, testni qaytadan boshlang.",
        )

    questions = session["questions"]
    mode = session["mode"]
    subject = session["subject"]
    level = session.get("level", user.level or "boshlangich")
    topic = session.get("topic") or body.topic or ""
    sess_meta = session.get("meta") or {}
    is_block = bool(sess_meta.get("block_mock"))
    tiered = exam_rules.is_tiered(subject, mode) and not is_block
    special_topic = topic in ("__missed__", "__checkpoint__", "__drill__", "__block__", "")
    total_count = len(questions)
    correct_count = 0
    answered_count = 0
    questions_with_answers = []
    graded = []

    import json as _json

    # MUHIM TARTIB: avval mavzuning umumiy savollar sonini yozamiz, SO'NGRA
    # har bir javobni qayd etamiz — aks holda "completed" holati noto'g'ri
    # hisoblanadi (solved_count >= total_questions solishtiruvi total hali
    # 0 bo'lgan paytda ishlab, mavzu hech qachon "tugallangan" bo'lib
    # ko'rinmay qolardi).
    if topic and not special_topic:
        set_total = sess_meta.get("pool_total") or total_count
        await db.set_topic_total_questions(user.id, subject, mode, topic, set_total)

    # OCHIQ javoblar: avval qoida (answer_check.py: birlik, yaxlitlash, chala yozuv, imlo), qoida "noto'g'ri" degan
    # shubhali javoblarni BITTA so'rov bilan AI (Claude/Gemini) hakamlik qiladi — admin paneldan o'chirib qo'yish mumkin.
    ai_verdict: dict[int, bool] = {}
    pending_open = []
    for _i, _q in enumerate(questions):
        if _q.get("qtype") == "open":
            _raw = body.answers.get(str(_i))
            _t = _raw.strip() if isinstance(_raw, str) else ""
            if _t and len(_t) <= 80 and not exam_rules.check_open_answer(_t, _q.get("accept") or []):
                # v229: son bilan son solishtirilgan bo'lsa (masalan 2210 va 2200) — qoida natijasi yakuniy, AI'ga yuborilmaydi
                try:
                    import answer_check as _ac
                    _acc = _q.get("accept") or []
                    if _ac.eval_expr(_t) is not None and _acc and all(_ac.eval_expr(a) is not None for a in _acc):
                        continue
                except Exception:  # noqa: BLE001
                    pass
                pending_open.append({"i": _i, "question": _q.get("question", ""), "accepted": _q.get("accept") or [], "user": _t})
    if pending_open and ai.is_any_ai_configured() and (await db.get_setting("ai_judge_open", "1")) == "1":
        try:
            ai_verdict = await ai.judge_open_answers(pending_open, subject)
        except Exception:  # noqa: BLE001
            logger.exception("AI hakamligi xato berdi — qoida natijasi qoladi")

    for idx, q in enumerate(questions):
        raw = body.answers.get(str(idx))
        if q.get("qtype") == "open":
            # OCHIQ (yozma) javob: matn normallashtirilib, qabul qilinadigan javoblar bilan solishtiriladi
            user_text = raw.strip() if isinstance(raw, str) else ""
            is_correct = exam_rules.check_open_answer(user_text, q.get("accept") or [])
            judged_ai = False
            if not is_correct and ai_verdict.get(idx):
                is_correct, judged_ai = True, True
            if user_text:
                answered_count += 1
            questions_with_answers.append({**q, "user_index": None, "user_text": user_text[:200], "is_correct": bool(is_correct),
                                           **({"judged_by": "ai"} if judged_ai else {})})
        else:
            user_idx = raw if isinstance(raw, int) and not isinstance(raw, bool) else None
            is_correct = user_idx is not None and user_idx == q.get("correct_index")
            if user_idx is not None:
                answered_count += 1
            questions_with_answers.append({**q, "user_index": user_idx, "is_correct": bool(is_correct)})
        if is_correct:
            correct_count += 1
        graded.append({"is_correct": bool(is_correct), "difficulty": q.get("difficulty"),
                       "block": q.get("block"), "section": q.get("section"), "qtype": q.get("qtype") or "closed",
                       "subject": q.get("_subject"), "coef": q.get("_coef"), "role": q.get("_role")})

        # --- MAVZULASHTIRILGAN PROGRESS + XATO SAVOLLAR BANKI ---
        # "Mavzusiz test" (xato savollarni takrorlash) rejimida ham
        # bu yozuv ishlaydi — to'g'ri javob berilsa MissedQuestion'dan
        # o'chadi, xato bo'lsa yana bir bor "missed" hisoblanadi.
        if topic == "__missed__":
            record_topic = q.get("_missed_topic", "")
        elif is_block:
            record_topic = q.get("topic", "")
        elif tiered and special_topic:
            record_topic = q.get("topic", "")  # nazorat / mashq / to'liq imtihon: har bir savol o'z mavzusiga yoziladi
        else:
            record_topic = topic
        await db.record_topic_answer(
            user_id=user.id, subject=(q.get("_subject") if is_block else subject) or subject, mode=mode, topic=record_topic,
            question_text=q.get("question", ""),
            question_json=_json.dumps(
                {k: v for k, v in q.items() if not k.startswith("_")}, ensure_ascii=False,
            ),
            is_correct=bool(is_correct),
        )

    result = _f215.score_block(graded, sess_meta.get("specs") or []) if is_block else (scoring.score_session(subject, mode, graded, sess_meta) if tiered else None)
    if result is None:
        result = scoring.score_result(mode, correct_count, total_count)
    result["answered"] = answered_count
    result["wrong"] = answered_count - correct_count
    result["skipped"] = total_count - answered_count

    log = await db.log_quiz_result(
        user_id=user.id,
        subject=subject,
        topic=sess_meta.get("label") or ("Mavzusiz test" if topic == "__missed__" else topic),
        correct_count=correct_count,
        total_count=total_count,
        questions_json=_json.dumps(questions_with_answers, ensure_ascii=False),
        mode=mode,
        time_spent_seconds=body.time_spent_seconds,
        score_label=result["label"],
        level=level,
    )
    await db.update_streak(user.id)

    # Yakuniy yozuv bazaga tushdi — endi shu urinishning xotiradagi
    # sessiyasiga (savollar + autosave keshi) ehtiyoj yo'q.
    await db.clear_quiz_session(body.attempt_token)
    await db.clear_autosaved_progress(body.attempt_token)

    certificate = None
    cert_note = ""
    _min_time = max(60, int(total_count * 10))
    if not is_block and scoring.certificate_eligible(result) and answered_count * 2 < total_count:
        cert_note = (f"Sertifikat (PDF) berilmadi: savollarning kamida yarmiga javob berish kerak "
                     f"(siz {answered_count} / {total_count} ta savolga javob berdingiz).")
    elif not is_block and scoring.certificate_eligible(result) and int(body.time_spent_seconds or 0) < _min_time:
        cert_note = "Sertifikat (PDF) berilmadi: test juda tez yakunlandi — savollar to'liq ishlanmadi."
    elif not is_block and scoring.certificate_eligible(result):
        cert = await db.create_certificate(
            user_id=user.id, subject=subject, mode=mode,
            score_label=result["label"], quiz_log_id=log.id,
            correct_count=result["correct"], total_count=result["total"],
            percent=result["percent"],
        )
        certificate = {"verification_id": cert.verification_id}

    if cert_note:
        result["certificate_note"] = cert_note
    return JSONResponse({
        "status": "saqlandi", "quiz_id": log.id, "result": result, "certificate": certificate,
    })


class EvaluateRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    answer: str = Field(..., min_length=1, max_length=4000)


@app.post("/api/evaluate")
@limiter.limit("20/minute")
async def api_evaluate(request: Request, body: EvaluateRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    question = prompt_safety.sanitize_user_text(body.question, prompt_safety.MAX_QUESTION_LENGTH)
    answer_text = prompt_safety.sanitize_user_text(body.answer, prompt_safety.MAX_ANSWER_LENGTH)

    if prompt_safety.looks_like_injection(answer_text):
        raise HTTPException(
            status_code=400,
            detail="Javobingiz noto'g'ri formatda. Iltimos, faqat savolga oid javob yozing.",
        )

    result = await ai.evaluate_free_answer(question, answer_text, user.subject, user.level)
    if result is None:
        raise HTTPException(
            status_code=503,
            detail="Baholash tizimi hozircha sozlanmagan yoki vaqtinchalik ishlamayapti.",
        )

    return JSONResponse(result)


# ---------------------------------------------------------------------------
# OVOZ (TTS) — repetitorning javobini sifatli, serverda generatsiya
# qilingan ovoz sifatida qaytaradi (batafsil izoh: tts.py). Brauzerning
# o'z ichki ovozidan farqli, bu HAR DOIM bir xil, sifatli natija beradi.
# ---------------------------------------------------------------------------

class TtsRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)
    lang: str = Field("uz", pattern="^(uz|ru|en)$")
    voice: str = Field("male", pattern="^(male|female)$")
    rate: str = Field("+0%", pattern=r"^[+-]\d{1,2}%$")


@app.post("/api/tts")
@limiter.limit("30/minute")
async def api_tts(request: Request, body: TtsRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    clean_text = prompt_safety.sanitize_user_text(body.text, tts_module.MAX_TTS_TEXT_LENGTH)
    audio_bytes = await tts_module.synthesize_speech(clean_text, lang=body.lang, voice_gender=body.voice, rate=body.rate)
    if audio_bytes is None:
        # Zaxira: server tomonida ovoz generatsiya qilinmadi (masalan internet
        # uzilishi) — frontend buni 503 sifatida ko'rib, brauzerning o'z
        # (zaxira) ovoziga avtomatik o'tadi, foydalanuvchi sezmaydi.
        raise HTTPException(status_code=503, detail="Ovoz hozircha generatsiya qilinmadi.")

    return Response(content=audio_bytes, media_type="audio/mpeg")


# ---------------------------------------------------------------------------
# IELTS/SERTIFIKAT — SPEAKING va WRITING bo'limlari.
# Faqat "english" fani, "ielts"/"cefr" rejimida ko'rinadi (quiz_select.html
# tepasidagi Savollar/Speaking/Writing tablari orqali kiriladi).
# Speaking: chat ko'rinmaydi (talab qilinganidek) — savol ovozli o'qiladi,
# javob yozib/gapirib kiritiladi, faqat YAKUNDA natija ko'rsatiladi.
# Ikkalasi ham kunlik AI limitidan foydalanadi (bir xil hisoblagich).
# ---------------------------------------------------------------------------

@app.get("/ielts/speaking", response_class=HTMLResponse)
async def ielts_speaking_topics_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    return templates.TemplateResponse(request, "ielts_speaking_topics.html", {
        "user": user, "topics": ielts_topics.SPEAKING_TOPICS, "active_tab": "quiz",
        "full_mock_access": db.get_plan_limits(user.plan)["full_mock_access"],
    })


@app.get("/ielts/speaking/{topic_id}", response_class=HTMLResponse)
async def ielts_speaking_practice_page(request: Request, topic_id: str):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    topic = ielts_topics.SPEAKING_TOPICS_BY_ID.get(topic_id)
    if topic is None:
        return RedirectResponse("/ielts/speaking", status_code=302)
    return templates.TemplateResponse(request, "ielts_speaking_practice.html", {
        "user": user, "topic": topic, "active_tab": "quiz",
    })


class SpeakingSubmitRequest(BaseModel):
    topic_id: str = Field(..., max_length=60)
    answers: list[dict] = Field(..., max_length=10)


@app.post("/api/ielts/speaking/submit")
@limiter.limit("15/minute")
async def api_ielts_speaking_submit(request: Request, body: SpeakingSubmitRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    topic = ielts_topics.SPEAKING_TOPICS_BY_ID.get(body.topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Mavzu topilmadi.")

    usage = await db.check_and_use_ai_message(user.id)
    if not usage["allowed"]:
        return JSONResponse({
            "limit_reached": True, "used": usage["used"], "limit": usage["limit"], "plan": usage["plan"],
            "window_hours": usage["window_hours"], "retry_after_seconds": usage["retry_after_seconds"],
            "message": (
                f"So'nggi {usage['window_hours']} soat ichidagi AI suhbat limitingiz "
                f"({usage['limit']} ta savol) tugadi. {format_retry_after(usage['retry_after_seconds'])}"
            ),
        }, status_code=402)

    qa_pairs = []
    for qa in body.answers[:10]:
        question = prompt_safety.sanitize_user_text(str(qa.get("question", "")), 500)
        answer = prompt_safety.sanitize_user_text(str(qa.get("answer", "")), prompt_safety.MAX_ANSWER_LENGTH)
        if prompt_safety.looks_like_injection(answer):
            raise HTTPException(status_code=400, detail="Javobingiz noto'g'ri formatda.")
        qa_pairs.append({"question": question, "answer": answer})

    result = await ai.evaluate_speaking(topic["title_uz"], qa_pairs, user.level or "ortacha")
    if result is None:
        raise HTTPException(status_code=503, detail="Baholash tizimi hozircha vaqtinchalik ishlamayapti.")

    await db.save_speaking_writing_log(
        user_id=user.id, section="speaking", topic_id=topic["id"], topic_title=topic["title_uz"],
        content=str(qa_pairs), band_score=str(result.get("band", "")), feedback=str(result.get("feedback", "")),
    )
    return JSONResponse(result)


@app.get("/ielts/writing", response_class=HTMLResponse)
async def ielts_writing_topics_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    return templates.TemplateResponse(request, "ielts_writing_topics.html", {
        "user": user, "topics": ielts_topics.WRITING_TOPICS, "active_tab": "quiz",
    })


@app.get("/ielts/writing/{topic_id}", response_class=HTMLResponse)
async def ielts_writing_practice_page(request: Request, topic_id: str):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    topic = ielts_topics.WRITING_TOPICS_BY_ID.get(topic_id)
    if topic is None:
        return RedirectResponse("/ielts/writing", status_code=302)
    return templates.TemplateResponse(request, "ielts_writing_practice.html", {
        "user": user, "topic": topic, "active_tab": "quiz",
    })


class WritingSubmitRequest(BaseModel):
    topic_id: str = Field(..., max_length=60)
    essay: str = Field(..., min_length=1, max_length=6000)


@app.post("/api/ielts/writing/submit")
@limiter.limit("15/minute")
async def api_ielts_writing_submit(request: Request, body: WritingSubmitRequest):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")

    topic = ielts_topics.WRITING_TOPICS_BY_ID.get(body.topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Mavzu topilmadi.")

    usage = await db.check_and_use_ai_message(user.id)
    if not usage["allowed"]:
        return JSONResponse({
            "limit_reached": True, "used": usage["used"], "limit": usage["limit"], "plan": usage["plan"],
            "window_hours": usage["window_hours"], "retry_after_seconds": usage["retry_after_seconds"],
            "message": (
                f"So'nggi {usage['window_hours']} soat ichidagi AI suhbat limitingiz "
                f"({usage['limit']} ta savol) tugadi. {format_retry_after(usage['retry_after_seconds'])}"
            ),
        }, status_code=402)

    essay = prompt_safety.sanitize_user_text(body.essay, 6000)
    if prompt_safety.looks_like_injection(essay):
        raise HTTPException(status_code=400, detail="Inshoyingiz noto'g'ri formatda.")
    if len(essay.split()) < 20:
        raise HTTPException(status_code=400, detail="Insho juda qisqa — kamida 20 so'z yozing.")

    result = await ai.evaluate_writing(topic["title_uz"], topic["prompt_en"], essay)
    if result is None:
        raise HTTPException(status_code=503, detail="Baholash tizimi hozircha vaqtinchalik ishlamayapti.")

    await db.save_speaking_writing_log(
        user_id=user.id, section="writing", topic_id=topic["id"], topic_title=topic["title_uz"],
        content=essay, band_score=str(result.get("band", "")), feedback=str(result.get("feedback", "")),
    )
    return JSONResponse(result)


@app.get("/ielts/history", response_class=HTMLResponse)
async def ielts_history_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    entries = await db.get_speaking_writing_history(user.id, limit=50)
    return templates.TemplateResponse(request, "ielts_history.html", {
        "user": user, "entries": entries, "active_tab": "quiz",
    })


# ---------------------------------------------------------------------------
# SERTIFIKATLAR — ko'rish (modal/viewer sahifasi), PDF yuklab olish,
# ochiq tekshirish sahifasi (QR kod shu yerga olib boradi)
# ---------------------------------------------------------------------------

@app.get("/terms", response_class=HTMLResponse)
async def terms_page(request: Request):
    return templates.TemplateResponse(request, "legal.html", {"kind": "terms", "title": "Foydalanish shartlari", "updated": "30.10.2026"})


@app.get("/privacy", response_class=HTMLResponse)
async def privacy_page(request: Request):
    return templates.TemplateResponse(request, "legal.html", {"kind": "privacy", "title": "Maxfiylik siyosati", "updated": "30.10.2026"})


@app.get("/verify", response_class=HTMLResponse)
async def verify_page(request: Request, id: str = ""):
    vid = (id or "").strip()[:80]
    if vid:
        cert = await db.get_certificate_by_verification_id(vid)
        if cert is not None:
            return RedirectResponse(f"/certificate/{vid}", status_code=302)
    return templates.TemplateResponse(request, "legal.html", {"kind": "verify", "title": "Sertifikat haqiqiyligini tekshirish", "vid": vid})


@app.get("/certificate/{verification_id}", response_class=HTMLResponse)
async def certificate_verify_page(request: Request, verification_id: str):
    """
    OCHIQ sahifa — login talab qilinmaydi. Sertifikatdagi QR kod yoki
    havola orqali kelgan har kim shu sertifikat haqiqiyligini tekshira oladi.
    """
    cert = await db.get_certificate_by_verification_id(verification_id)
    if cert is None:
        return templates.TemplateResponse(request, "certificate_verify.html", {
            "found": False, "verification_id": verification_id,
        })

    owner = await db.get_user_by_id(cert.user_id)
    current_user = await get_current_user(request)

    # Javoblar xulosasi (faqat DTM) va mavzular bo'yicha taqsimot (barcha
    # rejimlar uchun, agar savollarda "topic" bo'lsa) — quiz_log'dan olinadi.
    answer_grid = None
    topic_breakdown = None
    if cert.quiz_log_id:
        quiz_log = await db.get_quiz_by_id_any(cert.quiz_log_id)
        if quiz_log and quiz_log.questions_json:
            import json as _json
            try:
                questions_with_answers = _json.loads(quiz_log.questions_json)
                if cert.mode == "dtm":
                    answer_grid = scoring.build_answer_grid(questions_with_answers)
                topic_breakdown = scoring.build_topic_breakdown(questions_with_answers)
            except _json.JSONDecodeError:
                pass

    return templates.TemplateResponse(request, "certificate_verify.html", {
        "found": True,
        "cert": cert,
        "owner_name": (owner.first_name if owner else "") or "LongoUZ foydalanuvchisi",
        "subject_name": db.SUBJECT_NAMES.get(cert.subject, cert.subject),
        "mode_name": db.TEST_MODE_BY_CODE.get(cert.mode, {}).get("name", cert.mode),
        "answer_grid": answer_grid,
        "topic_breakdown": topic_breakdown,
        "student_id": f"LZ{cert.user_id:08d}",
        # Yuklab olish tugmasi faqat sertifikat egasiga ko'rinadi
        "is_owner": bool(current_user and current_user.id == cert.user_id),
        # Egasi bo'lsa, "Orqaga" tugmasi to'g'ridan-to'g'ri test natijasi
        # (review) sahifasiga qaytaradi — aks holda bosh sahifaga.
        "quiz_log_id": cert.quiz_log_id,
    })


def _cert_level_from_label(label: str) -> str:
    """Milliy sertifikat bahosi yorlig'idan ("B+ daraja · 61.2 / 100 ball") darajani ajratadi."""
    m = re.match(r"^(A\+|A|B\+|B|C\+|C) daraja", label or "")
    if m:
        return m.group(1)
    return "Daraja yo'q" if "daraja yo'q" in (label or "") else ""


@app.get("/certificate/{verification_id}/pdf")
async def certificate_download_pdf(request: Request, verification_id: str):
    """PDF yuklab olish — faqat sertifikat egasi (login qilingan) uchun."""
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(f"/login?next=/certificate/{verification_id}", status_code=302)

    cert = await db.get_certificate_by_verification_id(verification_id)
    if cert is None or cert.user_id != user.id:
        raise HTTPException(status_code=404, detail="Sertifikat topilmadi.")

    answer_grid = None
    topic_breakdown = None
    if cert.quiz_log_id:
        quiz_log = await db.get_quiz_by_id_any(cert.quiz_log_id)
        if quiz_log and quiz_log.questions_json:
            import json as _json
            try:
                questions_with_answers = _json.loads(quiz_log.questions_json)
                if cert.mode == "dtm":
                    answer_grid = scoring.build_answer_grid(questions_with_answers)
                topic_breakdown = scoring.build_topic_breakdown(questions_with_answers)
            except _json.JSONDecodeError:
                pass

    pdf_bytes = certificate_gen.generate_certificate_pdf(
        full_name=user.first_name or "LongoUZ foydalanuvchisi",
        subject_name=db.SUBJECT_NAMES.get(cert.subject, cert.subject),
        score_label=cert.score_label,
        mode_name=db.TEST_MODE_BY_CODE.get(cert.mode, {}).get("name", cert.mode),
        issued_date=cert.issued_at.strftime("%d.%m.%Y"),
        verification_id=cert.verification_id,
        correct_count=cert.correct_count,
        total_count=cert.total_count,
        percent=cert.percent,
        mode_code=cert.mode,
        answer_grid=answer_grid,
        topic_breakdown=topic_breakdown,
        student_id=f"LZ{cert.user_id:08d}",
        grade_override=_cert_level_from_label(cert.score_label) if cert.mode == "certificate" else "",
    )
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="LongoUZ-sertifikat-{cert.verification_id}.pdf"'},
    )


# ---------------------------------------------------------------------------
# BALANS (hamyon) — hozircha faqat vizual/demo to'ldirish oynasi. Haqiqiy
# to'lov provayderi (Click / Paynet / SQB) hali ulanmagan: "to'ldirish"
# bosilganda hech qanday real pul o'tkazilmaydi, faqat ko'rgazma uchun.
# ---------------------------------------------------------------------------

@app.get("/balance", response_class=HTMLResponse)
async def balance_page(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(
            f"/login?next={request.url.path}" + (f"?{request.url.query}" if request.url.query else ""),
            status_code=302,
        )
    history = await db.get_balance_history(user.id)
    return templates.TemplateResponse(request, "balance.html", {
        "user": user, "history": history,
    })


@app.post("/api/balance/topup")
@limiter.limit("10/minute")
async def api_balance_topup(request: Request, amount: int = Form(...), method: str = Form("click")):
    user = await get_current_user(request)
    if user is None:
        raise HTTPException(status_code=401, detail="Avval tizimga kiring.")
    if amount < 1000 or amount > 10_000_000:
        raise HTTPException(status_code=400, detail="Noto'g'ri summa.")
    if method not in ("click", "paynet", "sqb"):
        method = "click"
    # DEMO: hozircha haqiqiy to'lov provayderi ulanmagan, shuning uchun
    # kartadan real pul yechilmaydi — bu faqat ko'rgazma/vizual oqim.
    new_balance = await db.add_demo_balance(user.id, amount, method)
    return JSONResponse({"status": "ok", "balance": new_balance})


# v215: DTM blok mock, adaptiv test, analitika, yo'riqnoma (yuqoridagi barcha yordamchilar aniqlangandan keyin ulanadi)
_f215.register(app, get_current_user, templates, limiter, shuffle_question_options, _public_question)


@app.get(f"{ADMIN_PREFIX}/bank", response_class=HTMLResponse)
async def admin_bank_page(request: Request):
    if not require_admin(request):
        return RedirectResponse(f"{ADMIN_PREFIX}/login", status_code=302)
    return templates.TemplateResponse(request, "admin_bank.html", {"active_tab": "bank", "status": await _f215.bank_status()})



if __name__ == "__main__":
    import asyncio
    import re as _re
    import shutil
    import socket
    import subprocess
    import threading

    import uvicorn

    # Eslab qolish oson portlar (faqat 6 va 0 raqamlari):
    #   6060 — oddiy HTTP (kompyuter va istalgan qurilma)
    #   6600 — HTTPS (telefonda mikrofon / AI repetitor jonli suhbati uchun)
    HTTP_PORT = int(os.getenv("SERVER_PORT", "6060"))
    HTTPS_PORT = int(os.getenv("HTTPS_PORT", "6600"))
    HOST = os.getenv("SERVER_HOST", "0.0.0.0")

    def _lan_ips() -> list[str]:
        ips: set[str] = set()
        try:
            for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
                ips.add(info[4][0])
            probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            probe.connect(("8.8.8.8", 80))
            ips.add(probe.getsockname()[0])
            probe.close()
        except OSError:
            pass
        return sorted(ip for ip in ips if not ip.startswith("127."))

    https_on = os.getenv("HTTPS", "1").strip().lower() in ("1", "true", "yes", "on")
    ssl_kwargs: dict = {}
    if https_on:
        try:
            from pathlib import Path

            from https_cert import ensure_self_signed_cert

            cert_path, key_path = ensure_self_signed_cert(Path(__file__).resolve().parent / "certs", _lan_ips())
            ssl_kwargs = {"ssl_certfile": str(cert_path), "ssl_keyfile": str(key_path)}
        except Exception as exc:  # cryptography o'rnatilmagan bo'lishi mumkin
            logger.warning("HTTPS sertifikatini yaratib bo'lmadi (%s) — faqat HTTP ishlaydi.", exc)
            https_on = False

    def _start_tunnel() -> None:
        """TUNNEL=1 bo'lsa va cloudflared o'rnatilgan bo'lsa — istalgan Wi-Fi/mobil internetdan
        ochiladigan ommaviy HTTPS manzil (trycloudflare.com) yaratadi."""
        exe = shutil.which("cloudflared")
        if not exe:
            print("  [!] TUNNEL=1, lekin cloudflared topilmadi: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/")
            return
        proc = subprocess.Popen([exe, "tunnel", "--url", f"http://localhost:{HTTP_PORT}", "--no-autoupdate"],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        def _read() -> None:
            for line in proc.stdout or []:
                m = _re.search(r"https://[a-z0-9-]+\.trycloudflare\.com", line)
                if m:
                    print("\n" + "=" * 62 + f"\n  ISTALGAN INTERNETDAN (Wi-Fi / mobil): {m.group(0)}\n" + "=" * 62 + "\n")
                    break
            for _ in proc.stdout or []:
                pass
        threading.Thread(target=_read, daemon=True).start()

    print("\n" + "=" * 62)
    print("  LongoUZ serveri ishga tushmoqda")
    print(f"  Shu kompyuterda      : http://localhost:{HTTP_PORT}")
    for ip in _lan_ips():
        print(f"  Boshqa qurilma (Wi-Fi): http://{ip}:{HTTP_PORT}")
    if https_on:
        print(f"  Telefonda mikrofon   : https://<IP>:{HTTPS_PORT}  (brauzer ogohlantirsa: Davom etish)")
    print("  Barcha qurilmalarda port bir xil: 6060 (HTTP) va 6600 (HTTPS).")
    print("  Boshqa Wi-Fi yoki mobil internetdan ochish: TUNNEL=1 python main.py")
    print("=" * 62 + "\n")

    if os.getenv("TUNNEL", "0").strip().lower() in ("1", "true", "yes", "on"):
        _start_tunnel()

    async def _serve_all() -> None:
        common = dict(host=HOST, proxy_headers=True, forwarded_allow_ips="*", log_level="info")
        servers = [uvicorn.Server(uvicorn.Config(app, port=HTTP_PORT, **common))]
        if https_on:
            # Ikkinchi server ayni shu `app` ni ishlatadi; lifespan faqat birinchisida ishlaydi.
            servers.append(uvicorn.Server(uvicorn.Config(app, port=HTTPS_PORT, lifespan="off", **common, **ssl_kwargs)))
        tasks = [asyncio.create_task(sv.serve()) for sv in servers]
        try:
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        finally:
            for sv in servers:
                sv.should_exit = True
            await asyncio.gather(*tasks, return_exceptions=True)

    try:
        asyncio.run(_serve_all())
    except KeyboardInterrupt:
        pass

