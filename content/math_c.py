"""Matematika: qo'shimcha mavzular (8–11-sinf): masalalar, planimetriya, stereometriya, tahlil, ehtimollik."""
from ._dsl import C, O, M
from ._ph import N, ON

Q = {}

Q["M8.9"] = [
    C(1, "2³ · 2⁴ ni darajali ko'rinishda yozing.", "2⁷", ["2¹²", "4⁷", "2¹"], "Asoslar teng: darajalar qo'shiladi."),
    N(1, "5⁰ ning qiymatini toping.", 1, [0, 5, 10], "", "Noldan farqli sonning nol darajasi 1 ga teng."),
    C(2, "(3²)³ ni soddalashtiring.", "3⁶", ["3⁵", "3⁸", "9⁵"], "Daraja darajaga: ko'rsatkichlar ko'paytiriladi."),
    N(2, "2⁻³ ning qiymatini toping.", 0.125, [-8, 8, 0.25], "", "2⁻³ = 1/8 = 0,125."),
    C(2, "a⁷ : a² ni soddalashtiring.", "a⁵", ["a⁹", "a¹⁴", "a³·⁵"], "Bo'lishda ko'rsatkichlar ayiriladi."),
    N(3, "2⁵ + 2⁵ ning qiymatini toping.", 64, [32, 10, 128], "", "32 + 32 = 64."),
    ON(3, "(−2)⁴ − 2⁴ ni hisoblang.", 0, "16 − 16 = 0."),
    ON(3, "3ˣ = 81 tenglamada x ni toping.", 4, "81 = 3⁴."),
]

Q["M8.10"] = [
    N(1, "200 ning 15 foizini toping.", 30, [3, 15, 300], "", "200·0,15 = 30."),
    N(1, "50 ning 10 foizini toping.", 5, [10, 0.5, 15], "", "50·0,1 = 5."),
    N(2, "Narx 20% ga oshib 120 so'm bo'ldi. Dastlabki narx necha so'm?", 100, [96, 144, 140], "", "x·1,2 = 120 → x = 100."),
    N(2, "Narx 25% ga arzonlashib 300 so'm bo'ldi. Dastlabki narx necha so'm?", 400, [375, 225, 325], "", "x·0,75 = 300 → x = 400."),
    N(2, "40 soni 160 ning necha foizi?", 25, [4, 40, 400], "", "40/160 = 0,25."),
    C(3, "Narx avval 20% ga oshirildi, so'ng 20% ga kamaytirildi. Dastlabki narxga nisbatan natija?", "4% ga kamaygan", ["O'zgarmagan", "4% ga oshgan", "10% ga kamaygan"], "1,2·0,8 = 0,96."),
    ON(3, "1000 so'm omonat yiliga 10% murakkab foiz bilan 2 yilda necha so'm bo'ladi?", 1210, "1000·1,1² = 1210."),
]

Q["M8.11"] = [
    N(1, "Avtomobil 60 km/soat tezlik bilan 3 soat yursa, yo'l necha km?", 180, [20, 63, 120], "", "S = v·t = 180."),
    N(2, "Velosipedchi 15 km/soat tezlik bilan 120 km yo'lni necha soatda bosib o'tadi?", 8, [7, 9, 105], "", "t = 120/15 = 8."),
    N(2, "Ikki poyezd bir-biriga qarab 60 va 40 km/soat tezlikda yuradi. Oraliq 300 km. Necha soatda uchrashadi?", 3, [5, 7.5, 2], "", "300/(60+40) = 3."),
    N(2, "Qayiqning turg'un suvdagi tezligi 15 km/soat, oqim tezligi 3 km/soat. Oqim bo'ylab tezligi?", 18, [12, 45, 5], "km/soat", "15 + 3 = 18."),
    N(3, "Qayiq oqim bo'ylab 36 km ni 2 soatda bosib o'tdi. Oqim tezligi 3 km/soat. Qaytishda (oqimga qarshi) necha soat ketadi?", 3, [2, 4, 2.5], "", "Oqim bo'ylab 18 km/s, o'zining tezligi 15; oqimga qarshi 12 km/s; 36/12 = 3."),
    ON(3, "Avval 60 km/soat tezlik bilan 1 soat, so'ng 40 km/soat tezlik bilan 1 soat yurildi. O'rtacha tezlik (km/soat)?", 50, "(60 + 40)/2 = 50."),
]

Q["M8.12"] = [
    C(1, "Bir ishchi ishni 6 kunda, ikkinchisi 3 kunda bajaradi. Birgalikda necha kunda bajaradi?", "2", ["9", "4,5", "3"], "1/6 + 1/3 = 1/2 → 2 kun."),
    N(2, "A ishni 10 kunda, B 15 kunda bajaradi. Birgalikda necha kunda?", 6, [25, 12, 5], "", "1/10 + 1/15 = 1/6."),
    N(2, "Basseyn 1-quvur bilan 4 soatda, 2-quvur bilan 12 soatda to'ladi. Ikkalasi birga necha soatda to'ldiradi?", 3, [8, 6, 4], "", "1/4 + 1/12 = 1/3."),
    N(2, "Ishchi soatiga 5 ta detal tayyorlaydi. 40 ta detalni necha soatda tayyorlaydi?", 8, [5, 35, 200], "", "40/5 = 8."),
    N(3, "A va B birgalikda ishni 8 kunda, A yolg'iz 12 kunda bajaradi. B yolg'iz necha kunda bajaradi?", 24, [4, 20, 10], "", "1/8 − 1/12 = 1/24."),
    ON(3, "Ikki ishchi birga ishni 6 kunda, birinchisi yolg'iz 10 kunda bajaradi. Ikkinchisi yolg'iz necha kunda bajaradi?", 15, "1/6 − 1/10 = 1/15."),
]

Q["M8.13"] = [
    N(1, "200 g eritmada tuz 10 foiz. Tuz massasi necha gramm?", 20, [10, 2, 180], "g", "200·0,1 = 20."),
    N(1, "Qotishmada 3 qism mis va 2 qism rux bor. 50 g qotishmada mis necha gramm?", 30, [20, 15, 25], "g", "50·3/5 = 30."),
    N(2, "20% li 300 g eritmaga 100 g suv qo'shildi. Yangi konsentratsiya necha foiz?", 15, [20, 10, 25], "%", "Tuz 60 g; 60/400 = 15%."),
    N(2, "40% li 100 g eritmaga 100 g suv qo'shildi. Konsentratsiya necha foiz?", 20, [10, 40, 25], "%", "Tuz 40 g; 40/200 = 20%."),
    C(3, "10% li 200 g va 30% li 300 g eritmalar aralashtirildi. Hosil bo'lgan eritma konsentratsiyasi?", "22%", ["20%", "25%", "18%"], "(20 + 90)/500 = 22%."),
    N(3, "10% li 200 g eritmadan necha gramm suv bug'latilsa, u 20% li bo'ladi?", 100, [50, 20, 180], "g", "Tuz 20 g; 20/m = 0,2 → m = 100; bug'latildi 100 g."),
    ON(3, "5% li 400 g eritmada necha gramm suv bor?", 380, "Tuz 20 g; suv 380 g."),
]

Q["M8.14"] = [
    C(1, "x + y = 5 va x − y = 1 tizimning yechimi (x; y)?", "(3; 2)", ["(2; 3)", "(4; 1)", "(1; 4)"], "Qo'shsak 2x = 6."),
    C(2, "2x + y = 7 va x − y = 2 tizimning yechimi?", "(3; 1)", ["(2; 3)", "(4; −1)", "(1; 5)"], "Qo'shsak 3x = 9, x = 3, y = 1."),
    N(2, "x + y = 10 va x − y = 4 bo'lsa, x·y nechaga teng?", 21, [24, 40, 28], "", "x = 7, y = 3."),
    ON(2, "3x + 2y = 12 va y = 3 bo'lsa, x ni toping.", 2, "3x = 6."),
    N(3, "x + 2y = 8 va 3x − y = 3 bo'lsa, x + y nechaga teng?", 5, [4, 6, 3], "", "y = 3x − 3; 7x = 14, x = 2, y = 3."),
    O(3, "x + y = 2 va 2x + 2y = 4 tizim nechta yechimga ega? (bir-ikki so'z)", ["cheksiz", "cheksiz ko'p", "cheksiz ko'p yechim"], "Tenglamalar teng kuchli — cheksiz ko'p."),
]

Q["M8.15"] = [
    N(1, "|−7| ning qiymati?", 7, [-7, 0, 14], "", "Modul manfiy bo'lmaydi."),
    C(1, "|x| = 3 tenglamaning yechimi?", "x = 3 yoki x = −3", ["x = 3", "x = −3", "yechimi yo'q"], "Ikki ildiz."),
    C(2, "|x − 2| = 5 tenglamaning yechimi?", "x = 7 yoki x = −3", ["x = 7", "x = 3 yoki x = −7", "x = 5"], "x − 2 = ±5."),
    C(2, "|x| < 2 tengsizlikning yechimi?", "−2 < x < 2", ["x < −2 yoki x > 2", "x < 2", "x > −2"], "Modul ichi (−2; 2) oraliqda."),
    N(2, "|x| = 4 tenglama ildizlari yig'indisi?", 0, [4, 8, -4], "", "4 + (−4) = 0."),
    C(3, "|2x − 1| = 3 tenglamaning yechimi?", "x = 2 yoki x = −1", ["x = 2", "x = −2 yoki x = 1", "x = 1 yoki x = 2"], "2x − 1 = ±3."),
    ON(3, "x = 2 da |x − 1| + |x − 3| ifodaning qiymatini toping.", 2, "1 + 1 = 2."),
]

Q["M8.16"] = [
    C(1, "x² − 9 ni ko'paytuvchilarga ajrating.", "(x − 3)(x + 3)", ["(x − 3)²", "(x + 3)²", "(x − 9)(x + 1)"], "Kvadratlar ayirmasi."),
    C(1, "a² + 2ab + b² ni ko'paytuvchilarga ajrating.", "(a + b)²", ["(a − b)²", "(a + b)(a − b)", "a² + b²"], "To'liq kvadrat."),
    C(2, "x² − 5x + 6 ni ko'paytuvchilarga ajrating.", "(x − 2)(x − 3)", ["(x + 2)(x + 3)", "(x − 1)(x − 6)", "(x + 1)(x − 6)"], "Ildizlari 2 va 3."),
    C(2, "2x² − 8 ni ko'paytuvchilarga ajrating.", "2(x − 2)(x + 2)", ["2(x − 4)²", "(2x − 4)(x + 4)", "2(x² − 8)"], "2(x² − 4)."),
    C(2, "x³ − x ni ko'paytuvchilarga ajrating.", "x(x − 1)(x + 1)", ["x(x − 1)²", "(x − 1)(x² + 1)", "x²(x − 1)"], "x(x² − 1)."),
    C(3, "a³ + b³ ni ko'paytuvchilarga ajrating.", "(a + b)(a² − ab + b²)", ["(a + b)(a² + ab + b²)", "(a + b)³", "(a − b)(a² + ab + b²)"], "Kublar yig'indisi."),
    ON(3, "x = 7, y = 3 da x² − y² ning qiymatini toping.", 40, "(7 − 3)(7 + 3) = 40."),
]

Q["M8.17"] = [
    N(1, "Uchburchak ichki burchaklarining yig'indisi necha gradus?", 180, [90, 360, 270], "°", "Teorema."),
    N(1, "Tomonlari 3, 4, 5 bo'lgan uchburchak perimetri?", 12, [60, 7, 15], "", "3 + 4 + 5 = 12."),
    N(2, "Uchburchakning ikki burchagi 40° va 60°. Uchinchi burchagi necha gradus?", 80, [100, 70, 90], "°", "180 − 100 = 80."),
    C(2, "Teng yonli uchburchakda asosidagi burchaklar qanday?", "Teng", ["Har xil", "To'g'ri burchak", "O'tmas burchak"], "Teng yonli uchburchak xossasi."),
    C(2, "Tomonlari 3, 4 va 8 bo'lgan uchburchak mavjudmi?", "Yo'q, 3 + 4 < 8", ["Ha", "Faqat to'g'ri burchakli", "Faqat teng yonli"], "Uchburchak tengsizligi."),
    N(3, "Uchburchakning tashqi burchagi 110°, unga qo'shni bo'lmagan ichki burchaklardan biri 40°. Ikkinchisi?", 70, [60, 80, 30], "°", "Tashqi burchak qo'shni bo'lmagan ikki ichki burchak yig'indisiga teng: 110 − 40 = 70."),
    O(3, "Uchburchak medianalari kesishish nuqtasida uchidan boshlab qanday nisbatda bo'linadi? (masalan 3:1 ko'rinishda)", ["2:1", "2 : 1", "2 ga 1"], "Medianalar uchidan 2:1 nisbatda bo'linadi."),
]

Q["M8.18"] = [
    N(1, "Tomonlari 5 va 8 bo'lgan to'g'ri to'rtburchak yuzi?", 40, [13, 26, 80], "", "5·8."),
    N(1, "Tomoni 7 bo'lgan kvadrat yuzi?", 49, [14, 28, 7], "", "7²."),
    N(2, "Parallelogramm asosi 10, balandligi 6. Yuzi?", 60, [30, 16, 120], "", "S = a·h."),
    N(2, "Trapetsiya asoslari 6 va 10, balandligi 4. Yuzi?", 32, [64, 24, 40], "", "(6 + 10)/2·4."),
    N(2, "Romb diagonallari 6 va 8. Yuzi?", 24, [48, 14, 28], "", "S = d₁d₂/2."),
    N(3, "Kvadrat diagonali 8. Yuzi?", 32, [64, 16, 8], "", "S = d²/2 = 32."),
    ON(3, "To'g'ri to'rtburchak perimetri 30, bir tomoni 9. Yuzini toping.", 54, "Ikkinchi tomon 6; 9·6 = 54."),
]

Q["M8.19"] = [
    C(1, "Radiusi 5 bo'lgan aylana uzunligi?", "10π", ["5π", "25π", "20π"], "C = 2πr."),
    C(1, "Radiusi 3 bo'lgan doira yuzi?", "9π", ["6π", "3π", "18π"], "S = πr²."),
    C(2, "Diametri 12 bo'lgan doira yuzi?", "36π", ["144π", "12π", "72π"], "r = 6; S = 36π."),
    N(2, "Aylana uzunligi 16π bo'lsa, radiusi?", 8, [16, 4, 32], "", "2πr = 16π."),
    N(2, "Doira yuzi 49π bo'lsa, diametri?", 14, [7, 49, 28], "", "r = 7, d = 14."),
    N(3, "Doira radiusi 2 marta orttirilsa, yuzi necha marta ortadi?", 4, [2, 8, 16], "", "S ~ r²."),
    O(3, "Radiusi 6 bo'lgan aylananing 60° li yoyi uzunligini yozing (π bilan).", ["2π", "2pi", "2 π"], "l = 2π·6·60/360 = 2π."),
]

Q["M8.20"] = [
    N(1, "Katetlari 3 va 4 bo'lgan to'g'ri burchakli uchburchak gipotenuzasi?", 5, [7, 12, 3.5], "", "√(9 + 16)."),
    N(2, "Gipotenuza 17, bir katet 8. Ikkinchi katet?", 15, [9, 25, 12], "", "√(289 − 64) = 15."),
    C(2, "Tomonlari 6, 8, 10 bo'lgan uchburchak to'g'ri burchaklimi?", "Ha", ["Yo'q", "Faqat teng yonli", "Aniqlab bo'lmaydi"], "36 + 64 = 100."),
    N(2, "Tomonlari 3, 4, 5 uchburchakka o'xshash uchburchakning kichik tomoni 6. Katta tomoni?", 10, [8, 12, 7.5], "", "k = 2."),
    N(3, "O'xshashlik koeffitsienti 2 bo'lsa, yuzlar nisbati?", 4, [2, 8, 6], "", "Yuzlar nisbati k²."),
    O(3, "Tomoni 2 bo'lgan muntazam uchburchak balandligi? (radikal bilan yozing)", ["√3", "sqrt(3)", "sqrt3", "1,73", "1.73"], "h = a√3/2 = √3."),
]

Q["M9.7"] = [
    N(1, "x² − 5x + 6 = 0 tenglama ildizlari yig'indisi?", 5, [6, -5, 1], "", "Vyet: x₁ + x₂ = 5."),
    N(1, "x² − 5x + 6 = 0 tenglama ildizlari ko'paytmasi?", 6, [5, -6, 1], "", "x₁·x₂ = 6."),
    C(2, "x² + px + q = 0 tenglama ildizlari yig'indisi nimaga teng?", "−p", ["p", "q", "−q"], "Vyet teoremasi."),
    N(2, "x² − 7x + 10 = 0 ildizlari kvadratlari yig'indisi?", 29, [49, 39, 20], "", "49 − 2·10 = 29."),
    N(2, "2x² − 6x + 4 = 0 ildizlari ko'paytmasi?", 2, [3, 4, -2], "", "c/a = 2."),
    C(3, "Ildizlari 2 va 3 bo'lgan keltirilgan kvadrat tenglama?", "x² − 5x + 6 = 0", ["x² + 5x + 6 = 0", "x² − 6x + 5 = 0", "x² − x − 6 = 0"], "x² − (x₁ + x₂)x + x₁x₂."),
    ON(3, "x² − 3x − 4 = 0 ildizlari ayirmasining moduli?", 5, "Ildizlar 4 va −1; |4 − (−1)| = 5."),
]

Q["M9.8"] = [
    C(1, "√x = 3 tenglamaning yechimi?", "9", ["3", "6", "√3"], "Kvadratga ko'tarsak x = 9."),
    N(2, "√(x + 1) = 4 tenglamada x ni toping.", 15, [16, 17, 3], "", "x + 1 = 16."),
    N(2, "√(2x − 1) = 3 tenglamada x ni toping.", 5, [4, 2, 10], "", "2x − 1 = 9."),
    N(2, "√(x + 7) = x − 5 tenglamaning ildizi?", 9, [2, 5, 7], "", "x² − 11x + 18 = 0; x = 2 yoki 9; x ≥ 5 → 9."),
    N(3, "√x + √(x + 7) = 7 tenglamaning ildizi?", 9, [4, 16, 7], "", "x = 9: 3 + 4 = 7."),
    ON(3, "√(3x + 4) = x tenglamaning ildizini toping.", 4, "x² − 3x − 4 = 0; x = 4 yoki −1; x ≥ 0 → 4."),
]

Q["M9.9"] = [
    C(1, "(x − 1)(x − 3) < 0 tengsizlik yechimi?", "1 < x < 3", ["x < 1 yoki x > 3", "x < 3", "x > 1"], "Ildizlar orasida manfiy."),
    C(2, "(x + 2)(x − 5) > 0 tengsizlik yechimi?", "x < −2 yoki x > 5", ["−2 < x < 5", "x > 5", "x < −2"], "Ildizlar tashqarisida musbat."),
    C(2, "x² − 4 ≤ 0 tengsizlik yechimi?", "−2 ≤ x ≤ 2", ["x ≤ −2 yoki x ≥ 2", "x ≤ 2", "−4 ≤ x ≤ 4"], "x² ≤ 4."),
    C(2, "(x − 1)/(x + 2) > 0 tengsizlik yechimi?", "x < −2 yoki x > 1", ["−2 < x < 1", "x > 1", "x < 1"], "Intervallar usuli."),
    N(3, "x² − x − 6 < 0 tengsizlikni qanoatlantiruvchi butun sonlar nechta?", 4, [3, 5, 2], "", "−2 < x < 3: −1, 0, 1, 2."),
    ON(3, "(x − 1)(x − 2)(x − 3) < 0 ni qanoatlantiruvchi eng katta butun sonni toping.", 0, "Yechim: x < 1 yoki 2 < x < 3; eng katta butun son 0."),
]

Q["M9.10"] = [
    C(1, "f(x) = x² funksiya qanday?", "Juft", ["Toq", "Davriy", "Juft ham, toq ham emas"], "f(−x) = f(x)."),
    C(1, "y = 1/x funksiyaning aniqlanish sohasi?", "x ≠ 0", ["x > 0", "x ≥ 0", "barcha haqiqiy sonlar"], "Maxraj nolga teng bo'lmaydi."),
    C(2, "y = √(x − 3) funksiyaning aniqlanish sohasi?", "x ≥ 3", ["x > 3", "x ≤ 3", "x ≠ 3"], "Ildiz ostidagi ifoda manfiy bo'lmaydi."),
    C(2, "y = x³ funksiya qanday?", "Toq", ["Juft", "Davriy", "Chegaralangan"], "f(−x) = −f(x)."),
    N(2, "f(x) = x² − 4x funksiyaning eng kichik qiymati?", -4, [0, -2, 4], "", "Uchi: x = 2; f(2) = −4."),
    C(3, "y = √(4 − x²) funksiyaning qiymatlar to'plami?", "[0; 2]", ["[−2; 2]", "[0; 4]", "(−∞; 2]"], "0 ≤ √(4 − x²) ≤ 2."),
    ON(3, "f(x) = 3x − 2 uchun f⁻¹(7) ni toping.", 3, "3x − 2 = 7 → x = 3."),
]

Q["M9.11"] = [
    N(1, "aₙ = 2n + 1 ketma-ketlikning 5-hadi?", 11, [9, 10, 13], "", "2·5 + 1."),
    C(2, "aₙ = n² ketma-ketlikning 3-hadi?", "9", ["6", "8", "27"], "3² = 9."),
    N(2, "a₁ = 3, aₙ₊₁ = aₙ + 4 bo'lsa, a₄ nechaga teng?", 15, [12, 19, 16], "", "3, 7, 11, 15."),
    N(2, "1 + 2 + … + 10 yig'indini toping.", 55, [50, 45, 100], "", "10·11/2."),
    N(2, "1 + 3 + 5 + … + 19 (10 ta had) yig'indisi?", 100, [90, 110, 190], "", "Toq sonlar yig'indisi n² = 100."),
    N(3, "2 + 4 + 6 + … + 100 yig'indini toping.", 2550, [2500, 5050, 5100], "", "2(1 + … + 50) = 2·1275."),
    ON(3, "1² + 2² + 3² + 4² ni hisoblang.", 30, "1 + 4 + 9 + 16 = 30."),
]

Q["M9.12"] = [
    C(2, "x² − 2x + a = 0 tenglama ildizga ega bo'lmasligi uchun a qanday bo'lishi kerak?", "a > 1", ["a < 1", "a = 1", "a ≤ 1"], "D = 4 − 4a < 0."),
    C(2, "ax = 6 tenglama a = 0 da?", "Yechimi yo'q", ["x = 6", "x = 0", "Cheksiz ko'p yechim"], "0·x = 6 bajarilmaydi."),
    N(3, "x² − 6x + a = 0 tenglama yagona ildizga ega bo'lsa, a nechaga teng?", 9, [6, 3, 36], "", "D = 36 − 4a = 0."),
    C(3, "x² + ax + 4 = 0 tenglama yagona ildizga ega (a > 0). a = ?", "4", ["2", "8", "16"], "D = a² − 16 = 0."),
    C(3, "|x| = a tenglama yechimga ega bo'lmasligi uchun?", "a < 0", ["a = 0", "a > 0", "a ≥ 0"], "Modul manfiy bo'lmaydi."),
    ON(3, "x² + 4x + a = 0 tenglamaning ildizlaridan biri 1 bo'lsa, a ni toping.", -5, "1 + 4 + a = 0."),
]

Q["M10.7"] = [
    C(1, "Asosiy trigonometrik ayniyat qaysi?", "sin²x + cos²x = 1", ["sin x + cos x = 1", "sin²x − cos²x = 1", "tg x + ctg x = 1"], "Asosiy ayniyat."),
    N(1, "sin 30° ning qiymati?", 0.5, [1, 0.866, 0], "", "sin 30° = 1/2."),
    N(1, "cos 60° ning qiymati?", 0.5, [1, 0.866, 0], "", "cos 60° = 1/2."),
    N(2, "sin 150° ning qiymati?", 0.5, [-0.5, 0.866, -0.866], "", "sin(180° − 30°) = sin 30°."),
    N(2, "cos 120° ning qiymati?", -0.5, [0.5, -0.866, 0.866], "", "cos(180° − 60°) = −cos 60°."),
    C(2, "tg x ni sin x va cos x orqali ifodalang.", "sin x / cos x", ["cos x / sin x", "sin x · cos x", "1 / sin x"], "Ta'rif."),
    ON(3, "sin α = 3/5, α o'tkir burchak. cos α ni toping (o'nli kasr).", 0.8, "cos α = √(1 − 0,36) = 0,8."),
    ON(3, "tg α = 3/4, α o'tkir burchak. sin α ni toping (o'nli kasr).", 0.6, "Gipotenuza 5, sin α = 3/5."),
]

Q["M10.8"] = [
    C(2, "log₂x > 3 tengsizlik yechimi?", "x > 8", ["0 < x < 8", "x > 3", "x > 6"], "Asos 1 dan katta."),
    C(2, "log₃x < 2 tengsizlik yechimi?", "0 < x < 9", ["x < 9", "x > 9", "0 < x < 6"], "Aniqlanish sohasi x > 0."),
    C(2, "log₀,₅ x > 1 tengsizlik yechimi?", "0 < x < 0,5", ["x > 0,5", "x < 0,5", "x > 2"], "Asos 1 dan kichik: tengsizlik belgisi o'zgaradi."),
    C(3, "log₂(x − 1) ≥ 2 tengsizlik yechimi?", "x ≥ 5", ["x ≥ 3", "1 < x ≤ 5", "x ≥ 4"], "x − 1 ≥ 4."),
    ON(3, "log₂(x − 3) = 2 tenglamada x ni toping.", 7, "x − 3 = 4."),
    C(3, "lg x² = 2 tenglama yechimi?", "x = 10 yoki x = −10", ["x = 10", "x = 100", "x = 1"], "x² = 100, x ≠ 0."),
]

Q["M10.9"] = [
    N(1, "Qirrasi 3 bo'lgan kub hajmi?", 27, [9, 18, 81], "", "3³."),
    N(2, "To'g'ri prizma asosi yuzi 12, balandligi 5. Hajmi?", 60, [17, 30, 120], "", "V = S·h."),
    N(2, "Piramida asosi yuzi 15, balandligi 6. Hajmi?", 30, [90, 45, 15], "", "V = S·h/3."),
    N(2, "Qirrasi 2 bo'lgan kubning to'la sirti?", 24, [8, 12, 16], "", "6·4."),
    N(3, "Muntazam to'rtburchakli piramida asosining tomoni 6, balandligi 4. Hajmi?", 48, [144, 24, 96], "", "36·4/3."),
    O(3, "O'lchamlari 2, 3, 4 bo'lgan to'g'ri burchakli parallelepipedning fazoviy diagonalini yozing.", ["√29", "sqrt(29)", "sqrt29"], "d = √(4 + 9 + 16) = √29."),
]

Q["M10.10"] = [
    C(1, "Silindr hajmi formulasi?", "V = πr²h", ["V = 2πrh", "V = πr²h/3", "V = 4πr³/3"], "Asos yuzi × balandlik."),
    C(1, "Shar sirti formulasi?", "S = 4πr²", ["S = πr²", "S = 2πr²", "S = 4πr³/3"], "Shar sirti."),
    C(2, "Radiusi 3, balandligi 5 bo'lgan silindr hajmi?", "45π", ["15π", "30π", "75π"], "π·9·5."),
    N(2, "Konusning radiusi 3, balandligi 4. Yasovchisi?", 5, [7, 12, 3.5], "", "√(9 + 16)."),
    C(2, "Radiusi 3, balandligi 4 bo'lgan konus hajmi?", "12π", ["36π", "4π", "24π"], "V = πr²h/3 = 12π."),
    C(3, "Radiusi 3 bo'lgan shar hajmi?", "36π", ["12π", "108π", "27π"], "4π·27/3."),
    ON(3, "Shar hajmi 36π bo'lsa, uning radiusi nechaga teng?", 3, "4r³/3 = 36 → r³ = 27."),
]

Q["M10.11"] = [
    N(1, "Qavariq beshburchak ichki burchaklari yig'indisi?", 540, [360, 720, 180], "°", "(n − 2)·180."),
    N(2, "Muntazam oltiburchakning ichki burchagi?", 120, [60, 135, 108], "°", "720/6."),
    C(2, "Muntazam beshburchakning ichki burchagi?", "108°", ["120°", "72°", "90°"], "540/5."),
    N(2, "Muntazam sakkizburchakning diagonallari soni?", 20, [16, 28, 24], "", "n(n − 3)/2."),
    N(3, "Ichki burchaklari yig'indisi 1080° bo'lgan ko'pburchakning tomonlari soni?", 8, [6, 7, 9], "", "(n − 2)·180 = 1080."),
    ON(3, "Muntazam ko'pburchakning tashqi burchagi 36°. Tomonlari sonini toping.", 10, "360/36 = 10."),
]

Q["M11.8"] = [
    C(1, "(x²)′ nimaga teng?", "2x", ["x", "x²/2", "2"], "Hosila qoidasi."),
    N(2, "f(x) = x³ bo'lsa, f′(2) nechaga teng?", 12, [8, 6, 3], "", "3x² = 12."),
    C(2, "y = x² grafigiga x = 1 nuqtada o'tkazilgan urinmaning burchak koeffitsienti?", "2", ["1", "0", "3"], "f′(1) = 2."),
    N(2, "s = t² + 3t bo'lsa, t = 2 da tezlik?", 7, [4, 10, 6], "", "v = s′ = 2t + 3."),
    N(3, "f(x) = x² − 4x funksiyaning ekstremum nuqtasi?", 2, [4, -2, 0], "", "f′ = 2x − 4 = 0."),
    C(3, "y = x³ grafigiga x = 1 nuqtada o'tkazilgan urinma tenglamasi?", "y = 3x − 2", ["y = 3x + 2", "y = x", "y = 3x − 1"], "f(1) = 1, k = 3."),
    ON(3, "y = 3x² − 2x grafigiga x = 1 nuqtada o'tkazilgan urinmaning burchak koeffitsientini toping.", 4, "y′ = 6x − 2 = 4."),
]

Q["M11.9"] = [
    C(1, "∫2x dx ni toping.", "x² + C", ["2x² + C", "x + C", "2 + C"], "Boshlang'ich funksiya."),
    C(2, "∫cos x dx ni toping.", "sin x + C", ["−sin x + C", "cos x + C", "−cos x + C"], "(sin x)′ = cos x."),
    N(2, "∫₀² x dx ni hisoblang.", 2, [4, 1, 8], "", "x²/2 |₀² = 2."),
    N(2, "∫₁³ 2 dx ni hisoblang.", 4, [2, 6, 3], "", "2(3 − 1)."),
    N(3, "y = x², Ox o'qi va x = 0, x = 3 chiziqlar bilan chegaralangan shakl yuzi?", 9, [27, 3, 6], "", "x³/3 |₀³ = 9."),
    ON(3, "∫₀¹ 3x² dx ni hisoblang.", 1, "x³ |₀¹ = 1."),
]

Q["M11.10"] = [
    N(1, "Tanga tashlanganda gerb tushish ehtimoli?", 0.5, [1, 0.25, 0], "", "1/2."),
    N(2, "Zar tashlanganda juft son tushish ehtimoli?", 0.5, [0.25, 1/6, 0.75], "", "3/6."),
    C(2, "Ikki tanga tashlanganda ikkalasi ham gerb tushish ehtimoli?", "1/4", ["1/2", "1/3", "3/4"], "(1/2)·(1/2)."),
    N(2, "10 ta shardan 3 tasi qizil. Tasodifiy olingan sharning qizil bo'lish ehtimoli?", 0.3, [0.7, 0.03, 3], "", "3/10."),
    C(3, "Ikki zar tashlanganda ochkolar yig'indisi 7 bo'lish ehtimoli?", "1/6", ["1/12", "7/36", "1/7"], "6 ta qulay holat / 36."),
    O(3, "Tanga 3 marta tashlanganda aynan 2 marta gerb tushish ehtimoli? (kasr)", ["3/8", "0,375", "0.375"], "C(3,2)/2³ = 3/8."),
]

Q["M11.11"] = [
    N(1, "C(5, 2) ni hisoblang.", 10, [20, 5, 25], "", "5!/(2!·3!)."),
    N(2, "5! nechaga teng?", 120, [24, 60, 720], "", "5·4·3·2·1."),
    N(2, "A(5, 2) joylashtirmalar sonini toping.", 20, [10, 25, 60], "", "5·4."),
    N(3, "(a + b)⁴ yoyilmasidagi koeffitsientlar yig'indisi?", 16, [8, 4, 32], "", "a = b = 1: 2⁴."),
    N(3, "8 kishidan 3 kishilik guruhni necha usulda tanlash mumkin?", 56, [24, 336, 512], "", "C(8,3) = 56."),
    ON(3, "(1 + x)⁵ yoyilmasida x² oldidagi koeffitsientni toping.", 10, "C(5,2) = 10."),
]
