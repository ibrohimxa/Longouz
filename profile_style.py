"""v267: shaxsiy ko'rinish (profil sozlamalari) — tariflarga qarab ochiladigan imkoniyatlar.

Free  — ism, rasm, avatar rangi, tungi/kunduzgi rejim, til.
Pro   — sayt urg'u rangi (6 ta), avatar ramkasi (neon), holat/bio satri, katta shrift, to'lqin effektlarini boshqarish.
Ultra — Pro'dagi hammasi + qo'shimcha 4 ta eksklyuziv rang, jonli (aylanuvchi aurora) ramka, profil muqovasi,
        ism ustidagi neon nur, profil belgisi (emoji).
"""
from __future__ import annotations

import json
import re

PLAN_RANK = {"free": 0, "pro": 1, "ultra": 2}

# kod: (nomi, rang, to'q varianti, kerakli tarif)
ACCENTS = {
    "neon":   ("Neon yashil", "#1DEF6A", "#0BD855", "free"),
    "ocean":  ("Okean ko'k", "#3DA9FF", "#1D86E0", "pro"),
    "violet": ("Binafsha", "#A779FF", "#8B5CF6", "pro"),
    "sunset": ("Quyosh botishi", "#FF9F43", "#F57C00", "pro"),
    "rose":   ("Atirgul", "#FF5C8A", "#E63E6D", "pro"),
    "cyan":   ("Firuza", "#22E3E3", "#0FC2C2", "pro"),
    "gold":   ("Oltin", "#FFD54A", "#F2B705", "ultra"),
    "ice":    ("Muz", "#9EE7FF", "#5CC8F0", "ultra"),
    "lava":   ("Lava", "#FF4D2E", "#D9301A", "ultra"),
    "aurora": ("Aurora", "#7CFFB2", "#3DE0A0", "ultra"),
}
FRAMES = {
    "none":   ("Ramkasiz", "free"),
    "neon":   ("Neon halqa", "pro"),
    "double": ("Ikki qavat", "pro"),
    "aurora": ("Jonli aurora", "ultra"),
    "gold":   ("Oltin toj", "ultra"),
}
BANNERS = {
    "none":   ("Muqovasiz", "free", ""),
    "forest": ("Tungi o'rmon", "ultra", "linear-gradient(135deg,#052e16,#0b5d2a 45%,#16a34a)"),
    "galaxy": ("Galaktika", "ultra", "radial-gradient(120% 140% at 10% 10%,#4c1d95 0,#1e1b4b 45%,#020617 100%)"),
    "sunrise": ("Tong", "ultra", "linear-gradient(135deg,#7c2d12,#ea580c 45%,#facc15)"),
    "ocean":  ("Okean", "ultra", "linear-gradient(135deg,#082f49,#0369a1 50%,#22d3ee)"),
    "aurora": ("Aurora", "ultra", "linear-gradient(120deg,#022c22,#0f766e 30%,#7c3aed 65%,#22c55e)"),
}
BADGES = ("", "🔥", "⚡", "🎯", "🏆", "📚", "🧠", "🚀", "💎", "👑", "🦉", "⭐")
FONTS = {"normal": "free", "large": "pro"}

DEFAULTS = {"accent": "neon", "frame": "none", "bio": "", "font": "normal", "fx": True,
            "banner": "none", "glow": False, "badge": ""}


def _allowed(need: str, plan: str) -> bool:
    return PLAN_RANK.get(plan or "free", 0) >= PLAN_RANK.get(need, 0)


def load(user) -> dict:
    """Saqlangan sozlamalar + tarifga mos bo'lmaganlari standartga qaytariladi (tarif tushsa ham sayt buzilmaydi)."""
    try:
        raw = json.loads(getattr(user, "prefs", "") or "{}")
        if not isinstance(raw, dict):
            raw = {}
    except Exception:  # noqa: BLE001
        raw = {}
    p = dict(DEFAULTS)
    p.update({k: raw[k] for k in DEFAULTS if k in raw})
    plan = getattr(user, "plan", "free") or "free"
    if p["accent"] not in ACCENTS or not _allowed(ACCENTS[p["accent"]][3], plan):
        p["accent"] = "neon"
    if p["frame"] not in FRAMES or not _allowed(FRAMES[p["frame"]][1], plan):
        p["frame"] = "none"
    if p["banner"] not in BANNERS or not _allowed(BANNERS[p["banner"]][1], plan):
        p["banner"] = "none"
    if p["font"] not in FONTS or not _allowed(FONTS[p["font"]], plan):
        p["font"] = "normal"
    if not _allowed("pro", plan):
        p["bio"] = ""
        p["fx"] = True
    if not _allowed("ultra", plan):
        p["glow"] = False
        p["badge"] = ""
    p["bio"] = str(p["bio"] or "")[:80]
    p["badge"] = p["badge"] if p["badge"] in BADGES else ""
    p["fx"] = bool(p["fx"])
    p["glow"] = bool(p["glow"])
    return p


def validate(data: dict, plan: str) -> tuple[dict | None, str]:
    """Yangi qiymatlarni tekshiradi. Xato bo'lsa (None, sabab)."""
    out = {}
    if "accent" in data:
        a = str(data["accent"])
        if a not in ACCENTS:
            return None, "Noto'g'ri rang."
        if not _allowed(ACCENTS[a][3], plan):
            return None, f"Bu rang {ACCENTS[a][3].capitalize()} tarifida ochiladi."
        out["accent"] = a
    if "frame" in data:
        f = str(data["frame"])
        if f not in FRAMES:
            return None, "Noto'g'ri ramka."
        if not _allowed(FRAMES[f][1], plan):
            return None, f"Bu ramka {FRAMES[f][1].capitalize()} tarifida ochiladi."
        out["frame"] = f
    if "banner" in data:
        b = str(data["banner"])
        if b not in BANNERS:
            return None, "Noto'g'ri muqova."
        if not _allowed(BANNERS[b][1], plan):
            return None, "Profil muqovasi Ultra tarifida ochiladi."
        out["banner"] = b
    if "font" in data:
        f = str(data["font"])
        if f not in FONTS:
            return None, "Noto'g'ri shrift."
        if not _allowed(FONTS[f], plan):
            return None, "Katta shrift Pro tarifida ochiladi."
        out["font"] = f
    if "bio" in data:
        if not _allowed("pro", plan):
            return None, "Holat satri Pro tarifida ochiladi."
        bio = re.sub(r"[<>]", "", str(data["bio"] or "")).strip()[:80]
        out["bio"] = bio
    if "fx" in data:
        if not _allowed("pro", plan):
            return None, "Effektlarni boshqarish Pro tarifida ochiladi."
        out["fx"] = bool(data["fx"])
    if "glow" in data:
        if not _allowed("ultra", plan):
            return None, "Ism nuri Ultra tarifida ochiladi."
        out["glow"] = bool(data["glow"])
    if "badge" in data:
        b = str(data["badge"] or "")
        if b not in BADGES:
            return None, "Noto'g'ri belgi."
        if b and not _allowed("ultra", plan):
            return None, "Profil belgisi Ultra tarifida ochiladi."
        out["badge"] = b
    return out, ""


def css(p: dict) -> str:
    """Butun ilova sahifalariga qo'llanadigan kichik CSS (urg'u rangi, shrift)."""
    rules = []
    acc = ACCENTS.get(p.get("accent", "neon"))
    if acc and p.get("accent") != "neon":
        c, d = acc[1], acc[2]
        rules.append(f":root:root{{--accent-green:{c};--accent-green-dark:{d};--success:{c};--lz-green:{c};--lz-accent:{c}}}")
    if p.get("font") == "large":
        rules.append("html{font-size:17.5px}")
    return "".join(rules)


def options(plan: str) -> dict:
    """Profil sahifasi uchun: har bir variant va qulfi."""
    return {
        "accents": [{"code": k, "name": v[0], "color": v[1], "need": v[3], "ok": _allowed(v[3], plan)} for k, v in ACCENTS.items()],
        "frames": [{"code": k, "name": v[0], "need": v[1], "ok": _allowed(v[1], plan)} for k, v in FRAMES.items()],
        "banners": [{"code": k, "name": v[0], "need": v[1], "ok": _allowed(v[1], plan), "bg": v[2]} for k, v in BANNERS.items()],
        "badges": [b for b in BADGES if b],
        "pro": _allowed("pro", plan), "ultra": _allowed("ultra", plan),
    }


AVATAR_RE = re.compile(r"^data:image/(jpeg|png|webp);base64,[A-Za-z0-9+/=]+$")
AVATAR_MAX = 160_000
