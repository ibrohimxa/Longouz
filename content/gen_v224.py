"""v224: chizmali (SVG) savollar — fizika, matematika, kimyo, biologiya.

Har bir savol parametrlardan tuziladi va to'g'ri javob KOD orqali hisoblanadi (qo'lda yozilmaydi), chizma ham
xuddi shu parametrlardan chiziladi — shuning uchun matn, chizma va javob doim bir-biriga mos keladi.
Xato variantlar odatiy xatolardan (formula aralashtirish, yarim/ikki baravar, teskari nisbat) olinadi.
"""
import math

from ._dsl import C, expand
from ._ph import fmt
from . import figs_math as G
from . import figs_phys as P
from . import figs_sci as S

G_ACC = 10


def _sp(unit):
    return "" if not unit else (unit if unit == "°" else " " + unit)


def _uniq(correct, wrong, unit=""):
    out, seen = [], {correct}
    for w in wrong:
        s = (fmt(w) if isinstance(w, (int, float)) else str(w)) + _sp(unit)
        s = s.replace("y = 1x", "y = x").replace("y = -1x", "y = −x")
        if s not in seen and not s.startswith("-0 "):
            seen.add(s)
            out.append(s)
    return out[:3]


def NC(d, q, x, wrong, unit, expl, fig):
    corr = fmt(x) + _sp(unit)
    w = _uniq(corr, wrong, unit)
    k = 2
    while len(w) < 3:
        w = _uniq(corr, list(wrong) + [x * k, x + k, x * (k + 1)], unit)
        k += 1
    return C(d, q, corr, w, expl, fig=fig)


# ------------------------------------------------------------------ FIZIKA
def phys():
    out = {}
    # Richag muvozanati: F1*l1 = F2*l2
    L = []
    for l1, l2, F1 in [(2, 1, 30), (3, 1, 20), (4, 2, 25), (1, 3, 60), (2, 3, 45), (3, 2, 40), (5, 1, 12), (1, 4, 80), (3, 4, 60), (4, 3, 30)]:
        F2 = F1 * l1 / l2
        fig = P.lever(l1, l2, f"F₁={F1} N", "F₂ = ?")
        L.append(NC(2, f"Chizmadagi richag muvozanatda. Yelkalar {l1} m va {l2} m, F₁ = {F1} N. F₂ ni toping.", F2,
                    [F1 * l2 / l1, F1, F1 * (l1 + l2) / l2], "N", f"F₁·l₁ = F₂·l₂ ⇒ F₂ = {F1}·{l1}/{l2} = {fmt(F2)} N.", fig))
    out["P7.7"] = L
    # Gidravlik press: F2 = F1*S2/S1
    L = []
    for S1, S2, F1 in [(2, 20, 50), (5, 100, 40), (4, 40, 30), (10, 200, 25), (3, 60, 15), (8, 64, 20), (5, 50, 120), (2, 30, 10)]:
        F2 = F1 * S2 / S1
        fig = P.hydraulic(f"{S1} sm²", f"{S2} sm²", f"F₁={F1} N", "F₂ = ?")
        L.append(NC(2, f"Gidravlik press (chizma): kichik porshen yuzi {S1} sm², kattasi {S2} sm², kichik porshenga {F1} N kuch qo'yildi. Katta porshendagi kuch?",
                    F2, [F1 * S1 / S2, F1 * (S2 - S1) / S1, F2 / 2], "N", f"F₂/F₁ = S₂/S₁ ⇒ F₂ = {F1}·{S2}/{S1} = {fmt(F2)} N.", fig))
    out["P7.5"] = L
    # Qiya tekislik (ishqalanishsiz va ishqalanish bilan)
    L = []
    for ang, mu in [(30, 0), (30, 0.2), (45, 0), (60, 0), (30, 0.1), (45, 0.5), (60, 0.3), (30, 0.3)]:
        s, c = math.sin(math.radians(ang)), math.cos(math.radians(ang))
        a = G_ACC * (s - mu * c)
        if a <= 0:
            continue
        a = round(a, 2)
        fig = P.incline(ang, mu=bool(mu), labelA=f"{ang}°")
        mtxt = f"ishqalanish koeffitsienti μ = {fmt(mu)}" if mu else "ishqalanish yo'q"
        L.append(NC(3 if mu else 2, f"Jism chizmadagi {ang}° li qiya tekislikdan sirpanib tushmoqda ({mtxt}, g = 10 m/s²). Tezlanishni toping (0,01 gacha yaxlitlang).",
                    a, [round(G_ACC * s, 2) if mu else round(G_ACC * c, 2), round(G_ACC * (s + mu * c), 2) if mu else G_ACC, round(G_ACC * c - mu * G_ACC * s, 2) if mu else round(G_ACC * s / 2, 2)],
                    "m/s²", f"a = g(sinα − μcosα) = 10·({fmt(round(s, 3))} − {fmt(mu)}·{fmt(round(c, 3))}) ≈ {fmt(a)} m/s².", fig))
    out["P9.7"] = L
    # Ketma-ket / parallel rezistorlar
    L = []
    for rs in [(2, 3), (4, 6), (5, 10, 5), (1, 2, 3), (6, 3), (10, 15), (8, 2, 10)]:
        tot = sum(rs)
        fig = P.circuit_series([f"{r} Ω" for r in rs])
        par = 1 / sum(1 / r for r in rs)
        L.append(NC(1, f"Chizmadagi rezistorlar ketma-ket ulangan ({', '.join(str(r) + ' Ω' for r in rs)}). Umumiy qarshilik?", tot,
                    [round(par, 2), tot / len(rs), max(rs)], "Ω", f"Ketma-ket: R = {' + '.join(map(str, rs))} = {tot} Ω.", fig))
        if len(rs) == 2:
            figp = P.circuit_parallel([f"{r} Ω" for r in rs])
            L.append(NC(2, f"Chizmadagi {rs[0]} Ω va {rs[1]} Ω rezistorlar parallel ulangan. Umumiy qarshilik?", round(par, 2),
                        [tot, round(par * 2, 2), abs(rs[0] - rs[1]) or tot / 4], "Ω", f"R = R₁R₂/(R₁+R₂) = {rs[0]}·{rs[1]}/{tot} = {fmt(round(par, 2))} Ω.", figp))
    for rs, U in [((2, 3), 10), ((4, 6), 20), ((5, 5, 10), 40), ((1, 2, 3), 12)]:
        tot = sum(rs)
        I = U / tot
        fig = P.circuit_series([f"{r} Ω" for r in rs], emf=f"{U} V")
        L.append(NC(2, f"Chizmadagi zanjirga {U} V kuchlanish berilgan (ichki qarshilik hisobga olinmaydi). Zanjirdagi tok kuchi?", round(I, 2),
                    [round(U * tot, 1), round(U / min(rs), 2), round(tot / U, 2)], "A", f"I = U/R = {U}/{tot} = {fmt(round(I, 2))} A.", fig))
    out["P11.5"] = L
    # v–t grafigi: tezlanish va yo'l
    L = []
    for v0, v1, t in [(0, 10, 5), (2, 12, 5), (4, 16, 4), (0, 20, 4), (10, 0, 5), (6, 18, 6), (5, 15, 2)]:
        a = (v1 - v0) / t
        sdist = (v0 + v1) / 2 * t
        vt = sorted(set([0, v0, v1, max(v0, v1) + 2]))
        fig = P.graph([(0, v0), (t, v1)], list(range(1, t + 1)), [v for v in vt if v], xmax=t + 1, ymax=max(v0, v1) + 4,
                      dots=[(0, v0, ""), (t, v1, "")])
        L.append(NC(2, f"Chizmada jism tezligining vaqtga bog'liqlik grafigi berilgan (0 s da {v0} m/s, {t} s da {v1} m/s). Tezlanishni toping.", a,
                    [v1 / t, (v1 + v0) / t, -a if a else 1], "m/s²", f"a = (v − v₀)/t = ({v1} − {v0})/{t} = {fmt(a)} m/s².", fig))
        L.append(NC(3, f"Shu grafik bo'yicha (0 s da {v0} m/s, {t} s da {v1} m/s) jism {t} s da qancha yo'l bosgan?", sdist,
                    [v1 * t, (v1 - v0) * t / 2 if v1 != v0 else v1, v0 * t + v1], "m", f"Yo'l = grafik ostidagi yuza = (v₀ + v)/2 · t = {fmt(sdist)} m.", fig))
    out["P9.2"] = L
    return out


# ------------------------------------------------------------------ MATEMATIKA
def math_q():
    out = {"MF.1": [], "MF.3": [], "MF.4": [], "MF.6": [], "MF.9": [], "MF.2": []}
    for a, b, c in [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25), (12, 16, 20), (20, 21, 29)]:
        fig = G.right_triangle(f"{a}", f"{b}", "?")
        out["MF.1"].append(NC(1, f"Chizmadagi to'g'ri burchakli uchburchakning katetlari {a} va {b}. Gipotenuzani toping.", c,
                              [a + b, c + 1, c - 1], "", f"c = √({a}² + {b}²) = √{a*a + b*b} = {c}.", fig))
        fig2 = G.right_triangle(f"{a}", "?", f"{c}")
        out["MF.1"].append(NC(2, f"Chizmada gipotenuza {c}, bir kateti {a}. Ikkinchi katetni toping.", b,
                              [c - a, c + a if c + a != b else b + 2, b + 1], "", f"b = √({c}² − {a}²) = √{c*c - a*a} = {b}.", fig2))
        out["MF.1"].append(NC(2, f"Katetlari {a} va {b} bo'lgan to'g'ri burchakli uchburchak (chizma) yuzini toping.", a * b / 2,
                              [a * b, a + b + c, a * c / 2], "", f"S = ab/2 = {a}·{b}/2 = {fmt(a*b/2)}.", fig))
    for w, h in [(6, 4), (8, 5), (12, 5), (9, 7), (10, 3)]:
        out["MF.3"].append(NC(1, f"Chizmadagi to'g'ri to'rtburchakning tomonlari {w} va {h}. Yuzini toping.", w * h,
                              [2 * (w + h), w + h, w * h / 2], "", f"S = a·b = {w}·{h} = {w*h}.", G.rect_diagonals(str(w), str(h))))
        out["MF.3"].append(NC(1, f"Tomonlari {w} va {h} bo'lgan to'g'ri to'rtburchak (chizma) perimetrini toping.", 2 * (w + h),
                              [w * h, w + h, 4 * w], "", f"P = 2(a + b) = 2·({w} + {h}) = {2*(w+h)}.", G.rect_diagonals(str(w), str(h))))
    for b1, b2, h in [(10, 6, 4), (12, 8, 5), (9, 5, 6), (14, 6, 3), (11, 7, 8)]:
        out["MF.3"].append(NC(2, f"Chizmadagi trapetsiya asoslari {b1} va {b2}, balandligi {h}. Yuzini toping.", (b1 + b2) * h / 2,
                              [(b1 + b2) * h, b1 * b2 * h / 2, (b1 + b2) / 2 + h], "", f"S = (a + b)/2 · h = ({b1} + {b2})/2 · {h} = {fmt((b1+b2)*h/2)}.",
                              G.trapezoid(str(b1), str(b2), f"h={h}")))
    for base, side, hh in [(8, 5, 4), (10, 6, 5), (7, 4, 3), (12, 9, 6)]:
        out["MF.3"].append(NC(2, f"Chizmadagi parallelogrammning asosi {base}, unga tushirilgan balandlik {hh} (yon tomoni {side}). Yuzini toping.", base * hh,
                              [base * side, base * hh / 2, 2 * (base + side)], "", f"S = a·h = {base}·{hh} = {base*hh}.", G.parallelogram(str(base), str(side), f"h={hh}")))
    for m, b in [(2, 1), (-1, 3), (1, -2), (3, -1), (-2, 0), (0.5, 1)]:
        fig = G.graph_linear(m, b, dots=[(0, b, "")])
        out["MF.4"].append(C(2, "Chizmada qaysi funksiyaning grafigi tasvirlangan?", f"y = {fmt(m) if m not in (1, -1) else ('' if m == 1 else '−')}x {'+ ' + fmt(b) if b > 0 else ('− ' + fmt(-b) if b < 0 else '')}".replace("  ", " ").strip(),
                             _uniq("", [f"y = {fmt(-m)}x {'+ ' + fmt(b) if b > 0 else ('− ' + fmt(-b) if b < 0 else '')}".strip(),
                                        f"y = {fmt(m)}x {'+ ' + fmt(-b) if -b > 0 else ('− ' + fmt(b) if b > 0 else '+ 1')}".strip(),
                                        f"y = {fmt(b) if b else 1}x {'+ ' + fmt(m) if m > 0 else '− ' + fmt(-m)}".strip()]),
                             f"Grafik Oy o'qini y = {fmt(b)} da kesadi, burchak koeffitsienti k = {fmt(m)}.", fig=fig))
    for a, b, c in [(1, -2, -3), (1, 0, -4), (1, 2, -3), (-1, 0, 4), (1, -4, 3), (1, -6, 5)]:
        D = b * b - 4 * a * c
        x1, x2 = sorted([(-b - math.sqrt(D)) / (2 * a), (-b + math.sqrt(D)) / (2 * a)])
        xv, yv = -b / (2 * a), c - b * b / (4 * a)
        fig = G.graph_parabola(a, b, c, x1=-5, x2=6, ymin=-6, ymax=8, show=[(x1, 0, ""), (x2, 0, ""), (xv, yv, "")])
        out["MF.4"].append(C(2, f"Chizmada y = {'' if a == 1 else '−' if a == -1 else a}x² {('+ ' if b > 0 else '− ') + str(abs(b)) + 'x ' if b else ''}{'+ ' if c > 0 else '− '}{abs(c)} parabolasi tasvirlangan. Uning Ox o'qi bilan kesishish nuqtalari abssissalari?",
                             f"{fmt(x1)} va {fmt(x2)}", [f"{fmt(-x1)} va {fmt(-x2)}", f"{fmt(xv)} va {fmt(yv)}", f"0 va {fmt(c)}"],
                             f"ax² + bx + c = 0 ⇒ D = {D}, x = {fmt(x1)}; {fmt(x2)}.", fig=fig))
        out["MF.4"].append(NC(2, f"Chizmadagi y = {'' if a == 1 else '−' if a == -1 else a}x² {('+ ' if b > 0 else '− ') + str(abs(b)) + 'x ' if b else ''}{'+ ' if c > 0 else '− '}{abs(c)} parabola uchining ordinatasini toping.", yv,
                              [xv, c, -yv if yv else 2], "", f"y₀ = c − b²/(4a) = {fmt(yv)}.", fig))
    for labels, vals in [(["Du", "Se", "Ch", "Pa", "Ju"], [12, 18, 9, 15, 21]), (["A", "B", "C", "D"], [30, 45, 25, 40]),
                         (["2021", "2022", "2023", "2024"], [40, 55, 50, 75]), (["Mat", "Fiz", "Kim", "Bio", "Tar"], [24, 16, 12, 20, 8])]:
        fig = G.bar_chart(labels, vals)
        mean = sum(vals) / len(vals)
        out["MF.6"].append(NC(2, f"Diagrammada ({', '.join(f'{l}: {v}' for l, v in zip(labels, vals))}) qiymatlarning o'rta arifmetigini toping.", round(mean, 2),
                              [round(sum(vals) / (len(vals) - 1), 2), sorted(vals)[len(vals) // 2], max(vals) - min(vals)], "", f"O'rtacha = {sum(vals)}/{len(vals)} = {fmt(round(mean, 2))}.", fig))
        out["MF.6"].append(NC(1, "Diagrammadagi eng katta va eng kichik qiymatlar ayirmasini toping.", max(vals) - min(vals),
                              [max(vals), max(vals) + min(vals), round(mean, 1)], "", f"{max(vals)} − {min(vals)} = {max(vals) - min(vals)}.", fig))
    for (x1, y1), (x2, y2) in [((-2, -1), (1, 3)), ((0, 0), (3, 4)), ((-3, 2), (3, -6)), ((1, 1), (4, 5)), ((-4, -3), (2, 5)), ((-1, 4), (2, 0))]:
        d = math.hypot(x2 - x1, y2 - y1)
        fig = G.coord_points([(x1, y1, "A"), (x2, y2, "B")], xr=(-5, 5), yr=(-6, 6), segs=[((x1, y1), (x2, y2))])
        out["MF.9"].append(NC(2, f"Chizmadagi A({x1}; {y1}) va B({x2}; {y2}) nuqtalar orasidagi masofani toping.", round(d, 2),
                              [abs(x2 - x1) + abs(y2 - y1), round(d * d, 2), round(d / 2, 2)], "", f"AB = √(({x2}−{x1})² + ({y2}−{y1})²) = {fmt(round(d, 2))}.", fig))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out["MF.9"].append(C(2, f"Chizmadagi A({x1}; {y1}) va B({x2}; {y2}) kesma o'rtasining koordinatalari?", f"({fmt(mx)}; {fmt(my)})",
                             [f"({fmt(x2 - x1)}; {fmt(y2 - y1)})", f"({fmt(my)}; {fmt(mx)})", f"({fmt(x1 + x2)}; {fmt(y1 + y2)})"], "O'rta nuqta: ((x₁+x₂)/2; (y₁+y₂)/2).", fig=fig))
    for arc in (60, 80, 100, 120, 140):
        fig = G.inscribed_angle(True, arc)
        out["MF.2"].append(NC(2, f"Chizmada markaziy burchak AOB = {arc}°. Shu yoyga tiralgan ichki chizilgan ACB burchakni toping.", arc / 2,
                              [arc, 180 - arc, 2 * arc if 2 * arc < 360 else arc + 10], "°", f"Ichki chizilgan burchak markaziy burchakning yarmiga teng: {arc}°/2 = {fmt(arc/2)}°.", fig))
    return out


# ------------------------------------------------------------------ KIMYO
ELEM = [("H", 1), ("He", 2), ("Li", 3), ("Be", 4), ("B", 5), ("C", 6), ("N", 7), ("O", 8), ("F", 9), ("Ne", 10), ("Na", 11), ("Mg", 12),
        ("Al", 13), ("Si", 14), ("P", 15), ("S", 16), ("Cl", 17), ("Ar", 18)]


def _shells(z):
    out, caps = [], [2, 8, 8]
    for cap in caps:
        if z <= 0:
            break
        out.append(min(cap, z))
        z -= min(cap, z)
    return out


def chem():
    L = []
    syms = [e for e, _ in ELEM]
    for sym, z in ELEM[2:]:
        sh = _shells(z)
        fig = S.bohr_atom(sh, "?")
        wrong = [s for s in syms if s != sym]
        idx = syms.index(sym)
        near = [syms[i] for i in (idx - 1, idx + 1, idx + 8, idx - 8) if 0 <= i < len(syms) and syms[i] != sym]
        L.append(C(2, f"Chizmada atomning elektron qavatlari tasvirlangan ({' , '.join(map(str, sh))}). Bu qaysi element?", sym,
                   (near + wrong)[:3], f"Elektronlar soni {z} ⇒ tartib raqami {z}: {sym}.", fig=fig))
        L.append(C(1, f"Chizmadagi atomning tashqi qavatida nechta elektron bor (qavatlar: {' , '.join(map(str, sh))})?", str(sh[-1]),
                   [str(x) for x in sorted({z, len(sh), (sh[-1] % 8) + 1, sh[0]} - {sh[-1]})][:3], f"Tashqi qavat — oxirgi qavat: {sh[-1]} ta elektron.", fig=S.bohr_atom(sh, sym)))
    return {"K8.9": L}


# ------------------------------------------------------------------ BIOLOGIYA
_GDESC = {"AA": "dominant gomozigota", "Aa": "geterozigota", "aA": "geterozigota", "aa": "retsessiv gomozigota"}


def _gx(p1, p2):
    a, b = "".join(p1), "".join(p2)
    return f"{a} ({_GDESC[a]}) × {b} ({_GDESC[b]})"


def bio():
    L = []
    crosses = [
        (("A", "a"), ("a", "a"), "1 : 1", ["3 : 1", "1 : 2 : 1", "Hammasi bir xil"], "Aa × aa ⇒ Aa : aa = 1 : 1 (tahliliy chatishtirish)."),
        (("A", "A"), ("a", "a"), "Hammasi Aa (100%)", ["1 : 1", "3 : 1", "1 : 2 : 1"], "AA × aa ⇒ barcha nasl Aa (Mendelning 1-qonuni)."),
        (("A", "a"), ("A", "a"), "1 : 2 : 1", ["3 : 1", "1 : 1", "9 : 3 : 3 : 1"], "Aa × Aa ⇒ genotip bo'yicha AA : Aa : aa = 1 : 2 : 1."),
        (("A", "A"), ("A", "a"), "1 : 1 (AA : Aa)", ["3 : 1", "1 : 2 : 1", "Hammasi aa"], "AA × Aa ⇒ AA : Aa = 1 : 1."),
    ]
    for p1, p2, ans, wr, ex in crosses:
        fig = S.punnett(p1, p2)
        L.append(C(2, f"Chizmadagi Pennet katagi: {_gx(p1, p2)}. Shu chatishtirishda nasllarning genotip nisbati qanday?", ans, wr, ex, fig=fig))
    for p1, p2 in [(("A", "a"), ("a", "a")), (("A", "a"), ("A", "a")), (("A", "A"), ("a", "a"))]:
        cells = ["".join(sorted(b + a, key=lambda c: (c.lower(), c.islower()))) for b in p1 for a in p2]
        rec = cells.count("aa")
        frac = {0: "0%", 1: "25%", 2: "50%", 4: "100%"}[rec]
        L.append(C(2, f"Chizmadagi chatishtirishda {_gx(p1, p2)}, A — dominant: retsessiv belgili (aa) nasllar ulushi?", frac,
                   [x for x in ("0%", "25%", "50%", "75%", "100%") if x != frac][:3], f"Katakda aa — {rec} ta (4 tadan) ⇒ {frac}.", fig=S.punnett(p1, p2)))
    return {"B10.5": L}


def extend(packs):
    gens = {"physics": phys, "math": math_q, "chemistry": chem, "biology": bio}
    for pack in packs:
        g = gens.get(pack["subject"])
        if not g:
            continue
        by_code = {t["code"]: t for t in pack["topics"]}
        have = {q["question"].strip().lower() for q in pack["questions"]}
        try:
            items_by_code = g()
        except Exception:  # noqa: BLE001
            continue
        for code, items in items_by_code.items():
            t = by_code.get(code)
            if not t:
                continue
            uniq = []
            for it in items:
                k = it["q"].strip().lower()
                if k in have:
                    continue
                if it.get("kind") == "c" and (len(it["w"]) < 3 or len({it["a"], *it["w"]}) < len(it["w"]) + 1):
                    continue
                have.add(k)
                uniq.append(it)
            if uniq:
                pack["questions"].extend(expand(t["name"], t["grade"], uniq, t.get("block", "")))
    return packs
