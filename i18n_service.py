"""v267: SAYT TILLARI — tarjima xizmati.

Brauzer (static/i18n.js) sahifadagi matnni avval tayyor lug'at (static/i18n/<til>.js) bilan tarjima qiladi.
Lug'atda yo'q matnlar (yangi savollar, bildirishnomalar, kamdan-kam xabarlar) shu yerga yuboriladi:
avval bazadagi keshdan qidiriladi, topilmasa Gemini bilan tarjima qilinib, keshga yoziladi — keyingi
foydalanuvchilarga darhol beriladi. Admin panel tarjima qilinmaydi.
"""
from __future__ import annotations

import hashlib
import json
import logging
import re
import time
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, select
from sqlalchemy.orm import Mapped, mapped_column

import database as db

logger = logging.getLogger("longouz.i18n")

LANGS = ("uz", "uzc", "en", "ru", "tr")
AI_LANGS = {"en": "English", "ru": "Russian", "tr": "Turkish"}
LANG_COOKIE = "lz_lang"


class I18nCache(db.Base):
    __tablename__ = "i18n_cache"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lang: Mapped[str] = mapped_column(String(5), index=True)
    src_hash: Mapped[str] = mapped_column(String(40), index=True)
    src: Mapped[str] = mapped_column(Text, default="")
    dst: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


def lang_of(request) -> str:
    v = (request.cookies.get(LANG_COOKIE) or "uz").strip()
    return v if v in LANGS else "uz"


def _h(lang: str, s: str) -> str:
    return hashlib.sha1(f"{lang}\x00{s}".encode("utf-8")).hexdigest()


_MEM: dict[str, str] = {}
_DAY = {"d": "", "calls": 0}
DAILY_AI_CALLS = 2500
_PH = re.compile(r"\{\d+\}")

_SYSTEM = (
    "You are a professional UI and education-content translator for LongoUz, an Uzbek exam-preparation website "
    "(DTM university entrance tests, national certificate, IELTS). Translate each Uzbek (Latin script) string to {lang}. "
    "Rules: keep the meaning exact and natural for a website; keep placeholders like {{0}} {{1}} exactly; keep numbers, "
    "math expressions, formulas, chemical formulas, units and punctuation; do not translate brand names (LongoUz, LongoAI, "
    "Pro, Ultra, Free, IELTS, SAT, DTM, Gemini, Google, Telegram, Click, Payme, UzCard, Humo); 'DTM' may stay as is; "
    "'Milliy sertifikat' = national certificate; 'ball' = score points; 'so'm' = UZS (keep 'so'm' in Turkish/English as 'UZS'). "
    "Return ONLY a JSON object mapping the given index (as string) to the translation."
)


async def _ai_translate(lang: str, items: list[str]) -> dict[str, str]:
    import ai_gemini
    import ai_keys
    if lang not in AI_LANGS or not items or not ai_gemini.is_gemini_configured():
        return {}
    today = datetime.utcnow().strftime("%Y-%m-%d")
    if _DAY["d"] != today:
        _DAY.update(d=today, calls=0)
    if _DAY["calls"] >= DAILY_AI_CALLS:
        return {}
    _DAY["calls"] += 1
    payload = json.dumps({str(i): s for i, s in enumerate(items)}, ensure_ascii=False)
    try:
        resp = await ai_gemini._call_gemini_with_retry(
            model=ai_keys.get("GEMINI_MODEL", ai_gemini.GEMINI_MODEL),
            contents=payload,
            config={"system_instruction": _SYSTEM.format(lang=AI_LANGS[lang]), "max_output_tokens": 8000,
                    "response_mime_type": "application/json", "thinking_config": {"thinking_level": "low"},
                    "automatic_function_calling": ai_gemini._NO_AFC_CONFIG},
        )
        data = json.loads(ai_gemini._strip_json_fence(resp.text or "{}"))
    except Exception as e:  # noqa: BLE001
        logger.warning("Tarjima (Gemini) ishlamadi: %s", e)
        return {}
    out: dict[str, str] = {}
    for i, s in enumerate(items):
        t = data.get(str(i)) if isinstance(data, dict) else None
        if isinstance(t, str) and t.strip():
            # joy belgilari ({0}) yo'qolmasin
            if sorted(_PH.findall(s)) == sorted(_PH.findall(t)):
                out[s] = t.strip()
    return out


async def translate(lang: str, items: list[str]) -> dict[str, str]:
    if lang not in AI_LANGS:
        return {}
    items = [s for s in dict.fromkeys(items) if isinstance(s, str) and 1 < len(s) <= 2000][:60]
    result: dict[str, str] = {}
    need = []
    for s in items:
        k = _h(lang, s)
        if k in _MEM:
            result[s] = _MEM[k]
        else:
            need.append(s)
    if need:
        hashes = {_h(lang, s): s for s in need}
        try:
            async with db.async_session() as session:
                rows = (await session.execute(select(I18nCache.src_hash, I18nCache.dst)
                                              .where(I18nCache.src_hash.in_(list(hashes))))).all()
            for h, dst in rows:
                s = hashes.get(h)
                if s is not None and dst:
                    result[s] = dst
                    _MEM[h] = dst
        except Exception:  # noqa: BLE001
            logger.exception("i18n kesh o'qilmadi")
        missing = [s for s in need if s not in result]
        for i in range(0, len(missing), 30):
            part = missing[i:i + 30]
            got = await _ai_translate(lang, part)
            if not got:
                continue
            result.update(got)
            try:
                async with db.async_session() as session:
                    for s, t in got.items():
                        session.add(I18nCache(lang=lang, src_hash=_h(lang, s), src=s, dst=t))
                        _MEM[_h(lang, s)] = t
                    await session.commit()
            except Exception:  # noqa: BLE001
                logger.exception("i18n kesh yozilmadi")
    return result


def head_tags(version: str) -> bytes:
    """Har bir ommaviy sahifa <head> boshiga qo'shiladi. HTML barcha tillar uchun BIR XIL (kesh xavfsiz):
    tanlangan til cookie'dan brauzerda o'qiladi va lug'at sinxron yuklanadi."""
    return (
        "<script>(function(){var m=document.cookie.match(/(?:^|; )lz_lang=(\\w+)/),l=m&&m[1];"
        "if(l&&l!=='uz'&&/^(uzc|en|ru|tr)$/.test(l)){document.write('<script src=\"/static/i18n/'+(l==='uzc'?'en':l)+'.js?v=" + version + "\"><\\/script>')}})()</script>"
        f'<script src="/static/i18n.js?v={version}"></script>'
    ).encode()


_STARTED = time.time()
