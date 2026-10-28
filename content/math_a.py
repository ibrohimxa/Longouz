"""Matematika: 8–9-sinf mavzulari va savol banki."""
from ._dsl import C, O, M
from ._ph import N, ON, fmt

Q = {}

# ─────────────────────────── 8-SINF ────────────────────────────

Q["M8.1"] = [  # Kvadrat ildiz va haqiqiy sonlar
    C(1, "√144 qanday qiymatga teng?", "12", ["72", "11", "14"], "12² = 144."),
    C(1, "√(4·25) ni soddalashtiring.", "10", ["20", "50", "√100"], "√100 = 10."),
    N(1, "√169 qiymatini toping.", 13, [11, 14, 26], "", "13² = 169."),
    C(2, "√12 ni soddalashtiring.", "2√3", ["3√2", "4√3", "√12"], "√(4·3) = 2√3."),
    C(2, "√18 + √8 ni hisoblang.", "5√2", ["√26", "3√2 + 2√2", "2√5"], "3√2 + 2√2 = 5√2."),
    N(2, "√(0,25) qiymatini toping.", 0.5, [0.05, 0.25, 5], "", "0,5² = 0,25."),
    C(2, "√75 − √27 ni hisoblang.", "2√3", ["√48", "5√3", "4√3"], "5√3 − 3√3 = 2√3."),
    C(3, "√(3) · √(27) qiymatini hisoblang.", "9", ["81", "3√3", "27"], "√81 = 9."),
    ON(3, "(√5 − √3)(√5 + √3) ni hisoblang.", 2, "5 − 3 = 2."),
    ON(3, "√(2 + √(2 + √4)) ni hisoblang.", 2, "√4 = 2; √(2+2) = 2; √(2+2) = 2."),
    O(3, "√(49/64) ni kasr sifatida yozing (kasr chizish bilan: a/b shaklida).", ["7/8"], "7/8."),
]

Q["M8.2"] = [  # Kvadrat tenglama
    C(1, "x² − 9 = 0 tenglamani yeching.", "x = ±3", ["x = 3", "x = −3", "x = ±9"], "x² = 9 → x = ±3."),
    N(1, "x² − 5x + 6 = 0 tenglamasining katta ildizi qancha?", 3, [2, 5, 6], "", "x = 2 va x = 3."),
    C(1, "x² + 4x + 4 = 0 tenglamani yeching.", "x = −2", ["x = ±2", "x = 2", "x = ±4"], "(x+2)² = 0."),
    N(2, "2x² − 7x + 3 = 0 tenglamasining kichik ildizi qancha?", 0.5, [3, -0.5, 1.5], "", "x = 3 va x = 1/2."),
    C(2, "x² + 6x + 9 = 0 tenglamasining diskriminanti qancha?", "0", ["36", "−36", "9"], "D = 36−36 = 0."),
    C(2, "x² − x − 12 = 0 tenglamasining ildizlari yig'indisi qancha?", "1", ["12", "−12", "−1"], "Viyet: x₁+x₂ = 1."),
    C(2, "x² + px + 12 = 0 ildizlari 3 va 4 bo'lsa, p qancha?", "−7", ["7", "12", "−12"], "p = −(3+4) = −7."),
    ON(3, "3x² − 12 = 0 tenglamaning musbat ildizi qancha?", 2, "x² = 4 → x = 2."),
    ON(3, "x² − 2x − 8 = 0 ildizlari ko'paytmasi qancha?", -8, "Viyet: x₁x₂ = c/a = −8."),
    O(3, "x² + 6x + 5 = 0 tenglamasining kichik ildizini yozing.", ["-5", "−5"], "x = −1 va x = −5."),
]

Q["M8.3"] = [  # Algebraik kasrlar
    C(1, "a/b · b/a = ?", "1", ["a²/b²", "0", "a/b"], "Kasrlar ko'paytmasi."),
    C(1, "(x+1)/(x+1) = ? (x ≠ −1)", "1", ["0", "x", "x+1"], "Kasrni qisqartirish."),
    C(2, "1/(x−1) + 1/(1−x) = ?", "0", ["2/(x−1)", "1/(x²−1)", "2"], "1/(x−1) − 1/(x−1) = 0."),
    C(2, "(a²−b²)/(a+b) ni soddalashtiring.", "a − b", ["a + b", "(a−b)²", "a²−b"], "(a+b)(a−b)/(a+b) = a−b."),
    C(2, "2/(x+3) + 3/(x+3) = ?", "5/(x+3)", ["5/2(x+3)", "6/(x+3)²", "5"], "Maxrajlar teng."),
    C(3, "(x²−4)/(x−2) · (x−2)/(x+2) ni soddalashtiring.", "x − 2", ["x + 2", "1", "(x−2)²"], "(x+2)(x−2)/(x−2) · (x−2)/(x+2) = x−2."),
    ON(3, "a/(a−1) − 1/(a−1) ifodasi (a ≠ 1) qisqartirilganda nimaga teng?", 1, "(a−1)/(a−1) = 1."),
    M(2, [("a/b · c/d", "ac/bd"), ("a/b ÷ c/d", "ad/bc"), ("a/b + a/b", "2a/b")], "Kasr arifmetikasi qoidalari."),
    O(3, "(x²−1)/(x+1) ifodasini soddalashtiring (x ≠ −1). Natija?", ["x-1", "x − 1"], "(x+1)(x−1)/(x+1) = x−1."),
]

Q["M8.4"] = [  # Nisbat, proporsiya va foiz
    C(1, "20 ning 25% i qancha?", "5", ["4", "10", "2,5"], "20·0,25 = 5."),
    C(1, "a:b = 2:3 va a = 10 bo'lsa, b = ?", "15", ["6", "12", "7"], "10/b = 2/3 → b = 15."),
    N(1, "50 sonining 40% i qancha?", 20, [25, 15, 10], "", "50·0,4."),
    N(2, "200 ning nechi foizi 50 ga teng?", 25, [20, 40, 15], "%", "50/200·100 = 25%."),
    C(2, "Narx 800 so'mdan 1000 so'mga oshdi. Foizda qancha oshdi?", "25%", ["20%", "200 so'm", "200"], "200/800·100 = 25%."),
    N(2, "a:b:c = 2:3:5 va ularning yig'indisi 100 bo'lsa, c qancha?", 50, [20, 30, 40], "", "5·10 = 50."),
    C(3, "Bank 12% yillik foiz to'laydi. 5000 so'm 1 yilda qancha bo'ladi?", "5600 so'm", ["5060 so'm", "5500 so'm", "6000 so'm"], "5000·1,12 = 5600."),
    ON(3, "540 sonining necha foizi 135?", 25, "135/540·100 = 25%."),
    O(3, "3:4 nisbatdagi ikki son yig'indisi 70. Katta sonni yozing.", ["40"], "4·10 = 40."),
]

Q["M8.5"] = [  # Chiziqli tengsizliklar va to'plamlar
    C(1, "x + 3 > 7. Yechim?", "x > 4", ["x > 10", "x < 4", "x = 4"], "x > 7 − 3 = 4."),
    C(1, "|x| < 5 ning yechimi qaysi?", "−5 < x < 5", ["x < 5", "x > −5", "x < −5 yoki x > 5"], "Modul tengsizligi."),
    C(2, "2x − 1 ≤ x + 3. Yechim?", "x ≤ 4", ["x ≤ 2", "x ≥ 4", "x < 4"], "x ≤ 4."),
    C(2, "−2x < 6. Yechim?", "x > −3", ["x < −3", "x > 3", "x < 3"], "Ikki tomonga −2 ga bo'lganda tengsizlik belgisi o'zgaradi."),
    C(2, "|2x − 3| ≤ 5 ning yechimi?", "−1 ≤ x ≤ 4", ["−5 ≤ x ≤ 5", "x ≤ 4", "x ≥ −1"], "−5 ≤ 2x−3 ≤ 5 → −1 ≤ x ≤ 4."),
    C(3, "1 < 3x − 2 < 7. Butun son yechinmlari soni qancha?", "2 ta", ["3 ta", "1 ta", "4 ta"], "1 < x < 3 → x = 2 (faqat 2 ta butun)."),
    ON(3, "x + 2 > 5 va x − 1 < 4 tengsizliklar tizimining yechimini to'plamga yozing: a < x < b shaklda, a+b ni toping.", 8, "3 < x < 5 → a+b = 8."),
    O(3, "2x + 1 > 9 tengsizlikning kichik butun son yechimini yozing.", ["5"], "2x > 8 → x > 4 → kichik butun 5."),
    M(2, [("|x| < a (a > 0)", "−a < x < a"), ("|x| > a (a > 0)", "x < −a yoki x > a"), ("|x| = a", "x = a yoki x = −a")], "Modul tengsizliklari yechimi."),
]

Q["M8.6"] = [  # Funksiyalar asoslari
    C(1, "y = 2x + 1 grafigi qaysi nuqtadan o'tadi?", "(0; 1)", ["(0; 2)", "(1; 0)", "(0; 0)"], "x = 0 → y = 1."),
    C(1, "y = x² funksiyasi x = −3 da qanday qiymat oladi?", "9", ["−9", "6", "−6"], "(−3)² = 9."),
    C(2, "y = kx + b to'g'ri chiziqda k < 0 bo'lsa grafik qanday?", "Chapdan o'nga pastga tushadi", ["Chapdan o'nga ko'tariladi", "Gorizontal", "Vertikal"], "Manfiy burchak koeffitsiyenti."),
    C(2, "y = x² parabola o'qi simmetriyasi qaysi?", "x = 0 (y o'qi)", ["y = 0", "y = x", "x = 1"], "Parabola simmetriya o'qi."),
    C(2, "y = 2x² − 4x + 3 funksiyasining eng kichik qiymati qancha?", "1", ["3", "−1", "2"], "Uch: x=1, y=2−4+3=1."),
    ON(3, "y = x² − 6x + 8 funksiyaning nollari (x o'qi bilan kesishish nuqtalari) necha: nechtasi bor?", 2, "x=2 va x=4."),
    ON(3, "y = x² + 4x + 4 funksiyaning eng kichik qiymati necha?", 0, "(x+2)² ≥ 0, min = 0."),
    O(3, "y = 2x − 4 grafikining x o'qi bilan kesishish nuqtasining x-koordinatasi.", ["2"], "0 = 2x−4 → x = 2."),
    M(2, [("y = kx + b (k > 0)", "Ko'tariluvchi to'g'ri chiziq"), ("y = ax² (a > 0)", "Tepasi pastga qaratilgan parabola"), ("y = a/x (a > 0)", "Giperbola, I va III chorakda")], "Grafik turlari."),
]

Q["M8.7"] = [  # Kvadrat ko'p hadlar
    C(1, "(x + 3)(x − 3) ning kengaytmasi?", "x² − 9", ["x² + 9", "x² − 6x + 9", "x² + 6x − 9"], "Ko'phadlar ko'paytmasi: a² − b²."),
    C(1, "(a + b)² ni kengaytiring.", "a² + 2ab + b²", ["a² + b²", "a² − 2ab + b²", "a² + 2ab − b²"], "Ikki hadning kvadrati formulasi."),
    N(2, "(x + 5)(x − 2) ko'paytmani oching. x qoshidagi bo'sh kat koeffitsienti qancha?", 3, [2, 5, -2], "", "(x+5)(x−2)=x²+3x−10 → koef=3."),
    C(2, "x² + 5x + 6 ni ko'paytuvchilarga ajrating.", "(x+2)(x+3)", ["(x+1)(x+6)", "(x+5)(x+1)", "(x−2)(x−3)"], "2+3=5, 2·3=6."),
    C(2, "4x² − 9 ni ko'paytuvchilarga ajrating.", "(2x−3)(2x+3)", ["(2x)²−9", "(x−3)(x+3)", "(4x−9)(x−1)"], "Farqlar kvadrati."),
    C(3, "x² − 7x + 12 ni ko'paytuvchilarga ajrating.", "(x−3)(x−4)", ["(x+3)(x+4)", "(x−3)(x+4)", "(x+3)(x−4)"], "−3·−4=12, −3+−4=−7."),
    ON(3, "(3a − 2b)² = 9a² + ? + 4b² — bo'sh joyga nima kiradi? (ab ko'rinishida yozing)", -12, "−12ab."),
    O(3, "x² + 7x + 10 ni (x+a)(x+b) shaklda yozing. a·b qancha?", ["10"], "2+5=7, 2·5=10."),
    M(2, [("a² − b²", "(a−b)(a+b)"), ("a² + 2ab + b²", "(a+b)²"), ("a² − 2ab + b²", "(a−b)²")], "Ayrim kasr formulalari."),
]

Q["M8.8"] = [  # Sonlar sistemalari va bo'linuvchanlik
    C(1, "24 ni 6 ga bo'lganda qoldiq qancha?", "0", ["2", "4", "3"], "24 = 4·6."),
    C(1, "Qaysi son 2 ga va 5 ga bo'linadi?", "30", ["25", "24", "21"], "30 = 2·3·5."),
    C(2, "EKB(12, 18) qancha?", "6", ["36", "2", "3"], "12 = 2²·3; 18 = 2·3²; EKB = 2·3 = 6."),
    C(2, "EKU(4, 6) qancha?", "12", ["2", "24", "8"], "4 = 2²; 6 = 2·3; EKU = 2²·3 = 12."),
    C(2, "a va b ning EKB·EKU = a·b ning ifodasi to'g'rimi?", "Ha, doim to'g'ri", ["Yo'q, faqat tub sonlar uchun", "Faqat ular teng bo'lganda", "Yo'q, hech qachon emas"], "Teorema."),
    N(2, "EKB(24, 36) qancha?", 12, [6, 4, 18], "", "24=2³·3; 36=2²·3²; EKB=2²·3=12."),
    ON(3, "EKU(8, 12) qancha?", 24, "8=2³; 12=2²·3; EKU=2³·3=24."),
    O(3, "Ikkita son EKB si 5, EKU si 60. Bir soni 15 bo'lsa, ikkinchisi qancha? (sonni yozing)", ["20"], "15·x = 5·60 → x = 20."),
    M(2, [("EKB", "Eng katta umumiy bo'luvchi"), ("EKU", "Eng kichik umumiy karrali"), ("Tub son", "Faqat 1 va o'ziga bo'linadigan son")], "Sonlar nazariyasi atamalar."),
]

# ─────────────────────────── 9-SINF ────────────────────────────

Q["M9.1"] = [  # Kvadrat funksiya va parametr
    C(1, "y = x² + 2x + 1 funksiyasining minimal qiymati qancha?", "0", ["1", "−1", "2"], "y = (x+1)² ≥ 0."),
    C(1, "y = −x² + 4 funksiyasining maksimal qiymati qancha?", "4", ["−4", "0", "2"], "x = 0 → y = 4."),
    N(2, "y = 2x² − 8x + 6 funksiyasining uchi x-koordinatasi qancha?", 2, [4, -2, 3], "", "x = −b/2a = 8/4 = 2."),
    C(2, "y = x² + bx + 9 funksiyaning grafigi x o'qiga tegilsa b ning qiymatlari?", "b = ±6", ["b = ±3", "b = ±9", "b = ±18"], "D = 0: b² − 36 = 0 → b = ±6."),
    C(3, "y = x² − 4x + m + 1 funksiya grafigi x o'qini kesmasligi uchun m qanday bo'lishi kerak?", "m > 3", ["m < 3", "m > −3", "m ≥ 3"], "D < 0: 16 − 4(m+1) < 0 → m > 3."),
    ON(3, "y = ax² + 4x + 1 funksiyaning grafigi x o'qiga tegilishi uchun a qancha? (a ≠ 0)", 4, "D = 0: 16 − 4a = 0 → a = 4."),
    O(3, "y = x² − 5x + 4 funksiyasining eng kichik qiymatini toping.", ["−2.25", "-9/4", "-2,25"], "x=2,5; y=6,25−12,5+4=−2,25."),
    M(2, [("D > 0", "Grafik x o'qini ikki nuqtada kesadi"), ("D = 0", "Grafik x o'qiga tegiladi"), ("D < 0", "Grafik x o'qini kesmaydimad")], "Diskriminant belgisi va grafik joylashuvi."),
]

Q["M9.2"] = [  # Tengsizliklar tizimi va ikkinchi darajali
    C(1, "x² < 9. Yechim?", "−3 < x < 3", ["x < 3", "x > −3", "x < −3 yoki x > 3"], "x² − 9 < 0 → (x−3)(x+3) < 0."),
    C(2, "x² − 5x + 6 > 0. Yechim?", "x < 2 yoki x > 3", ["2 < x < 3", "x > 6", "x < 5"], "Ildizlar 2 va 3; kvadrat koeffitsiyent musbat."),
    C(2, "(x−1)(x+3) ≤ 0. Yechim?", "−3 ≤ x ≤ 1", ["x ≤ −3 yoki x ≥ 1", "−1 ≤ x ≤ 3", "x ≤ 1"], "Parabola pastda − 3 ≤ x ≤ 1."),
    C(3, "x² − x − 6 < 0 va x > 0 tizimi. Yechim?", "0 < x < 3", ["−2 < x < 3", "0 < x < 4", "x > 0"], "x² − x − 6 < 0 → −2 < x < 3; kesma x > 0: 0 < x < 3."),
    ON(3, "x² ≥ 4 tengsizlikning yechimida butun son yechimlari: x = ±2, ±3, ±4, ... Kichik butun musbat son?", 2, "x ≤ −2 yoki x ≥ 2; kichik musbat butun x = 2."),
    O(3, "(x−2)(x−5) ≤ 0 tengsizlikning [a; b] yechim oralig'ida a + b qancha?", ["7"], "2 ≤ x ≤ 5; a+b = 7."),
    C(2, "x² − 4 > 0 tengsizlikning yechimi?", "x < −2 yoki x > 2", ["−2 < x < 2", "x > 2", "x > 4"], "Ildizlar ±2; a=1>0 → tashqarida."),
    ON(3, "(x+1)² > 0 tengligsizlik qachon bajarilmaydi? x ning bu qiymatini yozing.", -1, "(x+1)² = 0 → x = −1."),
]

Q["M9.3"] = [  # Progressiyalar
    C(1, "1, 3, 5, 7, ... — bu qanday progressiya?", "Arifmetik, d = 2", ["Geometrik", "Harmonik", "Arifmetik, d = 3"], "Har haddan keyingisi 2 ga ortadi."),
    N(1, "2, 6, 18, 54, ... geometrik progressiyaning nechidanji hadi — 486?", 5, [4, 6, 7], "", "a₅ = 2·3⁴ = 162. a₆ = 486."),
    N(2, "Arifmetik progressiyaning 1-hadi 3, farq 5. 10-had qancha?", 48, [45, 50, 53], "", "a₁₀ = 3 + 9·5 = 48."),
    C(2, "Geometrik progressiya: a₁ = 2, q = 3. n-had formulasi?", "aₙ = 2·3ⁿ⁻¹", ["aₙ = 2·3ⁿ", "aₙ = 2n+3", "aₙ = 3ⁿ"], "Umumiy formula: aₙ = a₁·q^(n−1)."),
    N(2, "Arifmetik progressiya: a₁ = 1, a₁₀ = 19. d qancha?", 2, [18, 10, 9], "", "d = (19−1)/9 = 2."),
    C(3, "Arifmetik progressiyaning 5-hadi 11, 9-hadi 19. 1-had qancha?", "3", ["1", "5", "7"], "d = (19−11)/4 = 2; a₁ = 11−8 = 3."),
    ON(3, "Geometrik progressiyaning 1-hadi 4, 3-hadi 36. Nomuvofiq ildiz q qancha?", 3, "q² = 9 → q = 3 (musbat)."),
    O(3, "1 + 2 + 3 + ... + 100 yig'indisi qancha?", ["5050"], "S = 100·101/2 = 5050."),
    M(2, [("Arifmetik progressiya", "aₙ = a₁ + (n−1)d"), ("Geometrik progressiya", "aₙ = a₁·qⁿ⁻¹"), ("Arifmetik o'rta", "a_{n} = (a_{n-1}+a_{n+1})/2")], "Progressiya formulalari."),
]

Q["M9.4"] = [  # Kombinatorika asoslari
    C(1, "5! (5 faktorial) qancha?", "120", ["60", "24", "720"], "5! = 5·4·3·2·1 = 120."),
    C(1, "3 xil kitobni tokchaga necha xil usulda joylashtirish mumkin?", "6", ["3", "9", "12"], "3! = 6."),
    N(2, "C(5,2) — 5 dan 2 tani tanlash kombinatsiyalari soni qancha?", 10, [20, 5, 15], "", "5!/(2!3!) = 10."),
    C(2, "P(4,2) — 4 elementdan 2 taning joylashtirma soni?", "12", ["6", "8", "24"], "4·3 = 12."),
    C(2, "Kumchi tangani 4 marta tashlasak, «bosh» tomonining tushish variantlari soni?", "16", ["8", "4", "2"], "2⁴ = 16."),
    C(3, "5 nafar kishidan 3 ta rahbar va 2 ta yordamchi saylash uchun necha xil tarkib bo'ladi?", "10", ["6", "20", "5"], "C(5,3) = C(5,2) = 10."),
    ON(3, "0,1,2,3,4 raqamlaridan 3 xonali (0 bilan boshlanmaydigan) nechta turli son tuziladi?", 48, "4·4·3 = 48."),
    O(3, "C(6,3) qancha?", ["20"], "6!/(3!3!) = 20."),
    M(2, [("Joylashtirish Pₙ", "n!"), ("Kombinatsiya C(n,k)", "n!/(k!(n−k)!)"), ("Joylashtirma A(n,k)", "n!/(n−k)!")], "Kombinatorika formulalari."),
]

Q["M9.5"] = [  # Ehtimollik asoslari
    C(1, "Qop ichida 3 ta qizil va 2 ta ko'k shar. Tasodifiy olingan sharning qizil bo'lish ehtimoli?", "3/5", ["2/5", "3/2", "1/3"], "P = 3/5."),
    C(1, "Tangani bir marta tashlaganda «dum» kelish ehtimoli?", "1/2", ["1/6", "2/3", "0"], "2 ta teng imkoniyat."),
    N(2, "Kubik zarni tashlash. «6» kelish ehtimoli necha kasr? (sonni yozing: 1/6 = ...)", 1, [6, 5, 3], "/6", "P = 1/6; son = 1."),
    C(2, "A va B — mustaqil hodisalar: P(A) = 0,4; P(B) = 0,5. P(A va B) = ?", "0,2", ["0,9", "0,45", "0,1"], "P(A)·P(B) = 0,2."),
    C(2, "Hamma imkoniyatlar ehtimollari yig'indisi qancha?", "1", ["0,5", "100", "n"], "Ehtimollik aksiomasi."),
    C(3, "10 ta chipta: 3 ta yutuvchi. 2 ta chipta olsak ikkalasi ham yutuvchi bo'lish ehtimoli?", "3/45 = 1/15", ["3/10", "9/100", "6/90"], "C(3,2)/C(10,2) = 3/45."),
    ON(3, "P(A) = 0,7. Hodisa sodir bo'lmaslik ehtimoli qancha (o'nli kasr)?", 0.3, "1 − 0,7 = 0,3."),
    O(3, "Qopda 5 ta qizil, 3 ta yashil shar. Tasodifiy olingan yashil bo'lish ehtimolini kasr sifatida yozing (a/b).", ["3/8"], "P = 3/8."),
]

Q["M9.6"] = [  # Statistika asoslari
    N(1, "3, 5, 7, 9, 11 — arifmetik o'rtacha qancha?", 7, [5, 9, 35], "", "35/5 = 7."),
    C(1, "2, 3, 5, 5, 8, 9 — moda qancha?", "5", ["7", "3", "9"], "Eng ko'p uchraydi."),
    C(2, "1, 2, 4, 5, 8 — mediana (o'rtacha qiymat)?", "4", ["5", "3", "2"], "Tartiblangan: o'rta element = 4."),
    N(2, "10, 20, 30, 40, 50 ma'lumotlar arifmetik o'rtachasi qancha?", 30, [35, 25, 150], "", "150/5 = 30."),
    C(3, "Dispersiya — bu nima?", "Og'ishlar kvadratining o'rtachasi", ["Barcha ma'lumotlar yig'indisi", "O'rtacha qiymat", "Eng katta va kichik farq"], "Statistik o'lchov."),
    ON(3, "3, 6, 9, 12 ma'lumotlarning arifmetik o'rtachasi qancha?", 7.5, "(3+6+9+12)/4 = 30/4 = 7,5."),
    O(3, "Ma'lumotlar: 4, 7, 7, 9, 11, 13. Medianananing qiymatini toping.", ["8"], "(7+9)/2 = 8."),
    M(2, [("O'rtacha", "Yig'indi / ta"), ("Moda", "Eng ko'p uchraydigan qiymat"), ("Mediana", "O'rta element (tartiblanganda)")], "Statistika o'lchovlari."),
]
