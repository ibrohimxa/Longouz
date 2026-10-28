"""Fizika: elektr, magnit, tebranishlar va to'lqinlar (8-, 9-, 10-, 11-sinf)."""
import math
from ._dsl import C, O, M
from ._ph import N, ON, fmt
from . import figs_phys as F

k = 9e9
Q = {}

Q["P11.1"] = [
    C(1, "Elementar zaryad qiymati?", "1,6·10⁻¹⁹ C", ["9·10⁹ C", "6,02·10²³ C", "1,6·10⁻³¹ C"], "e = 1,6·10⁻¹⁹ C."),
    C(1, "Bir xil ishorali zaryadlar...", "itarishadi", ["tortishadi", "ta'sirlashmaydi", "yo'qoladi"], "Kulon."),
    C(1, "Kulon qonuni formulasi?", "F = k·q₁q₂/r²", ["F = k·q₁q₂·r", "F = k·q/r", "F = q₁q₂/r"], "Masofa kvadratiga teskari."),
    N(2, "q₁ = 2·10⁻⁶ C va q₂ = 3·10⁻⁶ C, r = 0,3 m (k = 9·10⁹). Kuch?", 0.6, [0.06, 6, 1.8], "N", "9e9·6e-12/0,09 = 0,6."),
    C(2, "Masofa 3 marta ortsa Kulon kuchi...", "9 marta kamayadi", ["3 marta kamayadi", "9 marta ortadi", "o'zgarmaydi"], "1/r²."),
    C(2, "Dielektrik muhitda (ε > 1) Kulon kuchi vakuumga nisbatan...", "ε marta kamayadi", ["ε marta ortadi", "o'zgarmaydi", "nolga teng"], "F = kq₁q₂/(εr²)."),
    N(3, "Jism 5·10¹² ortiqcha elektronga ega. Zaryadi (e = 1,6·10⁻¹⁹)?", -8e-7, [8e-7, -3.2e-7, -1.6e-6], "C", "q = −Ne."),
    N(3, "Ikki bir xil zaryadli shar orasidagi kuch 4 N edi; masofa 2 marta kamaytirilsa, kuch?", 16, [8, 2, 1], "N", "1/r² → ×4."),
    ON(3, "Ikki bir xil metall sharcha zaryadlari +6 nC va −2 nC. Ular tegizilib ajratildi. Har birining zaryadi necha nC?", 2, "(6−2)/2 = 2 nC."),
    M(2, [("Kulon", "zaryad birligi"), ("Elementar zaryad", "1,6·10⁻¹⁹ C"), ("k", "9·10⁹ N·m²/C²")], "Elektrostatika."),
]

Q["P11.2"] = [
    C(1, "Maydon kuchlanganligi ta'rifi?", "E = F / q", ["E = F·q", "E = q/F", "E = F/r"], "Birlik sinov zaryadiga ta'sir kuchi."),
    C(1, "Kuchlanganlikning SI birligi?", "N/C (V/m)", ["J/C", "C/m", "N·m"], "E."),
    C(1, "Musbat nuqtaviy zaryad maydon chiziqlari...", "zaryaddan chiqib ketadi", ["zaryadga kiradi", "yopiq aylana", "o'zgarmas"], "Radial tashqariga."),
    N(2, "q = 2·10⁻⁸ C zaryaddan 0,3 m masofada kuchlanganlik (k = 9·10⁹)?", 2000, [600, 20000, 6000], "N/C", "kq/r² = 9e9·2e-8/0,09."),
    N(2, "Maydon kuchlanganligi 500 N/C. 4·10⁻⁶ C zaryadga ta'sir kuchi?", 0.002, [0.02, 125000000, 2], "N", "F = qE."),
    N(3, "Ikki perpendikulyar maydon kuchlanganligi 30 N/C va 40 N/C. Natijaviy?", 50, [70, 10, 1200], "N/C", "√(900+1600)."),
    C(2, "Ikki teng, qarama-qarshi ishorali zaryad orasidagi o'rtada maydon...", "nolga teng emas, zaryadlarni tutashtiruvchi chiziq bo'ylab yo'nalgan", ["nolga teng", "tashqariga qarab", "aylana bo'ylab"], "Maydonlar qo'shiladi."),
    C(3, "Ikki bir xil musbat nuqtaviy zaryad orasidagi aynan o'rta nuqtada natijaviy kuchlanganlik...", "nolga teng", ["bitta zaryad maydonidan ikki baravar katta", "bitta zaryad maydoniga teng", "cheksiz katta"], "Ikkita teng, qarama-qarshi yo'nalgan maydon."),
    ON(3, "Elektron (m = 9,1·10⁻³¹ kg, e = 1,6·10⁻¹⁹ C) E = 910 N/C maydonda. Tezlanishi necha ·10¹⁴ m/s²? (a = eE/m)", 1.6, "a = 1,6·10⁻¹⁹·910/9,1·10⁻³¹ = 1,6·10¹⁴ m/s²."),
]

Q["P11.3"] = [
    C(1, "Potensiallar farqi (kuchlanish) ta'rifi?", "U = A / q", ["U = q / A", "U = A·q", "U = F·q"], "Maydonning zaryadni ko'chirishdagi ishi."),
    C(1, "Kuchlanishning SI birligi?", "volt", ["amper", "om", "farad"], "1 V = 1 J/C."),
    N(2, "2 C zaryadni ko'chirishda maydon 50 J ish bajardi. Kuchlanish?", 25, [100, 0.04, 52], "V", "A/q."),
    N(2, "Bir jinsli maydonda E = 200 V/m, plastinkalar orasi 3 sm. Kuchlanish?", 6, [600, 0.15, 66.7], "V", "U = Ed = 200·0,03."),
    N(3, "Elektron U = 100 V potensiallar farqida tezlashtirildi. Olingan energiya (e = 1,6·10⁻¹⁹)?", 1.6e-17, [1.6e-19, 1.6e-21, 100], "J", "eU."),
    N(3, "q = 4·10⁻⁹ C zaryad maydonda 500 V potensial farqini o'tdi. Ish?", 2e-6, [2e-7, 8e-12, 1.25e11], "J", "A = qU."),
    C(2, "Ekvipotensial sirt bo'ylab zaryadni ko'chirishda maydon ishi...", "nolga teng", ["maksimal", "manfiy", "musbat"], "Δφ = 0."),
    ON(3, "Tinch turgan proton U = 1000 V da tezlandi. Uning kinetik energiyasi necha eV?", 1000, "1 eV = e·1 V."),
    ON(3, "Plastinkalar orasidagi masofa 2 sm, E = 5000 V/m. Kuchlanish necha V?", 100, "U = Ed = 5000·0,02."),
]

_ccs = F.cap_circuit("series", ["C₁", "C₂"])
_ccp = F.cap_circuit("parallel", ["C₁", "C₂", "C₃"])
Q["P11.4"] = [
    C(1, "Kondensator sig'imi formulasi?", "C = q / U", ["C = q·U", "C = U/q", "C = q/U²"], "Zaryad kuchlanishga nisbati."),
    C(1, "Yassi kondensator sig'imi plastinkalar yuzi ortganda...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "C = εε₀S/d."),
    N(2, "C₁ = 6 μF va C₂ = 3 μF ketma-ket ulangan. Umumiy sig'im?", 2, [9, 18, 4.5], "μF", "6·3/9.", fig=_ccs),
    N(2, "C₁ = 2, C₂ = 3, C₃ = 5 μF parallel. Umumiy sig'im?", 10, [30, 1, 0.97], "μF", "Yig'indi.", fig=_ccp),
    N(2, "Kondensator 10 μF, kuchlanish 100 V. Zaryadi?", 0.001, [0.1, 1000, 10], "C", "q = CU = 10⁻⁵·100."),
    N(3, "10 μF kondensator 200 V gacha zaryadlangan. Energiyasi?", 0.2, [2, 0.02, 1], "J", "CU²/2 = 10⁻⁵·40000/2."),
    N(3, "Manbaga ulangan kondensatorning plastinkalari orasi 2 marta kamaytirilsa, sig'im...", 2, [0.5, 1, 4], "marta oshadi", "C ∼ 1/d."),
    C(2, "Manbadan uzilgan zaryadlangan kondensatorning plastinkalari uzoqlashtirilsa, kuchlanish...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "q = const, C kamayadi → U = q/C ortadi."),
    ON(3, "Ketma-ket ulangan 4 μF va 12 μF kondensatorlarga 80 V qo'yildi. Birinchi kondensator kuchlanishi necha V?", 60, "C = 3 μF; q = 240 μC; U₁ = 240/4 = 60 V."),
    ON(3, "Parallel ulangan 2 μF va 8 μF kondensatorlarga 50 V berilgan. Jami zaryad necha mkC?", 500, "C = 10 μF; q = 500 μC."),
]

_cs = F.circuit_series(["R₁", "R₂", "R₃"])
_cp = F.circuit_parallel(["R₁", "R₂"])
_cm = F.circuit_mixed("R₁", "R₂", "R₃")
Q["P11.5"] = [
    C(1, "Om qonuni (zanjir qismi uchun)?", "I = U / R", ["I = U·R", "I = R/U", "I = U²/R"], "Tok kuchlanishga to'g'ri, qarshilikka teskari proporsional."),
    C(1, "Ketma-ket ulangan rezistorlarda barcha qismlarda bir xil bo'ladi:", "tok kuchi", ["kuchlanish", "quvvat", "qarshilik"], "I = const.", fig=_cs),
    C(1, "Parallel ulangan rezistorlarda bir xil bo'ladi:", "kuchlanish", ["tok kuchi", "quvvat", "qarshilik"], "U = const.", fig=_cp),
    N(2, "R₁ = 2 Ω, R₂ = 3 Ω, R₃ = 5 Ω ketma-ket. Umumiy qarshilik?", 10, [30, 1, 0.97], "Ω", "Yig'indi.", fig=_cs),
    N(2, "R₁ = 6 Ω va R₂ = 3 Ω parallel. Umumiy qarshilik?", 2, [9, 18, 4.5], "Ω", "6·3/9.", fig=_cp),
    N(3, "Chizma: R₁ = 4 Ω ketma-ket, R₂ = R₃ = 6 Ω parallel. R_umumiy?", 7, [16, 3.33, 10], "Ω", "4 + 3 = 7.", fig=_cm),
    N(3, "Shu zanjirga 14 V berilsa, umumiy tok?", 2, [3.5, 1, 7], "A", "I = 14/7.", fig=_cm),
    N(2, "Uzunligi 2 m, ko'ndalang kesimi 0,5 mm², ρ = 1,7·10⁻⁸ Ω·m mis sim qarshiligi?", 0.068, [0.0068, 0.68, 6.8], "Ω", "R = ρl/S = 1,7e-8·2/5e-7 = 0,068."),
    ON(3, "Qarshiligi 10 Ω bo'lgan sim 5 ta teng bo'lakka kesilib, parallel ulandi. Umumiy qarshilik necha Ω?", 0.4, "Har biri 2 Ω; parallel 2/5 = 0,4."),
    M(2, [("Ketma-ket", "R = R₁ + R₂"), ("Parallel", "1/R = 1/R₁ + 1/R₂"), ("Om qonuni", "I = U/R")], "Ulanishlar."),
]

Q["P11.6"] = [
    C(1, "To'liq zanjir uchun Om qonuni?", "I = ε / (R + r)", ["I = ε / R", "I = ε·(R + r)", "I = ε/r"], "ε — EYK, r — ichki qarshilik."),
    N(2, "ε = 12 V, r = 1 Ω, R = 5 Ω. Tok?", 2, [12, 2.4, 6], "A", "12/6."),
    N(2, "Shu zanjirda tashqi qarshilikdagi kuchlanish?", 10, [12, 2, 6], "V", "U = IR = 2·5."),
    N(3, "Manba qisqa tutashuv toki: ε = 9 V, r = 0,5 Ω?", 18, [4.5, 9, 0.056], "A", "ε/r."),
    N(3, "R = r bo'lganda foydali quvvat maksimal. ε = 20 V, r = 5 Ω bo'lsa, maksimal quvvat?", 20, [80, 40, 10], "W", "I = 2 A; P = I²R = 4·5."),
    N(3, "Tok manbasi EYK 6 V; tashqi zanjirda tok 1 A bo'lganda uchlaridagi kuchlanish 5,5 V. r?", 0.5, [5.5, 1, 6], "Ω", "r = (ε − U)/I."),
    C(2, "Ikki bir xil batareya ketma-ket ulansa (ε, r):", "EYK = 2ε, r = 2r", ["EYK = ε, r = r/2", "EYK = 2ε, r = r/2", "EYK = ε, r = 2r"], "Ketma-ket."),
    C(2, "Ikki bir xil batareya parallel ulansa:", "EYK = ε, r = r/2", ["EYK = 2ε, r = 2r", "EYK = 2ε, r = r/2", "EYK = ε, r = 2r"], "Parallel."),
    ON(3, "Manba ε = 10 V, r = 2 Ω. Tashqi qarshilik necha Ω bo'lganda tok 1 A bo'ladi?", 8, "R = ε/I − r = 8."),
]

_wh = F.wheatstone()
Q["P11.7"] = [
    C(1, "Kirxgofning birinchi qonuni?", "Tugunga kiruvchi toklar yig'indisi chiquvchilarga teng", ["Kuchlanishlar yig'indisi 0", "Toklar ko'paytmasi 1", "Qarshiliklar yig'indisi 0"], "Zaryadning saqlanishi."),
    C(1, "Kirxgofning ikkinchi qonuni?", "Yopiq konturda EYK lar algebraik yig'indisi kuchlanishlar pasayishlari yig'indisiga teng", ["Tokning yig'indisi nolga teng", "Barcha qarshiliklar teng", "Quvvat doim saqlanadi"], "Energiyaning saqlanishi."),
    N(2, "Tugunga 3 A va 2 A tok kiradi, bitta tok chiqadi. Chiquvchi tok?", 5, [1, 6, 1.5], "A", "Kirxgof-1."),
    C(2, "Uitston ko'prigi muvozanat sharti (R₁/R₃ = R₂/R₄ ko'rinishida) bajarilsa, R₅ dan o'tuvchi tok...", "nolga teng", ["maksimal", "teskari yo'nalgan", "R₅ ga bog'liq emas va nolga teng emas"], "A va B potensiallari teng.", fig=_wh),
    N(3, "Muvozanatli ko'prik: R₁ = R₂ = 6 Ω, R₃ = R₄ = 12 Ω, R₅ = 100 Ω. Umumiy qarshilik?", 9, [18, 4, 12], "Ω", "R₅ tok o'tkazmaydi: (6+6) ∥ (12+12) = 12·24/36 = 8? → 8 Ω."),
    N(3, "Tugunlarda tok: 2 A kiradi va 3 A kiradi, 4 A chiqadi. Qolgan tok?", 1, [5, 9, 0], "A (chiqadi)", "5 − 4 = 1."),
    ON(3, "Muvozanatli ko'prik: yuqori qo'llar 4 Ω va 4 Ω, pastki qo'llar 8 Ω va 8 Ω. Ko'prik qarshiligi (diagonal) tok o'tkazmasa, umumiy qarshilik necha Ω? (chap shox 4+8, o'ng shox 4+8)", 6, "Chap 12, o'ng 12 parallel = 6."),
    ON(3, "Uch tok bir tugunda: I₁ = 5 A (kiradi), I₂ = 2 A (chiqadi). I₃ necha A kirishi kerak (yoki chiqishi) — modul?", 3, "5 − 2 = 3 chiqadi."),
]
# yuqoridagi N(3, ... Ω) uchun javobni to'g'rilaymiz
Q["P11.7"][4] = N(3, "Muvozanatli ko'prik: R₁ = R₂ = 6 Ω, R₃ = R₄ = 12 Ω, R₅ = 100 Ω. A va B nuqtalar orasidagi umumiy qarshilik?", 8, [18, 4, 12], "Ω", "R₅ tok o'tkazmaydi: (6+6) ∥ (12+12) = 12·24/36 = 8 Ω.", fig=_wh)

Q["P11.8"] = [
    C(1, "Joul–Lens qonuni?", "Q = I²Rt", ["Q = IUt²", "Q = R/It", "Q = U/I"], "Ajralgan issiqlik."),
    C(1, "Quvvat formulasi?", "P = UI", ["P = U/I", "P = I/U", "P = U²I"], "P = I²R = U²/R."),
    N(2, "220 V, 5 A bo'lgan choynak quvvati?", 1100, [44, 225, 4400], "W", "UI."),
    N(2, "Qarshiligi 20 Ω rezistordan 3 A tok 10 s o'tdi. Issiqlik?", 1800, [600, 180, 60], "J", "I²Rt = 9·20·10."),
    N(3, "100 W lampa 10 soat ishladi. Energiya (kWh)?", 1, [10, 0.1, 100], "kWh", "0,1 kW·10 h."),
    N(3, "1 kWh narxi 1000 so'm. 2 kW isitkich 5 soat ishlasa to'lov?", 10000, [2000, 5000, 20000], "so'm", "10 kWh."),
    C(2, "Bir xil kuchlanishli manbaga ulangan ikki lampa: kichik qarshilikli lampa quvvati...", "katta", ["kichik", "bir xil", "nolga teng"], "P = U²/R."),
    ON(3, "220 V ga mo'ljallangan 55 Ω spiral. Quvvat necha W?", 880, "U²/R = 48400/55 = 880."),
    ON(3, "Elektr qozon FIK 80%, quvvati 2,1 kW. 1 kg suvni 20 °C dan 100 °C gacha qizdirish uchun necha sekund kerak? (c = 4200, 336 kJ foydali issiqlik)", 200, "A_t = 336000/0,8 = 420000; t = 420000/2100 = 200 s."),
]

Q["P11.9"] = [
    C(1, "Metallarda tok tashuvchilar?", "erkin elektronlar", ["musbat ionlar", "manfiy ionlar", "protonlar"], "Elektron gazi."),
    C(1, "Elektrolitlarda tok tashuvchilar?", "musbat va manfiy ionlar", ["faqat elektronlar", "faqat protonlar", "neytronlar"], "Ionlar."),
    C(1, "Faradeyning elektroliz qonuni?", "m = k·I·t", ["m = I/t", "m = kU", "m = I²t"], "Massa zaryadga proporsional."),
    N(2, "k = 3·10⁻⁷ kg/C, I = 2 A, t = 1000 s. Ajralgan massa?", 6e-4, [6e-7, 6e-2, 1.5e-3], "kg", "kIt."),
    C(2, "n-tipli yarimo'tkazgichda asosiy tashuvchilar:", "elektronlar", ["teshiklar", "ionlar", "protonlar"], "Donor aralashmasi."),
    C(2, "p–n o'tish tok o'tkazadi:", "faqat bir yo'nalishda (to'g'ri ulanganda)", ["ikkala yo'nalishda teng", "umuman o'tkazmaydi", "faqat qizdirilganda"], "Diod."),
    C(2, "Yarimo'tkazgichlarning qarshiligi temperatura ortganda...", "kamayadi", ["ortadi", "o'zgarmaydi", "nolga teng"], "Tashuvchilar ortadi."),
    ON(3, "Elektrolizda 5 A tok 20 minut o'tdi. Zaryad necha kulon?", 6000, "q = It = 5·1200."),
    ON(3, "Kumush uchun k = 1,12·10⁻⁶ kg/C. 10 A tok 100 s o'tganda necha gramm kumush ajraladi?", 1.12, "m = 1,12e-6·1000 = 1,12e-3 kg = 1,12 g."),
]

_mag = F.magnet_field("in", "+", "right")
Q["P11.10"] = [
    C(1, "Amper kuchi formulasi?", "F = I·B·l·sinα", ["F = qvB", "F = BS", "F = I²R"], "Tokli o'tkazgichga."),
    C(1, "Lorens kuchi formulasi?", "F = q·v·B·sinα", ["F = IBl", "F = qE", "F = BIS"], "Harakatlanuvchi zaryadga."),
    N(2, "B = 0,5 T, I = 4 A, l = 0,2 m, α = 90°. Amper kuchi?", 0.4, [4, 0.04, 2.5], "N", "IBl."),
    N(2, "q = 2·10⁻⁶ C, v = 10³ m/s, B = 0,1 T, v ⟂ B. Lorens kuchi?", 2e-4, [2e-5, 2e-3, 0.2], "N", "qvB."),
    C(2, "Lorens kuchi zarra tezligiga nisbatan...", "perpendikulyar, ish bajarmaydi", ["parallel", "teskari", "ish bajaradi"], "Energiya o'zgarmaydi.", fig=_mag),
    N(3, "Proton (m = 1,67·10⁻²⁷, q = 1,6·10⁻¹⁹) B = 0,1 T da v = 10⁶ m/s. Aylana radiusi?", 0.104, [0.0104, 1.04, 0.208], "m", "R = mv/(qB) = 1,67e-27·1e6/(1,6e-20) = 0,104 m."),
    C(3, "Zaryadlangan zarra bir jinsli magnit maydonda aylana bo'ylab harakatlanmoqda. Tezligi 2 marta oshsa, aylanish davri...", "o'zgarmaydi", ["2 marta ortadi", "2 marta kamayadi", "4 marta ortadi"], "T = 2πm/(qB) tezlikka bog'liq emas."),
    C(2, "Chizmada musbat zaryad B (varoqqa, ⊗) maydonida o'ngga harakatlanmoqda. Chap qo'l qoidasiga ko'ra kuch yo'nalishi?", "Pastga", ["Yuqoriga", "O'ngga", "Chapga"], "F = qv × B: v = +x, B = −z → F = −y... (rasmda pastga).", fig=_mag) if False else C(2, "Chizmada musbat zaryad varoqqa yo'nalgan maydonda o'ngga harakatlanmoqda. Lorens kuchi qaysi tomonga?", "Yuqoriga (sahifada)", ["Pastga", "O'ngga", "Chapga"], "v = +x, B = −z: v×B = (1,0,0)×(0,0,−1) = (0·(−1)−0·0, 0·0−1·(−1), 0) = (0,1,0) → +y (rasmda yuqoriga).", fig=_mag),
    ON(3, "Elektron B = 2·10⁻³ T da tezlik 3,2·10⁷ m/s bilan aylanadi (m = 9,1·10⁻³¹, e = 1,6·10⁻¹⁹). Radius necha mm? (R = mv/(eB))", 91, "R = 9,1e-31·3,2e7/(1,6e-19·2e-3) = 0,091 m = 91 mm."),
    ON(3, "Tokli o'tkazgich (l = 0,5 m) B = 0,2 T maydonda, B bilan 30° burchak. I = 10 A. Amper kuchi necha N?", 0.5, "F = 10·0,2·0,5·0,5."),
]

Q["P11.11"] = [
    C(1, "Magnit oqimi formulasi?", "Φ = B·S·cosα", ["Φ = B/S", "Φ = B·l·v", "Φ = L·I"], "Weber."),
    C(1, "Faradey induksiya qonuni?", "ε = −ΔΦ/Δt", ["ε = BIl", "ε = −L·I", "ε = Φ·t"], "Oqim o'zgarish tezligi."),
    N(2, "B = 0,2 T, S = 0,05 m², B ⟂ yuza. Oqim?", 0.01, [0.25, 0.1, 0.001], "Wb", "BS."),
    N(2, "Oqim 0,3 Wb dan 0,1 Wb gacha 0,1 s da kamaydi. Induksiya EYK moduli?", 2, [0.02, 20, 0.2], "V", "0,2/0,1."),
    N(3, "Uzunligi 0,5 m sim B = 0,4 T maydonda 10 m/s tezlik bilan (perpendikulyar) harakatlanadi. EYK?", 2, [20, 0.2, 5], "V", "Blv."),
    C(2, "Lens qoidasi: induksion tok...", "uni keltirib chiqargan sababga qarshilik qiladi", ["sababga yordam beradi", "doim soat strelkasi bo'yicha", "magnit oqimiga bog'liq emas"], "Energiya saqlanishi."),
    N(3, "100 o'ramli g'altakda oqim 0,02 s da 0,01 Wb ga o'zgardi. EYK?", 50, [0.5, 5, 500], "V", "N·ΔΦ/Δt = 100·0,5."),
    ON(3, "Kontur yuzi 0,1 m², B = 0,5 T, B va normal orasidagi burchak 60°. Oqim necha mWb?", 25, "0,5·0,1·0,5 = 0,025 Wb = 25 mWb."),
    ON(3, "Sim 0,4 m uzunlikda, B = 0,5 T, tezlik 5 m/s, v va B orasida 30°. EYK necha V?", 0.5, "Blv sinα = 0,5·0,4·5·0,5."),
]

Q["P11.12"] = [
    C(1, "Induktivlikning SI birligi?", "genri (H)", ["farad", "veber", "tesla"], "L."),
    C(1, "O'zinduksiya EYK formulasi?", "ε = −L·ΔI/Δt", ["ε = −LI", "ε = BIl", "ε = RI"], "Tok o'zgarishiga qarshi."),
    N(2, "L = 0,5 H, I = 4 A. G'altak magnit energiyasi?", 4, [8, 2, 1], "J", "LI²/2."),
    N(2, "L = 2 H g'altakda tok 0,1 s da 5 A dan 1 A gacha kamaydi. O'zinduksiya EYK moduli?", 80, [8, 40, 20], "V", "2·4/0,1."),
    N(3, "Tok 3 A, oqim 0,6 Wb. Induktivlik?", 0.2, [1.8, 5, 0.02], "H", "L = Φ/I."),
    C(2, "G'altakka temir o'zak kiritilsa induktivlik...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "μ > 1."),
    ON(3, "G'altak induktivligi 0,2 H, undagi tok 2 A dan 6 A gacha ortsa, magnit energiya necha J ga ortadi?", 3.2, "0,1(36−4) = 3,2."),
    ON(3, "L = 0,1 H, tok 0,05 s da 0 dan 10 A gacha tekis ortdi. O'zinduksiya EYK moduli necha V?", 20, "0,1·10/0,05."),
]

_sn = F.sine(100, 20, amp_lbl="100", T_lbl="20")
Q["P11.13"] = [
    C(1, "Tomson formulasi?", "T = 2π√(LC)", ["T = 2π√(L/C)", "T = 2πLC", "T = 1/√(LC)"], "LC kontur davri."),
    N(2, "L = 1 mH, C = 4 μF. Davr (π = 3,14)?", 3.97e-4, [1.26e-3, 6.28e-3, 4e-3], "s", "2π√(4e-9) = 6,28·6,32e-5 ≈ 3,97e-4."),
    C(1, "LC konturda tebranish vaqtida energiya...", "elektr va magnit shakllar orasida almashadi", ["yo'qoladi", "faqat issiqlikka aylanadi", "o'zgarmaydi shakli"], "Ideal kontur."),
    C(2, "Kondensator sig'imi 4 marta oshsa davr...", "2 marta oshadi", ["4 marta oshadi", "2 marta kamayadi", "o'zgarmaydi"], "T ∼ √C."),
    N(3, "ω₀ = 1/√(LC): L = 4 H, C = 1 F. ω₀?", 0.5, [2, 4, 0.25], "rad/s", "1/√4."),
    N(3, "Kontur chastotasi 1 kHz edi. L 4 marta orttirilsa, chastota?", 500, [250, 2000, 4000], "Hz", "ν ∼ 1/√L."),
    C(2, "Zaryad q(t) = q₀cos(ωt) bo'lsa, tok i(t) q(t) ga nisbatan fazada...", "π/2 ga ilgarilaydi", ["bir xil fazada", "π ga kechikadi", "π/2 ga kechikadi"], "i = q'."),
    ON(3, "Tebranish konturida L = 1 H, C = 4 μF. Siklik chastota ω₀ necha rad/s? (ω₀ = 1/√(LC))", 500, "LC = 4·10⁻⁶ → ω = 1/(2·10⁻³) = 500."),
    ON(3, "Konturda max zaryad 4 μC, C = 2 μF. Maksimal kuchlanish necha V?", 2, "U = q/C = 2."),
]

Q["P11.14"] = [
    C(1, "Sanoat o'zgaruvchan tok chastotasi (O'zbekiston)?", "50 Hz", ["60 Hz", "100 Hz", "220 Hz"], "Standart."),
    C(1, "Ta'sir etuvchi (effektiv) kuchlanish formulasi?", "U = U₀/√2", ["U = U₀·√2", "U = U₀/2", "U = U₀"], "Amplitudaning 0,707 qismi."),
    N(2, "Amplituda 311 V, effektiv qiymat (√2 = 1,41)?", 220.6, [440, 311, 156], "V", "311/1,41 ≈ 220,6."),
    N(2, "Tok amplitudasi 10 A. Effektiv qiymat (√2 = 1,41)?", 7.09, [14.1, 5, 10], "A", "10/1,41."),
    C(2, "Faqat aktiv qarshilikli zanjirda tok va kuchlanish orasida fazalar farqi?", "0", ["π/2", "π", "π/4"], "Fazada.", fig=_sn),
    C(2, "Induktiv g'altakda tok kuchlanishga nisbatan...", "π/2 ga kechikadi", ["π/2 ga ilgarilaydi", "fazada", "π ga ilgarilaydi"], "u = Li'."),
    C(2, "Sig'imli zanjirda tok kuchlanishga nisbatan...", "π/2 ga ilgarilaydi", ["π/2 ga kechikadi", "fazada", "π/2 ga kechikadi va ilgarilaydi"], "i = Cu'."),
    N(3, "Chizmadagi sinusoida amplitudasi 100 V, davri 20 ms. Chastota?", 50, [20, 100, 0.02], "Hz", "ν = 1/T = 1/0,02.", fig=_sn),
    ON(3, "u = 100 sin(200πt) V. Chastota necha Hz?", 100, "ω = 200π = 2πν → ν = 100."),
    ON(3, "u = 141 sin(314t) V. Effektiv kuchlanish necha V? (141/√2 = 100)", 100, "U = U₀/√2."),
]

Q["P11.15"] = [
    C(1, "Induktiv qarshilik formulasi?", "X_L = ωL", ["X_L = 1/(ωL)", "X_L = L/ω", "X_L = ω/L"], "Chastotaga proporsional."),
    C(1, "Sig'im qarshiligi formulasi?", "X_C = 1/(ωC)", ["X_C = ωC", "X_C = C/ω", "X_C = ω/C"], "Chastotaga teskari."),
    C(2, "RLC zanjirda rezonans sharti?", "X_L = X_C", ["R = X_L", "R = X_C", "L = C"], "Z = R, cosφ = 1."),
    N(2, "R = 3 Ω, X_L = 8 Ω, X_C = 4 Ω. To'liq qarshilik?", 5, [7, 15, 1], "Ω", "√(9 + 16)."),
    N(3, "R = 30 Ω, X_L = 50 Ω, X_C = 10 Ω, U = 100 V. Zanjirdagi tok kuchi?", 2, [3.33, 1.5, 5], "A", "Z = √(900+1600) = 50; I = 100/50."),
    N(3, "Rezonans chastotasi: L = 0,1 H, C = 10 μF. ω₀ (rad/s)?", 1000, [100, 10000, 31.6], "rad/s", "1/√(10⁻⁶) = 1000."),
    N(2, "Transformator: N₁ = 500, N₂ = 100, U₁ = 220 V. U₂?", 44, [1100, 110, 4.4], "V", "U₂ = U₁N₂/N₁."),
    C(2, "Transformator doimiy tokda ishlaydimi?", "Yo'q, o'zgaruvchan tokda ishlaydi", ["Ha", "Faqat yuklamasiz", "Faqat yuqori kuchlanishda"], "Oqim o'zgarishi kerak."),
    ON(3, "Pasaytiruvchi transformator: U₁ = 1000 V, U₂ = 100 V. N₁ = 2000 bo'lsa, N₂ necha o'ram?", 200, "N₂ = N₁U₂/U₁."),
    ON(3, "RLC zanjirda U = 120 V, rezonansda R = 24 Ω. Tok necha A?", 5, "I = U/R."),
]

Q["P11.16"] = [
    C(1, "Mayatnik davri formulasi?", "T = 2π√(l/g)", ["T = 2π√(g/l)", "T = 2π√(m/k)", "T = 2πlg"], "Matematik mayatnik."),
    C(1, "Prujinali mayatnik davri?", "T = 2π√(m/k)", ["T = 2π√(k/m)", "T = 2π√(l/g)", "T = 2π mk"], "Massa/qattiqlik."),
    N(2, "Mayatnik uzunligi 1 m (g = π² m/s²) — davr?", 2, [1, 4, 6.28], "s", "T = 2π√(1/π²) = 2."),
    N(2, "Prujina k = 100 N/m, m = 1 kg. Davr (π = 3,14)?", 0.628, [6.28, 0.0628, 1.57], "s", "2π√(0,01) = 0,628."),
    C(2, "Mayatnik uzunligi 4 marta oshsa davr...", "2 marta oshadi", ["4 marta oshadi", "o'zgarmaydi", "2 marta kamayadi"], "T ∼ √l."),
    N(3, "Tebranish tenglamasi x = 0,1 cos(10πt). Chastota?", 5, [10, 20, 0.2], "Hz", "ω = 10π → ν = 5."),
    C(2, "Chizmadagi grafikdan amplituda va davr topiladi: u(t) sinusoidasida davr necha?", "20 ms", ["100 ms", "10 ms", "40 ms"], "Chizmaga qarang.", fig=_sn),
    N(3, "To'lqin tezligi 340 m/s, chastota 170 Hz. To'lqin uzunligi?", 2, [0.5, 57800, 20], "m", "λ = v/ν."),
    ON(3, "Uzunligi 2,5 m matematik mayatnik (g = 10, π² ≈ 10) davri necha s?", 3.14, "T = 2π√(0,25) = π ≈ 3,14.") if False else ON(3, "Matematik mayatnik 10 s da 5 ta tebranish qildi. Davri necha s?", 2, "T = 10/5."),
    ON(3, "To'lqin chastotasi 4 Hz, uzunligi 3 m. Tezligi necha m/s?", 12, "v = λν."),
]

Q["P11.17"] = [
    C(1, "Tovush qaysi muhitda tarqalmaydi?", "Vakuumda", ["Havoda", "Suvda", "Po'latda"], "Mexanik to'lqin muhit talab qiladi."),
    C(1, "Havoda tovush tezligi taxminan?", "340 m/s", ["3·10⁸ m/s", "34 m/s", "1500 m/s"], "20 °C da."),
    C(1, "Tovush balandligi nimaga bog'liq?", "chastotaga", ["amplitudaga", "tezlikka", "muhit zichligiga"], "Chastota ortsa, balandroq."),
    C(1, "Tovush kuchi (balandligi emas) nimaga bog'liq?", "amplitudaga", ["chastotaga", "davrga", "to'lqin uzunligiga"], "Amplituda katta — kuchli."),
    N(2, "Chaqmoq chaqnashidan 3 s keyin momaqaldiroq eshitildi (v = 340 m/s). Masofa?", 1020, [113, 340, 3000], "m", "s = vt."),
    N(2, "Aks sado 2 s da qaytdi (v = 340). Devorgacha masofa?", 340, [680, 170, 1360], "m", "s = vt/2."),
    C(2, "Infratovush chastotasi...", "20 Hz dan kichik", ["20 kHz dan katta", "20–20000 Hz", "1 MHz"], "Eshitilmaydi."),
    ON(3, "Tovush suvda 1500 m/s tezlikda, chastota 500 Hz. To'lqin uzunligi necha m?", 3, "λ = v/ν."),
    ON(3, "Eshitish chegarasi 20 Hz–20 kHz. 20 kHz tovushning havodagi to'lqin uzunligi necha mm? (v = 340)", 17, "λ = 340/20000 = 0,017 m."),
]

Q["P11.18"] = [
    C(1, "Elektromagnit to'lqinlarning vakuumdagi tezligi?", "3·10⁸ m/s", ["340 m/s", "3·10⁶ m/s", "3·10⁵ m/s"], "c."),
    C(1, "Elektromagnit to'lqinlar ko'ndalang yoki bo'ylama?", "ko'ndalang", ["bo'ylama", "ikkalasi", "aylana"], "E ⟂ B ⟂ v."),
    C(2, "To'lqin uzunligi ortish tartibida: rentgen, ko'zga ko'rinadigan, radio. To'g'ri qator?", "rentgen < ko'rinadigan < radio", ["radio < ko'rinadigan < rentgen", "ko'rinadigan < radio < rentgen", "rentgen < radio < ko'rinadigan"], "Shkala."),
    N(2, "Chastota 100 MHz bo'lgan radio to'lqin uzunligi (c = 3·10⁸)?", 3, [0.33, 30, 300], "m", "λ = c/ν."),
    N(2, "To'lqin uzunligi 600 nm yorug'lik chastotasi?", 5e14, [5e12, 2e-15, 1.8e17], "Hz", "3e8/6e-7."),
    C(2, "Maksvell farazi: o'zgaruvchan magnit maydon...", "uyurmaviy elektr maydon hosil qiladi", ["zaryadsiz maydon hosil qilmaydi", "faqat tinch zaryad", "gravitatsiya hosil qiladi"], "Va aksincha."),
    N(3, "Radiolokator signali jismdan qaytib 2·10⁻⁴ s da qaytdi. Masofa (c = 3·10⁸)?", 30000, [60000, 3000, 6000], "m", "s = ct/2."),
    ON(3, "Quyoshdan Yergacha 1,5·10¹¹ m. Yorug'lik necha sekundda yetib keladi?", 500, "t = s/c."),
    ON(3, "Mobil aloqa to'lqin uzunligi 0,3 m. Chastota necha MHz? (c = 3·10⁸)", 1000, "ν = 1·10⁹ Hz."),
]
