"""v268: MATEMATIKA va FIZIKA — eng kam savolli mavzularga DTM 2024–2026 / milliy sertifikat uslubidagi
o'ylantiradigan savollar. Barcha hisob-kitoblar kod bilan tekshirilgan."""
from __future__ import annotations

from ._dsl import C, O

MATH: dict[str, list] = {
    "Harakat masalalari": [
        C(2, "Avtomobil yo'lning birinchi yarmini 60 km/soat, ikkinchi yarmini 40 km/soat tezlikda o'tdi. Butun yo'ldagi o'rtacha tezlik?", "48 km/soat", ["50 km/soat", "45 km/soat", "52 km/soat"], "v = 2·60·40/(60 + 40) = 48. O'rtacha tezlik tezliklarning o'rta arifmetigi emas!"),
        C(2, "Qayiq oqim bo'ylab 30 km ni 2 soatda, oqimga qarshi shu masofani 3 soatda o'tdi. Daryo oqimi tezligi?", "2,5 km/soat", ["5 km/soat", "12,5 km/soat", "3 km/soat"], "v + u = 15, v − u = 10 → u = 2,5."),
        C(3, "Birinchi mashina 60 km/soat tezlikda yo'lga chiqdi, 1 soatdan keyin shu yerdan ikkinchisi 80 km/soat tezlikda ketdi. Ikkinchi mashina necha soatda birinchisiga yetib oladi?", "3 soatda", ["1 soatda", "4 soatda", "2 soatda"], "Oradagi masofa 60 km, yaqinlashish tezligi 80 − 60 = 20 → 60/20 = 3."),
        C(3, "300 m uzunlikdagi poyezd ustun yonidan 15 s da o'tadi. U 450 m uzunlikdagi ko'prikdan necha sekundda to'liq o'tadi?", "37,5 s", ["22,5 s", "30 s", "45 s"], "v = 300/15 = 20 m/s; (300 + 450)/20 = 37,5 s."),
        O(2, "Oralaridagi masofa 360 km bo'lgan ikki shahardan bir vaqtda 70 va 50 km/soat tezlikda ikki mashina bir-biriga qarab yo'lga chiqdi. Necha soatdan keyin uchrashadi?", ["3"], "360/(70 + 50) = 3 soat."),
    ],
    "Ish va birgalikda ishlash masalalari": [
        C(2, "Birinchi ishchi ishni 6 soatda, ikkinchisi 3 soatda bajaradi. Birgalikda necha soatda bajarishadi?", "2 soatda", ["4,5 soatda", "3 soatda", "1,5 soatda"], "1/6 + 1/3 = 1/2 → 2 soat."),
        C(2, "Bitta quvur hovuzni 6 soatda to'ldiradi, ikkinchisi to'la hovuzni 9 soatda bo'shatadi. Ikkalasi birga ochiq bo'lsa, bo'sh hovuz necha soatda to'ladi?", "18 soatda", ["15 soatda", "3 soatda", "12 soatda"], "1/6 − 1/9 = 1/18."),
        C(3, "A va B birgalikda ishni 12 kunda bajaradi. A yolg'iz 20 kunda bajaradi. B yolg'iz necha kunda bajaradi?", "30 kunda", ["8 kunda", "32 kunda", "24 kunda"], "1/12 − 1/20 = 1/30."),
        C(3, "A ishni yolg'iz 12 kunda bajaradi. U 4 kun ishlagach, B qo'shildi va qolgan ishni birgalikda 4 kunda tugatishdi. B yolg'iz necha kunda bajarardi?", "12 kunda", ["6 kunda", "8 kunda", "16 kunda"], "4 kunda 1/3 bajarildi; qolgan 2/3 ni 4 kunda → birgalikdagi unum 1/6; B = 1/6 − 1/12 = 1/12."),
        O(3, "Uch nasos birgalikda idishni 2 soatda to'ldiradi. Birinchisi yolg'iz 6 soatda, ikkinchisi 4 soatda to'ldiradi. Uchinchisi yolg'iz necha soatda to'ldiradi?", ["12"], "1/2 − 1/6 − 1/4 = 1/12."),
    ],
    "Intervallar usuli": [
        C(2, "(x − 1)(x + 2)/(x − 3) ≤ 0 tengsizlikning yechimi?", "(−∞; −2] ∪ [1; 3)", ["[−2; 1] ∪ (3; ∞)", "(−∞; −2] ∪ [1; 3]", "[−2; 3)"], "Nollar: −2, 1, 3 (3 — maxrajni nolga aylantiradi, kirmaydi). Ishoralar o'ngdan: +, −, +, −."),
        C(2, "x² − 5x + 6 < 0 tengsizlikning butun yechimlari soni?", "0", ["1", "2", "3"], "2 < x < 3 oraliqda butun son yo'q."),
        C(3, "(x² − 9)/(x − 5) < 0 tengsizlikning [−10; 10] dagi butun yechimlari soni?", "8", ["7", "9", "10"], "Yechim: x < −3 yoki 3 < x < 5 → −10…−4 (7 ta) va 4 (1 ta)."),
        C(3, "(x + 1)²(x − 2) ≥ 0 tengsizlikning yechimi?", "{−1} ∪ [2; ∞)", ["[2; ∞)", "[−1; ∞)", "(−∞; −1] ∪ [2; ∞)"], "(x + 1)² ≥ 0; x = −1 da ifoda 0 ga teng — yechimga kiradi. Juft karrali ildizni unutmang!"),
        O(2, "x(x − 4) ≤ 0 tengsizlikning butun yechimlari yig'indisini toping.", ["10"], "0 ≤ x ≤ 4: 0 + 1 + 2 + 3 + 4 = 10."),
    ],
    "Parametrli tenglamalar": [
        C(2, "a ning qanday qiymatlarida x² + ax + 9 = 0 tenglama yagona yechimga ega?", "a = ±6", ["a = 6", "a = 9", "a = ±3"], "D = a² − 36 = 0."),
        C(3, "a ning qanday qiymatlarida x² − 2x + a = 0 tenglama ikkita turli musbat ildizga ega?", "0 < a < 1", ["a < 1", "a > 0", "0 ≤ a ≤ 1"], "D > 0 → a < 1; ildizlar ko'paytmasi a > 0, yig'indisi 2 > 0."),
        C(3, "a ning qanday qiymatida (a − 2)x = a² − 4 tenglama cheksiz ko'p yechimga ega?", "a = 2", ["a = −2", "a = ±2", "bunday a yo'q"], "a = 2 da 0·x = 0 — har qanday x yechim; a = −2 da yagona yechim x = 0."),
        C(2, "a ning qanday qiymatida ax = 5 tenglama yechimga ega emas?", "a = 0", ["a = 5", "a = −5", "a = 1"], "0·x = 5 — yechim yo'q."),
        O(3, "x² − (a + 1)x + a = 0 tenglamaning ildizlaridan biri 3 ga teng. Ikkinchi ildizni toping.", ["1"], "x = 3: 9 − 3a − 3 + a = 0 → a = 3; ildizlar ko'paytmasi a = 3 → ikkinchi ildiz 1."),
    ],
    "Logarifmik tengsizliklar": [
        C(2, "log₂(x − 1) < 3 tengsizlikning butun yechimlari soni?", "7", ["8", "9", "6"], "0 < x − 1 < 8 → 1 < x < 9: 2, 3, …, 8."),
        C(3, "log₁/₃(x + 2) ≥ −2 tengsizlikning butun yechimlari soni?", "9", ["8", "10", "7"], "Asos 1 dan kichik — belgi almashadi: 0 < x + 2 ≤ 9 → −2 < x ≤ 7: −1, …, 7."),
        C(3, "log₂x + log₂(x − 2) ≤ 3 tengsizlikning yechimi?", "(2; 4]", ["[−2; 4]", "(0; 4]", "(2; ∞)"], "x > 2 va x(x − 2) ≤ 8 → −2 ≤ x ≤ 4; aniqlanish sohasi bilan kesishma (2; 4]."),
        C(2, "lg x > 2 tengsizlikning yechimi?", "x > 100", ["x > 20", "x > 2", "0 < x < 100"], "lg x > lg 100."),
        O(3, "log₀,₅(2x − 1) > −1 tengsizlikning butun yechimlari sonini toping.", ["1"], "0 < 2x − 1 < 2 → 0,5 < x < 1,5 → faqat x = 1."),
    ],
    "Prizma va piramida": [
        C(2, "Muntazam uchburchakli prizmaning asos tomoni 4, balandligi 5. Hajmi?", "20√3", ["40√3", "80", "10√3"], "V = (√3/4)·16·5 = 20√3."),
        C(3, "Muntazam to'rtburchakli piramida asosining tomoni 6, apofemasi 5. Hajmi?", "48", ["60", "144", "36"], "Balandlik h = √(5² − 3²) = 4; V = 36·4/3 = 48."),
        C(2, "Shu piramida (asos tomoni 6, apofema 5) yon sirtining yuzi?", "60", ["30", "96", "120"], "4 · (1/2 · 6 · 5) = 60."),
        C(2, "Kub diagonali 6√3. Kub hajmi?", "216", ["108", "36√3", "72"], "Diagonal a√3 → a = 6, V = 216."),
        O(3, "To'g'ri burchakli parallelepipedning o'lchamlari 2, 3 va 6. Uning diagonalini toping.", ["7"], "√(4 + 9 + 36) = 7."),
    ],
    "Boshlang'ich funksiya va integral yuzasi": [
        C(2, "f(x) = 2x + 1 funksiyaning F(1) = 5 shartni qanoatlantiruvchi boshlang'ich funksiyasi?", "x² + x + 3", ["x² + x + 5", "x² + x", "2x² + x + 2"], "F = x² + x + C; 1 + 1 + C = 5 → C = 3."),
        C(3, "y = x² va y = 2x chiziqlar bilan chegaralangan shakl yuzi?", "4/3", ["8/3", "2", "4"], "∫₀² (2x − x²)dx = 4 − 8/3 = 4/3."),
        C(2, "y = cos x, y = 0, x = 0, x = π/2 chiziqlar bilan chegaralangan shakl yuzi?", "1", ["π/2", "2", "0"], "∫₀^(π/2) cos x dx = sin(π/2) − sin 0 = 1."),
        C(3, "y = 4 − x² parabola va Ox o'qi bilan chegaralangan shakl yuzi?", "32/3", ["16/3", "8", "64/3"], "∫₋₂² (4 − x²)dx = 16 − 16/3 = 32/3."),
        O(2, "∫₀² (3x² − 2x)dx integralni hisoblang.", ["4"], "(x³ − x²)|₀² = 8 − 4 = 4."),
    ],
    "Ehtimollik: klassik va ko'p bosqichli": [
        C(2, "Ikki o'yin soqqasi tashlandi. Tushgan ochkolar yig'indisi 8 bo'lish ehtimoli?", "5/36", ["1/6", "1/9", "7/36"], "(2,6),(3,5),(4,4),(5,3),(6,2) — 5 ta qulay hol."),
        C(3, "Qutida 5 ta qizil va 3 ta ko'k shar bor. Qaytarmasdan 2 ta shar olindi. Ikkalasi ham qizil bo'lish ehtimoli?", "5/14", ["25/64", "5/8", "10/28"], "5/8 · 4/7 = 20/56 = 5/14."),
        C(3, "Soqqa 3 marta tashlandi. Kamida bir marta 6 tushish ehtimoli?", "91/216", ["1/2", "1/6", "125/216"], "1 − (5/6)³ = 91/216. «Kamida bitta» — qarama-qarshi hodisa orqali."),
        C(2, "Tanga 3 marta tashlandi. Rosa 2 marta «gerb» tushish ehtimoli?", "3/8", ["1/4", "1/2", "2/3"], "C(3,2)/8 = 3/8."),
        O(3, "1 dan 30 gacha sonlardan biri tasodifan tanlandi. U 3 ga ham, 5 ga ham bo'linmaslik ehtimolini kasr ko'rinishida yozing.", ["8/15", "16/30"], "3 ga bo'linadi 10 ta, 5 ga 6 ta, 15 ga 2 ta → 14 ta; 30 − 14 = 16; 16/30 = 8/15."),
    ],
    "Kombinatsiya, Nyuton binomi va masalalar": [
        C(2, "6 o'g'il va 4 qiz boladan 3 o'g'il va 2 qizdan iborat komissiya necha usulda tuziladi?", "120", ["60", "210", "720"], "C(6,3) · C(4,2) = 20 · 6 = 120."),
        C(2, "(x + 2)⁵ yoyilmasida x³ oldidagi koeffitsient?", "40", ["10", "80", "20"], "C(5,3) · 2² = 10 · 4 = 40."),
        C(3, "(2x − 1/x)⁶ yoyilmasidagi ozod had?", "−160", ["160", "−20", "60"], "Umumiy had C(6,k)(2x)^(6−k)(−1/x)^k; x darajasi 6 − 2k = 0 → k = 3: 20 · 8 · (−1) = −160."),
        C(2, "(3x − 1)⁴ yoyilmasidagi koeffitsientlar yig'indisi?", "16", ["81", "4", "256"], "x = 1 qo'yamiz: (3 − 1)⁴ = 16."),
        O(3, "«MATEMATIKA» so'zidagi harflardan nechta turli 3 harfli «so'z» tuzish mumkin, agar barcha harflar turlicha bo'lsa? (M, A, T, E, I, K — 6 xil harf)", ["120"], "6 xil harfdan 3 tasini tartib bilan: 6 · 5 · 4 = 120."),
    ],
    "Integral va aniqlangan integral": [
        C(2, "∫₁ᵉ (1/x)dx = ?", "1", ["e", "0", "e − 1"], "ln e − ln 1 = 1."),
        C(3, "∫₀^π sin x dx = ?", "2", ["0", "1", "π"], "−cos π + cos 0 = 1 + 1 = 2."),
        C(2, "∫ (6x² + 4x)dx = ?", "2x³ + 2x² + C", ["12x + 4 + C", "6x³ + 4x² + C", "3x³ + 2x² + C"], "6x³/3 + 4x²/2."),
        C(3, "∫₀¹ eˣ dx = ?", "e − 1", ["e", "1", "e + 1"], "eˣ|₀¹ = e − 1."),
        O(3, "∫₋₁¹ (x³ + 2)dx integralni hisoblang.", ["4"], "x³ toq funksiya — simmetrik oraliqda integrali 0; ∫2dx = 4."),
    ],
    "Fazoviy jismlar: hajm va sirt (chizma)": [
        C(2, "Silindr asosining radiusi 3, balandligi 4. To'la sirti?", "42π", ["24π", "36π", "30π"], "2πrh + 2πr² = 24π + 18π."),
        C(2, "Konus asosining radiusi 3, balandligi 4. Yon sirti?", "15π", ["12π", "24π", "9π"], "l = 5, S = πrl = 15π."),
        C(3, "Shar sirtining yuzi 36π. Shar hajmi?", "36π", ["108π", "12π", "288π"], "4πr² = 36π → r = 3; V = 4/3·π·27 = 36π."),
        C(3, "Kub ichiga shar chizilgan. Kub qirrasi 6. Shar hajmi?", "36π", ["288π", "72π", "108π"], "r = 3; V = 4/3·π·27 = 36π."),
        O(2, "Kubning to'la sirti 54. Uning hajmini toping.", ["27"], "6a² = 54 → a = 3 → V = 27."),
    ],
    "To'plamlar va Venn diagrammasi (chizma)": [
        C(2, "Sinfda 40 o'quvchi bor. 25 tasi matematika, 20 tasi fizika to'garagiga qatnashadi, 8 tasi hech biriga qatnashmaydi. Ikkalasiga qatnashadiganlar nechta?", "13", ["5", "12", "17"], "25 + 20 − x = 40 − 8 → x = 13."),
        C(2, "Shu sinfda faqat matematika to'garagiga qatnashadiganlar nechta?", "12", ["25", "13", "7"], "25 − 13 = 12."),
        C(3, "A = {1, 2, 3, 4}, B = {3, 4, 5}. (A ∪ B) \\ (A ∩ B) to'plam elementlari soni?", "3", ["2", "5", "4"], "A ∪ B = {1,2,3,4,5}, A ∩ B = {3,4} → {1, 2, 5}."),
        C(3, "100 kishidan 60 tasi ingliz, 50 tasi rus tilini biladi, 20 tasi ikkalasini ham biladi. Hech qaysi tilni bilmaydiganlar nechta?", "10", ["0", "30", "20"], "60 + 50 − 20 = 90; 100 − 90 = 10."),
        O(2, "4 elementli to'plamning nechta qism to'plami bor?", ["16"], "2⁴ = 16 (bo'sh to'plam va to'plamning o'zi ham kiradi)."),
    ],
}

PHYS: dict[str, list] = {
    "Fizik kattaliklar, SI birliklari va o'lchash": [
        C(1, "72 km/soat necha m/s ga teng?", "20 m/s", ["72 m/s", "7,2 m/s", "36 m/s"], "72 · 1000/3600 = 20."),
        C(2, "Quyidagilardan qaysi biri SI ning asosiy birligi EMAS?", "Nyuton", ["Kilogramm", "Amper", "Kelvin"], "Nyuton — hosilaviy birlik: 1 N = 1 kg·m/s²."),
        C(2, "Bosim birligi paskalni SI asosiy birliklari orqali ifodalang.", "kg/(m·s²)", ["kg·m/s²", "kg/m³", "N·m"], "Pa = N/m² = kg·m/s² : m² = kg/(m·s²)."),
        C(3, "Jism tezligi v = at formuladan topiladi. a birligi m/s², t birligi s. v ning birligi?", "m/s", ["m/s²", "m", "m·s"], "m/s² · s = m/s — o'lchamlik tahlili."),
    ],
    "Gidrodinamika: uzluksizlik va Bernulli tenglamasi": [
        C(2, "Diametri 4 sm quvurda suv 2 m/s tezlikda oqadi. Quvur diametri 2 sm ga torayganda tezlik?", "8 m/s", ["4 m/s", "1 m/s", "16 m/s"], "S₁v₁ = S₂v₂; yuza diametr kvadratiga proporsional: 2 · (4/2)² = 8."),
        C(2, "Idishdagi suv sathidan 5 m pastdagi teshikdan suv qanday tezlikda otiladi? (g = 10 m/s²)", "10 m/s", ["5 m/s", "50 m/s", "100 m/s"], "Torrichelli: v = √(2gh) = √100."),
        C(3, "Quvur torayganda suyuqlik bosimi qanday o'zgaradi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Avval ortib, keyin kamayadi"], "Bernulli: tezlik ortgan joyda statik bosim kamayadi."),
        O(2, "Ko'ndalang kesimi 20 sm² bo'lgan quvurda suv 3 m/s tezlikda oqadi. 1 sekundda necha litr suv oqib o'tadi?", ["6"], "Q = Sv = 0,002 · 3 = 0,006 m³/s = 6 L/s."),
    ],
    "Temperatura va issiqlik uzatish turlari": [
        C(1, "Vakuumda issiqlik qaysi usulda uzatiladi?", "Nurlanish", ["Konveksiya", "Issiqlik o'tkazuvchanlik", "Barcha usullarda"], "Konveksiya va o'tkazuvchanlik uchun modda kerak."),
        C(2, "27 °C temperatura Kelvin shkalasida necha?", "300 K", ["246 K", "27 K", "327 K"], "T = t + 273."),
        C(2, "Isitish radiatorlari xonaning pastki qismiga o'rnatilishiga sabab?", "Issiq havo ko'tarilib, konveksiya oqimi hosil bo'ladi", ["Nurlanish faqat pastga yo'naladi", "Pastda havo zichligi kam", "Devor issiqlikni yaxshi o'tkazadi"], "Isigan havo kengayadi, zichligi kamayib yuqoriga ko'tariladi."),
        C(3, "Temperaturalar farqi Selsiy shkalasida 25 °C. Kelvin shkalasida farq?", "25 K", ["298 K", "248 K", "0 K"], "Shkala bo'linmalari bir xil — farq o'zgarmaydi."),
    ],
    "MKT asosiy tenglamasi va temperatura": [
        C(2, "Ideal gazning absolyut temperaturasi 4 marta oshsa, molekulalarning o'rtacha kvadratik tezligi qanday o'zgaradi?", "2 marta ortadi", ["4 marta ortadi", "16 marta ortadi", "O'zgarmaydi"], "v ~ √T."),
        C(2, "Molekula ilgarilanma harakatining o'rtacha kinetik energiyasi qaysi kattalikka bog'liq?", "Faqat absolyut temperaturaga", ["Gaz turiga", "Bosimga va hajmga", "Molyar massaga"], "E = (3/2)kT."),
        C(3, "Bosim 10⁵ Pa, temperatura 300 K bo'lgan gazda molekulalar konsentratsiyasi taxminan? (k = 1,38·10⁻²³ J/K)", "2,4·10²⁵ m⁻³", ["2,4·10²³ m⁻³", "4,1·10²⁵ m⁻³", "7,2·10²⁶ m⁻³"], "n = p/(kT) = 10⁵/(1,38·10⁻²³·300)."),
        C(3, "Hajm o'zgarmasdan gaz temperaturasi 2 marta kamaydi. Bosim?", "2 marta kamayadi", ["2 marta ortadi", "4 marta kamayadi", "O'zgarmaydi"], "p = nkT, n o'zgarmas."),
    ],
    "Siklik jarayonlar va grafik transformatsiya": [
        C(2, "Yopiq siklda gazning ichki energiyasi o'zgarishi nimaga teng?", "Nolga", ["Bajarilgan ishga", "Olingan issiqlikka", "Sikl yuziga"], "Gaz boshlang'ich holatiga qaytadi."),
        C(2, "p–V diagrammasida siklning yuzi nimani ifodalaydi?", "Sikl davomida bajarilgan to'liq ishni", ["Ichki energiyani", "Olingan issiqlikni", "Temperaturani"], "A = ∮p dV."),
        C(3, "Izobarik jarayonda bosim 2·10⁵ Pa, hajm 1 L dan 3 L gacha ortdi. Gaz bajargan ish?", "400 J", ["600 J", "200 J", "4000 J"], "A = pΔV = 2·10⁵ · 2·10⁻³."),
        C(3, "p–V diagrammadagi izoterma V–T diagrammasida qanday ko'rinadi?", "Vertikal to'g'ri chiziq (T = const)", ["Giperbola", "Gorizontal chiziq", "Koordinata boshidan o'tuvchi chiziq"], "T o'zgarmaydi, V o'zgaradi."),
    ],
    "Gazlar aralashmasi va Dalton qonuni": [
        C(2, "Dalton qonuniga ko'ra gazlar aralashmasining bosimi?", "Komponentlar parsial bosimlarining yig'indisiga teng", ["Eng katta parsial bosimga teng", "Parsial bosimlarning o'rtachasiga teng", "Faqat temperaturaga bog'liq"], "p = p₁ + p₂ + …"),
        C(3, "Idishda 1 mol azot va 3 mol kislorod bor, umumiy bosim 200 kPa. Azotning parsial bosimi?", "50 kPa", ["100 kPa", "150 kPa", "66,7 kPa"], "p(N₂) = 1/4 · 200."),
        C(3, "Teng hajmli ikki idishda 100 kPa va 300 kPa bosimli bir xil temperaturadagi gazlar bor. Idishlar ulanganda bosim?", "200 kPa", ["400 kPa", "150 kPa", "300 kPa"], "Hajm 2 marta ortadi: (100 + 300)/2."),
        O(2, "Aralashmada vodorodning parsial bosimi 30 kPa, geliyniki 70 kPa. Aralashma bosimini kPa da toping.", ["100"], "30 + 70."),
    ],
    "Murakkab issiqlik balansi masalalari": [
        C(2, "20 °C li 2 kg suvga 80 °C li 1 kg suv quyildi. Aralashma temperaturasi?", "40 °C", ["50 °C", "60 °C", "30 °C"], "(2·20 + 1·80)/3 = 40."),
        C(3, "50 °C li 2 kg suvga 0 °C li 0,5 kg muz tashlandi. Muz to'liq eridimi va oxirgi temperatura taxminan? (c = 4,2 kJ/(kg·K), λ = 330 kJ/kg)", "Eridi, ≈24 °C", ["Erimadi, 0 °C", "Eridi, 40 °C", "Eridi, ≈10 °C"], "Suv 0 °C gacha 420 kJ beradi > 165 kJ; (420 − 165)/(2,5·4,2) ≈ 24,3 °C."),
        C(3, "Bir xil massali suv (c = 4200) va temir (c = 460) bir xil issiqlik oldi. Qaysi biri ko'proq isiydi?", "Temir, taxminan 9 marta ko'proq", ["Suv", "Ikkalasi bir xil", "Temir, 2 marta ko'proq"], "Δt = Q/(cm); 4200/460 ≈ 9,1."),
    ],
    "Kirxgof qonunlari va Uitston ko'prigi": [
        C(2, "Kirxgofning birinchi qonuni qaysi saqlanish qonunining natijasi?", "Elektr zaryadining saqlanishi", ["Energiyaning saqlanishi", "Impulsning saqlanishi", "Massaning saqlanishi"], "Tugunga kirgan tok = chiqqan tok."),
        C(2, "Tugunga 3 A va 5 A tok kiradi, bitta simdan 2 A chiqadi. Ikkinchi chiquvchi simdagi tok?", "6 A", ["10 A", "4 A", "8 A"], "3 + 5 = 2 + I."),
        C(3, "Uitston ko'prigi muvozanatda (galvanometr toki nol). R₁ = 4 Ω, R₂ = 8 Ω, R₃ = 6 Ω. R₄ = ? (R₁/R₂ = R₃/R₄)", "12 Ω", ["3 Ω", "16 Ω", "2 Ω"], "4/8 = 6/R₄ → R₄ = 12."),
        C(3, "Kirxgofning ikkinchi qonuni nimani ifodalaydi?", "Yopiq konturdagi EYK lar yig'indisi kuchlanish tushishlari yig'indisiga teng", ["Tugundagi toklar yig'indisi nolga teng", "Qarshiliklar ketma-ket qo'shiladi", "Quvvat kuchlanishga proporsional"], "Energiya saqlanish qonuni."),
    ],
    "Magnit maydon: Amper va Lorens kuchlari": [
        C(2, "Uzunligi 0,4 m, toki 5 A bo'lgan o'tkazgich induksiyasi 0,2 Tl bo'lgan maydonga perpendikulyar joylashgan. Amper kuchi?", "0,4 N", ["4 N", "0,04 N", "10 N"], "F = BIL = 0,2·5·0,4."),
        C(3, "Lorens kuchi zarra ustida ish bajaradimi?", "Yo'q, u tezlikka doim perpendikulyar", ["Ha, har doim musbat ish", "Faqat elektronda", "Faqat maydon bir jinsli bo'lmasa"], "F ⊥ v → A = 0, tezlik moduli o'zgarmaydi."),
        C(3, "Proton (m = 1,67·10⁻²⁷ kg, q = 1,6·10⁻¹⁹ C) 10⁶ m/s tezlikda B = 0,5 Tl maydonga perpendikulyar uchib kirdi. Aylana radiusi taxminan?", "2,1 sm", ["21 sm", "0,2 mm", "2,1 m"], "r = mv/(qB) ≈ 0,021 m."),
        C(2, "O'tkazgich magnit chiziqlariga parallel joylashsa, Amper kuchi?", "Nolga teng", ["Maksimal", "BIL/2", "Yo'nalishi tokka teskari"], "F = BIL·sin α, α = 0."),
    ],
    "O'zgaruvchan tok": [
        C(2, "Tarmoqdagi kuchlanishning amplituda qiymati 311 V. Effektiv qiymati?", "220 V", ["311 V", "155 V", "440 V"], "U = U₀/√2 ≈ 220."),
        C(3, "Induktivligi 0,2 Gn g'altakning 50 Hz chastotadagi induktiv qarshiligi taxminan?", "62,8 Ω", ["10 Ω", "31,4 Ω", "0,016 Ω"], "X_L = 2πνL."),
        C(3, "Chastota 2 marta oshirilsa, kondensatorning sig'im qarshiligi?", "2 marta kamayadi", ["2 marta ortadi", "4 marta kamayadi", "O'zgarmaydi"], "X_C = 1/(2πνC)."),
        C(2, "O'zgaruvchan tok zanjiridagi faol qarshilikda tok va kuchlanish fazalari?", "Mos keladi", ["Tok π/2 ga oldinda", "Kuchlanish π/2 ga oldinda", "Qarama-qarshi"], "Rezistorda faza siljishi yo'q."),
    ],
    "Interferensiya, difraksiya va panjara": [
        C(3, "Yung tajribasida λ = 600 nm, tirqishlar orasi 0,4 mm, ekrangacha masofa 2 m. Qo'shni yorug' polosalar orasidagi masofa?", "3 mm", ["0,3 mm", "30 mm", "1,5 mm"], "Δx = λL/d."),
        C(3, "Davri 2 mkm bo'lgan panjaraga 500 nm li yorug'lik tushdi. Kuzatiladigan eng katta maksimum tartibi?", "3", ["4", "2", "5"], "d/λ = 4, lekin k = 4 da sin φ = 1 — 90° burchakda kuzatilmaydi."),
        C(2, "Interferensiya kuzatilishi uchun to'lqinlar qanday bo'lishi kerak?", "Kogerent", ["Turli chastotali", "Faqat qutblangan", "Faqat ko'zga ko'rinadigan"], "Chastotasi bir xil, faza farqi o'zgarmas."),
        C(2, "Yo'l farqi yarim to'lqinlarning toq soniga teng bo'lsa, kuzatiladi?", "Minimum (qorong'i)", ["Maksimum", "Hech narsa", "Kamalak"], "Δ = (2k + 1)λ/2."),
    ],
    "Foton, Kompton effekti va de Broyl to'lqinlari": [
        C(2, "To'lqin uzunligi 663 nm bo'lgan foton energiyasi taxminan? (h = 6,63·10⁻³⁴ J·s)", "3·10⁻¹⁹ J", ["3·10⁻²⁸ J", "1,5·10⁻¹⁹ J", "6·10⁻¹⁸ J"], "E = hc/λ."),
        C(3, "10⁶ m/s tezlikdagi elektronning de Broyl to'lqin uzunligi taxminan? (m = 9,1·10⁻³¹ kg)", "0,73 nm", ["73 nm", "7,3 mm", "0,073 pm"], "λ = h/(mv) ≈ 7,3·10⁻¹⁰ m."),
        C(3, "Kompton effektida sochilgan nurlanish to'lqin uzunligi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Nolga teng bo'ladi"], "Foton elektronga energiya beradi → λ ortadi."),
        C(2, "Foton tinchlikdagi massasi?", "Nolga teng", ["Elektron massasiga teng", "hν/c²", "Cheksiz"], "Foton faqat harakatda mavjud."),
    ],
    "Atom modellari va Bor postulatlari": [
        C(2, "Vodorod atomida elektron 3-sathdan 2-sathga o'tganda chiqqan foton energiyasi taxminan? (Eₙ = −13,6/n² eV)", "1,89 eV", ["10,2 eV", "12,1 eV", "3,4 eV"], "13,6(1/4 − 1/9)."),
        C(3, "Rezerford tajribasida alfa-zarralarning ozgina qismi katta burchakka og'ishi nimani ko'rsatdi?", "Atomda kichik, og'ir, musbat yadro borligini", ["Atom bir jinsli ekanini", "Elektronlar musbatligini", "Atom bo'linmasligini"], "Musbat zaryad kichik hajmda to'plangan."),
        C(2, "Borning birinchi postulatiga ko'ra statsionar holatda elektron?", "Nurlanmaydi", ["Doim nurlanadi", "Yadroga tushadi", "Tezligini oshiradi"], "Statsionar orbitada energiya o'zgarmaydi."),
        C(3, "Vodorod atomini ionlashtirish uchun asosiy holatdan qancha energiya kerak?", "13,6 eV", ["10,2 eV", "3,4 eV", "1,89 eV"], "n = 1 dan n = ∞ ga."),
    ],
    "Zarbalar: elastik va noelastik to'qnashuvlar": [
        C(3, "3 m/s tezlikdagi 2 kg sharcha tinch turgan 1 kg sharchaga urilib, birga harakatlandi. Umumiy tezlik?", "2 m/s", ["3 m/s", "1,5 m/s", "1 m/s"], "2·3 = 3·v."),
        C(3, "Shu noelastik to'qnashuvda qancha mexanik energiya issiqlikka aylandi?", "3 J", ["9 J", "6 J", "0 J"], "9 J − 6 J."),
        C(2, "Massalari teng ikki shar markaziy elastik to'qnashsa (biri tinch)?", "Tezliklar almashadi", ["Ikkalasi to'xtaydi", "Birga harakatlanadi", "Ikkalasi qaytadi"], "Impuls va energiya saqlanadi."),
        C(2, "Qaysi to'qnashuvda kinetik energiya saqlanadi?", "Mutlaq elastik", ["Mutlaq noelastik", "Har qandayida", "Hech qaysisida"], "Noelastikda energiyaning bir qismi issiqlikka aylanadi."),
    ],
    "Issiqlik dvigatellari va FIK": [
        C(2, "Isitgich 500 K, sovitgich 300 K bo'lgan ideal issiqlik mashinasining FIK?", "40%", ["60%", "30%", "100%"], "η = 1 − 300/500."),
        C(3, "Dvigatel isitgichdan 1000 J oladi, FIK 25%. Sovitgichga qancha issiqlik beradi?", "750 J", ["250 J", "1000 J", "1250 J"], "A = 250 J; Q₂ = 1000 − 250."),
        C(3, "Karno sikli FIK ini oshirish uchun eng samarali yo'l?", "Isitgich temperaturasini oshirish yoki sovitgichnikini pasaytirish", ["Ishchi jism massasini oshirish", "Gazni almashtirish", "Siklni tezlashtirish"], "η = 1 − T₂/T₁ — faqat temperaturalarga bog'liq."),
        C(2, "Nima uchun issiqlik dvigatelining FIK 100% bo'la olmaydi?", "Sovitgichga issiqlik berish shart (II qonun)", ["Ishqalanish doim bor", "Yoqilg'i yetmaydi", "Gaz siqilmaydi"], "Termodinamikaning ikkinchi qonuni."),
    ],
    "Ichki energiya va termodinamikaning birinchi qonuni": [
        C(2, "Gaz 500 J issiqlik olib, 200 J ish bajardi. Ichki energiyasi qanday o'zgardi?", "300 J ga ortdi", ["700 J ga ortdi", "300 J ga kamaydi", "O'zgarmadi"], "ΔU = Q − A."),
        C(3, "Adiabatik kengayishda gaz temperaturasi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Avval ortib keyin kamayadi"], "Q = 0 → ΔU = −A < 0."),
        C(3, "Izotermik jarayonda gaz 300 J issiqlik oldi. Gaz bajargan ish?", "300 J", ["0 J", "150 J", "600 J"], "T = const → ΔU = 0 → A = Q."),
        C(2, "Izoxorik isitishda gaz bajargan ish?", "Nolga teng", ["Olingan issiqlikka teng", "pV ga teng", "Manfiy"], "ΔV = 0."),
    ],
    "Elektr maydon kuchlanganligi": [
        C(2, "2 nC nuqtaviy zaryaddan 30 sm masofada maydon kuchlanganligi? (k = 9·10⁹)", "200 N/C", ["60 N/C", "600 N/C", "20 N/C"], "E = kq/r² = 9·10⁹·2·10⁻⁹/0,09."),
        C(3, "Masofa 3 marta ortsa, nuqtaviy zaryad maydoni kuchlanganligi?", "9 marta kamayadi", ["3 marta kamayadi", "9 marta ortadi", "O'zgarmaydi"], "E ~ 1/r²."),
        C(3, "Zaryadlangan o'tkazgich shar ichida maydon kuchlanganligi?", "Nolga teng", ["Sirtidagidan katta", "Markazga qarab ortadi", "kq/R²"], "Zaryadlar sirtda joylashadi."),
        C(2, "Kuchlanganlik vektori musbat zaryad maydonida qayerga yo'nalgan?", "Zaryaddan tashqariga", ["Zaryad tomonga", "Aylana bo'ylab", "Yo'nalishsiz"], "Musbat sinov zaryadiga ta'sir yo'nalishi."),
    ],
    "To'liq zanjir: EYK va ichki qarshilik": [
        C(2, "EYK 12 V, ichki qarshilik 1 Ω, tashqi qarshilik 5 Ω. Zanjirdagi tok?", "2 A", ["12 A", "2,4 A", "1 A"], "I = E/(R + r)."),
        C(2, "Shu manba qisqa tutashtirilsa, tok?", "12 A", ["2 A", "6 A", "Cheksiz"], "I = E/r."),
        C(3, "Tashqi zanjirda eng katta quvvat qachon ajraladi?", "R = r bo'lganda", ["R = 0 da", "R → ∞ da", "R = 2r da"], "Moslashtirilgan yuklama sharti."),
        C(3, "EYK 12 V, r = 1 Ω, R = 5 Ω bo'lsa, manba qisqichlaridagi kuchlanish?", "10 V", ["12 V", "2 V", "6 V"], "U = IR = 2·5."),
    ],
    "Elektromagnit induksiya": [
        C(2, "100 o'ramli g'altakdagi magnit oqimi 0,2 s da 0,6 Wb ga o'zgardi. Induksiya EYK?", "300 V", ["3 V", "12 V", "30 V"], "ε = NΔΦ/Δt."),
        C(3, "Lens qoidasiga ko'ra induksion tok?", "O'zini hosil qilgan oqim o'zgarishiga qarshilik qiladi", ["Oqimni doim kuchaytiradi", "Oqimga bog'liq emas", "Faqat o'zgarmas tok hosil qiladi"], "Energiya saqlanishining natijasi."),
        C(2, "Magnitni g'altak ichida qimirlatmay tutib tursak, induksion tok?", "Hosil bo'lmaydi", ["Doim hosil bo'ladi", "Maksimal bo'ladi", "Yo'nalishini o'zgartiradi"], "Oqim o'zgarmaydi."),
        C(3, "Generatorda mexanik energiya qanday energiyaga aylanadi?", "Elektr energiyasiga", ["Issiqlikka", "Yorug'likka", "Kimyoviy energiyaga"], "Elektromagnit induksiya hodisasi."),
    ],
    "O'zinduksiya va magnit maydon energiyasi": [
        C(2, "Induktivligi 0,5 Gn g'altakdan 4 A tok o'tmoqda. Magnit maydon energiyasi?", "4 J", ["2 J", "8 J", "1 J"], "W = LI²/2 = 0,5·16/2."),
        C(3, "Shu g'altakda tok 10 A/s tezlikda o'zgarsa, o'zinduksiya EYK?", "5 V", ["50 V", "20 V", "0,5 V"], "ε = L·ΔI/Δt."),
        C(3, "Tok 2 marta oshirilsa, g'altak magnit maydoni energiyasi?", "4 marta ortadi", ["2 marta ortadi", "O'zgarmaydi", "2 marta kamayadi"], "W ~ I²."),
        C(2, "Induktivlik birligi?", "Genri", ["Veber", "Tesla", "Farad"], "1 Gn = 1 Wb/A."),
    ],
    "Elektromagnit tebranishlar (LC kontur)": [
        C(3, "L = 0,1 Gn, C = 10 mkF bo'lgan konturning tebranish davri taxminan?", "6,28 ms", ["0,63 ms", "62,8 ms", "1 ms"], "T = 2π√(LC) = 2π·10⁻³ s."),
        C(2, "Kondensator sig'imi 4 marta oshirilsa, kontur tebranish davri?", "2 marta ortadi", ["4 marta ortadi", "2 marta kamayadi", "O'zgarmaydi"], "T ~ √C."),
        C(3, "LC konturda kondensator to'liq zaryadlangan paytda g'altakdagi tok?", "Nolga teng", ["Maksimal", "Yarmiga teng", "Doim o'zgarmas"], "Energiya to'liq elektr maydonda."),
        C(2, "Tebranish konturida qaysi energiyalar o'zaro aylanadi?", "Elektr va magnit maydon energiyalari", ["Issiqlik va yorug'lik", "Kinetik va potensial", "Kimyoviy va elektr"], "Ideal konturda yig'indi o'zgarmas."),
    ],
    "Tovush": [
        C(2, "Tovush tezligi 340 m/s, chastotasi 170 Hz. To'lqin uzunligi?", "2 m", ["0,5 m", "57 800 m", "1 m"], "λ = v/ν."),
        C(2, "Aks-sado 3 s dan keyin eshitildi (v = 340 m/s). To'siqgacha masofa?", "510 m", ["1020 m", "340 m", "113 m"], "Tovush borib qaytadi: 340·3/2."),
        C(3, "Tovush balandligi qaysi kattalikka bog'liq?", "Chastotaga", ["Amplitudaga", "Tezlikka", "Muhit zichligiga"], "Qattiqligi — amplitudaga, balandligi — chastotaga."),
        C(2, "Tovush vakuumda tarqaladimi?", "Yo'q", ["Ha, yorug'lik tezligida", "Ha, sekinroq", "Faqat yuqori chastotalisi"], "Mexanik to'lqinga muhit kerak."),
    ],
    "Elektromagnit to'lqinlar": [
        C(2, "Chastotasi 100 MHz bo'lgan radioto'lqin uzunligi?", "3 m", ["30 m", "0,3 m", "300 m"], "λ = c/ν = 3·10⁸/10⁸."),
        C(3, "Elektromagnit to'lqinda E va B vektorlari qanday joylashgan?", "O'zaro va tarqalish yo'nalishiga perpendikulyar", ["Parallel", "Tarqalish yo'nalishiga parallel", "Faqat E perpendikulyar"], "EM to'lqin ko'ndalang."),
        C(2, "Qaysi nurlanishning to'lqin uzunligi eng qisqa?", "Gamma-nurlar", ["Radioto'lqinlar", "Infraqizil", "Ko'rinadigan yorug'lik"], "Chastota eng katta."),
        C(3, "Elektromagnit to'lqinlarni birinchi bo'lib tajribada kim hosil qilgan?", "G. Gers", ["J. Maksvell", "A. Popov", "M. Faradey"], "Maksvell nazariy bashorat qilgan."),
    ],
    "Dispersiya va qutblanish": [
        C(2, "Shisha prizmada qaysi rang eng kuchli sinadi?", "Binafsha", ["Qizil", "Sariq", "Yashil"], "Binafsha uchun sindirish ko'rsatkichi eng katta."),
        C(3, "Qutblanish hodisasi yorug'likning qanday xossasini isbotlaydi?", "Ko'ndalang to'lqin ekanini", ["Bo'ylama to'lqin ekanini", "Zarra ekanini", "Tezligi cheksizligini"], "Faqat ko'ndalang to'lqin qutblanadi."),
        C(2, "Kamalak qaysi hodisa natijasida hosil bo'ladi?", "Dispersiya", ["Qutblanish", "Fotoeffekt", "Interferensiya"], "Tomchilarda oq yorug'lik ranglarga ajraladi."),
        C(3, "Ikki qutblagich o'qlari perpendikulyar bo'lsa, o'tgan yorug'lik?", "Deyarli o'tmaydi", ["To'liq o'tadi", "Yarmi o'tadi", "Ikki baravar kuchayadi"], "Malyus qonuni: I = I₀cos²90° = 0."),
    ],
    "Maxsus nisbiylik nazariyasi": [
        C(3, "Kosmik kema 0,6c tezlikda uchmoqda. Kemadagi 10 s yer kuzatuvchisi uchun qancha davom etadi?", "12,5 s", ["8 s", "10 s", "16 s"], "γ = 1/√(1 − 0,36) = 1,25."),
        C(3, "Shu kemadagi 1 m uzunlikdagi sterjen (harakat yo'nalishida) yerdan qanday ko'rinadi?", "0,8 m", ["1,25 m", "1 m", "0,6 m"], "l = l₀/γ."),
        C(2, "Nisbiylik nazariyasining ikkinchi postulati?", "Vakuumda yorug'lik tezligi barcha inersial sanoq sistemalarida bir xil", ["Barcha tezliklar qo'shiladi", "Vaqt hamma joyda bir xil", "Massa doim o'zgarmas"], "c = const."),
        C(2, "Massasi 1 kg jismning tinchlikdagi energiyasi?", "9·10¹⁶ J", ["3·10⁸ J", "9·10⁸ J", "1 J"], "E = mc²."),
    ],
    "Issiqlik nurlanishi va Plank gipotezasi": [
        C(3, "Quyosh sirti temperaturasi ~5800 K. Nurlanish maksimumi to'lqin uzunligi taxminan? (b = 2,9·10⁻³ m·K)", "500 nm", ["5 mkm", "50 nm", "290 nm"], "Vin: λ = b/T."),
        C(3, "Absolyut qora jism temperaturasi 2 marta oshsa, nurlanish quvvati?", "16 marta ortadi", ["4 marta", "2 marta", "8 marta"], "Stefan–Bolsman: P ~ T⁴."),
        C(2, "Plank gipotezasiga ko'ra energiya qanday nurlanadi?", "Alohida porsiyalar (kvantlar) bilan", ["Uzluksiz", "Faqat to'lqin bilan", "Faqat yuqori temperaturada"], "E = hν."),
        C(2, "Jism qizdirilganda rangi qizildan oqqa o'tishi nimani bildiradi?", "Nurlanish maksimumi qisqa to'lqinlarga siljiydi", ["Jism soviydi", "Nurlanish kamayadi", "Rang o'zgarmaydi"], "Vin qonuni."),
    ],
    "Atom yadrosi va bog'lanish energiyasi": [
        C(2, "²³⁸₉₂U yadrosida nechta neytron bor?", "146", ["92", "238", "330"], "N = A − Z."),
        C(3, "Massa defekti 0,03 m.a.b. Bog'lanish energiyasi taxminan? (1 m.a.b. ≈ 931,5 MeV)", "28 MeV", ["2,8 MeV", "280 MeV", "0,03 MeV"], "0,03·931,5 ≈ 27,9."),
        C(2, "Izotoplar bir-biridan nima bilan farq qiladi?", "Neytronlar soni bilan", ["Protonlar soni bilan", "Elektronlar soni bilan", "Kimyoviy xossalari bilan"], "Z bir xil, A har xil."),
        C(3, "Yarim yemirilish davri 8 kun. 24 kundan keyin dastlabki yadrolarning qancha qismi qoladi?", "1/8", ["1/3", "1/4", "1/16"], "3 ta yarim davr: (1/2)³."),
    ],
    "Yadro reaksiyalari, bo'linish va sintez": [
        C(2, "Alfa-yemirilishda yadro massa soni va zaryadi qanday o'zgaradi?", "A − 4, Z − 2", ["A − 2, Z − 4", "A, Z + 1", "A − 1, Z"], "Alfa-zarra — ⁴₂He."),
        C(2, "Beta-minus yemirilishda?", "A o'zgarmaydi, Z bittaga ortadi", ["A − 4, Z − 2", "Z bittaga kamayadi", "A bittaga ortadi"], "Neytron protonga aylanadi."),
        C(3, "Quyosh energiyasining manbai?", "Yengil yadrolar sintezi (termoyadro reaksiyasi)", ["Og'ir yadrolar bo'linishi", "Kimyoviy yonish", "Radioaktiv yemirilish"], "Vodorod geliyga aylanadi."),
        C(3, "Zanjir reaksiyasi uchun nima zarur?", "Kritik massa va bo'linishda ko'payuvchi neytronlar", ["Yuqori bosim", "Juda past temperatura", "Faqat alfa-zarralar"], "Har bo'linish yangi bo'linishlarga sabab bo'ladi."),
    ],
    "Elementar zarralar va kvarklar": [
        C(2, "Proton qanday kvarklardan tuzilgan?", "uud", ["udd", "uuu", "ud̄"], "Zaryad: 2/3 + 2/3 − 1/3 = +1."),
        C(2, "Elektronning antizarrasi?", "Pozitron", ["Proton", "Neytrino", "Foton"], "Zaryadi +e, massasi elektronniki bilan teng."),
        C(3, "Neytron kvark tarkibi?", "udd", ["uud", "ddd", "uus"], "2/3 − 1/3 − 1/3 = 0."),
        C(3, "Zarra va antizarra uchrashganda nima sodir bo'ladi?", "Annigilyatsiya — energiya (fotonlar) ajraladi", ["Yangi yadro hosil bo'ladi", "Hech narsa", "Ular birikadi"], "Massa energiyaga aylanadi."),
    ],
    "MKT asoslari, mol va Avogadro doimiysi": [
        C(2, "36 g suvda necha mol modda bor?", "2 mol", ["36 mol", "0,5 mol", "18 mol"], "ν = m/M = 36/18."),
        C(3, "2 mol moddada nechta molekula bor?", "1,2·10²⁴", ["6·10²³", "3·10²³", "2·10²³"], "N = νN_A."),
        C(2, "Diffuziya qaysi holatda eng tez boradi?", "Gazlarda", ["Qattiq jismlarda", "Suyuqliklarda", "Barchasida bir xil"], "Molekulalar orasi katta, harakat erkin."),
        C(3, "Broun harakatini nima keltirib chiqaradi?", "Suyuqlik molekulalarining tartibsiz urilishlari", ["Konveksiya oqimlari", "Yorug'lik bosimi", "Gravitatsiya"], "Zarra molekulalar zarbalarida tebranadi."),
    ],
    "Ideal gaz holat tenglamasi": [
        C(3, "2 mol ideal gaz 300 K da 0,05 m³ hajmni egallaydi. Bosim taxminan? (R = 8,31)", "≈100 kPa", ["≈10 kPa", "≈1 MPa", "≈50 kPa"], "p = νRT/V = 99 720 Pa."),
        C(2, "Bosim va temperatura 2 martadan oshsa, gaz hajmi?", "O'zgarmaydi", ["4 marta ortadi", "2 marta kamayadi", "4 marta kamayadi"], "V ~ T/p."),
        C(3, "Normal sharoitda 1 mol ideal gaz hajmi?", "22,4 L", ["1 L", "11,2 L", "24,5 L"], "0 °C, 101,3 kPa."),
        C(2, "Klapeyron–Mendeleyev tenglamasi?", "pV = (m/M)RT", ["pV = const", "p/T = const", "pV = mRT"], "Ideal gaz holat tenglamasi."),
    ],
    "To'yingan bug', namlik va qaynash": [
        C(2, "Havo nisbiy namligi 60%, shu temperaturada to'yingan bug' bosimi 2,33 kPa. Suv bug'ining parsial bosimi taxminan?", "1,4 kPa", ["2,33 kPa", "3,9 kPa", "0,6 kPa"], "p = φ·p₀."),
        C(3, "Tog'da suv nima uchun 100 °C dan past temperaturada qaynaydi?", "Atmosfera bosimi kamroq", ["Havo sovuqroq", "Suv tozaroq", "Kislorod ko'p"], "Qaynash: to'yingan bug' bosimi = tashqi bosim."),
        C(2, "Shudring nuqtasi nima?", "Bug' to'yinib, kondensatsiya boshlanadigan temperatura", ["Suv qaynaydigan temperatura", "Muz eriydigan temperatura", "Eng yuqori namlik"], "Havo shu temperaturagacha sovisa shudring tushadi."),
        C(3, "Temperatura oshganda (bug' miqdori o'zgarmasa) nisbiy namlik?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "100% ga yetadi"], "To'yingan bug' bosimi ortadi."),
    ],
    "Sirt taranglik, kapillyarlik va Laplas bosimi": [
        C(3, "Radiusi 0,5 mm kapillyarda suv qancha balandlikka ko'tariladi? (σ = 0,073 N/m, ρ = 1000, g = 10)", "≈2,9 sm", ["≈29 sm", "≈0,3 sm", "≈1,5 sm"], "h = 2σ/(ρgr) ≈ 0,029 m."),
        C(2, "Kapillyar radiusi 2 marta kichraysa, suyuqlik ko'tarilish balandligi?", "2 marta ortadi", ["2 marta kamayadi", "4 marta ortadi", "O'zgarmaydi"], "h ~ 1/r."),
        C(2, "Sovun qo'shilganda suvning sirt tarangligi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Nolga teng"], "Sirt-aktiv modda."),
        C(3, "Simob shisha kapillyarda qanday harakat qiladi?", "Pasayadi (ho'llamaydi)", ["Ko'tariladi", "O'zgarmaydi", "To'liq to'ldiradi"], "Ho'llamaydigan suyuqlik — qavariq menisk."),
    ],
    "Qattiq jismlarning mexanik xossalari": [
        C(2, "Ko'ndalang kesimi 1 mm² simga 1000 N kuch ta'sir qilmoqda. Mexanik kuchlanish?", "10⁹ Pa", ["10⁶ Pa", "10³ Pa", "10¹² Pa"], "σ = F/S = 1000/10⁻⁶."),
        C(3, "Guk qonuni qaysi deformatsiyalar uchun o'rinli?", "Elastik (kichik) deformatsiyalar", ["Plastik", "Har qanday", "Faqat siqilish"], "Mutanosiblik chegarasigacha."),
        C(2, "Kristall jismlarning amorf jismlardan farqi?", "Aniq erish temperaturasi bor", ["Erish temperaturasi yo'q", "Doim shaffof", "Har doim yumshoq"], "Masalan, muz va shisha."),
        C(3, "Bir xil simning uzunligi 2 marta oshirilsa, bir xil kuch ta'sirida absolyut uzayish?", "2 marta ortadi", ["O'zgarmaydi", "2 marta kamayadi", "4 marta ortadi"], "Δl = Fl/(ES)."),
    ],
    "Adiabata, ikkinchi qonun va Karno sikli": [
        C(3, "Karno sikli qanday jarayonlardan iborat?", "Ikki izoterma va ikki adiabata", ["Ikki izobara va ikki izoxora", "To'rt izoterma", "Izobara va adiabata"], "Ideal qaytar sikl."),
        C(2, "Termodinamikaning ikkinchi qonuniga ko'ra issiqlik o'z-o'zidan?", "Faqat issiq jismdan sovuqqa o'tadi", ["Sovuqdan issiqqa o'tadi", "Ikki tomonga bir xil", "Umuman o'tmaydi"], "Klauzius ta'rifi."),
        C(3, "Adiabatik siqilishda gaz temperaturasi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Nolga tushadi"], "Tashqi kuch ishi ichki energiyaga aylanadi (dizel yonishi)."),
        C(3, "Muzlatkich ichidan issiqlikni olib chiqish uchun nima zarur?", "Tashqi manba ishi (kompressor)", ["Hech narsa", "Faqat freon", "Yorug'lik"], "Ikkinchi qonun: ish sarflanishi kerak."),
    ],
    "Potensial, kuchlanish va maydon ishi": [
        C(2, "2 nC zaryaddan 30 sm masofadagi potensial? (k = 9·10⁹)", "60 V", ["200 V", "6 V", "600 V"], "φ = kq/r."),
        C(3, "1 mkC zaryadni potensiallar farqi 60 V bo'lgan nuqtalar orasida ko'chirishda maydon ishi?", "6·10⁻⁵ J", ["60 J", "6·10⁻³ J", "1,7·10⁻⁸ J"], "A = qU."),
        C(3, "Ekvipotensial sirt bo'ylab zaryad ko'chirilganda maydon ishi?", "Nolga teng", ["Maksimal", "qE·d", "Manfiy"], "U = 0."),
        C(2, "Elektronvolt — bu?", "Energiya birligi", ["Kuchlanish birligi", "Zaryad birligi", "Quvvat birligi"], "1 eV = 1,6·10⁻¹⁹ J."),
    ],
    "Suyuqlik, gaz va yarimo'tkazgichlarda tok": [
        C(2, "Elektrolitlarda tokni qanday zarralar tashiydi?", "Musbat va manfiy ionlar", ["Faqat elektronlar", "Faqat protonlar", "Neytronlar"], "Elektrolitik dissotsiatsiya."),
        C(3, "Yarimo'tkazgich temperaturasi oshsa, qarshiligi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Cheksiz bo'ladi"], "Erkin zaryad tashuvchilar soni ortadi."),
        C(3, "p-tip yarimo'tkazgichda asosiy zaryad tashuvchilar?", "Kovaklar", ["Elektronlar", "Ionlar", "Protonlar"], "Akseptor aralashma."),
        C(2, "Yashin — bu gazlarda qanday razryad?", "Uchqunli razryad", ["Yolqinli razryad", "Tojsimon razryad", "Elektroliz"], "Juda katta kuchlanishda."),
    ],
}


def extend(packs: list) -> int:
    from .gen_v242 import _add
    added = 0
    for pack in packs:
        if pack.get("subject") == "math":
            added += _add(pack, MATH)
        elif pack.get("subject") == "physics":
            added += _add(pack, PHYS)
    return added
