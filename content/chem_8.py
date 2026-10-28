"""Kimyo: 8-sinf — asosiy tushunchalar, stexiometriya, oddiy va murakkab moddalar sinflari, eritmalar, atom va bog'lanish."""
from ._dsl import C, O, M

Q = {}

Q["K8.1"] = [
    C(1, "1 mol moddada nechta zarracha (atom yoki molekula) bor?", "6,02·10²³", ["6,02·10²²", "3,01·10²³", "6,02·10²⁴"], "Avogadro doimiysi N_A = 6,02·10²³ mol⁻¹."),
    C(1, "Normal sharoitda (n.sh.) 1 mol har qanday gazning hajmi qancha?", "22,4 l", ["11,2 l", "24,5 l", "44,8 l"], "Molyar hajm V_m = 22,4 l/mol."),
    C(1, "Moddaning mol miqdorini massa orqali topish formulasi qaysi?", "n = m / M", ["n = m · M", "n = m · V", "n = V · M"], "Mol = massa / molyar massa."),
    C(2, "H₂SO₄ ning molyar massasi qancha? (Ar: H=1, S=32, O=16)", "98 g/mol", ["96 g/mol", "64 g/mol", "49 g/mol"], "2·1 + 32 + 4·16 = 98."),
    C(2, "88 g karbonat angidrid (CO₂) necha mol bo'ladi?", "2 mol", ["1 mol", "4 mol", "0,5 mol"], "M(CO₂) = 44 g/mol; 88 : 44 = 2."),
    C(2, "Normal sharoitda 11,2 l kislorod (O₂) ning massasi qancha?", "16 g", ["8 g", "32 g", "11,2 g"], "n = 11,2 : 22,4 = 0,5 mol; m = 0,5 · 32 = 16 g."),
    C(2, "3 mol suvda nechta molekula bor?", "1,806·10²⁴", ["6,02·10²³", "1,806·10²³", "6,02·10²⁴"], "3 · 6,02·10²³ = 18,06·10²³ = 1,806·10²⁴."),
    M(2, [("Avogadro doimiysi", "6,02·10²³ mol⁻¹"), ("Gazning n.sh. dagi molyar hajmi", "22,4 l/mol"), ("Suvning molyar massasi", "18 g/mol")], "Asosiy kattaliklar."),
    C(3, "Quyidagi namunalarning qaysi birida atomlar soni eng ko'p?", "36 g H₂O", ["44 g CO₂", "22,4 l (n.sh.) N₂", "1 mol Ne"], "36 g H₂O = 2 mol → 6 mol atom; CO₂ — 3 mol; N₂ — 2 mol; Ne — 1 mol."),
    C(3, "Zichligi n.sh. da 1,25 g/l bo'lgan gazning molyar massasi qancha?", "28 g/mol", ["14 g/mol", "32 g/mol", "44 g/mol"], "M = ρ · V_m = 1,25 · 22,4 = 28 g/mol (N₂ yoki CO)."),
    O(3, "Normal sharoitda 5,6 l ammiak (NH₃) necha gramm keladi? (faqat son, vergul bilan)", ["4,25", "4.25", "4,25 g", "4.25 g"], "n = 0,25 mol; M(NH₃) = 17; m = 4,25 g."),
]

Q["K8.2"] = [
    C(1, "Suv (H₂O) molekulasida kislorodning valentligi nechaga teng?", "II", ["I", "III", "IV"], "Kislorod deyarli barcha birikmalarda ikki valentli."),
    C(1, "CaCO₃ ning nisbiy molekulyar massasi qancha? (Ca=40, C=12, O=16)", "100", ["84", "116", "56"], "40 + 12 + 48 = 100."),
    C(1, "Elementning massa ulushi qaysi formula bilan topiladi?", "ω = n·Ar(E) / Mr", ["ω = n·Mr / Ar(E)", "ω = Ar(E) / (n·Mr)", "ω = n + Ar(E) / Mr"], "Element atomlarining umumiy massasi modda massasiga bo'linadi."),
    C(2, "H₂SO₄ da oltingugurtning massa ulushi taxminan qancha?", "32,7%", ["16,3%", "65,3%", "2,0%"], "32 : 98 = 0,3265."),
    C(2, "Fe₂O₃ da temirning massa ulushi qancha?", "70%", ["30%", "56%", "35%"], "112 : 160 = 0,70."),
    C(2, "Fosfor(V) oksidning formulasi qaysi?", "P₂O₅", ["P₂O₃", "PO₅", "P₅O₂"], "Fosfor V valentli, kislorod II valentli → P₂O₅."),
    C(2, "Ammiak (NH₃) da azotning valentligi nechaga teng?", "III", ["I", "IV", "V"], "Azot uchta vodorod bilan bog'langan."),
    M(2, [("SO₂ da oltingugurt valentligi", "IV"), ("SO₃ da oltingugurt valentligi", "VI"), ("H₂S da oltingugurt valentligi", "II")], "Oltingugurt o'zgaruvchan valentli."),
    C(3, "Quyidagi birikmalarning qaysi birida kislorodning massa ulushi eng katta?", "H₂O", ["CO₂", "SO₂", "MgO"], "H₂O — 88,9%; CO₂ — 72,7%; SO₂ — 50%; MgO — 40%."),
    C(3, "Tarkibi 40% C, 6,7% H va 53,3% O bo'lgan moddaning eng sodda formulasi qaysi?", "CH₂O", ["C₂H₄O", "CHO", "C₂H₂O"], "C : H : O = 40/12 : 6,7/1 : 53,3/16 = 3,33 : 6,7 : 3,33 = 1 : 2 : 1."),
    O(3, "Al₂O₃ da alyuminiyning massa ulushi necha foiz? (butun songacha yaxlitlang)", ["53", "53%"], "54 : 102 = 0,529 ≈ 53%."),
]

Q["K8.3"] = [
    C(1, "Moddalar massasining saqlanish qonunini kashf etgan olimlar kimlar?", "M.V. Lomonosov va A. Lavuazye", ["D.I. Mendeleyev va A. Butlerov", "J. Dalton va A. Avogadro", "S. Arrenius va J. Gey-Lyussak"], "Reaksiyaga kirishgan moddalar massasi hosil bo'lgan moddalar massasiga teng."),
    C(1, "2H₂ + O₂ → 2H₂O reaksiyasi qaysi turga kiradi?", "Birikish", ["Parchalanish", "O'rin olish", "Almashinish"], "Ikki moddadan bitta murakkab modda hosil bo'lgan."),
    C(1, "Quyidagilardan qaysi biri parchalanish reaksiyasi?", "CaCO₃ → CaO + CO₂", ["Zn + 2HCl → ZnCl₂ + H₂", "NaOH + HCl → NaCl + H₂O", "C + O₂ → CO₂"], "Bitta moddadan ikkita modda hosil bo'ladi."),
    C(2, "Zn + 2HCl → ZnCl₂ + H₂ reaksiyasi qaysi turga kiradi?", "O'rin olish", ["Birikish", "Parchalanish", "Almashinish"], "Oddiy modda murakkab moddadagi atomni siqib chiqargan."),
    C(2, "Quyidagilardan qaysi biri almashinish reaksiyasi?", "BaCl₂ + Na₂SO₄ → BaSO₄ + 2NaCl", ["Fe + CuSO₄ → FeSO₄ + Cu", "2KClO₃ → 2KCl + 3O₂", "CaO + H₂O → Ca(OH)₂"], "Ikki murakkab modda tarkibiy qismlarini almashtirgan."),
    C(2, "Al + O₂ → Al₂O₃ reaksiya tenglamasi tenglashtirilganda koeffitsiyentlar yig'indisi nechaga teng?", "9", ["7", "8", "10"], "4Al + 3O₂ → 2Al₂O₃; 4 + 3 + 2 = 9."),
    M(2, [("2Mg + O₂ → 2MgO", "birikish"), ("CaCO₃ → CaO + CO₂", "parchalanish"), ("Fe + CuSO₄ → FeSO₄ + Cu", "o'rin olish")], "Reaksiya turlari."),
    C(2, "Quyidagi reaksiyalardan qaysi biri neytrallanish reaksiyasi?", "NaOH + HCl → NaCl + H₂O", ["Zn + H₂SO₄ → ZnSO₄ + H₂", "2H₂O → 2H₂ + O₂", "S + O₂ → SO₂"], "Asos kislota bilan reaksiyaga kirishib, tuz va suv hosil qiladi."),
    C(3, "10 g Mg yonganda 16,67 g MgO hosil bo'ldi. Reaksiyaga kirishgan kislorod massasi qancha?", "6,67 g", ["10 g", "16,67 g", "26,67 g"], "Massa saqlanish qonuni: 16,67 − 10 = 6,67 g."),
    C(3, "24,5 g KClO₃ parchalanganda (2KClO₃ → 2KCl + 3O₂) n.sh. da necha litr O₂ ajraladi? (M(KClO₃) = 122,5)", "6,72 l", ["4,48 l", "3,36 l", "11,2 l"], "n(KClO₃) = 0,2 mol → n(O₂) = 0,3 mol → 0,3 · 22,4 = 6,72 l."),
    O(3, "2KClO₃ → 2KCl + 3O₂. 0,4 mol KClO₃ dan necha mol kislorod hosil bo'ladi? (faqat son)", ["0,6", "0.6", "0,6 mol", "0.6 mol"], "0,4 · 3 / 2 = 0,6 mol."),
]

Q["K8.4"] = [
    C(1, "Havoda kislorodning hajmiy ulushi taxminan qancha?", "21%", ["78%", "1%", "50%"], "Havoning ~78% azot, ~21% kislorod."),
    C(1, "Laboratoriyada kislorod qanday olinadi?", "KMnO₄ ni qizdirib", ["Zn ni HCl ga solib", "CaC₂ ga suv ta'sir ettirib", "CaCO₃ ni HCl bilan"], "2KMnO₄ → K₂MnO₄ + MnO₂ + O₂."),
    C(1, "Kislorod haqida qaysi fikr to'g'ri?", "Yonishni qo'llab-quvvatlaydi, o'zi yonmaydi", ["O'zi yonadi", "Suvda juda yaxshi eriydi", "Havodan yengil"], "Kislorod — oksidlovchi."),
    C(2, "Kislorodni aniqlash uchun qanday usul qo'llaniladi?", "Cho'g'langan cho'p alangalanib ketadi", ["Ohakli suv loyqalanadi", "Gaz portlab «chiqillaydi»", "Lakmus qizaradi"], "Kislorodda cho'g'langan cho'p yorqin yonadi."),
    C(2, "4P + 5O₂ → 2P₂O₅ tenglamasida kislorod oldidagi koeffitsiyent nechaga teng?", "5", ["3", "2", "4"], "Fosforning yonishi."),
    C(2, "Quyidagilardan qaysi biri oksid emas?", "H₂SO₄", ["CO₂", "Fe₂O₃", "P₂O₅"], "Oksid — ikki elementdan iborat, biri kislorod bo'lgan birikma."),
    C(2, "Ozonning formulasi qaysi?", "O₃", ["O₂", "O", "H₂O₂"], "Ozon — kislorodning allotropik shakli."),
    M(2, [("Oltingugurtning yonishidan", "SO₂"), ("Fosforning yonishidan", "P₂O₅"), ("Vodorodning yonishidan", "H₂O")], "Yonish mahsulotlari."),
    C(3, "n.sh. da 5,6 l kislorod bilan necha gramm magniy to'liq yonadi? (2Mg + O₂ → 2MgO)", "12 g", ["6 g", "24 g", "3 g"], "n(O₂) = 0,25 mol → n(Mg) = 0,5 mol → 0,5 · 24 = 12 g."),
    C(3, "20 g kalsiy yonganda necha gramm CaO hosil bo'ladi?", "28 g", ["14 g", "56 g", "20 g"], "n(Ca) = 0,5 mol → n(CaO) = 0,5 mol → 0,5 · 56 = 28 g."),
    O(3, "CH₄ + 2O₂ → CO₂ + 2H₂O. n.sh. da 11,2 l metan yonishi uchun necha litr kislorod kerak? (faqat son)", ["22,4", "22.4"], "Hajmlar nisbati 1 : 2 → 11,2 · 2 = 22,4 l."),
]

Q["K8.5"] = [
    C(1, "Laboratoriyada vodorod qanday olinadi?", "Zn ga HCl ta'sir ettirib", ["CaCO₃ ga HCl ta'sir ettirib", "KMnO₄ ni qizdirib", "NH₄Cl ni NaOH bilan"], "Zn + 2HCl → ZnCl₂ + H₂↑."),
    C(1, "Eng yengil gaz qaysi?", "Vodorod", ["Geliy", "Azot", "Metan"], "Vodorodning molyar massasi 2 g/mol."),
    C(1, "Suvni elektroliz qilganda qaysi gaz katodda ajraladi?", "Vodorod", ["Kislorod", "Xlor", "Azot"], "Katodda H₂, anodda O₂ ajraladi."),
    C(2, "Suv elektrolizida ajralgan H₂ va O₂ hajmlarining nisbati qanday?", "2 : 1", ["1 : 2", "1 : 1", "3 : 1"], "2H₂O → 2H₂ + O₂."),
    C(2, "CuO + H₂ → Cu + H₂O reaksiyasida vodorod qanday vazifani bajaradi?", "Qaytaruvchi", ["Oksidlovchi", "Katalizator", "Erituvchi"], "Vodorod misni oksiddan qaytaradi."),
    C(2, "Suv molekulasida vodorod va kislorodning massa nisbati qanday?", "1 : 8", ["1 : 16", "2 : 1", "1 : 2"], "2 : 16 = 1 : 8."),
    C(2, "2Na + 2H₂O → 2NaOH + H₂ reaksiyasida 2 mol natriydan necha mol vodorod hosil bo'ladi?", "1 mol", ["2 mol", "0,5 mol", "4 mol"], "Nisbat 2 : 1."),
    M(2, [("Zn + H₂SO₄ →", "ZnSO₄ + H₂"), ("CuO + H₂ →", "Cu + H₂O"), ("2Na + 2H₂O →", "2NaOH + H₂")], "Vodorodli reaksiyalar."),
    C(3, "n.sh. da 22,4 l vodorod hosil qilish uchun kamida necha gramm Zn kerak (kislota yetarli)?", "65 g", ["32,5 g", "130 g", "22,4 g"], "Zn + 2HCl → ZnCl₂ + H₂: 1 mol Zn = 65 g."),
    C(3, "36 g suv elektroliz qilinganda n.sh. da necha litr kislorod ajraladi?", "22,4 l", ["44,8 l", "11,2 l", "33,6 l"], "n(H₂O) = 2 mol → n(O₂) = 1 mol."),
    O(3, "9 g suv to'liq elektroliz qilinganda n.sh. da necha litr vodorod ajraladi? (faqat son)", ["11,2", "11.2"], "n(H₂O) = 0,5 mol → n(H₂) = 0,5 mol → 11,2 l."),
]

Q["K8.6"] = [
    C(1, "Quyidagilardan qaysi biri ishqor?", "NaOH", ["Cu(OH)₂", "Fe(OH)₃", "Al(OH)₃"], "Suvda eriydigan asoslar ishqorlar deyiladi."),
    C(1, "Quyidagilardan qaysi biri tuz?", "NaCl", ["HCl", "NaOH", "CO₂"], "Tuz — metall kationi va kislota qoldig'idan iborat."),
    C(1, "CuSO₄ ning nomi qaysi?", "Mis(II) sulfat", ["Mis sulfit", "Mis(II) sulfid", "Mis(I) sulfat"], "SO₄²⁻ — sulfat ioni."),
    C(2, "Quyidagilardan qaysi biri amfoter oksid?", "ZnO", ["Na₂O", "CO₂", "SO₃"], "ZnO, Al₂O₃, BeO — amfoter oksidlar."),
    C(2, "Qaysi oksid suv bilan reaksiyaga kirishib kislota hosil qiladi?", "SO₃", ["CaO", "Na₂O", "MgO"], "SO₃ + H₂O → H₂SO₄."),
    C(2, "Quyidagi asoslardan qaysi biri suvda erimaydi?", "Cu(OH)₂", ["NaOH", "KOH", "Ba(OH)₂"], "Cu(OH)₂ — erimaydigan asos."),
    C(2, "Kislorodsiz kislota qaysi?", "HCl", ["H₂SO₄", "HNO₃", "H₃PO₄"], "HCl tarkibida kislorod yo'q."),
    M(2, [("Na₂O", "asosli oksid"), ("CO₂", "kislotali oksid"), ("Al₂O₃", "amfoter oksid")], "Oksidlar tasnifi."),
    C(3, "14 g CaO suv bilan reaksiyaga kirishsa, necha gramm Ca(OH)₂ hosil bo'ladi?", "18,5 g", ["14 g", "37 g", "9,25 g"], "n(CaO) = 0,25 mol; M(Ca(OH)₂) = 74; 0,25 · 74 = 18,5 g."),
    C(3, "4 g NaOH ni to'liq neytrallash uchun necha gramm H₂SO₄ kerak?", "4,9 g", ["9,8 g", "2,45 g", "19,6 g"], "H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O; n(NaOH) = 0,1 mol → n(H₂SO₄) = 0,05 mol → 4,9 g."),
    O(3, "Mg(OH)₂ ning molyar massasi necha g/mol? (faqat son)", ["58"], "24 + 2·(16 + 1) = 58."),
]

Q["K8.7"] = [
    C(1, "Eruvchanlik nima?", "Ma'lum haroratda 100 g erituvchida erishi mumkin bo'lgan moddaning maksimal massasi", ["Eritmaning 1 litridagi modda mol soni", "Erigan modda massasining eritma massasiga nisbati", "Moddaning suvdagi erish tezligi"], "Eruvchanlik koeffitsiyenti S — g/100 g suv."),
    C(1, "Harorat ortganda qattiq moddalarning suvda eruvchanligi odatda qanday o'zgaradi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Nolga tushadi"], "Ko'pchilik tuzlar issiq suvda yaxshi eriydi."),
    C(1, "Harorat ortganda gazlarning suvda eruvchanligi qanday o'zgaradi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Avval ortadi, keyin o'zgarmaydi"], "Gaz isitilganda eritmadan chiqib ketadi."),
    C(2, "Massa ulush formulasi qaysi?", "ω = m(modda) / m(eritma) · 100%", ["ω = m(modda) / m(erituvchi) · 100%", "ω = m(eritma) / m(modda) · 100%", "ω = n / V"], "Eritma massasi = modda + erituvchi."),
    C(2, "40 g tuz va 160 g suvdan tayyorlangan eritmada tuzning massa ulushi qancha?", "20%", ["25%", "40%", "16%"], "40 : 200 = 0,2."),
    C(2, "Bosim ortganda gazning suvda eruvchanligi qanday o'zgaradi? (Genri qonuni)", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Nolga teng bo'ladi"], "Gaz eruvchanligi bosimga to'g'ri proporsional."),
    C(2, "O'ta to'yingan eritma haqida qaysi fikr to'g'ri?", "Barqaror emas, ozgina ta'sirda ortiqcha modda cho'kadi", ["Unda yana modda eriydi", "Cho'kma bilan muvozanatda bo'ladi", "Faqat gazlardan hosil bo'ladi"], "O'ta to'yingan eritma barqarorsiz."),
    M(2, [("To'yinmagan eritma", "Yana modda erishi mumkin"), ("To'yingan eritma", "Cho'kma bilan muvozanatda bo'ladi"), ("O'ta to'yingan eritma", "Ozgina ta'sirda ortiqcha modda cho'kadi")], "Eritma turlari."),
    C(3, "300 g 10% li eritmaga 20 g shu tuz qo'shildi. Yangi eritmada massa ulush taxminan qancha?", "15,6%", ["12%", "16,7%", "20%"], "(30 + 20) : 320 = 0,15625."),
    C(3, "200 g 15% li eritmaga 100 g suv qo'shildi. Yangi massa ulush qancha?", "10%", ["7,5%", "5%", "12%"], "30 : 300 = 0,10."),
    O(3, "250 g 8% li eritma tayyorlash uchun necha gramm tuz kerak? (faqat son)", ["20", "20 g"], "250 · 0,08 = 20 g."),
]

Q["K8.8"] = [
    C(1, "Molyar konsentratsiya formulasi qaysi?", "C_M = n / V (litr)", ["C_M = m / V", "C_M = n · V", "C_M = V / n"], "1 litr eritmadagi modda mol miqdori."),
    C(1, "Mis kuporosining formulasi qaysi?", "CuSO₄·5H₂O", ["CuSO₄·7H₂O", "FeSO₄·7H₂O", "Na₂CO₃·10H₂O"], "Mis kuporosi — pentagidrat."),
    C(1, "Mol qism formulasi qaysi?", "X₁ = n₁ / (n₁ + n₂)", ["X₁ = n₁ · n₂", "X₁ = m₁ / m₂", "X₁ = n₁ / V"], "Mol qismlar yig'indisi 1 ga teng."),
    C(2, "0,5 mol NaOH 250 ml eritmada erigan. Molyar konsentratsiya qancha?", "2 mol/l", ["0,5 mol/l", "1 mol/l", "0,125 mol/l"], "0,5 : 0,25 = 2."),
    C(2, "ω = 98% va ρ = 1,84 g/ml bo'lgan H₂SO₄ ning molyar konsentratsiyasi qancha? (C_M = 10·ω·ρ / M)", "18,4 mol/l", ["1,84 mol/l", "9,2 mol/l", "36,8 mol/l"], "10 · 98 · 1,84 : 98 = 18,4."),
    C(2, "1 mol CuSO₄·5H₂O ning massasi qancha? (CuSO₄ = 160, H₂O = 18)", "250 g", ["160 g", "178 g", "214 g"], "160 + 5·18 = 250."),
    C(2, "Ikki komponentli eritmada X₁ + X₂ nimaga teng?", "1", ["0", "100", "2"], "Mol qismlar yig'indisi birga teng."),
    M(2, [("Mis kuporosi", "CuSO₄·5H₂O"), ("Temir kuporosi", "FeSO₄·7H₂O"), ("Kristall soda", "Na₂CO₃·10H₂O")], "Kristallogidratlar."),
    C(3, "25 g CuSO₄·5H₂O 175 g suvda eritildi. Eritmada suvsiz CuSO₄ ning massa ulushi qancha?", "8%", ["12,5%", "16%", "10%"], "n = 0,1 mol → 16 g CuSO₄; eritma 200 g; 16 : 200 = 0,08."),
    C(3, "2 mol suv va 3 mol etanoldan iborat aralashmada suvning mol qismi qancha?", "0,4", ["0,6", "0,67", "0,2"], "2 : (2 + 3) = 0,4."),
    O(3, "4 g NaOH 500 ml eritmada erigan. Molyar konsentratsiya necha mol/l? (faqat son, vergul bilan)", ["0,2", "0.2"], "n = 4 : 40 = 0,1 mol; 0,1 : 0,5 = 0,2."),
]

Q["K8.9"] = [
    C(1, "Atom yadrosi qanday zarrachalardan tashkil topgan?", "Proton va neytronlardan", ["Proton va elektronlardan", "Neytron va elektronlardan", "Faqat protonlardan"], "Elektronlar yadro atrofida harakatlanadi."),
    C(1, "Davriy qonunni kim kashf etgan va qachon?", "D.I. Mendeleyev, 1869-yil", ["A. Lavuazye, 1789-yil", "J. Dalton, 1808-yil", "N. Bor, 1913-yil"], "Elementlar xossalari atom massasiga davriy bog'liq (zamonaviy talqinda — yadro zaryadiga)."),
    C(1, "Elektronning zaryadi qanday?", "Manfiy", ["Musbat", "Zaryadsiz", "O'zgaruvchan"], "Elektron — manfiy zaryadli zarracha."),
    C(2, "Elementning tartib raqami nimani bildiradi?", "Yadrodagi protonlar sonini", ["Neytronlar sonini", "Valent elektronlar sonini", "Atom massasini"], "Z = yadro zaryadi = protonlar soni."),
    C(2, "²³₁₁Na atomida nechta neytron bor?", "12", ["11", "23", "34"], "N = A − Z = 23 − 11 = 12."),
    C(2, "Davrda chapdan o'ngga o'tganda metallik xossalari qanday o'zgaradi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Avval ortadi, keyin kamayadi"], "Nometallik xossalari kuchayadi."),
    C(2, "Guruhda yuqoridan pastga atom radiusi qanday o'zgaradi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Davriy o'zgaradi"], "Elektron qavatlar soni ortadi."),
    M(2, [("Proton", "+1 zaryad, massasi ≈ 1 m.a.b."), ("Neytron", "zaryadsiz, massasi ≈ 1 m.a.b."), ("Elektron", "−1 zaryad, massasi juda kichik")], "Elementar zarrachalar."),
    C(3, "Xlor atomining elektron konfiguratsiyasi qaysi?", "1s²2s²2p⁶3s²3p⁵", ["1s²2s²2p⁶3s²3p⁶", "1s²2s²2p⁶3s²3p³", "1s²2s²2p⁶3s¹"], "Cl (Z = 17) — 7 ta valent elektron."),
    C(3, "Fe³⁺ ionida nechta elektron bor? (Fe: Z = 26)", "23", ["26", "29", "24"], "26 − 3 = 23."),
    O(3, "Tartib raqami 16 bo'lgan elementning kimyoviy belgisini yozing.", ["S", "s", "oltingugurt"], "16-element — oltingugurt (S)."),
]

Q["K8.10"] = [
    C(1, "NaCl da qanday kimyoviy bog'lanish bor?", "Ion bog'lanish", ["Kovalent qutbli", "Kovalent qutbsiz", "Metall bog'lanish"], "Na⁺ va Cl⁻ ionlari orasida."),
    C(1, "H₂ molekulasidagi bog'lanish turi qaysi?", "Kovalent qutbsiz", ["Kovalent qutbli", "Ion", "Vodorod"], "Bir xil atomlar orasida."),
    C(1, "HCl molekulasidagi bog'lanish turi qaysi?", "Kovalent qutbli", ["Kovalent qutbsiz", "Ion", "Metall"], "Turli elektrmanfiylikdagi atomlar orasida."),
    C(2, "N₂ molekulasida atomlar orasida nechta umumiy elektron juft bor?", "3", ["1", "2", "4"], "N≡N — uchlamchi bog'."),
    C(2, "Qaysi molekulada qutbli kovalent bog' bor?", "H₂O", ["O₂", "Cl₂", "N₂"], "Faqat H₂O da turli atomlar bog'langan."),
    C(2, "Ion kristall panjarali moddalarning xossasi qaysi?", "Qattiq, yuqori haroratda suyuqlanadi, suyuqlanmasi elektr tokini o'tkazadi", ["Past haroratda suyuqlanadi va uchuvchan", "Qattiq holatda elektr tokini yaxshi o'tkazadi", "Yumshoq va oson bug'lanadi"], "Ion panjara mustahkam."),
    C(2, "Metall bog'lanish qaysi moddalarga xos?", "Metallar va qotishmalar", ["Faqat tuzlar", "Faqat gazlar", "Organik moddalar"], "Erkin elektronlar «gazi» bilan."),
    M(2, [("NaCl", "ion bog'lanish"), ("O₂", "kovalent qutbsiz bog'lanish"), ("H₂O", "kovalent qutbli bog'lanish")], "Bog'lanish turlari."),
    C(3, "Quyidagi juftliklarning qaysi birida ikkala modda ham faqat ion bog'lanishli?", "KCl va MgO", ["Cl₂ va HCl", "NH₃ va CH₄", "CO₂ va SO₂"], "Metall + nometall — ion bog'."),
    C(3, "Donor-akseptor mexanizmida bog' hosil bo'ladigan zarracha qaysi?", "NH₄⁺", ["CH₄", "CO₂", "NaCl"], "NH₃ ning juft elektroni H⁺ ga beriladi."),
    O(3, "CO₂ molekulasida nechta qo'shbog' bor? (faqat son)", ["2", "ikki", "ikkita"], "O=C=O."),
]
