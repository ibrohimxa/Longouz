"""Biologiya va kimyo savollari uchun SVG chizmalar."""
import math
from .svgkit import svg, line, poly, rect, circle, text, path, f, INK, GRAY, BLUE, RED, GREEN, ORANGE


def _num(x, y, n):
    return circle(x, y, 10, "#fff", INK, 1.6) + text(x, y + 4, str(n), 12, "middle", INK, "700")


def animal_cell():
    """Hayvon hujayrasi: 1 — yadro, 2 — mitoxondriya, 3 — endoplazmatik to'r (EPT), 4 — hujayra membranasi."""
    p = ['<ellipse cx="170" cy="105" rx="140" ry="88" fill="#fef9c3" stroke="#111827" stroke-width="3"/>',
         '<circle cx="150" cy="100" r="32" fill="#bfdbfe" stroke="#111827" stroke-width="2.4"/><circle cx="150" cy="100" r="9" fill="#2563eb"/>',
         '<ellipse cx="238" cy="78" rx="24" ry="12" fill="#fecaca" stroke="#111827" stroke-width="2"/>',
         path("M 224 78 q 6 -8 12 0 t 12 0", INK, 1.4),
         path("M 95 150 q 18 -14 36 0 t 36 0 t 36 0", "#16a34a", 3), path("M 95 160 q 18 -14 36 0 t 36 0 t 36 0", "#16a34a", 3)]
    p += [_num(150, 58, 1), line(150, 68, 150, 80, INK, 1.2), _num(238, 52, 2), line(238, 62, 238, 68, INK, 1.2),
          _num(170, 188, 3), line(170, 178, 170, 168, INK, 1.2), _num(300, 105, 4), line(290, 105, 306, 105, INK, 1.2)]
    return svg(340, 215, "".join(p))


def dna_ladder(top="A–T", rungs=("A", "T", "G", "C"), partner=("T", "A", "C", "G"), hide=1):
    """DNK zanjiri: chap zanjirda asoslar, o'ng zanjirda komplementar asoslar ('?' — yashirilgan)."""
    parts = [line(100, 20, 100, 190, INK, 3), line(240, 20, 240, 190, INK, 3)]
    for i, (a, b) in enumerate(zip(rungs, partner)):
        y = 40 + i * 42
        parts += [line(100, y, 240, y, GRAY, 2, "4 3"), circle(100, y, 14, "#bfdbfe", INK, 1.6), text(100, y + 5, a, 14, "middle", INK, "700"),
                  circle(240, y, 14, "#fecaca", INK, 1.6), text(240, y + 5, "?" if i == hide else b, 14, "middle", INK, "700")]
    parts.append(text(170, 208, "1-zanjir  ⟷  2-zanjir", 11, "middle", GRAY, "600"))
    return svg(340, 215, "".join(parts))


def heart_diagram():
    """Yurak: 1 — o'ng bo'lmacha, 2 — o'ng qorincha, 3 — chap bo'lmacha, 4 — chap qorincha."""
    parts = [path("M 170 190 C 70 140 60 60 120 45 C 150 38 170 60 170 70 C 170 60 190 38 220 45 C 280 60 270 140 170 190 Z", INK, 3, "#fecaca"),
             line(170, 70, 170, 185, INK, 2.4), line(80, 110, 260, 110, INK, 2.4)]
    parts += [_num(125, 85, 1), _num(125, 150, 2), _num(215, 85, 3), _num(215, 150, 4)]
    parts.append(text(60, 100, "O'ng", 11, "end", GRAY, "600")); parts.append(text(280, 100, "Chap", 11, "start", GRAY, "600"))
    return svg(340, 215, "".join(parts))


def neuron():
    """Neyron: 1 — dendritlar, 2 — tana (yadro), 3 — akson, 4 — sinaptik uchlar."""
    parts = [circle(110, 105, 28, "#bfdbfe", INK, 2.6), circle(110, 105, 9, "#2563eb", INK, 1)]
    for a in (150, 190, 215, 245):
        r = math.radians(a)
        parts.append(line(110 + 28 * math.cos(r), 105 + 28 * math.sin(r), 110 + 62 * math.cos(r), 105 + 62 * math.sin(r), INK, 2))
    parts.append(line(138, 105, 270, 105, INK, 3))
    for y in (85, 105, 125):
        parts.append(line(270, 105, 300, y, INK, 2))
        parts.append(circle(304, y, 4, "#fecaca", INK, 1.4))
    parts += [_num(62, 60, 1), _num(110, 150, 2), _num(200, 90, 3), _num(318, 150, 4)]
    return svg(340, 215, "".join(parts))


def punnett(p1=("A", "a"), p2=("A", "a")):
    """Pennet katagi 2×2."""
    parts = []
    x0, y0, s = 90, 60, 70
    for i, a in enumerate(p2):
        parts.append(text(x0 + s * (i + 0.5), y0 - 10, a, 16, "middle", BLUE, "700"))
    for j, b in enumerate(p1):
        parts.append(text(x0 - 14, y0 + s * (j + 0.5) + 5, b, 16, "middle", RED, "700"))
        for i, a in enumerate(p2):
            g = "".join(sorted(b + a, key=lambda c: (c.lower(), c.islower())))
            parts.append(rect(x0 + s * i, y0 + s * j, s, s, "#f8fafc", INK, 2))
            parts.append(text(x0 + s * (i + 0.5), y0 + s * (j + 0.5) + 6, g, 18, "middle", INK, "700"))
    return svg(340, 215, "".join(parts))


def mitosis_phases():
    """Mitoz: A — profaza, B — metafaza, C — anafaza, D — telofaza sxemasi (xromosomalar chizig'i)."""
    parts = []
    for k, lab in enumerate("ABCD"):
        cx = 45 + k * 80
        parts += [circle(cx, 100, 32, "#fef9c3", INK, 2), text(cx, 160, lab, 15, "middle", INK, "700")]
        if lab == "A":
            for dx, dy in ((-10, -8), (6, -12), (-4, 8), (10, 6), (-14, 4)):
                parts.append(line(cx + dx - 4, 100 + dy, cx + dx + 4, 100 + dy + 6, RED, 3))
        elif lab == "B":
            for dy in (-14, -4, 6, 14):
                parts.append(line(cx - 8, 100 + dy, cx + 8, 100 + dy, RED, 3))
        elif lab == "C":
            for dy in (-14, 14):
                parts += [line(cx - 10, 100 + dy, cx - 2, 100 + dy, RED, 3), line(cx + 2, 100 + dy, cx + 10, 100 + dy, RED, 3)]
            parts += [line(cx - 20, 90, cx - 20, 110, GRAY, 1.4)]
        else:
            parts += [line(cx, 74, cx, 126, INK, 2.4), circle(cx - 14, 100, 8, "#fecaca", INK, 1.4), circle(cx + 14, 100, 8, "#fecaca", INK, 1.4)]
    return svg(340, 190, "".join(parts))


def bohr_atom(shells, name="Na"):
    """Atomning elektron qavatlari (Bor modeli): shells — qavatlardagi elektronlar soni ro'yxati."""
    cx, cy = 170, 105
    parts = [circle(cx, cy, 16, "#fecaca", INK, 2), text(cx, cy + 5, name, 12, "middle", INK, "700")]
    for i, n in enumerate(shells):
        r = 32 + i * 24
        parts.append(circle(cx, cy, r, "none", GRAY, 1.4))
        for k in range(n):
            a = 2 * math.pi * k / n + i * 0.5
            parts.append(circle(cx + r * math.cos(a), cy + r * math.sin(a), 4.5, BLUE, INK, 1))
    return svg(340, 215, "".join(parts))


def skeleton(chain):
    """Uglerod skeleti (zig-zag): chain = zanjir uzunligi; oxirida OH bo'lsa 'OH' chiqariladi."""
    pts = []
    x, y = 40, 120
    for i in range(chain):
        pts.append((x + i * 46, y - (22 if i % 2 else 0)))
    parts = [poly(pts, INK, 3)]
    for i, (px, py) in enumerate(pts, start=1):
        parts.append(text(px, py + (-8 if i % 2 == 0 else 20), "", 11))
    return svg(340, 170, "".join(parts)), pts


def alcohol(n=2):
    """Spirt: n ta uglerodli zanjir + OH."""
    pts = [(50 + i * 52, 110 - (26 if i % 2 else 0)) for i in range(n)]
    parts = [poly(pts, INK, 3)]
    lx, ly = pts[-1]
    parts += [line(lx, ly, lx + 40, ly + (-26 if (n - 1) % 2 == 0 else 26), INK, 3), text(lx + 54, ly + (-26 if (n - 1) % 2 == 0 else 26) + 5, "OH", 16, "middle", RED, "700")]
    return svg(340, 170, "".join(parts))
