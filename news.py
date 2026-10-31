"""LongoUZ v229 — YANGILIKLAR VA REKLAMA (rasm bilan).

Admin panel → «Yangiliklar» bo'limidan:
  - yangilik, e'lon yoki reklama (banner) qo'shiladi: sarlavha, matn, rasm, tugma havolasi;
  - rasm brauzerda o'zi kichraytiriladi (≤1280px, JPEG/WebP) va bazaga saqlanadi
    (Vercel'da fayl tizimi yozib bo'lmaydi — shuning uchun rasm bazada, alohida manzildan beriladi);
  - yozuvni vaqtincha yashirish, tepaga mahkamlash, o'chirish mumkin.
Saytda: bosh sahifa va kabinetda «Yangiliklar» kartochkalari, to'liq ro'yxat — /news sahifasida.
Ko'rishlar va bosishlar soni sanaladi (reklama samaradorligi uchun).
"""
from __future__ import annotations

import base64
import binascii
import hashlib
import json
import logging
import re
from datetime import datetime

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from sqlalchemy import Boolean, DateTime, Integer, String, Text, delete, select, update
from sqlalchemy.orm import Mapped, mapped_column

import database as db

logger = logging.getLogger("longouz.news")

KINDS = {"news": "Yangilik", "ad": "Reklama", "promo": "Aksiya", "update": "Yangilanish"}
MAX_IMAGE_BYTES = 900_000  # ~0.9 MB (brauzer rasmni oldindan siqadi)
_DATA_URL = re.compile(r"^data:(image/(?:jpeg|png|webp|gif));base64,([A-Za-z0-9+/=\s]+)$")


class NewsPost(db.Base):
    __tablename__ = "news_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kind: Mapped[str] = mapped_column(String(20), default="news", index=True)
    title: Mapped[str] = mapped_column(String(200), default="")
    body: Mapped[str] = mapped_column(Text, default="")
    image_mime: Mapped[str] = mapped_column(String(30), default="")
    image_b64: Mapped[str] = mapped_column(Text, default="")
    link_url: Mapped[str] = mapped_column(String(500), default="")
    link_label: Mapped[str] = mapped_column(String(60), default="")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    pinned: Mapped[bool] = mapped_column(Boolean, default=False)
    views: Mapped[int] = mapped_column(Integer, default=0)
    clicks: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)


def _safe_link(url: str) -> str:
    url = (url or "").strip()[:500]
    if not url:
        return ""
    if url.startswith("/") and not url.startswith("//"):
        return url
    if re.match(r"^https?://", url, re.I):
        return url
    if re.match(r"^(t\.me|www\.)", url, re.I):
        return "https://" + url
    return ""


def _public(p: NewsPost) -> dict:
    return {
        "id": p.id, "kind": p.kind, "kind_name": KINDS.get(p.kind, "Yangilik"), "title": p.title, "body": p.body,
        "image": (f"/news/img/{p.id}?v={hashlib.md5((p.image_b64 or '')[:200].encode()).hexdigest()[:8]}" if p.image_b64 else ""),
        "link_url": p.link_url, "link_label": p.link_label or ("Batafsil" if p.link_url else ""),
        "pinned": bool(p.pinned), "date": p.created_at.strftime("%d.%m.%Y") if p.created_at else "",
    }


async def list_posts(active_only: bool = True, limit: int = 30) -> list[dict]:
    try:
        async with db.async_session() as s:
            q = select(NewsPost)
            if active_only:
                q = q.where(NewsPost.is_active == True)  # noqa: E712
            q = q.order_by(NewsPost.pinned.desc(), NewsPost.created_at.desc()).limit(limit)
            rows = (await s.execute(q)).scalars().all()
        return [_public(r) | ({"is_active": r.is_active, "views": r.views, "clicks": r.clicks} if not active_only else {}) for r in rows]
    except Exception:  # noqa: BLE001 — jadval hali yaratilmagan bo'lsa ham sayt ishlayversin
        logger.debug("yangiliklar o'qilmadi", exc_info=True)
        return []


def register(app, prefix: str, require_admin, templates) -> None:
    # ------------------------------------------------------------------ OMMAVIY
    @app.get("/api/news")
    async def api_news(limit: int = 6):
        items = await list_posts(True, max(1, min(int(limit or 6), 30)))
        return JSONResponse({"items": items}, headers={"Cache-Control": "public, max-age=60"})

    @app.get("/news/img/{post_id}")
    async def news_image(post_id: int, request: Request):
        async with db.async_session() as s:
            p = await s.get(NewsPost, post_id)
        if p is None or not p.image_b64:
            raise HTTPException(status_code=404, detail="Rasm topilmadi.")
        etag = '"' + hashlib.md5(p.image_b64[:4000].encode()).hexdigest() + '"'
        if request.headers.get("if-none-match") == etag:
            return Response(status_code=304, headers={"ETag": etag})
        try:
            data = base64.b64decode(p.image_b64)
        except (binascii.Error, ValueError):
            raise HTTPException(status_code=404, detail="Rasm buzilgan.")
        return Response(content=data, media_type=p.image_mime or "image/jpeg",
                        headers={"Cache-Control": "public, max-age=604800, immutable", "ETag": etag})

    @app.post("/api/news/{post_id}/seen")
    async def news_seen(post_id: int, request: Request):
        kind = "clicks" if request.query_params.get("click") == "1" else "views"
        try:
            async with db.async_session() as s:
                await s.execute(update(NewsPost).where(NewsPost.id == post_id).values({kind: getattr(NewsPost, kind) + 1}))
                await s.commit()
        except Exception:  # noqa: BLE001
            pass
        return JSONResponse({"ok": True})

    @app.get("/news", response_class=HTMLResponse)
    async def news_page(request: Request):
        return templates.TemplateResponse(request, "news.html", {"items": await list_posts(True, 50)})

    # ------------------------------------------------------------------ ADMIN
    def guard(request: Request):
        if not require_admin(request):
            raise HTTPException(status_code=401, detail="Admin sifatida kiring.")
        if request.headers.get("x-requested-with") != "fetch":
            raise HTTPException(status_code=400, detail="Noto'g'ri so'rov.")

    @app.get(f"{prefix}/news", response_class=HTMLResponse)
    async def admin_news_page(request: Request):
        if not require_admin(request):
            return RedirectResponse(f"{prefix}/login", status_code=302)
        return templates.TemplateResponse(request, "admin_news.html", {
            "active_tab": "news", "items": await list_posts(False, 100), "kinds": KINDS,
        })

    @app.post(f"{prefix}/api/news")
    async def admin_news_save(request: Request):
        guard(request)
        b = await request.json()
        title = str(b.get("title") or "").strip()[:200]
        body = str(b.get("body") or "").strip()[:4000]
        if not title and not body:
            raise HTTPException(status_code=422, detail="Sarlavha yoki matn yozing.")
        kind = b.get("kind") if b.get("kind") in KINDS else "news"
        mime, b64 = "", ""
        img = str(b.get("image") or "")
        if img:
            m = _DATA_URL.match(img.strip())
            if not m:
                raise HTTPException(status_code=422, detail="Rasm formati JPG, PNG, WebP yoki GIF bo'lsin.")
            mime, b64 = m.group(1), re.sub(r"\s+", "", m.group(2))
            if len(b64) * 3 // 4 > MAX_IMAGE_BYTES:
                raise HTTPException(status_code=413, detail="Rasm juda katta (0,9 MB dan oshmasin).")
        pid = int(b.get("id") or 0)
        async with db.async_session() as s:
            if pid:
                p = await s.get(NewsPost, pid)
                if p is None:
                    raise HTTPException(status_code=404, detail="Yozuv topilmadi.")
            else:
                p = NewsPost()
                s.add(p)
            p.kind, p.title, p.body = kind, title, body
            p.link_url, p.link_label = _safe_link(str(b.get("link_url") or "")), str(b.get("link_label") or "").strip()[:60]
            p.pinned = bool(b.get("pinned"))
            p.is_active = bool(b.get("is_active", True))
            if b64:
                p.image_mime, p.image_b64 = mime, b64
            elif b.get("remove_image"):
                p.image_mime, p.image_b64 = "", ""
            await s.commit()
            pid = p.id
        try:
            await db.log_admin_action("admin", "news_saved", f"#{pid} {title[:80]}")
        except Exception:  # noqa: BLE001
            pass
        return JSONResponse({"ok": True, "id": pid})

    @app.post(f"{prefix}/api/news/{{post_id}}/toggle")
    async def admin_news_toggle(post_id: int, request: Request):
        guard(request)
        b = await request.json()
        field = "pinned" if b.get("field") == "pinned" else "is_active"
        async with db.async_session() as s:
            p = await s.get(NewsPost, post_id)
            if p is None:
                raise HTTPException(status_code=404, detail="Yozuv topilmadi.")
            setattr(p, field, not getattr(p, field))
            await s.commit()
            val = getattr(p, field)
        return JSONResponse({"ok": True, field: val})

    @app.post(f"{prefix}/api/news/{{post_id}}/delete")
    async def admin_news_delete(post_id: int, request: Request):
        guard(request)
        async with db.async_session() as s:
            await s.execute(delete(NewsPost).where(NewsPost.id == post_id))
            await s.commit()
        try:
            await db.log_admin_action("admin", "news_deleted", f"#{post_id}")
        except Exception:  # noqa: BLE001
            pass
        return JSONResponse({"ok": True})
