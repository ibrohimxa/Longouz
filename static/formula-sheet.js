// ============================================================================
// LongoUZ — test paytidagi YORDAMCHI QO'LLANMA (fan bo'yicha moslashadi):
//   - matematika        → "Formulalar"  (barcha asosiy formulalar, guruhlangan)
//   - fizika            → "Formulalar"  (formula + BIRLIK ustuni, doimiylar)
//   - kimyo, biologiya  → "Mendeleyev"  (118 element, xalqaro standart tartib;
//                          elementga bosilsa proton/elektron/neytron va h.k.)
// Tugma sahifa headerida, SOAT OLDIDA joylashtiriladi. Oyna ochilganda orqadagi
// savollar xiralashadi (backdrop blur).
// ============================================================================

(function () {
  "use strict";
  const body = document.body;
  const subject = body.dataset.subject;

  const PANEL_CONFIG = {
    math: { label: "Formulalar", icon: "sigma", builder: buildFormulaBody, title: "Matematika formulalari", wide: true },
    physics: { label: "Formulalar", icon: "sigma", builder: buildFormulaBody, title: "Fizika formulalari va birliklari", wide: true },
    chemistry: { label: "Mendeleyev", icon: "table", builder: buildPeriodicTableBody, title: "Mendeleyev davriy jadvali", periodic: true },
    biology: { label: "Yordamchi", icon: "table", builder: buildBiologyBody, title: "Biologiya yordamchisi", periodic: true, tabs: true },
  };
  const config = PANEL_CONFIG[subject];
  if (!config) return;

  const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ===================== MATEMATIKA FORMULALARI =====================
  const MATH_FORMULA_GROUPS = [
    { title: "Qisqa ko'paytirish", items: [
      ["Yig'indi kvadrati", "(a+b)² = a² + 2ab + b²"],
      ["Ayirma kvadrati", "(a−b)² = a² − 2ab + b²"],
      ["Kvadratlar ayirmasi", "a² − b² = (a−b)(a+b)"],
      ["Yig'indi kubi", "(a+b)³ = a³ + 3a²b + 3ab² + b³"],
      ["Kublar yig'indisi", "a³ + b³ = (a+b)(a² − ab + b²)"],
      ["Kublar ayirmasi", "a³ − b³ = (a−b)(a² + ab + b²)"],
    ]},
    { title: "Foizlar va nisbatlar", items: [
      ["A ning n% i", "A × n ÷ 100"],
      ["Necha foiz ekanini topish", "(qism ÷ butun) × 100%"],
      ["Foizga oshirish", "A × (1 + n⁄100)"],
      ["Foizga kamaytirish", "A × (1 − n⁄100)"],
      ["Murakkab foiz", "S = A·(1 + p⁄100)ⁿ"],
      ["Oddiy foiz", "I = A·p·t ÷ 100"],
      ["Eritma konsentratsiyasi", "C = m(modda) ÷ m(eritma) × 100%"],
      ["Proporsiya", "a⁄b = c⁄d  ⇒  ad = bc"],
    ]},
    { title: "Sonlar nazariyasi", items: [
      ["EKUB va EKUK", "EKUB(a,b) · EKUK(a,b) = a · b"],
      ["3 va 9 ga bo'linish", "raqamlar yig'indisi 3 (9) ga bo'linadi"],
      ["4 ga bo'linish", "oxirgi ikki raqam 4 ga bo'linadi"],
      ["Juft / toq son", "2k  /  2k+1"],
      ["Natural sonlar yig'indisi", "1+2+…+n = n(n+1) ÷ 2"],
      ["Kvadratlar yig'indisi", "1²+2²+…+n² = n(n+1)(2n+1) ÷ 6"],
    ]},
    { title: "Tenglamalar va tengsizliklar", items: [
      ["Chiziqli tenglama", "ax + b = 0  →  x = −b ⁄ a"],
      ["Kvadrat tenglama", "ax² + bx + c = 0"],
      ["Diskriminant", "D = b² − 4ac"],
      ["Ildizlar", "x₁,₂ = (−b ± √D) ⁄ 2a"],
      ["Viet teoremasi", "x₁+x₂ = −b⁄a,  x₁·x₂ = c⁄a"],
      ["Parabola uchi", "x₀ = −b⁄2a,  y₀ = f(x₀)"],
      ["Modulli tenglama", "|x| = a  ⇒  x = ±a  (a ≥ 0)"],
      ["Koshi tengsizligi", "(a+b)⁄2 ≥ √(ab),  a,b ≥ 0"],
    ]},
    { title: "Progressiyalar", items: [
      ["Arifmetik: n-had", "aₙ = a₁ + (n−1)d"],
      ["Arifmetik: yig'indi", "Sₙ = n(a₁+aₙ) ÷ 2 = n(2a₁+(n−1)d) ÷ 2"],
      ["Arifmetik: o'rta had", "aₙ = (aₙ₋₁ + aₙ₊₁) ÷ 2"],
      ["Geometrik: n-had", "bₙ = b₁ · q^(n−1)"],
      ["Geometrik: yig'indi (q≠1)", "Sₙ = b₁(qⁿ−1) ÷ (q−1)"],
      ["Cheksiz kamayuvchi", "S = b₁ ÷ (1−q),  |q| < 1"],
    ]},
    { title: "Daraja va ildiz", items: [
      ["Ko'paytma", "aⁿ · aᵐ = aⁿ⁺ᵐ"],
      ["Bo'linma", "aⁿ ÷ aᵐ = aⁿ⁻ᵐ"],
      ["Daraja darajasi", "(aⁿ)ᵐ = aⁿᵐ"],
      ["Manfiy va nol daraja", "a⁻ⁿ = 1⁄aⁿ,  a⁰ = 1 (a≠0)"],
      ["Kasr daraja", "a^(m⁄n) = ⁿ√(aᵐ)"],
      ["Ildiz ko'paytmasi", "√(ab) = √a · √b  (a,b ≥ 0)"],
    ]},
    { title: "Logarifm", items: [
      ["Ta'rif", "logₐb = x  ⇔  aˣ = b"],
      ["Asosiy ayniyat", "a^(logₐb) = b"],
      ["Ko'paytma", "logₐ(xy) = logₐx + logₐy"],
      ["Bo'linma", "logₐ(x⁄y) = logₐx − logₐy"],
      ["Daraja", "logₐ(xⁿ) = n · logₐx"],
      ["Yangi asosga o'tish", "logₐb = logᶜb ⁄ logᶜa"],
      ["Maxsus qiymatlar", "logₐ1 = 0,  logₐa = 1"],
    ]},
    { title: "Trigonometriya", items: [
      ["Asosiy ayniyat", "sin²α + cos²α = 1"],
      ["Tangens / kotangens", "tanα = sinα⁄cosα,  cotα = cosα⁄sinα"],
      ["Qo'shimcha ayniyatlar", "1+tan²α = 1⁄cos²α,  1+cot²α = 1⁄sin²α"],
      ["Qo'sh burchak sinusi", "sin2α = 2 sinα cosα"],
      ["Qo'sh burchak kosinusi", "cos2α = cos²α − sin²α = 1 − 2sin²α"],
      ["Yig'indi sinusi", "sin(α±β) = sinα cosβ ± cosα sinβ"],
      ["Yig'indi kosinusi", "cos(α±β) = cosα cosβ ∓ sinα sinβ"],
      ["Darajani pasaytirish", "sin²α = (1−cos2α)⁄2,  cos²α = (1+cos2α)⁄2"],
      ["Burchaklar qiymati", "sin30°=½, sin45°=√2⁄2, sin60°=√3⁄2"],
      ["Radian", "π rad = 180°"],
      ["sin x = a", "x = (−1)ⁿ arcsin a + πn"],
      ["cos x = a", "x = ± arccos a + 2πn"],
      ["tan x = a", "x = arctan a + πn"],
    ]},
    { title: "Hosila", items: [
      ["Doimiy", "(C)′ = 0"],
      ["Daraja", "(xⁿ)′ = n·xⁿ⁻¹"],
      ["Ko'paytma", "(uv)′ = u′v + uv′"],
      ["Bo'linma", "(u⁄v)′ = (u′v − uv′) ⁄ v²"],
      ["Murakkab funksiya", "(f(g(x)))′ = f′(g)·g′"],
      ["sin, cos", "(sin x)′ = cos x,  (cos x)′ = −sin x"],
      ["tan", "(tan x)′ = 1⁄cos²x"],
      ["Ko'rsatkichli", "(eˣ)′ = eˣ,  (aˣ)′ = aˣ·ln a"],
      ["Logarifmik", "(ln x)′ = 1⁄x,  (logₐx)′ = 1⁄(x·ln a)"],
      ["Ildiz", "(√x)′ = 1⁄(2√x)"],
      ["Urinma tenglamasi", "y = f(x₀) + f′(x₀)(x − x₀)"],
    ]},
    { title: "Integral", items: [
      ["Daraja", "∫xⁿdx = xⁿ⁺¹⁄(n+1) + C  (n≠−1)"],
      ["1/x", "∫dx⁄x = ln|x| + C"],
      ["Ko'rsatkichli", "∫eˣdx = eˣ + C"],
      ["sin, cos", "∫sin x dx = −cos x + C,  ∫cos x dx = sin x + C"],
      ["Nyuton–Leybnits", "∫ₐᵇ f(x)dx = F(b) − F(a)"],
      ["Egri trapetsiya yuzi", "S = ∫ₐᵇ (f(x) − g(x)) dx"],
    ]},
    { title: "Planimetriya", items: [
      ["Uchburchak yuzi", "S = ½·a·h = ½ab·sinC"],
      ["Geron formulasi", "S = √(p(p−a)(p−b)(p−c)),  p=(a+b+c)⁄2"],
      ["Ichki / tashqi aylana", "S = p·r,  S = abc ⁄ 4R"],
      ["Sinuslar teoremasi", "a⁄sinA = b⁄sinB = c⁄sinC = 2R"],
      ["Kosinuslar teoremasi", "c² = a² + b² − 2ab·cosC"],
      ["Pifagor teoremasi", "c² = a² + b²"],
      ["Teng tomonli uchburchak", "S = a²√3 ⁄ 4"],
      ["To'rtburchak, kvadrat", "S = a·b,  S = a²"],
      ["Parallelogramm, romb", "S = a·h,  S = d₁d₂ ⁄ 2"],
      ["Trapetsiya", "S = (a+b)⁄2 · h"],
      ["Aylana", "l = 2πr,  S = πr²"],
      ["Doira sektori", "S = πr²α⁄360°,  l = πrα⁄180°"],
      ["Ichki burchaklar yig'indisi", "(n−2)·180°"],
    ]},
    { title: "Stereometriya", items: [
      ["Prizma, silindr hajmi", "V = S(asos)·h,  V = πr²h"],
      ["Piramida, konus hajmi", "V = S(asos)·h⁄3,  V = πr²h⁄3"],
      ["Silindr sirti", "S(yon) = 2πrh,  S(to'liq) = 2πr(r+h)"],
      ["Konus sirti", "S(yon) = πrl,  S(to'liq) = πr(r+l)"],
      ["Shar", "V = 4πr³⁄3,  S = 4πr²"],
      ["Kub", "V = a³,  S = 6a²,  d = a√3"],
      ["Parallelepiped", "V = a·b·c,  d = √(a²+b²+c²)"],
      ["Kesik konus", "V = πh(R² + Rr + r²) ⁄ 3"],
    ]},
    { title: "Koordinatalar va vektorlar", items: [
      ["Ikki nuqta orasidagi masofa", "d = √((x₂−x₁)² + (y₂−y₁)²)"],
      ["Kesma o'rtasi", "((x₁+x₂)⁄2 ; (y₁+y₂)⁄2)"],
      ["To'g'ri chiziq", "y = kx + b,  k = (y₂−y₁)⁄(x₂−x₁)"],
      ["Parallel / perpendikulyar", "k₁ = k₂  /  k₁·k₂ = −1"],
      ["Aylana tenglamasi", "(x−a)² + (y−b)² = R²"],
      ["Nuqtadan to'g'ri chiziqqacha", "d = |Ax₀+By₀+C| ⁄ √(A²+B²)"],
      ["Vektor uzunligi", "|a| = √(x² + y²)"],
      ["Skalyar ko'paytma", "a·b = x₁x₂ + y₁y₂ = |a||b|cosφ"],
    ]},
    { title: "Kombinatorika va ehtimollik", items: [
      ["Faktorial", "n! = 1·2·3·…·n,  0! = 1"],
      ["O'rin almashtirish", "Pₙ = n!"],
      ["Joylashtirish", "Aₙᵏ = n! ⁄ (n−k)!"],
      ["Guruhlash", "Cₙᵏ = n! ⁄ (k!(n−k)!)"],
      ["Nyuton binomi", "(a+b)ⁿ = Σ Cₙᵏ · aⁿ⁻ᵏ · bᵏ"],
      ["Ehtimollik", "P(A) = m ⁄ n"],
      ["Qarama-qarshi hodisa", "P(Ā) = 1 − P(A)"],
      ["Yig'indi ehtimoli", "P(A∪B) = P(A) + P(B) − P(A∩B)"],
      ["Mustaqil hodisalar", "P(A∩B) = P(A)·P(B)"],
      ["O'rta arifmetik", "x̄ = (x₁+x₂+…+xₙ) ⁄ n"],
    ]},
    { title: "Harakat, ish va aralashma masalalari", items: [
      ["Yo'l", "s = v · t"],
      ["O'rtacha tezlik", "v(o'rt) = s(butun) ⁄ t(butun)"],
      ["Oqim bo'ylab / qarshi", "v = v₀ + v(oqim),  v = v₀ − v(oqim)"],
      ["Birgalikda ishlash", "1⁄t = 1⁄t₁ + 1⁄t₂"],
      ["Uchrashuv", "t = s ⁄ (v₁ + v₂)"],
    ]},
  ];

  // ===================== FIZIKA FORMULALARI (formula + BIRLIK) =====================
  const PHYSICS_FORMULA_GROUPS = [
    { title: "Kinematika", items: [
      ["Tezlik", "v = s / t", "m/s"],
      ["Tezlanish", "a = (v − v₀) / t", "m/s²"],
      ["Tezlik (tekis o'zgaruvchan)", "v = v₀ + at", "m/s"],
      ["Yo'l", "s = v₀t + at²/2", "m"],
      ["Tezlikka bog'liq yo'l", "s = (v² − v₀²) / 2a", "m"],
      ["Erkin tushish balandligi", "h = gt²/2", "m"],
      ["Erkin tushish tezligi", "v = gt = √(2gh)", "m/s"],
      ["Gorizontal otilgan jism uchish masofasi", "L = v₀·√(2h/g)", "m"],
      ["Yuqoriga otilganda maks. balandlik", "H = v₀² / 2g", "m"],
      ["Burchak ostida: uchish uzoqligi", "L = v₀² sin2α / g", "m"],
      ["Burchak ostida: maks. balandlik", "H = v₀² sin²α / 2g", "m"],
      ["Aylanish davri / chastotasi", "T = t/N,  f = N/t", "s,  Hz"],
      ["Burchak tezlik", "ω = 2π/T = 2πf", "rad/s"],
      ["Chiziqli tezlik", "v = ωR = 2πR/T", "m/s"],
      ["Markazga intilma tezlanish", "aₘ = v²/R = ω²R", "m/s²"],
    ]},
    { title: "Dinamika", items: [
      ["Nyutonning 2-qonuni", "F = ma", "N"],
      ["Og'irlik kuchi", "P = mg", "N"],
      ["Ishqalanish kuchi", "Fishq = μN", "N"],
      ["Guk qonuni", "F = kx", "N"],
      ["Butun olam tortishish", "F = G·m₁m₂ / r²", "N"],
      ["Erkin tushish tezlanishi", "g = GM / R²", "m/s²"],
      ["1-kosmik tezlik", "v = √(gR) = √(GM/R)", "m/s"],
      ["Qiyalikda tezlanish", "a = g(sinα − μcosα)", "m/s²"],
      ["Jism impulsi", "p = mv", "kg·m/s"],
      ["Kuch impulsi", "F·t = Δp = mv − mv₀", "N·s"],
      ["Impulsning saqlanishi", "m₁v₁ + m₂v₂ = m₁u₁ + m₂u₂", "kg·m/s"],
    ]},
    { title: "Statika va gidrostatika", items: [
      ["Kuch momenti", "M = F·d", "N·m"],
      ["Muvozanat sharti", "ΣF = 0,  ΣM = 0", "—"],
      ["Richag", "F₁/F₂ = l₂/l₁", "—"],
      ["Zichlik", "ρ = m / V", "kg/m³"],
      ["Bosim", "p = F / S", "Pa"],
      ["Suyuqlik bosimi", "p = ρgh", "Pa"],
      ["Arximed kuchi", "Fa = ρ(suyuq)·g·V", "N"],
      ["Uzluksizlik tenglamasi", "S₁v₁ = S₂v₂", "m³/s"],
      ["Bernulli tenglamasi", "p + ρv²/2 + ρgh = const", "Pa"],
    ]},
    { title: "Ish, quvvat, energiya", items: [
      ["Mexanik ish", "A = F·s·cosα", "J"],
      ["Quvvat", "N = A / t = F·v", "W"],
      ["Kinetik energiya", "Ek = mv² / 2", "J"],
      ["Potensial energiya", "Ep = mgh", "J"],
      ["Elastik deformatsiya energiyasi", "Ep = kx² / 2", "J"],
      ["Kinetik energiya teoremasi", "A = Ek₂ − Ek₁", "J"],
      ["Energiyaning saqlanishi", "Ek + Ep = const", "J"],
      ["FIK", "η = A(foydali) / A(sarflangan) × 100%", "%"],
    ]},
    { title: "Molekulyar-kinetik nazariya", items: [
      ["Modda miqdori", "ν = m / M = N / N_A", "mol"],
      ["Molekulalar soni", "N = ν·N_A,  N_A = 6,02·10²³", "mol⁻¹"],
      ["MKT asosiy tenglamasi", "p = (1/3)·n·m₀·v̄² = (2/3)·n·Ēk", "Pa"],
      ["Molekula o'rtacha kinetik energiyasi", "Ēk = (3/2)·kT", "J"],
      ["Bosim va temperatura", "p = nkT,  k = 1,38·10⁻²³", "Pa,  J/K"],
      ["Klapeyron–Mendeleyev", "pV = νRT = (m/M)RT,  R = 8,31", "Pa·m³,  J/(mol·K)"],
      ["Temperatura shkalalari", "T = t + 273", "K"],
      ["Izotermik (Boyl–Mariott)", "p₁V₁ = p₂V₂  (T=const)", "—"],
      ["Izobarik (Gey-Lyussak)", "V₁/T₁ = V₂/T₂  (p=const)", "—"],
      ["Izoxorik (Sharl)", "p₁/T₁ = p₂/T₂  (V=const)", "—"],
      ["Birlashgan gaz qonuni", "p₁V₁/T₁ = p₂V₂/T₂", "—"],
      ["Nisbiy namlik", "φ = ρ / ρ(to'yingan) × 100%", "%"],
    ]},
    { title: "Termodinamika", items: [
      ["Isitish / sovutish issiqligi", "Q = cmΔt", "J"],
      ["Erish issiqligi", "Q = λm", "J"],
      ["Bug'lanish issiqligi", "Q = Lm", "J"],
      ["Yonish issiqligi", "Q = qm", "J"],
      ["Gaz bajargan ish", "A = pΔV", "J"],
      ["Bir atomli gaz ichki energiyasi", "U = (3/2)·νRT", "J"],
      ["Termodinamikaning 1-qonuni", "Q = ΔU + A", "J"],
      ["Issiqlik mashinasi FIK", "η = (Q₁ − Q₂) / Q₁", "—"],
      ["Karno sikli FIK", "η = (T₁ − T₂) / T₁", "—"],
    ]},
    { title: "Elektrostatika", items: [
      ["Kulon qonuni", "F = k·q₁q₂ / r²,  k = 9·10⁹", "N"],
      ["Elektr maydon kuchlanganligi", "E = F / q = kq / r²", "V/m  (N/C)"],
      ["Maydon potensiali", "φ = kq / r", "V"],
      ["Kuchlanish (potensiallar farqi)", "U = A / q = E·d", "V"],
      ["Kondensator sig'imi", "C = q / U = ε₀εS / d", "F"],
      ["Kondensator energiyasi", "W = CU²/2 = q²/2C", "J"],
      ["Ketma-ket / parallel kondensator", "1/C = Σ1/Cᵢ  /  C = ΣCᵢ", "F"],
    ]},
    { title: "O'zgarmas tok", items: [
      ["Tok kuchi", "I = q / t", "A"],
      ["Om qonuni (qism)", "I = U / R", "A"],
      ["O'tkazgich qarshiligi", "R = ρ·l / S", "Ω"],
      ["Ketma-ket ulash", "R = R₁ + R₂,  I = const", "Ω"],
      ["Parallel ulash", "1/R = 1/R₁ + 1/R₂,  U = const", "Ω"],
      ["To'liq zanjir uchun Om qonuni", "I = ε / (R + r)", "A"],
      ["Elektr quvvati", "P = UI = I²R = U²/R", "W"],
      ["Joul–Lens qonuni", "Q = I²Rt", "J"],
      ["Tok ishi", "A = UIt", "J"],
    ]},
    { title: "Magnetizm", items: [
      ["Amper kuchi", "F = B·I·l·sinα", "N"],
      ["Lorens kuchi", "F = q·v·B·sinα", "N"],
      ["Magnit oqimi", "Φ = B·S·cosα", "Wb"],
      ["Induksiya EYuK (Faradey)", "ε = −ΔΦ / Δt", "V"],
      ["Harakatlanuvchi o'tkazgichda EYuK", "ε = B·l·v·sinα", "V"],
      ["O'zinduksiya EYuK", "ε = −L·ΔI / Δt", "V"],
      ["Magnit maydon energiyasi", "W = LI² / 2", "J"],
      ["Zaryad aylana radiusi", "R = mv / (qB)", "m"],
    ]},
    { title: "Tebranishlar va to'lqinlar", items: [
      ["Garmonik tebranish", "x = A·cos(ωt + φ₀)", "m"],
      ["Chastota va davr", "f = 1/T,  ω = 2πf", "Hz,  rad/s"],
      ["Prujinali mayatnik davri", "T = 2π√(m/k)", "s"],
      ["Matematik mayatnik davri", "T = 2π√(l/g)", "s"],
      ["Tebranish konturi (Tomson)", "T = 2π√(LC)", "s"],
      ["O'zgaruvchan tok: ta'sir qiymati", "I = Iₘ/√2,  U = Uₘ/√2", "A,  V"],
      ["Induktiv qarshilik", "X_L = ωL", "Ω"],
      ["Sig'im qarshiligi", "X_C = 1 / (ωC)", "Ω"],
      ["To'liq qarshilik", "Z = √(R² + (X_L − X_C)²)", "Ω"],
      ["Transformator", "U₁/U₂ = N₁/N₂ = I₂/I₁", "—"],
      ["To'lqin tezligi", "v = λ·f = λ/T", "m/s"],
    ]},
    { title: "Optika", items: [
      ["Yorug'lik sindirish ko'rsatkichi", "n = c / v = sinα / sinβ", "—"],
      ["To'liq ichki qaytish", "sinα₀ = 1 / n", "—"],
      ["Yupqa linza formulasi", "1/F = 1/d + 1/f", "1/m"],
      ["Linzaning optik kuchi", "D = 1/F", "dptr"],
      ["Chiziqli kattalashtirish", "Γ = f / d = H / h", "—"],
      ["Interferensiya maksimumi", "Δ = kλ", "m"],
      ["Difraksion panjara", "d·sinφ = kλ", "m"],
    ]},
    { title: "Kvant va atom fizikasi", items: [
      ["Foton energiyasi", "E = hν = hc / λ,  h = 6,63·10⁻³⁴", "J"],
      ["Foton impulsi", "p = h / λ", "kg·m/s"],
      ["Fotoeffekt (Eynshteyn)", "hν = A_chiq + mv²/2", "J"],
      ["Fotoeffektning qizil chegarasi", "ν_min = A_chiq / h", "Hz"],
      ["Bor: vodorod sathlari", "Eₙ = −13,6 / n²", "eV"],
      ["Foton nurlanishi", "hν = Eₘ − Eₙ", "J"],
      ["Energiya birligi", "1 eV = 1,6·10⁻¹⁹", "J"],
    ]},
    { title: "Yadro fizikasi va nisbiylik", items: [
      ["Yadro tarkibi", "A = Z + N", "—"],
      ["Massa defekti", "Δm = Z·mₚ + N·mₙ − m(yadro)", "kg  (a.m.b.)"],
      ["Bog'lanish energiyasi", "E = Δm·c²", "J"],
      ["Radioaktiv yemirilish", "N = N₀·2^(−t/T)", "—"],
      ["Alfa-yemirilish", "(A, Z) → (A−4, Z−2) + ⁴₂He", "—"],
      ["Beta-minus yemirilish", "(A, Z) → (A, Z+1) + e⁻", "—"],
      ["Massa va energiya", "E = mc²,  c = 3·10⁸", "J,  m/s"],
      ["1 a.m.b. ekvivalenti", "1 a.m.b. = 931,5", "MeV"],
    ]},
    { title: "Doimiylar va ko'paytiruvchilar", items: [
      ["Erkin tushish tezlanishi", "g = 9,8 ≈ 10", "m/s²"],
      ["Yorug'lik tezligi", "c = 3·10⁸", "m/s"],
      ["Gravitatsiya doimiysi", "G = 6,67·10⁻¹¹", "N·m²/kg²"],
      ["Suvning solishtirma issiqlik sig'imi", "c = 4200", "J/(kg·°C)"],
      ["Elementar zaryad", "e = 1,6·10⁻¹⁹", "C"],
      ["Elektron massasi", "mₑ = 9,1·10⁻³¹", "kg"],
      ["Prefikslar", "k=10³, M=10⁶, G=10⁹, m=10⁻³, μ=10⁻⁶, n=10⁻⁹", "—"],
    ]},
  ];

  function buildFormulaBody() {
    const isPhysics = subject === "physics";
    const groups = isPhysics ? PHYSICS_FORMULA_GROUPS : MATH_FORMULA_GROUPS;
    return `
      <div class="fs-search-row">
        <input type="search" class="fs-search" placeholder="Formulani qidirish…" aria-label="Formulani qidirish" autocomplete="off">
      </div>
      <div class="formula-sheet-body">` + groups.map((group) => `
      <section class="formula-group">
        <h4>${esc(group.title)}</h4>
        <table class="formula-table">
          <thead><tr><th>Nima</th><th>Formula</th>${isPhysics ? "<th>Birlik</th>" : ""}</tr></thead>
          <tbody>
            ${group.items.map((row) => `<tr><td>${esc(row[0])}</td><td class="formula-expr">${esc(row[1])}</td>${isPhysics ? `<td class="formula-unit">${esc(row[2] || "")}</td>` : ""}</tr>`).join("")}
          </tbody>
        </table>
      </section>`).join("") + `</div>`;
  }

  function wireFormulaSearch(root) {
    const input = root.querySelector(".fs-search");
    if (!input) return;
    input.addEventListener("input", () => {
      const q = input.value.trim().toLowerCase();
      root.querySelectorAll(".formula-group").forEach((group) => {
        let any = false;
        group.querySelectorAll("tbody tr").forEach((tr) => {
          const hit = !q || tr.textContent.toLowerCase().includes(q);
          tr.hidden = !hit;
          if (hit) any = true;
        });
        group.hidden = !any;
      });
    });
  }

  // ===================== MENDELEYEV DAVRIY JADVALI =====================
  // Har bir yozuv: [tartib raqami, belgisi, o'zbekcha nomi, atom massasi, davr, guruh, kategoriya]
  const ELEMENTS = [
    [1,"H","Vodorod",1.008,1,1,"nonmetal"],[2,"He","Geliy",4.003,1,18,"noble"],
    [3,"Li","Litiy",6.94,2,1,"alkali"],[4,"Be","Berilliy",9.012,2,2,"alkaline"],
    [5,"B","Bor",10.81,2,13,"metalloid"],[6,"C","Uglerod",12.011,2,14,"nonmetal"],
    [7,"N","Azot",14.007,2,15,"nonmetal"],[8,"O","Kislorod",15.999,2,16,"nonmetal"],
    [9,"F","Ftor",18.998,2,17,"halogen"],[10,"Ne","Neon",20.180,2,18,"noble"],
    [11,"Na","Natriy",22.990,3,1,"alkali"],[12,"Mg","Magniy",24.305,3,2,"alkaline"],
    [13,"Al","Alyuminiy",26.982,3,13,"post-transition"],[14,"Si","Kremniy",28.085,3,14,"metalloid"],
    [15,"P","Fosfor",30.974,3,15,"nonmetal"],[16,"S","Oltingugurt",32.06,3,16,"nonmetal"],
    [17,"Cl","Xlor",35.45,3,17,"halogen"],[18,"Ar","Argon",39.948,3,18,"noble"],
    [19,"K","Kaliy",39.098,4,1,"alkali"],[20,"Ca","Kaltsiy",40.078,4,2,"alkaline"],
    [21,"Sc","Skandiy",44.956,4,3,"transition"],[22,"Ti","Titan",47.867,4,4,"transition"],
    [23,"V","Vanadiy",50.942,4,5,"transition"],[24,"Cr","Xrom",51.996,4,6,"transition"],
    [25,"Mn","Marganets",54.938,4,7,"transition"],[26,"Fe","Temir",55.845,4,8,"transition"],
    [27,"Co","Kobalt",58.933,4,9,"transition"],[28,"Ni","Nikel",58.693,4,10,"transition"],
    [29,"Cu","Mis",63.546,4,11,"transition"],[30,"Zn","Rux",65.38,4,12,"transition"],
    [31,"Ga","Galliy",69.723,4,13,"post-transition"],[32,"Ge","German",72.630,4,14,"metalloid"],
    [33,"As","Mishyak",74.922,4,15,"metalloid"],[34,"Se","Selen",78.971,4,16,"nonmetal"],
    [35,"Br","Brom",79.904,4,17,"halogen"],[36,"Kr","Kripton",83.798,4,18,"noble"],
    [37,"Rb","Rubidiy",85.468,5,1,"alkali"],[38,"Sr","Stronsiy",87.62,5,2,"alkaline"],
    [39,"Y","Ittriy",88.906,5,3,"transition"],[40,"Zr","Sirkoniy",91.224,5,4,"transition"],
    [41,"Nb","Niobiy",92.906,5,5,"transition"],[42,"Mo","Molibden",95.95,5,6,"transition"],
    [43,"Tc","Texnetsiy",98,5,7,"transition"],[44,"Ru","Ruteniy",101.07,5,8,"transition"],
    [45,"Rh","Rodiy",102.906,5,9,"transition"],[46,"Pd","Palladiy",106.42,5,10,"transition"],
    [47,"Ag","Kumush",107.868,5,11,"transition"],[48,"Cd","Kadmiy",112.414,5,12,"transition"],
    [49,"In","Indiy",114.818,5,13,"post-transition"],[50,"Sn","Qalay",118.710,5,14,"post-transition"],
    [51,"Sb","Surma",121.760,5,15,"metalloid"],[52,"Te","Tellur",127.60,5,16,"metalloid"],
    [53,"I","Yod",126.904,5,17,"halogen"],[54,"Xe","Ksenon",131.293,5,18,"noble"],
    [55,"Cs","Seziy",132.905,6,1,"alkali"],[56,"Ba","Bariy",137.327,6,2,"alkaline"],
    [72,"Hf","Gafniy",178.49,6,4,"transition"],[73,"Ta","Tantal",180.948,6,5,"transition"],
    [74,"W","Volfram",183.84,6,6,"transition"],[75,"Re","Reniy",186.207,6,7,"transition"],
    [76,"Os","Osmiy",190.23,6,8,"transition"],[77,"Ir","Iridiy",192.217,6,9,"transition"],
    [78,"Pt","Platina",195.085,6,10,"transition"],[79,"Au","Oltin",196.967,6,11,"transition"],
    [80,"Hg","Simob",200.592,6,12,"transition"],[81,"Tl","Talliy",204.38,6,13,"post-transition"],
    [82,"Pb","Qo'rg'oshin",207.2,6,14,"post-transition"],[83,"Bi","Vismut",208.980,6,15,"post-transition"],
    [84,"Po","Poloniy",209,6,16,"post-transition"],[85,"At","Astat",210,6,17,"halogen"],
    [86,"Rn","Radon",222,6,18,"noble"],
    [87,"Fr","Fransiy",223,7,1,"alkali"],[88,"Ra","Radiy",226,7,2,"alkaline"],
    [104,"Rf","Rezerfordiy",267,7,4,"transition"],[105,"Db","Dubniy",268,7,5,"transition"],
    [106,"Sg","Siborgiy",269,7,6,"transition"],[107,"Bh","Boriy",270,7,7,"transition"],
    [108,"Hs","Xassiy",269,7,8,"transition"],[109,"Mt","Meytneriy",278,7,9,"transition"],
    [110,"Ds","Darmshtatiy",281,7,10,"transition"],[111,"Rg","Rentgeniy",282,7,11,"transition"],
    [112,"Cn","Kopernitsiy",285,7,12,"transition"],[113,"Nh","Nihoniy",286,7,13,"post-transition"],
    [114,"Fl","Flerovyum",289,7,14,"post-transition"],[115,"Mc","Moskoviy",290,7,15,"post-transition"],
    [116,"Lv","Livermoriy",293,7,16,"post-transition"],[117,"Ts","Tennessin",294,7,17,"halogen"],
    [118,"Og","Oganeson",294,7,18,"noble"],
    // Lantanoidlar (8-qator sifatida ko'rsatiladi, guruh 3 dan boshlab)
    [57,"La","Lantan",138.905,8,3,"lanthanide"],[58,"Ce","Seriy",140.116,8,4,"lanthanide"],
    [59,"Pr","Praseodim",140.908,8,5,"lanthanide"],[60,"Nd","Neodim",144.242,8,6,"lanthanide"],
    [61,"Pm","Prometiy",145,8,7,"lanthanide"],[62,"Sm","Samariy",150.36,8,8,"lanthanide"],
    [63,"Eu","Yevropiy",151.964,8,9,"lanthanide"],[64,"Gd","Gadoliniy",157.25,8,10,"lanthanide"],
    [65,"Tb","Terbiy",158.925,8,11,"lanthanide"],[66,"Dy","Disproziy",162.500,8,12,"lanthanide"],
    [67,"Ho","Golmiy",164.930,8,13,"lanthanide"],[68,"Er","Erbiy",167.259,8,14,"lanthanide"],
    [69,"Tm","Tuliy",168.934,8,15,"lanthanide"],[70,"Yb","Itterbiy",173.045,8,16,"lanthanide"],
    [71,"Lu","Lyutetsiy",174.967,8,17,"lanthanide"],
    // Aktinoidlar (9-qator)
    [89,"Ac","Aktiniy",227,9,3,"actinide"],[90,"Th","Toriy",232.038,9,4,"actinide"],
    [91,"Pa","Protaktiniy",231.036,9,5,"actinide"],[92,"U","Uran",238.029,9,6,"actinide"],
    [93,"Np","Neptuniy",237,9,7,"actinide"],[94,"Pu","Plutoniy",244,9,8,"actinide"],
    [95,"Am","Amerisiy",243,9,9,"actinide"],[96,"Cm","Kyuriy",247,9,10,"actinide"],
    [97,"Bk","Berkeliy",247,9,11,"actinide"],[98,"Cf","Kaliforniy",251,9,12,"actinide"],
    [99,"Es","Eynshteyniy",252,9,13,"actinide"],[100,"Fm","Fermiy",257,9,14,"actinide"],
    [101,"Md","Mendeleviy",258,9,15,"actinide"],[102,"No","Nobeliy",259,9,16,"actinide"],
    [103,"Lr","Lourensiy",262,9,17,"actinide"],
  ];

  const CATEGORY_LABELS = {
    alkali: "Ishqoriy metallar", alkaline: "Ishqoriy-yer metallar", transition: "O'tish metallari",
    "post-transition": "Boshqa metallar", metalloid: "Yarim metallar", nonmetal: "Nometallar",
    halogen: "Galogenlar", noble: "Inert (zotli) gazlar", lanthanide: "Lantanoidlar", actinide: "Aktinoidlar",
  };

  const GASES = new Set([1, 2, 7, 8, 9, 10, 17, 18, 36, 54, 86]);
  const LIQUIDS = new Set([35, 80]);
  const SUPERSCRIPT = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" };
  const sup = (n) => String(n).split("").map((d) => SUPERSCRIPT[d]).join("");

  // Elektron konfiguratsiya: Madelung qoidasi + ma'lum istisnolar (ular qisqa yozuvda).
  const ORBITALS = [[1,"s",2],[2,"s",2],[2,"p",6],[3,"s",2],[3,"p",6],[4,"s",2],[3,"d",10],[4,"p",6],[5,"s",2],[4,"d",10],[5,"p",6],[6,"s",2],[4,"f",14],[5,"d",10],[6,"p",6],[7,"s",2],[5,"f",14],[6,"d",10],[7,"p",6]];
  const NOBLE_CORES = [[86, "Rn"], [54, "Xe"], [36, "Kr"], [18, "Ar"], [10, "Ne"], [2, "He"]];
  const CONFIG_EXCEPTIONS = {
    24: "[Ar] 3d⁵ 4s¹", 29: "[Ar] 3d¹⁰ 4s¹", 41: "[Kr] 4d⁴ 5s¹", 42: "[Kr] 4d⁵ 5s¹", 44: "[Kr] 4d⁷ 5s¹",
    45: "[Kr] 4d⁸ 5s¹", 46: "[Kr] 4d¹⁰", 47: "[Kr] 4d¹⁰ 5s¹", 57: "[Xe] 5d¹ 6s²", 58: "[Xe] 4f¹ 5d¹ 6s²",
    64: "[Xe] 4f⁷ 5d¹ 6s²", 78: "[Xe] 4f¹⁴ 5d⁹ 6s¹", 79: "[Xe] 4f¹⁴ 5d¹⁰ 6s¹", 89: "[Rn] 6d¹ 7s²",
    90: "[Rn] 6d² 7s²", 91: "[Rn] 5f² 6d¹ 7s²", 92: "[Rn] 5f³ 6d¹ 7s²", 93: "[Rn] 5f⁴ 6d¹ 7s²",
    96: "[Rn] 5f⁷ 6d¹ 7s²", 103: "[Rn] 5f¹⁴ 7s² 7p¹",
  };

  function electronConfig(z) {
    if (CONFIG_EXCEPTIONS[z]) return CONFIG_EXCEPTIONS[z];
    const filled = [];
    let left = z;
    for (const [n, l, cap] of ORBITALS) {
      if (left <= 0) break;
      const e = Math.min(cap, left);
      filled.push({ n, l, e });
      left -= e;
    }
    const core = NOBLE_CORES.find(([cz]) => cz < z);
    let coreElectrons = 0;
    const rest = [];
    for (const orb of filled) {
      if (core && coreElectrons + orb.e <= core[0]) { coreElectrons += orb.e; continue; }
      rest.push(orb);
    }
    const lOrder = { s: 0, p: 1, d: 2, f: 3 };
    rest.sort((a, b) => a.n - b.n || lOrder[a.l] - lOrder[b.l]);
    const text = rest.map((o) => `${o.n}${o.l}${sup(o.e)}`).join(" ");
    return core ? `[${core[1]}] ${text}` : text;
  }

  function blockOf(group, cat) {
    if (cat === "lanthanide" || cat === "actinide") return "f";
    if (group <= 2) return "s";
    if (group >= 13) return "p";
    return "d";
  }

  function stateOf(z) {
    if (GASES.has(z)) return "Gaz";
    if (LIQUIDS.has(z)) return "Suyuqlik";
    if (z >= 104) return "Noma'lum (sintetik)";
    return "Qattiq";
  }

  // Panel: 1-qator guruh raqamlari, 2–8 davrlar, 9 — bo'sh qator, 10–11 f-elementlar.
  const GRID_ROW = (period) => (period <= 7 ? period + 1 : period + 2);

  function buildPeriodicTableBody() {
    const groupLabels = Array.from({ length: 18 }, (_, i) =>
      `<span class="pt-group-label" style="grid-column:${i + 1}; grid-row:1;">${i + 1}</span>`).join("");

    const cells = ELEMENTS.map((el) => {
      const [num, sym, name, mass, period, group, cat] = el;
      return `<button type="button" class="pt-element pt-cat-${cat}" style="grid-column:${group}; grid-row:${GRID_ROW(period)};"
        aria-label="${esc(name)}, ${num}" title="${esc(name)}, ${num}" data-num="${num}" data-cat="${cat}">
        <span class="pt-element-num">${num}</span>
        <span class="pt-element-sym">${sym}</span>
        <span class="pt-element-mass">${mass}</span>
      </button>`;
    }).join("");

    const markers = `
      <div class="pt-marker pt-cat-lanthanide" style="grid-column:3; grid-row:7;" aria-hidden="true">57–71</div>
      <div class="pt-marker pt-cat-actinide" style="grid-column:3; grid-row:8;" aria-hidden="true">89–103</div>`;

    const legend = Object.keys(CATEGORY_LABELS).map((cat) =>
      `<button type="button" class="pt-legend-item" data-cat="${cat}"><i class="pt-cat-${cat}"></i>${CATEGORY_LABELS[cat]}</button>`
    ).join("");

    return `
      <div class="pt-toolbar">
        <input type="search" class="fs-search pt-search" placeholder="Element qidirish (nomi, belgisi yoki raqami)…" aria-label="Element qidirish" autocomplete="off">
        <span class="pt-hint">Elementni bosing — tafsilotlari ko'rinadi</span>
      </div>
      <div class="periodic-table-wrap">
        <div class="periodic-table-grid">${groupLabels}${cells}${markers}</div>
      </div>
      <div class="periodic-table-legend">${legend}</div>
      <div class="pt-detail-panel" id="pt-detail-panel">
        <p class="pt-detail-empty">Tafsilotlarni ko'rish uchun jadvaldan elementni tanlang.</p>
      </div>`;
  }

  function showElement(root, num) {
    const el = ELEMENTS.find((e) => e[0] === num);
    if (!el) return;
    const [z, sym, name, mass, period, group, cat] = el;
    const massNumber = Math.round(mass);
    const neutrons = massNumber - z;
    const isF = cat === "lanthanide" || cat === "actinide";
    const groupText = isF ? "—  (f-elementlar)" : group;
    const periodText = isF ? (cat === "lanthanide" ? 6 : 7) : period;
    const panel = root.querySelector("#pt-detail-panel");
    panel.innerHTML = `
      <div class="pt-detail-symbol pt-cat-${cat}"><small>${z}</small>${sym}<em>${mass}</em></div>
      <div class="pt-detail-info">
        <div class="pt-detail-name">${esc(name)} <span>(${sym})</span></div>
        <div class="pt-detail-grid">
          <div><b>Protonlar (p⁺)</b>${z}</div>
          <div><b>Elektronlar (e⁻)</b>${z} <small>(neytral atom)</small></div>
          <div><b>Neytronlar (n⁰)</b>${neutrons} <small>(A − Z)</small></div>
          <div><b>Massa soni (A)</b>${massNumber}</div>
          <div><b>Atom massasi</b>${mass} <small>a.m.b.</small></div>
          <div><b>Davr</b>${periodText}</div>
          <div><b>Guruh</b>${groupText}</div>
          <div><b>Blok</b>${blockOf(group, cat)}-element</div>
          <div><b>Turi</b>${CATEGORY_LABELS[cat]}</div>
          <div><b>Holati (25 °C)</b>${stateOf(z)}</div>
          <div class="pt-detail-wide"><b>Elektron konfiguratsiya</b><span class="pt-config">${electronConfig(z)}</span></div>
        </div>
      </div>`;
  }

  function wirePeriodicTableEvents(root) {
    const buttons = Array.from(root.querySelectorAll(".pt-element"));
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        root.querySelectorAll(".pt-element.is-active").forEach((b) => b.classList.remove("is-active"));
        btn.classList.add("is-active");
        showElement(root, parseInt(btn.dataset.num, 10));
      });
    });

    const search = root.querySelector(".pt-search");
    const legendItems = Array.from(root.querySelectorAll(".pt-legend-item"));
    let activeCat = null;

    function applyFilters() {
      const q = (search.value || "").trim().toLowerCase();
      buttons.forEach((btn) => {
        const el = ELEMENTS.find((e) => e[0] === parseInt(btn.dataset.num, 10));
        const matchesText = !q || String(el[0]) === q || el[1].toLowerCase().startsWith(q) || el[2].toLowerCase().includes(q);
        const matchesCat = !activeCat || el[6] === activeCat;
        btn.classList.toggle("pt-dim", !(matchesText && matchesCat));
      });
    }
    search.addEventListener("input", applyFilters);
    legendItems.forEach((item) => {
      item.addEventListener("click", () => {
        activeCat = activeCat === item.dataset.cat ? null : item.dataset.cat;
        legendItems.forEach((i) => i.classList.toggle("is-active", i.dataset.cat === activeCat));
        applyFilters();
      });
    });
  }

  // ===================== TUGMA VA OYNA =====================
  const ICONS = {
    sigma: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 5H7l6 7-6 7h11"/></svg>',
    table: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg>',
  };

  // ===================== BIOLOGIYA YORDAMCHISI =====================
  const CODON_AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG";
  const CODON_BASES = "UCAG";
  const AA_INFO = {
    F: ["Fen", "Fenilalanin", "np"], L: ["Ley", "Leysin", "np"], S: ["Ser", "Serin", "po"], Y: ["Tir", "Tirozin", "po"],
    C: ["Sis", "Sistein", "po"], W: ["Tri", "Triptofan", "np"], P: ["Pro", "Prolin", "np"], H: ["Gis", "Gistidin", "ba"],
    Q: ["Gln", "Glutamin", "po"], R: ["Arg", "Arginin", "ba"], I: ["Ile", "Izoleysin", "np"], M: ["Met", "Metionin (START)", "np"],
    T: ["Tre", "Treonin", "po"], N: ["Asn", "Asparagin", "po"], K: ["Liz", "Lizin", "ba"], V: ["Val", "Valin", "np"],
    A: ["Ala", "Alanin", "np"], D: ["Asp", "Asparagin kislota", "ac"], E: ["Glu", "Glutamin kislota", "ac"], G: ["Gli", "Glitsin", "np"],
    "*": ["STOP", "To'xtash kodoni", "st"],
  };
  const AA_CLASS_LABEL = { np: "Qutbsiz", po: "Qutbli", ba: "Asosli (+)", ac: "Kislotali (−)", st: "STOP" };

  function buildCodonBody() {
    const idx = (a, b, c) => a * 16 + b * 4 + c;
    let html = '<p class="bio-note">mRNK kodonlari (5′→3′). Chap — 1-asos, tepada — 2-asos, o\'ngda — 3-asos. Kodon bosilsa aminokislota ko\'rsatiladi.</p>';
    html += '<div class="codon-legend">' + Object.keys(AA_CLASS_LABEL).map((k) => `<span class="codon-chip codon-${k}">${AA_CLASS_LABEL[k]}</span>`).join("") + "</div>";
    html += '<div class="codon-detail" id="codon-detail" aria-live="polite">Kodonni tanlang</div>';
    html += '<table class="codon-table"><thead><tr><th>1-asos</th>' + [...CODON_BASES].map((b) => `<th>${b}</th>`).join("") + "<th>3-asos</th></tr></thead><tbody>";
    for (let a = 0; a < 4; a++) {
      for (let c = 0; c < 4; c++) {
        html += "<tr>";
        if (c === 0) html += `<th rowspan="4" class="codon-first">${CODON_BASES[a]}</th>`;
        for (let b = 0; b < 4; b++) {
          const aa = CODON_AA[idx(a, b, c)];
          const info = AA_INFO[aa];
          const codon = CODON_BASES[a] + CODON_BASES[b] + CODON_BASES[c];
          html += `<td><button type="button" class="codon-btn codon-${info[2]}" data-codon="${codon}" data-name="${esc(info[1])}" data-abbr="${esc(info[0])}" aria-label="${codon} — ${esc(info[1])}">${codon}<small>${esc(info[0])}</small></button></td>`;
        }
        html += `<th class="codon-third">${CODON_BASES[c]}</th></tr>`;
      }
    }
    return html + "</tbody></table>";
  }

  const BIO_REFERENCE = [
    { title: "Genetika (Mendel qonunlari)", items: [
      ["I qonun (bir xillik)", "AA × aa → barchasi Aa (F₁ bir xil)"],
      ["II qonun (ajralish)", "Aa × Aa → fenotip 3:1, genotip 1:2:1"],
      ["Tahliliy chatishtirish", "Aa × aa → 1:1; AA × aa → barchasi Aa"],
      ["Digibrid chatishtirish", "AaBb × AaBb → fenotip 9:3:3:1"],
      ["To'liq bo'lmagan dominantlik", "Aa × Aa → 1:2:1 (fenotip ham)"],
      ["Gametalar xili", "2ⁿ (n — geterozigota genlar soni)"],
      ["Genotiplar soni (F₂, n juft gen)", "3ⁿ"],
      ["Fenotiplar soni (F₂, to'liq dominant.)", "2ⁿ"],
      ["Qon guruhlari", "I: ii · II: IᴬIᴬ, Iᴬi · III: IᴮIᴮ, Iᴮi · IV: IᴬIᴮ"],
      ["Xardi–Vaynberg", "p + q = 1;  p² + 2pq + q² = 1"],
    ]},
    { title: "Molekulyar biologiya", items: [
      ["Chargaff qoidasi", "A = T,  G = C;  A+G = T+C"],
      ["Komplementarlik", "A–T (2 ta H-bog'), G–C (3 ta H-bog')"],
      ["RNKda", "A–U,  G–C (timin o'rniga uratsil)"],
      ["Bitta nukleotid uzunligi", "0,34 nm"],
      ["DNK spirali bir burami", "10 juft nukleotid = 3,4 nm"],
      ["Nukleotidning o'rtacha massasi", "≈ 345 (a.m.b.)"],
      ["Aminokislotaning o'rtacha massasi", "≈ 110 (a.m.b.)"],
      ["Genetik kod", "triplet: 1 aminokislota = 3 nukleotid (kodon)"],
      ["Oqsil uzunligi", "aminokislotalar = mRNK nukleotidlari ÷ 3 (stop-kodonsiz)"],
      ["Boshlang'ich / to'xtash kodonlari", "AUG (start);  UAA, UAG, UGA (stop)"],
    ]},
    { title: "Hujayra va bo'linish", items: [
      ["Mitoz", "2n → 2n (2 ta hujayra, genetik bir xil)"],
      ["Meyoz", "2n → n (4 ta gaploid hujayra)"],
      ["Interfaza", "G₁ → S (DNK ikkilanadi) → G₂"],
      ["Mitoz fazalari", "profaza → metafaza → anafaza → telofaza"],
      ["Anafazada xromosomalar", "2n → 4n (xromatidlar ajraladi)"],
      ["Mitoxondriya vazifasi", "ATF sintezi (nafas olish)"],
      ["Ribosoma / EPT / Golji", "oqsil sintezi / tashish / modifikatsiya va ajratish"],
    ]},
    { title: "Energiya almashinuvi", items: [
      ["Fotosintez", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  (yorug'lik, xlorofill)"],
      ["Nafas olish (aerob)", "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 38 ATF (darslik)"],
      ["Glikoliz", "1 glyukoza → 2 PVK + 2 ATF (sitoplazma)"],
      ["Bijg'ish (anaerob)", "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ + 2 ATF"],
      ["ATF gidrolizi", "ATF → ADF + F  (≈ 40 kJ/mol energiya)"],
      ["Energiya piramidasi", "har keyingi bosqichga ≈ 10% o'tadi (Lindeman qoidasi)"],
    ]},
    { title: "Evolyutsiya va ekologiya", items: [
      ["Evolyutsiya omillari", "irsiyat, o'zgaruvchanlik, tabiiy tanlanish, kurash"],
      ["Gomologik a'zolar", "tuzilishi bir, vazifasi har xil (qush qanoti — odam qo'li)"],
      ["Analogik a'zolar", "vazifasi bir, tuzilishi har xil (hasharot va qush qanoti)"],
      ["Oziq zanjiri", "ishlab chiqaruvchi → iste'molchi → parchalovchi"],
    ]},
  ];

  function buildBioReferenceBody() {
    return '<div class="formula-sheet-body">' + BIO_REFERENCE.map((group) => `
      <section class="formula-group">
        <h4>${esc(group.title)}</h4>
        <table class="formula-table">
          <thead><tr><th>Nima</th><th>Qoida / formula</th></tr></thead>
          <tbody>${group.items.map((row) => `<tr><td>${esc(row[0])}</td><td class="formula-expr">${esc(row[1])}</td></tr>`).join("")}</tbody>
        </table>
      </section>`).join("") + "</div>";
  }

  function buildBiologyBody() {
    return `
      <div class="bio-tabs" role="tablist">
        <button type="button" role="tab" class="bio-tab active" data-pane="pt" aria-selected="true">Mendeleyev jadvali</button>
        <button type="button" role="tab" class="bio-tab" data-pane="codon" aria-selected="false">Genetik kod</button>
        <button type="button" role="tab" class="bio-tab" data-pane="ref" aria-selected="false">Qoidalar va formulalar</button>
      </div>
      <div class="bio-pane" data-pane="pt">${buildPeriodicTableBody()}</div>
      <div class="bio-pane" data-pane="codon" hidden>${buildCodonBody()}</div>
      <div class="bio-pane" data-pane="ref" hidden>${buildBioReferenceBody()}</div>`;
  }

  function wireBiologyTabs(root) {
    const tabs = root.querySelectorAll(".bio-tab");
    tabs.forEach((tab) => tab.addEventListener("click", () => {
      tabs.forEach((t) => { t.classList.toggle("active", t === tab); t.setAttribute("aria-selected", t === tab ? "true" : "false"); });
      root.querySelectorAll(".bio-pane").forEach((p) => { p.hidden = p.dataset.pane !== tab.dataset.pane; });
    }));
    const detail = root.querySelector("#codon-detail");
    root.querySelectorAll(".codon-btn").forEach((btn) => btn.addEventListener("click", () => {
      if (detail) detail.innerHTML = `<b>${esc(btn.dataset.codon)}</b> → ${esc(btn.dataset.name)} (${esc(btn.dataset.abbr)})`;
    }));
  }


  const toggleBtn = document.createElement("button");
  toggleBtn.type = "button";
  toggleBtn.id = "formula-sheet-toggle";
  toggleBtn.className = "formula-sheet-toggle";
  toggleBtn.title = config.title;
  toggleBtn.setAttribute("aria-label", config.title);
  toggleBtn.innerHTML = `${ICONS[config.icon]}<span>${config.label}</span>`;

  const overlay = document.createElement("aside");
  overlay.id = "formula-sheet-overlay";
  overlay.className = "formula-sheet-overlay fs-drawer";
  overlay.setAttribute("role", "complementary");
  overlay.setAttribute("aria-label", config.title);
  overlay.setAttribute("aria-hidden", "true");
  overlay.innerHTML = `
    <div class="formula-sheet-card${config.periodic ? " periodic-table-card" : " formula-wide-card"}">
      <div class="formula-sheet-header">
        <h3>${config.title}</h3>
        <button type="button" class="formula-sheet-close" aria-label="Yopish">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>
      </div>
      <p class="formula-sheet-sub">Test davomida ochiq tursin — savolga javob berganda yopilmaydi. Yopish uchun yana shu tugmani bosing.</p>
      <div class="formula-sheet-scroll">${config.builder()}</div>
    </div>`;

  function mount() {
    const timerEl = document.getElementById("quiz-timer");
    if (timerEl && timerEl.parentNode) {
      timerEl.parentNode.insertBefore(toggleBtn, timerEl);
    } else {
      document.body.appendChild(toggleBtn);
    }
    document.body.appendChild(overlay);
    if (config.periodic) wirePeriodicTableEvents(overlay);
    else wireFormulaSearch(overlay);
    if (config.tabs) wireBiologyTabs(overlay);

    function syncTop() {
      const header = document.querySelector(".site-header");
      const h = header ? Math.round(header.getBoundingClientRect().bottom) : 0;
      document.documentElement.style.setProperty("--fs-top", Math.max(h, 0) + "px");
    }
    function setOpen(open) {
      syncTop();
      overlay.classList.toggle("is-open", open);
      overlay.setAttribute("aria-hidden", open ? "false" : "true");
      if ("inert" in overlay) overlay.inert = !open;
      document.body.classList.toggle("fs-open", open);
      toggleBtn.classList.toggle("is-active", open);
      toggleBtn.setAttribute("aria-pressed", open ? "true" : "false");
    }
    setOpen(false);
    toggleBtn.addEventListener("click", () => setOpen(!overlay.classList.contains("is-open")));
    overlay.querySelector(".formula-sheet-close").addEventListener("click", () => setOpen(false));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && overlay.classList.contains("is-open")) setOpen(false); });
    window.addEventListener("resize", syncTop);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
