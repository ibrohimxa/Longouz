"""Vercel kirish nuqtasi: butun FastAPI ilovasini (main.py) serverless funksiya sifatida ochadi."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
os.chdir(ROOT)

from main import app  # noqa: E402,F401  (Vercel `app` ASGI obyektini topadi)
