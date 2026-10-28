"""Fizika banki uchun yordamchilar: sonli javoblar kod orqali hisoblanadi (xato bo'lmasligi uchun)."""
from ._dsl import C, O, M


def fmt(x):
    if (x == 0 or abs(x) >= 1) and abs(x - round(x)) < 1e-9 * max(1, abs(x)) and abs(x) < 1e7:
        return str(int(round(x)))
    s = "%.6g" % x if 1e3 <= abs(x) < 1e7 else "%.4g" % x
    if "e" in s:
        m, e = s.split("e")
        e = int(e)
        sup = str(e).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
        return m.replace(".", ",") + "·10" + sup
    return s.replace(".", ",")


def N(d, q, x, wrong, unit, expl, fig=None, b=None):
    """Yopiq sonli savol: to'g'ri javob x; wrong — 3 ta xato son."""
    u = (" " + unit) if unit else ""
    return C(d, q, fmt(x) + u, [fmt(w) + u for w in wrong], expl, b=b, fig=fig)


def ON(d, q, x, expl, b=None):
    """Ochiq sonli savol (faqat sonni yozing)."""
    acc = [fmt(x)]
    if "," in acc[0]:
        acc.append(acc[0].replace(",", "."))
    return O(d, q, acc, expl, b=b)
