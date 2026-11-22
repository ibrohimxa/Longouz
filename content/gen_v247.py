"""v247: barcha fanlar bo'yicha kam savolli mavzularga DTM 2026 / milliy sertifikat uslubidagi yangi savollar
va bazadagi xato / chala savollarning tuzatilishi.

Aniq fanlar (matematika, fizika, kimyo) savollari hisob-kitob bilan tekshirilgan; gumanitar fanlar
savollari maktab darsliklaridagi aniq faktlarga tayanadi. Shubhali faktlar qo'shilmagan.
"""
from __future__ import annotations

import re

from ._dsl import C, O

MATH: dict[str, list] = {
    "M8.3": [
        C(1, "3x/6 kasrni qisqartiring.", "x/2", ["3x", "x/3", "2x"], "Surat va maxrajni 3 ga bo'lamiz."),
        C(2, "(x² − 9)/(x² + 3x) ni soddalashtiring (x ≠ 0, x ≠ −3).", "(x − 3)/x", ["(x + 3)/x", "x − 3", "(x − 3)/(x + 3)"], "x² − 9 = (x − 3)(x + 3), x² + 3x = x(x + 3); (x + 3) qisqaradi."),
        C(2, "1/x − 1/(x + 1) ifodani soddalashtiring (x ≠ 0; −1).", "1/(x(x + 1))", ["1/(x + 1)", "−1/(x(x + 1))", "1/x²"], "(x + 1 − x)/(x(x + 1)) = 1/(x(x + 1))."),
        C(3, "(a² − 2ab + b²)/(a² − b²) ni soddalashtiring (a ≠ ±b).", "(a − b)/(a + b)", ["(a + b)/(a − b)", "a − b", "1/(a + b)"], "(a − b)²/((a − b)(a + b)) = (a − b)/(a + b)."),
        C(3, "x/(x − 2) + 2/(2 − x) ifodaning qiymati (x ≠ 2)?", "1", ["(x + 2)/(x − 2)", "0", "−1"], "2/(2 − x) = −2/(x − 2); (x − 2)/(x − 2) = 1."),
        O(2, "(4a² − 1)/(2a + 1) ifodaning a = 3 dagi qiymatini toping.", ["5"], "(2a − 1)(2a + 1)/(2a + 1) = 2a − 1 = 5."),
    ],
    "M8.4": [
        C(1, "120 ning 15% i qancha?", "18", ["12", "15", "20"], "120 · 0,15 = 18."),
        C(2, "Mahsulot narxi avval 20% ga qimmatlab, keyin 20% ga arzonlashdi. Dastlabki narxga nisbatan qanday o'zgardi?", "4% ga arzonlashdi", ["O'zgarmadi", "4% ga qimmatladi", "2% ga arzonlashdi"], "1,2 · 0,8 = 0,96 — narx 4% ga kamaydi."),
        C(2, "x : 6 = 10 : 15 proporsiyadan x ni toping.", "4", ["9", "5", "25"], "x = 6 · 10 / 15 = 4."),
        C(3, "Ikki son 5 : 7 nisbatda, ularning ayirmasi 18 ga teng. Kichik sonni toping.", "45", ["63", "36", "54"], "7k − 5k = 2k = 18 → k = 9; kichik son 5 · 9 = 45."),
        C(3, "Ish haqi avval 10% ga, keyin yana 10% ga oshdi. Jami necha foizga oshdi?", "21%", ["20%", "19%", "22%"], "1,1 · 1,1 = 1,21."),
        O(2, "Kitob 25% chegirma bilan 36 000 so'mga sotildi. Chegirmagacha narxi necha so'm edi?", ["48000", "48 000"], "0,75x = 36 000 → x = 48 000."),
    ],
    "M8.5": [
        C(1, "3x ≥ 12 tengsizlikning yechimi?", "x ≥ 4", ["x ≤ 4", "x > 4", "x ≥ 9"], "Ikkala tomonni 3 ga bo'lamiz."),
        C(2, "5 − 2x > 1 tengsizlikning yechimi?", "x < 2", ["x > 2", "x < −2", "x > −2"], "−2x > −4 → x < 2 (manfiy songa bo'lganda belgi almashadi)."),
        C(2, "|x − 1| > 3 tengsizlikning yechimi?", "x < −2 yoki x > 4", ["−2 < x < 4", "x > 4", "x < −4 yoki x > 2"], "x − 1 > 3 yoki x − 1 < −3."),
        C(3, "|x + 2| ≤ 3 tengsizlikning butun yechimlari soni?", "7", ["6", "5", "3"], "−5 ≤ x ≤ 1: −5, −4, …, 1 — 7 ta."),
        O(3, "(x − 1)/3 − (x + 1)/2 < 0 tengsizlikning eng kichik butun yechimini toping.", ["-4", "−4"], "2(x − 1) − 3(x + 1) < 0 → −x − 5 < 0 → x > −5; eng kichik butun yechim −4."),
    ],
    "M8.6": [
        C(1, "y = −3x + 6 funksiya grafigi Oy o'qini qaysi nuqtada kesadi?", "(0; 6)", ["(2; 0)", "(0; −3)", "(6; 0)"], "x = 0 da y = 6."),
        C(2, "y = 2x − 1 va y = −x + 5 grafiklari qaysi nuqtada kesishadi?", "(2; 3)", ["(3; 2)", "(1; 1)", "(2; 1)"], "2x − 1 = −x + 5 → x = 2, y = 3."),
        C(2, "y = x² − 4x + 1 parabola uchining koordinatalari?", "(2; −3)", ["(−2; 13)", "(2; 1)", "(4; 1)"], "x₀ = 4/2 = 2, y₀ = 4 − 8 + 1 = −3."),
        C(3, "y = kx + 3 to'g'ri chiziq A(2; 7) nuqtadan o'tadi. k ni toping.", "2", ["5", "3,5", "−2"], "7 = 2k + 3 → k = 2."),
        C(3, "y = −x² + 6x − 5 funksiyaning eng katta qiymati?", "4", ["5", "−5", "9"], "x₀ = 3: −9 + 18 − 5 = 4."),
    ],
    "M8.7": [
        C(1, "(a − b)² ni kengaytiring.", "a² − 2ab + b²", ["a² − b²", "a² + b²", "a² + 2ab − b²"], "Ayirmaning kvadrati formulasi."),
        C(2, "(x + 2)³ ni kengaytiring.", "x³ + 6x² + 12x + 8", ["x³ + 8", "x³ + 2x² + 4x + 8", "x³ + 6x² + 6x + 8"], "(a + b)³ = a³ + 3a²b + 3ab² + b³."),
        C(2, "101² − 99² ni hisoblang.", "400", ["200", "4", "2000"], "(101 − 99)(101 + 99) = 2 · 200 = 400."),
        C(3, "a + b = 5 va ab = 6 bo'lsa, a² + b² ni toping.", "13", ["25", "19", "31"], "(a + b)² − 2ab = 25 − 12 = 13."),
        O(3, "x + 1/x = 3 bo'lsa, x² + 1/x² ni toping.", ["7"], "(x + 1/x)² − 2 = 9 − 2 = 7."),
    ],
    "M8.13": [
        C(2, "30% li 200 g eritmaga 50 g tuz qo'shildi. Yangi eritmaning konsentratsiyasi?", "44%", ["40%", "35%", "50%"], "Tuz: 60 + 50 = 110 g, eritma: 250 g; 110/250 = 0,44."),
        C(2, "Qotishma 2 kg mis va 3 kg qalaydan iborat. Misning ulushi necha foiz?", "40%", ["60%", "66,7%", "20%"], "2/5 = 0,4."),
        C(3, "20% li va 50% li eritmalardan 300 g 30% li eritma tayyorlash kerak. 20% li eritmadan necha gramm olinadi?", "200 g", ["100 g", "150 g", "250 g"], "0,2x + 0,5(300 − x) = 90 → −0,3x = −60 → x = 200."),
        C(3, "Yangi mevada 80%, quritilganida 20% suv bor. 100 kg yangi mevadan necha kg quritilgan meva olinadi?", "25 kg", ["20 kg", "40 kg", "80 kg"], "Quruq modda 20 kg; quritilgan mevada u 80%: 20 / 0,8 = 25 kg."),
        O(2, "40% li 150 g eritmada necha gramm erigan modda bor?", ["60"], "150 · 0,4 = 60."),
    ],
    "M8.15": [
        C(1, "|−3| + |5| ni hisoblang.", "8", ["2", "−8", "−2"], "3 + 5 = 8."),
        C(2, "|x + 1| = 0 tenglamaning yechimi?", "x = −1", ["x = 1", "x = ±1", "Yechimi yo'q"], "Modul faqat ichidagi ifoda nol bo'lganda nolga teng."),
        C(2, "|x − 3| = −2 tenglama nechta ildizga ega?", "Ildizi yo'q", ["1 ta", "2 ta", "Cheksiz ko'p"], "Modul manfiy bo'la olmaydi."),
        C(3, "|x − 1| = 2x + 1 tenglamani yeching.", "x = 0", ["x = −2", "x = 0 va x = −2", "x = 2"], "x ≥ 1: x − 1 = 2x + 1 → x = −2 (mos emas); x < 1: 1 − x = 2x + 1 → x = 0 (mos)."),
        O(3, "|x| + |x − 4| = 4 tenglamaning nechta butun yechimi bor?", ["5"], "0 ≤ x ≤ 4 oraliqdagi barcha x yechim: 0, 1, 2, 3, 4."),
    ],
    "M8.16": [
        C(1, "6x + 9 ni ko'paytuvchilarga ajrating.", "3(2x + 3)", ["6(x + 9)", "3(2x + 9)", "9(x + 1)"], "Umumiy ko'paytuvchi 3."),
        C(2, "ax + ay + bx + by ni ko'paytuvchilarga ajrating.", "(a + b)(x + y)", ["(a + x)(b + y)", "ab(x + y)", "(a − b)(x − y)"], "Guruhlash: a(x + y) + b(x + y)."),
        C(2, "x² − 6x + 9 ni ko'paytuvchilarga ajrating.", "(x − 3)²", ["(x + 3)²", "(x − 3)(x + 3)", "(x − 9)(x + 1)"], "To'la kvadrat."),
        C(3, "2x² + 5x − 3 ni ko'paytuvchilarga ajrating.", "(2x − 1)(x + 3)", ["(2x + 1)(x − 3)", "(2x − 3)(x + 1)", "(x − 1)(2x + 3)"], "(2x − 1)(x + 3) = 2x² + 6x − x − 3."),
        C(3, "x⁴ − 16 ni ko'paytuvchilarga ajrating.", "(x − 2)(x + 2)(x² + 4)", ["(x² − 4)²", "(x − 2)²(x + 2)²", "(x − 4)(x + 4)"], "(x² − 4)(x² + 4) = (x − 2)(x + 2)(x² + 4)."),
    ],
    "M9.1": [
        C(1, "y = x² − 6x + 5 parabola uchining abssissasi?", "3", ["−3", "6", "5"], "x₀ = −b/(2a) = 6/2 = 3."),
        C(2, "x² − 4x + 3 = 0 tenglamaning diskriminanti?", "4", ["28", "−4", "16"], "D = 16 − 12 = 4."),
        C(2, "y = −2x² + 8x funksiyaning eng katta qiymati?", "8", ["4", "2", "16"], "x₀ = 2: −8 + 16 = 8."),
        C(3, "x² + 2x + a = 0 tenglama ikki xil haqiqiy ildizga ega bo'lishi uchun a qanday bo'lishi kerak?", "a < 1", ["a > 1", "a ≤ 1", "a < −1"], "D = 4 − 4a > 0 → a < 1."),
        C(3, "x² − (m + 1)x + 4 = 0 tenglama ikki karrali (bitta) ildizga ega. m ning musbat qiymatini toping.", "3", ["4", "5", "1"], "(m + 1)² = 16 → m + 1 = ±4 → m = 3 yoki m = −5."),
    ],
    "M9.2": [
        C(1, "x² ≤ 16 tengsizlikning yechimi?", "−4 ≤ x ≤ 4", ["x ≤ 4", "x ≥ 4", "x ≤ −4 yoki x ≥ 4"], "|x| ≤ 4."),
        C(2, "x² − 3x < 0 tengsizlikning yechimi?", "0 < x < 3", ["x < 0 yoki x > 3", "x < 3", "−3 < x < 0"], "x(x − 3) < 0."),
        C(2, "x² + 1 < 0 tengsizlikning yechimi?", "Yechimi yo'q", ["x < −1", "Barcha x", "−1 < x < 1"], "x² + 1 har doim musbat."),
        C(3, "{x² − 9 < 0; x − 1 ≥ 0} tizimning butun yechimlari soni?", "2", ["3", "5", "4"], "−3 < x < 3 va x ≥ 1: x = 1; 2."),
        O(3, "x² − 2x − 8 ≤ 0 tengsizlikning butun yechimlari yig'indisini toping.", ["7"], "−2 ≤ x ≤ 4: −2 − 1 + 0 + 1 + 2 + 3 + 4 = 7."),
    ],
    "M9.8": [
        C(2, "√(x − 2) = −3 tenglamaning yechimi?", "Yechimi yo'q", ["x = 11", "x = −7", "x = 7"], "Arifmetik kvadrat ildiz manfiy bo'la olmaydi."),
        C(2, "√(5 − x) = 2 tenglamaning ildizi?", "1", ["3", "−1", "9"], "5 − x = 4 → x = 1."),
        C(3, "√(x + 3) = x + 1 tenglamaning ildizi?", "1", ["−2", "1 va −2", "2"], "x + 3 = x² + 2x + 1 → x² + x − 2 = 0 → x = 1 yoki x = −2; x = −2 da o'ng tomon manfiy — chet ildiz."),
        O(3, "√(2x + 3) = x tenglamaning ildizini toping.", ["3"], "2x + 3 = x² → x = 3 yoki x = −1; x ≥ 0 bo'lishi kerak."),
    ],
    "M9.10": [
        C(1, "y = 1/(x − 5) funksiyaning aniqlanish sohasi?", "x ≠ 5", ["x > 5", "x ≠ −5", "Barcha x"], "Maxraj nolga teng bo'lmasligi kerak."),
        C(2, "Quyidagilardan qaysi biri toq funksiya?", "y = x³ − x", ["y = x² + 1", "y = |x|", "y = x + 1"], "f(−x) = −x³ + x = −f(x)."),
        C(2, "y = √(6 − 2x) funksiyaning aniqlanish sohasi?", "x ≤ 3", ["x ≥ 3", "x < 3", "x ≤ 6"], "6 − 2x ≥ 0."),
        C(3, "y = √(x + 2) + 1/(x − 1) funksiyaning aniqlanish sohasi?", "x ≥ −2, x ≠ 1", ["x > −2", "x ≥ −2", "x ≠ 1"], "Ikkala shart birgalikda bajarilishi kerak."),
        O(2, "f(x) = 2x² − 3 bo'lsa, f(−2) ni toping.", ["5"], "2 · 4 − 3 = 5."),
    ],
    "M9.11": [
        C(1, "3; 7; 11; … arifmetik progressiyaning ayirmasi?", "4", ["3", "7", "−4"], "7 − 3 = 4."),
        C(2, "2; 6; 18; … geometrik progressiyaning 5-hadi?", "162", ["54", "486", "96"], "2 · 3⁴ = 162."),
        C(2, "a₁ = 5, d = −2 bo'lgan arifmetik progressiyaning 10-hadi?", "−13", ["−15", "23", "−11"], "5 + 9 · (−2) = −13."),
        C(3, "8; 4; 2; … cheksiz kamayuvchi geometrik progressiyaning yig'indisi?", "16", ["14", "12", "Cheksiz"], "S = b₁/(1 − q) = 8/0,5 = 16."),
        O(3, "Arifmetik progressiyada a₃ = 7, a₇ = 19. a₁ ni toping.", ["1"], "4d = 12 → d = 3; a₁ = 7 − 2 · 3 = 1."),
    ],
    "M10.2": [
        C(1, "cos x = 0 tenglamaning umumiy yechimi?", "x = π/2 + πn", ["x = πn", "x = 2πn", "x = π/2 + 2πn"], "Kosinus π/2 + πn nuqtalarda nolga teng."),
        C(2, "sin 2x = 0 tenglamaning umumiy yechimi?", "x = πn/2", ["x = πn", "x = 2πn", "x = π/4 + πn"], "2x = πn."),
        C(2, "cos x = −1 tenglamaning umumiy yechimi?", "x = π + 2πn", ["x = πn", "x = −π/2 + 2πn", "x = 2πn"], "Kosinus faqat π + 2πn da −1 ga teng."),
        C(3, "2cos²x − cos x − 1 = 0 tenglamaning [0; 2π) oraliqdagi yechimlari soni?", "3", ["2", "4", "1"], "cos x = 1 → x = 0; cos x = −1/2 → x = 2π/3, 4π/3."),
        O(3, "tg x = √3 tenglamaning (0°; 90°) oraliqdagi yechimi necha gradus?", ["60", "60°"], "tg 60° = √3."),
    ],
    "M10.4": [
        C(1, "log₃ 81 ni hisoblang.", "4", ["3", "27", "9"], "3⁴ = 81."),
        C(2, "2^(x²) = 16 tenglamaning ildizlari?", "x = ±2", ["x = 4", "x = 2", "x = ±4"], "x² = 4."),
        C(2, "lg x + lg 4 = 2 bo'lsa, x ni toping.", "25", ["96", "50", "1/2"], "lg 4x = 2 → 4x = 100."),
        C(3, "9ˣ − 4 · 3ˣ + 3 = 0 tenglama ildizlari yig'indisi?", "1", ["4", "3", "0"], "t = 3ˣ: t² − 4t + 3 = 0 → t = 1; 3 → x = 0; 1."),
        O(3, "log₂(x − 1) + log₂(x + 1) = 3 tenglamani yeching.", ["3"], "x² − 1 = 8 → x = ±3; x > 1 sharti bo'yicha x = 3."),
    ],
    "M10.7": [
        C(1, "sin(π − α) nimaga teng?", "sin α", ["−sin α", "cos α", "−cos α"], "Keltirish formulasi: II chorakda sinus musbat."),
        C(2, "cos(π/2 + α) nimaga teng?", "−sin α", ["sin α", "cos α", "−cos α"], "π/2 dan keyin funksiya nomi almashadi; II chorakda kosinus manfiy."),
        C(2, "sin 15° · cos 15° ni hisoblang.", "1/4", ["1/2", "√3/4", "1/8"], "½ · sin 30° = 1/4."),
        C(3, "cos² 22,5° − sin² 22,5° ni hisoblang.", "√2/2", ["1/2", "√3/2", "1"], "cos 45° = √2/2."),
        O(3, "tg α = 2 bo'lsa, (sin α + cos α)/(sin α − cos α) ni toping.", ["3"], "Surat va maxrajni cos α ga bo'lamiz: (2 + 1)/(2 − 1) = 3."),
    ],
    "M10.10": [
        C(1, "Konus hajmi formulasi?", "V = ⅓πr²h", ["V = πr²h", "V = 4/3 πr³", "V = 2πrh"], "Konus hajmi silindr hajmining uchdan biriga teng."),
        C(2, "Silindrning r = 4, h = 3. Yon sirti?", "24π", ["48π", "12π", "32π"], "S = 2πrh = 24π."),
        C(2, "Shar radiusi 2 marta oshirilsa, hajmi necha marta oshadi?", "8 marta", ["2 marta", "4 marta", "6 marta"], "V ~ r³: 2³ = 8."),
        C(3, "Radiusi 5 bo'lgan shar markazidan 3 masofada tekislik bilan kesildi. Kesim yuzi?", "16π", ["25π", "9π", "4π"], "Kesim radiusi: r² = 25 − 9 = 16."),
        O(3, "Konusning yasovchisi 10, asos radiusi 6. Balandligini toping.", ["8"], "h = √(100 − 36) = 8."),
    ],
    "M11.4": [
        C(1, "lim(x→3) (2x + 1) ni hisoblang.", "7", ["6", "5", "∞"], "Uzluksiz funksiya — qiymatni qo'yamiz."),
        C(2, "lim(x→0) (sin 3x)/x ni hisoblang.", "3", ["1", "0", "1/3"], "sin 3x ~ 3x."),
        C(2, "lim(x→∞) (1 + 1/x)ˣ nimaga teng?", "e", ["1", "∞", "0"], "Ikkinchi ajoyib limit."),
        C(3, "lim(x→∞) (x² − 3x)/(2x² + 1) ni hisoblang.", "1/2", ["0", "∞", "−3"], "Eng katta darajalar koeffitsientlari nisbati: 1/2."),
        O(3, "lim(x→0) (tg 5x)/(sin x) ni toping.", ["5"], "tg 5x ~ 5x, sin x ~ x."),
    ],
    "M11.5": [
        C(1, "f′(x) < 0 bo'lgan oraliqda funksiya qanday?", "Kamayuvchi", ["O'suvchi", "O'zgarmas", "Davriy"], "Hosila manfiy — funksiya kamayadi."),
        C(2, "f(x) = x² − 6x + 1 funksiyaning minimum nuqtasi?", "x = 3", ["x = −3", "x = 6", "x = 1"], "f′(x) = 2x − 6 = 0."),
        C(2, "f(x) = x³ − 3x² funksiyaning burilish nuqtasi abssissasi?", "1", ["0", "2", "3"], "f″(x) = 6x − 6 = 0."),
        C(3, "f(x) = x³ − 12x funksiyaning [0; 3] kesmadagi eng kichik qiymati?", "−16", ["−9", "0", "−18"], "f′ = 3x² − 12 = 0 → x = 2; f(2) = −16, f(0) = 0, f(3) = −9."),
        O(3, "f(x) = x + 4/x (x > 0) funksiyaning eng kichik qiymatini toping.", ["4"], "f′ = 1 − 4/x² = 0 → x = 2; f(2) = 4."),
    ],
    "M11.6": [
        C(2, "6 kishi bir qatorga necha xil usulda o'tirishi mumkin?", "720", ["36", "120", "64"], "6! = 720."),
        C(2, "10 o'quvchidan 2 navbatchini necha usulda tanlash mumkin?", "45", ["90", "20", "100"], "C(10, 2) = 45."),
        C(3, "Tanga 3 marta tashlandi. Kamida bitta «gerb» tushish ehtimoli?", "7/8", ["1/2", "3/8", "1/8"], "1 − (1/2)³ = 7/8."),
        C(3, "«KITOB» so'zi harflaridan nechta turli 5 harfli harflar ketma-ketligini tuzish mumkin?", "120", ["60", "25", "24"], "Barcha harflar har xil: 5! = 120."),
        O(3, "Qutida 4 ta oq va 6 ta qora shar bor. Tavakkaliga olingan shar oq bo'lish ehtimolini o'nli kasrda yozing.", ["0,4", "0.4"], "4/10 = 0,4."),
    ],
    "M11.7": [
        C(2, "∫₀² (3x² + 1) dx ni hisoblang.", "10", ["8", "12", "14"], "[x³ + x]₀² = 8 + 2 = 10."),
        C(3, "y = x² va y = 4 chiziqlar bilan chegaralangan figuraning yuzi?", "32/3", ["16/3", "8", "16"], "∫₋₂² (4 − x²) dx = 16 − 16/3 = 32/3."),
        C(3, "sin x + cos x ifodaning eng katta qiymati?", "√2", ["2", "1", "√3"], "sin x + cos x = √2 · sin(x + π/4)."),
        C(3, "log₂ 3 · log₃ 4 ni hisoblang.", "2", ["log₂ 12", "1", "4"], "Asosni almashtirish: log₂ 4 = 2."),
        O(3, "Geometrik progressiyada b₂ = 6, b₄ = 54 (q > 0). b₁ ni toping.", ["2"], "q² = 9 → q = 3; b₁ = 6/3 = 2."),
    ],
    "M11.8": [
        C(1, "(sin x)′ nimaga teng?", "cos x", ["−cos x", "sin x", "−sin x"], "Asosiy hosilalar jadvali."),
        C(2, "Jism s(t) = 2t³ − t qonun bo'yicha harakatlanadi. t = 1 da tezlik?", "5", ["1", "6", "4"], "v = s′ = 6t² − 1 = 5."),
        C(2, "s(t) = t² + 4t qonun bilan harakatlanayotgan jismning tezlanishi?", "2", ["4", "2t + 4", "0"], "a = s″ = 2."),
        C(3, "y = x² − 2x grafigiga o'tkazilgan urinma Ox o'qiga parallel bo'lgan nuqtaning abssissasi?", "1", ["2", "0", "−1"], "y′ = 2x − 2 = 0."),
        O(3, "y = √x grafigiga x = 4 nuqtada o'tkazilgan urinmaning burchak koeffitsientini o'nli kasrda yozing.", ["0,25", "0.25", "1/4"], "y′ = 1/(2√x) = 1/4."),
    ],
    "MF.5": [
        C(1, "y = cos x funksiyaning eng kichik qiymati?", "−1", ["0", "1", "−2"], "Kosinusning qiymatlar sohasi [−1; 1]."),
        C(2, "y = sin 3x funksiyaning eng kichik musbat davri?", "2π/3", ["3π", "π/3", "6π"], "T = 2π/3."),
        C(2, "y = 2 + sin x funksiyaning qiymatlar sohasi?", "[1; 3]", ["[−1; 1]", "[0; 2]", "[2; 3]"], "sin x ∈ [−1; 1] → 2 + sin x ∈ [1; 3]."),
        O(2, "y = 5cos x funksiyaning eng katta qiymatini yozing.", ["5"], "Amplituda 5."),
    ],
    "MF.7": [
        C(2, "Qirrasi 3 bo'lgan kubning diagonali?", "3√3", ["3√2", "9", "6"], "d = a√3."),
        C(2, "To'g'ri burchakli parallelepiped o'lchamlari 2, 3, 6. Diagonali?", "7", ["11", "√13", "6"], "√(4 + 9 + 36) = 7."),
        O(3, "Shar radiusi 3. Uning sirti π ning necha baravariga teng?", ["36"], "S = 4πr² = 36π."),
    ],
    "MF.8": [
        C(1, "A = {1; 2; 3}, B = {2; 3; 4}. A ∩ B ni toping.", "{2; 3}", ["{1; 4}", "{1; 2; 3; 4}", "{2}"], "Ikkala to'plamga tegishli elementlar."),
        C(2, "A = {1; 2; 3}, B = {2; 3; 4}. A ∪ B to'plamning elementlari soni?", "4", ["6", "3", "2"], "{1; 2; 3; 4}."),
        C(2, "30 o'quvchidan 20 tasi futbolni, 15 tasi basketbolni yoqtiradi; har biri kamida bittasini yoqtiradi. Ikkalasini yoqtiruvchilar soni?", "5", ["10", "15", "0"], "20 + 15 − 30 = 5."),
    ],
}

PHYS: dict[str, list] = {
    "P7.1": [
        C(1, "Yo'l va ko'chish moduli qachon teng bo'ladi?", "To'g'ri chiziqli, bir yo'nalishdagi harakatda", ["Aylana bo'ylab harakatda", "Har doim", "Hech qachon"], "Yo'nalish o'zgarmasa, trayektoriya uzunligi ko'chish moduliga teng."),
        C(2, "Jism 6 m shimolga, so'ng 6 m janubga yurdi. Ko'chish moduli?", "0 m", ["12 m", "6 m", "6√2 m"], "Jism boshlang'ich nuqtaga qaytdi."),
        C(2, "Jism 8 m g'arbga, so'ng 6 m shimolga yurdi. Yo'l va ko'chish moduli farqi?", "4 m", ["2 m", "0 m", "14 m"], "Yo'l 14 m, ko'chish √(64 + 36) = 10 m."),
    ],
    "P7.3": [
        C(1, "Jismga ta'sir etuvchi kuchlarning teng ta'sir etuvchisi nolga teng bo'lsa, jism…", "tinch turadi yoki to'g'ri chiziqli tekis harakatlanadi", ["albatta tinch turadi", "tezlanish bilan harakatlanadi", "aylana bo'ylab harakatlanadi"], "Nyutonning birinchi qonuni."),
        C(2, "5 N va 12 N kuchlar o'zaro perpendikulyar. Teng ta'sir etuvchi?", "13 N", ["17 N", "7 N", "60 N"], "√(25 + 144) = 13."),
        C(3, "Bir nuqtaga 4 N va 7 N kuchlar qo'yilgan. Teng ta'sir etuvchi qaysi qiymatni qabul qila olmaydi?", "2 N", ["3 N", "8 N", "11 N"], "3 N ≤ R ≤ 11 N."),
    ],
    "P9.4": [
        C(1, "Gorizontal otilgan jismning trayektoriyasi qanday chiziq?", "Parabola", ["To'g'ri chiziq", "Aylana", "Giperbola"], "Gorizontal tekis va vertikal tekis tezlanuvchan harakatlar qo'shiladi."),
        C(2, "Jism 80 m balandlikdan gorizontal otildi (g = 10 m/s²). Uchish vaqti?", "4 s", ["8 s", "2 s", "16 s"], "t = √(2h/g) = √16 = 4 s."),
        C(3, "Burchak ostida otilgan jismning eng yuqori nuqtadagi tezligi (v₀ = 20 m/s, α = 60°)?", "10 m/s", ["0", "17,3 m/s", "20 m/s"], "Faqat gorizontal tashkil etuvchi qoladi: v₀cos 60° = 10 m/s."),
    ],
    "P9.8": [
        C(1, "Qo'zg'aluvchan blok kuchdan necha marta yutuq beradi (ishqalanishsiz, blok vaznsiz)?", "2 marta", ["Yutuq bermaydi", "4 marta", "1,5 marta"], "Yuk ikkita ip tarmog'iga osilgan."),
        C(2, "Atvud mashinasida m₁ = m₂ = 2 kg. Tizimning tezlanishi?", "0", ["10 m/s²", "5 m/s²", "2,5 m/s²"], "Massalar teng — tizim muvozanatda."),
        O(3, "Atvud mashinasida m₁ = 3 kg, m₂ = 7 kg (g = 10 m/s²). Tezlanish necha m/s²?", ["4"], "a = (7 − 3) · 10 / 10 = 4."),
    ],
    "P9.9": [
        C(2, "Yer markazidan 3R masofada erkin tushish tezlanishi (Yer sirtida g₀ = 10 m/s²)?", "≈1,1 m/s²", ["3,3 m/s²", "5 m/s²", "0,9 m/s²"], "g = g₀ / 9 ≈ 1,1 m/s²."),
        C(1, "Gravitatsiya doimiysi G ning qiymati?", "6,67·10⁻¹¹ N·m²/kg²", ["9,8 N/kg", "6,02·10²³ mol⁻¹", "1,38·10⁻²³ J/K"], "Kavendish tajribasida aniqlangan."),
        C(3, "Ikki jismning massalari ham, ular orasidagi masofa ham 2 marta oshirildi. Tortishish kuchi qanday o'zgaradi?", "O'zgarmaydi", ["4 marta ortadi", "2 marta kamayadi", "2 marta ortadi"], "(2 · 2)/2² = 1."),
    ],
    "P9.10": [
        C(2, "Yuqoriga harakatlanayotgan lift 3 m/s² tezlanish bilan tormozlanmoqda (tezlanish pastga). 40 kg bolaning og'irligi (g = 10 m/s²)?", "280 N", ["520 N", "400 N", "120 N"], "P = m(g − a) = 40 · 7 = 280 N."),
        C(3, "Lift pastga a = g tezlanish bilan harakatlanmoqda. Undagi odamning og'irligi?", "Nolga teng", ["2mg", "mg", "mg/2"], "P = m(g − a) = 0 — vaznsizlik."),
        O(2, "Lift 1 m/s² tezlanish bilan yuqoriga ko'tarilmoqda. 50 kg odamning og'irligi necha N? (g = 10 m/s²)", ["550"], "P = m(g + a) = 50 · 11."),
    ],
    "P9.12": [
        C(1, "Kinetik energiya formulasi?", "E = mv²/2", ["E = mgh", "E = kx²/2", "E = mv"], "Harakatlanayotgan jism energiyasi."),
        C(2, "2 kg jism 5 m balandlikda turibdi (g = 10 m/s²). Potensial energiyasi?", "100 J", ["10 J", "50 J", "1000 J"], "E = mgh = 2 · 10 · 5."),
        C(3, "Jism tezligi 3 marta oshsa, kinetik energiyasi…", "9 marta ortadi", ["3 marta ortadi", "6 marta ortadi", "o'zgarmaydi"], "E ~ v²."),
    ],
    "P9.13": [
        C(1, "Jism impulsi formulasi?", "p = mv", ["p = mv²/2", "p = Ft²", "p = m/v"], "Impuls — massa va tezlik ko'paytmasi."),
        C(2, "4 kg jism 3 m/s tezlik bilan harakatlanmoqda. Impulsi?", "12 kg·m/s", ["18 kg·m/s", "7 kg·m/s", "36 kg·m/s"], "p = 4 · 3."),
        O(3, "Massasi 50 kg tinch turgan qayiqdan 10 kg tosh gorizontal 5 m/s tezlik bilan otildi. Qayiq qanday tezlik oladi (m/s)?", ["1"], "Impuls saqlanishi: 50v = 10 · 5."),
    ],
    "P9.14": [
        C(2, "Kater oqim bo'ylab 20 km ni 1 soatda, oqimga qarshi 2 soatda o'tdi. Oqim tezligi?", "5 km/soat", ["10 km/soat", "15 km/soat", "2,5 km/soat"], "v + u = 20, v − u = 10 → u = 5."),
        C(2, "Kater oqim bo'ylab 20 km/soat, oqimga qarshi 10 km/soat tezlikda suzadi. Uning turg'un suvdagi tezligi?", "15 km/soat", ["10 km/soat", "20 km/soat", "30 km/soat"], "(20 + 10)/2 = 15."),
        C(3, "Bir yo'nalishda 72 km/soat va 54 km/soat tezlikda ketayotgan ikki avtomobil. Ikkinchisiga nisbatan birinchisining tezligi?", "5 m/s", ["35 m/s", "18 m/s", "126 km/soat"], "72 − 54 = 18 km/soat = 5 m/s."),
    ],
    "P9.15": [
        C(2, "Quvur diametri 2 marta kamaysa, undagi suyuqlik tezligi…", "4 marta ortadi", ["2 marta ortadi", "4 marta kamayadi", "o'zgarmaydi"], "S ~ d², Sv = const."),
        O(3, "Quvurda suv 2 m/s tezlikda oqmoqda, kesim yuzi 10 sm². 1 s da necha litr suv oqib o'tadi?", ["2"], "Q = Sv = 10·10⁻⁴ · 2 = 2·10⁻³ m³ = 2 l."),
    ],
    "P9.16": [
        C(2, "Prujinani teng ikkiga bo'lsak, har bir bo'lakning qattiqligi…", "2 marta ortadi", ["2 marta kamayadi", "o'zgarmaydi", "4 marta ortadi"], "k ~ 1/l."),
        C(1, "Richagning muvozanat sharti?", "F₁l₁ = F₂l₂", ["F₁l₂ = F₂l₁", "F₁ + F₂ = 0", "F₁/l₁ = F₂/l₂"], "Kuch momentlari teng."),
        O(2, "Qattiqligi 200 N/m prujinaga 10 N kuch ta'sir etmoqda. Cho'zilish necha sm?", ["5"], "x = F/k = 0,05 m."),
    ],
    "P8.4": [
        C(2, "Dvigatel FIK 30%, isitkichdan 2000 J issiqlik olgan. Sovitkichga berilgan issiqlik?", "1400 J", ["600 J", "2600 J", "1000 J"], "A = 0,3 · 2000 = 600 J; Q₂ = 2000 − 600 = 1400 J."),
        C(1, "Bug' turbinasi va ichki yonuv dvigateli qaysi turdagi dvigatellar?", "Issiqlik dvigatellari", ["Elektr dvigatellari", "Gidravlik dvigatellar", "Magnit dvigatellari"], "Yoqilg'i energiyasini mexanik ishga aylantiradi."),
    ],
    "P10.1": [
        C(1, "Kislorodning (O₂) molyar massasi?", "0,032 kg/mol", ["0,016 kg/mol", "32 kg/mol", "0,064 kg/mol"], "M(O₂) = 32 g/mol."),
        O(2, "88 g karbonat angidrid (M = 44 g/mol) necha mol?", ["2"], "ν = 88/44 = 2."),
    ],
    "P10.2": [
        C(1, "27 °C necha kelvin?", "300 K", ["246 K", "273 K", "327 K"], "T = t + 273."),
        C(3, "Gaz konsentratsiyasi o'zgarmay, molekulalarning o'rtacha kinetik energiyasi 2 marta oshdi. Bosim…", "2 marta ortadi", ["4 marta ortadi", "o'zgarmaydi", "2 marta kamayadi"], "p = ⅔ nĒ."),
    ],
    "P10.3": [
        C(2, "Izotermik jarayonda gaz hajmi 3 marta kamaydi. Bosim…", "3 marta ortdi", ["3 marta kamaydi", "9 marta ortdi", "o'zgarmadi"], "Boyl–Mariott qonuni: pV = const."),
        C(3, "Gaz bosimi 2 marta, absolyut temperaturasi 4 marta oshdi. Hajm qanday o'zgardi?", "2 marta ortdi", ["8 marta ortdi", "2 marta kamaydi", "o'zgarmadi"], "V ~ T/p = 4/2 = 2."),
    ],
    "P10.6": [
        C(2, "Idishda 2 mol He va 2 mol Ne bor, umumiy bosim 200 kPa. He ning parsial bosimi?", "100 kPa", ["200 kPa", "50 kPa", "400 kPa"], "Mol ulushi 1/2."),
        O(3, "Idishda parsial bosimlari 30 kPa, 50 kPa va 20 kPa bo'lgan uch gaz bor. Umumiy bosim necha kPa?", ["100"], "Dalton qonuni: bosimlar qo'shiladi."),
    ],
    "P10.7": [
        C(2, "Tog' cho'qqisida suv 100 °C dan past temperaturada qaynaydi, chunki…", "atmosfera bosimi past", ["havo sovuq", "suv tozaroq", "kislorod ko'p"], "Qaynash temperaturasi tashqi bosimga bog'liq."),
        C(1, "Havoning nisbiy namligini o'lchaydigan asbob?", "Psixrometr (gigrometr)", ["Barometr", "Manometr", "Dinamometr"], "Quruq va nam termometr ko'rsatishlari farqi bo'yicha."),
    ],
    "P10.8": [
        C(2, "Temperatura ortganda suyuqlikning sirt taranglik koeffitsiyenti…", "kamayadi", ["ortadi", "o'zgarmaydi", "avval ortib, keyin kamayadi"], "Molekulalararo bog'lanish zaiflashadi."),
        C(2, "Suvga sovun qo'shilsa, uning sirt tarangligi…", "kamayadi", ["ortadi", "o'zgarmaydi", "nolga teng bo'ladi"], "Sovun — sirt-faol modda."),
    ],
    "P10.9": [
        C(1, "Elastik deformatsiya qanday deformatsiya?", "Kuch olingach yo'qoladigan", ["Kuch olingach saqlanib qoladigan", "Faqat siqilish", "Faqat buralish"], "Jism dastlabki shakliga qaytadi."),
        O(3, "Uzunligi 1 m, kesimi 1 mm² po'lat sim (E = 2·10¹¹ Pa) 200 N kuch bilan cho'zildi. Absolyut uzayish necha mm?", ["1"], "Δl = FL/(ES) = 200 · 1 / (2·10¹¹ · 10⁻⁶) = 10⁻³ m."),
    ],
    "P10.11": [
        C(2, "Karno siklida isitkich 600 K, sovitkich 450 K. FIK?", "25%", ["75%", "33%", "50%"], "η = 1 − 450/600 = 0,25."),
        C(2, "Ideal gaz izotermik kengayganda olgan issiqlik nimaga sarflanadi?", "To'liq ish bajarishga", ["Ichki energiyani oshirishga", "Temperaturani oshirishga", "Hech narsaga"], "ΔU = 0, demak Q = A."),
    ],
    "P10.12": [
        C(2, "1 kg suvni 20 °C dan 100 °C gacha isitish uchun kerakli issiqlik (c = 4200 J/(kg·°C))?", "336 kJ", ["420 kJ", "84 kJ", "3,36 kJ"], "Q = 4200 · 1 · 80 = 336 000 J."),
        C(2, "20 °C li 2 kg suv va 80 °C li 1 kg suv aralashtirildi. Muvozanat temperaturasi?", "40 °C", ["50 °C", "60 °C", "30 °C"], "(2 · 20 + 1 · 80)/3 = 40."),
        O(3, "30 °C li 3 kg suvga 90 °C li necha kg suv qo'shilsa, aralashma 50 °C bo'ladi?", ["1,5", "1.5"], "3 · 20 = m · 40 → m = 1,5 kg."),
    ],
    "P11.2": [
        C(2, "Nuqtaviy zaryaddan masofa 3 marta ortsa, maydon kuchlanganligi…", "9 marta kamayadi", ["3 marta kamayadi", "9 marta ortadi", "o'zgarmaydi"], "E ~ 1/r²."),
        C(2, "Zaryadlangan o'tkazgich ichidagi elektr maydon kuchlanganligi?", "Nolga teng", ["Sirtdagidan katta", "Markazda maksimal", "Cheksiz"], "Zaryadlar o'tkazgich sirtida joylashadi."),
    ],
    "P11.3": [
        C(1, "Bir jinsli elektr maydonda kuchlanish va kuchlanganlik bog'lanishi?", "U = E·d", ["U = E/d", "U = E·d²", "U = q·E"], "d — kuch chiziqlari bo'ylab masofa."),
        O(2, "Nuqtaviy zaryaddan (q = 1·10⁻⁹ C) 0,1 m masofadagi potensial necha volt? (k = 9·10⁹ N·m²/C²)", ["90"], "φ = kq/r = 9·10⁹ · 10⁻⁹ / 0,1 = 90 V."),
    ],
    "P11.6": [
        C(2, "ε = 6 V, r = 1 Ω manbaga R = 2 Ω rezistor ulangan. Manba ichida ajraladigan quvvat?", "4 W", ["8 W", "12 W", "2 W"], "I = 6/3 = 2 A; P = I²r = 4 W."),
        C(3, "Manbaning qisqa tutashuv toki 10 A, EYK 5 V. Ichki qarshilik?", "0,5 Ω", ["2 Ω", "50 Ω", "5 Ω"], "r = ε/I = 0,5 Ω."),
    ],
    "P11.7": [
        C(2, "Kirxgofning birinchi qonuni qaysi saqlanish qonuniga asoslangan?", "Elektr zaryadining saqlanishi", ["Energiyaning saqlanishi", "Impulsning saqlanishi", "Massaning saqlanishi"], "Tugunda zaryad to'planib qolmaydi."),
        C(2, "Kirxgofning ikkinchi qonuni qaysi saqlanish qonuniga asoslangan?", "Energiyaning saqlanishi", ["Elektr zaryadining saqlanishi", "Impulsning saqlanishi", "Massaning saqlanishi"], "Yopiq kontur bo'ylab potensiallar o'zgarishi yig'indisi nolga teng."),
    ],
    "P11.9": [
        C(2, "Vakuumda elektr toki qanday hosil qilinadi?", "Termoelektron emissiya yordamida", ["Ionlar harakati bilan", "Elektroliz yordamida", "Kovaklar harakati bilan"], "Qizdirilgan katoddan elektronlar uchib chiqadi."),
        C(2, "p-tipli yarimo'tkazgichda asosiy zaryad tashuvchilar?", "kovaklar", ["elektronlar", "ionlar", "protonlar"], "Akseptor kiritmalar kovaklar hosil qiladi."),
    ],
    "P11.11": [
        C(2, "G'altakdan o'tayotgan magnit oqimi o'zgarmasa, induksion tok…", "hosil bo'lmaydi", ["maksimal bo'ladi", "doimiy bo'ladi", "o'zgaruvchan bo'ladi"], "ε = −ΔΦ/Δt = 0."),
        O(3, "Yuzasi 0,02 m² kontur magnit maydonga perpendikulyar joylashgan. Induksiya 0,5 s da 0 dan 1 T gacha tekis ortdi. EYK necha mV?", ["40"], "ΔΦ = 0,02 Wb; ε = 0,02/0,5 = 0,04 V."),
    ],
    "P11.12": [
        C(1, "G'altak magnit maydoni energiyasi formulasi?", "W = LI²/2", ["W = CU²/2", "W = LI", "W = L²I/2"], "L — induktivlik, I — tok."),
        C(3, "G'altakdagi tok 2 marta oshsa, magnit maydon energiyasi…", "4 marta ortadi", ["2 marta ortadi", "o'zgarmaydi", "2 marta kamayadi"], "W ~ I²."),
        O(2, "L = 0,4 H g'altakdan 5 A tok o'tmoqda. Magnit maydon energiyasi necha J?", ["5"], "W = 0,4 · 25 / 2 = 5 J."),
    ],
    "P11.13": [
        C(2, "LC konturda kondensator to'liq zaryadlangan paytda g'altakdagi tok?", "Nolga teng", ["Maksimal", "Maksimalning yarmiga teng", "Doimiy"], "Energiya to'liq elektr maydonda."),
        O(3, "Tebranish konturida C = 10 μF, maksimal kuchlanish 100 V. Elektr maydonning maksimal energiyasi necha J?", ["0,05", "0.05"], "W = CU²/2 = 10⁻⁵ · 10⁴ / 2 = 0,05 J."),
    ],
    "P11.17": [
        C(1, "Ultratovush chastotasi qanday?", "20 kHz dan yuqori", ["20 Hz dan kichik", "20 Hz – 20 kHz", "Faqat 1 kHz"], "Inson eshitish chegarasidan yuqori."),
        C(2, "Havoda tovush qanday to'lqin sifatida tarqaladi?", "Bo'ylama", ["Ko'ndalang", "Elektromagnit", "Sirt to'lqini"], "Havo zarralari to'lqin yo'nalishi bo'ylab tebranadi."),
    ],
    "P11.18": [
        C(2, "Elektromagnit to'lqinlar mavjudligini tajribada birinchi isbotlagan olim?", "G. Gers", ["J. Maksvell", "M. Faradey", "A. Popov"], "Gers 1888-yilda tajribada isbotlagan."),
        C(2, "Radioaloqada tovush signalini yuqori chastotali to'lqinga «yuklash» jarayoni?", "Modulyatsiya", ["Detektorlash", "Interferensiya", "Dispersiya"], "Qabul qilishda teskari jarayon — detektorlash."),
    ],
    "P11.22": [
        C(2, "Kamalak hosil bo'lishi qaysi hodisa bilan bog'liq?", "Dispersiya", ["Qutblanish", "Fotoeffekt", "Difraksiya"], "Suv tomchilarida yorug'lik sinib, ranglarga ajraladi."),
        C(3, "Shishada qaysi rangli nurning tezligi eng katta?", "Qizil", ["Binafsha", "Yashil", "Ko'k"], "Qizil nur uchun sindirish ko'rsatkichi eng kichik."),
    ],
    "P11.23": [
        C(2, "Maxsus nisbiylik nazariyasining birinchi postulati?", "Barcha inersial sanoq sistemalarida fizik qonunlar bir xil", ["Yorug'lik tezligi manbaga bog'liq", "Vaqt absolyut", "Massa doimiy"], "Eynshteyn nisbiylik prinsipi."),
        C(3, "v = 0,6c tezlikdagi jismning relyativistik massasi tinchlikdagi massasidan necha marta katta?", "1,25", ["1,6", "0,8", "1,67"], "1/√(1 − 0,36) = 1/0,8 = 1,25."),
    ],
    "P11.24": [
        C(1, "Plank doimiysi qiymati?", "6,63·10⁻³⁴ J·s", ["1,38·10⁻²³ J/K", "9,1·10⁻³¹ kg", "1,6·10⁻¹⁹ C"], "h = 6,63·10⁻³⁴ J·s."),
        C(2, "Absolyut qora jism nima?", "Tushgan barcha nurlanishni yutadigan jism", ["Barcha nurni qaytaradigan jism", "Qora rangga bo'yalgan har qanday jism", "Nur chiqarmaydigan jism"], "Ideal yutuvchi va ideal nurlantiruvchi."),
    ],
    "P11.26": [
        C(2, "Fotoeffekt uchun Eynshteyn tenglamasi?", "hν = A + mv²/2", ["hν = A − mv²/2", "E = mc²", "hν = mv"], "A — chiqish ishi."),
        C(3, "Foton to'lqin uzunligi 2 marta kamaysa, uning impulsi…", "2 marta ortadi", ["2 marta kamayadi", "4 marta ortadi", "o'zgarmaydi"], "p = h/λ."),
    ],
    "P11.28": [
        C(2, "Yadroda nuklonlarni ushlab turuvchi kuchlar?", "Yadro kuchlari (kuchli o'zaro ta'sir)", ["Elektrostatik kuchlar", "Gravitatsion kuchlar", "Magnit kuchlar"], "Qisqa masofada ta'sir etuvchi juda katta kuchlar."),
        O(2, "²⁷₁₃Al yadrosida nechta neytron bor?", ["14"], "N = A − Z = 27 − 13."),
    ],
    "P11.30": [
        C(2, "Alfa-yemirilishda yadroning massa va zaryad soni qanday o'zgaradi?", "A 4 ga, Z 2 ga kamayadi", ["A o'zgarmaydi, Z 1 ga ortadi", "A 2 ga, Z 4 ga kamayadi", "A 1 ga kamayadi, Z o'zgarmaydi"], "Geliy yadrosi (⁴₂He) ajraladi."),
        C(2, "Beta-minus yemirilishda yadroning zaryad soni…", "1 ga ortadi", ["1 ga kamayadi", "2 ga kamayadi", "o'zgarmaydi"], "Neytron protonga aylanib, elektron ajraladi."),
    ],
    "P11.31": [
        C(1, "Fotonning tinchlikdagi massasi?", "Nolga teng", ["Elektron massasiga teng", "Proton massasiga teng", "Cheksiz"], "Foton faqat harakatda mavjud."),
        C(2, "d kvarkning elektr zaryadi?", "−1/3 e", ["+2/3 e", "−2/3 e", "+1/3 e"], "Neytron (udd): 2/3 − 1/3 − 1/3 = 0."),
    ],
}

CHEM: dict[str, list] = {
    "K8.11": [
        C(1, "A guruhcha elementining guruh raqami nimani bildiradi?", "Tashqi qavatdagi elektronlar sonini", ["Elektron qavatlar sonini", "Neytronlar sonini", "Atom massasini"], "Masalan, Na (IA) — tashqi qavatda 1 elektron."),
        C(2, "Davr raqami nimani bildiradi?", "Elektron qavatlar sonini", ["Valent elektronlar sonini", "Protonlar sonini", "Izotoplar sonini"], "Masalan, 3-davr elementlarida 3 ta qavat."),
        C(2, "Guruhda yuqoridan pastga metallik xossalar qanday o'zgaradi?", "Kuchayadi", ["Susayadi", "O'zgarmaydi", "Avval kuchayib, keyin susayadi"], "Atom radiusi ortib, tashqi elektron oson beriladi."),
        O(2, "Natriy (Na) nechanchi guruhda joylashgan? (raqam bilan)", ["1", "I"], "Na — IA guruh."),
    ],
    "K8.13": [
        C(1, "Kimyoviy tenglamani tenglashtirish qaysi qonunga asoslanadi?", "Massaning saqlanish qonuni", ["Avogadro qonuni", "Tarkibning doimiylik qonuni", "Davriy qonun"], "Reaksiyadan oldin va keyin atomlar soni teng."),
        C(2, "Al + HCl → AlCl₃ + H₂ tenglamani tenglashtiring. HCl oldidagi koeffitsient?", "6", ["3", "2", "4"], "2Al + 6HCl → 2AlCl₃ + 3H₂."),
        C(2, "CH₄ + O₂ → CO₂ + H₂O tenglamadagi koeffitsientlar yig'indisi?", "6", ["4", "5", "7"], "CH₄ + 2O₂ → CO₂ + 2H₂O: 1 + 2 + 1 + 2 = 6."),
        C(3, "Fe₂O₃ + CO → Fe + CO₂ tenglamani tenglashtiring. CO oldidagi koeffitsient?", "3", ["2", "1", "4"], "Fe₂O₃ + 3CO → 2Fe + 3CO₂."),
        O(3, "KClO₃ → KCl + O₂ tenglamadagi koeffitsientlar yig'indisini toping.", ["7"], "2KClO₃ → 2KCl + 3O₂: 2 + 2 + 3 = 7."),
    ],
    "K8.14": [
        C(1, "Cu belgisi qaysi elementga tegishli?", "Mis", ["Kumush", "Kalsiy", "Xrom"], "Lotincha cuprum."),
        C(1, "Kalsiyning kimyoviy belgisi?", "Ca", ["K", "C", "Cl"], "Calcium."),
        C(2, "S belgisi qaysi element?", "Oltingugurt", ["Kremniy", "Qalay", "Natriy"], "Lotincha sulfur."),
        C(2, "Si belgisi qaysi element?", "Kremniy", ["Kumush", "Oltingugurt", "Qalay"], "Lotincha silicium."),
    ],
    "K8.15": [
        C(1, "Qaysi moddada kovalent qutbsiz bog'lanish bor?", "Cl₂", ["HCl", "NaCl", "H₂O"], "Bir xil metallmas atomlari orasida."),
        C(2, "Metall bog'lanish qaysi moddalarga xos?", "Metallar va qotishmalarga", ["Tuzlarga", "Gazlarga", "Kislotalarga"], "Erkin elektronlar «elektron gazi» hosil qiladi."),
        C(2, "Qaysi moddada ionli bog'lanish bor?", "KF", ["HF", "F₂", "CF₄"], "Faol metall va faol metallmas o'rtasida."),
        C(3, "Vodorod bog'lanish suvning qaysi xossasini tushuntiradi?", "Nisbatan yuqori qaynash temperaturasini", ["Rangsizligini", "Elektr tokini yomon o'tkazishini", "Hidsizligini"], "Molekulalar o'zaro qo'shimcha bog'lanadi."),
    ],
    "K9.16": [
        C(2, "Kaliy suv bilan reaksiyaga kirishganda qanday gaz ajraladi?", "Vodorod", ["Kislorod", "Azot", "Xlor"], "2K + 2H₂O → 2KOH + H₂↑."),
        C(2, "Qaysi metall suyultirilgan sulfat kislotadan vodorodni siqib chiqaradi?", "Temir", ["Kumush", "Mis", "Oltin"], "Faollik qatorida vodoroddan oldin turadi."),
        C(3, "Qaysi juftlikda reaksiya boradi?", "Mg + FeSO₄", ["Cu + ZnSO₄", "Ag + CuSO₄", "Fe + MgSO₄"], "Faolroq metall kamroq faol metallni tuzidan siqib chiqaradi."),
    ],
    "K9.17": [
        C(2, "Elektrokimyoviy korroziya qachon tezlashadi?", "Metall elektrolit eritmasi bilan tegib turganda", ["Quruq havoda", "Vakuumda", "Past temperaturali quruq joyda"], "Galvanik juftlar hosil bo'ladi."),
        C(2, "Temir mis bilan tutashib, nam muhitda qolsa, qaysi metall tezroq yemiriladi?", "Temir", ["Mis", "Ikkalasi bir xil", "Hech biri"], "Faolroq metall anod vazifasini bajaradi."),
        C(1, "Korroziya ingibitori nima?", "Korroziyani sekinlashtiruvchi modda", ["Korroziyani tezlashtiruvchi modda", "Zang turi", "Bo'yoq turi"], "Ingibitor — to'xtatuvchi."),
    ],
    "K9.18": [
        C(2, "Grafitning kristall panjara turi?", "Atom", ["Ionli", "Molekulyar", "Metall"], "Uglerod atomlari kovalent bog'langan."),
        C(2, "Quruq muz (qattiq CO₂) qanday kristall panjaraga ega?", "Molekulyar", ["Atom", "Ionli", "Metall"], "Shuning uchun oson sublimatsiyalanadi."),
        C(3, "Kvars (SiO₂) yuqori qattiqligi va erish temperaturasi qaysi panjara turi bilan bog'liq?", "Atom panjara", ["Molekulyar panjara", "Ionli panjara", "Metall panjara"], "Si–O kovalent bog'lar butun kristallni bog'laydi."),
    ],
    "K9.19": [
        C(2, "Karbamid (CO(NH₂)₂, Mr = 60) da azotning massa ulushi?", "46,7%", ["23,3%", "35%", "28%"], "28/60 ≈ 0,467."),
        C(2, "Kaliyli o'g'itlar o'simlikka nima uchun kerak?", "Ildiz va tuganak rivoji hamda kasalliklarga chidamlilik uchun", ["Faqat bargni yashil qilish uchun", "Fotosintezni to'xtatish uchun", "Urug'ni zararsizlantirish uchun"], "Kaliy suv almashinuvi va fermentlar ishini boshqaradi."),
        C(1, "Go'ng qanday o'g'it?", "Organik o'g'it", ["Mineral o'g'it", "Mikroo'g'it", "Sintetik o'g'it"], "Tabiiy organik qoldiq."),
    ],
    "K9.20": [
        C(1, "Ozon qatlami Yerni nimadan himoya qiladi?", "Ultrabinafsha nurlardan", ["Infraqizil nurlardan", "Radio to'lqinlardan", "Meteoritlardan"], "O₃ qisqa to'lqinli UB nurlarni yutadi."),
        C(2, "Smog hosil bo'lishiga asosan nima sabab bo'ladi?", "Sanoat va transport chiqindi gazlari", ["Okean bug'lari", "O'simliklar fotosintezi", "Tog' shamollari"], "Tutun, azot oksidlari va changlar."),
        C(2, "Kislotali tuproqni neytrallash uchun unga nima qo'shiladi?", "Ohak (CaCO₃)", ["Osh tuzi", "Sulfat kislota", "Ammiakli selitra"], "Ohaklash."),
    ],
    "K10.11": [
        C(2, "Neft haydalganda eng yuqori temperaturada qaynaydigan qoldiq?", "Mazut", ["Benzin", "Kerosin", "Ligroin"], "Mazutdan surkov moylari olinadi."),
        C(2, "Tabiiy gaz tarkibida metandan tashqari qanday gazlar bo'ladi?", "Etan, propan, butan", ["Kislorod, ozon", "Xlor, ftor", "Neon, argon"], "Yo'ldosh uglevodorodlar."),
        C(2, "O'zbekistondagi yirik gaz-kimyo majmuasi?", "Sho'rtan gaz-kimyo majmuasi", ["Olmaliq kon-metallurgiya kombinati", "Navoiy kon-metallurgiya kombinati", "Bekobod metallurgiya kombinati"], "Polietilen va suyultirilgan gaz ishlab chiqaradi."),
    ],
    "K10.12": [
        C(1, "CH₃–CH₂–OH qaysi sinfga kiradi?", "Spirtlar", ["Aldegidlar", "Karbon kislotalar", "Efirlar"], "–OH gidroksil guruhi."),
        C(2, "HCHO moddaning nomi?", "Metanal (formaldegid)", ["Metanol", "Metan kislota", "Etanal"], "Eng oddiy aldegid."),
        C(2, "CH₃–CH₂–CH₂–CH₂–CH₃ moddaning nomi?", "Pentan", ["Butan", "Geksan", "2-metilbutan"], "Besh uglerodli tarmoqlanmagan alkan."),
        O(1, "C₂H₆ uglevodorodining nomini yozing.", ["etan", "Etan"], "Ikki uglerodli alkan."),
    ],
    "K11.13": [
        C(2, "D vitamini yetishmasa qanday kasallik rivojlanadi?", "Raxit", ["Singa", "Shapko'rlik", "Beri-beri"], "Suyaklar to'g'ri shakllanmaydi."),
        C(2, "C vitamini yetishmasligidan qanday kasallik rivojlanadi?", "Singa", ["Raxit", "Beri-beri", "Shapko'rlik"], "Milklar qonaydi, tishlar bo'shashadi."),
        C(2, "Adrenalin qaysi bezning gormoni?", "Buyrak usti bezi", ["Qalqonsimon bez", "Oshqozon osti bezi", "Gipofiz"], "Stress gormoni."),
    ],
}

ENG: dict[str, list] = {
    "E28": [
        C(1, "Read: 'Dilnoza works in a hospital. She helps sick children every day.' — What is Dilnoza's job most likely?", "a nurse or a doctor", ["a teacher", "a driver", "a farmer"], "Kasalxonada bemor bolalarga yordam beradi."),
        C(2, "Read: 'The museum is free on Mondays, but visitors pay 20,000 sum on other days.' — When can you visit the museum for free?", "On Mondays", ["On Sundays", "Every day", "Never"], "Matnda aniq aytilgan: free on Mondays."),
        C(2, "Read: 'Bobur saved money for three months and finally bought a bicycle.' — What is the main idea?", "Bobur bought a bicycle after saving money.", ["Bobur lost his money.", "Bobur's bicycle was stolen.", "Bobur borrowed a bicycle."], "Asosiy fikr — pul yig'ib velosiped sotib olgani."),
        C(3, "Read: 'Many students study late at night, but research shows that sleep improves memory more than extra hours of reading.' — What does the text suggest?", "Getting enough sleep helps students remember more.", ["Students should read all night.", "Sleep has no effect on memory.", "Research is not useful for students."], "Uyqu xotirani ko'proq yaxshilaydi."),
    ],
    "E29": [
        C(2, "Read: 'After the long drought, the farmers were relieved when the rain finally came.' — 'relieved' means:", "no longer worried", ["very angry", "surprised and afraid", "bored"], "relieved — xavotirdan qutulgan."),
        C(2, "Read: 'Aziz always arrives on time and never forgets his homework.' — What can we infer about Aziz?", "He is responsible.", ["He is lazy.", "He is often late.", "He dislikes school."], "Har doim vaqtida keladi va vazifani unutmaydi — mas'uliyatli."),
        C(3, "Read: 'The film was so dull that half of the audience left before the end.' — 'dull' means:", "boring", ["exciting", "frightening", "funny"], "Tomoshabinlar chiqib ketgan — zerikarli."),
        C(3, "Read: 'Sardor took his umbrella, although the sky was clear in the morning.' — Why did he probably take it?", "He expected it might rain later.", ["It was raining in the morning.", "He wanted to sell it.", "The sky was dark."], "although — ertalab ochiq bo'lsa ham, keyin yomg'ir kutgan."),
    ],
    "E37": [
        C(2, "Every morning she ___ coffee, but today she ___ tea.", "drinks / is drinking", ["is drinking / drinks", "drank / drinks", "drinks / drinks"], "Odat — Present Simple; bugungi vaqtinchalik holat — Present Continuous."),
        C(2, "When I arrived, the lesson ___ already ___.", "had / started", ["has / started", "was / starting", "did / start"], "O'tmishdagi nuqtadan oldin tugagan ish — Past Perfect."),
        C(3, "I ___ this book three times, and I'm reading it again now.", "have read", ["read", "had read", "am reading"], "Hozirgacha bo'lgan tajriba — Present Perfect."),
        C(3, "This time next week we ___ on the beach.", "will be lying", ["will lie", "lie", "are lying to"], "Kelajakdagi aniq paytda davom etayotgan ish — Future Continuous."),
    ],
    "E43": [
        C(2, "My grandmother ___ her blood pressure checked every month.", "has", ["makes", "does", "lets"], "have something done — ishni boshqaga bajartirish."),
        C(3, "I got my brother ___ me with the boxes.", "to help", ["help", "helped", "helping"], "get + kishi + to-infinitive."),
    ],
    "E44": [
        C(2, "Could you tell me ___ the bank opens?", "what time", ["what time does", "when does", "does what time"], "Bilvosita savolda yordamchi fe'l (does) ishlatilmaydi."),
        C(3, "I asked her if she ___ come to the party.", "would", ["will she", "does", "would she"], "O'zlashtirma savolda zamon moslashuvi va darak gap tartibi."),
    ],
    "E48": [
        C(2, "___ the rain, the match continued.", "Despite", ["Although", "Unless", "Even though"], "Despite + ot (the rain)."),
        C(3, "You can't enter the building ___ you have a pass.", "unless", ["despite", "although", "in spite of"], "unless = if not."),
    ],
}

RUS: dict[str, list] = {
    "R31": [
        C(1, "Найдите приставку в слове «подоконник».", "под-", ["подо-", "окон-", "-ник"], "под-окон-ник: приставка под-, корень -окон-, суффикс -ник."),
        C(2, "Каким способом образовано слово «пароход»?", "Сложением основ", ["Приставочным", "Суффиксальным", "Бессуффиксным"], "пар + о + ход."),
        C(2, "Укажите однокоренное слово к слову «вода».", "подводный", ["водитель", "вожатый", "возить"], "Корень -вод- со значением «вода»."),
    ],
    "R32": [
        C(2, "В каком слове ударение поставлено верно?", "тОрты", ["звОнит", "катАлог", "щАвель"], "Нормы: тОрты, звонИт, каталОг, щавЕль."),
        C(2, "В каком слове ударение падает на последний слог?", "жалюзИ", ["тОрты", "бАнты", "крАны"], "жалюзИ; остальные — с ударением на первом слоге."),
        C(3, "В каком ряду во всех словах ударение падает на второй слог?", "звонИт, красИвее, щавЕль", ["тОрты, звонИт, щавЕль", "каталОг, бАнты, свЁкла", "жалюзИ, договОр, звонИт"], "звонИт, красИвее, щавЕль — 2-й слог; тОрты, бАнты, свЁкла — 1-й; каталОг, жалюзИ, договОр — 3-й."),
    ],
    "R33": [
        C(2, "В каком предложении нужно поставить тире между подлежащим и сказуемым?", "Москва столица России.", ["Он мой друг.", "Сегодня холодно.", "Я студент."], "Подлежащее и сказуемое — существительные в именительном падеже; при местоимении тире не ставится."),
        C(2, "Нужно ли тире в предложении «Дважды два четыре»?", "Да, подлежащее и сказуемое выражены числительными", ["Нет", "Только в разговорной речи", "Нужна запятая"], "Дважды два — четыре."),
        C(3, "В каком предложении тире НЕ ставится?", "Брат как отец.", ["Книга источник знаний.", "Курить здоровью вредить.", "Мой брат врач."], "Перед сравнительным союзом «как» тире не ставится."),
    ],
    "R34": [
        C(1, "Кто автор романа «Отцы и дети»?", "И. С. Тургенев", ["Л. Н. Толстой", "Ф. М. Достоевский", "И. А. Гончаров"], "Роман 1862 года."),
        C(2, "Главный герой романа «Преступление и наказание»?", "Родион Раскольников", ["Евгений Базаров", "Григорий Печорин", "Илья Обломов"], "Роман Ф. М. Достоевского."),
        C(2, "Кто написал роман «Герой нашего времени»?", "М. Ю. Лермонтов", ["А. С. Пушкин", "Н. В. Гоголь", "А. П. Чехов"], "Главный герой — Печорин."),
    ],
}


# ---------------------------------------------------------------------------
# Xato / chala savollarni tuzatish (sanitize_packs dan KEYIN qo'llanadi)
# kalit — savolning hozirgi matni; qiymat — almashtiriladigan maydonlar
# ---------------------------------------------------------------------------
FIXES: dict[str, dict] = {
    # kontekstsiz (oldingi savolga bog'liq) savollar
    "Mashinada ipning taranglik kuchi?": {"question": "Chizmadagi Atvud mashinasida (m₁ = 1 kg, m₂ = 3 kg, g = 10 m/s², ishqalanishsiz) ipning taranglik kuchi?"},
    "Holda ip tarangligi?": {"question": "Chizmadagi tizimda stol ustidagi m₁ = 2 kg jism (ishqalanishsiz) ip orqali osilgan m₂ = 3 kg yuk bilan bog'langan (g = 10 m/s²). Ipning taranglik kuchi?"},
    "Funksiyaning davri?": {"question": "Chizmadagi y = 2cos 2x funksiyaning eng kichik musbat davri?"},
    "Kubning to'la sirti?": {"question": "Chizmadagi kubning (qirrasi a = 4) to'la sirti?"},
    "Diagrammada |B|?": {"question": "Chizmadagi Venn diagrammasi bo'yicha B to'plam elementlari soni (|B|)?"},
    "Diagrammada A ∪ B elementlari soni?": {"question": "Chizmadagi Venn diagrammasi bo'yicha A ∪ B to'plam elementlari soni?"},
    "A ∩ B elementlari soni?": {"question": "Chizmadagi Venn diagrammasi bo'yicha A ∩ B to'plam elementlari soni?"},
    "To'g'ri to'rtburchakning diagonali?": {"question": "Chizmadagi to'g'ri to'rtburchakning diagonali?"},
    "Chiziq x = 4 da y qiymati?": {"question": "Chizmadagi to'g'ri chiziq x = 4 da qanday y qiymatni oladi?"},
    "Parabolaning uchi (V) koordinatalari?": {"question": "Chizmadagi parabola uchining (V) koordinatalari?"},
    "Ma'lumotlarning o'rtacha qiymati?": {"question": "Diagrammadagi ma'lumotlarning o'rtacha qiymati?"},
    "Uchburchak yuzi?": {"question": "Chizmadagi uchburchakning yuzi?"},
    "Zanjirga 14 V berilsa, umumiy tok?": {"question": "Chizmadagi zanjirga 14 V kuchlanish berilsa, umumiy tok qancha bo'ladi?"},
    "Pozitron...": {"question": "Pozitron qanday zarra?"},
    "Mezonlar...": {"question": "Mezonlar qanday tuzilgan?"},
    "Омонимы:": {"question": "Укажите пару омонимов."},
    "Паронимы:": {"question": "Укажите пару паронимов."},
    # biologiya — g'alati / noaniq ifodalar
    "Doimiy ravishda 1 juft nukleotid o'rnini bosuvchi mutatsiya qanday ataladi?": {"question": "Bitta nukleotid juftining almashinishi bilan bog'liq mutatsiya qanday ataladi?"},
    # ona tili va adabiyot — noto'g'ri javoblar
    "«Kitobxon» so'zida o'zak nima?": {"options": ["faqat kitob", "kitob va xon", "ki", "faqat xon"], "correct_index": 0,
                                         "explanation": "Kitobxon = kitob (o'zak) + -xon (ot yasovchi qo'shimcha)."},
    "«Shahar tinch uxladi» gapida qaysi ma'no ko'chishi bor?": {"options": ["Metonimiya", "Sinekdoxa", "Metafora", "Vazifadoshlik"], "correct_index": 0,
                                                              "explanation": "Shahar orqali uning aholisi nazarda tutilgan — bog'liqlik asosidagi ko'chish, metonimiya («Auditoriya kuldi» kabi)."},
    "«Go'ro'g'li» turkumiga kiruvchi doston?": {"options": ["Layli va Majnun", "Xamsa", "Alpomish", "Avazxon"], "correct_index": 3,
                                                "explanation": "«Avazxon» — Go'ro'g'li turkumidagi doston."},
    "«Kecha va kunduz» romanidagi Miryoqub qaysi qizning eri (ismini yozing)?": {
        "question": "«Kecha va kunduz» romanida Zebini xotinlikka olgan mingboshining ismini yozing.",
        "options": ["akbarali", "akbarali mingboshi"], "correct_index": 0,
        "explanation": "Zebi Akbarali mingboshiga majburan xotin qilib beriladi."},
    "Said Ahmadning urush mavzusidagi asari?": {"question": "Said Ahmadning «Ufq» trilogiyasining birinchi kitobi qaysi?",
                                                "explanation": "Trilogiya: «Qirq besh kun», «Hijron kunlari», «Ufq bo'sag'asida»."},
    "«Qirq besh kun» qaysi urush haqida? (bir so'z yoki ibora: ikkinchi jahon urushi — «jahon»)": {
        "question": "Said Ahmadning «Qirq besh kun» kitobida qaysi kanal qurilishi tasvirlangan? (Katta … kanali)",
        "options": ["farg'ona", "katta farg'ona", "katta farg'ona kanali", "fargona"], "correct_index": 0,
        "explanation": "1939-yilda 45 kunda qazilgan Katta Farg'ona kanali."},
    "«Bu dunyoda o'lib bo'lmaydi» romanining bosh qahramoni?": {
        "question": "Tog'ay Murodning «Bu dunyoda o'lib bo'lmaydi» romani qaysi yili nashr etilgan?",
        "options": ["1976", "1993", "2001", "1985"], "correct_index": 2,
        "explanation": "Roman 2001-yilda nashr etilgan; «Otamdan qolgan dalalar» — 1993-yilda."},
    # tarix — shubhali sanalar o'rniga aniq faktlar
    "Fitratning «Munozara» asari qaysi yilda?": {"question": "Fitratning «Munozara» asari ilk bor qaysi yili (Istanbulda) nashr etilgan?",
                                                  "options": ["1917", "1906", "1924", "1909"], "correct_index": 3,
                                                  "explanation": "«Munozara» 1909-yilda Istanbulda fors tilida chop etilgan, ruscha tarjimasi 1911-yilda chiqqan."},
    "«Yosh buxoroliklar» partiyasi qachon tuzilgan?": {"question": "«Yosh buxoroliklar» harakati qachon shakllangan?",
                                                       "options": ["XIX asr o'rtasida", "XX asr boshida", "XVIII asr oxirida", "XX asr o'rtasida"], "correct_index": 1,
                                                       "explanation": "Harakat XX asr boshida (1910-yillar) shakllangan."},
    "«Turon» partiyasi qachon?": {"question": "Toshkentdagi «Turon» jamiyati va teatr truppasini tashkil etgan jadid?",
                                  "options": ["Abdulla Avloniy", "Fitrat", "Cho'lpon", "Behbudiy"], "correct_index": 0,
                                  "explanation": "«Turon» jamiyati va teatr truppasi Abdulla Avloniy tashabbusi bilan tuzilgan."},
    "Arabshohiylar sulolasi qachongacha hukmronlik qilgan?": {"question": "Xiva xonligida Arabshohiylardan keyin hokimiyatga kelgan sulola?",
                                                              "options": ["Mang'itlar", "Qo'ng'irotlar", "Minglar", "Ashtarxoniylar"], "correct_index": 1,
                                                              "explanation": "Xivada Arabshohiylardan keyin Qo'ng'irotlar sulolasi hukmronlik qilgan."},
    "Rossiyada Birinchi jahon urushiga sabab bo'lgan blok?": {"question": "Birinchi jahon urushida Rossiya qaysi harbiy blok tarkibida bo'lgan?"},
}

# keng tarqalgan imlo xatolari (savol, variant va izohlarda)
TYPOS = [
    (re.compile(r"\byechinmlari\b"), "yechimlari"),
    (re.compile(r"\btengligsizlik\b"), "tengsizlik"),
    (re.compile(r"\bchuvalanglarning\b"), "chuvalchanglarning"),
    (re.compile(r"x qoshidagi bo'sh kat koeffitsienti"), "x oldidagi koeffitsient"),
    (re.compile(r"\bShaxarcha \(Shereshevskiy–Terner\) sindromida"), "Shereshevskiy–Terner sindromida"),
    (re.compile(r"(?<=\d) , (?=\d)"), ", "),
]


def _fix_text(s: str) -> str:
    for rx, rep in TYPOS:
        s = rx.sub(rep, s)
    return s


def fix(packs: list) -> int:
    """FIXES va TYPOS ni qo'llaydi. Matn o'zgargan savol bazada yangi savol sifatida yoziladi,
    eskisi esa (tayyor bank qatori bo'lsa) avtomatik nofaol qilinadi."""
    n = 0
    for pack in packs:
        seen = {q["question"].strip().lower() for q in pack["questions"]}
        for q in pack["questions"]:
            new = dict(FIXES.get(q["question"], {}))
            text = _fix_text(new.get("question", q["question"]))
            if text != q["question"]:
                if text.strip().lower() in seen:  # bunday savol allaqachon bor — takror qilmaymiz
                    new.pop("question", None)
                    text = q["question"]
                new["question"] = text
            for k, v in new.items():
                if q.get(k) != v:
                    q[k] = v
                    n += 1
            if q.get("explanation"):
                q["explanation"] = _fix_text(q["explanation"])
            if q.get("options"):
                q["options"] = [_fix_text(str(o)) for o in q["options"]]
            seen.add(q["question"].strip().lower())
    return n


def extend(packs: list) -> int:
    from .gen_v242 import _add
    from . import gen_v247b, gen_v247c
    banks = {
        "math": MATH, "physics": PHYS, "chemistry": CHEM, "english": ENG, "russian": RUS,
        "biology": gen_v247b.BIO, "native": gen_v247b.NATIVE, "history": gen_v247c.HIST,
    }
    added = 0
    for pack in packs:
        bank = banks.get(pack.get("subject"))
        if bank:
            added += _add(pack, bank)
    return added
