"""Kimyo: qo'shimcha mavzular (davriy jadval, oksidlanish darajasi, tenglashtirish, o'g'itlar, termokimyo va h.k.)."""
from ._dsl import C, O, M
from ._ph import N, ON

Q = {}

Q["K8.11"] = [
    C(1, "Davriy jadvalda gorizontal qatorlar nima deb ataladi?", "Davrlar", ["Guruhlar", "Oilalar", "Bloklar"], "Gorizontal qator — davr."),
    C(1, "Davriy jadvalda vertikal ustunlar nima deb ataladi?", "Guruhlar", ["Davrlar", "Qatorlar", "Seriyalar"], "Vertikal ustun — guruh."),
    N(1, "Davriy jadvalda nechta davr bor?", 7, [5, 8, 9], "", "Yettita davr."),
    C(2, "Davriy jadvaldagi elementning tartib raqami fizik jihatdan nimani ifodalaydi?", "Yadro zaryadini (protonlar sonini)", ["Neytronlar sonini", "Atom massasini", "Valent elektronlarni"], "Z = protonlar soni."),
    N(2, "3-davrda nechta element bor?", 8, [2, 18, 10], "", "Na dan Ar gacha 8 ta."),
    C(2, "Davr bo'ylab chapdan o'ngga metallik xossalar qanday o'zgaradi?", "Kamayadi", ["Ortadi", "O'zgarmaydi", "Avval ortadi, keyin kamayadi"], "Metallmaslik kuchayadi."),
    ON(3, "Xlor (Cl) davriy jadvalning nechanchi davrida joylashgan? (raqam)", 3, "Xlor — 3-davr, VII A guruh."),
]

Q["K8.12"] = [
    N(1, "H₂O dagi kislorodning oksidlanish darajasi?", -2, [2, 0, -1], "", "Kislorod odatda −2."),
    N(1, "Oddiy moddalarda (O₂, Fe) element oksidlanish darajasi?", 0, [1, -1, 2], "", "Oddiy moddalarda 0."),
    N(2, "H₂SO₄ dagi oltingugurtning oksidlanish darajasi?", 6, [4, -2, 2], "", "2 + x − 8 = 0 → +6."),
    N(2, "KMnO₄ dagi marganetsning oksidlanish darajasi?", 7, [4, 6, 2], "", "1 + x − 8 = 0 → +7."),
    N(2, "NH₃ dagi azotning oksidlanish darajasi?", -3, [3, 0, -1], "", "x + 3 = 0 → −3."),
    C(3, "Fe₂O₃ dagi temirning oksidlanish darajasi?", "+3", ["+2", "+6", "+1"], "2x − 6 = 0."),
    ON(3, "K₂Cr₂O₇ dagi xromning oksidlanish darajasi (son)?", 6, "2 + 2x − 14 = 0 → +6."),
]

Q["K8.13"] = [
    C(1, "H₂ + O₂ → H₂O tenglamaning to'g'ri tenglashtirilgani?", "2H₂ + O₂ → 2H₂O", ["H₂ + O₂ → 2H₂O", "2H₂ + 2O₂ → 2H₂O", "H₂ + 2O₂ → H₂O"], "Har ikki tomonda 4 H va 2 O."),
    C(1, "Mg + O₂ → MgO tenglamaning to'g'ri tenglashtirilgani?", "2Mg + O₂ → 2MgO", ["Mg + O₂ → MgO", "Mg + O₂ → 2MgO", "2Mg + 2O₂ → 2MgO"], "2 Mg, 2 O."),
    N(2, "N₂ + 3H₂ → 2NH₃ tenglamadagi koeffitsientlar yig'indisi?", 6, [5, 4, 3], "", "1 + 3 + 2 = 6."),
    N(2, "4Al + 3O₂ → 2Al₂O₃ tenglamadagi koeffitsientlar yig'indisi?", 9, [7, 8, 6], "", "4 + 3 + 2 = 9."),
    N(3, "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O tenglamadagi koeffitsientlar yig'indisi?", 13, [12, 11, 10], "", "1 + 5 + 3 + 4 = 13."),
    ON(3, "2Fe + 3Cl₂ → 2FeCl₃ tenglamada Cl₂ oldidagi koeffitsientni yozing.", 3, "6 ta Cl atomi."),
]

Q["K9.16"] = [
    C(1, "Qaysi metall vodorodni suyultirilgan kislotalardan siqib chiqara olmaydi?", "Mis", ["Rux", "Temir", "Magniy"], "Mis vodoroddan keyin turadi."),
    C(1, "Quyidagilardan qaysi biri eng faol metall?", "Natriy", ["Mis", "Kumush", "Oltin"], "Natriy — ishqoriy metall."),
    C(2, "Zn + CuSO₄ ni aralashtirsak nima bo'ladi?", "Rux misni siqib chiqaradi", ["Reaksiya bormaydi", "Mis ruxni siqib chiqaradi", "Gaz ajraladi"], "Zn faolroq."),
    C(2, "Cu + HCl (suyultirilgan) reaksiyasi?", "Bormaydi", ["Vodorod ajraladi", "CuCl₂ + H₂ hosil bo'ladi", "Portlash bo'ladi"], "Mis vodoroddan keyin."),
    C(2, "Fe + CuSO₄ reaksiya mahsulotlari?", "FeSO₄ + Cu", ["Fe₂(SO₄)₃ + Cu", "CuFe + SO₄", "Reaksiya bormaydi"], "Temir (II) sulfat va mis."),
    C(3, "Faollik kamayish tartibini toping.", "Mg > Zn > Fe > Cu", ["Cu > Fe > Zn > Mg", "Zn > Mg > Cu > Fe", "Fe > Mg > Zn > Cu"], "Kuchlanish qatori."),
    ON(3, "6,5 g rux xlorid kislota bilan reaksiyaga kirishganda (Zn + 2HCl → ZnCl₂ + H₂) necha litr vodorod (n.sh.) ajraladi?", 2.24, "6,5/65 = 0,1 mol; V = 0,1·22,4 = 2,24 l."),
]

Q["K10.11"] = [
    C(1, "Tabiiy gazning asosiy tarkibiy qismi?", "Metan", ["Etan", "Propan", "Vodorod"], "CH₄ ≈ 95%."),
    C(1, "Neft qanday aralashma?", "Uglevodorodlar aralashmasi", ["Faqat spirtlar", "Sof modda", "Faqat suv va tuzlar"], "Alkanlar, sikloalkanlar, arenlar."),
    C(2, "Neftni fraksiyalarga ajratish usuli?", "Fraksiyalab haydash (rektifikatsiya)", ["Filtrlash", "Elektroliz", "Kristallash"], "Qaynash haroratlari farqiga asoslangan."),
    C(2, "Krekking nima?", "Katta molekulali uglevodorodlarni kichiklariga parchalash", ["Uglevodorodlarni polimerlash", "Spirtni suvsizlantirish", "Metanni yoqish"], "Termik yoki katalitik."),
    C(2, "Benzin fraksiyasida uglerod atomlari soni taxminan?", "5–11", ["1–4", "20–30", "40 dan ko'p"], "C₅–C₁₁."),
    C(3, "Oktan soni nimani ko'rsatadi?", "Benzinning detonatsiyaga chidamliligini", ["Qaynash haroratini", "Zichligini", "Yonish issiqligini"], "Oktan soni yuqori — sifatli."),
    O(3, "Neftni fraksiyalarga ajratish jarayonining nomini yozing (bir so'z).", ["rektifikatsiya", "haydash", "fraksiyalab haydash"], "Fraksiyalab haydash — rektifikatsiya."),
]

Q["K11.13"] = [
    C(1, "C vitaminining kimyoviy nomi?", "Askorbin kislota", ["Retinol", "Tiamin", "Kalsiferol"], "Askorbin kislota."),
    C(1, "Aspirinning kimyoviy nomi?", "Atsetilsalitsil kislota", ["Askorbin kislota", "Sirka kislota", "Salitsil spirt"], "Og'riq qoldiruvchi."),
    C(2, "Insulin qaysi turdagi moddalarga kiradi?", "Oqsil tabiatli gormon", ["Vitamin", "Uglevod", "Yog'"], "Peptid gormon."),
    C(2, "Penitsillin qaysi guruh dori vositasi?", "Antibiotik", ["Vitamin", "Gormon", "Og'riq qoldiruvchi"], "A. Fleming kashfiyoti."),
    C(2, "A vitamini nimada eriydi?", "Yog'da", ["Suvda", "Spirtda faqat", "Hech nimada"], "Yog'da eriydigan vitamin."),
    C(3, "Gormonlar nima?", "Ichki sekretsiya bezlari ishlab chiqaradigan biologik faol moddalar", ["Fermentlar", "Vitaminlar", "Mineral tuzlar"], "Qon orqali tarqaladi."),
    O(3, "Qandli diabetda yetishmaydigan gormon nomini yozing.", ["insulin"], "Insulin."),
]

Q["K8.14"] = [
    M(1, [("Na", "Natriy"), ("K", "Kaliy"), ("Fe", "Temir")], "Element belgilari."),
    C(1, "Au belgisi qaysi elementga tegishli?", "Oltin", ["Kumush", "Alyuminiy", "Argon"], "Aurum — oltin."),
    C(1, "Ag belgisi qaysi elementga tegishli?", "Kumush", ["Oltin", "Alyuminiy", "Argon"], "Argentum — kumush."),
    C(2, "Pb belgisi qaysi elementga tegishli?", "Qo'rg'oshin", ["Fosfor", "Platina", "Qalay"], "Plumbum."),
    C(2, "Hg belgisi qaysi elementga tegishli?", "Simob", ["Vodorod", "Gelyy", "Marganets"], "Hydrargyrum."),
    C(3, "Sn belgisi qaysi elementga tegishli?", "Qalay", ["Rux", "Selen", "Kremniy"], "Stannum."),
    O(3, "Kaliy elementining kimyoviy belgisini yozing.", ["K", "k"], "Kalium — K."),
]

Q["K8.15"] = [
    C(1, "NaCl dagi kimyoviy bog'lanish turi?", "Ionli", ["Kovalent qutbsiz", "Metall", "Vodorod"], "Metall va metallmas."),
    C(1, "H₂O molekulasida bog'lanish turi?", "Kovalent qutbli", ["Ionli", "Kovalent qutbsiz", "Metall"], "O–H bog'i qutbli."),
    C(2, "O₂ molekulasida bog'lanish turi?", "Kovalent qutbsiz", ["Kovalent qutbli", "Ionli", "Vodorod"], "Bir xil atomlar."),
    C(2, "Ionli birikmalarga xos xossa?", "Erish harorati yuqori, eritmasi tok o'tkazadi", ["Past erish harorati", "Tok o'tkazmaydi", "Gaz holatida"], "Kristall panjara ionli."),
    C(2, "HCl molekulasida bog'lanish turi?", "Kovalent qutbli", ["Ionli", "Kovalent qutbsiz", "Metall"], "Elektromanfiylik farqi bor."),
    C(3, "Quyidagilardan qaysi birida faqat kovalent bog'lanish bor?", "CH₄", ["NaCl", "KBr", "MgO"], "Metan — organik, kovalent."),
    ON(3, "N₂ molekulasida nechta umumiy elektron juft bor? (son)", 3, "N≡N uchlamchi bog'."),
]

Q["K9.17"] = [
    C(1, "Korroziya nima?", "Metallarning muhit ta'sirida emirilishi", ["Metallarning erishi", "Metallarning kristallanishi", "Metallarning magnitlanishi"], "Kimyoviy yoki elektrokimyoviy."),
    C(1, "Temir zanglashi uchun nima zarur?", "Kislorod va namlik", ["Faqat quruq havo", "Faqat azot", "Vakuum"], "O₂ + H₂O."),
    C(2, "Metallni korroziyadan himoya qilish usuli?", "Bo'yash yoki qoplash", ["Namlash", "Kislotaga solish", "Qizdirish"], "Himoya qoplama."),
    C(2, "Galvanizatsiya nima?", "Temirni rux bilan qoplash", ["Temirni mis bilan eritish", "Temirni suvga solish", "Temirni bo'yash"], "Rux qatlami."),
    C(2, "Zangning asosiy tarkibi?", "Fe₂O₃·nH₂O", ["FeSO₄", "Fe(NO₃)₃", "FeCl₂"], "Gidratlangan temir (III) oksid."),
    C(3, "Protektor himoyada temir quvurga qaysi metall biriktiriladi?", "Magniy", ["Mis", "Kumush", "Oltin"], "Faolroq metall o'zi emiriladi."),
    O(3, "Temir, xrom va nikeldan iborat korroziyaga chidamli qotishma nomi (ikki so'z)?", ["zanglamas po'lat", "zanglamas pulat"], "Zanglamas po'lat."),
]

Q["K9.18"] = [
    C(1, "Olmosning kristall panjarasi turi?", "Atom", ["Molekulyar", "Ionli", "Metall"], "Atomlar kovalent bog'langan."),
    C(1, "Muzning kristall panjarasi turi?", "Molekulyar", ["Atom", "Ionli", "Metall"], "H₂O molekulalari."),
    C(2, "NaCl kristall panjarasi turi?", "Ionli", ["Atom", "Molekulyar", "Metall"], "Na⁺ va Cl⁻ ionlari."),
    C(2, "Metallarning plastikligi ularning qaysi xususiyati bilan bog'liq?", "Metall kristall panjara", ["Ionli panjara", "Molekulyar panjara", "Atom panjara"], "Erkin elektronlar."),
    C(2, "Molekulyar panjarali moddalar xossasi?", "Past erish harorati, uchuvchan", ["Juda qattiq", "Yuqori erish harorati", "Tok o'tkazadi"], "Zaif molekulalararo kuchlar."),
    C(3, "Quyidagilardan qaysi biri eng qattiq?", "Olmos", ["Grafit", "NaCl", "Muz"], "Atom panjarasi."),
    ON(3, "NaCl kristalida Na⁺ ioni atrofida nechta Cl⁻ ioni bor? (son)", 6, "Koordinatsion son 6."),
]

Q["K9.19"] = [
    C(1, "Azotli o'g'itga misol?", "Ammiakli selitra", ["Superfosfat", "Kaliy xlorid", "Ohak"], "NH₄NO₃."),
    C(1, "Fosforli o'g'itga misol?", "Superfosfat", ["Mochevina", "Kaliy xlorid", "Ammiakli selitra"], "Ca(H₂PO₄)₂."),
    C(2, "Kaliyli o'g'itga misol?", "Kaliy xlorid", ["Superfosfat", "Mochevina", "Ammofos"], "KCl."),
    C(2, "Ammiakli selitraning formulasi?", "NH₄NO₃", ["(NH₄)₂SO₄", "NaNO₃", "KNO₃"], "Ammoniy nitrat."),
    C(2, "Karbamid (mochevina) formulasi?", "(NH₂)₂CO", ["NH₄Cl", "(NH₄)₂CO₃", "NH₂OH"], "Eng ko'p azotli o'g'itlardan."),
    N(3, "NH₄NO₃ dagi azotning massa ulushi necha foiz? (Mr = 80)", 35, [28, 17.5, 70], "%", "28/80 = 0,35."),
    ON(3, "Ammiakli selitrada nechta azot atomi bor? (son)", 2, "NH₄NO₃: bitta NH₄⁺ va bitta NO₃⁻."),
]

Q["K9.20"] = [
    C(1, "Kislotali yomg'ir hosil bo'lishiga asosan sabab bo'ladigan gazlar?", "SO₂ va azot oksidlari", ["O₂ va N₂", "He va Ne", "H₂ va CH₄"], "Kislotalar hosil qiladi."),
    C(1, "Issiqxona effektini kuchaytiruvchi asosiy gaz?", "Karbonat angidrid", ["Azot", "Argon", "Kislorod"], "CO₂."),
    C(2, "Ozon qatlamini yemiruvchi moddalar?", "Freonlar", ["Azot", "Argon", "Suv bug'i"], "Xlorftoruglerodlar."),
    C(2, "SO₂ + H₂O → ?", "H₂SO₃", ["H₂SO₄", "H₂S", "SO₃"], "Sulfit kislota."),
    C(2, "Ozonning formulasi?", "O₃", ["O₂", "O", "O₄"], "Kislorodning allotropik shakli."),
    C(3, "Kislotali yomg'irning pH qiymati odatda qanday?", "5,6 dan past", ["7 ga teng", "9 dan yuqori", "14 ga teng"], "Oddiy yomg'ir ham biroz kislotali (≈5,6)."),
    O(3, "Avtomobil gazlaridagi zaharli uglerod oksidi (is gazi) formulasini yozing.", ["CO", "co"], "Is gazi — CO."),
]

Q["K10.12"] = [
    C(1, "CH₃–CH₂–CH₃ moddaning nomi?", "Propan", ["Butan", "Etan", "Metan"], "3 ta C atomi."),
    C(1, "C₂H₅OH ning nomi?", "Etanol", ["Metanol", "Propanol", "Glitserin"], "Etil spirti."),
    C(2, "CH₃–CH(CH₃)–CH₃ ning nomi?", "2-metilpropan", ["Butan", "Pentan", "2-metilbutan"], "Izobutan."),
    C(2, "CH₃COOH ning nomi?", "Etan kislota (sirka kislota)", ["Metan kislota", "Propan kislota", "Etanol"], "Sirka kislota."),
    C(2, "CH₂=CH₂ ning nomi?", "Eten (etilen)", ["Etan", "Etin", "Propen"], "Qo'sh bog'li."),
    C(3, "CH₃–CH=CH–CH₃ ning nomi?", "2-buten", ["1-buten", "Butan", "2-butin"], "Qo'sh bog' 2-o'rinda."),
    O(3, "CH₄ uglevodorodining nomini yozing.", ["metan", "Metan"], "Metan."),
]

Q["K10.13"] = [
    N(2, "CH₄ + 2O₂ → CO₂ + 2H₂O. 1 mol metan yonishiga necha mol kislorod kerak?", 2, [1, 3, 4], "mol", "Tenglamadan."),
    N(2, "11,2 l (n.sh.) metan yonganda necha litr CO₂ hosil bo'ladi?", 11.2, [22.4, 5.6, 44.8], "l", "1 mol CH₄ → 1 mol CO₂."),
    N(3, "2 mol etilen (C₂H₄) to'liq yonganda necha mol CO₂ hosil bo'ladi?", 4, [2, 6, 8], "mol", "C₂H₄ + 3O₂ → 2CO₂ + 2H₂O."),
    N(3, "1 mol propan (C₃H₈) to'liq yonishiga necha mol O₂ kerak?", 5, [3, 4, 7], "mol", "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O."),
    N(3, "44 g propan (Mr = 44) to'liq yonganda necha litr CO₂ (n.sh.) hosil bo'ladi?", 67.2, [22.4, 44.8, 89.6], "l", "1 mol propan → 3 mol CO₂ = 67,2 l."),
    ON(3, "2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O. 1 mol atsetilen yonganda necha mol suv hosil bo'ladi?", 1, "2 mol → 2 mol; 1 mol → 1 mol."),
]

Q["K11.14"] = [
    N(1, "1 mol gazning normal sharoitdagi hajmi necha litr?", 22.4, [11.2, 24, 44.8], "l", "Molyar hajm."),
    N(2, "2 mol gazning n.sh. dagi hajmi?", 44.8, [22.4, 11.2, 67.2], "l", "2·22,4."),
    N(2, "11,2 l (n.sh.) gaz necha mol?", 0.5, [1, 2, 0.25], "mol", "11,2/22,4."),
    C(2, "Avogadro qonuni: bir xil sharoitda teng hajmli gazlarda...", "Molekulalar soni teng bo'ladi", ["Massa teng bo'ladi", "Zichlik teng bo'ladi", "Molyar massa teng bo'ladi"], "Teng hajmlarda molekulalar soni teng."),
    N(3, "O₂ ning H₂ ga nisbatan nisbiy zichligi?", 16, [8, 32, 2], "", "32/2 = 16."),
    ON(3, "5,6 l (n.sh.) gaz necha mol? (o'nli kasr)", 0.25, "5,6/22,4 = 0,25."),
]

Q["K11.15"] = [
    C(1, "Ekzotermik reaksiyada nima sodir bo'ladi?", "Issiqlik ajraladi", ["Issiqlik yutiladi", "Massa kamayadi", "Gaz ajraladi"], "ΔH < 0."),
    C(1, "Endotermik reaksiyada nima sodir bo'ladi?", "Issiqlik yutiladi", ["Issiqlik ajraladi", "Yorug'lik chiqadi", "Portlash bo'ladi"], "ΔH > 0."),
    C(2, "Yonish reaksiyalari odatda qanday?", "Ekzotermik", ["Endotermik", "Almashinish", "Qaytmas bo'lmagan"], "Issiqlik chiqadi."),
    C(2, "ΔH < 0 bo'lsa reaksiya?", "Ekzotermik", ["Endotermik", "Neytral", "Muvozanatli"], "Entalpiya kamayadi."),
    C(3, "Gess qonuni nimani ifodalaydi?", "Reaksiya issiqlik effekti oraliq bosqichlarga bog'liq emas", ["Massaning saqlanishini", "Gaz hajmlarining nisbatini", "Reaksiya tezligini"], "Boshlang'ich va oxirgi holatga bog'liq."),
    N(3, "C + O₂ → CO₂ + 393 kJ. 2 mol C yonganda qancha issiqlik (kJ) ajraladi?", 786, [393, 1179, 196.5], "kJ", "2·393."),
    O(3, "Issiqlik effekti birligini yozing (kJ/...).", ["kJ/mol", "kj/mol", "kJ/моль"], "kJ/mol."),
]
