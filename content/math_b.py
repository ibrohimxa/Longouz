"""Matematika: 10–11-sinf mavzulari va savol banki."""
from ._dsl import C, O, M
from ._ph import N, ON, fmt

Q = {}

# ─────────────────────────── 10-SINF ────────────────────────────

Q["M10.1"] = [  # Trigonometrik funksiyalar va formulalar
    C(1, "sin²α + cos²α = ?", "1", ["0", "2", "sin·cos"], "Asosiy trigonometrik tenglik."),
    N(1, "sin 30° qancha? (kasr sifatida: a/b → faqat a ni yozing, b=2 da)", 1, [2, 3, 0], "/2", "sin 30° = 1/2."),
    C(1, "cos 0° = ?", "1", ["0", "−1", "1/2"], "cos 0° = 1."),
    C(2, "tg α = sin α / cos α bo'lsa, tg 45° = ?", "1", ["0", "√2", "1/√2"], "sin 45° = cos 45° → tg = 1."),
    C(2, "sin(90° − α) = ?", "cos α", ["−cos α", "sin α", "tg α"], "Qo'shimcha burchak formulasi."),
    C(2, "cos 2α = ?", "cos²α − sin²α", ["2sinαcosα", "1 − sin²α", "2cos²α"], "Ikki burchak kosinus formulasi."),
    C(3, "sin(α + β) = ?", "sin α·cos β + cos α·sin β", ["sin α + sin β", "sin α·sin β", "cos α·cos β"], "Yig'indi sinusi formulasi."),
    ON(3, "sin α = 3/5 va α I chorakda bo'lsa, cos α qancha? (kasr: a/b, faqat a)", 4, "cos²α = 1−9/25 = 16/25 → cos α = 4/5."),
    O(3, "2sin²α − 1 ifodasi qanday qayta yoziladi (cos 2α orqali)?", ["−cos2α", "-cos 2α"], "1 − 2sin²α = cos 2α → 2sin²α − 1 = −cos 2α."),
    M(2, [("sin 0°", "0"), ("cos 90°", "0"), ("tg 45°", "1")], "Trigonometrik jadval qiymatlari."),
]

Q["M10.2"] = [  # Trigonometrik tenglamalar
    C(1, "sin x = 0 ning umumiy yechimi?", "x = πn", ["x = π/2 + πn", "x = πn/2", "x = 2πn"], "Sinus nollanishi."),
    C(1, "cos x = 1 ning yechimi?", "x = 2πn", ["x = πn", "x = π/2 + 2πn", "x = 0"], "cos 2πn = 1."),
    C(2, "sin x = 1/2 ning asosiy yechimi (0 ≤ x ≤ π)?", "x = π/6 va x = 5π/6", ["x = π/6", "x = π/3", "x = π/4"], "sin π/6 = 1/2; simetrikasi 5π/6."),
    C(2, "2cos x − √3 = 0. cos x = ?", "√3/2", ["1/2", "√2/2", "√3"], "cos x = √3/2."),
    C(3, "tg x = 1 ning umumiy yechimi?", "x = π/4 + πn", ["x = π/4", "x = π/4 + 2πn", "x = π/4 + πn/2"], "Tangens π ga davriy."),
    ON(3, "sin²x + sin x − 2 = 0. Almashtirish t = sin x: t² + t − 2 = 0. t ning mumkin bo'lgan qiymati?", 1, "t = 1 (chunki |sin x| ≤ 1); t = −2 mumkin emas."),
    O(3, "2sin x − 1 = 0 tenglamasining [0; π] oralig'idagi yechinmlari soni.", ["2"], "sin x = 1/2: x = π/6 va x = 5π/6."),
]

Q["M10.3"] = [  # Logarifm va ko'rsatkichli funksiyalar
    C(1, "log₂ 8 = ?", "3", ["4", "2", "8"], "2³ = 8."),
    C(1, "log₁₀ 100 = ?", "2", ["10", "20", "1"], "10² = 100."),
    C(2, "log_a(mn) = ?", "log_a m + log_a n", ["log_a m · log_a n", "log_a(m+n)", "log_a m − log_a n"], "Ko'paytma logarifmi."),
    C(2, "log₂(1/8) = ?", "−3", ["3", "−1/3", "1/3"], "log₂ 2⁻³ = −3."),
    C(2, "2ˣ = 16. x = ?", "4", ["8", "2", "6"], "2⁴ = 16."),
    C(3, "log₃ 27 + log₃ 3 = ?", "4", ["3", "9", "6"], "3 + 1 = 4."),
    ON(3, "log₂ 32 qancha?", 5, "2⁵ = 32."),
    O(3, "10ˣ = 1000 tenglamasini yeching.", ["3"], "10³ = 1000."),
    M(2, [("log_a(mn)", "log_a m + log_a n"), ("log_a(m/n)", "log_a m − log_a n"), ("log_a(mⁿ)", "n·log_a m")], "Logarifm xossalari."),
]

Q["M10.4"] = [  # Ko'rsatkichli va logarifmik tenglamalar
    C(1, "2ˣ = 32. x = ?", "5", ["4", "6", "3"], "2⁵ = 32."),
    C(2, "3ˣ⁺¹ = 27. x = ?", "2", ["3", "1", "4"], "3ˣ⁺¹ = 3³ → x+1 = 3 → x = 2."),
    C(2, "log₂(x+1) = 3. x = ?", "7", ["8", "6", "3"], "x+1 = 2³ = 8 → x = 7."),
    C(3, "4ˣ = 2ˣ⁺² tenglamani yeching. x = ?", "2", ["1", "4", "3"], "2²ˣ = 2ˣ⁺² → 2x = x+2 → x = 2."),
    ON(3, "log₅(x−1) = 2. x qancha?", 26, "x−1 = 25 → x = 26."),
    O(3, "e = 2,718... logarifmning kalit maqomi qaysi?", ["e", "natural", "tabiiy"], "ln = natural log."),
    C(2, "5²ˣ⁻¹ = 125 tenglamasini yeching.", "x = 2", ["x = 1", "x = 3", "x = 0,5"], "5²ˣ⁻¹ = 5³ → 2x−1=3 → x=2."),
    ON(3, "log₃(2x+1) = 3 tenglamasining yechimi?", 13, "2x+1=27 → x=13."),
]

Q["M10.5"] = [  # Vektorlar va koordinatalar
    N(1, "A(1;2) va B(4;6) nuqtalar. AB vektori modulini hisoblang.", 5, [3, 4, 7], "", "√((4-1)²+(6-2)²) = √(9+16) = 5."),
    C(1, "a⃗ = (3;4). |a⃗| = ?", "5", ["7", "12", "√7"], "√(9+16) = 5."),
    C(2, "a⃗ = (2;1) va b⃗ = (3;−1). a⃗·b⃗ (skalyar ko'paytma) = ?", "5", ["6", "2", "−1"], "2·3 + 1·(−1) = 5."),
    C(2, "Vektorlarning skalyar ko'paytmasi a⃗·b⃗ = 0 nimani bildiradi?", "Vektorlar perpendikulyar", ["Parallel", "Teng", "Qarama-qarshi"], "Perpendikulyarlik sharti."),
    N(2, "a⃗=(1;2) va b⃗=(3;4). a⃗+b⃗ ning x-koordinatasi?", 4, [2, 6, 5], "", "1+3=4."),
    C(3, "OA⃗ = (3;4), OB⃗ = (0;0). AB⃗ vektori?", "(−3;−4)", ["(3;4)", "(0;0)", "(6;8)"], "B−A = (0−3; 0−4)."),
    ON(3, "a⃗ = (6;8). |a⃗| qancha?", 10, "√(36+64) = 10."),
    O(3, "a⃗=(2;3) va b⃗=(4;6). Bu vektorlar parallel bo'ladimi? Javob: ha yoki yo'q.", ["ha", "Ha"], "2/4 = 3/6 = 1/2 → parallel."),
]

Q["M10.6"] = [  # Stereometriya: asoslar
    C(1, "Kubning nechta qirrasi bor?", "12", ["6", "8", "4"], "Kub — 12 qirra."),
    C(1, "Sferani ikkita tekislik kesishi natijasida hosil bo'ladigan figura?", "Aylana", ["Kvadrat", "Ellips", "Uchburchak"], "To'g'ri tekislik sferani doira bo'yicha kesadi."),
    C(2, "To'g'ri to'rtburchakli parallelepiped hajmi V = a·b·c bo'lsa, a=2, b=3, c=5 da V = ?", "30", ["10", "25", "6"], "V = 2·3·5 = 30."),
    C(2, "Muntazam tetraedrdagi tenglanar tomonlar soni qancha?", "4", ["3", "6", "8"], "Tetraed — 4 ta teng uchburchak yuz."),
    N(2, "Silindr r=3, h=4. Yon sirti (π oldidagi son)?", 24, [12, 36, 6], "π", "2πrh=2·3·4=24π."),
    ON(3, "Konus r=3, h=4, yasovchisi l=5. To'la sirti (π oldidagi son)?", 24, "πrl + πr² = 15π + 9π = 24π."),
    O(3, "Kub qirrasini 2 barobarga oshirsak, hajmi necha barobarga oshadi? (son yozing)", ["8"], "V = a³ → (2a)³ = 8a³; 8 marta."),
]

# ─────────────────────────── 11-SINF ────────────────────────────

Q["M11.1"] = [  # Hosila va differentsial hisob
    C(1, "f(x) = x³ ning hosilasi f'(x) = ?", "3x²", ["x²", "3x", "2x³"], "Darajaning hosila qoidasi."),
    C(1, "f(x) = sin x → f'(x) = ?", "cos x", ["−cos x", "−sin x", "tg x"], "Sinus hosilasi."),
    C(2, "f(x) = x⁴ − 2x² + 1. f'(x) = ?", "4x³ − 4x", ["4x³ − 2x", "4x³ + 4x", "x³ − 4x"], "Qo'sh chiziqli."),
    C(2, "f(x) = ln x. f'(x) = ?", "1/x", ["1/ln x", "ln 1/x", "x/ln x"], "Logarifm hosilasi."),
    C(2, "f(x) = eˣ. f'(x) = ?", "eˣ", ["e^(x−1)", "x·eˣ⁻¹", "eˣ−1"], "Eksponent o'z hosilasi."),
    C(3, "f(x) = x·sin x. f'(x) = ?", "sin x + x·cos x", ["cos x", "x·cos x", "sin x − x·cos x"], "Ko'paytma hosilasi: u'v + uv'."),
    ON(3, "f(x) = x² − 4x + 3 ning f'(x) = 0 bo'lgan x qiymatini toping.", 2, "2x − 4 = 0 → x = 2."),
    O(3, "f(x) = 5x³ − 3x ning f'(2) qiymatini hisoblang.", ["57"], "f'(x) = 15x² − 3; f'(2) = 60 − 3 = 57."),
    M(2, [("(u + v)' ", "u' + v'"), ("(u·v)'", "u'v + uv'"), ("(u/v)'", "(u'v − uv')/v²")], "Hosila qoidalari."),
]

Q["M11.2"] = [  # Integral
    C(1, "∫2x dx = ?", "x² + C", ["2x²+ C", "x + C", "2 + C"], "Darajaning integrali."),
    C(1, "∫cos x dx = ?", "sin x + C", ["−sin x + C", "tg x + C", "cos²x + C"], "Kosinus integrali."),
    C(2, "∫(x² + 3) dx = ?", "x³/3 + 3x + C", ["x³ + 3x + C", "x³/3 + 3 + C", "2x + C"], "Bo'g'in bo'yicha integrallash."),
    N(2, "∫₁² 2x dx qiymatini hisoblang.", 3, [4, 2, 6], "", "[x²]₁² = 4 − 1 = 3."),
    C(3, "∫₀^π sin x dx = ?", "2", ["0", "−2", "π"], "[−cos x]₀^π = 1+1 = 2."),
    ON(3, "∫₀¹ (x + 1) dx qancha?", 1.5, "[x²/2 + x]₀¹ = 0,5 + 1 = 1,5."),
    O(3, "∫eˣ dx = ?", ["e^x + C", "eˣ + C"], "eˣ ning integrali o'zi."),
]

Q["M11.3"] = [  # Koordinatali geometriya: to'g'ri chiziq va konus kesimlari
    C(1, "Ikki nuqta A(1;2), B(3;6). Ularni birlashtiruvchi kesmaning o'rtasi?", "(2; 4)", ["(1; 3)", "(4; 8)", "(2; 3)"], "((1+3)/2; (2+6)/2)."),
    C(2, "ax + by + c = 0 to'g'ri chiziqqa parallel to'g'ri chiziq shakli?", "ax + by + c₁ = 0 (c₁ ≠ c)", ["ax − by + c = 0", "bx + ay + c = 0", "−ax − by − c = 0"], "Bir xil normal vektor."),
    C(2, "x² + y² = r² — bu qanday egri chiziq?", "Aylana", ["Ellips", "Giperbola", "Parabola"], "Markaziy aylana tenglamasi."),
    N(2, "A(0;0) va B(5;12) oralidagi masofa qancha?", 13, [17, 5, 12], "", "√(25+144) = 13."),
    C(3, "Ikki to'g'ri chiziq y = 3x + 1 va y = 3x − 2. Ular nima?", "Parallel", ["Kesishadi", "Perpendikulyar", "Ustma-ust tushadi"], "Bir xil burchak koeffitsiyenti."),
    ON(3, "Aylana markazi (0;0), radius 5. (3;4) nuqtasi aylananing ichida, tashqarisida yoki ustida?", 1, "3²+4²=25=5²; ustida. Son javob: 1 (ustida)."),
    O(3, "To'g'ri chiziq 2x + 3y = 12. Bu to'g'ri chiziq y o'qini qaysi nuqtada kesadi? (y ni yozing)", ["4"], "x=0: 3y=12 → y=4."),
]

Q["M11.4"] = [  # Limit asoslari
    C(1, "lim(x→2) (x² − 4)/(x − 2) = ?", "4", ["0", "∞", "2"], "(x+2)(x−2)/(x−2) → x+2; x=2: 4."),
    C(1, "lim(x→∞) (1/x) = ?", "0", ["∞", "1", "−∞"], "1/∞ → 0."),
    C(2, "lim(x→0) (sin x)/x = ?", "1", ["0", "∞", "sin 1"], "1-chi ajoyib limit."),
    C(2, "lim(x→∞) (2x + 3)/(x + 1) = ?", "2", ["3", "∞", "0"], "Yuqori daraja koeffitsiyentlari nisbati."),
    C(3, "lim(x→1) (x³ − 1)/(x − 1) = ?", "3", ["1", "0", "∞"], "x³−1=(x−1)(x²+x+1); limit=1+1+1=3."),
    ON(3, "lim(x→∞) (3x² + 1)/(x² − 2) qancha?", 3, "Yuqori darajalar nisbati."),
    O(3, "lim(x→0) (1 − cos x)/x² = ? (son)", ["0.5", "1/2", "0,5"], "Ikkinchi ajoyib limit va Taylor qatori."),
]

Q["M11.5"] = [  # Funksiya tadqiqi (hosila orqali)
    C(1, "f'(x) > 0 bo'lganda funksiya qanday?", "O'suvchi", ["Kamayuvchi", "Doimiy", "Toq"], "Hosila musbat — funksiya o'sadi."),
    C(2, "f'(x₀) = 0 bo'lsa, x₀ nima deyiladi?", "Kritik nuqta", ["O'sish nuqtasi", "Uzilish nuqtasi", "Kesish nuqtasi"], "Hosilaning nollanish nuqtasi."),
    C(2, "f''(x₀) > 0 bo'lsa, x₀ da...", "Minimum", ["Maksimum", "Burilish nuqtasi", "O'sish nuqtasi"], "Ikkinchi hosila musbat → minimum."),
    C(3, "f(x) = x³ − 3x ning mahalliy maksimumi qaerda?", "x = −1", ["x = 1", "x = 0", "x = 3"], "f'(x) = 3x²−3 = 0 → x = ±1; f''(1) > 0 min; f''(−1) < 0 max."),
    ON(3, "f(x) = 2x − x² ning eng katta qiymati qancha?", 1, "f'(x) = 2−2x = 0 → x=1; f(1) = 1."),
    O(3, "f(x) = x³ ning x = 0 dagi egrilik tabiati: burilish nuqtami yoki ekstremummi?", ["burilish", "burilish nuqtasi"], "f\'\' (0) = 0, burilish nuqtasi."),
    C(2, "f(x) = x³ − 3x² funksiyasining x=2 dagi hosilasi?", "0", ["3", "6", "−3"], "f'(x) = 3x²−6x; f'(2)=12−12=0."),
    ON(3, "f(x) = x⁴ − 8x² + 7 ning f'(x) = 0 musbat ildizlaridan kichigi qancha?", 2, "f'=4x³−16x=4x(x²−4)=0 → x=0,±2; musbat: 2."),
]

Q["M11.6"] = [  # Murakkab masalalar: to'liq hisob va kombinatsiya
    N(1, "5 ta toq son yig'indisi: 1+3+5+7+9 = ?", 25, [20, 15, 30], "", "5² = 25."),
    N(2, "1² + 2² + 3² + ... + 10² = ?", 385, [55, 100, 330], "", "n(n+1)(2n+1)/6 = 385."),
    C(2, "log₂ 4 + log₂ 8 = ?", "5", ["3", "4", "12"], "2 + 3 = 5."),
    C(3, "2sin x cos x = 1 tenglamaning [0; 2π] oralig'idagi yechimlari soni?", "2", ["1", "4", "∞"], "sin 2x = 1 → 2x = π/2 + 2πn → x = π/4, 5π/4."),
    ON(3, "P(n,2) = 30. n qancha?", 6, "n(n−1) = 30 → n = 6."),
    O(3, "Uchburchakning tomonlari 3, 4, 5. Bu qanday uchburchak? (bir so'z)", ["to'g'ri burchakli", "to'g'ri", "rectangular"], "3²+4²=5²."),
    M(2, [("Arifmetik progressiya yig'indisi", "Sₙ = n(a₁+aₙ)/2"), ("Geometrik progressiya yig'indisi (|q|<1)", "S∞ = a₁/(1−q)"), ("Hosila ko'paytma qoidasi", "(uv)' = u'v + uv'")], "Asosiy formulalar."),
]

Q["M11.7"] = [  # DTM murakkab masalalar
    C(1, "sin(3π/2) = ?", "−1", ["0", "1", "√2/2"], "3π/2 = 270°; sin 270° = −1."),
    N(2, "Arifmetik progressiya: a₁ = 2, d = 3. S₁₀ yig'indisi qancha?", 155, [150, 160, 145], "", "S₁₀ = 10(2·2+9·3)/2 = 5·31 = 155."),
    C(2, "f(x) = |x − 2| funksiyasi x = 2 da uzilishlimi?", "Yo'q (uzluksiz)", ["Ha (uzilish bor)", "Chekli uzilish", "O'chirib tashlash mumkin"], "Modul funksiyasi hamma joyda uzluksiz."),
    C(3, "∫₀¹ x² dx = ?", "1/3", ["1", "1/2", "3"], "[x³/3]₀¹ = 1/3."),
    ON(3, "C(8,3) qancha?", 56, "8!/(3!5!) = 56."),
    O(3, "lim(x→3) (x²−9)/(x−3) ni hisoblang.", ["6"], "(x+3)(x−3)/(x−3) → x+3; x=3: 6."),
    M(2, [("sin²x + cos²x", "1"), ("1 + tg²x", "1/cos²x"), ("1 + ctg²x", "1/sin²x")], "Asosiy trigonometrik tengliklar."),
]

# ─── QOSHIMCHA SAVOLLAR: 6 dan kam bo'lgan mavzular to'ldirish ───
# M9.2 ga qo'shimcha (to'g'ridan-to'g'ri math_a.py Q["M9.2"] ga qo'shiladi)
# Lekin biz bu yerga qo'sha olmaymiz — matematik_a da. Shuning uchun math_b ga alohida belgi qo'yamiz.
_M9_2_EXTRA = [
    # Bu savollar math_a.Q["M9.2"] ga merge qilinadi (mathematics.py ichida)
]
_M10_4_EXTRA = [
    # Bu savollar math_b.Q["M10.4"] ga merge qilinadi
]
_M11_5_EXTRA = [
    # Bu savollar math_b.Q["M11.5"] ga merge qilinadi
]
