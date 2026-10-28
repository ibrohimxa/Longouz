"""API kalitlarini .env dan ishonchli o'qish va admin paneldan saqlash.

Muammo: kalit .env ga keyin qo'yilsa yoki fayl BOM/qo'shtirnoq bilan saqlansa,
modul importida o'qilgan bo'sh qiymat qolib ketardi. Endi kalit HAR chaqiruvda
o'qiladi, .env o'zgarsa qayta yuklanadi."""

import logging
import os
import re
from pathlib import Path

from dotenv import dotenv_values

logger = logging.getLogger(__name__)
ENV_PATH = Path(__file__).resolve().parent / ".env"
_KEY_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,60}$")
_loaded_mtime: float | None = None


def _clean(value: str | None) -> str:
    return (value or "").strip().strip('"').strip("'").strip()


def reload_env(force: bool = False) -> None:
    """.env o'zgargan bo'lsa, undagi QIYMATI BOR kalitlarni os.environ ga yozadi."""
    global _loaded_mtime
    try:
        mtime = ENV_PATH.stat().st_mtime
    except OSError:
        return
    if not force and _loaded_mtime == mtime:
        return
    try:
        values = dotenv_values(ENV_PATH, encoding="utf-8-sig")
    except Exception as exc:  # noqa: BLE001
        logger.warning(".env o'qilmadi: %s", exc)
        return
    for name, raw in values.items():
        value = _clean(raw)
        if name and value:
            os.environ[name.lstrip("﻿")] = value
    _loaded_mtime = mtime


def get(name: str, default: str = "") -> str:
    reload_env()
    return _clean(os.environ.get(name)) or default


def save(name: str, value: str) -> None:
    """Kalitni .env ga yozadi (bor qatorni almashtiradi) va darhol kuchga kiritadi."""
    if not _KEY_RE.match(name):
        raise ValueError("Noto'g'ri o'zgaruvchi nomi")
    value = _clean(value)
    if "\n" in value or "\r" in value:
        raise ValueError("Qiymatda yangi qator bo'lmasligi kerak")
    os.environ[name] = value
    try:
        lines = ENV_PATH.read_text(encoding="utf-8-sig").splitlines() if ENV_PATH.exists() else []
    except OSError:
        lines = []
    out, done = [], False
    for ln in lines:
        if ln.split("=", 1)[0].strip() == name:
            out.append(f"{name}={value}")
            done = True
        else:
            out.append(ln)
    if not done:
        out.append(f"{name}={value}")
    try:
        ENV_PATH.write_text("\n".join(out) + "\n", encoding="utf-8")
        reload_env(force=True)
    except OSError:
        # Vercel kabi faqat-o'qish fayl tizimida: qiymat bazada (SiteSetting "env:NAME") saqlanadi, main.py yozadi
        logger.info("%s .env ga yozilmadi (fayl tizimi yozishga yopiq) — bazada saqlanadi.", name)


def mask(value: str) -> str:
    return "—" if not value else (value[:4] + "…" + value[-3:] if len(value) > 10 else "•••")
