"""v215: matematika, fizika va kimyo uchun HISOBLANADIGAN savollar.

Har bir javob kod orqali hisoblanadi (qo'lda yozilmaydi), shuning uchun to'g'ri javob xato bo'lishi mumkin emas.
Xato variantlar — o'quvchilar odatda qiladigan xatolar (formula chalkashligi, birlik, daraja) asosida tuziladi.
Mavjud mavzu nomlariga qo'shiladi (yangi mavzu yaratilmaydi). Takror savollar avtomatik filtrlanadi.
"""
import math
import re
from itertools import product
from ._dsl import expand, validate
from ._ph import N, ON, fmt

G = 10  # erkin tushish tezlanishi (maktab masalalarida)


def _clean(x):
    return abs(x - round(x, 4)) < 1e-9


def _wrongs(x, errs):
    out = []
    for e in errs:
        if e is None or isinstance(e, complex):
            continue
        try:
            if not math.isfinite(e):
                continue
        except TypeError:
            continue
        if fmt(e) == fmt(x) or any(fmt(e) == fmt(o) for o in out):
            continue
        if (x >= 0 and e < 0) or abs(round(e, 2) - e) > 1e-9 or abs(e) > max(60 * abs(x), 100):
            continue
        out.append(e)
    for e in (x * 2, x / 2, x + 1, x - 1, x * 10, x / 10, x + 2, x * 3, x + 5):
        if len(out) >= 3:
            break
        if fmt(e) != fmt(x) and not any(fmt(e) == fmt(o) for o in out) and _clean(e):
            out.append(e)
    return out[:3]


def Q_(d, text, x, errs, unit, expl, openq=False):
    text = re.sub(r"(?<=\d)\.(?=\d)", ",", text)
    if not _clean(x):
        return None
    if openq:
        return ON(d, text + (f" ({unit})" if unit else ""), x, expl)
    w = _wrongs(x, errs)
    if len(w) < 3:
        return None
    return N(d, text, x, w, unit, expl)


def _add(lst, item):
    if item is not None:
        lst.append(item)


# =============================================================== MATEMATIKA
def math_items():
    D = {}
    # ---- M8.1 Kvadrat ildiz
    L = D.setdefault("M8.1", [])
    for a, b in [(3, 4), (5, 12), (6, 8), (7, 24), (9, 12), (8, 15)]:
        c = math.isqrt(a * a + b * b)
        if c * c == a * a + b * b:
            _add(L, Q_(2, f"√({a * a} + {b * b}) ning qiymatini toping.", c, [a + b, c * c, c + 1], "", f"{a * a} + {b * b} = {c * c}, √{c * c} = {c}."))
    for k in (12, 13, 15, 17, 18, 19, 21, 25):
        _add(L, Q_(1, f"√{k * k} ni hisoblang.", k, [k * 2, k * k, k - 1], "", f"{k}² = {k * k}."))
    for a, k in [(2, 3), (3, 2), (5, 2), (7, 3), (4, 5)]:
        _add(L, Q_(2, f"√({a}²·{k}²) ni hisoblang.", a * k, [a + k, a * k * k, a * a * k], "", f"√({a * a}·{k * k}) = {a}·{k} = {a * k}."))
    # ---- M8.2 Kvadrat tenglama va diskriminant
    L = D.setdefault("M8.2", [])
    for a, b, c in [(1, -5, 6), (1, 2, -8), (2, -3, -2), (1, -6, 9), (3, 1, -2), (1, -7, 12), (2, 5, -3), (1, 4, 4), (1, 0, -16), (4, -4, 1)]:
        Dsc = b * b - 4 * a * c
        _add(L, Q_(1, f"{a if a != 1 else ''}x² {'+' if b >= 0 else '−'} {abs(b) if abs(b) != 1 else ''}x {'+' if c >= 0 else '−'} {abs(c)} = 0 tenglamaning diskriminantini toping.".replace("  ", " "), Dsc,
                   [b * b + 4 * a * c, b * b - 2 * a * c, -b * b - 4 * a * c], "", f"D = b² − 4ac = {b * b} − {4 * a * c} = {Dsc}."))
        if Dsc >= 0:
            r1, r2 = (-b - math.sqrt(Dsc)) / (2 * a), (-b + math.sqrt(Dsc)) / (2 * a)
            _add(L, Q_(2, f"{a}x² {'+' if b >= 0 else '−'} {abs(b)}x {'+' if c >= 0 else '−'} {abs(c)} = 0 tenglama ildizlarining yig'indisini toping.", r1 + r2, [-(r1 + r2), r1 * r2, r1 - r2], "", f"Vyet teoremasi: x₁ + x₂ = −b/a = {fmt(-b / a)}."))
            _add(L, Q_(3, f"{a}x² {'+' if b >= 0 else '−'} {abs(b)}x {'+' if c >= 0 else '−'} {abs(c)} = 0 tenglama ildizlarining ko'paytmasini toping.", r1 * r2, [-(r1 * r2), -b / a, r1 + r2], "", f"x₁·x₂ = c/a = {fmt(c / a)}.", openq=True))
    # ---- M9.3 Progressiyalar
    L = D.setdefault("M9.3", [])
    for a1, d, n in [(2, 3, 10), (5, 4, 8), (1, 2, 15), (10, -2, 7), (3, 5, 12), (7, 3, 9), (4, 6, 11), (20, -3, 6)]:
        an = a1 + (n - 1) * d
        Sn = (a1 + an) * n / 2
        _add(L, Q_(1, f"Arifmetik progressiyada a₁ = {a1}, d = {d}. a_{n} ni toping.", an, [a1 + n * d, a1 * n + d, an + d], "", f"a_n = a₁ + (n − 1)d = {a1} + {n - 1}·{d} = {an}."))
        _add(L, Q_(2, f"Arifmetik progressiyada a₁ = {a1}, d = {d}. Dastlabki {n} ta had yig'indisini toping.", Sn, [Sn + an, Sn - a1, (a1 + an) * n], "", f"S_n = (a₁ + a_n)·n/2 = ({a1} + {an})·{n}/2 = {fmt(Sn)}.", openq=(n % 2 == 1)))
    for b1, q, n in [(2, 2, 6), (3, 2, 5), (1, 3, 5), (5, 2, 4), (2, 3, 4), (4, 2, 7), (6, 2, 5)]:
        bn = b1 * q ** (n - 1)
        Sn = b1 * (q ** n - 1) / (q - 1)
        _add(L, Q_(2, f"Geometrik progressiyada b₁ = {b1}, q = {q}. b_{n} ni toping.", bn, [b1 * q * n, b1 * q ** n, b1 + (n - 1) * q], "", f"b_n = b₁·q^(n−1) = {b1}·{q}^{n - 1} = {fmt(bn)}."))
        _add(L, Q_(3, f"Geometrik progressiyada b₁ = {b1}, q = {q}. Dastlabki {n} ta had yig'indisini toping.", Sn, [Sn - b1, bn * q, b1 * (q ** n + 1) / (q + 1)], "", f"S_n = b₁(qⁿ − 1)/(q − 1) = {fmt(Sn)}."))
    # ---- M9.4 Kombinatorika
    L = D.setdefault("M9.4", [])
    for n, k in [(5, 2), (6, 3), (7, 2), (8, 3), (10, 2), (9, 4), (6, 2), (7, 3), (10, 3), (8, 2)]:
        c, a = math.comb(n, k), math.perm(n, k)
        _add(L, Q_(2, f"C({n}, {k}) ning qiymatini toping.", c, [a, n * k, c + k], "", f"C(n,k) = n!/(k!(n−k)!) = {c}."))
        _add(L, Q_(2, f"{n} ta elementdan {k} tasini tanlab, tartibli joylashtirishlar soni A({n}, {k}) ni toping.", a, [c, n ** k, math.factorial(n)], "", f"A(n,k) = n!/(n−k)! = {a}."))
    for n in (4, 5, 6, 7):
        _add(L, Q_(1, f"{n}! ni hisoblang.", math.factorial(n), [n * n, sum(range(1, n + 1)), math.factorial(n - 1)], "", f"{n}! = {math.factorial(n)}."))
    for n in (4, 5, 6):
        _add(L, Q_(2, f"{n} ta turli kitobni javonga necha xil usulda qator qilib terish mumkin?", math.factorial(n), [n * n, math.factorial(n) * 2, math.factorial(n - 1)], "", f"P = {n}! = {math.factorial(n)}.", openq=True))
    # ---- M9.5 Ehtimollik
    L = D.setdefault("M9.5", [])
    for s in (7, 8, 9, 10, 6, 5, 4):
        cnt = sum(1 for a, b in product(range(1, 7), repeat=2) if a + b == s)
        _add(L, Q_(2, f"Ikkita o'yin soqqasi tashlanganda tushgan ochkolar yig'indisi {s} bo'lish usullari soni nechta?", cnt, [cnt + 1, 36 - cnt, s], "", f"Mumkin bo'lgan juftliklar sanab chiqiladi: {cnt} ta (jami 36)."))
    for w, b in [(3, 5), (4, 6), (2, 8), (5, 5), (6, 4), (7, 3)]:
        p = w / (w + b)
        _add(L, Q_(1, f"Qutida {w} ta oq va {b} ta qora shar bor. Tasodifiy olingan sharning oq bo'lish ehtimolini toping (o'nli kasr).", p, [b / (w + b), w / b, 1 / (w + b)], "", f"P = {w}/{w + b} = {fmt(p)}."))
    # ---- M9.6 Statistika
    L = D.setdefault("M9.6", [])
    for arr in ([3, 5, 7, 9, 11], [2, 4, 4, 6, 9], [10, 20, 30, 40, 50, 60], [1, 3, 3, 5, 8], [12, 15, 15, 18, 20], [4, 8, 6, 2, 10], [7, 7, 8, 9, 14]):
        mean = sum(arr) / len(arr)
        srt = sorted(arr)
        med = srt[len(srt) // 2] if len(srt) % 2 else (srt[len(srt) // 2 - 1] + srt[len(srt) // 2]) / 2
        s = ", ".join(map(str, arr))
        _add(L, Q_(1, f"{s} sonlarining o'rta arifmetigini toping.", mean, [med, max(arr), sum(arr)], "", f"({'+'.join(map(str, arr))})/{len(arr)} = {fmt(mean)}."))
        _add(L, Q_(2, f"{s} sonlarining medianasini toping.", med, [mean + 1, srt[0], srt[-1]], "", f"Tartiblangan qatorda o'rtadagi qiymat: {fmt(med)}."))
    # ---- M10.3 Logarifm
    L = D.setdefault("M10.3", [])
    for b, k in [(2, 5), (3, 4), (5, 3), (2, 8), (10, 4), (7, 2), (4, 3), (6, 3)]:
        v = b ** k
        _add(L, Q_(1, f"log_{b} {v} ni hisoblang.", k, [v // b, b * k, k + 1], "", f"{b}^{k} = {v}, demak log_{b} {v} = {k}."))
    for b, x, y in [(2, 4, 8), (3, 9, 3), (2, 16, 2), (5, 25, 5), (3, 27, 3), (2, 32, 2)]:
        r = math.log(x * y, b)
        _add(L, Q_(2, f"log_{b} {x} + log_{b} {y} ni hisoblang.", round(r), [math.log(x, b) * math.log(y, b), x + y, round(r) + 1], "", f"log_{b}({x}·{y}) = log_{b} {x * y} = {round(r)}."))
    # ---- M10.1 Trigonometriya
    L = D.setdefault("M10.1", [])
    for name, val in [("sin 30°", 0.5), ("cos 60°", 0.5), ("sin 90°", 1), ("cos 0°", 1), ("tg 45°", 1), ("cos 90°", 0), ("sin 0°", 0), ("sin 150°", 0.5), ("cos 120°", -0.5), ("sin 210°", -0.5), ("tg 135°", -1), ("cos 180°", -1), ("sin 270°", -1)]:
        _add(L, Q_(1, f"{name} ning qiymatini toping.", val, [-val, 1 - val, val + 1], "", f"Jadval qiymati: {name} = {fmt(val)}."))
    # ---- M11.1 Hosila
    L = D.setdefault("M11.1", [])
    for a, b, c, x0 in [(1, 2, 3, 2), (3, -1, 5, 1), (2, 4, 0, 3), (1, 0, -4, 5), (5, 3, 2, 1), (4, -8, 1, 2), (2, -6, 7, 4), (1, 6, 9, 2)]:
        dv = 2 * a * x0 + b
        _add(L, Q_(2, f"f(x) = {a if a != 1 else ''}x² {'+' if b >= 0 else '−'} {abs(b)}x {'+' if c >= 0 else '−'} {abs(c)} bo'lsa, f′({x0}) ni toping.", dv, [a * x0 * x0 + b * x0 + c, a * x0 + b, 2 * a * x0], "", f"f′(x) = {2 * a}x {'+' if b >= 0 else '−'} {abs(b)}; f′({x0}) = {dv}."))
    for n, x0 in [(3, 2), (4, 1), (5, 1), (3, 3), (4, 2)]:
        dv = n * x0 ** (n - 1)
        _add(L, Q_(1, f"f(x) = x^{n} funksiyaning x = {x0} nuqtadagi hosilasini toping.", dv, [x0 ** n, n * x0 ** n, (n - 1) * x0 ** (n - 1)], "", f"f′(x) = {n}x^{n - 1}; f′({x0}) = {dv}."))
    # ---- M11.2 Integral
    L = D.setdefault("M11.2", [])
    for k, a, b in [(1, 0, 2), (2, 0, 3), (1, 1, 3), (3, 0, 2), (2, 1, 4), (4, 0, 1), (1, 0, 4), (6, 0, 2)]:
        v = k * (b ** 3 - a ** 3) / 3
        if _clean(v):
            _add(L, Q_(2, f"{a} dan {b} gacha {k if k != 1 else ''}x² ning aniq integralini hisoblang: ∫₍{a}₎^{b} {k if k != 1 else ''}x² dx.", v, [k * (b ** 2 - a ** 2) / 2, k * (b ** 3 - a ** 3), v + k], "", f"{k}x³/3 ning chegaralardagi ayirmasi = {fmt(v)}."))
    # ---- M8.14 Chiziqli tenglamalar tizimi
    L = D.setdefault("M8.14", [])
    for x, y in [(2, 1), (3, 2), (4, 1), (1, 5), (5, 3), (2, 6), (7, 2)]:
        a1, b1, a2, b2 = 1, 1, 1, -1
        _add(L, Q_(1, f"x + y = {x + y}, x − y = {x - y} tizimda x ni toping.", x, [y, x + y, x - y], "", "Tenglamalarni qo'shsak: 2x = " + str(2 * x) + f", x = {x}."))
        _add(L, Q_(2, f"2x + y = {2 * x + y}, x + 2y = {x + 2 * y} tizimda x + y ni toping.", x + y, [x - y, x * y, 2 * x + y], "", f"Qo'shsak: 3(x+y) = {3 * (x + y)}, x + y = {x + y}."))
    # ---- M8.4 / M8.10 foiz
    L = D.setdefault("M8.10", [])
    for base, p in [(80, 25), (150, 20), (240, 15), (60, 5), (320, 12.5), (900, 4), (45, 40), (500, 18)]:
        v = base * p / 100
        _add(L, Q_(1, f"{base} ning {fmt(p)}% ini toping.", v, [base + v, base - v, base / p], "", f"{base}·{fmt(p / 100)} = {fmt(v)}."))
    for base, p in [(200, 20), (150, 10), (80, 25), (400, 15), (60, 50)]:
        up = base * (1 + p / 100)
        _add(L, Q_(2, f"Mahsulot narxi {base} so'm edi, u {p}% ga oshdi. Yangi narx necha so'm?", up, [base * p / 100, base * (1 - p / 100), up + p], "", f"{base}·{fmt(1 + p / 100)} = {fmt(up)}."))
        dn = base * (1 - p / 100)
        _add(L, Q_(2, f"Mahsulot narxi {base} so'm edi, u {p}% ga arzonlashdi. Yangi narx necha so'm?", dn, [base * p / 100, base * (1 + p / 100), dn - p], "", f"{base}·{fmt(1 - p / 100)} = {fmt(dn)}.", openq=True))
    # ---- M8.18 / M8.19 / M8.17 / M8.20 Geometriya
    L = D.setdefault("M8.18", [])
    for a, b in [(6, 4), (9, 5), (12, 7), (8, 8), (15, 4), (11, 6)]:
        _add(L, Q_(1, f"To'g'ri to'rtburchakning tomonlari {a} va {b}. Yuzini toping.", a * b, [2 * (a + b), a + b, a * a], "", f"S = a·b = {a * b}."))
        _add(L, Q_(1, f"To'g'ri to'rtburchakning tomonlari {a} va {b}. Perimetrini toping.", 2 * (a + b), [a * b, a + b, 2 * a * b], "", f"P = 2(a + b) = {2 * (a + b)}."))
    L = D.setdefault("M8.17", [])
    for a, h in [(10, 6), (8, 5), (12, 9), (14, 4), (7, 8), (16, 3)]:
        _add(L, Q_(1, f"Uchburchakning asosi {a}, balandligi {h}. Yuzini toping.", a * h / 2, [a * h, a + h, a * h / 3], "", f"S = a·h/2 = {fmt(a * h / 2)}."))
    for A, B in [(50, 60), (40, 75), (35, 80), (65, 45), (30, 90)]:
        _add(L, Q_(1, f"Uchburchakning ikki burchagi {A}° va {B}°. Uchinchi burchagini toping.", 180 - A - B, [90 - A, 360 - A - B, A + B], "°", "Burchaklar yig'indisi 180°."))
    L = D.setdefault("M8.20", [])
    for a, b in [(3, 4), (5, 12), (8, 15), (6, 8), (9, 12), (7, 24), (20, 21)]:
        c = math.isqrt(a * a + b * b)
        if c * c == a * a + b * b:
            _add(L, Q_(1, f"To'g'ri burchakli uchburchakning katetlari {a} va {b}. Gipotenuzasini toping.", c, [a + b, a * b, c * c], "", f"c² = {a * a} + {b * b} = {c * c}, c = {c}."))
            _add(L, Q_(2, f"To'g'ri burchakli uchburchakning gipotenuzasi {c}, katetlaridan biri {a}. Ikkinchi katetini toping.", b, [c - a, c + a, b * b], "", f"b² = {c * c} − {a * a} = {b * b}."))
    L = D.setdefault("M8.19", [])
    for r in (2, 3, 4, 5, 6, 7, 10):
        _add(L, Q_(1, f"Doira radiusi {r}. Yuzi π ning necha baravariga teng?", r * r, [2 * r, r, r * r * 2], "", f"S = πr² = {r * r}π."))
        _add(L, Q_(1, f"Aylana radiusi {r}. Uzunligi π ning necha baravariga teng?", 2 * r, [r, r * r, 4 * r], "", f"C = 2πr = {2 * r}π."))
    L = D.setdefault("M10.6", [])
    for a, b, c in [(2, 3, 4), (5, 4, 3), (6, 2, 5), (3, 3, 3), (7, 2, 2), (4, 5, 6)]:
        _add(L, Q_(1, f"To'g'ri burchakli parallelepipedning o'lchamlari {a}, {b}, {c}. Hajmini toping.", a * b * c, [a + b + c, 2 * (a * b + b * c + a * c), a * b * c * 2], "", f"V = abc = {a * b * c}."))
        _add(L, Q_(2, f"To'g'ri burchakli parallelepipedning o'lchamlari {a}, {b}, {c}. To'la sirtini toping.", 2 * (a * b + b * c + a * c), [a * b * c, a * b + b * c + a * c, 2 * a * b * c], "", f"S = 2(ab + bc + ac) = {2 * (a * b + b * c + a * c)}."))
    for a in (2, 3, 4, 5, 6):
        _add(L, Q_(1, f"Qirrasi {a} bo'lgan kubning hajmini toping.", a ** 3, [a * a, 6 * a * a, 3 * a], "", f"V = a³ = {a ** 3}."))
    L = D.setdefault("M10.11", [])
    for n in (5, 6, 8, 10, 12, 9, 7):
        _add(L, Q_(2, f"Qavariq {n} burchakning ichki burchaklari yig'indisi necha gradus?", (n - 2) * 180, [n * 180, (n - 1) * 180, (n - 2) * 90], "°", f"(n − 2)·180° = {(n - 2) * 180}°."))
    for n in (6, 8, 9, 10, 12, 5):
        _add(L, Q_(2, f"Muntazam {n} burchakning bitta ichki burchagi necha gradus?", (n - 2) * 180 / n, [360 / n, (n - 2) * 90 / n, (n - 1) * 180 / n], "°", f"(n − 2)·180°/n = {fmt((n - 2) * 180 / n)}°."))
    # ---- M9.7 Vyet
    L = D.setdefault("M9.7", [])
    for p, q in [(5, 6), (7, 10), (-3, -10), (9, 20), (-2, -15), (8, 15), (11, 30)]:
        _add(L, Q_(2, f"x² {'−' if p > 0 else '+'} {abs(p)}x {'+' if q > 0 else '−'} {abs(q)} = 0 tenglama ildizlari kvadratlarining yig'indisini toping (Vyet teoremasi bilan).", p * p - 2 * q, [p * p, p * p + 2 * q, p - 2 * q], "", f"x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂ = {p * p} − {2 * q} = {p * p - 2 * q}."))
    # ---- M8.8 EKUB/EKUK
    L = D.setdefault("M8.8", [])
    for a, b in [(12, 18), (24, 36), (15, 25), (28, 42), (16, 24), (30, 45), (18, 27), (20, 30)]:
        g = math.gcd(a, b)
        _add(L, Q_(1, f"{a} va {b} sonlarining EKUB ini toping.", g, [a * b // g, a + b, g * 2], "", f"EKUB({a}, {b}) = {g}."))
        _add(L, Q_(2, f"{a} va {b} sonlarining EKUK ini toping.", a * b // g, [g, a * b, a + b], "", f"EKUK = {a}·{b}/EKUB = {a * b // g}."))
    # ---- M8.9 daraja
    L = D.setdefault("M8.9", [])
    for a, m, n in [(2, 3, 4), (3, 2, 3), (5, 2, 2), (2, 5, 2), (3, 3, 1), (10, 2, 3)]:
        _add(L, Q_(1, f"{a}^{m}·{a}^{n} ning qiymatini toping.", a ** (m + n), [a ** (m * n), (a * a) ** (m + n), a ** m + a ** n], "", f"Ko'rsatkichlar qo'shiladi: {a}^{m + n} = {a ** (m + n)}."))
    # ---- M10.2/M11.3 koordinata
    L = D.setdefault("M11.3", [])
    for (x1, y1, x2, y2) in [(0, 0, 3, 4), (1, 1, 4, 5), (2, 3, 5, 7), (-1, 2, 2, 6), (0, 0, 5, 12), (1, 2, 7, 10)]:
        dd = math.hypot(x2 - x1, y2 - y1)
        _add(L, Q_(2, f"A({x1}; {y1}) va B({x2}; {y2}) nuqtalar orasidagi masofani toping.", dd, [abs(x2 - x1) + abs(y2 - y1), dd * dd, abs(x2 - x1)], "", f"AB = √(({x2}−({x1}))² + ({y2}−({y1}))²) = {fmt(dd)}."))
    L = D.setdefault("M10.5", [])
    for (a1, a2, b1, b2) in [(1, 2, 3, 4), (2, -1, 4, 3), (3, 0, 2, 5), (1, 1, 2, 2), (4, 3, -3, 4), (2, 5, 1, -2)]:
        dot = a1 * b1 + a2 * b2
        _add(L, Q_(2, f"a⃗({a1}; {a2}) va b⃗({b1}; {b2}) vektorlarning skalyar ko'paytmasini toping.", dot, [a1 * b2 + a2 * b1, a1 * b1 - a2 * b2, a1 + a2 + b1 + b2], "", f"a·b = {a1}·{b1} + {a2}·{b2} = {dot}."))
    return D


# =============================================================== FIZIKA
def phys_items():
    D = {}
    L = D.setdefault("P7.2", [])
    for s, t in [(120, 4), (150, 3), (200, 5), (90, 6), (360, 12), (45, 9), (240, 8)]:
        _add(L, Q_(1, f"Jism {t} s da {s} m yo'l bosdi. O'rtacha tezligi necha m/s?", s / t, [s * t, s - t, t / s], "m/s", f"v = s/t = {fmt(s / t)} m/s."))
    for v, t in [(5, 12), (20, 3), (15, 4), (8, 25), (30, 6)]:
        _add(L, Q_(1, f"Jism {v} m/s tezlik bilan {t} s harakatlandi. Bosib o'tgan yo'li necha metr?", v * t, [v + t, v / t, v * t * 2], "m", f"s = v·t = {v * t} m.", openq=True))
    for kmh in (36, 72, 54, 90, 108, 18):
        _add(L, Q_(2, f"{kmh} km/soat tezlik necha m/s ga teng?", kmh / 3.6, [kmh * 3.6, kmh / 60, kmh / 36], "m/s", f"{kmh}/3,6 = {fmt(kmh / 3.6)} m/s."))
    L = D.setdefault("P9.1", [])
    for v0, a, t in [(0, 2, 5), (5, 3, 4), (10, 2, 6), (0, 4, 3), (2, 2, 8), (20, -2, 5), (0, 5, 4), (3, 1, 10)]:
        v = v0 + a * t
        s = v0 * t + a * t * t / 2
        _add(L, Q_(1, f"Jism v₀ = {v0} m/s boshlang'ich tezlik va a = {a} m/s² tezlanish bilan {t} s harakatlandi. Oxirgi tezligi?", v, [v0 + a, a * t, v0 * t], "m/s", f"v = v₀ + at = {v0} + {a}·{t} = {v} m/s."))
        _add(L, Q_(2, f"Jism v₀ = {v0} m/s boshlang'ich tezlik va a = {a} m/s² tezlanish bilan {t} s harakatlandi. Bosib o'tgan yo'li?", s, [v0 * t + a * t * t, v * t, a * t * t], "m", f"s = v₀t + at²/2 = {fmt(s)} m."))
    for s, t in [(100, 10), (50, 5), (200, 10), (72, 6), (18, 3)]:
        a = 2 * s / t ** 2
        _add(L, Q_(2, f"Tinch holatdan tekis tezlanuvchan harakat boshlagan jism {t} s da {s} m yo'l bosdi. Tezlanishi?", a, [s / t, s / t ** 2, 2 * s / t], "m/s²", f"s = at²/2 → a = 2s/t² = {fmt(a)} m/s²."))
    L = D.setdefault("P9.3", [])
    for t in (1, 2, 3, 4, 5, 6):
        _add(L, Q_(1, f"Jism erkin tushmoqda (g = 10 m/s²). {t} s da qancha balandlikdan o'tadi?", G * t * t / 2, [G * t, G * t * t, G * t / 2], "m", f"h = gt²/2 = {fmt(G * t * t / 2)} m."))
        _add(L, Q_(1, f"Jism erkin tushmoqda (g = 10 m/s²). {t} s oxirida tezligi?", G * t, [G * t * t / 2, G / t, G + t], "m/s", f"v = gt = {G * t} m/s."))
    for h in (20, 45, 80, 125, 5, 180):
        t = math.sqrt(2 * h / G)
        _add(L, Q_(2, f"Jism {h} m balandlikdan erkin tushadi (g = 10 m/s²). Yerga tushish vaqti?", t, [h / G, 2 * h / G, h / 2], "s", f"t = √(2h/g) = {fmt(t)} s."))
    for v0 in (10, 20, 30, 40, 25, 50):
        _add(L, Q_(2, f"Jism yuqoriga {v0} m/s tezlik bilan otildi (g = 10 m/s²). Maksimal ko'tarilish balandligi?", v0 * v0 / (2 * G), [v0 * v0 / G, v0 / G, v0 * v0 / 4], "m", f"H = v₀²/(2g) = {fmt(v0 * v0 / (2 * G))} m."))
    L = D.setdefault("P9.6", [])
    for m, a in [(2, 3), (5, 4), (10, 2), (4, 6), (3, 5), (8, 2), (1.5, 4), (6, 3)]:
        _add(L, Q_(1, f"Massasi {fmt(m)} kg jismga {fmt(a)} m/s² tezlanish beruvchi kuch necha N?", m * a, [m + a, m / a, a / m], "N", f"F = ma = {fmt(m * a)} N."))
    for F, m in [(20, 4), (30, 6), (50, 10), (12, 3), (45, 9), (100, 25)]:
        _add(L, Q_(1, f"Massasi {m} kg jismga {F} N kuch ta'sir qilmoqda. Tezlanishi?", F / m, [F * m, m / F, F - m], "m/s²", f"a = F/m = {fmt(F / m)} m/s².", openq=True))
    L = D.setdefault("P7.4", [])
    for m in (2, 5, 8, 12, 20, 0.5):
        _add(L, Q_(1, f"Massasi {fmt(m)} kg jismning og'irligi (g = 10 m/s²)?", m * G, [m / G, m + G, m * G * 2], "N", f"P = mg = {fmt(m * G)} N."))
    for k, x in [(200, 0.05), (100, 0.1), (500, 0.02), (50, 0.2), (400, 0.03), (1000, 0.01)]:
        _add(L, Q_(2, f"Bikrligi {k} N/m bo'lgan prujina {fmt(x)} m ga cho'zildi. Elastiklik kuchi?", k * x, [k / x, k * x * x, k + x], "N", f"F = kx = {fmt(k * x)} N."))
    L = D.setdefault("P7.5", [])
    for F, S in [(100, 0.5), (200, 0.1), (60, 0.02), (500, 2), (90, 0.03), (1200, 0.4)]:
        _add(L, Q_(1, f"{fmt(F)} N kuch {fmt(S)} m² yuzaga tekis ta'sir qiladi. Bosim necha Pa?", F / S, [F * S, S / F, F - S], "Pa", f"p = F/S = {fmt(F / S)} Pa."))
    for rho, h in [(1000, 2), (1000, 5), (800, 3), (1000, 10), (1000, 0.5), (800, 10)]:
        _add(L, Q_(2, f"Zichligi {rho} kg/m³ bo'lgan suyuqlikning {fmt(h)} m chuqurlikdagi gidrostatik bosimi (g = 10)?", rho * G * h, [rho * h, rho * G, rho * G * h / 2], "Pa", f"p = ρgh = {fmt(rho * G * h)} Pa."))
    L = D.setdefault("P7.6", [])
    for rho, V in [(1000, 0.002), (1000, 0.01), (800, 0.005), (1000, 0.5), (1000, 0.03), (900, 0.02)]:
        _add(L, Q_(2, f"Hajmi {fmt(V)} m³ jism zichligi {rho} kg/m³ bo'lgan suyuqlikka to'liq botirildi (g = 10). Arximed kuchi?", rho * G * V, [rho * V, G * V, rho * G / V], "N", f"F = ρgV = {fmt(rho * G * V)} N."))
    L = D.setdefault("P6.2", [])
    for m, V in [(200, 0.1), (54, 0.02), (780, 0.1), (500, 0.5), (90, 0.1), (1200, 0.4)]:
        _add(L, Q_(1, f"Massasi {m} kg, hajmi {fmt(V)} m³ jismning zichligi (kg/m³)?", m / V, [m * V, V / m, m - V], "kg/m³", f"ρ = m/V = {fmt(m / V)} kg/m³."))
    L = D.setdefault("P7.8", [])
    for F, s in [(50, 4), (120, 3), (30, 10), (200, 2.5), (15, 8), (80, 6)]:
        _add(L, Q_(1, f"{F} N kuch jismni kuch yo'nalishida {fmt(s)} m ga ko'chirdi. Bajarilgan ish?", F * s, [F / s, F + s, F * s / 2], "J", f"A = Fs = {fmt(F * s)} J."))
    for A, t in [(600, 10), (1200, 20), (500, 5), (900, 30), (2400, 60)]:
        _add(L, Q_(1, f"{t} s da {A} J ish bajarildi. Quvvat?", A / t, [A * t, t / A, A - t], "W", f"N = A/t = {fmt(A / t)} W.", openq=True))
    for m, v in [(2, 10), (4, 5), (10, 3), (1, 20), (5, 4), (3, 6)]:
        _add(L, Q_(1, f"Massasi {m} kg jism {v} m/s tezlik bilan harakatlanmoqda. Kinetik energiyasi?", m * v * v / 2, [m * v, m * v * v, m * v * v / 4], "J", f"E = mv²/2 = {fmt(m * v * v / 2)} J."))
    for m, h in [(2, 5), (10, 3), (5, 8), (4, 12), (1, 50), (20, 2)]:
        _add(L, Q_(1, f"Massasi {m} kg jism {h} m balandlikda (g = 10). Potensial energiyasi?", m * G * h, [m * h, m * G, m * G * h / 2], "J", f"E = mgh = {m * G * h} J."))
    L = D.setdefault("P9.11", [])
    for m, v in [(2, 5), (10, 3), (0.5, 20), (4, 8), (6, 7), (3, 9)]:
        _add(L, Q_(1, f"Massasi {fmt(m)} kg jism {v} m/s tezlik bilan harakatlanmoqda. Impulsi?", m * v, [m * v * v / 2, m / v, m + v], "kg·m/s", f"p = mv = {fmt(m * v)} kg·m/s."))
    for m1, v1, m2 in [(2, 6, 4), (3, 8, 6), (5, 10, 5), (1, 12, 3), (4, 9, 5)]:
        v = m1 * v1 / (m1 + m2)
        _add(L, Q_(3, f"{m1} kg massali, {v1} m/s tezlikli jism tinch turgan {m2} kg massali jismga urilib, ular birga harakatlandi (noelastik zarba). Umumiy tezlik?", v, [v1 / 2, m1 * v1 / m2, (m1 + m2) * v1 / m1], "m/s", f"m₁v₁ = (m₁ + m₂)v → v = {fmt(v)} m/s."))
    L = D.setdefault("P9.5", [])
    for v, r in [(10, 5), (20, 10), (6, 3), (8, 4), (15, 5), (12, 6)]:
        _add(L, Q_(2, f"Jism {r} m radiusli aylana bo'ylab {v} m/s tezlik bilan tekis harakatlanmoqda. Markazga intilma tezlanishi?", v * v / r, [v / r, v * v * r, v * r], "m/s²", f"a = v²/r = {fmt(v * v / r)} m/s²."))
    L = D.setdefault("P8.2", [])
    for c, m, dt in [(4200, 2, 10), (4200, 0.5, 20), (900, 3, 50), (460, 5, 100), (380, 4, 25), (4200, 1, 5)]:
        _add(L, Q_(2, f"Solishtirma issiqlik sig'imi {c} J/(kg·°C) bo'lgan {fmt(m)} kg moddani {dt}°C ga isitish uchun qancha issiqlik kerak?", c * m * dt, [c * m, c * dt, c * m * dt / 2], "J", f"Q = cmΔt = {fmt(c * m * dt)} J."))
    L = D.setdefault("P8.3", [])
    for lam, m in [(330000, 2), (330000, 0.5), (84000, 3), (25000, 10), (330000, 4)]:
        _add(L, Q_(2, f"Erish issiqligi {lam} J/kg bo'lgan {fmt(m)} kg moddani erish haroratida to'liq eritish uchun qancha issiqlik kerak?", lam * m, [lam / m, lam + m, lam * m * 2], "J", f"Q = λm = {fmt(lam * m)} J."))
    L = D.setdefault("P11.5", [])
    for U, R in [(12, 4), (220, 55), (9, 3), (36, 6), (6, 2), (100, 20), (24, 8)]:
        _add(L, Q_(1, f"Zanjir qismida kuchlanish {U} V, qarshilik {R} Ω. Tok kuchi?", U / R, [U * R, R / U, U - R], "A", f"I = U/R = {fmt(U / R)} A."))
    for r1, r2 in [(3, 6), (4, 12), (10, 15), (6, 12), (20, 5), (8, 8)]:
        rs, rp = r1 + r2, r1 * r2 / (r1 + r2)
        _add(L, Q_(1, f"{r1} Ω va {r2} Ω qarshiliklar ketma-ket ulangan. Umumiy qarshilik?", rs, [rp, r1 * r2, abs(r1 - r2)], "Ω", f"R = R₁ + R₂ = {rs} Ω."))
        _add(L, Q_(2, f"{r1} Ω va {r2} Ω qarshiliklar parallel ulangan. Umumiy qarshilik?", rp, [rs, r1 * r2, (r1 + r2) / 2], "Ω", f"R = R₁R₂/(R₁ + R₂) = {fmt(rp)} Ω."))
    L = D.setdefault("P11.8", [])
    for U, I in [(220, 5), (12, 3), (110, 2), (9, 0.5), (24, 10), (36, 2.5)]:
        _add(L, Q_(1, f"{U} V kuchlanishda {fmt(I)} A tok o'tmoqda. Quvvat?", U * I, [U / I, I / U, U + I], "W", f"P = UI = {fmt(U * I)} W."))
    for I, R, t in [(2, 10, 5), (3, 4, 10), (5, 2, 20), (1, 50, 30), (4, 5, 6)]:
        _add(L, Q_(2, f"R = {R} Ω qarshilikdan I = {I} A tok {t} s o'tganda ajraladigan issiqlik (Joul–Lens)?", I * I * R * t, [I * R * t, I * R, I * I * R], "J", f"Q = I²Rt = {I * I * R * t} J."))
    L = D.setdefault("P11.1", [])
    for q1, q2, r in [(2e-6, 3e-6, 0.3), (1e-6, 1e-6, 0.1), (4e-6, 5e-6, 0.2), (2e-6, 2e-6, 0.6), (3e-6, 6e-6, 0.9)]:
        F = 9e9 * q1 * q2 / r ** 2
        if _clean(F):
            _add(L, Q_(3, f"{fmt(q1)} C va {fmt(q2)} C nuqtaviy zaryadlar vakuumda {fmt(r)} m masofada (k = 9·10⁹). O'zaro ta'sir kuchi?", F, [F * r, 9e9 * q1 * q2 / r, F / 2], "N", f"F = kq₁q₂/r² = {fmt(F)} N."))
    L = D.setdefault("P10.3", [])
    L = D.setdefault("P10.4", [])
    for p1, V1, V2 in [(100, 6, 2), (200, 4, 8), (150, 10, 5), (300, 2, 6), (120, 5, 10), (60, 12, 4)]:
        p2 = p1 * V1 / V2
        _add(L, Q_(2, f"O'zgarmas temperaturada gaz hajmi {V1} l dan {V2} l ga o'zgardi. Dastlabki bosim {p1} kPa edi. Oxirgi bosim?", p2, [p1 * V2 / V1, p1 + V1 - V2, p1 * V1 * V2], "kPa", f"Boyl–Mariott: p₁V₁ = p₂V₂ → p₂ = {fmt(p2)} kPa."))
    for T1, T2 in [(300, 600), (200, 400), (250, 500), (300, 450), (273, 546), (400, 200)]:
        _add(L, Q_(2, f"O'zgarmas hajmda gaz absolyut temperaturasi {T1} K dan {T2} K ga o'zgarsa, bosim necha marta o'zgaradi?", T2 / T1, [T1 / T2, T2 - T1, T2 / T1 + 1], "marta", f"Sharl qonuni: p₂/p₁ = T₂/T₁ = {fmt(T2 / T1)}."))
    L = D.setdefault("P11.16", [])
    for v, f_ in [(340, 170), (340, 680), (3, 6), (12, 4), (300, 50), (20, 5)]:
        _add(L, Q_(1, f"To'lqin tezligi {v} m/s, chastotasi {f_} Hz. To'lqin uzunligi?", v / f_, [v * f_, f_ / v, v - f_], "m", f"λ = v/f = {fmt(v / f_)} m."))
    for T in (0.5, 0.2, 2, 4, 0.25, 0.1):
        _add(L, Q_(1, f"Tebranish davri {T} s. Chastotasi?", 1 / T, [T, T * 2, 1 - T], "Hz", f"ν = 1/T = {fmt(1 / T)} Hz."))
    L = D.setdefault("P11.19", [])
    for a in (20, 30, 35, 40, 50, 25):
        _add(L, Q_(1, f"Tushish burchagi {a}° bo'lsa, qaytish burchagi necha gradus?", a, [90 - a, 2 * a, 180 - a], "°", "Qaytish burchagi tushish burchagiga teng."))
    L = D.setdefault("P11.20", [])
    for d, f_ in [(30, 15), (20, 10), (60, 20), (40, 20), (12, 6), (45, 15)]:
        fi = d * f_ / (d - f_)
        _add(L, Q_(3, f"Fokus masofasi {f_} sm bo'lgan yig'uvchi linzadan {d} sm masofada buyum turibdi. Tasvir linzadan qancha masofada hosil bo'ladi?", fi, [d - f_, d + f_, d * f_ / (d + f_)], "sm", f"1/f = 1/d + 1/f′ → f′ = {fmt(fi)} sm."))
    for f_ in (0.5, 0.25, 0.2, 0.1, 2, 0.4):
        _add(L, Q_(1, f"Linzaning fokus masofasi {f_} m. Optik kuchi necha dioptriya?", 1 / f_, [f_, f_ * 2, 10 * f_], "dptr", f"D = 1/F = {fmt(1 / f_)} dptr."))
    L = D.setdefault("P11.29", [])
    for T, t in [(10, 30), (5, 20), (8, 24), (2, 10), (6, 18), (4, 16)]:
        k = t / T
        if k == int(k):
            n0 = 2 ** int(k) * 10
            _add(L, Q_(2, f"Yarim yemirilish davri {T} kun bo'lgan moddaning dastlabki miqdori {n0} g. {t} kundan so'ng qancha qoladi?", n0 / 2 ** int(k), [n0 / int(k), n0 / 2, n0 - 2 * int(k)], "g", f"N = N₀/2^(t/T) = {n0}/2^{int(k)} = {fmt(n0 / 2 ** int(k))} g."))
    L = D.setdefault("P11.4", [])
    for c1, c2 in [(2, 3), (4, 4), (6, 3), (10, 10), (5, 20), (3, 6)]:
        _add(L, Q_(2, f"{c1} μF va {c2} μF sig'imli kondensatorlar parallel ulangan. Umumiy sig'im?", c1 + c2, [c1 * c2 / (c1 + c2), c1 * c2, abs(c1 - c2)], "μF", f"Parallel: C = C₁ + C₂ = {c1 + c2} μF."))
        cs = c1 * c2 / (c1 + c2)
        _add(L, Q_(2, f"{c1} μF va {c2} μF sig'imli kondensatorlar ketma-ket ulangan. Umumiy sig'im?", cs, [c1 + c2, c1 * c2, (c1 + c2) / 2], "μF", f"Ketma-ket: 1/C = 1/C₁ + 1/C₂ → C = {fmt(cs)} μF."))
    L = D.setdefault("P11.14", [])
    L = D.setdefault("P11.15", [])
    for n1, n2, U1 in [(100, 400, 50), (200, 50, 120), (50, 500, 22), (1000, 100, 220), (300, 900, 40)]:
        U2 = U1 * n2 / n1
        _add(L, Q_(2, f"Transformatorning birlamchi chulg'amida {n1} o'ram, ikkilamchisida {n2} o'ram. Birlamchi kuchlanish {U1} V bo'lsa, ikkilamchi kuchlanish?", U2, [U1 * n1 / n2, U1 + n2 - n1, U1 * n2], "V", f"U₂/U₁ = n₂/n₁ → U₂ = {fmt(U2)} V."))
    L = D.setdefault("P11.25", [])
    for A, E in [(2, 5), (3, 7), (1.5, 4.5), (4, 9), (2.5, 6)]:
        _add(L, Q_(2, f"Chiqish ishi {fmt(A)} eV bo'lgan metallga energiyasi {fmt(E)} eV foton tushdi. Fotoelektronning maksimal kinetik energiyasi?", E - A, [E + A, E / A, A - E if A > E else A], "eV", f"Eynshteyn: hν = A + E_k → E_k = {fmt(E - A)} eV."))
    return D


# =============================================================== KIMYO
AM = {"H": 1, "C": 12, "N": 14, "O": 16, "F": 19, "Na": 23, "Mg": 24, "Al": 27, "Si": 28, "P": 31, "S": 32, "Cl": 35.5, "K": 39, "Ca": 40, "Fe": 56, "Cu": 64, "Zn": 65, "Br": 80, "Ag": 108, "Ba": 137}
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def _M(parts):
    return sum(AM[s] * n for s, n in parts)


def _f(parts):
    return "".join(s + (str(n).translate(SUB) if n > 1 else "") for s, n in parts)


CMP = [
    ([("H", 2), ("O", 1)], "suv"), ([("C", 1), ("O", 2)], "karbonat angidrid"), ([("N", 1), ("H", 3)], "ammiak"),
    ([("H", 2), ("S", 1), ("O", 4)], "sulfat kislota"), ([("Na", 1), ("O", 1), ("H", 1)], "natriy gidroksid"), ([("Ca", 1), ("C", 1), ("O", 3)], "kalsiy karbonat"),
    ([("H", 1), ("N", 1), ("O", 3)], "nitrat kislota"), ([("Mg", 1), ("O", 1)], "magniy oksidi"), ([("Al", 2), ("O", 3)], "alyuminiy oksidi"), ([("Fe", 2), ("O", 3)], "temir(III) oksidi"),
    ([("C", 6), ("H", 12), ("O", 6)], "glyukoza"), ([("C", 2), ("H", 6), ("O", 1)], "etanol"), ([("Cu", 1), ("S", 1), ("O", 4)], "mis(II) sulfat"), ([("Na", 1), ("Cl", 1)], "osh tuzi"),
    ([("K", 1), ("O", 1), ("H", 1)], "kaliy gidroksid"), ([("Ca", 1), ("O", 1), ("H", 1)], None), ([("C", 2), ("H", 4)], "etilen"), ([("C", 6), ("H", 6)], "benzol"), ([("Zn", 1), ("O", 1)], "rux oksidi"),
    ([("H", 3), ("P", 1), ("O", 4)], "fosfat kislota"), ([("N", 2), ("O", 5)], "azot(V) oksidi"), ([("S", 1), ("O", 3)], "oltingugurt(VI) oksidi"), ([("C", 3), ("H", 8)], "propan"), ([("C", 4), ("H", 10)], "butan"),
]


def chem_items():
    D = {}
    L = D.setdefault("K8.1", [])
    for parts, nm in CMP:
        if not nm:
            continue
        M = _M(parts)
        fm = _f(parts)
        _add(L, Q_(1, f"{fm} ({nm}) ning nisbiy molekulyar massasi (Mr) nechaga teng? (Cl = 35,5 deb oling)", M, [M + 2, M - 2, M * 2], "", f"Mr = " + " + ".join(f"{AM[s]}·{n}" if n > 1 else f"{AM[s]}" for s, n in parts) + f" = {fmt(M)}."))
    for parts, nm in CMP[:12]:
        M = _M(parts)
        for m in (M, 2 * M, M / 2):
            n = m / M
            if _clean(m) and _clean(n):
                _add(L, Q_(2, f"{fmt(m)} g {_f(parts)} necha mol modda bo'ladi?", n, [m * M, M / m, n + 1], "mol", f"n = m/M = {fmt(m)}/{fmt(M)} = {fmt(n)} mol.", openq=(m == 2 * M)))
        _add(L, Q_(2, f"{fmt(2)} mol {_f(parts)} ning massasi necha gramm?", 2 * M, [M, M / 2, 2 + M], "g", f"m = n·M = 2·{fmt(M)} = {fmt(2 * M)} g."))
    for n, k in [(0.5, 11.2), (2, 44.8), (1, 22.4), (3, 67.2), (0.25, 5.6), (4, 89.6)]:
        _add(L, Q_(1, f"{fmt(n)} mol gaz n.sh. da qancha hajm (litr) egallaydi?", k, [n / 22.4, n * 24, k * 2], "l", f"V = n·22,4 = {fmt(k)} l.", openq=True))
    for V in (11.2, 44.8, 67.2, 5.6, 112, 22.4):
        n = V / 22.4
        _add(L, Q_(1, f"n.sh. da {fmt(V)} l gaz necha mol bo'ladi?", n, [V * 22.4, V / 24, n + 1], "mol", f"n = V/22,4 = {fmt(n)} mol."))
    for n in (0.5, 2, 0.1, 3, 0.25):
        N_ = n * 6.02
        _add(L, Q_(2, f"{fmt(n)} mol moddada necha dona molekula bor? (Avogadro soni 6,02·10²³; javobda 10²³ ning koeffitsiyenti)", N_, [n / 6.02, n * 602, N_ * 10], "·10²³", f"N = n·Nₐ = {fmt(n)}·6,02·10²³ = {fmt(N_)}·10²³."))
    L = D.setdefault("K8.2", [])
    for parts, nm in CMP:
        if len(parts) < 2 or not nm:
            continue
        M = _M(parts)
        for s, n in parts[:1]:
            w = AM[s] * n / M * 100
            if _clean(w):
                _add(L, Q_(2, f"{_f(parts)} tarkibidagi {s} elementining massa ulushi necha foiz? (Cl = 35,5)", w, [100 - w, w / 2, w * 2], "%", f"w = Ar·n/Mr·100% = {fmt(AM[s] * n)}/{fmt(M)}·100% = {fmt(w)}%.", openq=False))
        for s, n in parts[1:2]:
            w = AM[s] * n / M * 100
            if _clean(w):
                _add(L, Q_(2, f"{_f(parts)} tarkibidagi {s} elementining massa ulushi necha foiz?", w, [100 - w, w / 2, w * 2], "%", f"w = {fmt(AM[s] * n)}/{fmt(M)}·100% = {fmt(w)}%."))
    L = D.setdefault("K8.7", [])
    for ms, mr in [(20, 200), (30, 150), (15, 300), (40, 160), (10, 250), (50, 400), (45, 180), (24, 120)]:
        w = ms / mr * 100
        _add(L, Q_(1, f"{ms} g tuz eritmaning {mr} g massasida erigan. Massa ulushi necha foiz?", w, [ms / (mr - ms) * 100, mr / ms, 100 - w], "%", f"w = m(modda)/m(eritma)·100% = {fmt(w)}%."))
    for mr, w in [(200, 10), (500, 20), (150, 40), (300, 15), (250, 8), (400, 25)]:
        ms = mr * w / 100
        _add(L, Q_(1, f"{mr} g {w}% li eritmada necha gramm erigan modda bor?", ms, [mr - ms, mr / w, ms * 2], "g", f"m = {mr}·{w}/100 = {fmt(ms)} g.", openq=True))
        _add(L, Q_(2, f"{mr} g {w}% li eritma tayyorlash uchun necha gramm suv kerak?", mr - ms, [ms, mr, mr + ms], "g", f"m(suv) = {mr} − {fmt(ms)} = {fmt(mr - ms)} g."))
    for m1, w1, w2 in [(200, 20, 10), (300, 30, 10), (100, 40, 20), (400, 15, 5), (250, 24, 12), (500, 10, 5)]:
        m2 = m1 * w1 / w2
        _add(L, Q_(3, f"{m1} g {w1}% li eritmani {w2}% li eritmagacha suyultirish uchun necha gramm suv qo'shish kerak?", m2 - m1, [m2, m1 * w2 / w1, m1 * (w1 - w2) / 100], "g", f"Modda massasi o'zgarmaydi: {fmt(m1 * w1 / 100)} g; yangi eritma {fmt(m2)} g; qo'shiladigan suv {fmt(m2 - m1)} g."))
    L = D.setdefault("K8.8", [])
    for n, V in [(2, 1), (1, 2), (0.5, 0.25), (3, 1.5), (0.1, 0.5), (4, 2), (1.5, 3), (0.6, 0.3)]:
        c = n / V
        _add(L, Q_(1, f"{fmt(n)} mol modda {fmt(V)} l eritmada erigan. Molyar konsentratsiya (mol/l)?", c, [n * V, V / n, c + 1], "mol/l", f"C = n/V = {fmt(c)} mol/l."))
    for cM, V, M in [(0.5, 2, 40), (1, 1, 98), (2, 0.5, 58.5), (0.1, 5, 40), (0.2, 0.5, 98), (1, 0.25, 40)]:
        m = cM * V * M
        _add(L, Q_(3, f"{fmt(cM)} M li {fmt(V)} l eritma tayyorlash uchun molyar massasi {fmt(M)} g/mol bo'lgan moddadan necha gramm kerak?", m, [cM * V, V * M, m * 2], "g", f"m = C·V·M = {fmt(m)} g."))
    L = D.setdefault("K9.3", [])
    for k in range(1, 14):
        _add(L, Q_(1, f"Eritmada [H⁺] = 10⁻{k} mol/l. pH nechaga teng?", k, [14 - k, k + 1, k - 1 if k > 1 else 7], "", f"pH = −lg[H⁺] = {k}."))
    for k in (2, 3, 4, 5, 9, 11, 12):
        _add(L, Q_(2, f"Eritmaning pH = {k}. Undagi [OH⁻] ning 10 ning manfiy darajasi (10⁻ˣ dagi x) nechaga teng? (25°C)", 14 - k, [k, 14 + k, 7 - k if k < 7 else 7], "", f"pOH = 14 − pH = {14 - k}."))
    L = D.setdefault("K10.3", [])
    for n in range(1, 9):
        M = 12 * n + 2 * n + 2
        _add(L, Q_(1, f"C{str(n).translate(SUB)}H{str(2 * n + 2).translate(SUB)} alkanning molyar massasi (g/mol)?", M, [M - 2, M + 2, 14 * n], "g/mol", f"M = 12·{n} + {2 * n + 2} = {M}."))
    for M in (30, 44, 58, 72, 86, 16, 100):
        n = (M - 2) / 14
        _add(L, Q_(2, f"Molyar massasi {M} g/mol bo'lgan alkan molekulasida nechta uglerod atomi bor?", n, [n + 1, n - 1 if n > 1 else 3, M / 12], "", f"CₙH₂ₙ₊₂: 14n + 2 = {M} → n = {fmt(n)}."))
    L = D.setdefault("K10.13", [])
    for m, parts in [(16, "CH₄"), (32, "CH₄"), (8, "CH₄"), (4, "CH₄")]:
        V = m / 16 * 22.4
        _add(L, Q_(2, f"{m} g metan (CH₄) to'liq yonganda n.sh. da necha litr CO₂ hosil bo'ladi? (CH₄ + 2O₂ → CO₂ + 2H₂O)", V, [V * 2, V / 2, m * 22.4], "l", f"n(CH₄) = {fmt(m / 16)} mol → n(CO₂) = {fmt(m / 16)} mol → V = {fmt(V)} l."))
    L = D.setdefault("K8.3", [])
    for mag, o2 in [(24, 16), (48, 32), (12, 8), (72, 48), (6, 4)]:
        _add(L, Q_(2, f"2Mg + O₂ → 2MgO. {mag} g magniy yonganda qancha (g) MgO hosil bo'ladi?", mag + o2, [mag, o2, (mag + o2) * 2], "g", f"Massa saqlanadi: {mag} + {o2} = {mag + o2} g (kislorod {o2} g sarflanadi)."))
    for m_caco3 in (100, 200, 50, 25, 10, 500):
        m = m_caco3 * 56 / 100
        _add(L, Q_(3, f"CaCO₃ → CaO + CO₂. {m_caco3} g CaCO₃ parchalanganda necha gramm CaO hosil bo'ladi? (Ca = 40)", m, [m_caco3 * 44 / 100, m_caco3 / 2, m_caco3], "g", f"n(CaCO₃) = {fmt(m_caco3 / 100)} mol; M(CaO) = 56; m = {fmt(m)} g."))
    L = D.setdefault("K9.12", [])
    for m_zn in (13, 6.5, 65, 32.5, 130):
        V = m_zn / 65 * 22.4
        _add(L, Q_(3, f"{fmt(m_zn)} g rux (Zn = 65) kislota bilan reaksiyaga kirishganda (Zn + 2HCl → ZnCl₂ + H₂) n.sh. da necha litr vodorod ajraladi?", V, [V * 2, V / 2, m_zn * 22.4], "l", f"n(Zn) = {fmt(m_zn / 65)} mol = n(H₂); V = {fmt(V)} l."))
    L = D.setdefault("K11.12", [])
    for m, w in [(200, 80), (500, 90), (250, 60), (400, 75), (100, 95), (150, 40)]:
        pure = m * w / 100
        _add(L, Q_(2, f"{m} g texnik namunada {w}% sof modda bor. Sof modda massasi?", pure, [m - pure, m / w, pure * 2], "g", f"m = {m}·{w}/100 = {fmt(pure)} g."))
    for th, pr in [(100, 80), (50, 90), (200, 75), (40, 50), (250, 60), (80, 95)]:
        _add(L, Q_(2, f"Reaksiyaning nazariy unumi {th} g, amalda {th * pr / 100:g} g mahsulot olindi. Unum necha foiz?", pr, [100 - pr, pr / 2, th - pr], "%", f"η = amaliy/nazariy·100% = {pr}%."))
    L = D.setdefault("K8.12", [])
    OX = [("H₂SO₄", "S", "+6"), ("HNO₃", "N", "+5"), ("KMnO₄", "Mn", "+7"), ("NH₃", "N", "−3"), ("SO₂", "S", "+4"), ("H₂S", "S", "−2"), ("K₂Cr₂O₇", "Cr", "+6"), ("CO₂", "C", "+4"), ("CH₄", "C", "−4"), ("Na₂SO₃", "S", "+4"), ("Cl₂O₇", "Cl", "+7"), ("HClO₃", "Cl", "+5"), ("P₂O₅", "P", "+5"), ("NO₂", "N", "+4"), ("Fe₂O₃", "Fe", "+3"), ("MnO₂", "Mn", "+4")]
    vals = ["−4", "−3", "−2", "+2", "+3", "+4", "+5", "+6", "+7"]
    from ._dsl import C
    for f_, el, ox in OX:
        wr = [v for v in vals if v != ox]
        # eng yaqin 3 ta qiymatni xato variant qilib olamiz
        wr.sort(key=lambda v: abs(int(v.replace("−", "-")) - int(ox.replace("−", "-"))))
        L.append(C(2, f"{f_} birikmasida {el} elementining oksidlanish darajasi qanday?", ox, wr[:3], f"Molekula neytral: oksidlanish darajalari yig'indisi 0. {el} = {ox}."))
    return D


# =============================================================== BIOLOGIYA
def bio_items():
    from ._dsl import C
    D = {}
    L = D.setdefault("B9.2", [])
    for tot, a in [(1000, 300), (2000, 600), (1200, 240), (800, 160), (3000, 900), (1500, 450), (2400, 720)]:
        g = tot // 2 - a
        _add(L, Q_(2, f"DNK molekulasida jami {tot} ta nukleotid bor, adenin (A) {a} ta. Guanin (G) nechta?", g, [a, tot - a, tot // 2], "", f"Chargaff qoidasi: A = T = {a}; G = C = ({tot} − 2·{a})/2 = {g}."))
        _add(L, Q_(2, f"DNKda jami {tot} ta nukleotid, A = {a} ta. Timin (T) nechta?", a, [g, tot - a, 2 * a], "", f"A = T bo'lgani uchun T = {a}."))
    for n in (100, 150, 200, 300, 500, 250):
        _add(L, Q_(1, f"DNKning bir zanjirida {n} ta nukleotid bor. Ikki zanjirli DNKda jami nechta nukleotid bo'ladi?", 2 * n, [n, n // 2, 4 * n], "", f"Ikkinchi zanjir komplementar: 2·{n} = {2 * n}."))
    L = D.setdefault("B9.6", [])
    for aa in (50, 100, 120, 200, 150, 300, 80, 250):
        _add(L, Q_(2, f"Oqsil {aa} ta aminokislotadan iborat. Uni kodlovchi iRNK qismida nechta nukleotid bor (stop-kodonsiz)?", 3 * aa, [aa, 2 * aa, 6 * aa], "", f"Har bir aminokislota 3 nukleotid (kodon): 3·{aa} = {3 * aa}."))
        _add(L, Q_(3, f"Oqsil {aa} ta aminokislotadan iborat. Uni kodlovchi ikki zanjirli DNK qismida nechta nukleotid bo'ladi (stop-kodonsiz)?", 6 * aa, [3 * aa, 2 * aa, 12 * aa], "", f"iRNK: 3·{aa}; DNK ikki zanjirli: 2·3·{aa} = {6 * aa}."))
    for nt in (300, 600, 900, 1200, 450, 750):
        _add(L, Q_(2, f"iRNK qismida {nt} ta nukleotid bor. U nechta aminokislotali oqsilni kodlaydi?", nt // 3, [nt, nt // 2, nt * 3], "", f"{nt}/3 = {nt // 3} ta kodon."))
    L = D.setdefault("B11.5", [])
    for n in (100, 200, 500, 1000, 1500, 2000):
        _add(L, Q_(2, f"DNKning bir zanjirida {n} ta nukleotid bor. Nukleotidlararo masofa 0,34 nm bo'lsa, DNK uzunligi necha nm?", n * 0.34, [n * 0.34 * 2, n * 3.4, n / 0.34], "nm", f"L = {n}·0,34 = {fmt(n * 0.34)} nm."))
    for n in (100, 200, 400, 600, 1000):
        _add(L, Q_(2, f"Bitta nukleotidning o'rtacha massasi 345 a.m.b. Bir zanjirli {n} nukleotidli DNK massasi (a.m.b.)?", 345 * n, [345 * n * 2, 345 + n, 345 / n], "", f"{n}·345 = {345 * n}."))
    L = D.setdefault("B10.5", [])
    for n in (1, 2, 3, 4, 5):
        _add(L, Q_(2, f"AaBb... genotipli organizmda {n} juft gen geterozigota holatda. U necha xil gameta hosil qiladi?", 2 ** n, [2 * n, n * n, 4 ** n], "", f"Gameta turlari soni 2ⁿ = {2 ** n}."))
        _add(L, Q_(3, f"{n} juft gen bo'yicha geterozigotalar chatishtirilganda F₂ da nechta turli genotip hosil bo'ladi (to'liq dominantlik)?", 3 ** n, [2 ** n, 4 ** n, 3 * n], "", f"Genotip sinflari 3ⁿ = {3 ** n}."))
    for tot in (160, 320, 480, 640, 800, 1200):
        _add(L, Q_(2, f"Aa × Aa chatishtirishdan {tot} ta nasl olindi. To'liq dominantlikda retsessiv (aa) fenotipli nechta nasl kutiladi?", tot // 4, [tot // 2, tot * 3 // 4, tot // 3], "", f"3:1 qonuniyat: retsessiv ulushi 1/4 → {tot // 4}."))
        _add(L, Q_(2, f"Aa × Aa chatishtirishdan {tot} ta nasl olindi. Dominant fenotipli nechta nasl kutiladi?", tot * 3 // 4, [tot // 4, tot // 2, tot], "", f"Dominant ulushi 3/4 → {tot * 3 // 4}."))
    L = D.setdefault("B10.4", [])
    for q2 in (0.04, 0.09, 0.16, 0.25, 0.01, 0.36, 0.49):
        q = round(math.sqrt(q2), 4)
        _add(L, Q_(2, f"Xardi–Vaynberg: retsessiv gomozigotalar (aa) ulushi {q2}. Retsessiv allel chastotasi q ni toping.", q, [q2, 1 - q, q2 / 2], "", f"q = √q² = {fmt(q)}."))
        _add(L, Q_(3, f"Xardi–Vaynberg: aa ulushi {q2}. Geterozigotalar (Aa) ulushi qancha?", round(2 * (1 - q) * q, 4), [q * q, 1 - q2, 2 * q], "", f"2pq = 2·{fmt(1 - q)}·{fmt(q)} = {fmt(round(2 * (1 - q) * q, 4))}."))
    L = D.setdefault("B9.3", [])
    for g in (1, 2, 3, 5, 10):
        _add(L, Q_(2, f"Aerob sharoitda {g} molekula glyukoza to'liq parchalanganda necha molekula ATF hosil bo'ladi (38 ATF/glyukoza)?", 38 * g, [2 * g, 36 * g, 18 * g], "", f"{g}·38 = {38 * g}."))
        _add(L, Q_(2, f"Anaerob glikoliz (bijg'ish) da {g} molekula glyukozadan nechta ATF hosil bo'ladi?", 2 * g, [38 * g, 36 * g, 4 * g], "", f"Glikoliz: 2 ATF/glyukoza → {2 * g}."))
    return D


# =============================================================== INGLIZ TILI
IRR = [("go", "went", "gone"), ("see", "saw", "seen"), ("take", "took", "taken"), ("write", "wrote", "written"), ("eat", "ate", "eaten"), ("drink", "drank", "drunk"), ("buy", "bought", "bought"), ("bring", "brought", "brought"),
       ("begin", "began", "begun"), ("break", "broke", "broken"), ("choose", "chose", "chosen"), ("come", "came", "come"), ("do", "did", "done"), ("drive", "drove", "driven"), ("fall", "fell", "fallen"), ("find", "found", "found"),
       ("fly", "flew", "flown"), ("forget", "forgot", "forgotten"), ("give", "gave", "given"), ("grow", "grew", "grown"), ("know", "knew", "known"), ("leave", "left", "left"), ("make", "made", "made"), ("meet", "met", "met"),
       ("read", "read", "read"), ("run", "ran", "run"), ("say", "said", "said"), ("sell", "sold", "sold"), ("sing", "sang", "sung"), ("sit", "sat", "sat"), ("speak", "spoke", "spoken"), ("swim", "swam", "swum"),
       ("teach", "taught", "taught"), ("tell", "told", "told"), ("think", "thought", "thought"), ("win", "won", "won"), ("wear", "wore", "worn"), ("steal", "stole", "stolen"), ("throw", "threw", "thrown"), ("ride", "rode", "ridden")]
PLUR = [("child", "children"), ("man", "men"), ("woman", "women"), ("tooth", "teeth"), ("foot", "feet"), ("mouse", "mice"), ("person", "people"), ("city", "cities"), ("box", "boxes"), ("leaf", "leaves"),
        ("knife", "knives"), ("wolf", "wolves"), ("bus", "buses"), ("baby", "babies"), ("potato", "potatoes"), ("goose", "geese"), ("church", "churches"), ("country", "countries"), ("day", "days"), ("life", "lives")]
COMP = [("big", "bigger", "the biggest"), ("good", "better", "the best"), ("bad", "worse", "the worst"), ("far", "farther", "the farthest"), ("happy", "happier", "the happiest"), ("hot", "hotter", "the hottest"),
        ("easy", "easier", "the easiest"), ("small", "smaller", "the smallest"), ("large", "larger", "the largest"), ("thin", "thinner", "the thinnest"), ("busy", "busier", "the busiest"), ("cheap", "cheaper", "the cheapest"),
        ("beautiful", "more beautiful", "the most beautiful"), ("expensive", "more expensive", "the most expensive"), ("difficult", "more difficult", "the most difficult"), ("interesting", "more interesting", "the most interesting")]
ORD = [(1, "first"), (2, "second"), (3, "third"), (4, "fourth"), (5, "fifth"), (8, "eighth"), (9, "ninth"), (12, "twelfth"), (20, "twentieth"), (21, "twenty-first"), (22, "twenty-second"), (30, "thirtieth"), (40, "fortieth"), (100, "hundredth")]
POSS = [("I", "mine", "my"), ("you", "yours", "your"), ("he", "his", "his"), ("she", "hers", "her"), ("we", "ours", "our"), ("they", "theirs", "their")]
OBJ = [("I", "me"), ("he", "him"), ("she", "her"), ("we", "us"), ("they", "them")]


def _bad_forms(good, pool):
    import random
    r = random.Random(good)
    c = [x for x in pool if x != good]
    r.shuffle(c)
    return c[:3]


def eng_items():
    from ._dsl import C, O
    D = {}
    L = D.setdefault("E2", [])
    pasts = [x[1] for x in IRR]
    for v, p2, pp in IRR:
        wrong = [pp if pp != p2 else v + "ed", v + "ed" if not v.endswith("e") else v + "d", _bad_forms(p2, pasts)[0]]
        wrong = [w for i, w in enumerate(wrong) if w != p2 and w not in wrong[:i]]
        for extra in pasts:
            if len(wrong) >= 3:
                break
            if extra != p2 and extra not in wrong:
                wrong.append(extra)
        L.append(C(1, f"Past Simple: yesterday she ____ ({v}) it.", p2, wrong[:3], f"{v} — {p2} — {pp} (noto'g'ri fe'l)."))
    L = D.setdefault("E3", [])
    pps = [x[2] for x in IRR]
    for v, p2, pp in IRR:
        if p2 == pp:
            continue
        wrong = [p2, v + "ed" if not v.endswith("e") else v + "d"] + [x for x in _bad_forms(pp, pps)]
        wrong = [w for i, w in enumerate(wrong) if w != pp and w not in wrong[:i]]
        L.append(C(2, f"Present Perfect: I have already ____ ({v}) it.", pp, wrong[:3], f"{v} — {p2} — {pp}: have + V3."))
    L = D.setdefault("E9", [])
    pl = [x[1] for x in PLUR]
    for sg, p2 in PLUR:
        wrong = [sg + "s", sg + "es" if not sg.endswith("s") else sg + "ses"] + _bad_forms(p2, pl)
        wrong = [w for i, w in enumerate(wrong) if w != p2 and w not in wrong[:i]][:3]
        if len(wrong) == 3:
            L.append(C(1, f"“{sg}” so'zining ko'plik shakli qaysi?", p2, wrong, f"{sg} → {p2}."))
    L = D.setdefault("E7", [])
    for adj, comp, sup in COMP:
        others = [c[1] for c in COMP if c[1] != comp]
        wr = [adj + "er" if len(adj) < 7 else "more " + adj + "er", "more " + adj, others[0]]
        wr = [w for i, w in enumerate(wr) if w != comp and w not in wr[:i]]
        for extra in others:
            if len(wr) >= 3:
                break
            if extra not in wr:
                wr.append(extra)
        L.append(C(1, f"“{adj}” sifatining qiyosiy darajasi (comparative) qaysi?", comp, wr[:3], f"{adj} → {comp}."))
        others_s = [c[2] for c in COMP if c[2] != sup]
        ws = ["the " + adj + "est" if len(adj) < 7 else "the most " + adj + "est", "most " + adj, others_s[1]]
        ws = [w for i, w in enumerate(ws) if w != sup and w not in ws[:i]]
        for extra in others_s:
            if len(ws) >= 3:
                break
            if extra not in ws:
                ws.append(extra)
        L.append(C(2, f"“{adj}” sifatining orttirma darajasi (superlative) qaysi?", sup, ws[:3], f"{adj} → {sup}."))
    L = D.setdefault("E36", [])
    ords = [o[1] for o in ORD]
    for n, w in ORD:
        wr = _bad_forms(w, ords)
        L.append(C(1, f"{n}-chi (tartib son) inglizcha qanday yoziladi?", w, wr, f"{n} → {w}."))
    L = D.setdefault("E35", [])
    for pr, mine, my in POSS:
        if mine == my:
            continue
        obj = {"I": "me", "you": "you", "we": "us", "they": "them", "he": "him", "she": "her"}[pr]
        wr = [my, my + "s", pr, obj, obj + "self", "of " + obj]
        wr = [w for i, w in enumerate(wr) if w != mine and w not in wr[:i]]
        L.append(C(1, f"This book belongs to {obj}. It is ____.", mine, wr[:3], f"Mustaqil egalik olmoshi: {mine}."))
    for pr, ob in OBJ:
        L.append(C(1, f"Please call ____ tomorrow. ({pr})", ob, [pr, pr + "'s", ob + "self"], f"{pr} → {ob} (to'ldiruvchi kelishik)."))
    L = D.setdefault("E1", [])
    for v, s3 in [("go", "goes"), ("watch", "watches"), ("study", "studies"), ("play", "plays"), ("have", "has"), ("do", "does"), ("fly", "flies"), ("teach", "teaches"), ("miss", "misses"), ("carry", "carries"), ("enjoy", "enjoys"), ("wash", "washes")]:
        wr = [v, v + "s" if v + "s" != s3 else v + "es", v + "ies" if not v.endswith("y") else v + "es"]
        wr = [w for i, w in enumerate(wr) if w != s3 and w not in wr[:i]]
        for extra in (v + "ing", "is " + v, "does " + v):
            if len(wr) >= 3:
                break
            if extra != s3 and extra not in wr:
                wr.append(extra)
        L.append(C(1, f"He/She ____ (Present Simple, “{v}”).", s3, wr[:3], f"3-shaxs birlikda: {v} → {s3}."))
    return D


def _pairs(D, topics_by_code):
    for code, items in D.items():
        name = topics_by_code.get(code)
        if name and items:
            yield code, name, items


def extend(packs):
    """Mavjud paketlarga hisoblangan savollarni qo'shadi (takror matnlar o'tkazib yuboriladi)."""
    spec = {"math": math_items, "physics": phys_items, "chemistry": chem_items, "biology": bio_items, "english": eng_items}
    for pack in packs:
        fn = spec.get(pack["subject"])
        if not fn:
            continue
        by_code = {t["code"]: (t["name"], t["grade"], t.get("block", "")) for t in pack["topics"]}
        if not by_code:
            continue
        have = {q["question"].strip().lower() for q in pack["questions"]}
        for code, items in fn().items():
            if code not in by_code:
                continue
            name, grade, block = by_code[code]
            seen, uniq = set(), []
            for it in items:
                k = it["q"].strip().lower()
                if k in have or k in seen:
                    continue
                seen.add(k)
                uniq.append(it)
            if not uniq:
                continue
            # generator savollari mavjudlari bilan aralashmasligi uchun: ularning tarif darajasi mavjud banklar orqali emas, qiyinlikka qarab beriladi
            recs = expand(name, grade, uniq, block)
            for r in recs:
                r["min_plan"] = 0 if r["difficulty"] == 1 else (1 if r["difficulty"] == 2 else 2)
            pack["questions"].extend(recs)
            have.update(seen)
    return packs
