"""SVG chizma yordamchilari (fizika, matematika, biologiya savollari uchun). Hamma chizma oq fonli — qorong'u rejimda ham o'qiladi."""
import math

INK = "#111827"
GRAY = "#6b7280"
BLUE = "#2563eb"
RED = "#dc2626"
GREEN = "#16a34a"
ORANGE = "#ea580c"
FONT = 'font-family="Arial, sans-serif"'

_DEFS = (
    '<defs>'
    + "".join(
        f'<marker id="{i}" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="{c}"/></marker>'
        for i, c in (("ah", INK), ("ahr", RED), ("ahb", BLUE), ("ahg", GREEN), ("aho", ORANGE))
    )
    + '</defs>'
)
_MARK = {INK: "ah", RED: "ahr", BLUE: "ahb", GREEN: "ahg", ORANGE: "aho"}


def f(x):
    """Raqamni SVG uchun qisqa yozuvga aylantiradi."""
    return f"{x:.1f}".rstrip("0").rstrip(".") if abs(x - round(x)) > 1e-9 else str(int(round(x)))


def svg(w, h, inner):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{_DEFS}'
            f'<rect width="{w}" height="{h}" rx="8" fill="#ffffff"/>{inner}</svg>')


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line(x1, y1, x2, y2, c=INK, w=2, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{_MARK.get(c, "ah")})"' if arrow else ""
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{c}" stroke-width="{w}"{d}{m} stroke-linecap="round"/>'


def poly(pts, c=INK, w=2, fill="none", dash=None, closed=False):
    tag = "polygon" if closed else "polyline"
    d = f' stroke-dasharray="{dash}"' if dash else ""
    p = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
    return f'<{tag} points="{p}" fill="{fill}" stroke="{c}" stroke-width="{w}"{d} stroke-linejoin="round" stroke-linecap="round"/>'


def rect(x, y, w, h, fill="none", c=INK, sw=2, rx=0):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{rx}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>'


def circle(cx, cy, r, fill="none", c=INK, sw=2):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>'


def text(x, y, t, size=13, anchor="middle", fill=INK, weight="400", rot=None):
    tr = f' transform="rotate({rot} {f(x)} {f(y)})"' if rot else ""
    return f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" font-size="{size}" {FONT} font-weight="{weight}" fill="{fill}"{tr}>{esc(t)}</text>'


def path(d, c=INK, w=2, fill="none", dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}"{ds} stroke-linecap="round" stroke-linejoin="round"/>'


class Plot:
    """Koordinata o'qlari bilan grafik. Ma'lumot koordinatalari -> piksel."""

    def __init__(self, xmin, xmax, ymin, ymax, w=340, h=240, left=46, right=18, top=18, bottom=40,
                 xlabel="", ylabel="", xticks=None, yticks=None, grid=True, xfmt=None, yfmt=None):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.w, self.h, self.l, self.r, self.t, self.b = w, h, left, right, top, bottom
        self.parts = []
        self.xticks = xticks
        self.yticks = yticks
        self.xfmt = xfmt or (lambda v: f(v))
        self.yfmt = yfmt or (lambda v: f(v))
        if grid:
            for v in (xticks or []):
                self.parts.append(line(self.X(v), self.t, self.X(v), h - self.b, "#e5e7eb", 1))
            for v in (yticks or []):
                self.parts.append(line(self.l, self.Y(v), w - self.r, self.Y(v), "#e5e7eb", 1))
        x0 = self.X(0) if xmin <= 0 <= xmax else self.l
        y0 = self.Y(0) if ymin <= 0 <= ymax else h - self.b
        self.parts.append(line(self.l, y0, w - self.r + 6, y0, INK, 1.8, arrow=True))
        self.parts.append(line(x0, h - self.b, x0, self.t - 8, INK, 1.8, arrow=True))
        for v in (xticks or []):
            if abs(v) < 1e-12 and xmin <= 0 <= xmax and ymin == 0:
                continue
            self.parts.append(line(self.X(v), y0 - 3, self.X(v), y0 + 3, INK, 1.2))
            self.parts.append(text(self.X(v), h - self.b + 15 if ymin >= 0 else y0 + 16, self.xfmt(v), 11))
        for v in (yticks or []):
            if abs(v) < 1e-12 and ymin == 0:
                continue
            self.parts.append(line(x0 - 3, self.Y(v), x0 + 3, self.Y(v), INK, 1.2))
            self.parts.append(text(self.l - 6 if xmin >= 0 else x0 - 6, self.Y(v) + 4, self.yfmt(v), 11, "end"))
        if xlabel:
            self.parts.append(text(w - self.r, h - 6, xlabel, 12, "end", INK, "600"))
        if ylabel:
            self.parts.append(text(self.l + 6, self.t - 4, ylabel, 12, "start", INK, "600"))

    def X(self, v):
        return self.l + (v - self.xmin) / (self.xmax - self.xmin) * (self.w - self.l - self.r)

    def Y(self, v):
        return self.h - self.b - (v - self.ymin) / (self.ymax - self.ymin) * (self.h - self.t - self.b)

    def line(self, pts, c=BLUE, w=2.6, dash=None):
        self.parts.append(poly([(self.X(x), self.Y(y)) for x, y in pts], c, w, dash=dash))
        return self

    def curve(self, fn, x1, x2, n=60, c=BLUE, w=2.6):
        pts = [(x1 + (x2 - x1) * i / n, fn(x1 + (x2 - x1) * i / n)) for i in range(n + 1)]
        return self.line(pts, c, w)

    def dot(self, x, y, label="", dx=8, dy=-8, c=RED, anchor="start"):
        self.parts.append(circle(self.X(x), self.Y(y), 4, c, c, 1))
        if label:
            self.parts.append(text(self.X(x) + dx, self.Y(y) + dy, label, 12, anchor, INK, "700"))
        return self

    def guide(self, x=None, y=None):
        if x is not None:
            self.parts.append(line(self.X(x), self.Y(0 if self.ymin <= 0 else self.ymin), self.X(x), self.Y(y if y is not None else 0), GRAY, 1, "4 3"))
        if y is not None:
            self.parts.append(line(self.X(self.xmin if x is None else 0 if self.xmin <= 0 else self.xmin), self.Y(y), self.X(x if x is not None else self.xmax), self.Y(y), GRAY, 1, "4 3"))
        return self

    def label(self, x, y, t, size=12, anchor="middle", fill=INK, weight="600"):
        self.parts.append(text(self.X(x), self.Y(y), t, size, anchor, fill, weight))
        return self

    def raw(self, s):
        self.parts.append(s)
        return self

    def out(self):
        return svg(self.w, self.h, "".join(self.parts))
