"""Kimyo: 11-sinf — kislorodli va azotli organik birikmalar, polimerlar, umumiy kimyo va masalalar."""
from ._dsl import C, O, M

Q = {}

Q["K11.1"] = [
    C(1, "Spirtlarning funksional guruhi qaysi?", "–OH", ["–CHO", "–COOH", "–NH₂"], "Gidroksil guruh."),
    C(1, "Etanolning formulasi qaysi?", "C₂H₅OH", ["CH₃OH", "C₃H₇OH", "CH₃CHO"], "Etil spirti."),
    C(1, "Glitserin necha atomli spirt?", "Uch atomli", ["Bir atomli", "Ikki atomli", "To'rt atomli"], "CH₂(OH)–CH(OH)–CH₂(OH)."),
    C(2, "Glitserinning sifat reaksiyasida Cu(OH)₂ bilan qanday rang hosil bo'ladi?", "Yorqin ko'k eritma", ["Qizil cho'kma", "Sariq cho'kma", "Rangsizlanish"], "Mis(II) glitserat kompleksi."),
    C(2, "Etanol natriy bilan reaksiyaga kirishsa, qaysi mahsulotlar hosil bo'ladi?", "C₂H₅ONa va H₂", ["C₂H₄ va NaOH", "CH₃CHO va H₂", "C₂H₆ va Na₂O"], "2C₂H₅OH + 2Na → 2C₂H₅ONa + H₂."),
    C(2, "Fenol qaysi reagent bilan oq cho'kma hosil qiladi?", "Bromli suv", ["Ohakli suv", "NaCl eritmasi", "Fenolftalein"], "2,4,6-tribromfenol cho'kmasi."),
    C(2, "Spirtlarning qaynash harorati mos alkanlarnikidan yuqori bo'lishiga sabab nima?", "Molekulalararo vodorod bog'lar", ["Katta molekulyar massa", "Ion bog'lar", "Uchlamchi bog'lar"], "–OH guruhlari vodorod bog' hosil qiladi."),
    M(2, [("Etanol", "bir atomli spirt"), ("Etilen glikol", "ikki atomli spirt"), ("Glitserin", "uch atomli spirt")], "Spirtlar tasnifi."),
    C(3, "Etanol konsentrlangan H₂SO₄ bilan 140 °C da qizdirilsa, asosiy mahsulot qaysi?", "Dietil efir", ["Etilen", "Atsetilen", "Sirka aldegidi"], "Molekulalararo degidratatsiya; 170 °C da — etilen."),
    C(3, "4,6 g etanol (M = 46) natriy bilan reaksiyaga kirishsa, n.sh. da necha litr H₂ ajraladi?", "1,12 l", ["2,24 l", "0,56 l", "4,48 l"], "n = 0,1 mol → n(H₂) = 0,05 mol."),
    O(3, "9,2 g glitserin (M = 92) ortiqcha natriy bilan to'liq reaksiyaga kirishsa, necha mol H₂ ajraladi? (faqat son, vergul bilan)", ["0,15", "0.15", "0,15 mol", "0.15 mol"], "0,1 mol · 3 OH / 2 = 0,15 mol."),
]

Q["K11.2"] = [
    C(1, "Aldegidlarning funksional guruhi qaysi?", "–CHO", ["–OH", "–COOH", "–CO–"], "Karbonil guruh uglerod zanjirining chetida."),
    C(1, "Formaldegidning suvdagi eritmasi qanday ataladi?", "Formalin", ["Aseton", "Fenol", "Glitserin"], "HCHO ning ~40% li eritmasi."),
    C(1, "Eng sodda keton qaysi?", "Aseton (propanon)", ["Formaldegid", "Etanal", "Metanol"], "CH₃–CO–CH₃."),
    C(2, "Kumush ko'zgu reaksiyasida aldegid Ag₂O ning ammiakli eritmasi bilan reaksiyaga kirishsa, nima hosil bo'ladi?", "Karbon kislota va Ag", ["Spirt va Ag₂O", "Keton va H₂", "Alkan va CO₂"], "R–CHO + Ag₂O → R–COOH + 2Ag."),
    C(2, "Aldegid qaytarilsa, qaysi modda hosil bo'ladi?", "Birlamchi spirt", ["Ikkilamchi spirt", "Karbon kislota", "Keton"], "R–CHO + H₂ → R–CH₂OH."),
    C(2, "Aldegid Cu(OH)₂ bilan qizdirilganda qanday cho'kma hosil bo'ladi?", "G'isht-qizil Cu₂O", ["Ko'k Cu(OH)₂", "Qora CuO", "Oq CuCl"], "Aldegidlarga xos sifat reaksiyasi."),
    C(2, "Ikkilamchi spirt oksidlansa, qaysi modda hosil bo'ladi?", "Keton", ["Aldegid", "Karbon kislota", "Alkan"], "Masalan, izopropanol → aseton."),
    M(2, [("Kumush ko'zgu reaksiyasi", "Ag cho'kadi"), ("Cu(OH)₂ bilan qizdirish", "Cu₂O g'isht-qizil cho'kma"), ("H₂ (Ni) bilan", "birlamchi spirt")], "Aldegidlarning reaksiyalari."),
    C(3, "CH₃CHO + Ag₂O → CH₃COOH + 2Ag. 4,4 g etanaldan (M = 44) necha gramm Ag olinadi?", "21,6 g", ["10,8 g", "43,2 g", "4,4 g"], "n = 0,1 mol → n(Ag) = 0,2 mol → 0,2 · 108 = 21,6 g."),
    C(3, "1 mol formaldegid Ag₂O ning ammiakli eritmasi bilan to'liq oksidlanganda necha mol Ag hosil bo'ladi?", "4 mol", ["2 mol", "1 mol", "3 mol"], "HCHO → CO₂ gacha oksidlanadi: 4 elektron."),
    O(3, "Propanalning (C₂H₅CHO) molyar massasi necha g/mol? (faqat son)", ["58"], "C₃H₆O: 36 + 6 + 16 = 58."),
]

Q["K11.3"] = [
    C(1, "Karbon kislotalarning funksional guruhi qaysi?", "–COOH", ["–OH", "–CHO", "–NH₂"], "Karboksil guruh."),
    C(1, "Chumoli kislotaning formulasi qaysi?", "HCOOH", ["CH₃COOH", "C₂H₅COOH", "C₁₇H₃₅COOH"], "Metan kislota."),
    C(1, "Karbon kislotalar lakmusni qanday rangga bo'yaydi?", "Qizil", ["Ko'k", "Sariq", "Rangsiz qoldiradi"], "Kislotali muhit."),
    C(2, "Stearin kislotaning formulasi qaysi?", "C₁₇H₃₅COOH", ["C₁₅H₃₁COOH", "C₁₇H₃₃COOH", "C₁₇H₃₁COOH"], "To'yingan yuqori karbon kislota."),
    C(2, "Karbon kislota va spirt o'zaro ta'sirlashganda qanday modda hosil bo'ladi?", "Murakkab efir", ["Oddiy efir", "Aldegid", "Keton"], "Efirlanish reaksiyasi."),
    C(2, "CH₃COOH + NaHCO₃ reaksiyasida qanday gaz ajraladi?", "CO₂", ["H₂", "O₂", "CO"], "CH₃COOH + NaHCO₃ → CH₃COONa + H₂O + CO₂↑."),
    C(2, "Qaysi karbon kislota aldegidlarga xos kumush ko'zgu reaksiyasini beradi?", "Chumoli kislota", ["Sirka kislota", "Propion kislota", "Stearin kislota"], "HCOOH molekulasida aldegid guruhi ham bor."),
    M(2, [("HCOOH", "chumoli kislota"), ("CH₃COOH", "sirka kislota"), ("C₁₇H₃₅COOH", "stearin kislota")], "Karbon kislotalar nomlari."),
    C(3, "6 g CH₃COOH (M = 60) NaHCO₃ bilan reaksiyaga kirishsa, n.sh. da necha litr CO₂ ajraladi?", "2,24 l", ["4,48 l", "1,12 l", "6 l"], "n = 0,1 mol = n(CO₂)."),
    C(3, "0,5 mol sirka kislota va 0,5 mol etanol reaksiyasidan unum 80% bo'lsa, necha gramm etilatsetat (M = 88) hosil bo'ladi?", "35,2 g", ["44 g", "28,2 g", "17,6 g"], "0,5 · 0,8 = 0,4 mol; 0,4 · 88 = 35,2 g."),
    O(3, "CH₃COOH va C₂H₅OH dan hosil bo'ladigan murakkab efirning nomini yozing.", ["etil asetat", "etilatsetat", "etilasetat", "etil etanoat"], "CH₃COOC₂H₅."),
]

Q["K11.4"] = [
    C(1, "Yog'lar qanday moddalar efirlari?", "Glitserin va yuqori karbon kislotalar", ["Etanol va sirka kislota", "Glyukoza va fruktoza", "Metanol va chumoli kislota"], "Trigliseridlar."),
    C(1, "Yog'larni ishqor bilan gidrolizlash jarayoni qanday ataladi?", "Sovunlanish", ["Vulkanizatsiya", "Gidrogenlash", "Krekinglash"], "Sovun va glitserin hosil bo'ladi."),
    C(1, "Sovun qanday modda?", "Yuqori karbon kislotalarning natriy (kaliy) tuzi", ["Glitserin", "Yuqori spirt", "Aldegid"], "Masalan, C₁₇H₃₅COONa."),
    C(2, "Suyuq yog'lar tarkibida qanday kislota qoldiqlari ko'proq bo'ladi?", "To'yinmagan", ["To'yingan", "Faqat sirka", "Faqat chumoli"], "Masalan, olein kislota."),
    C(2, "Qattiq yog'lar tarkibida asosan qanday kislotalar qoldig'i bor?", "To'yingan (palmitin, stearin)", ["Linol", "Olein", "Arxidon"], "To'yingan kislotalar yog'ni qattiq qiladi."),
    C(2, "Suyuq yog'larni gidrogenlash natijasida nima olinadi?", "Qattiq yog' (margarin asosi)", ["Glitserin", "Sovun", "Spirt"], "Qo'shbog'lar to'yinadi."),
    C(2, "Murakkab efir kislotali muhitda to'liq gidrolizlanganda qaysi moddalar hosil bo'ladi?", "Karbon kislota va spirt", ["Aldegid va suv", "Alkan va CO₂", "Faqat spirt"], "Efirlanishga teskari reaksiya."),
    M(2, [("C₁₅H₃₁COOH", "palmitin kislota"), ("C₁₇H₃₅COOH", "stearin kislota"), ("C₁₇H₃₃COOH", "olein kislota")], "Yuqori karbon kislotalar."),
    C(3, "Tristearin + 3NaOH → glitserin + 3C₁₇H₃₅COONa. 1 mol tristearin dan necha mol sovun hosil bo'ladi?", "3 mol", ["1 mol", "2 mol", "6 mol"], "Uchta efir bog'i uziladi."),
    C(3, "Olein kislota C₁₇H₃₃COOH molekulasida nechta qo'shbog' (C=C) bor?", "1", ["0", "2", "3"], "CₙH₂ₙ₋₁COOH — bitta C=C."),
    O(3, "Yog'lar gidrolizida hosil bo'ladigan uch atomli spirtning nomini yozing.", ["glitserin", "glisserin", "propantriol-1,2,3"], "Glitserin."),
]

Q["K11.5"] = [
    C(1, "Glyukozaning molekulyar formulasi qaysi?", "C₆H₁₂O₆", ["C₁₂H₂₂O₁₁", "(C₆H₁₀O₅)ₙ", "C₅H₁₀O₅"], "Monosaxarid."),
    C(1, "Saxarozaning molekulyar formulasi qaysi?", "C₁₂H₂₂O₁₁", ["C₆H₁₂O₆", "(C₆H₁₀O₅)ₙ", "C₁₂H₂₄O₁₂"], "Disaxarid."),
    C(1, "Kraxmal va sellyuloza qaysi uglevodlar guruhiga kiradi?", "Polisaxaridlar", ["Monosaxaridlar", "Disaxaridlar", "Aminokislotalar"], "(C₆H₁₀O₅)ₙ."),
    C(2, "Glyukoza qanday tuzilishga ega?", "Aldegidospirt", ["Ketonospirt", "Karbon kislota", "Oddiy efir"], "Tarkibida –CHO va –OH guruhlar bor."),
    C(2, "Saxaroza gidrolizlanganda qaysi moddalar hosil bo'ladi?", "Glyukoza va fruktoza", ["Faqat glyukoza", "Glyukoza va galaktoza", "Kraxmal va suv"], "C₁₂H₂₂O₁₁ + H₂O → C₆H₁₂O₆ + C₆H₁₂O₆."),
    C(2, "Kraxmalning sifat reaksiyasi qaysi?", "Yod eritmasi bilan ko'k rang", ["Kumush ko'zgu", "Bromli suvni rangsizlantirish", "FeCl₃ bilan binafsha rang"], "Kraxmal + I₂ → ko'k."),
    C(2, "Glyukozaning spirtli bijg'ishi mahsulotlari qaysi?", "C₂H₅OH va CO₂", ["CH₃COOH va H₂", "C₃H₇OH va O₂", "CH₃CHO va CO"], "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂."),
    M(2, [("Glyukoza", "monosaxarid"), ("Saxaroza", "disaxarid"), ("Kraxmal", "polisaxarid")], "Uglevodlar tasnifi."),
    C(3, "180 g glyukoza spirtli bijg'ishga uchrasa, n.sh. da necha litr CO₂ ajraladi? (M(C₆H₁₂O₆) = 180)", "44,8 l", ["22,4 l", "89,6 l", "67,2 l"], "n = 1 mol → n(CO₂) = 2 mol."),
    C(3, "342 g saxaroza to'liq gidrolizlanganda hosil bo'lgan monosaxaridlarning umumiy massasi qancha? (M(saxaroza) = 342)", "360 g", ["342 g", "180 g", "378 g"], "Gidrolizga 1 mol suv (18 g) sarflanadi: 342 + 18 = 360."),
    O(3, "90 g glyukoza Ag₂O ning ammiakli eritmasi bilan to'liq oksidlansa, necha mol Ag hosil bo'ladi? (faqat son)", ["1", "1 mol"], "n(glyukoza) = 0,5 mol; har bir mol 2 mol Ag beradi."),
]

Q["K11.6"] = [
    C(1, "Aminlar qaysi modda hosilalari hisoblanadi?", "Ammiak", ["Metan", "Suv", "Etilen"], "NH₃ dagi H atomlari radikallarga almashgan."),
    C(1, "Eng sodda alifatik amin qaysi?", "Metilamin CH₃NH₂", ["Anilin", "Etilamin", "Dimetilamin"], "Birlamchi amin."),
    C(1, "Anilinning formulasi qaysi?", "C₆H₅NH₂", ["C₆H₅OH", "C₆H₅NO₂", "CH₃NH₂"], "Aromatik amin."),
    C(2, "Aminlar qanday kimyoviy xossaga ega?", "Asos xossasi", ["Kislota xossasi", "Amfoter xossa", "Inert"], "Azotdagi juft elektron proton biriktiradi."),
    C(2, "Anilin bromli suv bilan reaksiyaga kirishsa, nima kuzatiladi?", "2,4,6-tribromanilinning oq cho'kmasi", ["Ko'k rang", "Gaz ajralishi", "Hech narsa"], "Anilinga xos sifat reaksiyasi."),
    C(2, "Nitrobenzolni anilinga aylantirish reaksiyasi kim nomi bilan ataladi?", "Zinin reaksiyasi", ["Kucherov reaksiyasi", "Vyurs reaksiyasi", "Konovalov reaksiyasi"], "C₆H₅NO₂ → C₆H₅NH₂."),
    C(2, "(CH₃)₂NH qanday amin?", "Ikkilamchi amin", ["Birlamchi amin", "Uchlamchi amin", "To'rtlamchi amin"], "Azot atomi ikkita radikal bilan bog'langan."),
    M(2, [("CH₃NH₂", "birlamchi amin"), ("(CH₃)₂NH", "ikkilamchi amin"), ("(CH₃)₃N", "uchlamchi amin")], "Aminlar tasnifi."),
    C(3, "Quyidagilarni asoslik kuchi kamayish tartibida joylashtiring.", "Metilamin > ammiak > anilin", ["Anilin > ammiak > metilamin", "Ammiak > metilamin > anilin", "Metilamin > anilin > ammiak"], "Alkil guruh asoslikni oshiradi, fenil kamaytiradi."),
    C(3, "9,3 g anilin (M = 93) ortiqcha bromli suv bilan reaksiyaga kirishsa, necha gramm 2,4,6-tribromanilin (M = 330) hosil bo'ladi?", "33 g", ["16,5 g", "9,3 g", "66 g"], "n = 0,1 mol → 0,1 · 330 = 33 g."),
    O(3, "Metilaminning molyar massasi necha g/mol? (faqat son)", ["31"], "CH₅N: 12 + 5 + 14 = 31."),
]

Q["K11.7"] = [
    C(1, "Aminokislota molekulasida qaysi funksional guruhlar bor?", "–NH₂ va –COOH", ["–OH va –CHO", "–NO₂ va –OH", "–CO– va –NH₂"], "Amino va karboksil."),
    C(1, "Oqsillar qanday moddalarning polimeri?", "Aminokislotalar", ["Glyukoza", "Etilen", "Glitserin"], "Peptid bog'lar orqali."),
    C(1, "Eng sodda aminokislota qaysi?", "Glitsin (aminosirka kislota)", ["Alanin", "Valin", "Seril"], "NH₂CH₂COOH."),
    C(2, "Peptid bog'ning tuzilishi qaysi?", "–CO–NH–", ["–CO–O–", "–NH–NH–", "–C≡N"], "Amid bog'."),
    C(2, "Oqsillarning biuret reaksiyasida qanday rang hosil bo'ladi?", "Binafsha", ["Sariq", "Ko'k", "Qizil"], "Cu(OH)₂ va ishqor ishtirokida."),
    C(2, "Oqsillarning ksantoprotein reaksiyasida (konsentrlangan HNO₃) qanday rang hosil bo'ladi?", "Sariq", ["Binafsha", "Yashil", "Rangsiz"], "Aromatik halqalar nitrlanadi."),
    C(2, "Aminokislotalar nima uchun amfoter xossaga ega?", "Ham kislotali (–COOH), ham asosli (–NH₂) guruh bor", ["Faqat –NH₂ guruhi bor", "Ular tuzlar", "Ular uglevodlar"], "Ham kislota, ham asos bilan reaksiyaga kirishadi."),
    M(2, [("Biuret reaksiyasi", "binafsha rang"), ("Ksantoprotein reaksiyasi", "sariq rang"), ("Denaturatsiya", "oqsil tuzilishining buzilishi")], "Oqsillar xossalari."),
    C(3, "10 ta aminokislotadan hosil bo'lgan chiziqli peptidda nechta peptid bog' bor?", "9", ["10", "11", "8"], "n aminokislota — n − 1 ta peptid bog'."),
    C(3, "Glitsin NH₂CH₂COOH ning molyar massasi qancha?", "75 g/mol", ["89 g/mol", "60 g/mol", "61 g/mol"], "14 + 2 + 12 + 2 + 12 + 32 + 1 = 75."),
    O(3, "5 ta aminokislotadan hosil bo'lgan chiziqli peptidda nechta peptid bog' bor? (faqat son)", ["4", "to'rt"], "5 − 1 = 4."),
]

Q["K11.8"] = [
    C(1, "Polietilenning monomeri qaysi?", "Etilen", ["Propilen", "Stirol", "Vinilxlorid"], "nCH₂=CH₂ → (–CH₂–CH₂–)ₙ."),
    C(1, "Polivinilxloridning (PVX) monomeri qaysi?", "Vinilxlorid", ["Etilen", "Stirol", "Tetraftoretilen"], "CH₂=CHCl."),
    C(1, "Polimerlanish darajasi nimani bildiradi?", "Makromolekuladagi monomer bo'g'inlari sonini", ["Polimer zichligini", "Suyuqlanish haroratini", "Zaryadini"], "n qiymati."),
    C(2, "Polikondensatsiya reaksiyasi polimerlanishdan nimasi bilan farq qiladi?", "Past molekulyar modda (masalan, suv) ajraladi", ["Hech narsa ajralmaydi", "Faqat gaz ajraladi", "Faqat qo'shbog'li monomerlar ishtirok etadi"], "Kapron, lavsan — polikondensatsiya mahsulotlari."),
    C(2, "Teflonning monomeri qaysi?", "Tetraftoretilen", ["Vinilxlorid", "Stirol", "Propilen"], "CF₂=CF₂."),
    C(2, "Polistirolning monomeri qaysi?", "Stirol", ["Etilen", "Butadien", "Akrilonitril"], "C₆H₅–CH=CH₂."),
    C(2, "Kapron qanday polimer?", "Poliamid", ["Poliefir", "Poliolefin", "Polisaxarid"], "Aminokaproin kislotadan yoki kaprolaktamdan."),
    M(2, [("Polietilen", "etilen"), ("Polivinilxlorid", "vinilxlorid"), ("Polistirol", "stirol")], "Polimerlar va monomerlar."),
    C(3, "Molyar massasi 28000 bo'lgan polietilenning polimerlanish darajasi qancha? (M(C₂H₄) = 28)", "1000", ["2800", "100", "28"], "28000 : 28 = 1000."),
    C(3, "Izopren kauchuk (C₅H₈)ₙ ning molyar massasi 1360 bo'lsa, n qancha? (M(C₅H₈) = 68)", "20", ["10", "40", "68"], "1360 : 68 = 20."),
    O(3, "Polipropilenning molyar massasi 42000 (M(C₃H₆) = 42). Polimerlanish darajasi n nechaga teng? (faqat son)", ["1000"], "42000 : 42 = 1000."),
]

Q["K11.9"] = [
    C(1, "Harorat ko'tarilganda kimyoviy reaksiya tezligi odatda qanday o'zgaradi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Nolga teng bo'ladi"], "Faol to'qnashuvlar ko'payadi."),
    C(1, "Katalizator reaksiyaga qanday ta'sir qiladi?", "Tezlikni oshiradi, muvozanatni siljitmaydi", ["Muvozanatni o'ngga siljitadi", "Muvozanatni chapga siljitadi", "Reaksiyani to'xtatadi"], "Katalizator to'g'ri va teskari reaksiyani teng tezlashtiradi."),
    C(1, "Muvozanat siljishi qoidasini kim ta'riflagan?", "Le Shatelye", ["Mendeleyev", "Butlerov", "Avogadro"], "Tashqi ta'sirga qarshi tomonga siljiydi."),
    C(2, "Van't-Goff qoidasiga ko'ra harorat 10 °C ga ortganda reaksiya tezligi necha marta ortadi?", "2–4 marta", ["10 marta", "100 marta", "O'zgarmaydi"], "Harorat koeffitsiyenti γ = 2–4."),
    C(2, "Massalar ta'siri qonuniga ko'ra aA + bB → mahsulot reaksiyasi tezligi qanday ifodalanadi?", "v = k·[A]ᵃ·[B]ᵇ", ["v = k·[A] + [B]", "v = k / ([A]·[B])", "v = [A]ᵃ − [B]ᵇ"], "Konsentratsiyalar ko'paytmasiga to'g'ri proporsional."),
    C(2, "N₂ + 3H₂ ⇌ 2NH₃ muvozanatida bosim oshirilsa, muvozanat qaysi tomonga siljiydi?", "O'ngga (NH₃ hosil bo'lishi tomon)", ["Chapga", "Siljimaydi", "Avval o'ngga, keyin chapga"], "Gaz mollari soni kamayadigan tomon."),
    C(2, "Endotermik reaksiyada harorat oshirilsa, muvozanat qaysi tomonga siljiydi?", "To'g'ri reaksiya tomonga", ["Teskari reaksiya tomonga", "Siljimaydi", "Ikkala tomonga teng"], "Issiqlik yutiladigan tomon."),
    M(2, [("Katalizator", "tezlikni oshiradi, muvozanatni siljitmaydi"), ("Haroratni oshirish", "endotermik reaksiya tomon siljitadi"), ("Bosimni oshirish", "gaz mollari kamayadigan tomon siljitadi")], "Muvozanatga ta'sir omillari."),
    C(3, "Harorat koeffitsiyenti γ = 2. Harorat 30 °C ga oshirilsa, reaksiya tezligi necha marta ortadi?", "8 marta", ["6 marta", "4 marta", "16 marta"], "2³ = 8."),
    C(3, "2SO₂ + O₂ → 2SO₃ reaksiyasida v = k·[SO₂]²·[O₂]. SO₂ konsentratsiyasi 2 marta oshirilsa, tezlik necha marta ortadi?", "4 marta", ["2 marta", "8 marta", "6 marta"], "2² = 4."),
    O(3, "H₂ + I₂ ⇌ 2HI muvozanatiga bosimning o'zgarishi qanday ta'sir qiladi? (siljiydi / siljimaydi)", ["siljimaydi", "siljimaydi."], "Gaz mollari soni o'zgarmaydi (2 = 2)."),
]

Q["K11.10"] = [
    C(1, "Oksidlovchi qanday zarrachani qabul qiladi?", "Elektron", ["Proton", "Neytron", "Pozitron"], "Oksidlovchi o'zi qaytariladi."),
    C(1, "Elektrolizda anodda qanday jarayon boradi?", "Oksidlanish", ["Qaytarilish", "Neytrallanish", "Gidroliz"], "Anod — musbat elektrod."),
    C(1, "Elektrolizda katodda qanday jarayon boradi?", "Qaytarilish", ["Oksidlanish", "Parchalanish", "Kondensatsiya"], "Katod — manfiy elektrod."),
    C(2, "KMnO₄ da marganetsning oksidlanish darajasi qancha?", "+7", ["+2", "+4", "+6"], "1 + x − 8 = 0 → x = +7."),
    C(2, "K₂Cr₂O₇ da xromning oksidlanish darajasi qancha?", "+6", ["+3", "+7", "+2"], "2 + 2x − 14 = 0 → x = +6."),
    C(2, "NaCl suvli eritmasi elektroliz qilinganda katodda qaysi modda ajraladi?", "H₂", ["Na", "Cl₂", "O₂"], "Faol metall kationi o'rniga suv qaytariladi."),
    C(2, "NaCl suyuqlanmasi elektroliz qilinganda qaysi mahsulotlar olinadi?", "Na va Cl₂", ["NaOH va H₂", "Na₂O va Cl₂", "H₂ va Cl₂"], "Katodda Na, anodda Cl₂."),
    M(2, [("Katod", "qaytarilish jarayoni"), ("Anod", "oksidlanish jarayoni"), ("Oksidlovchi", "elektron qabul qiladi")], "Elektroliz va OQR."),
    C(3, "Cu(NO₃)₂ eritmasi elektrolizida katodda 6,4 g Cu ajraldi. Anodda n.sh. da necha litr O₂ ajraladi?", "1,12 l", ["2,24 l", "0,56 l", "4,48 l"], "n(Cu) = 0,1 mol → 0,2 mol e⁻ → n(O₂) = 0,05 mol."),
    C(3, "KMnO₄ + HCl reaksiyasida (Mn⁺⁷ → Mn⁺²) bitta Mn atomi nechta elektron qabul qiladi?", "5", ["7", "2", "3"], "+7 → +2: 5 ta elektron."),
    O(3, "CuCl₂ eritmasi elektroliz qilinganda katodda 0,2 mol Cu ajraldi. Anodda necha mol Cl₂ ajraladi? (faqat son, vergul bilan)", ["0,2", "0.2", "0,2 mol", "0.2 mol"], "CuCl₂ → Cu + Cl₂: nisbat 1 : 1."),
]

Q["K11.11"] = [
    C(1, "Quyidagi qatorlardan qaysi biri metallning genetik qatoriga mos keladi?", "Ca → CaO → Ca(OH)₂ → CaCO₃", ["Ca → CaCO₃ → CaO → Ca", "C → CO₂ → H₂CO₃ → CO", "S → SO₂ → H₂S → S"], "Metall → asosli oksid → asos → tuz."),
    C(1, "Nometallning genetik qatori qaysi?", "S → SO₂ → H₂SO₃ → Na₂SO₃", ["Na → Na₂O → NaOH", "Ca → CaO → Ca(OH)₂", "Fe → FeO → Fe(OH)₂"], "Nometall → kislotali oksid → kislota → tuz."),
    C(1, "CaCO₃ qizdirilganda qaysi moddalar hosil bo'ladi?", "CaO va CO₂", ["Ca va CO₂", "Ca(OH)₂ va CO", "CaC₂ va O₂"], "CaCO₃ → CaO + CO₂."),
    C(2, "C₂H₅OH → C₂H₄ o'zgarishi uchun qaysi sharoit kerak?", "Konsentrlangan H₂SO₄, 170 °C", ["NaOH, 100 °C", "HCl, 20 °C", "H₂, Ni"], "Molekula ichida degidratatsiya."),
    C(2, "CH₄ → C₂H₂ o'zgarishi qaysi sharoitda boradi?", "1500 °C da piroliz", ["20 °C da xlorlash", "Ni, 200 °C", "KMnO₄ eritmasida"], "2CH₄ → C₂H₂ + 3H₂."),
    C(2, "Na → NaOH → Na₂SO₄ zanjirida ikkinchi bosqichda qaysi reagent kerak?", "H₂SO₄", ["HCl", "CO₂", "NaCl"], "2NaOH + H₂SO₄ → Na₂SO₄ + 2H₂O."),
    C(2, "Cu → CuO → CuSO₄ → Cu(OH)₂ zanjirida oxirgi bosqichda qaysi reagent kerak?", "NaOH", ["HCl", "H₂O", "NaCl"], "CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄."),
    M(2, [("C₂H₄ → C₂H₅OH", "gidratatsiya"), ("C₂H₅OH → CH₃CHO", "oksidlanish (CuO, t)"), ("CH₃CHO → CH₃COOH", "oksidlanish (Ag₂O, NH₃)")], "Organik moddalar o'zgarishlari."),
    C(3, "C₂H₂ → CH₃CHO → CH₃COOH → CH₃COONa → CH₄ zanjirida oxirgi bosqichda qaysi reagent va sharoit kerak?", "NaOH, suyuqlantirish", ["H₂O, 100 °C", "HCl, 20 °C", "Na, eritma"], "Dyuma reaksiyasi."),
    C(3, "FeS₂ → SO₂ → SO₃ → H₂SO₄ → CuSO₄ zanjirida oxirgi bosqichda qaysi modda ishlatiladi?", "CuO", ["Cu (suyultirilgan kislota bilan)", "NaCl", "H₂O"], "CuO + H₂SO₄ → CuSO₄ + H₂O."),
    O(3, "CaC₂ → X → CH₃CHO zanjirida X moddaning formulasini yozing.", ["C2H2", "C₂H₂", "atsetilen"], "CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂; C₂H₂ + H₂O → CH₃CHO."),
]

Q["K11.12"] = [
    C(1, "Aralashma massasi qanday topiladi?", "Komponentlar massalari yig'indisi", ["Komponentlar massalari ko'paytmasi", "Kattaroq komponent massasi", "Komponentlar massalari ayirmasi"], "Massa additiv kattalik."),
    C(1, "Reaksiya unumi qanday topiladi?", "η = amaliy massa / nazariy massa · 100%", ["η = nazariy / amaliy · 100%", "η = amaliy + nazariy", "η = nazariy − amaliy"], "Unum 100% dan oshmaydi."),
    C(1, "Tozaligi 80% bo'lgan 100 g namunada sof moddaning massasi qancha?", "80 g", ["20 g", "100 g", "180 g"], "100 · 0,8 = 80 g."),
    C(2, "125 g CaCO₃ (tozaligi 80%) to'liq parchalanganda necha gramm CaO hosil bo'ladi? (CaCO₃ = 100, CaO = 56)", "56 g", ["70 g", "100 g", "44 g"], "m(sof) = 100 g → 1 mol → 56 g CaO."),
    C(2, "Reaksiyaning nazariy unumi 40 g, amaliy unumi 75% bo'lsa, amalda necha gramm mahsulot olinadi?", "30 g", ["53,3 g", "40 g", "10 g"], "40 · 0,75 = 30."),
    C(2, "100 g 10% li va 100 g 30% li eritmalar aralashtirilsa, massa ulush qancha bo'ladi?", "20%", ["40%", "15%", "25%"], "(10 + 30) : 200 = 0,20."),
    C(2, "0,2 mol A va 0,3 mol B moddalar 1 : 1 nisbatda reaksiyaga kirishadi. Qaysi modda ortiqcha qoladi?", "B moddadan 0,1 mol", ["A moddadan 0,1 mol", "Ikkalasi ham to'liq sarflanadi", "A moddadan 0,2 mol"], "A to'liq sarflanadi, B dan 0,1 mol ortadi."),
    M(2, [("Unum", "η = amaliy / nazariy · 100%"), ("Massa ulush", "ω = m(modda) / m(aralashma)"), ("Molyar konsentratsiya", "C_M = n / V")], "Hisoblash formulalari."),
    C(3, "10 g Zn va Cu aralashmasi ortiqcha HCl bilan reaksiyaga kirishib, 2,24 l (n.sh.) H₂ ajratdi. Aralashmada Cu ning massa ulushi qancha?", "35%", ["65%", "50%", "25%"], "n(Zn) = 0,1 mol → 6,5 g; Cu = 3,5 g → 35%."),
    C(3, "100 g 20% li NaOH eritmasiga 100 g 18,25% li HCl eritmasi qo'shildi. Hosil bo'lgan eritma muhiti qanday?", "Neytral", ["Ishqoriy", "Kislotali", "Aniqlab bo'lmaydi"], "n(NaOH) = 0,5 mol; n(HCl) = 0,5 mol."),
    O(3, "50 g CaCO₃ (tozaligi 80%) parchalanganda n.sh. da necha litr CO₂ ajraladi? (faqat son, vergul bilan)", ["8,96", "8.96"], "m(sof) = 40 g → 0,4 mol → 8,96 l."),
]
