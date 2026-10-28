"""Fizika: optika, nisbiylik, kvant, atom va yadro fizikasi (9- va 11-sinf)."""
import math
from ._dsl import C, O, M
from ._ph import N, ON, fmt
from . import figs_phys as F

h, c, e = 6.63e-34, 3e8, 1.6e-19
Q = {}

Q["P11.19"] = [
    C(1, "Yorug'lik qaytish qonuni?", "Tushish burchagi qaytish burchagiga teng", ["Tushish burchagi sinish burchagiga teng", "Qaytish burchagi 90°", "Burchaklar yig'indisi 180°"], "α = α'."),
    C(1, "Yorug'lik sinishi qonuni (Snellius)?", "n₁ sinα = n₂ sinβ", ["n₁ cosα = n₂ cosβ", "sinα = n·cosβ", "α = nβ"], "Ikki muhit chegarasi.", fig=F.refraction()),
    C(1, "Muhitning absolyut sindirish ko'rsatkichi formulasi?", "n = c / v", ["n = v / c", "n = c·v", "n = c − v"], "Yorug'lik tezligi nisbati."),
    N(2, "Yorug'lik havodan shishaga (n = 1,5) tushadi. α = 30° (sin = 0,5). sinβ?", 0.333, [0.75, 0.5, 1.5], "", "sinβ = sinα/n = 0,5/1,5.", fig=F.refraction(30, 19.5, "n = 1", "n = 1,5")),
    N(2, "Shishada (n = 1,5) yorug'lik tezligi (c = 3·10⁸)?", 2e8, [4.5e8, 3e8, 1.5e8], "m/s", "v = c/n."),
    N(3, "To'liq ichki qaytishning chegaraviy burchagi: shishadan (n = 2) havoga, sinα₀ = 1/n. α₀ (sin 30° = 0,5)?", 30, [60, 45, 90], "°", "sinα₀ = 0,5."),
    C(2, "To'liq ichki qaytish qachon yuz beradi?", "Zichroq muhitdan siyrakroq muhitga, burchak chegaraviydan katta bo'lganda", ["Siyrakdan zichga", "Hech qachon", "Faqat vakuumda"], "n₁ > n₂ va α > α₀."),
    C(2, "Yassi ko'zgudagi tasvir...", "mavhum, jism o'lchamiga teng, ko'zgu ortida", ["haqiqiy, kichik", "haqiqiy, katta", "mavhum, katta"], "Simmetrik."),
    ON(3, "Ko'zgudan 2 m masofada turgan odam o'z tasvirigacha necha metr uzoqlikda?", 4, "2·2."),
    ON(3, "Suv (n = 4/3) da yorug'lik tezligi necha 10⁸ m/s? (c = 3·10⁸)", 2.25, "v = 3/(4/3) = 2,25·10⁸."),
]

Q["P11.20"] = [
    C(1, "Yupqa linza formulasi?", "1/F = 1/d + 1/f", ["F = d + f", "1/F = d·f", "F = d/f"], "d — jismgacha, f — tasvirgacha."),
    C(1, "Optik kuch (D) formulasi va birligi?", "D = 1/F, dioptriya", ["D = F, metr", "D = F², joul", "D = 1/F, nyuton"], "1 dpt = 1/m."),
    N(2, "F = 0,25 m linza optik kuchi?", 4, [0.25, 2, 25], "dpt", "D = 1/F."),
    C(2, "Chizmada jism fokusdan uzoqda (d > F) — yig'uvchi linza tasviri qanday?", "Haqiqiy, teskari", ["Mavhum, to'g'ri", "Haqiqiy, to'g'ri", "Mavhum, teskari"], "d > F.", fig=F.lens(3, 6)),
    C(2, "Chizmada jism fokus ichida (d < F) — yig'uvchi linza tasviri qanday?", "Mavhum, to'g'ri, kattalashgan", ["Haqiqiy, teskari", "Mavhum, kichraygan", "Haqiqiy, to'g'ri"], "Lupa.", fig=F.lens(4, 2)),
    N(2, "F = 20 sm yig'uvchi linza, jism d = 30 sm da. Tasvirgacha f?", 60, [12, 6, 50], "sm", "1/f = 1/20 − 1/30 = 1/60."),
    N(3, "Shu holatda chiziqli kattalashtirish (Γ = f/d)?", 2, [0.5, 3, 1], "marta", "60/30."),
    C(2, "Sochuvchi linza tasviri har doim...", "mavhum, to'g'ri, kichraygan", ["haqiqiy, teskari", "haqiqiy, kattalashgan", "mavhum, kattalashgan"], "Sochuvchi linza.", fig=F.lens(4, 6, "div")),
    ON(3, "Yig'uvchi linza (F = 10 sm), jism d = 20 sm. Tasvir linzadan necha sm da?", 20, "1/f = 1/10 − 1/20 = 1/20."),
    ON(3, "Linzaning optik kuchi +2,5 dpt. Fokus masofa necha sm?", 40, "F = 1/2,5 = 0,4 m."),
]

Q["P11.21"] = [
    C(1, "Interferensiya maksimum sharti?", "Δ = kλ", ["Δ = (2k+1)λ/2", "Δ = λ/4", "Δ = 0 faqat"], "Yo'l farqi to'lqin uzunligining butun soniga teng."),
    C(1, "Interferensiya minimum sharti?", "Δ = (2k+1)λ/2", ["Δ = kλ", "Δ = kλ/2", "Δ = 2kλ"], "Yarim to'lqinlarning toq soni."),
    C(1, "Kogerent to'lqinlar...", "chastotasi bir xil va fazalar farqi doimiy", ["amplitudasi bir xil", "tezligi bir xil", "to'lqin uzunligi har xil"], "Ta'rif."),
    N(2, "λ = 600 nm to'lqinlar yo'l farqi 1,8 μm. Maksimumlar tartibi k?", 3, [2, 6, 1.8], "", "Δ/λ = 3."),
    N(3, "Difraksion panjara doimiysi d = 2 μm, λ = 500 nm. Birinchi tartibli maksimum: sinφ?", 0.25, [0.5, 1, 0.025], "", "sinφ = λ/d."),
    N(3, "Panjara 1 mm da 500 ta chiziqqa ega. Panjara doimiysi?", 2e-6, [5e-4, 2e-3, 5e-7], "m", "d = 1 mm/500 = 2 μm."),
    N(3, "d = 4 μm, λ = 500 nm. Kuzatiladigan eng yuqori tartibli maksimum (sinφ < 1)?", 7, [8, 4, 16], "", "kλ < d → k < 8 → k_max = 7."),
    C(2, "Yupqa moy pardasidagi ranglar nima sababdan?", "Interferensiya", ["Difraksiya", "Dispersiya faqat", "Qutblanish"], "Yo'l farqi."),
    ON(3, "Ikki kogerent manbadan nuqtagacha yo'l farqi 1,5 μm. λ = 500 nm bo'lsa, bu nuqtada nechanchi maksimum?", 3, "Δ/λ = 3 — maksimum."),
    ON(3, "Panjara doimiysi 5 μm, λ = 500 nm. 2-tartibli maksimum uchun sinφ nimaga teng?", 0.2, "sinφ = kλ/d = 2·0,5/5 = 0,2."),
]

Q["P11.22"] = [
    C(1, "Oq yorug'likning prizmada spektrga ajralishi nima deyiladi?", "Dispersiya", ["Interferensiya", "Difraksiya", "Qutblanish"], "Nyuton tajribasi."),
    C(1, "Prizmada eng ko'p og'adigan rang?", "Binafsha", ["Qizil", "Yashil", "Sariq"], "n binafsha uchun katta."),
    C(1, "Yorug'likning qutblanishi uning...", "ko'ndalang to'lqin ekanini isbotlaydi", ["bo'ylama ekanini", "zarracha ekanini", "tezligi cheksizligini"], "Faqat ko'ndalang to'lqinlar qutblanadi."),
    C(2, "Malus qonuni?", "I = I₀ cos²φ", ["I = I₀ cosφ", "I = I₀ sinφ", "I = I₀/φ"], "Analizator burchagi."),
    N(2, "Qutblangan nur analizatordan φ = 60° da o'tadi (cos 60° = 0,5). I₀ = 100 birlik. I?", 25, [50, 100, 12.5], "birlik", "100·0,25."),
    C(2, "Ko'rinadigan yorug'likdan to'lqin uzunligi kattaroq nurlanish?", "Infraqizil", ["Ultrabinafsha", "Rentgen", "Gamma"], "IQ."),
    C(2, "Qaysi nurlanish eng qisqa to'lqin uzunlikka ega?", "Gamma", ["Rentgen", "Ultrabinafsha", "Radio"], "Shkala."),
    ON(3, "Tabiiy nur ikki qutblagichdan o'tdi: biri 100% o'tkazadi (nurni qutblaydi), ikkinchisi 45° burchakda. Birinchidan keyin intensivlik 50 birlik. Yakuniy intensivlik necha birlik?", 25, "50·cos²45° = 25."),
    ON(3, "Yorug'lik qutblagichdan keyin analizatorga φ = 0° burchakda tushadi. I₀ = 80. Intensivlik necha?", 80, "cos²0 = 1."),
]

Q["P11.23"] = [
    C(1, "Maxsus nisbiylik nazariyasining ikkinchi postulati?", "Vakuumda yorug'lik tezligi barcha inersial sanoq sistemalarida bir xil", ["Yorug'lik tezligi manbaga bog'liq", "Hamma tezliklar nisbiy", "Vaqt absolyut"], "c = invariant."),
    C(1, "Eynshteyn massa–energiya formulasi?", "E = mc²", ["E = mv²/2", "E = mgh", "E = hν"], "Tinchlik energiyasi."),
    N(2, "1 mg modda to'liq energiyaga aylansa (c = 3·10⁸)?", 9e10, [9e13, 3e5, 9e7], "J", "10⁻⁶ kg·9·10¹⁶."),
    N(3, "Vaqt sekinlashishi: v = 0,6c bo'lgan kosmik kemadagi 8 s ning Yerdagi davomiyligi? (√(1−0,36) = 0,8)", 10, [6.4, 5, 13.3], "s", "τ = τ₀/0,8."),
    N(3, "v = 0,8c uzunlik qisqarishi: 10 m tinch uzunlik, harakatdagi uzunlik (√(1−0,64) = 0,6)?", 6, [8, 12.5, 4], "m", "l = l₀·0,6."),
    C(2, "Maykelson–Morli tajribasi nimani ko'rsatdi?", "Efir 'shamoli' yo'q, yorug'lik tezligi barcha yo'nalishda bir xil", ["Efir mavjud", "Yorug'lik tezligi cheksiz", "Yorug'lik zarracha"], "Salbiy natija."),
    C(2, "Nisbiylik nazariyasiga ko'ra jismni c tezlikka yetkazish uchun...", "cheksiz energiya kerak", ["kichik kuch yetarli", "energiya nol", "massa nolga teng"], "Massali jism uchun mumkin emas."),
    ON(3, "Tinch massasi 2 kg jismning tinchlik energiyasi necha ·10¹⁷ J? (c = 3·10⁸)", 1.8, "E = 2·9·10¹⁶ = 1,8·10¹⁷."),
    ON(3, "Elektron tinchlik energiyasi 0,511 MeV. Necha ·10⁻¹⁴ joul? (1 MeV = 1,6·10⁻¹³ J; yaxlitlab 3 xona)", 8.18, "0,511·1,6·10⁻¹³ = 8,176·10⁻¹⁴ ≈ 8,18·10⁻¹⁴ J."),
]

Q["P11.24"] = [
    C(1, "Plank gipotezasi?", "Nurlanish energiya porsiyalari — kvantlar bilan chiqadi", ["Energiya uzluksiz", "Nurlanish faqat to'lqin", "Energiya yo'qoladi"], "E = hν."),
    C(1, "Foton energiyasi?", "E = hν = hc/λ", ["E = mc", "E = h/ν", "E = hλ"], "Plank doimiysi h = 6,63·10⁻³⁴ J·s."),
    N(2, "ν = 5·10¹⁴ Hz foton energiyasi (h = 6,63·10⁻³⁴)?", 3.315e-19, [1.3e-48, 3.3e-20, 6.6e-19], "J", "hν."),
    N(2, "λ = 500 nm foton energiyasi (hc/λ)?", 3.978e-19, [1.3e-27, 3e-19, 5e-19], "J", "6,63e-34·3e8/5e-7 = 3,978e-19."),
    N(3, "Shu fotonning energiyasi eV da (e = 1,6·10⁻¹⁹)?", 2.49, [3.98, 0.4, 24.9], "eV", "3,978e-19/1,6e-19 = 2,486."),
    C(2, "Vin siljish qonuni: temperatura ortsa, nurlanish maksimumi...", "qisqa to'lqinlar tomon siljiydi", ["uzun to'lqinlar tomon", "joyida qoladi", "yo'qoladi"], "λ_max = b/T."),
    C(2, "Stefan–Bolsman qonuni: qora jism nurlanish quvvati...", "T⁴ ga proporsional", ["T ga proporsional", "T² ga", "T³ ga"], "P = σST⁴."),
    ON(3, "Temperatura 2 marta oshsa, qora jism nurlanish quvvati necha marta ortadi?", 16, "2⁴."),
    ON(3, "Foton chastotasi 3·10¹⁵ Hz. Energiyasi necha ·10⁻¹⁸ J? (h = 6,63·10⁻³⁴; yaxlitlab 2 xona)", 1.99, "6,63e-34·3e15 = 1,989e-18."),
]

Q["P11.25"] = [
    C(1, "Fotoeffekt uchun Eynshteyn tenglamasi?", "hν = A + E_k", ["hν = A − E_k", "hν = E_k/A", "ν = A·E_k"], "Energiya saqlanishi."),
    C(1, "Fotoeffektning qizil chegarasi nima?", "Eng kichik chastota (eng katta to'lqin uzunligi), undan fotoeffekt boshlanadi", ["Eng katta chastota", "Eng katta intensivlik", "Eng kichik tok"], "ν₀ = A/h."),
    C(2, "Yorug'lik intensivligi ortsa (chastota o'zgarmas), fotoelektronlar...", "soni ortadi, tezligi o'zgarmaydi", ["tezligi ortadi", "soni kamayadi", "tezligi kamayadi"], "Stoletov."),
    N(2, "A = 2 eV, foton energiyasi 5 eV. Maksimal kinetik energiya?", 3, [7, 2.5, 10], "eV", "5 − 2."),
    N(3, "Foton energiyasi 6,2 eV, A = 4,5 eV. To'xtatuvchi potensial?", 1.7, [10.7, 4.5, 6.2], "V", "eU = E_k → 1,7 V."),
    N(3, "A = 3,3·10⁻¹⁹ J. Qizil chegara chastotasi (h = 6,63·10⁻³⁴)?", 4.977e14, [2e-15, 3.3e14, 1e15], "Hz", "ν₀ = A/h = 4,977e14."),
    N(3, "λ = 200 nm fotonlar A = 4,5 eV ga tushadi (hc = 1240 eV·nm). E_k,max?", 1.7, [6.2, 4.5, 10.7], "eV", "1240/200 = 6,2; 6,2 − 4,5 = 1,7."),
    ON(3, "Fotoeffekt: foton energiyasi 8 eV, to'xtatuvchi potensial 3 V. Chiqish ishi necha eV?", 5, "A = 8 − 3."),
    ON(3, "A = 2,5 eV. Chastotasi 1,2·10¹⁵ Hz foton (h = 4,14·10⁻¹⁵ eV·s) E_k necha eV? (yaxlitlab 2 xona)", 2.47, "hν = 4,968 eV; − 2,5 = 2,468."),
    M(2, [("To'xtatuvchi potensial", "eU_t = E_k,max"), ("Qizil chegara", "ν₀ = A/h"), ("Foton energiyasi", "hν")], "Fotoeffekt."),
]

Q["P11.26"] = [
    C(1, "Foton impulsi?", "p = h/λ", ["p = hλ", "p = mc faqat tinch", "p = h/ν"], "p = hν/c."),
    C(1, "De Broyl to'lqin uzunligi?", "λ = h/(mv)", ["λ = hmv", "λ = mv/h", "λ = h/m"], "Zarra to'lqin xossalari."),
    C(2, "Kompton effektida sochilgan foton to'lqin uzunligi...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "Energiya elektronga beriladi."),
    N(2, "Elektron (m = 9,1·10⁻³¹) v = 10⁶ m/s. de Broyl λ (h = 6,63·10⁻³⁴)?", 7.29e-10, [7.3e-7, 1.4e-9, 6e-3], "m", "h/(mv) = 6,63e-34/9,1e-25 = 7,29e-10."),
    N(2, "Foton λ = 663 nm; impulsi?", 1e-27, [1e-25, 1e-29, 6.63e-34], "kg·m/s", "h/λ = 6,63e-34/6,63e-7."),
    C(2, "Yorug'likning korpuskulyar–to'lqin dualizmi...", "yorug'lik ham to'lqin, ham zarracha (foton) xossalarini namoyon qiladi", ["Faqat to'lqin", "Faqat zarracha", "Hech biri"], "Dualizm."),
    N(3, "Foton massasi relyativistik (m = hν/c²). ν = 3·10¹⁵ Hz. m (h = 6,63·10⁻³⁴, c = 3·10⁸)?", 2.21e-35, [6.63e-34, 2.2e-27, 7.4e-44], "kg", "6,63e-34·3e15/9e16 = 2,21e-35."),
    ON(3, "Elektron v = 2·10⁶ m/s: λ = h/(mv). (h = 6,63·10⁻³⁴; m = 9,1·10⁻³¹). Necha ·10⁻¹⁰ m? (yaxlitlab 2 xona)", 3.64, "λ = 3,643e-10."),
    ON(3, "Foton impulsi 2·10⁻²⁷ kg·m/s. Energiyasi necha ·10⁻¹⁹ J? (E = pc)", 6, "E = 2e-27·3e8 = 6e-19."),
]

_bo = F.bohr_levels([(3, 1), (2, 1), (4, 2)])
Q["P11.27"] = [
    C(1, "Rezerford tajribasida alfa-zarralar oltin folgada sochilishi nimani ko'rsatdi?", "Atomda massiv musbat yadro bor", ["Atom bo'linmas", "Elektron yo'q", "Atom uzluksiz zaryadlangan"], "Planetar model."),
    C(1, "Borning ikkinchi postulati?", "hν = E_n − E_m", ["hν = E_n·E_m", "ν = E_n/h faqat", "E = mc²"], "Sathlar orasidagi o'tish."),
    C(1, "Vodorod atomi energetik sathlari?", "Eₙ = −13,6 eV / n²", ["Eₙ = 13,6·n eV", "Eₙ = −13,6·n² eV", "Eₙ = 0"], "n = 1, 2, 3, …"),
    N(2, "n = 2 sathdagi vodorod energiyasi?", -3.4, [-13.6, -6.8, -1.51], "eV", "−13,6/4."),
    N(2, "n = 3 → n = 1 o'tishda chiqarilgan foton energiyasi?", 12.09, [10.2, 1.89, 13.6], "eV", "−1,51 − (−13,6) = 12,09."),
    N(3, "3 → 2 o'tish (Balmer) fotoni to'lqin uzunligi (hc = 1240 eV·nm; ΔE = 1,89 eV)?", 656, [1240, 400, 1000], "nm", "1240/1,89 = 656 nm."),
    C(2, "Chizmadagi o'tishlardan qaysi biri eng katta energiyali foton chiqaradi?", "A (3→1)", ["B (2→1)", "C (4→2)", "Hammasi teng"], "ΔE = 12,09 eV.", fig=_bo) if False else C(2, "Chizmada 3→1, 2→1 va 4→2 o'tishlar ko'rsatilgan (A, B, C). Qaysi o'tishda foton energiyasi eng katta?", "A (3→1)", ["B (2→1)", "C (4→2)", "Hammasi teng"], "ΔE: 12,09; 10,2; 2,55 eV.", fig=_bo),
    C(2, "Atom energiyani yutganda elektron...", "yuqoriroq sathga o'tadi", ["pastroq sathga o'tadi", "yadroga qulaydi", "atomni tark etmaydi doim"], "Qo'zg'algan holat."),
    ON(3, "Vodorod atomi n = 1 holatdan ionlanishi uchun necha eV kerak?", 13.6, "E_ion = 13,6 eV."),
    ON(3, "n = 4 → n = 2 o'tishdagi foton energiyasi necha eV? (yaxlitlab 2 xona; E₄ = −0,85)", 2.55, "−0,85 + 3,4 = 2,55."),
]

Q["P11.28"] = [
    C(1, "Atom yadrosi nimalardan iborat?", "Protonlar va neytronlar", ["Protonlar va elektronlar", "Faqat neytronlar", "Elektron va neytronlar"], "Nuklonlar."),
    C(1, "Massa soni A nimani bildiradi?", "Nuklonlar soni", ["Protonlar soni", "Elektronlar soni", "Neytronlar soni"], "A = Z + N."),
    N(2, "²³⁵₉₂U yadrosida neytronlar soni?", 143, [92, 235, 327], "", "N = A − Z = 143."),
    C(2, "Izotoplar...", "Z bir xil, A turlicha", ["A bir xil, Z turlicha", "ikkalasi bir xil", "ikkalasi turlicha"], "Bir element."),
    N(3, "⁴₂He yadrosi: m_p = 1,00728, m_n = 1,00866, M_yadro = 4,0015 (a.m.b.). Massa nuqsoni?", 0.0304, [0.0152, 4.0319, 0.304], "a.m.b.", "2·1,00728 + 2·1,00866 − 4,0015 = 4,03188 − 4,0015 = 0,03038 ≈ 0,0304."),
    N(3, "Massa nuqsoni 0,03 a.m.b. bo'lsa, bog'lanish energiyasi (1 a.m.b. = 931,5 MeV)?", 27.9, [0.03, 931.5, 2.79], "MeV", "0,03·931,5 = 27,9."),
    C(2, "Solishtirma bog'lanish energiyasi nimaga bog'liq?", "Yadro nuklonlar soniga — eng yuqorisi temir atrofida", ["Faqat protonlarga", "Faqat neytronlarga", "Bog'liq emas"], "Barqarorlik."),
    ON(3, "²³⁸₉₂U da neytron va protonlar farqi necha?", 54, "N = 146; Z = 92; farq 54."),
    ON(3, "Yadro bog'lanish energiyasi 28 MeV, A = 4. Solishtirma bog'lanish energiyasi necha MeV/nuklon?", 7, "28/4."),
]

_dc = F.decay(2)
Q["P11.29"] = [
    C(1, "Alfa-nur nimadan iborat?", "Geliy yadrolari", ["Elektronlar", "Fotonlar", "Neytronlar"], "²₄He."),
    C(1, "Gamma-nurlar...", "yuqori energiyali elektromagnit to'lqinlar", ["zaryadlangan zarralar", "neytronlar", "geliy yadrolari"], "Zaryadsiz."),
    C(2, "Alfa-yemirilishda Z va A qanday o'zgaradi?", "Z − 2, A − 4", ["Z + 1, A o'zgarmaydi", "Z − 1, A − 1", "Z − 4, A − 2"], "Soddi–Fayans."),
    C(2, "β⁻-yemirilishda yadro Z...", "bittaga ortadi, A o'zgarmaydi", ["ikkiga kamayadi", "o'zgarmaydi", "bittaga kamayadi va A ham"], "n → p + e + ν̄."),
    N(2, "T = 4 kun. 12 kunda boshlang'ich yadrolarning qanday qismi qoladi?", 0.125, [0.25, 0.5, 0.0625], "", "2⁻³."),
    N(3, "Boshlang'ich 640 ta yadro, T = 2 s. 6 s dan keyin qolgan yadrolar?", 80, [320, 160, 40], "ta", "640/8."),
    C(2, "Chizmadagi yemirilish grafigida N(t) har T davrda...", "2 marta kamayadi", ["ikki barobar ortadi", "o'zgarmaydi", "chiziqli kamayadi"], "Eksponent.", fig=_dc),
    N(3, "Dastlabki 2000 yadrodan 5 yarim yemirilish davridan so'ng qolgan yadrolar soni?", 62.5, [400, 125, 31.25], "ta", "2000/32."),
    ON(3, "Radioaktiv element 12 soatda 8 marta kamaydi. Yarim yemirilish davri necha soat?", 4, "8 = 2³ → 3T = 12."),
    ON(3, "²³⁸₉₂U α-yemirilishdan so'ng hosil bo'lgan yadroning massa soni necha?", 234, "238 − 4."),
]

Q["P11.30"] = [
    C(1, "Yadro reaksiyalarida saqlanadi:", "zaryad va massa soni", ["faqat massa", "faqat zaryad", "protonlar soni faqat"], "Z va A."),
    C(1, "Uran-235 bo'linishi zanjir reaksiyasi...", "ajralgan neytronlar yangi yadrolarni bo'ladi", ["fotonlar tufayli", "faqat alfa-zarralar", "elektronlar tufayli"], "Neytronlar."),
    C(1, "Termoyadro reaksiyasi...", "yengil yadrolarning juda yuqori temperaturada qo'shilishi", ["og'ir yadro bo'linishi", "elektronlar qo'shilishi", "alfa-yemirilish"], "Quyosh energiyasi."),
    N(2, "¹⁴₇N + ⁴₂He → X + ¹₁H. X yadrosining massa soni?", 17, [18, 14, 16], "", "14 + 4 − 1 = 17."),
    N(2, "Shu reaksiyada X ning zaryad soni?", 8, [9, 7, 6], "", "7 + 2 − 1 = 8 (kislorod-17)."),
    N(3, "D + T → He + n reaksiyada energiya (E = Δm·931,5): Δm = 0,0189 a.m.b.", 17.6, [0.0189, 931.5, 1.76], "MeV", "0,0189·931,5 = 17,6."),
    C(2, "Boshqariladigan zanjir reaksiyasi yadro reaktorida qaysi usul bilan ta'minlanadi?", "Neytronlarni yutuvchi sterjenlar", ["Faqat suv sovitgichi", "Uranni qizdirish", "Radiodan nurlantirish"], "Kadmiy/bor sterjenlar."),
    ON(3, "²³⁵₉₂U bitta yadrosi bo'linganda taxminan 200 MeV energiya ajraladi. 5 ta yadro necha MeV beradi?", 1000, "5·200."),
    ON(3, "Reaksiyada ²⁷₁₃Al + ⁴₂He → ³⁰₁₅P + X. X ning massa soni necha?", 1, "27 + 4 − 30 = 1 (neytron)."),
]

Q["P11.31"] = [
    C(1, "Proton kvark tarkibi?", "uud", ["udd", "uuu", "ddd"], "2/3+2/3−1/3 = +1."),
    C(1, "Neytron kvark tarkibi?", "udd", ["uud", "uus", "ddd"], "2/3 −1/3 −1/3 = 0."),
    C(1, "Leptonlar...", "kuchli ta'sirlashmaydigan zarralar (elektron, neytrino)", ["kvarklardan iborat", "mezonlar", "barionlar"], "Elektron — lepton."),
    C(2, "Barionlar...", "uchta kvarkdan iborat (proton, neytron)", ["ikkita kvarkdan", "kvarksiz", "faqat leptonlar"], "Adronlar sinfi."),
    C(2, "Pozitron...", "elektronning antizarrasi", ["protonning antizarrasi", "neytron", "foton"], "+e."),
    C(2, "Mezonlar...", "kvark va antikvarkdan iborat", ["uchta kvarkdan", "leptonlar", "fotonlar"], "Masalan π-mezon."),
    C(2, "Elektr zaryadi u kvark uchun?", "+2/3 e", ["−1/3 e", "+1 e", "0"], "u = +2/3, d = −1/3."),
    ON(3, "Proton va neytron kvark tarkibida jami nechta u kvark bor?", 3, "uud + udd = 3 ta u."),
    ON(3, "Neytron β-yemirilganda hosil bo'ladigan zarra proton, elektron va ... nima? (so'z bilan: antineytrino)", "antineytrino", "n → p + e⁻ + ν̄ₑ.") if False else ON(3, "Proton kvark tarkibida jami nechta d kvark bor?", 1, "uud — bitta d."),
]
