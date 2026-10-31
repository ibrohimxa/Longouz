"""v229: kimyo va biologiya — HISOBLAB TEKSHIRILGAN yangi savollar (yopiq, ochiq, moslashtirish) + chizmalar.

Manba-format: Milliy sertifikat (UzBMB) 2025/26 spetsifikatsiyasi — 40 ta test topshirig'i:
№1–32 yopiq (A–D), №33–35 moslashtirish, №36–40 qisqa ochiq javob; DTM — 30 savol (24 yopiq, 3 moslashtirish, 3 ochiq).
Shu sababli har bir mavzuga uchala turdagi savol qo'shiladi.

Har bir javob KOD orqali hisoblanadi (atom massalari — maktab qiymatlari: Cl = 35,5; Cu = 64 va h.k.),
shuning uchun matn, chizma va kalit doim bir-biriga mos keladi. Xato variantlar odatiy xatolardan olinadi
(molyar massani unutish, koeffitsiyentni hisobga olmaslik, 22,4 ga bo'lish o'rniga ko'paytirish va h.k.).
"""
from __future__ import annotations

import math
import re
from fractions import Fraction

from ._dsl import C, M, O, expand
from ._ph import fmt
from .svgkit import svg, line, rect, text, circle, INK, GRAY, BLUE, RED, GREEN, ORANGE

# ------------------------------------------------------------------ yordamchilar
AR = {"H": 1, "He": 4, "Li": 7, "C": 12, "N": 14, "O": 16, "F": 19, "Na": 23, "Mg": 24, "Al": 27, "Si": 28, "P": 31, "S": 32,
      "Cl": 35.5, "K": 39, "Ca": 40, "Cr": 52, "Mn": 55, "Fe": 56, "Cu": 64, "Zn": 65, "Br": 80, "Ag": 108, "I": 127, "Ba": 137, "Pb": 207}
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def pretty(formula: str) -> str:
    """H2SO4 -> H₂SO₄ ; CuSO4*5H2O -> CuSO₄·5H₂O"""
    parts = formula.split("*")
    out = []
    for i, p in enumerate(parts):
        m = re.match(r"^(\d+)(.*)$", p) if i else None
        if m:
            out.append(m.group(1) + m.group(2).translate(SUB))
        else:
            out.append(p.translate(SUB))
    return "·".join(out)


def _parse(s: str) -> dict:
    """Formula -> {element: soni}. Qavslar va kristallogidrat (*) qo'llab-quvvatlanadi."""
    total: dict = {}
    for k, part in enumerate(s.split("*")):
        mult = 1
        if k:
            m = re.match(r"^(\d+)(.*)$", part)
            if m:
                mult, part = int(m.group(1)), m.group(2)
        stack = [{}]
        i = 0
        while i < len(part):
            ch = part[i]
            if ch == "(":
                stack.append({}); i += 1
            elif ch == ")":
                i += 1
                m = re.match(r"\d+", part[i:])
                n = int(m.group()) if m else 1
                i += len(m.group()) if m else 0
                grp = stack.pop()
                for el, c in grp.items():
                    stack[-1][el] = stack[-1].get(el, 0) + c * n
            else:
                m = re.match(r"([A-Z][a-z]?)(\d*)", part[i:])
                if not m:
                    raise ValueError(s)
                el, n = m.group(1), int(m.group(2) or 1)
                if el not in AR:
                    raise ValueError(el)
                stack[-1][el] = stack[-1].get(el, 0) + n
                i += len(m.group())
        for el, c in stack[0].items():
            total[el] = total.get(el, 0) + c * mult
    return total


def Mr(s: str) -> float:
    return sum(AR[e] * n for e, n in _parse(s).items())


def num(x) -> str:
    """Javob ko'rinishi: butun bo'lsa butun, aks holda vergul bilan (4 xonagacha, ortiqcha nollarsiz)."""
    if isinstance(x, Fraction):
        return dec(x)
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    s = ("%.4f" % x).rstrip("0").rstrip(".")
    return s.replace(".", ",")


def dec(fr: Fraction) -> str:
    """Kasrni ANIQ o'nli ko'rinishda (maxraji 2 va 5 ning darajasi bo'lsa) — yaxlitlashsiz."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return str(fr.numerator)
    from decimal import Decimal, getcontext
    getcontext().prec = 30
    s = format(Decimal(fr.numerator) / Decimal(fr.denominator), "f")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s.replace(".", ",")


def accept(x) -> list:
    s = num(x)
    out = [s]
    if "," in s:
        out.append(s.replace(",", "."))
    return out


def NQ(d, q, x, wrong, unit, expl, fig=None):
    """Yopiq sonli savol; xato variantlar takrorlanmaydi, kerak bo'lsa avtomatik to'ldiriladi."""
    u = ("" if unit == "%" else " " + unit) if unit else ""
    corr = num(x) + u
    seen, w = {corr}, []
    pool = list(wrong) + [x * 2, x / 2, x * 1.5, x + 10, x * 3, x - 5]
    for v in pool:
        if v is None or v <= 0:
            continue
        s = num(v) + u
        if s not in seen:
            seen.add(s)
            w.append(s)
        if len(w) == 3:
            break
    return C(d, q, corr, w, expl, fig=fig)


def pct(fr: Fraction) -> str:
    return dec(Fraction(fr) * 100) + "%"


# ------------------------------------------------------------------ chizmalar
def beaker(label_top: str, label_mid: str, fill_frac: float = 0.6) -> str:
    """Eritma solingan stakan (chizma)."""
    x, y, w, h = 120, 30, 100, 150
    lvl = y + h - h * fill_frac
    p = [rect(x, lvl, w, y + h - lvl, "#bfdbfe", BLUE, 0)]
    p += [line(x, y, x, y + h, INK, 3), line(x + w, y, x + w, y + h, INK, 3), line(x, y + h, x + w, y + h, INK, 3),
          line(x - 8, y, x, y, INK, 3), line(x + w, y, x + w + 8, y, INK, 3)]
    for k in range(1, 5):
        yy = y + h - k * h / 5
        p.append(line(x + w - 14, yy, x + w, yy, GRAY, 1.4))
    p.append(text(170, lvl + (y + h - lvl) / 2 + 5, label_mid, 15, "middle", INK, "700"))
    p.append(text(170, 20, label_top, 13, "middle", INK, "700"))
    return svg(340, 200, "".join(p))


def food_chain(names: list, values: list) -> str:
    """Ozuqa zanjiri: qutilar va strelkalar; values — energiya (yoki '?')."""
    n = len(names)
    bw, gap = 72, 14
    total = n * bw + (n - 1) * gap
    x0 = (340 - total) / 2
    p = []
    colors = ["#bbf7d0", "#fde68a", "#fed7aa", "#fecaca", "#e9d5ff"]
    for i, (nm, v) in enumerate(zip(names, values)):
        x = x0 + i * (bw + gap)
        p.append(rect(x, 60, bw, 64, colors[i % len(colors)], INK, 2, 10))
        p.append(text(x + bw / 2, 86, nm, 11, "middle", INK, "700"))
        p.append(text(x + bw / 2, 108, str(v), 12, "middle", RED if v == "?" else INK, "700"))
        if i < n - 1:
            p.append(line(x + bw + 1, 92, x + bw + gap - 1, 92, INK, 2, arrow=True))
    p.append(text(170, 150, "Energiya oqimi →", 11, "middle", GRAY, "600"))
    return svg(340, 170, "".join(p))


def dna_pair(seq: str, hide: int) -> str:
    """DNK qo'sh zanjiri bo'lagi: yuqori zanjir ko'rsatilgan, pastki zanjirda bitta nukleotid '?' bilan yashirilgan."""
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
    n = len(seq)
    step = min(46, 300 / n)
    x0 = 170 - step * (n - 1) / 2
    p = [line(x0 - 20, 50, x0 + step * (n - 1) + 20, 50, INK, 3), line(x0 - 20, 150, x0 + step * (n - 1) + 20, 150, INK, 3)]
    for i, b in enumerate(seq):
        x = x0 + i * step
        p += [line(x, 64, x, 136, GRAY, 2, "4 3"), circle(x, 64, 13, "#bfdbfe", INK, 1.5), text(x, 69, b, 13, "middle", INK, "700"),
              circle(x, 136, 13, "#fecaca", INK, 1.5), text(x, 141, "?" if i == hide else comp[b], 13, "middle", RED if i == hide else INK, "700")]
    p.append(text(170, 32, "1-zanjir (5' → 3')", 11, "middle", GRAY, "600"))
    p.append(text(170, 180, "2-zanjir (komplementar)", 11, "middle", GRAY, "600"))
    return svg(340, 195, "".join(p))


# ================================================================== KIMYO
COMPOUNDS = ["H2O", "CO2", "NH3", "CH4", "HCl", "H2SO4", "HNO3", "H3PO4", "NaOH", "KOH", "Ca(OH)2", "NaCl", "KCl", "CaCO3",
             "MgO", "Al2O3", "Fe2O3", "Fe3O4", "CuO", "CuSO4", "ZnO", "SO2", "SO3", "NO2", "P2O5", "Na2CO3", "NaHCO3", "K2SO4",
             "Al(OH)3", "Fe(OH)3", "Mg(OH)2", "BaSO4", "AgNO3", "KMnO4", "C2H5OH", "C6H12O6", "CH3COOH", "C2H4", "C2H2", "C6H6",
             "CuSO4*5H2O", "Na2SO4*10H2O", "Ca3(PO4)2", "(NH4)2SO4", "NH4NO3", "KNO3", "Ba(OH)2", "MnO2", "Cr2O3", "ZnCl2"]
GASES = ["H2", "O2", "N2", "CO2", "CH4", "NH3", "SO2", "Cl2", "CO", "HCl", "NO2", "C2H6", "C2H4", "H2S", "He"]

CLASS_OF = {
    "NaOH": "asos (ishqor)", "KOH": "asos (ishqor)", "Ca(OH)2": "asos (ishqor)", "Ba(OH)2": "asos (ishqor)",
    "Fe(OH)3": "erimaydigan asos", "Cu(OH)2": "erimaydigan asos", "Mg(OH)2": "erimaydigan asos",
    "HCl": "kislota", "H2SO4": "kislota", "HNO3": "kislota", "H3PO4": "kislota",
    "CaO": "asosli oksid", "Na2O": "asosli oksid", "MgO": "asosli oksid",
    "CO2": "kislotali oksid", "SO3": "kislotali oksid", "P2O5": "kislotali oksid",
    "ZnO": "amfoter oksid", "Al2O3": "amfoter oksid",
    "NaCl": "o'rta tuz", "K2SO4": "o'rta tuz", "CaCO3": "o'rta tuz",
    "NaHCO3": "nordon tuz", "KHSO4": "nordon tuz",
}

# Oksidlanish darajasi: formula, element, qiymat (qoidalar bo'yicha hisoblangan va tekshirilgan)
OXID = [("H2SO4", "S", 6), ("HNO3", "N", 5), ("KMnO4", "Mn", 7), ("K2Cr2O7", "Cr", 6), ("H3PO4", "P", 5), ("HClO4", "Cl", 7),
        ("NH3", "N", -3), ("H2S", "S", -2), ("CO2", "C", 4), ("Fe2O3", "Fe", 3), ("NO2", "N", 4), ("SO2", "S", 4),
        ("KClO3", "Cl", 5), ("MnO2", "Mn", 4), ("Cr2O3", "Cr", 3), ("HNO2", "N", 3), ("Na2SO3", "S", 4), ("CH4", "C", -4),
        ("N2O", "N", 1), ("P2O5", "P", 5), ("Fe3O4", "Fe", None), ("NaClO", "Cl", 1), ("K2MnO4", "Mn", 6), ("CaH2", "H", -1)]
FIXED = {"H": 1, "O": -2, "Na": 1, "K": 1, "Li": 1, "Ca": 2, "Mg": 2, "Ba": 2, "Al": 3, "F": -1}


def ox_state(formula: str, el: str):
    comp = _parse(formula)
    if formula == "CaH2" and el == "H":
        return -1
    s = 0
    for e, n in comp.items():
        if e == el:
            continue
        if e not in FIXED:
            return None
        s += FIXED[e] * n
    x = Fraction(-s, comp[el])
    return int(x) if x.denominator == 1 else None


REACTIONS = [
    # (yozuv, {modda: koeff}, reagentlar, mahsulotlar)
    ("2H₂ + O₂ → 2H₂O", {"H2": 2, "O2": 1, "H2O": 2}, ["H2", "O2"], ["H2O"]),
    ("CaCO₃ → CaO + CO₂", {"CaCO3": 1, "CaO": 1, "CO2": 1}, ["CaCO3"], ["CaO", "CO2"]),
    ("2Mg + O₂ → 2MgO", {"Mg": 2, "O2": 1, "MgO": 2}, ["Mg", "O2"], ["MgO"]),
    ("Zn + 2HCl → ZnCl₂ + H₂", {"Zn": 1, "HCl": 2, "ZnCl2": 1, "H2": 1}, ["Zn", "HCl"], ["ZnCl2", "H2"]),
    ("CH₄ + 2O₂ → CO₂ + 2H₂O", {"CH4": 1, "O2": 2, "CO2": 1, "H2O": 2}, ["CH4", "O2"], ["CO2", "H2O"]),
    ("2Al + 6HCl → 2AlCl₃ + 3H₂", {"Al": 2, "HCl": 6, "AlCl3": 2, "H2": 3}, ["Al", "HCl"], ["AlCl3", "H2"]),
    ("Fe + S → FeS", {"Fe": 1, "S": 1, "FeS": 1}, ["Fe", "S"], ["FeS"]),
    ("2NaOH + H₂SO₄ → Na₂SO₄ + 2H₂O", {"NaOH": 2, "H2SO4": 1, "Na2SO4": 1, "H2O": 2}, ["NaOH", "H2SO4"], ["Na2SO4", "H2O"]),
    ("C + O₂ → CO₂", {"C": 1, "O2": 1, "CO2": 1}, ["C", "O2"], ["CO2"]),
    ("4P + 5O₂ → 2P₂O₅", {"P": 4, "O2": 5, "P2O5": 2}, ["P", "O2"], ["P2O5"]),
    ("2KMnO₄ → K₂MnO₄ + MnO₂ + O₂", {"KMnO4": 2, "K2MnO4": 1, "MnO2": 1, "O2": 1}, ["KMnO4"], ["O2"]),
    ("Fe₂O₃ + 3H₂ → 2Fe + 3H₂O", {"Fe2O3": 1, "H2": 3, "Fe": 2, "H2O": 3}, ["Fe2O3", "H2"], ["Fe", "H2O"]),
    ("Mg + 2HCl → MgCl₂ + H₂", {"Mg": 1, "HCl": 2, "MgCl2": 1, "H2": 1}, ["Mg", "HCl"], ["MgCl2", "H2"]),
    ("2H₂O₂ → 2H₂O + O₂", {"H2O2": 2, "H2O": 2, "O2": 1}, ["H2O2"], ["O2"]),
]
GASEOUS = {"H2", "O2", "CO2", "CH4", "N2", "NH3", "Cl2", "SO2", "CO", "HCl"}

THERMO = [
    ("C + O₂ → CO₂ + 394 kJ", "C", 1, 394, [3, 6, 24, 36]),
    ("CH₄ + 2O₂ → CO₂ + 2H₂O + 890 kJ", "CH4", 1, 890, [4, 8, 32, 48]),
    ("2H₂ + O₂ → 2H₂O + 572 kJ", "H2", 2, 572, [1, 2, 8, 10]),
    ("S + O₂ → SO₂ + 297 kJ", "S", 1, 297, [8, 16, 64, 96]),
]


def chem() -> dict:
    out: dict = {}

    # --- K8.1: molyar massa, modda miqdori (yopiq + ochiq)
    L = []
    for f in COMPOUNDS:
        m = Mr(f)
        comp = _parse(f)
        wrong = [m - 16 if "O" in comp else m + 16, m + AR[list(comp)[0]], m - 1 if "H" in comp else m + 2, m * 2]
        L.append(NQ(1, f"{pretty(f)} ning molyar massasini toping (g/mol).", m, wrong, "g/mol",
                    "M = " + " + ".join(f"{n}·{num(AR[e])}" if n > 1 else num(AR[e]) for e, n in comp.items()) + f" = {num(m)} g/mol."))
    for i, f in enumerate(COMPOUNDS[:30]):
        m = Mr(f)
        n = [0.5, 2, 0.25, 3, 1.5, 0.2, 4, 0.1][i % 8]
        mass = n * m
        L.append(NQ(2, f"{num(mass)} g {pretty(f)} necha mol bo'ladi?", n, [n * 2, n / 2, mass / 100, n + 1], "mol",
                    f"n = m / M = {num(mass)} / {num(m)} = {num(n)} mol."))
    for i, f in enumerate(COMPOUNDS[10:30]):
        m = Mr(f)
        n = [0.3, 2.5, 0.4, 1.2, 0.75][i % 5]
        L.append(O(3, f"{num(n)} mol {pretty(f)} ning massasini toping (g). Faqat sonni yozing.", accept(n * m),
                   f"m = n·M = {num(n)}·{num(m)} = {num(n * m)} g."))
    out["K8.1"] = L

    # --- K8.2: massa ulush (yopiq + ochiq)
    L = []
    for f in ["H2O", "CO2", "NH3", "CH4", "SO2", "SO3", "Fe2O3", "CuO", "MgO", "Al2O3", "CaCO3", "NaOH", "H2SO4", "HNO3",
              "CuSO4", "Na2CO3", "K2SO4", "NH4NO3", "C6H12O6", "C2H5OH", "Fe3O4", "P2O5", "Ca(OH)2", "KMnO4"]:
        comp = _parse(f)
        m = Mr(f)
        for el in list(comp)[:2]:
            w = 100 * AR[el] * comp[el] / m
            if abs(w * 10 - round(w * 10)) > 1e-6:      # faqat 1 xonali aniq qiymatlar (yaxlitlash bahsi bo'lmasin)
                continue
            others = [100 * AR[e] * c / m for e, c in comp.items() if e != el] + [100 - w, w / 2 + 3]
            L.append(NQ(2, f"{pretty(f)} tarkibidagi {el} ning massa ulushini toping (%).", w, others, "%",
                        f"ω({el}) = {comp[el]}·{num(AR[el])} / {num(m)} · 100% = {num(w)}%."))
    for f, el in [("NH4NO3", "N"), ("CuSO4*5H2O", "Cu"), ("CaCO3", "Ca"), ("Fe2O3", "Fe"), ("SO3", "S"), ("NaOH", "Na"), ("MgO", "Mg"), ("CO2", "C")]:
        comp = _parse(f)
        w = 100 * AR[el] * comp[el] / Mr(f)
        if abs(w * 10 - round(w * 10)) > 1e-6:
            continue
        L.append(O(3, f"{pretty(f)} dagi {el} ning massa ulushini foizda toping (faqat son).", accept(w),
                   f"ω({el}) = {comp[el]}·{num(AR[el])} / {num(Mr(f))} · 100% = {num(w)}%."))
    out["K8.2"] = L

    # --- K11.14: molyar hajm, zichlik
    L = []
    vols = [5.6, 11.2, 22.4, 33.6, 44.8, 67.2, 2.24, 4.48]
    for i, g in enumerate(GASES):
        m = Mr(g)
        V = vols[i % len(vols)]
        n = V / 22.4
        L.append(NQ(2, f"Normal sharoitda {num(V)} l {pretty(g)} ning massasini toping (g).", n * m, [m, V * m / 10, n * m * 2, n], "g",
                    f"n = V/22,4 = {num(V)}/22,4 = {num(n)} mol; m = n·M = {num(n)}·{num(m)} = {num(n * m)} g."))
        mass = [0.5, 2, 1.5, 0.25][i % 4] * m
        L.append(NQ(2, f"{num(mass)} g {pretty(g)} normal sharoitda qancha hajmni egallaydi (l)?", mass / m * 22.4,
                    [mass * 22.4, mass / 22.4, 22.4, mass / m * 11.2], "l", f"V = m/M·22,4 = {num(mass)}/{num(m)}·22,4 = {num(mass / m * 22.4)} l."))
        L.append(NQ(1, f"{pretty(g)} ning vodorodga nisbatan zichligini toping.", m / 2, [m, m / 29, m * 2], "",
                    f"D(H₂) = M/2 = {num(m)}/2 = {num(m / 2)}."))
    for g in ["CO2", "SO2", "NH3", "CH4", "Cl2", "N2"]:
        m = Mr(g)
        V = 11.2
        L.append(O(3, f"Normal sharoitda {num(V)} l {pretty(g)} da nechta molekula bor? Javobni ×10²³ ko'rinishida yozing (masalan 1,2).",
                   accept(V / 22.4 * 6.02), f"N = V/22,4·N_A = 0,5·6,02·10²³ = {num(V / 22.4 * 6.02)}·10²³."))
    out["K11.14"] = L

    # --- K8.7: eritmalar (chizmali stakan) — massa ulush
    L = []
    for msol, w in [(200, 15), (150, 20), (400, 5), (250, 12), (500, 8), (120, 25), (300, 10), (80, 40)]:
        salt = msol * w / 100
        L.append(NQ(1, f"Chizmadagi stakanda {msol} g {w}% li osh tuzi eritmasi bor. Eritmada necha gramm tuz bor?", salt,
                    [msol * w, w, msol - salt], "g", f"m(tuz) = {msol}·{w}/100 = {num(salt)} g.", fig=beaker(f"{msol} g eritma", f"ω = {w}%")))
    for msol, w, water in [(200, 15, 50), (150, 20, 50), (300, 10, 100), (400, 25, 100), (240, 30, 60), (500, 12, 100)]:
        salt = msol * w / 100
        nw = 100 * salt / (msol + water)
        if abs(nw * 10 - round(nw * 10)) > 1e-6:
            continue
        L.append(NQ(2, f"{msol} g {w}% li eritmaga {water} g suv qo'shildi. Hosil bo'lgan eritmaning massa ulushini toping (%).", nw,
                    [w - water / 10, 100 * salt / msol / 2, w + 5], "%",
                    f"m(modda) = {num(salt)} g; yangi eritma {msol + water} g; ω = {num(salt)}/{msol + water}·100% = {num(nw)}%.",
                    fig=beaker(f"{msol} g + {water} g suv", f"ω = {w}% → ?")))
    for m1, w1, m2, w2 in [(100, 10, 300, 30), (200, 20, 200, 40), (150, 8, 50, 40), (300, 5, 200, 20), (400, 15, 100, 40)]:
        w = (m1 * w1 + m2 * w2) / (m1 + m2)
        L.append(NQ(3, f"{m1} g {w1}% li va {m2} g {w2}% li bir xil modda eritmalari aralashtirildi. Aralashmaning massa ulushi (%)?", w,
                    [(w1 + w2) / 2 if (w1 + w2) / 2 != w else w + 3, w1 + w2, w2 - w1], "%",
                    f"ω = ({m1}·{w1} + {m2}·{w2}) / ({m1}+{m2}) = {num(w)}%."))
        L.append(O(3, f"{m1} g {w1}% li eritma va {m2} g {w2}% li eritma aralashtirilsa, massa ulushi necha foiz bo'ladi? (faqat son)", accept(w),
                   f"ω = ({m1}·{w1} + {m2}·{w2}) / {m1 + m2} = {num(w)}%."))
    out["K8.7"] = L

    # --- K8.8: molyar konsentratsiya
    L = []
    for f, mass, vol_ml in [("NaOH", 20, 500), ("NaOH", 8, 200), ("KOH", 28, 250), ("NaCl", 11.7, 200), ("H2SO4", 49, 500),
                            ("HCl", 7.3, 400), ("KNO3", 20.2, 100), ("CuSO4", 16, 250), ("Na2CO3", 10.6, 200), ("C6H12O6", 18, 100)]:
        m = Mr(f)
        cm = mass / m / (vol_ml / 1000)
        L.append(NQ(2, f"{num(mass)} g {pretty(f)} suvda eritilib, {vol_ml} ml eritma tayyorlandi. Eritmaning molyar konsentratsiyasi (mol/l)?", cm,
                    [mass / m, cm * 2, cm / 2, mass / vol_ml], "mol/l", f"n = {num(mass)}/{num(m)} = {num(mass / m)} mol; C = n/V = {num(mass / m)}/{num(vol_ml / 1000)} = {num(cm)} mol/l."))
    out["K8.8"] = L

    # --- K11.12 / K8.3: reaksiya tenglamasi bo'yicha hisob (yopiq + ochiq)
    L, L2 = [], []
    for eq, coef, reac, prod in REACTIONS:
        for r in reac:
            for p in prod:
                mr, mp = Mr(r), Mr(p)
                k = [0.5, 2, 0.2, 1, 0.25, 3][(len(r) + len(p)) % 6]
                n_r = coef[r] * k
                m_r = n_r * mr
                n_p = n_r * coef[p] / coef[r]
                m_p = n_p * mp
                if p in GASEOUS:
                    V = n_p * 22.4
                    L.append(NQ(2, f"{eq} reaksiyasi bo'yicha {num(m_r)} g {pretty(r)} to'liq reaksiyaga kirsa, normal sharoitda necha litr {pretty(p)} hosil bo'ladi?",
                                V, [n_r * 22.4 if coef[p] != coef[r] else V * 2, m_r * 22.4 / mp, V / 2, V * 3], "l",
                                f"n({pretty(r)}) = {num(m_r)}/{num(mr)} = {num(n_r)} mol; koeffitsiyentlar {coef[r]}:{coef[p]} ⇒ n({pretty(p)}) = {num(n_p)} mol; V = {num(n_p)}·22,4 = {num(V)} l."))
                L.append(NQ(2, f"{eq} reaksiyasida {num(m_r)} g {pretty(r)} sarflansa, necha gramm {pretty(p)} hosil bo'ladi?",
                            m_p, [m_r * mp / mr if coef[p] != coef[r] else m_p * 2, m_r + mp, m_p / 2], "g",
                            f"n({pretty(r)}) = {num(m_r)}/{num(mr)} = {num(n_r)} mol ⇒ n({pretty(p)}) = {num(n_r)}·{coef[p]}/{coef[r]} = {num(n_p)} mol; m = {num(n_p)}·{num(mp)} = {num(m_p)} g."))
                if len(L2) < 14:
                    L2.append(O(3, f"{eq}: {num(m_r)} g {pretty(r)} reaksiyaga kirganda hosil bo'lgan {pretty(p)} massasini toping (g, faqat son).",
                                accept(m_p), f"n({pretty(p)}) = {num(n_r)}·{coef[p]}/{coef[r]} = {num(n_p)} mol; m = {num(m_p)} g."))
    out["K11.12"] = L + L2

    # --- K11.15: termokimyo
    L = []
    for eq, sub, k_sub, Q, masses in THERMO:
        msub = Mr(sub)
        for mass in masses:
            q = Q * mass / (msub * k_sub)
            L.append(NQ(2, f"Termokimyoviy tenglama: {eq}. {mass} g {pretty(sub)} yonganda qancha issiqlik ajraladi (kJ)?", q,
                        [Q * mass / msub if k_sub != 1 else q * 2, Q * mass, Q / mass], "kJ",
                        f"n = {mass}/{num(msub)} = {num(mass / msub)} mol; Q = {num(mass / msub)}/{k_sub}·{Q} = {num(q)} kJ."))
    out["K11.15"] = L

    # --- K9.3: pH
    L = []
    for e in range(1, 7):
        L.append(NQ(1, f"Eritmada [H⁺] = 10⁻{str(e).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))} mol/l. Eritmaning pH qiymati?", e,
                    [14 - e, e + 1, 10 - e if 10 - e > 0 and 10 - e != e else e + 2], "", f"pH = −lg[H⁺] = {e}."))
        L.append(NQ(2, f"Eritmada [OH⁻] = 10⁻{str(e).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))} mol/l. Eritmaning pH qiymati?", 14 - e,
                    [e, 14 - e + 1, 7], "", f"pOH = {e}; pH = 14 − pOH = {14 - e}."))
    for c, ph, kind in [("0,01", 2, "HCl"), ("0,001", 3, "HNO3"), ("0,1", 1, "HCl"), ("0,01", 12, "NaOH"), ("0,001", 11, "KOH"), ("0,1", 13, "NaOH")]:
        L.append(NQ(2, f"{c} M {pretty(kind)} eritmasining pH qiymati (to'liq dissotsilanadi deb hisoblang)?", ph,
                    [14 - ph, ph + 1, 7], "", f"{'[H⁺]' if ph < 7 else '[OH⁻]'} = {c} mol/l ⇒ pH = {ph}."))
    out["K9.3"] = L

    # --- K8.12: oksidlanish darajasi (yopiq + ochiq)
    L = []
    for f, el, val in OXID:
        v = ox_state(f, el) if val is None else val
        calc = ox_state(f, el)
        if v is None or (calc is not None and calc != v):
            continue
        sv = (f"+{v}" if v > 0 else str(v)).replace("-", "−")
        wrong = sorted({x for x in (-v, v - 2, v + 2, v + 1, 0) if x != v}, key=lambda x: abs(x - v))[:3]
        L.append(C(1 if f in ("H2SO4", "HNO3", "CO2", "NH3", "H2S", "SO2") else 2,
                   f"{pretty(f)} birikmasida {el} ning oksidlanish darajasi?", sv,
                   [(f"+{x}" if x > 0 else str(x)).replace("-", "−") for x in wrong],
                   f"Molekula neytral: yig'indi 0. Ma'lum darajalar (H +1, O −2, ishqoriy metallar +1) bo'yicha {el} = {sv}."))
    for f, el, val in OXID[:10]:
        v = ox_state(f, el)
        if v is None:
            continue
        L.append(O(3, f"{pretty(f)} da {el} ning oksidlanish darajasini yozing (masalan: +3 yoki −2).",
                   [(f"+{v}" if v > 0 else str(v)), str(v), (f"+{v}" if v > 0 else str(v)).replace("-", "−")],
                   f"{el} = {v:+d}."))
    out["K8.12"] = L

    # --- K8.6: moddalar sinflari — moslashtirish
    groups = [
        [("NaOH", "asos (ishqor)"), ("HCl", "kislota"), ("CO2", "kislotali oksid")],
        [("CaO", "asosli oksid"), ("ZnO", "amfoter oksid"), ("NaHCO3", "nordon tuz")],
        [("H2SO4", "kislota"), ("Fe(OH)3", "erimaydigan asos"), ("K2SO4", "o'rta tuz")],
        [("P2O5", "kislotali oksid"), ("KOH", "asos (ishqor)"), ("Al2O3", "amfoter oksid")],
        [("MgO", "asosli oksid"), ("H3PO4", "kislota"), ("CaCO3", "o'rta tuz")],
        [("SO3", "kislotali oksid"), ("Cu(OH)2", "erimaydigan asos"), ("KHSO4", "nordon tuz")],
    ]
    L = [M(2, [(pretty(a), b) for a, b in g], "; ".join(f"{pretty(a)} — {b}" for a, b in g) + ".") for g in groups]
    # gaz — xossa
    L.append(M(2, [("Kislorod (O₂)", "yonishni quvvatlaydi"), ("Vodorod (H₂)", "eng yengil gaz"), ("Ammiak (NH₃)", "o'tkir hidli, suvda yaxshi eriydi")],
               "O₂ yonishni quvvatlaydi; H₂ — eng yengil gaz; NH₃ — o'tkir hidli va suvda juda yaxshi eriydi."))
    L.append(M(2, [("CaCO₃", "ohaktosh (bo'r, marmar)"), ("NaCl", "osh tuzi"), ("CuSO₄·5H₂O", "mis kuporosi")],
               "CaCO₃ — ohaktosh/bo'r/marmar; NaCl — osh tuzi; CuSO₄·5H₂O — mis kuporosi."))
    L.append(M(2, [("Metan", "CH₄"), ("Etilen", "C₂H₄"), ("Atsetilen", "C₂H₂")], "Metan CH₄, etilen C₂H₄, atsetilen C₂H₂."))
    L.append(M(2, [("Etanol", "C₂H₅OH"), ("Sirka kislota", "CH₃COOH"), ("Glyukoza", "C₆H₁₂O₆")], "Etanol C₂H₅OH, sirka kislota CH₃COOH, glyukoza C₆H₁₂O₆."))
    out["K8.6"] = L
    return out


# ================================================================== BIOLOGIYA
def _gametes(genes: list) -> dict:
    """genes: ['Aa','Bb',...] -> {gameta: ehtimol}"""
    res = {"": Fraction(1)}
    for g in genes:
        nxt = {}
        for k, p in res.items():
            for al in g:
                nxt[k + al] = nxt.get(k + al, 0) + p / 2
        res = nxt
    return res


def _norm_gt(pair: str) -> str:
    return "".join(sorted(pair, key=lambda c: (c.lower(), c.islower())))


def cross_prob(p1: list, p2: list, target: list) -> Fraction:
    """Har bir gen mustaqil: P = Π P(gen_i target_i)."""
    pr = Fraction(1)
    for g1, g2, t in zip(p1, p2, target):
        cnt = sum(1 for a in g1 for b in g2 if _norm_gt(a + b) == _norm_gt(t))
        pr *= Fraction(cnt, 4)
    return pr


def pheno_prob(p1: list, p2: list, dominant: list) -> Fraction:
    """dominant[i] True — i-gen bo'yicha dominant fenotip (to'liq dominantlik)."""
    pr = Fraction(1)
    for g1, g2, dom in zip(p1, p2, dominant):
        cnt = sum(1 for a in g1 for b in g2 if (any(c.isupper() for c in a + b)) == dom)
        pr *= Fraction(cnt, 4)
    return pr


def frac_str(fr: Fraction) -> str:
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)


def bio() -> dict:
    out: dict = {}
    comp = {"A": "T", "T": "A", "G": "C", "C": "G"}

    # --- B9.2: Chargaff qoidasi, DNK uzunligi va vodorod bog'lar (yopiq + ochiq + chizma)
    L = []
    for a in [10, 15, 18, 20, 22, 24, 26, 28, 30, 32, 35, 38, 40, 12]:
        g = 50 - a
        L.append(NQ(1, f"DNK molekulasida adenin (A) {a}% ni tashkil qiladi. Guanin (G) necha foiz?", g, [a, 100 - 2 * a, 50 + a, 2 * g], "%",
                    f"A = T = {a}%; A + G = 50% ⇒ G = 50 − {a} = {g}%."))
    for a, gq in [(600, 400), (300, 200), (450, 150), (120, 180), (240, 360), (500, 250), (800, 200), (150, 350)]:
        total = 2 * (a + gq)
        h = 2 * a + 3 * gq
        L.append(NQ(2, f"Ikki zanjirli DNK fragmentida {a} ta adenin va {gq} ta guaninli nukleotid bor. Fragmentdagi jami nukleotidlar soni?",
                    total, [a + gq, total * 2, 2 * a + 3 * gq], "ta", f"A = T = {a}, G = C = {gq} ⇒ jami 2·({a}+{gq}) = {total}."))
        L.append(NQ(3, f"DNK fragmentida {a} ta adenin va {gq} ta guaninli nukleotid bor. Ikki zanjir orasidagi vodorod bog'lar soni?",
                    h, [3 * a + 2 * gq, 2 * (a + gq), h * 2], "ta", f"A–T juftida 2 ta, G–C juftida 3 ta bog': 2·{a} + 3·{gq} = {h}."))
        L.append(O(3, f"Ikki zanjirli DNK bo'lagida {a} ta A va {gq} ta G nukleotid bor. Vodorod bog'lar sonini yozing.", [str(h)],
                   f"2·{a} + 3·{gq} = {h}."))
    for bp in [60, 90, 120, 150, 300, 450, 600, 1000, 1500, 2400]:
        Ln = bp * 0.34
        L.append(NQ(2, f"Ikki zanjirli DNK fragmenti {bp} juft nukleotiddan iborat. Uning uzunligini toping (nukleotidlar orasidagi masofa 0,34 nm).",
                    Ln, [bp * 2 * 0.34, bp / 0.34, Ln / 2], "nm", f"l = {bp}·0,34 = {num(Ln)} nm (juftlar soniga ko'paytiriladi)."))
    for seq, hide in [("ATGC", 1), ("GCTA", 2), ("TTAG", 3), ("CAGT", 0), ("AGCT", 2), ("GATC", 1), ("CTGA", 3), ("TACG", 0)]:
        ans = comp[seq[hide]]
        L.append(C(1, f"Chizmada DNK qo'sh zanjirining bo'lagi tasvirlangan (1-zanjir: {'-'.join(seq)}). 2-zanjirdagi «?» o'rnida qaysi nukleotid turadi?",
                   ans, [x for x in "ATGC" if x != ans][:3], f"Komplementarlik: A–T, G–C ⇒ {seq[hide]} qarshisida {ans}.", fig=dna_pair(seq, hide)))
    out["B9.2"] = L

    # --- B11.5: molekulyar biologiya (oqsil – iRNK – gen)
    L = []
    for k in [50, 80, 100, 120, 150, 200, 240, 300, 360, 500]:
        L.append(NQ(1, f"Oqsil molekulasi {k} ta aminokislotadan iborat. Uni kodlovchi iRNK dagi nukleotidlar soni (stop-kodonsiz)?", 3 * k,
                    [k, 6 * k, 3 * k + 3], "ta", f"Har bir aminokislota — 1 kodon (3 nukleotid): {k}·3 = {3 * k}."))
        L.append(NQ(2, f"Oqsil {k} ta aminokislotadan iborat. Shu oqsilni kodlovchi gen (ikki zanjirli DNK) dagi nukleotidlar soni (stop-kodonsiz)?", 6 * k,
                    [3 * k, 2 * k, 6 * k + 6], "ta", f"iRNK: 3·{k} = {3 * k}; DNK ikki zanjirli: 2·{3 * k} = {6 * k}."))
    for n in [303, 453, 603, 903, 1203, 363]:
        aa = n // 3 - 1
        L.append(NQ(3, f"iRNK molekulasi {n} ta nukleotiddan iborat va oxirida bitta stop-kodon bor. Sintezlanadigan oqsildagi aminokislotalar soni?", aa,
                    [n // 3, n, aa * 2], "ta", f"Kodonlar: {n}/3 = {n // 3}; stop-kodon aminokislota kodlamaydi ⇒ {aa}."))
        L.append(O(3, f"{n} nukleotidli iRNK (oxirida bitta stop-kodon) asosida nechta aminokislotali oqsil hosil bo'ladi? Sonni yozing.", [str(aa)],
                   f"{n}/3 − 1 = {aa}."))
    for k in [100, 150, 200, 250, 300]:
        L.append(NQ(2, f"Aminokislotaning o'rtacha molekulyar massasi 110 Da. {k * 110} Da massali oqsilda nechta aminokislota bor?", k,
                    [k * 3, k * 110 / 100, k / 2], "ta", f"{k * 110} / 110 = {k}."))
    out["B11.5"] = L

    # --- B10.5: Mendel — gametalar, sinflar, ehtimollar (yopiq + ochiq)
    L = []
    for n in range(1, 6):
        g = "".join("AaBbCcDdEe"[2 * i:2 * i + 2] for i in range(n))
        L.append(NQ(1, f"{g} genotipli organizm necha xil gameta hosil qiladi (genlar mustaqil irsiylanadi)?", 2 ** n,
                    [2 * n, n, 2 ** (n + 1)], "xil", f"Gameta turlari 2ⁿ = 2^{n} = {2 ** n}."))
        if n >= 2:
            L.append(NQ(2, f"{g} × {g} chatishtirishda F₂ da nechta genotip sinfi hosil bo'ladi?", 3 ** n, [2 ** n, 4 ** n, 3 * n], "ta",
                        f"Genotip sinflari 3ⁿ = {3 ** n}."))
            L.append(NQ(2, f"{g} × {g} chatishtirishda (to'liq dominantlik) nechta fenotip sinfi hosil bo'ladi?", 2 ** n, [3 ** n, 4 ** n, 2 * n + 1], "ta",
                        f"Fenotip sinflari 2ⁿ = {2 ** n}."))
    crosses = [
        (["Aa", "Bb"], ["Aa", "Bb"], ["aa", "bb"]), (["Aa", "Bb"], ["aa", "bb"], ["aa", "bb"]), (["Aa", "Bb"], ["Aa", "bb"], ["aa", "bb"]),
        (["Aa", "Bb"], ["Aa", "Bb"], ["AA", "BB"]), (["Aa", "Bb"], ["Aa", "Bb"], ["Aa", "Bb"]), (["AA", "Bb"], ["aa", "Bb"], ["Aa", "bb"]),
        (["Aa", "BB"], ["Aa", "bb"], ["aa", "Bb"]), (["Aa", "Bb", "Cc"], ["Aa", "Bb", "Cc"], ["aa", "bb", "cc"]),
        (["Aa", "Bb", "Cc"], ["aa", "bb", "cc"], ["Aa", "bb", "Cc"]), (["Aa", "Bb", "cc"], ["Aa", "bb", "Cc"], ["aa", "bb", "cc"]),
    ]
    for p1, p2, t in crosses:
        fr = cross_prob(p1, p2, t)
        P1, P2, T = "".join(p1), "".join(p2), "".join(_norm_gt(x) for x in t)
        wrong = [fr * 2, fr / 2, fr * 4 if fr * 4 <= 1 else fr * 3 / 2, Fraction(1, 4), Fraction(9, 16)]
        wr = []
        for w in wrong:
            if w != fr and 0 < w <= 1 and pct(w) not in wr and pct(w) != pct(fr):
                wr.append(pct(w))
        L.append(C(2 if len(p1) == 2 else 3, f"{P1} × {P2} chatishtirishda {T} genotipli nasllarning ulushi qancha (genlar mustaqil)?",
                   pct(fr), wr[:3], f"Har bir gen alohida: " + " · ".join(f"P({_norm_gt(x)})" for x in t) + f" = {frac_str(fr)} = {pct(fr)}."))
        L.append(O(3, f"{P1} × {P2} chatishtirishda {T} genotipli nasllar ehtimolini kasr ko'rinishida yozing (masalan 1/8).",
                   [frac_str(fr), dec(fr), dec(fr).replace(",", "."), dec(fr * 100) + "%"], f"{frac_str(fr)}."))
    for p1, p2, dom in [(["Aa", "Bb"], ["Aa", "Bb"], [True, True]), (["Aa", "Bb"], ["Aa", "Bb"], [True, False]),
                        (["Aa", "Bb"], ["aa", "bb"], [True, True]), (["Aa", "Bb"], ["Aa", "Bb"], [False, False])]:
        fr = pheno_prob(p1, p2, dom)
        desc = " va ".join(("dominant" if d else "retsessiv") + f" ({'A' if i == 0 else 'B'} geni bo'yicha)" for i, d in enumerate(dom))
        wr = [pct(x) for x in (Fraction(9, 16), Fraction(3, 16), Fraction(1, 16), Fraction(1, 4), Fraction(1, 2)) if x != fr][:3]
        L.append(C(2, f"{''.join(p1)} × {''.join(p2)} (to'liq dominantlik): {desc} fenotipli nasllar ulushi?", pct(fr), wr,
                   f"Fenotiplar ehtimoli ko'paytiriladi: {frac_str(fr)} = {pct(fr)}."))
    out["B10.5"] = L

    # --- B10.4: Xardi–Vaynberg
    L = []
    for q2p in [1, 4, 9, 16, 25, 36, 49, 64, 81]:
        q = math.sqrt(q2p / 100)
        p = 1 - q
        het = 2 * p * q * 100
        domh = p * p * 100
        L.append(NQ(3, f"Populyatsiyada retsessiv belgili (aa) individlar {q2p}% ni tashkil etadi. Geterozigotalar (Aa) ulushi necha foiz (Xardi–Vaynberg)?",
                    het, [100 - q2p, q2p * 2, domh if abs(domh - het) > 1e-9 else het / 2], "%",
                    f"q² = {num(q2p / 100)} ⇒ q = {num(q)}, p = {num(p)}; 2pq = 2·{num(p)}·{num(q)} = {num(het / 100)} = {num(het)}%."))
        L.append(NQ(3, f"Populyatsiyada aa genotipli individlar {q2p}%. Dominant gomozigotalar (AA) ulushi necha foiz?", domh,
                    [100 - q2p, het, (100 - q2p) / 2], "%", f"q = {num(q)}, p = {num(p)} ⇒ p² = {num(domh)}%."))
    for q2p, N in [(4, 1000), (16, 500), (1, 10000), (9, 2000), (25, 400)]:
        q = math.sqrt(q2p / 100)
        het = 2 * (1 - q) * q * N
        L.append(O(3, f"{N} ta individdan iborat populyatsiyada retsessiv gomozigotalar {q2p}%. Geterozigotalar sonini toping.", [num(het)],
                   f"q = {num(q)}, 2pq = {num(2 * (1 - q) * q)} ⇒ {num(het)} ta."))
    out["B10.4"] = L

    # --- B10.8: ozuqa zanjiri, 10% qoidasi (chizmali)
    L = []
    names = ["O'simlik", "Chigirtka", "Qurbaqa", "Ilon", "Burgut"]
    for E in [10000, 20000, 50000, 80000, 100000, 5000, 30000, 200000]:
        for lvl in (2, 3, 4):
            val = E / 10 ** (lvl - 1)
            vals = [E if i == 0 else ("?" if i == lvl - 1 else "") for i in range(lvl)]
            L.append(NQ(2, f"Chizmadagi ozuqa zanjirida produtsentlar {E} kJ energiya to'pladi. 10% qoidasiga ko'ra {names[lvl - 1].lower()} ({lvl - 1}-tartib konsument) qancha energiya oladi (kJ)?",
                        val, [E / 10 ** lvl, E / 10 ** (lvl - 2) if lvl > 1 else E, val * 2], "kJ",
                        f"Har bir pog'onaga ~10% o'tadi: {E}·0,1^{lvl - 1} = {num(val)} kJ.", fig=food_chain(names[:lvl], vals)))
    for m in [1, 2, 5, 10, 3]:
        L.append(NQ(2, f"O'simlik → chigirtka → qurbaqa → ilon zanjirida ilon massasi {m} kg ortishi uchun qancha o'simlik massasi kerak (10% qoidasi)?",
                    m * 1000, [m * 100, m * 10, m * 10000], "kg", f"Uch pog'ona: {m}·10·10·10 = {m * 1000} kg."))
    out["B10.8"] = L

    # --- B9.3: energiya almashinuvi (maktab darsligi: to'liq parchalanishda 38 ATF)
    L = []
    for n in [1, 2, 3, 5, 0.5, 4, 10]:
        L.append(NQ(1 if n in (1, 2) else 2, f"{num(n)} mol glyukoza kislorodli sharoitda to'liq parchalanganda necha mol ATF hosil bo'ladi?", 38 * n,
                    [2 * n, 36 * n, 6 * n], "mol", f"1 mol glyukoza → 38 mol ATF (glikolizda 2 + kislorodli bosqichda 36) ⇒ {num(38 * n)} mol."))
        L.append(NQ(2, f"{num(n)} mol glyukoza glikolizga (kislorodsiz bosqich) uchraganda necha mol ATF hosil bo'ladi?", 2 * n,
                    [38 * n, 36 * n, n], "mol", f"Glikolizda har mol glyukozadan 2 mol ATF ⇒ {num(2 * n)} mol."))
        L.append(NQ(2, f"{num(n)} mol glyukoza to'liq oksidlanganda necha mol CO₂ ajraladi?", 6 * n, [2 * n, 12 * n, 38 * n], "mol",
                    f"C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O ⇒ {num(6 * n)} mol CO₂."))
    out["B9.3"] = L

    # --- moslashtirish (aniq, darslik faktlari)
    out["B9.4"] = [
        M(2, [("Mitoxondriya", "ATF sintezi (hujayra nafasi)"), ("Ribosoma", "oqsil sintezi"), ("Lizosoma", "hujayra ichi hazmi")],
          "Mitoxondriya — energiya (ATF); ribosoma — oqsil sintezi; lizosoma — hazm fermentlari."),
        M(2, [("Xloroplast", "fotosintez"), ("Yadro", "irsiy axborotni saqlash"), ("Golji apparati", "moddalarni to'plash va chiqarish")],
          "Xloroplast — fotosintez; yadro — DNK; Golji — sekretsiya."),
        M(2, [("Sentriolalar", "bo'linish urchug'ini hosil qilish"), ("Hujayra membranasi", "tanlab o'tkazuvchanlik"), ("Ribosoma", "oqsil sintezi")],
          "Sentriolalar — urchuq; membrana — tanlab o'tkazish; ribosoma — oqsil."),
    ]
    out["B8.5"] = [
        M(2, [("Insulin", "oshqozon osti bezi"), ("Tiroksin", "qalqonsimon bez"), ("Adrenalin", "buyrak usti bezi")],
          "Insulin — oshqozon osti bezi; tiroksin — qalqonsimon bez; adrenalin — buyrak usti bezining mag'iz qavati."),
        M(2, [("Somatotropin (o'sish gormoni)", "gipofiz"), ("Insulin", "oshqozon osti bezi"), ("Tiroksin", "qalqonsimon bez")],
          "O'sish gormoni gipofizda ishlab chiqariladi."),
        M(2, [("Insulin yetishmasligi", "qandli diabet"), ("O'sish gormoni bolalikda kam", "pakanalik"), ("Tiroksin bolalikda kam", "kretinizm")],
          "Insulin kamligi — qandli diabet; somatotropin kamligi — pakanalik; tiroksin kamligi (bolalikda) — kretinizm."),
    ]
    out["B9.7"] = [
        M(2, [("C vitamini", "singa (lavsha)"), ("D vitamini", "raxit"), ("B₁ vitamini", "beri-beri")],
          "C — singa; D — raxit; B₁ — beri-beri."),
        M(2, [("A vitamini", "shapko'rlik"), ("C vitamini", "singa (lavsha)"), ("D vitamini", "raxit")], "A yetishmasa — shapko'rlik."),
    ]
    out["B8.3"] = [
        M(2, [("Eritrotsitlar", "kislorod tashish"), ("Leykotsitlar", "organizmni himoya qilish"), ("Trombotsitlar", "qon ivishi")],
          "Eritrotsit — O₂ tashish (gemoglobin); leykotsit — himoya; trombotsit — qon ivishi."),
    ]
    return out


# ================================================================== PAKETLARGA QO'SHISH
def extend(packs):
    gens = {"chemistry": chem, "biology": bio}
    for pack in packs:
        g = gens.get(pack["subject"])
        if not g:
            continue
        by_code = {t["code"]: t for t in pack["topics"]}
        have = {q["question"].strip().lower() for q in pack["questions"]}
        try:
            items_by_code = g()
        except Exception:  # noqa: BLE001
            import logging
            logging.getLogger(__name__).exception("gen_v229 %s xatosi", pack["subject"])
            continue
        for code, items in items_by_code.items():
            t = by_code.get(code)
            if not t:
                continue
            uniq = []
            for it in items:
                key = (it.get("q") or "|".join(a for a, _ in it.get("pairs", []))).strip().lower()
                if not key or key in have:
                    continue
                if it.get("kind") == "c" and (len(it["w"]) < 3 or len({it["a"], *it["w"]}) < len(it["w"]) + 1):
                    continue
                have.add(key)
                uniq.append(it)
            if uniq:
                pack["questions"].extend(expand(t["name"], t["grade"], uniq, t.get("block", "")))
    return packs
