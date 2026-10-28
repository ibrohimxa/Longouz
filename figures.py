"""Savol chizmalari (Dekart koordinatalari, geometrik shakllar, rasm, SVG) — tekshirish va tozalash.

Format (figure.js bilan bir xil):
  {"type": "plane", "xmin": -6, "xmax": 6, "ymin": -6, "ymax": 6, "axes": true, "grid": true,
   "items": [{"k": "pt", "x": 1, "y": 2, "l": "A"}, {"k": "line", "x1":0,"y1":0,"x2":3,"y2":4, "dash":false, "arrow":false, "l":""},
             {"k": "circle", "cx":0,"cy":0,"r":3,"fill":false}, {"k": "poly", "pts": [[0,0],[3,0],[0,4]], "fill": true},
             {"k": "text", "x":1,"y":1,"t":"S=12"}, {"k": "fn", "f": "x^2-2"}, {"k": "arc", "cx":0,"cy":0,"r":1,"a1":0,"a2":90}]}
  {"type": "image", "src": "/static/qfig/<hash>.png", "alt": ""}
  {"type": "svg", "svg": "<svg ...>...</svg>"}
Savol hujjati: {"q": <figure|null>, "o": [<figure|null> x4], "w": 100}  (w — savol chizmasi kengligi, %).
"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET

MAX_ITEMS = 120
MAX_SVG_BYTES = 60_000
IMAGE_SRC_RE = re.compile(r"^/static/qfig/[A-Za-z0-9_.-]{6,80}$")
FN_RE = re.compile(r"^[0-9x+\-*/^().,\s a-z]*$")
FN_ALLOWED_WORDS = {"x", "sin", "cos", "tan", "sqrt", "abs", "log", "ln", "exp", "pi", "e", "pow", "asin", "acos", "atan"}

SVG_TAGS = {"svg", "g", "path", "circle", "ellipse", "line", "polyline", "polygon", "rect", "text", "tspan", "defs",
            "marker", "title", "desc", "clipPath", "linearGradient", "stop"}
SVG_ATTRS = {"viewBox", "width", "height", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry", "d", "points",
             "fill", "stroke", "stroke-width", "stroke-dasharray", "stroke-linecap", "stroke-linejoin", "opacity",
             "fill-opacity", "stroke-opacity", "transform", "font-size", "font-family", "font-weight", "text-anchor",
             "dominant-baseline", "id", "marker-end", "marker-start", "refX", "refY", "markerWidth", "markerHeight",
             "orient", "preserveAspectRatio", "offset", "stop-color", "clip-path", "class", "xmlns"}


def _num(v, default=0.0, lo=-10_000.0, hi=10_000.0) -> float:
    try:
        n = float(v)
    except (TypeError, ValueError):
        return default
    if n != n or n in (float("inf"), float("-inf")):
        return default
    return max(lo, min(hi, round(n, 4)))


def _txt(v, limit=60) -> str:
    return str(v or "").strip()[:limit]


def sanitize_function_expr(expr: str) -> str:
    expr = _txt(expr, 80).lower()
    if not expr or not FN_RE.match(expr):
        return ""
    for word in re.findall(r"[a-z]+", expr):
        if word not in FN_ALLOWED_WORDS:
            return ""
    return expr


def _sanitize_plane_item(it: dict) -> dict | None:
    k = it.get("k")
    color = it.get("c") if isinstance(it.get("c"), str) and re.match(r"^#[0-9a-fA-F]{3,8}$", it.get("c", "")) else ""
    out: dict
    if k == "pt":
        out = {"k": "pt", "x": _num(it.get("x")), "y": _num(it.get("y")), "l": _txt(it.get("l"), 16)}
    elif k == "line":
        out = {"k": "line", "x1": _num(it.get("x1")), "y1": _num(it.get("y1")), "x2": _num(it.get("x2")), "y2": _num(it.get("y2")),
               "dash": bool(it.get("dash")), "arrow": bool(it.get("arrow")), "l": _txt(it.get("l"), 16),
               "ext": bool(it.get("ext"))}
    elif k == "circle":
        out = {"k": "circle", "cx": _num(it.get("cx")), "cy": _num(it.get("cy")), "r": _num(it.get("r"), 1, 0.001, 10_000),
               "fill": bool(it.get("fill")), "dash": bool(it.get("dash")), "l": _txt(it.get("l"), 16)}
    elif k == "arc":
        out = {"k": "arc", "cx": _num(it.get("cx")), "cy": _num(it.get("cy")), "r": _num(it.get("r"), 1, 0.001, 10_000),
               "a1": _num(it.get("a1"), 0, -720, 720), "a2": _num(it.get("a2"), 90, -720, 720), "l": _txt(it.get("l"), 16)}
    elif k == "poly":
        pts = []
        for p in (it.get("pts") or [])[:40]:
            if isinstance(p, (list, tuple)) and len(p) >= 2:
                pts.append([_num(p[0]), _num(p[1])])
        if len(pts) < 2:
            return None
        out = {"k": "poly", "pts": pts, "fill": bool(it.get("fill")), "closed": it.get("closed", True) is not False,
               "dash": bool(it.get("dash"))}
        names = it.get("names")
        if isinstance(names, list):
            out["names"] = [_txt(n, 8) for n in names[:40]]
    elif k == "text":
        t = _txt(it.get("t"), 60)
        if not t:
            return None
        out = {"k": "text", "x": _num(it.get("x")), "y": _num(it.get("y")), "t": t}
    elif k == "fn":
        f = sanitize_function_expr(it.get("f", ""))
        if not f:
            return None
        out = {"k": "fn", "f": f}
    else:
        return None
    if color:
        out["c"] = color
    return out


def sanitize_svg(raw: str) -> str:
    raw = (raw or "").strip()
    if not raw or len(raw.encode("utf-8")) > MAX_SVG_BYTES:
        return ""
    if re.search(r"<!DOCTYPE|<!ENTITY|<\?xml", raw, re.I):
        raw = re.sub(r"<\?xml[^>]*\?>", "", raw, flags=re.I).strip()
        if re.search(r"<!DOCTYPE|<!ENTITY", raw, re.I):
            return ""
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return ""

    def local(tag: str) -> str:
        return tag.split("}", 1)[1] if tag.startswith("{") else tag

    def clean(el: ET.Element) -> ET.Element | None:
        tag = local(el.tag)
        if tag not in SVG_TAGS:
            return None
        node = ET.Element(tag)
        for name, value in el.attrib.items():
            name = local(name)
            if name not in SVG_ATTRS or re.search(r"javascript:|url\(\s*['\"]?\s*(?!#)|data:|@import|expression\(", value, re.I):
                continue
            node.set(name, value[:2000])
        node.text = el.text if tag in ("text", "tspan", "title", "desc") else None
        for child in el:
            c = clean(child)
            if c is not None:
                node.append(c)
                c.tail = None
        return node

    if local(root.tag) != "svg":
        return ""
    cleaned = clean(root)
    if cleaned is None:
        return ""
    cleaned.set("xmlns", "http://www.w3.org/2000/svg")
    if not cleaned.get("viewBox"):
        w, h = cleaned.get("width", "300"), cleaned.get("height", "200")
        try:
            cleaned.set("viewBox", f"0 0 {float(re.sub(r'[^0-9.]', '', w) or 300)} {float(re.sub(r'[^0-9.]', '', h) or 200)}")
        except ValueError:
            cleaned.set("viewBox", "0 0 300 200")
    cleaned.attrib.pop("width", None)
    cleaned.attrib.pop("height", None)
    return ET.tostring(cleaned, encoding="unicode")


def sanitize_figure(fig) -> dict | None:
    if not isinstance(fig, dict):
        return None
    t = fig.get("type")
    if t == "plane":
        xmin, xmax = _num(fig.get("xmin"), -6), _num(fig.get("xmax"), 6)
        ymin, ymax = _num(fig.get("ymin"), -6), _num(fig.get("ymax"), 6)
        if xmax - xmin < 0.1:
            xmin, xmax = -6, 6
        if ymax - ymin < 0.1:
            ymin, ymax = -6, 6
        items = []
        for it in (fig.get("items") or [])[:MAX_ITEMS]:
            if isinstance(it, dict):
                s = _sanitize_plane_item(it)
                if s:
                    items.append(s)
        return {"type": "plane", "xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax,
                "axes": fig.get("axes", True) is not False, "grid": fig.get("grid", True) is not False,
                "equal": fig.get("equal", True) is not False, "items": items}
    if t == "image":
        src = str(fig.get("src") or "")
        if not IMAGE_SRC_RE.match(src):
            return None
        return {"type": "image", "src": src, "alt": _txt(fig.get("alt"), 120)}
    if t == "svg":
        svg = sanitize_svg(str(fig.get("svg") or ""))
        return {"type": "svg", "svg": svg} if svg else None
    return None


def sanitize_figures_doc(doc) -> dict:
    """Savol hujjatini tozalaydi; bo'sh bo'lsa {} qaytaradi."""
    if not isinstance(doc, dict):
        return {}
    q = sanitize_figure(doc.get("q"))
    opts_in = doc.get("o") if isinstance(doc.get("o"), list) else []
    opts = [sanitize_figure(opts_in[i]) if i < len(opts_in) else None for i in range(4)]
    if not q and not any(opts):
        return {}
    out: dict = {"q": q, "o": opts}
    w = _num(doc.get("w"), 100, 20, 100)
    if w != 100:
        out["w"] = int(w)
    return out


def figures_to_json(doc) -> str:
    clean = sanitize_figures_doc(doc)
    if not clean:
        return ""
    raw = json.dumps(clean, ensure_ascii=False, separators=(",", ":"))
    return raw if len(raw) <= 120_000 else ""


def parse_figures(raw: str) -> dict:
    if not raw:
        return {}
    try:
        val = json.loads(raw)
    except ValueError:
        return {}
    return val if isinstance(val, dict) else {}
