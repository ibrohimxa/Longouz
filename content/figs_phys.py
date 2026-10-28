"""Fizika savollari uchun SVG chizmalar."""
import math
from .svgkit import (svg, line, poly, rect, circle, text, path, Plot, f, INK, GRAY, BLUE, RED, GREEN, ORANGE)


# ----------------------------------------------------------------------------- grafiklar
def graph(points, xticks, yticks, xlabel="t, s", ylabel="v, m/s", xmax=None, ymax=None, ymin=0, xmin=0,
          dots=None, guides=None, color=BLUE, extra=None, w=340, h=240, xfmt=None, yfmt=None, lines=None):
    xmax = xmax if xmax is not None else max(xticks)
    ymax = ymax if ymax is not None else max(yticks)
    p = Plot(xmin, xmax, ymin, ymax, w=w, h=h, xlabel=xlabel, ylabel=ylabel, xticks=xticks, yticks=yticks, xfmt=xfmt, yfmt=yfmt)
    if lines:
        for pts, c in lines:
            p.line(pts, c)
    elif points:
        p.line(points, color)
    for g in (guides or []):
        p.guide(*g)
    for d in (dots or []):
        p.dot(*d)
    for e in (extra or []):
        p.raw(e)
    return p.out()


def pv_cycle(pts, labels=("1", "2", "3", "4"), xticks=(1, 2, 3, 4), yticks=(1, 2, 3, 4), xlabel="V", ylabel="p", xmax=None, ymax=None):
    """Yopiq sikl: pts — [(V,p)] 1->2->3->4->1 tartibida (to'g'ri chiziqli bo'laklar). Strelkalar yo'nalishni ko'rsatadi."""
    xmax = xmax or max(xticks) + 0.5
    ymax = ymax or max(yticks) + 0.5
    p = Plot(0, xmax, 0, ymax, xlabel=xlabel, ylabel=ylabel, xticks=list(xticks), yticks=list(yticks))
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        x1, y1, x2, y2 = p.X(a[0]), p.Y(a[1]), p.X(b[0]), p.Y(b[1])
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        p.raw(line(x1, y1, x2, y2, BLUE, 2.8))
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        p.raw(line(mx - dx / L * 4, my - dy / L * 4, mx + dx / L * 6, my + dy / L * 6, BLUE, 2.8, arrow=True))
    for (v, pr), lb in zip(pts, labels):
        p.dot(v, pr, lb, 8, -8)
    return p.out()


def isoprocess(kind):
    """kind: 'isotherm' (p-V giperbola), 'isobar', 'isochore' — p-V tekisligida."""
    p = Plot(0, 5, 0, 5, xlabel="V", ylabel="p", xticks=[], yticks=[], grid=False)
    if kind == "isotherm":
        p.curve(lambda v: 4 / v, 0.85, 4.8)
    elif kind == "isobar":
        p.line([(0.6, 2.5), (4.6, 2.5)])
    else:
        p.line([(2.5, 0.6), (2.5, 4.6)])
    return p.out()


def heating_curve():
    """Muz -> suv -> bug' isitish grafigi: T(Q). Bo'laklar: 1 (muz isiydi), 2 (erish), 3 (suv isiydi), 4 (qaynash), 5 (bug' isiydi)."""
    p = Plot(0, 10, -30, 140, w=360, h=250, xlabel="Q", ylabel="t, °C", xticks=[], yticks=[0, 100], grid=False)
    pts = [(0.5, -20), (2, 0), (4, 0), (6, 100), (9, 100), (9.6, 130)]
    p.line(pts)
    for i, (x, y) in enumerate([(1.3, -22), (3, 10), (5.2, 45), (7.5, 110), (9.3, 120)], start=1):
        p.label(x, y + (0 if i in (2, 4) else 0), str(i), 13, "middle", RED, "700")
    p.raw(line(p.X(0), p.Y(100), p.X(6), p.Y(100), GRAY, 1, "4 3"))
    return p.out()


def sine(amp, period, ylabel="u, V", xlabel="t, ms", amp_lbl=None, T_lbl=None, phase_cos=False):
    xs = [0, period / 4, period / 2, 3 * period / 4, period]
    p = Plot(0, period * 1.25, -amp * 1.3, amp * 1.3, w=360, h=220, xlabel=xlabel, ylabel=ylabel, xticks=[], yticks=[], grid=False)
    fn = (lambda t: amp * math.cos(2 * math.pi * t / period)) if phase_cos else (lambda t: amp * math.sin(2 * math.pi * t / period))
    p.curve(fn, 0, period * 1.2, 90)
    p.raw(line(p.X(0), p.Y(amp), p.X(period * 1.2), p.Y(amp), GRAY, 1, "4 3"))
    p.raw(text(p.X(0) - 4, p.Y(amp) + 4, amp_lbl or f(amp), 12, "end", INK, "700"))
    p.raw(text(p.X(0) - 4, p.Y(-amp) + 4, "−" + (amp_lbl or f(amp)), 12, "end", INK, "700"))
    p.raw(line(p.X(period), p.Y(amp * 0.15), p.X(period), p.Y(-amp * 0.15), INK, 1.4))
    p.raw(text(p.X(period), p.Y(-amp * 0.15) + 14, T_lbl or f(period), 12, "middle", INK, "700"))
    return p.out()


def decay(T_half, N0_label="N₀", times=(0, 1, 2, 3, 4)):
    p = Plot(0, 4.6 * T_half, 0, 1.15, w=340, h=240, xlabel="t, s", ylabel="N", xticks=[k * T_half for k in times], yticks=[], grid=True)
    p.curve(lambda t: 2 ** (-t / T_half), 0, 4.4 * T_half, 60)
    p.raw(text(p.l - 6 if hasattr(p, 'l') else 40, p.Y(1) + 4, N0_label, 12, "end", INK, "700"))
    for k in range(1, 3):
        p.raw(line(p.X(0), p.Y(2 ** -k), p.X(k * T_half), p.Y(2 ** -k), GRAY, 1, "4 3"))
    p.raw(text(p.l - 6, p.Y(0.5) + 4, "N₀/2", 11, "end", INK, "700"))
    p.raw(text(p.l - 6, p.Y(0.25) + 4, "N₀/4", 11, "end", INK, "700"))
    return p.out()


# ----------------------------------------------------------------------------- mexanika
def incline(angle=30, mu=False, show_forces=True, labelA="α", m_label="m"):
    a = math.radians(angle)
    bx0, by0, L = 30, 200, 250
    hh = L * math.tan(a)
    scale = 1.0
    if hh > 150:
        scale = 150 / hh
        L *= scale
        hh = 150
    bx1, by1 = bx0 + L, by0
    tx, ty = bx1, by0 - hh
    parts = [poly([(bx0, by0), (bx1, by1), (tx, ty)], INK, 2.4, "#f3f4f6", closed=True)]
    ux, uy = math.cos(a), -math.sin(a)       # nishab bo'ylab yuqoriga (piksel)
    nx, ny = -math.sin(a), -math.cos(a)      # tashqi normal
    s0 = L / math.cos(a) * 0.5
    cx, cy = bx0 + ux * s0, by0 + uy * s0
    w, h = 46, 30
    c1 = (cx - ux * w / 2, cy - uy * w / 2)
    c2 = (cx + ux * w / 2, cy + uy * w / 2)
    blk = [c1, c2, (c2[0] + nx * h, c2[1] + ny * h), (c1[0] + nx * h, c1[1] + ny * h)]
    parts.append(poly(blk, INK, 2, "#bfdbfe", closed=True))
    gx, gy = cx + nx * h / 2, cy + ny * h / 2
    parts.append(text(gx, gy + 4, m_label, 13, "middle", INK, "700"))
    if show_forces:
        parts.append(line(gx, gy, gx, gy + 62, RED, 2.2, arrow=True))
        parts.append(text(gx + 12, gy + 66, "mg", 12, "start", RED, "700"))
        parts.append(line(cx + nx * h / 2 - nx * 0, cy + ny * h / 2, cx + nx * (h / 2 + 52), cy + ny * (h / 2 + 52), GREEN, 2.2, arrow=True))
        parts.append(text(cx + nx * (h / 2 + 62), cy + ny * (h / 2 + 62), "N", 12, "middle", GREEN, "700"))
        if mu:
            parts.append(line(cx, cy + ny * h * 0.1, cx + ux * 46, cy + uy * 46 + ny * h * 0.1, ORANGE, 2.2, arrow=True))
            parts.append(text(cx + ux * 56, cy + uy * 56, "F", 12, "middle", ORANGE, "700"))
    arc_r = 38
    parts.append(path(f"M {f(bx1 - arc_r)} {f(by1)} A {arc_r} {arc_r} 0 0 0 {f(bx1 - arc_r * math.cos(a))} {f(by1 - arc_r * math.sin(a))}", INK, 1.6))
    parts.append(text(bx1 - arc_r - 14, by1 - 6, labelA, 14, "middle", INK, "700"))
    return svg(340, 225, "".join(parts))


def atwood(m1="m₁", m2="m₂", heavier=2):
    parts = [rect(120, 8, 100, 10, "#e5e7eb", INK, 1.5), circle(170, 46, 22, "#f3f4f6", INK, 2.4), circle(170, 46, 3, INK, INK, 1)]
    parts.append(line(170, 18, 170, 24, INK, 3))
    parts.append(line(148, 46, 148, 150, INK, 2))
    parts.append(line(192, 46, 192, 120, INK, 2))
    parts.append(rect(128, 150, 40, 40, "#bfdbfe", INK, 2))
    parts.append(text(148, 175, m1, 15, "middle", INK, "700"))
    parts.append(rect(172, 120, 40, 40, "#fde68a", INK, 2))
    parts.append(text(192, 145, m2, 15, "middle", INK, "700"))
    return svg(340, 205, "".join(parts))


def table_pulley(m1="m₁", m2="m₂", mu=False):
    parts = [rect(20, 70, 200, 12, "#d1d5db", INK, 2)]
    parts.append(rect(90, 36, 44, 34, "#bfdbfe", INK, 2))
    parts.append(text(112, 58, m1, 15, "middle", INK, "700"))
    parts.append(circle(236, 60, 17, "#f3f4f6", INK, 2.4))
    parts.append(circle(236, 60, 3, INK, INK, 1))
    parts.append(line(134, 52, 236, 43, INK, 2))
    parts.append(line(253, 60, 253, 128, INK, 2))
    parts.append(rect(233, 128, 40, 40, "#fde68a", INK, 2))
    parts.append(text(253, 153, m2, 15, "middle", INK, "700"))
    parts.append(line(112, 36, 112, 14, GRAY, 0))  # bo'sh
    if mu:
        parts.append(text(112, 98, "ishqalanish bor", 11, "middle", GRAY, "600"))
    return svg(340, 180, "".join(parts))


def lever(l1, l2, left_label="F₁", right_label="F₂", total=None):
    """Richag: tayanch ostida, chap va o'ng yelkalar masofalari yozilgan."""
    x0 = 30
    L = 280
    L1 = L * l1 / (l1 + l2)
    xf = x0 + L1
    parts = [rect(x0, 92, L, 10, "#fde68a", INK, 2)]
    parts.append(poly([(xf, 102), (xf - 16, 140), (xf + 16, 140)], INK, 2, "#d1d5db", closed=True))
    parts.append(line(x0 + 12, 92, x0 + 12, 52, RED, 2.4, arrow=False))
    parts.append(line(x0 + 12, 52, x0 + 12, 52, RED, 2.4))
    parts.append(line(x0 + 12, 50, x0 + 12, 92, RED, 2.4, arrow=True))
    parts.append(text(x0 + 12, 42, left_label, 13, "middle", RED, "700"))
    parts.append(line(x0 + L - 12, 52, x0 + L - 12, 90, BLUE, 2.4, arrow=True))
    parts.append(text(x0 + L - 12, 42, right_label, 13, "middle", BLUE, "700"))
    parts.append(line(x0 + 12, 118, xf, 118, GRAY, 1.4, arrow=False))
    parts.append(text((x0 + 12 + xf) / 2, 132, f"{f(l1)}", 12, "middle", INK, "700"))
    parts.append(line(xf, 118, x0 + L - 12, 118, GRAY, 1.4))
    parts.append(text((xf + x0 + L - 12) / 2, 132, f"{f(l2)}", 12, "middle", INK, "700"))
    parts.append(text(xf, 158, "tayanch", 11, "middle", GRAY, "600"))
    return svg(340, 170, "".join(parts))


def u_tube(h1_label, h2_label, left="suv", right="yog'", h1=60, h2=75):
    """Birlashgan idish (U-nay): ikki suyuqlik ustunlari. Chizma sxematik."""
    parts = []
    parts.append(path("M 90 20 L 90 160 Q 90 190 120 190 L 200 190 Q 230 190 230 160 L 230 20", INK, 3))
    parts.append(path("M 120 20 L 120 150 Q 120 160 130 160 L 190 160 Q 200 160 200 150 L 200 20", INK, 3))
    parts.append(rect(122, 190 - 40 - h1 + 40, 76, 0, "none", "none", 0))
    parts.append(poly([(91, 160), (119, 160), (119, 160 - h1 + 20 - 0), (91, 160 - h1 + 20)], BLUE, 0, "#bfdbfe", closed=True))
    parts.append(poly([(201, 160), (229, 160), (229, 160 - h2 + 20), (201, 160 - h2 + 20)], ORANGE, 0, "#fed7aa", closed=True))
    parts.append(rect(91, 160, 138, 28, "#bfdbfe", "none", 0))
    parts.append(text(105, 160 - h1 / 2 + 14, left, 12, "middle", INK, "700"))
    parts.append(text(215, 160 - h2 / 2 + 14, right, 12, "middle", INK, "700"))
    parts.append(line(60, 160 - h1 + 20, 88, 160 - h1 + 20, GRAY, 1.2, "3 3"))
    parts.append(text(40, 160 - h1 + 24, h1_label, 12, "middle", INK, "700"))
    parts.append(line(232, 160 - h2 + 20, 262, 160 - h2 + 20, GRAY, 1.2, "3 3"))
    parts.append(text(284, 160 - h2 + 24, h2_label, 12, "middle", INK, "700"))
    return svg(340, 205, "".join(parts))


def hydraulic(S1, S2, F1="F₁", F2="F₂"):
    parts = [path("M 60 70 L 60 150 L 270 150 L 270 40", INK, 3), path("M 100 70 L 100 120 L 230 120 L 230 40", INK, 3)]
    parts.append(rect(61, 125, 38, 24, "#bfdbfe", "none", 0))
    parts.append(rect(101, 122, 128, 27, "#bfdbfe", "none", 0))
    parts.append(rect(231, 122, 38, 27, "#bfdbfe", "none", 0))
    parts.append(rect(64, 96, 32, 8, "#9ca3af", INK, 2))
    parts.append(line(80, 96, 80, 60, INK, 2))
    parts.append(line(80, 30, 80, 70, RED, 2.4, arrow=True))
    parts.append(text(80, 22, F1, 13, "middle", RED, "700"))
    parts.append(text(80, 168, f"S₁ = {S1}", 12, "middle", INK, "700"))
    parts.append(rect(234, 76, 32, 8, "#9ca3af", INK, 2))
    parts.append(rect(226, 56, 48, 20, "#fde68a", INK, 2))
    parts.append(line(250, 76, 250, 84, INK, 2))
    parts.append(text(250, 46, F2, 13, "middle", BLUE, "700"))
    parts.append(text(250, 168, f"S₂ = {S2}", 12, "middle", INK, "700"))
    return svg(340, 180, "".join(parts))


def vessels():
    """Uchta turli shakldagi idish: suyuqlik balandligi bir xil (gidrostatik paradoks)."""
    parts = []
    # 1: to'g'ri silindr
    parts.append(path("M 30 50 L 30 150 L 90 150 L 90 50", INK, 3))
    parts.append(rect(31, 70, 58, 79, "#bfdbfe", "none", 0))
    # 2: yuqoriga kengayuvchi
    parts.append(path("M 130 50 L 150 150 L 190 150 L 210 50", INK, 3))
    parts.append(poly([(133, 70), (207, 70), (190, 149), (150, 149)], "none", 0, "#bfdbfe", closed=True))
    # 3: yuqoriga torayuvchi
    parts.append(path("M 240 50 L 232 150 L 310 150 L 302 50", INK, 3) if False else path("M 250 50 L 232 150 L 310 150 L 292 50", INK, 3))
    parts.append(poly([(252, 70), (290, 70), (309, 149), (233, 149)], "none", 0, "#bfdbfe", closed=True))
    for xs in (60, 170, 271):
        parts.append(line(xs, 150, xs, 70, GRAY, 1.2, "3 3"))
    for xs, lab in ((60, "1"), (170, "2"), (271, "3")):
        parts.append(text(xs, 172, lab, 14, "middle", INK, "700"))
    parts.append(text(170, 24, "h bir xil", 12, "middle", GRAY, "600"))
    return svg(340, 185, "".join(parts))


def floating(frac=0.6, label="jism"):
    """Suvda suzayotgan jism: botgan qismi `frac`."""
    parts = [rect(30, 90, 280, 90, "#bfdbfe", "none", 0), line(30, 90, 310, 90, BLUE, 2.4)]
    bw, bh = 90, 60
    top = 90 - bh * (1 - frac)
    parts.append(rect(125, top, bw, bh, "#fde68a", INK, 2.2))
    parts.append(text(170, top + bh / 2 + 5, label, 13, "middle", INK, "700"))
    parts.append(text(60, 130, "suv", 13, "middle", BLUE, "700"))
    parts.append(line(240, top, 240, 90, GRAY, 1.2))
    parts.append(text(262, (top + 90) / 2 + 4, "chiqib turgan", 10, "middle", GRAY))
    return svg(340, 190, "".join(parts))


def projectile(angle=45, v0="v₀", show_h=True, show_range=True):
    a = math.radians(angle)
    x0, y0, W = 40, 190, 260
    Hpx = (W * math.tan(a)) / 4
    pts = [(x0 + W * t / 40, y0 - 4 * Hpx * (t / 40) * (1 - t / 40)) for t in range(41)]
    parts = [line(20, y0, 320, y0, INK, 2), poly(pts, BLUE, 2.6)]
    parts.append(line(x0, y0, x0 + 55 * math.cos(a), y0 - 55 * math.sin(a), RED, 2.4, arrow=True))
    parts.append(text(x0 + 62 * math.cos(a) + 10, y0 - 62 * math.sin(a), v0, 13, "start", RED, "700"))
    parts.append(path(f"M {x0 + 28} {y0} A 28 28 0 0 0 {f(x0 + 28 * math.cos(a))} {f(y0 - 28 * math.sin(a))}", INK, 1.4))
    parts.append(text(x0 + 40, y0 - 8, "α", 13, "middle", INK, "700"))
    if show_h:
        parts.append(line(x0 + W / 2, y0, x0 + W / 2, y0 - Hpx, GRAY, 1.4, "4 3"))
        parts.append(text(x0 + W / 2 + 8, y0 - Hpx / 2, "H", 14, "start", INK, "700"))
    if show_range:
        parts.append(line(x0, y0 + 14, x0 + W, y0 + 14, GRAY, 1.4))
        parts.append(text(x0 + W / 2, y0 + 28, "L", 14, "middle", INK, "700"))
    return svg(340, 225, "".join(parts))


def horizontal_throw(v0="v₀", h="h"):
    pts = [(50 + 230 * t / 40, 40 + 130 * (t / 40) ** 2) for t in range(41)]
    parts = [line(20, 172, 320, 172, INK, 2), poly(pts, BLUE, 2.6), rect(30, 40, 20, 132, "#e5e7eb", INK, 2)]
    parts.append(line(52, 40, 100, 40, RED, 2.4, arrow=True))
    parts.append(text(108, 36, v0, 13, "start", RED, "700"))
    parts.append(line(22, 40, 22, 172, GRAY, 1.4))
    parts.append(text(12, 108, h, 13, "middle", INK, "700"))
    parts.append(line(50, 190, 280, 190, GRAY, 1.4))
    parts.append(text(165, 205, "s", 13, "middle", INK, "700"))
    return svg(340, 215, "".join(parts))


def vectors(items, size=(340, 230), origin=(110, 150), labels_dx=8):
    """items: [(dx_px, dy_px, 'F₁', color)] — bir nuqtadan chiqadigan vektorlar (dy yuqoriga musbat)."""
    ox, oy = origin
    parts = []
    for dx, dy, lab, c in items:
        parts.append(line(ox, oy, ox + dx, oy - dy, c, 2.6, arrow=True))
        parts.append(text(ox + dx + (labels_dx if dx >= 0 else -labels_dx), oy - dy - 6 if dy > 0 else oy - dy + 14, lab, 13, "start" if dx >= 0 else "end", c, "700"))
    parts.append(circle(ox, oy, 4, INK, INK, 1))
    return svg(size[0], size[1], "".join(parts))


def spring_system(kind="series", k1="k₁", k2="k₂"):
    def zig(x, y, n=6, w=60, h=10):
        pts = [(x, y)]
        step = w / (2 * n)
        for i in range(2 * n):
            pts.append((x + step * (i + 0.5), y + (h if i % 2 == 0 else -h)))
        pts.append((x + w, y))
        return poly(pts, INK, 2)
    parts = [line(20, 30, 20, 150, INK, 4)]
    if kind == "series":
        parts += [line(20, 90, 50, 90), zig(50, 90), line(110, 90, 140, 90), zig(140, 90), line(200, 90, 230, 90),
                  rect(230, 70, 36, 40, "#bfdbfe", INK, 2), text(248, 95, "m", 14, "middle", INK, "700"),
                  text(80, 72, k1, 13, "middle", INK, "700"), text(170, 72, k2, 13, "middle", INK, "700")]
    else:
        parts += [line(20, 55, 60, 55), zig(60, 55), line(120, 55, 160, 55), line(20, 125, 60, 125), zig(60, 125), line(120, 125, 160, 125),
                  line(160, 55, 160, 125), line(160, 90, 190, 90), rect(190, 70, 36, 40, "#bfdbfe", INK, 2),
                  text(208, 95, "m", 14, "middle", INK, "700"), text(90, 38, k1, 13, "middle", INK, "700"), text(90, 150, k2, 13, "middle", INK, "700")]
    return svg(300, 175, "".join(parts))


def movable_block(F_label="F", P_label="P"):
    """Qo'zg'aluvchan blok: yuk blokka osilgan, ip ikki tomonlama."""
    parts = [rect(100, 10, 120, 10, "#e5e7eb", INK, 1.5), line(120, 20, 120, 110, INK, 2), line(200, 20, 200, 90, INK, 2)]
    parts.append(circle(160, 110, 40, "#f3f4f6", INK, 2.4) if False else circle(160, 90, 40, "#f3f4f6", INK, 2.4))
    parts.append(circle(160, 90, 3, INK, INK, 1))
    parts.append(line(160, 90, 160, 160, INK, 2))
    parts.append(rect(140, 160, 40, 34, "#fde68a", INK, 2))
    parts.append(text(160, 182, P_label, 14, "middle", INK, "700"))
    parts.append(line(120, 90, 120, 32, RED, 2.4, arrow=True))
    parts.append(text(104, 30, F_label, 13, "end", RED, "700"))
    return svg(300, 210, "".join(parts))


def scale_reading(v_start, v_end, step_minor, pointer, unit="", major_every=5, title=""):
    """Shkala (lineyka/termometr): bo'linma qiymatini aniqlash va ko'rsatkichni o'qish uchun."""
    x0, x1, y = 30, 310, 90
    parts = [rect(x0 - 10, 70, x1 - x0 + 20, 44, "#fef9c3", INK, 2)]
    n = int(round((v_end - v_start) / step_minor))
    for i in range(n + 1):
        xv = x0 + (x1 - x0) * i / n
        major = (i % major_every == 0)
        parts.append(line(xv, 70, xv, 70 + (22 if major else 12), INK, 1.6 if major else 1.1))
        if major:
            parts.append(text(xv, 138, f(v_start + i * step_minor), 12, "middle", INK, "600"))
    px = x0 + (x1 - x0) * (pointer - v_start) / (v_end - v_start)
    parts.append(line(px, 46, px, 76, RED, 2.6, arrow=True))
    if unit:
        parts.append(text(x1 + 4, 154, unit, 12, "end", INK, "700"))
    if title:
        parts.append(text(170, 30, title, 12, "middle", GRAY, "600"))
    return svg(340, 165, "".join(parts))


# ----------------------------------------------------------------------------- elektr
def _bat(x, y, vertical=True):
    """Manba belgisi (uzun chiziq +, qisqa chiziq −), vertikal."""
    return line(x - 12, y, x + 12, y, INK, 3) + line(x - 6, y + 8, x + 6, y + 8, INK, 5)


def _res(x, y, label, w=44, h=16, vertical=False):
    if vertical:
        return rect(x - h / 2, y - w / 2, h, w, "#fff", INK, 2) + text(x + h / 2 + 6, y + 4, label, 12, "start", INK, "700")
    return rect(x - w / 2, y - h / 2, w, h, "#fff", INK, 2) + text(x, y - h / 2 - 5, label, 12, "middle", INK, "700")


def circuit_series(labels, emf="ε"):
    n = len(labels)
    W = 80 + 90 * n
    parts = [line(30, 40, W - 30, 40), line(W - 30, 40, W - 30, 130), line(W - 30, 130, 30, 130), line(30, 130, 30, 94),
             line(30, 40, 30, 86)]
    parts.append(line(18, 86, 42, 86, INK, 3))
    parts.append(line(24, 94, 36, 94, INK, 5))
    parts.append(text(60, 92, emf, 13, "middle", INK, "700"))
    xs = [30 + 60 + 90 * i for i in range(n)]
    for x, lb in zip(xs, labels):
        parts.append(rect(x - 22, 40 - 8, 44, 16, "#ffffff", INK, 2))
        parts.append(text(x, 28, lb, 12, "middle", INK, "700"))
    return svg(W, 150, "".join(parts))


def circuit_parallel(labels, emf="ε"):
    n = len(labels)
    W = 110 + 90 * n
    parts = [line(30, 30, W - 30, 30), line(30, 140, W - 30, 140), line(30, 30, 30, 84), line(30, 96, 30, 140)]
    parts.append(line(18, 84, 42, 84, INK, 3))
    parts.append(line(24, 92, 36, 92, INK, 5))
    parts.append(text(58, 92, emf, 13, "middle", INK, "700"))
    for i, lb in enumerate(labels):
        x = 110 + 90 * i
        parts.append(line(x, 30, x, 68))
        parts.append(rect(x - 8, 68, 16, 44, "#ffffff", INK, 2))
        parts.append(line(x, 112, x, 140))
        parts.append(text(x + 14, 94, lb, 12, "start", INK, "700"))
        parts.append(circle(x, 30, 3, INK, INK, 1))
        parts.append(circle(x, 140, 3, INK, INK, 1))
    return svg(W, 160, "".join(parts))


def circuit_mixed(r1, r2, r3, emf="ε"):
    """R1 ketma-ket, so'ng R2 va R3 parallel."""
    parts = [line(30, 30, 90, 30), line(30, 140, 290, 140), line(30, 30, 30, 84), line(30, 96, 30, 140)]
    parts.append(line(18, 84, 42, 84, INK, 3))
    parts.append(line(24, 92, 36, 92, INK, 5))
    parts.append(text(56, 92, emf, 13, "middle", INK, "700"))
    parts.append(rect(90, 22, 54, 16, "#fff", INK, 2))
    parts.append(text(117, 16, r1, 12, "middle", INK, "700"))
    parts.append(line(144, 30, 250, 30))
    for x, lb in ((180, r2), (250, r3)):
        parts.append(line(x, 30, x, 68))
        parts.append(rect(x - 8, 68, 16, 44, "#fff", INK, 2))
        parts.append(line(x, 112, x, 140))
        parts.append(text(x + 14, 94, lb, 12, "start", INK, "700"))
        parts.append(circle(x, 30, 3, INK, INK, 1))
        parts.append(circle(x, 140, 3, INK, INK, 1))
    return svg(300, 160, "".join(parts))


def wheatstone(r1="R₁", r2="R₂", r3="R₃", r4="R₄", r5="R₅"):
    cx, cy = 170, 100
    top, bot, lf, rt = (cx, 30), (cx, 170), (90, cy), (250, cy)
    parts = [line(*lf, *top), line(*top, *rt), line(*rt, *bot), line(*bot, *lf), line(*lf, *rt)]
    for (a, b, lb) in (((lf, top), None, r1), ((top, rt), None, r2), ((lf, bot), None, r3), ((rt, bot), None, r4)):
        pass
    def mid(p, q):
        return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    for (p, q, lb) in ((lf, top, r1), (top, rt, r2), (lf, bot, r3), (rt, bot, r4)):
        mx, my = mid(p, q)
        parts.append(circle(mx, my, 15, "#fff", INK, 2))
        parts.append(text(mx, my + 4, lb, 11, "middle", INK, "700"))
    mx, my = mid(lf, rt)
    parts.append(circle(mx, my, 15, "#fff", INK, 2))
    parts.append(text(mx, my + 4, r5, 11, "middle", INK, "700"))
    for p, nm in ((lf, "A"), (top, "C"), (rt, "B"), (bot, "D")):
        parts.append(circle(p[0], p[1], 4, INK, INK, 1))
        parts.append(text(p[0] + (-12 if p is lf else 12 if p is rt else 0), p[1] + (-10 if p is top else 18 if p is bot else 4), nm, 12, "middle", INK, "700"))
    return svg(340, 195, "".join(parts))


def cap_circuit(kind, labels, emf="ε"):
    """Kondensatorlar: 'series' | 'parallel'."""
    def cap_h(x, y, lb):
        return line(x - 5, y - 16, x - 5, y + 16, INK, 3) + line(x + 5, y - 16, x + 5, y + 16, INK, 3) + text(x, y - 22, lb, 12, "middle", INK, "700")

    def cap_v(x, y, lb):
        return line(x - 16, y - 5, x + 16, y - 5, INK, 3) + line(x - 16, y + 5, x + 16, y + 5, INK, 3) + text(x + 22, y + 4, lb, 12, "start", INK, "700")
    n = len(labels)
    parts = []
    if kind == "series":
        W = 90 + 90 * n
        parts += [line(30, 40, W - 30, 40), line(W - 30, 40, W - 30, 130), line(W - 30, 130, 30, 130), line(30, 130, 30, 94), line(30, 40, 30, 86)]
        parts += [line(18, 86, 42, 86, INK, 3), line(24, 94, 36, 94, INK, 5), text(58, 92, emf, 13, "middle", INK, "700")]
        for i, lb in enumerate(labels):
            x = 30 + 70 + 90 * i
            parts.append(rect(x - 12, 28, 24, 24, "#fff", "none", 0))
            parts.append(cap_h(x, 40, lb))
        return svg(W, 150, "".join(parts))
    W = 110 + 90 * n
    parts += [line(30, 30, W - 30, 30), line(30, 140, W - 30, 140), line(30, 30, 30, 84), line(30, 96, 30, 140)]
    parts += [line(18, 84, 42, 84, INK, 3), line(24, 92, 36, 92, INK, 5), text(58, 92, emf, 13, "middle", INK, "700")]
    for i, lb in enumerate(labels):
        x = 110 + 90 * i
        parts += [line(x, 30, x, 80), line(x, 90, x, 140), cap_v(x, 85, lb)]
    return svg(W, 160, "".join(parts))


def magnet_field(B="in", charge="+", v_dir="right", force_choices=True):
    """Magnit maydonda zaryad: B='in' (×) yoki 'out' (•). Tezlik yo'nalishi: right|left|up|down."""
    parts = [rect(10, 10, 320, 200, "#f8fafc", GRAY, 1.2, 8)]
    for ix in range(8):
        for iy in range(5):
            x, y = 40 + ix * 40, 35 + iy * 40
            if B == "in":
                parts.append(line(x - 5, y - 5, x + 5, y + 5, BLUE, 1.6) + line(x - 5, y + 5, x + 5, y - 5, BLUE, 1.6))
            else:
                parts.append(circle(x, y, 2.6, BLUE, BLUE, 1) + circle(x, y, 6, "none", BLUE, 1.2))
    cx, cy = 165, 110
    parts.append(circle(cx, cy, 13, "#fff", INK, 2.2))
    parts.append(text(cx, cy + 5, charge, 16, "middle", INK, "700"))
    dx, dy = {"right": (1, 0), "left": (-1, 0), "up": (0, -1), "down": (0, 1)}[v_dir]
    parts.append(line(cx + dx * 15, cy + dy * 15, cx + dx * 70, cy + dy * 70, RED, 3, arrow=True))
    parts.append(text(cx + dx * 80 + (6 if dx == 0 else 0), cy + dy * 80 + (4 if dy == 0 else 0) + (-6 if dy == 0 else 0), "v", 14, "middle", RED, "700"))
    parts.append(text(318, 202, "B ⊗ (varoqqa)" if B == "in" else "B ⊙ (o'zimizga)", 11, "end", BLUE, "700"))
    return svg(340, 220, "".join(parts))


def solenoid_current():
    """Tokli o'tkazgich va magnit maydon chiziqlari (o'ng qo'l qoidasi) — yuqoridan ko'rinish."""
    parts = []
    parts.append(circle(170, 100, 8, INK, INK, 1))
    parts.append(circle(170, 100, 13, "none", INK, 1.4))
    for r in (36, 62, 88):
        parts.append(circle(170, 100, r, "none", BLUE, 1.6, ) if False else f'<circle cx="170" cy="100" r="{r}" fill="none" stroke="{BLUE}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    parts.append(text(170, 104, "I", 12, "middle", "#fff", "700"))
    return svg(340, 205, "".join(parts))


def refraction(a1=45, a2=28, n1="n₁", n2="n₂", show_values=True):
    """Ikki muhit chegarasida nur sinishi. Yuqori muhit n1 (nur kelayotgan), pastki n2."""
    cx, cy = 170, 100
    parts = [rect(10, cy, 320, 100, "#dbeafe", "none", 0), line(10, cy, 330, cy, INK, 2.2), line(cx, 15, cx, 195, GRAY, 1.4, "5 4")]
    a = math.radians(a1)
    b = math.radians(a2)
    L = 85
    parts.append(line(cx - L * math.sin(a), cy - L * math.cos(a), cx, cy, RED, 2.6, arrow=True))
    parts.append(line(cx, cy, cx + L * math.sin(b), cy + L * math.cos(b), RED, 2.6, arrow=True))
    parts.append(path(f"M {f(cx - 30 * math.sin(a))} {f(cy - 30 * math.cos(a))} A 30 30 0 0 1 {cx} {cy - 30}", INK, 1.4))
    parts.append(path(f"M {cx} {cy + 30} A 30 30 0 0 0 {f(cx + 30 * math.sin(b))} {f(cy + 30 * math.cos(b))}", INK, 1.4))
    parts.append(text(cx - 22, cy - 38, f"{a1}°" if show_values else "α", 13, "middle", INK, "700"))
    parts.append(text(cx + 24, cy + 52, f"{a2}°" if show_values else "β", 13, "middle", INK, "700"))
    parts.append(text(40, 40, n1, 14, "middle", INK, "700"))
    parts.append(text(40, 176, n2, 14, "middle", INK, "700"))
    return svg(340, 205, "".join(parts))


def lens(f_len=4, d=6, kind="conv", obj_h=1.5, unit=24):
    """Yupqa linza: f_len — fokus masofa (kataklar), d — jismgacha masofa. Nurlar va tasvir chiziladi."""
    cx, cy = 170, 105
    parts = [line(8, cy, 332, cy, INK, 1.6)]
    parts.append(line(cx, 28, cx, 182, INK, 2.6))
    if kind == "conv":
        parts.append(poly([(cx - 8, 40), (cx, 28), (cx + 8, 40)], INK, 2) + poly([(cx - 8, 170), (cx, 182), (cx + 8, 170)], INK, 2))
    else:
        parts.append(poly([(cx - 8, 28), (cx, 40), (cx + 8, 28)], INK, 2) + poly([(cx - 8, 182), (cx, 170), (cx + 8, 182)], INK, 2))
    F = f_len * unit
    for sgn in (-1, 1):
        parts.append(circle(cx + sgn * F, cy, 2.6, INK, INK, 1))
        parts.append(text(cx + sgn * F, cy + 16, "F", 12, "middle", INK, "700"))
    ox = cx - d * unit
    oh = obj_h * unit
    parts.append(line(ox, cy, ox, cy - oh, BLUE, 3, arrow=True))
    parts.append(text(ox, cy + 16, "jism", 11, "middle", BLUE, "700"))
    tip = (ox, cy - oh)
    fsgn = 1 if kind == "conv" else -1
    # nur 1: o'qqa parallel -> linza -> fokus orqali
    parts.append(line(ox, tip[1], cx, tip[1], RED, 1.8))
    fx = cx + fsgn * F
    k = (cy - tip[1]) / (fx - cx) if fx != cx else 0
    # linzadan keyin: nuqtadan (cx, tip_y) dan (fx, cy) ga yo'nalish
    dxn, dyn = fx - cx, cy - tip[1]
    ext = 150
    parts.append(line(cx, tip[1], cx + dxn / abs(dxn) * ext, tip[1] + dyn / abs(dxn) * ext, RED, 1.8))
    # nur 2: markazdan
    sl = (cy - tip[1]) / (cx - ox)
    parts.append(line(ox, tip[1], cx + 140, tip[1] + sl * (cx + 140 - ox), GREEN, 1.8))
    # tasvir
    if abs(d - f_len) > 1e-9:
        if kind == "conv":
            di = 1 / (1 / f_len - 1 / d)
        else:
            di = -1 / (1 / f_len + 1 / d)  # mavhum, linza oldida
        m = -di / d if kind == "conv" else -di / d
        ix = cx + di * unit
        ih = -m * oh  # piksel: yuqoriga musbat uchun
        iy = cy + m * oh * -1 * -1  # tasvir uchi y
        iy = cy - (-m) * oh * (1 if False else 1) if False else cy + (di / d) * oh * (1 if kind == "conv" else -1) * (1 if kind == "conv" else 1)
        if kind == "conv":
            iy = cy + (di / d) * oh
        else:
            iy = cy - (abs(di) / d) * oh
        dash = None if (kind == "conv" and d > f_len) else "5 3"
        if 8 < ix < 332:
            parts.append(line(ix, cy, ix, iy, ORANGE, 3, dash, arrow=True))
            parts.append(text(ix, cy + (16 if iy < cy else -8), "tasvir", 11, "middle", ORANGE, "700"))
    return svg(340, 205, "".join(parts))


def bohr_levels(arrows, n_max=4):
    """Energetik sathlar (n=1..n_max); arrows — [(from_n, to_n)] o'tishlar."""
    parts = []
    ys = {1: 170, 2: 120, 3: 85, 4: 62, 5: 48}
    for n in range(1, n_max + 1):
        parts.append(line(70, ys[n], 270, ys[n], INK, 2.4))
        parts.append(text(56, ys[n] + 4, f"n={n}", 12, "end", INK, "700"))
    for i, (a, b) in enumerate(arrows):
        x = 110 + i * 55
        parts.append(line(x, ys[a], x, ys[b] + (-4 if b < a else 4), RED if b < a else BLUE, 2.4, arrow=True))
        parts.append(text(x + 8, (ys[a] + ys[b]) / 2 + 4, chr(ord("A") + i), 12, "start", INK, "700"))
    return svg(340, 195, "".join(parts))


def nuclear_chain(items):
    """Yadro reaksiyasi sxemasi: items — [(matn, x, y)]. Oddiy matnli sxema."""
    return svg(340, 120, "".join(text(x, y, t, 15, "middle", INK, "700") for t, x, y in items))


def energy_graph(Ek_label="E", labels=None):
    return ""


def triangle_forces_equilibrium():
    return ""
