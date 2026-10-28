"""Savollar uchun SVG chizmalar (jang tartibi, Registon ansambli, xronologiya, qo'shin ierarxiyasi)."""

_BOX = '<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#4b5563" stroke-width="1.5"/>'
_TXT = '<text x="{x}" y="{y}" text-anchor="middle" font-size="{fs}" font-family="Arial, sans-serif" font-weight="{fw}" fill="#111827">{t}</text>'


def _box(x, y, w, h, label, fill="#e0ecff", fs=16, fw="700", sub=None):
    out = _BOX.format(x=x, y=y, w=w, h=h, fill=fill)
    out += _TXT.format(x=x + w / 2, y=y + h / 2 + (0 if not sub else -2) + 5, fs=fs, fw=fw, t=label)
    if sub:
        out += _TXT.format(x=x + w / 2, y=y + h / 2 + 16, fs=11, fw="400", t=sub)
    return out


def _wrap(inner, w=320, h=210):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


def army_formation(highlight=None):
    """Amir Temur qo'shinining jang tartibi (yuqoriga qarab — dushman tomon). Harflar: A ilg'or, B o'ng qanot,
    C qalb, D chap qanot, E orqa (chandovul). highlight — ajratib ko'rsatiladigan harf."""
    cells = {
        "A": (110, 12, 100, 38), "B": (222, 70, 84, 70), "C": (110, 70, 100, 70),
        "D": (14, 70, 84, 70), "E": (110, 160, 100, 38),
    }
    colors = {"A": "#fde7c8", "B": "#d8f3dc", "C": "#e0ecff", "D": "#d8f3dc", "E": "#f3e0f7"}
    out = '<text x="160" y="8" text-anchor="middle" font-size="9" font-family="Arial" fill="#6b7280">↑ dushman tomon</text>'
    for k, (x, y, w, h) in cells.items():
        out += _box(x, y, w, h, k, fill=("#ffe08a" if k == highlight else colors[k]))
    return _wrap(out, 320, 206)


def registon():
    """Registon maydoni: A — g'arbda, B — shimolda (orqada), C — sharqda."""
    out = '<rect x="104" y="92" width="112" height="70" rx="4" fill="#fdf6e3" stroke="#9ca3af" stroke-dasharray="5 3"/>'
    out += _TXT.format(x=160, y=132, fs=11, fw="400", t="Registon maydoni")
    out += _box(14, 56, 78, 106, "A", fill="#e0ecff", fs=20)
    out += _box(114, 10, 92, 62, "B", fill="#ffe08a", fs=20)
    out += _box(228, 56, 78, 106, "C", fill="#d8f3dc", fs=20)
    out += '<text x="160" y="192" text-anchor="middle" font-size="9" font-family="Arial" fill="#6b7280">↓ janub</text>'
    return _wrap(out, 320, 200)


def timeline():
    """Amir Temur yurishlari xronologiyasi: harflar yil nuqtalarida."""
    out = '<line x1="20" y1="100" x2="300" y2="100" stroke="#4b5563" stroke-width="3"/>'
    pts = [("A", 55, "1391"), ("B", 125, "1395"), ("C", 195, "1402"), ("D", 265, "1405")]
    for lab, x, yr in pts:
        out += f'<circle cx="{x}" cy="100" r="13" fill="#e0ecff" stroke="#4b5563" stroke-width="1.5"/>'
        out += _TXT.format(x=x, y=105, fs=14, fw="700", t=lab)
        out += _TXT.format(x=x, y=135, fs=12, fw="400", t=yr)
    return _wrap(out, 320, 170)


def hierarchy():
    """Temur qo'shini ierarxiyasi piramidasi: 1 — eng yuqori (10 000), 4 — eng quyi (10)."""
    out = ""
    levels = [("1", 10000, 100, 36), ("2", 1000, 78, 80), ("3", 100, 56, 124), ("4", 10, 34, 168)]
    for lab, size, inset, y in levels:
        x = inset
        w = 320 - 2 * inset
        out += _BOX.format(x=x, y=y - 30, w=w, h=34, fill="#e0ecff")
        out += _TXT.format(x=160, y=y - 8, fs=13, fw="700", t=f"{lab}-pog'ona: {size:,}".replace(",", " ") + " kishi")
    return _wrap(out, 320, 210)
