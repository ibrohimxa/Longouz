"""Matematika savollari uchun SVG chizmalar."""
import math
from .svgkit import (svg, line, poly, rect, circle, text, path, Plot, f, INK, GRAY, BLUE, RED, GREEN, ORANGE)


def triangle(a_lbl, b_lbl, c_lbl, A="A", B="B", C="C", pts=((40, 175), (290, 175), (120, 35)), right_at=None, extra=None):
    """Uchburchak; tomonlar yozuvi: a_lbl = BC, b_lbl = CA, c_lbl = AB; uchlar harfi."""
    (ax, ay), (bx, by), (cx, cy) = pts
    parts = [poly([pts[0], pts[1], pts[2]], INK, 2.6, "#eef2ff", closed=True)]
    parts.append(text(ax - 14, ay + 6, A, 15, "middle", INK, "700"))
    parts.append(text(bx + 14, by + 6, B, 15, "middle", INK, "700"))
    parts.append(text(cx, cy - 8, C, 15, "middle", INK, "700"))
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    mx, my = mid(pts[1], pts[2]); parts.append(text(mx + 14, my, a_lbl, 13, "start", RED, "700"))
    mx, my = mid(pts[2], pts[0]); parts.append(text(mx - 10, my - 4, b_lbl, 13, "end", RED, "700"))
    mx, my = mid(pts[0], pts[1]); parts.append(text(mx, my + 20, c_lbl, 13, "middle", RED, "700"))
    if right_at is not None:
        px, py = pts[right_at]
        q1, q2 = pts[(right_at + 1) % 3], pts[(right_at + 2) % 3]
        def unit(p, q):
            d = math.hypot(q[0] - p[0], q[1] - p[1]); return ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
        u1, u2 = unit((px, py), q1), unit((px, py), q2)
        s = 14
        parts.append(poly([(px + u1[0] * s, py + u1[1] * s), (px + (u1[0] + u2[0]) * s, py + (u1[1] + u2[1]) * s), (px + u2[0] * s, py + u2[1] * s)], INK, 1.6))
    for e in (extra or []):
        parts.append(e)
    return svg(340, 215, "".join(parts))


def right_triangle(leg1, leg2, hyp, lbls=("A", "B", "C")):
    """To'g'ri burchakli uchburchak (to'g'ri burchak B da). leg1 = AB (gorizontal), leg2 = BC (vertikal)."""
    return triangle(leg2, hyp, leg1, A=lbls[0], B=lbls[1], C=lbls[2], pts=((40, 180), (250, 180), (250, 40)), right_at=1)


def inscribed_angle(central=True, arc_deg=80):
    """Aylana: markaziy burchak va unga tiralgan ichki burchak. A, B — yoy uchlari, C — aylanada, O — markaz."""
    cx, cy, r = 170, 105, 85
    ang = lambda d: (cx + r * math.cos(math.radians(d)), cy - r * math.sin(math.radians(d)))
    A, B, C = ang(90 + arc_deg / 2), ang(90 - arc_deg / 2), ang(250)
    parts = [circle(cx, cy, r, "#f8fafc", INK, 2.4), circle(cx, cy, 3, INK, INK, 1)]
    parts += [line(cx, cy, *A, RED, 2.2), line(cx, cy, *B, RED, 2.2), line(*C, *A, BLUE, 2.2), line(*C, *B, BLUE, 2.2)]
    parts += [text(A[0] - 8, A[1] - 6, "A", 14, "end", INK, "700"), text(B[0] + 8, B[1] - 6, "B", 14, "start", INK, "700"),
              text(C[0], C[1] + 18, "C", 14, "middle", INK, "700"), text(cx, cy + 16, "O", 13, "middle", INK, "700")]
    return svg(340, 215, "".join(parts))


def circle_tangent():
    cx, cy, r = 130, 105, 70
    px, py = 295, 105
    d = px - cx
    t = math.sqrt(d * d - r * r)
    ang = math.atan2(r, t)
    tx, ty = cx + r * math.cos(math.pi / 2 - (math.pi / 2 - (math.acos(r / d)))), 0
    a = math.acos(r / d)
    T = (cx + r * math.cos(a), cy - r * math.sin(a))
    parts = [circle(cx, cy, r, "#f8fafc", INK, 2.4), circle(cx, cy, 3, INK, INK, 1), line(cx, cy, *T, RED, 2.2), line(*T, px, py, BLUE, 2.4),
             line(cx, cy, px, py, GRAY, 1.4, "4 3"), circle(px, py, 3.5, INK, INK, 1),
             text(cx - 4, cy + 18, "O", 13, "end", INK, "700"), text(T[0], T[1] - 8, "T", 14, "middle", INK, "700"), text(px + 8, py + 5, "P", 14, "start", INK, "700")]
    return svg(340, 215, "".join(parts))


def rect_diagonals(w_lbl, h_lbl):
    parts = [rect(50, 40, 240, 130, "#eef2ff", INK, 2.6), line(50, 40, 290, 170, RED, 1.8, "5 3"), line(290, 40, 50, 170, RED, 1.8, "5 3")]
    parts += [text(170, 192, w_lbl, 14, "middle", INK, "700"), text(30, 108, h_lbl, 14, "middle", INK, "700")]
    return svg(340, 205, "".join(parts))


def parallelogram(base, side, height):
    parts = [poly([(60, 170), (240, 170), (300, 55), (120, 55)], INK, 2.6, "#eef2ff", closed=True), line(120, 55, 120, 170, RED, 1.8, "5 3")]
    parts += [text(150, 190, base, 14, "middle", INK, "700"), text(88, 108, side, 14, "end", INK, "700"), text(132, 118, height, 14, "start", RED, "700")]
    parts.append(poly([(120, 160), (130, 160), (130, 170)], INK, 1.4))
    return svg(340, 205, "".join(parts))


def trapezoid(b1, b2, h, side=None):
    parts = [poly([(40, 170), (300, 170), (240, 55), (100, 55)], INK, 2.6, "#eef2ff", closed=True), line(100, 55, 100, 170, RED, 1.8, "5 3")]
    parts += [text(170, 190, b1, 14, "middle", INK, "700"), text(170, 45, b2, 14, "middle", INK, "700"), text(88, 118, h, 14, "end", RED, "700")]
    if side:
        parts.append(text(285, 118, side, 13, "start", INK, "700"))
    return svg(340, 205, "".join(parts))


def graph_linear(m, b, x1=-4, x2=4, ticks=(-4, -3, -2, -1, 1, 2, 3, 4), dots=()):
    ys = [m * x + b for x in (x1, x2)]
    ymax = max(abs(min(ys)), abs(max(ys)), abs(b), 4) + 1
    ymax = math.ceil(ymax)
    p = Plot(x1, x2, -ymax, ymax, w=340, h=250, xticks=list(ticks), yticks=[v for v in range(-ymax + 1, ymax) if v and v % 2 == 0], xlabel="x", ylabel="y")
    p.line([(x1, m * x1 + b), (x2, m * x2 + b)])
    for (x, y, lb) in dots:
        p.dot(x, y, lb)
    return p.out()


def graph_parabola(a, b, c, x1=-5, x2=5, ymin=-6, ymax=8, show=()):
    p = Plot(x1, x2, ymin, ymax, w=340, h=260, xticks=[v for v in range(x1, x2 + 1) if v], yticks=[v for v in range(ymin, ymax + 1, 2) if v], xlabel="x", ylabel="y")
    xs = [x1 + (x2 - x1) * i / 120 for i in range(121)]
    pts = [(x, a * x * x + b * x + c) for x in xs if ymin - 2 <= a * x * x + b * x + c <= ymax + 2]
    p.line(pts)
    for (x, y, lb) in show:
        p.dot(x, y, lb)
    return p.out()


def graph_trig(kind="sin", amp=1, k=1):
    p = Plot(-0.3, 2 * math.pi + 0.3, -amp - 0.6, amp + 0.6, w=360, h=230,
             xticks=[math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi], yticks=[-amp, amp] if amp != 1 else [-1, 1],
             xfmt=lambda v: {round(math.pi / 2, 3): "π/2", round(math.pi, 3): "π", round(3 * math.pi / 2, 3): "3π/2", round(2 * math.pi, 3): "2π"}.get(round(v, 3), f(v)),
             xlabel="x", ylabel="y")
    fn = (lambda x: amp * math.sin(k * x)) if kind == "sin" else (lambda x: amp * math.cos(k * x))
    p.curve(fn, 0, 2 * math.pi, 120)
    return p.out()


def bar_chart(labels, values, ymax=None, title=""):
    ymax = ymax or (max(values) // 10 + 1) * 10
    n = len(values)
    w, h, l, b = 340, 230, 44, 36
    bw = (w - l - 20) / n
    parts = [line(l, h - b, w - 10, h - b, INK, 1.8), line(l, 20, l, h - b, INK, 1.8)]
    step = ymax / 5
    for i in range(6):
        y = h - b - (h - b - 24) * i / 5
        parts += [line(l - 3, y, l, y, INK, 1.2), text(l - 6, y + 4, f(i * step), 11, "end"), line(l, y, w - 10, y, "#e5e7eb", 1)]
    for i, (lb, v) in enumerate(zip(labels, values)):
        x = l + i * bw + bw * 0.18
        hh = (h - b - 24) * v / ymax
        parts += [rect(x, h - b - hh, bw * 0.64, hh, "#93c5fd", BLUE, 1.6), text(x + bw * 0.32, h - b + 15, lb, 11, "middle")]
    if title:
        parts.append(text(w / 2, 14, title, 12, "middle", GRAY, "600"))
    return svg(w, h, "".join(parts))


def pie_chart(items, colors=("#93c5fd", "#fca5a5", "#86efac", "#fde68a", "#c4b5fd")):
    """items: [(label, percent)] — foizlar yig'indisi 100."""
    cx, cy, r = 130, 108, 84
    parts = []
    a0 = -90.0
    for (lb, pct), col in zip(items, colors):
        a1 = a0 + pct * 3.6
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        large = 1 if pct > 50 else 0
        parts.append(path(f"M {f(cx)} {f(cy)} L {f(x0)} {f(y0)} A {r} {r} 0 {large} 1 {f(x1)} {f(y1)} Z", INK, 1.6, col))
        am = math.radians((a0 + a1) / 2)
        parts.append(text(cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am) + 4, f"{f(pct)}%", 12, "middle", INK, "700"))
        a0 = a1
    for i, ((lb, pct), col) in enumerate(zip(items, colors)):
        parts += [rect(236, 50 + i * 26, 14, 14, col, INK, 1), text(256, 62 + i * 26, lb, 13, "start", INK, "600")]
    return svg(340, 215, "".join(parts))


def cube_like(kind="cube", lbl_a="a", lbl_h="h"):
    parts = []
    if kind in ("cube", "prism"):
        dx, dy = 60, -42
        x, y = 60, 80
        w, h = 110, (110 if kind == "cube" else 80)
        parts += [poly([(x, y), (x + w, y), (x + w + dx, y + dy), (x + dx, y + dy)], INK, 2.4, "#bfdbfe", closed=True),
                  poly([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)], INK, 2.4, "#c7d2fe", closed=True),
                  poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], INK, 2.4, "#e0ecff", closed=True)]
        parts += [text(x + w / 2, y + h + 18, lbl_a, 14, "middle", INK, "700"), text(x - 10, y + h / 2 + 4, lbl_h, 14, "end", INK, "700")]
    elif kind == "cylinder":
        cx, top, bot, rx, ry = 170, 55, 160, 70, 18
        parts += [path(f"M {cx - rx} {top} L {cx - rx} {bot} A {rx} {ry} 0 0 0 {cx + rx} {bot} L {cx + rx} {top}", INK, 2.4, "#e0ecff"),
                  f'<ellipse cx="{cx}" cy="{top}" rx="{rx}" ry="{ry}" fill="#bfdbfe" stroke="{INK}" stroke-width="2.4"/>',
                  line(cx, top, cx + rx, top, RED, 1.8), text(cx + rx / 2, top - 6, lbl_a, 14, "middle", RED, "700"),
                  text(cx + rx + 14, (top + bot) / 2, lbl_h, 14, "start", INK, "700")]
    elif kind == "cone":
        cx, top, bot, rx, ry = 170, 30, 165, 75, 20
        parts += [path(f"M {cx - rx} {bot} L {cx} {top} L {cx + rx} {bot} A {rx} {ry} 0 0 1 {cx - rx} {bot}", INK, 2.4, "#e0ecff"),
                  line(cx, top, cx, bot, RED, 1.8, "5 3"), line(cx, bot, cx + rx, bot, RED, 1.8),
                  text(cx + 8, (top + bot) / 2, lbl_h, 14, "start", RED, "700"), text(cx + rx / 2, bot + 16, lbl_a, 14, "middle", RED, "700")]
    elif kind == "pyramid":
        base = [(60, 160), (230, 160), (290, 125), (120, 125)]
        apex = (175, 25)
        parts += [poly(base, INK, 2.2, "#dbeafe", closed=True)]
        for p in (base[0], base[1], base[2]):
            parts.append(line(apex[0], apex[1], p[0], p[1], INK, 2.2))
        parts.append(line(apex[0], apex[1], base[3][0], base[3][1], INK, 1.6, "5 3"))
        parts += [line(apex[0], apex[1], apex[0], 145, RED, 1.8, "5 3"), text(apex[0] + 6, 95, lbl_h, 14, "start", RED, "700"), text(145, 182, lbl_a, 14, "middle", INK, "700")]
    return svg(340, 205, "".join(parts))


def venn(a_lbl="A", b_lbl="B", only_a="", only_b="", both=""):
    parts = [circle(130, 100, 70, "#bfdbfe", BLUE, 2.4), circle(210, 100, 70, "#fecaca", RED, 2.4)]
    parts += [text(95, 40, a_lbl, 15, "middle", BLUE, "700"), text(245, 40, b_lbl, 15, "middle", RED, "700")]
    parts += [text(100, 105, only_a, 17, "middle", INK, "700"), text(240, 105, only_b, 17, "middle", INK, "700"), text(170, 105, both, 17, "middle", INK, "700")]
    return svg(340, 205, "".join(parts))


def coord_points(points, xr=(-5, 5), yr=(-5, 5), segs=()):
    """points: [(x,y,'A')]; segs: [((x1,y1),(x2,y2))]"""
    p = Plot(xr[0], xr[1], yr[0], yr[1], w=340, h=260, xticks=[v for v in range(xr[0], xr[1] + 1) if v], yticks=[v for v in range(yr[0], yr[1] + 1) if v], xlabel="x", ylabel="y")
    for a, b in segs:
        p.line([a, b], BLUE, 2.4)
    for x, y, lb in points:
        p.dot(x, y, lb)
    return p.out()
