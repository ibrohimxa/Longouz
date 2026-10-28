"""Vercel kirish nuqtasi — FastAPI ilovasini serverless muhitda ochadi.

MUHIM: Vercel Python runtime'da `app` nomi bilan ASGI objekti bo'lishi kerak.
staticfiles Vercel'da alohida CDN orqali yetkaziladi (vercel.json rewrites),
shuning uchun bu faylda StaticFiles mount QAYTA qilinmaydi.
"""
import os
import sys
import logging

# Loyiha ildizi (api/ dan bir daraja yuqori)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Joriy papka sifatida loyiha ildizini o'rnatamiz — templates/ va static/
# nisbiy yo'llar orqali topiladi
os.chdir(ROOT)

# Logni yoqamiz — Vercel dashboard'da ko'rinadi
logging.basicConfig(level=logging.INFO)

try:
    from main import app  # noqa: E402,F401
except Exception as exc:
    # Import xatosi bo'lsa ham Vercel funksiya ishga tushsin — debug uchun
    logging.exception("main.py import xatosi: %s", exc)
    raise
