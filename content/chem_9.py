"""Kimyo: 9-sinf — elektrolitlar, nometallar va metallar."""
from ._dsl import C, O, M

Q = {}

Q["K9.1"] = [
    C(1, "Eritilganda yoki suyuqlantirilganda ionlarga ajraladigan moddalar qanday ataladi?", "Elektrolitlar", ["Noelektrolitlar", "Katalizatorlar", "Indikatorlar"], "Elektrolitlar — kislotalar, ishqorlar, eruvchan tuzlar."),
    C(1, "Quyidagilardan qaysi biri kuchli elektrolit?", "HCl", ["CH₃COOH", "H₂CO₃", "NH₃·H₂O"], "HCl — kuchli kislota, to'liq dissotsiatsiyalanadi."),
    C(1, "Dissotsiatsiyalanish darajasi (α) qanday topiladi?", "α = n / N", ["α = N / (n + N)", "α = n · N", "α = n + N"], "n — dissotsiatsiyalangan, N — eritilgan molekulalar soni."),
    C(2, "Quyidagilardan qaysi biri kuchsiz elektrolit?", "H₂S", ["HNO₃", "KOH", "BaCl₂"], "H₂S, H₂CO₃, HF, HCN, H₂SiO₃ — kuchsiz kislotalar."),
    C(2, "Quyidagilardan qaysi biri noelektrolit?", "C₁₂H₂₂O₁₁ (shakar)", ["NaCl", "HCl", "KOH"], "Shakar suvda molekula holida eriydi."),
    C(2, "Al₂(SO₄)₃ ning bitta formula birligi to'liq dissotsiatsiyalanganda nechta ion hosil bo'ladi?", "5", ["2", "3", "6"], "Al₂(SO₄)₃ → 2Al³⁺ + 3SO₄²⁻."),
    C(2, "0,1 mol Ba(OH)₂ to'liq dissotsiatsiyalanganda necha mol OH⁻ ioni hosil bo'ladi?", "0,2 mol", ["0,1 mol", "0,3 mol", "0,4 mol"], "Ba(OH)₂ → Ba²⁺ + 2OH⁻."),
    M(2, [("HCl", "kuchli elektrolit"), ("CH₃COOH", "kuchsiz elektrolit"), ("C₆H₁₂O₆ (glyukoza)", "noelektrolit")], "Elektrolitlar tasnifi."),
    C(3, "0,2 mol CH₃COOH eritilgan va α = 5% bo'lsa, necha mol molekula ionlarga ajralgan?", "0,01 mol", ["0,1 mol", "0,05 mol", "0,001 mol"], "0,2 · 0,05 = 0,01."),
    C(3, "0,1 mol Na₃PO₄ to'liq dissotsiatsiyalanganda jami necha mol ion hosil bo'ladi?", "0,4 mol", ["0,3 mol", "0,1 mol", "0,5 mol"], "Na₃PO₄ → 3Na⁺ + PO₄³⁻ (4 ta ion)."),
    O(3, "1 mol Fe₂(SO₄)₃ to'liq dissotsiatsiyalanganda jami necha mol ion hosil bo'ladi? (faqat son)", ["5", "5 mol"], "2Fe³⁺ + 3SO₄²⁻ = 5 mol ion."),
]

Q["K9.2"] = [
    C(1, "Ion almashinish reaksiyalari qachon oxirigacha boradi?", "Cho'kma, gaz yoki kam dissotsiyalanuvchi modda hosil bo'lsa", ["Faqat qizdirilganda", "Faqat katalizator bo'lsa", "Har doim"], "Uchta shart: ↓, ↑ yoki H₂O."),
    C(1, "Quyidagilardan qaysi biri suvda erimaydi (cho'kma hosil qiladi)?", "BaSO₄", ["NaCl", "KNO₃", "Na₂SO₄"], "BaSO₄ — oq cho'kma."),
    C(1, "Ag⁺ + Cl⁻ → AgCl↓ qisqartirilgan ion tenglama qaysi juftlikka mos?", "AgNO₃ va NaCl", ["AgNO₃ va NaNO₃", "AgCl va HNO₃", "NaCl va KNO₃"], "AgCl — oq pishloqsimon cho'kma."),
    C(2, "H⁺ + OH⁻ → H₂O qisqartirilgan ion tenglama qaysi reaksiyaga mos?", "HCl + NaOH", ["CH₃COOH + NaOH", "Cu(OH)₂ + HCl", "H₂SiO₃ + KOH"], "Kuchli kislota va kuchli asos (ishqor) neytrallanishi."),
    C(2, "CO₃²⁻ + 2H⁺ → H₂O + CO₂↑ qisqartirilgan tenglama qaysi juftlikka mos?", "Na₂CO₃ va HCl", ["CaCO₃ va HCl", "Na₂SO₄ va HCl", "NaHCO₃ va NaOH"], "CaCO₃ erimaydi, uning formulasi ion ko'rinishida yozilmaydi."),
    C(2, "BaCl₂ + Na₂SO₄ reaksiyasining qisqartirilgan ion tenglamasi qaysi?", "Ba²⁺ + SO₄²⁻ → BaSO₄↓", ["Ba²⁺ + 2Cl⁻ → BaCl₂", "Na⁺ + Cl⁻ → NaCl", "2Na⁺ + SO₄²⁻ → Na₂SO₄"], "BaSO₄ cho'kmasi hosil bo'ladi."),
    C(2, "Quyidagi juftliklarning qaysi birida reaksiya amalda bormaydi?", "NaCl va KNO₃", ["CuSO₄ va NaOH", "BaCl₂ va H₂SO₄", "Na₂CO₃ va HCl"], "Cho'kma, gaz yoki suv hosil bo'lmaydi."),
    M(2, [("Ag⁺ + Cl⁻", "AgCl↓ — oq cho'kma"), ("Ba²⁺ + SO₄²⁻", "BaSO₄↓ — oq cho'kma"), ("Cu²⁺ + 2OH⁻", "Cu(OH)₂↓ — ko'k cho'kma")], "Sifat reaksiyalari."),
    C(3, "FeCl₃ + 3NaOH → Fe(OH)₃↓ + 3NaCl reaksiyasining to'liq ion tenglamasida chap tomondagi ionlar koeffitsiyentlari yig'indisi nechaga teng?", "10", ["7", "8", "12"], "Fe³⁺ + 3Cl⁻ + 3Na⁺ + 3OH⁻: 1 + 3 + 3 + 3 = 10."),
    C(3, "Na₂CO₃ eritmasiga 0,2 mol HCl qo'shildi. N.sh. da necha litr CO₂ ajraladi?", "2,24 l", ["4,48 l", "1,12 l", "0,224 l"], "Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂: 0,1 mol CO₂."),
    O(3, "BaCl₂ va H₂SO₄ reaksiyasida hosil bo'ladigan cho'kmaning formulasini yozing.", ["BaSO4", "BaSO₄", "baso4"], "BaSO₄ — oq cho'kma."),
]

Q["K9.3"] = [
    C(1, "Neytral muhitda pH qiymati nechaga teng (25 °C)?", "7", ["0", "14", "1"], "[H⁺] = [OH⁻] = 10⁻⁷."),
    C(1, "pH formulasi qaysi?", "pH = −lg[H⁺]", ["pH = lg[OH⁻]", "pH = [H⁺]", "pH = 14 + lg[H⁺]"], "Vodorod ko'rsatkich."),
    C(1, "Kislotali muhitda pH qanday bo'ladi?", "pH < 7", ["pH = 7", "pH > 7", "pH = 14"], "[H⁺] > 10⁻⁷."),
    C(2, "[H⁺] = 10⁻³ mol/l bo'lgan eritmaning pH i nechaga teng?", "3", ["−3", "11", "0,001"], "pH = −lg 10⁻³ = 3."),
    C(2, "pH = 11 bo'lgan eritmada [OH⁻] qancha? (K_w = 10⁻¹⁴)", "10⁻³ mol/l", ["10⁻¹¹ mol/l", "10⁻⁷ mol/l", "10⁻¹⁴ mol/l"], "pOH = 14 − 11 = 3."),
    C(2, "25 °C da suvning ion ko'paytmasi K_w nechaga teng?", "10⁻¹⁴", ["10⁻⁷", "10⁻¹", "10⁻²¹"], "K_w = [H⁺]·[OH⁻]."),
    C(2, "pH = 2 va pH = 4 bo'lgan ikki eritmada vodorod ionlari konsentratsiyasi qanday nisbatda?", "pH = 2 da 100 marta ko'p", ["pH = 2 da 2 marta ko'p", "pH = 4 da 100 marta ko'p", "Bir xil"], "10⁻² : 10⁻⁴ = 100."),
    M(2, [("pH = 3", "kislotali muhit"), ("pH = 7", "neytral muhit"), ("pH = 12", "ishqoriy muhit")], "Muhit turlari."),
    C(3, "0,001 M NaOH eritmasining pH i qancha? (NaOH to'liq dissotsiatsiyalanadi)", "11", ["3", "10", "12"], "pOH = 3 → pH = 11."),
    C(3, "0,005 mol Ba(OH)₂ 1 litr eritmada erigan. pH qancha?", "12", ["11", "2", "13"], "[OH⁻] = 0,01 → pOH = 2 → pH = 12."),
    O(3, "0,1 M HCl eritmasining pH ini yozing.", ["1"], "[H⁺] = 10⁻¹, pH = 1."),
]

Q["K9.4"] = [
    C(1, "NaCl suvli eritmasining muhiti qanday?", "Neytral (gidrolizlanmaydi)", ["Kislotali", "Ishqoriy", "Kuchsiz ishqoriy"], "Kuchli kislota va kuchli asos tuzi."),
    C(1, "Na₂CO₃ suvli eritmasining muhiti qanday?", "Ishqoriy", ["Kislotali", "Neytral", "Amfoter"], "Kuchsiz kislota va kuchli asos tuzi — anion bo'yicha gidroliz."),
    C(1, "AlCl₃ suvli eritmasining muhiti qanday?", "Kislotali", ["Ishqoriy", "Neytral", "Amfoter"], "Kuchsiz asos va kuchli kislota tuzi — kation bo'yicha gidroliz."),
    C(2, "CH₃COONa gidrolizi qaysi ion bo'yicha boradi?", "Anion bo'yicha", ["Kation bo'yicha", "Ham kation, ham anion bo'yicha", "Gidrolizlanmaydi"], "CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻."),
    C(2, "NH₄Cl suvli eritmasining muhiti va gidroliz turi qaysi?", "Kislotali, kation bo'yicha", ["Ishqoriy, anion bo'yicha", "Neytral, gidroliz yo'q", "Kislotali, anion bo'yicha"], "NH₄⁺ + H₂O ⇌ NH₃·H₂O + H⁺."),
    C(2, "Quyidagi tuzlarning qaysi biri gidrolizga uchramaydi?", "K₂SO₄", ["ZnCl₂", "Na₂S", "FeSO₄"], "K₂SO₄ — kuchli asos va kuchli kislota tuzi."),
    C(2, "Al₂S₃ suvga solinganda nima sodir bo'ladi?", "To'liq (qaytmas) gidroliz: Al(OH)₃↓ va H₂S↑", ["Tuz erib ketadi", "Faqat Al(OH)₃ hosil bo'ladi", "Reaksiya bormaydi"], "Al₂S₃ + 6H₂O → 2Al(OH)₃↓ + 3H₂S↑."),
    M(2, [("Na₃PO₄", "ishqoriy muhit"), ("Cu(NO₃)₂", "kislotali muhit"), ("KNO₃", "neytral muhit")], "Tuz eritmalari muhiti."),
    C(3, "Qaysi juftlikdagi tuzlarning suvli eritmalari ishqoriy muhitga ega?", "K₂S va Na₂SiO₃", ["NH₄Cl va FeCl₃", "NaCl va K₂SO₄", "ZnSO₄ va CuCl₂"], "Kuchsiz kislotalarning (H₂S, H₂SiO₃) ishqoriy-metall tuzlari."),
    C(3, "Quyidagi tuzlardan qaysi biri suvli eritmada mavjud bo'la olmaydi (to'liq gidrolizga uchraydi)?", "Cr₂S₃", ["Na₂S", "CuCl₂", "K₂CO₃"], "Kuchsiz asos va kuchsiz kislota tuzi ko'p hollarda to'liq gidrolizlanadi."),
    O(3, "Natriy sulfid (Na₂S) suvli eritmasining muhiti qanday? (kislotali / ishqoriy / neytral)", ["ishqoriy", "ishqor"], "S²⁻ + H₂O ⇌ HS⁻ + OH⁻."),
]

Q["K9.5"] = [
    C(1, "Galogenlar atomining tashqi qavatida nechta elektron bor?", "7", ["5", "6", "8"], "ns²np⁵."),
    C(1, "Galogenlar orasida eng faol nometall qaysi?", "Ftor", ["Xlor", "Brom", "Yod"], "Guruhda yuqoridan pastga faollik kamayadi."),
    C(1, "Xlor oddiy sharoitda qanday modda?", "O'tkir hidli sariq-yashil gaz", ["Rangsiz hidsiz gaz", "Qizil-qo'ng'ir suyuqlik", "Binafsha qattiq modda"], "Xlor zaharli, havodan og'ir."),
    C(2, "Laboratoriyada xlor olishning to'g'ri reaksiyasi qaysi?", "MnO₂ + 4HCl(kons) → MnCl₂ + Cl₂↑ + 2H₂O", ["MnO₂ + 2HCl → MnCl₂ + H₂O₂", "2NaCl + H₂SO₄ → Na₂SO₄ + 2HCl", "Zn + 2HCl → ZnCl₂ + H₂"], "Qizdirish talab etiladi."),
    C(2, "Xlorli suv tarkibida qaysi kislotalar bor?", "HCl va HClO", ["HCl va HClO₄", "HClO₃ va HClO₄", "Faqat HCl"], "Cl₂ + H₂O ⇌ HCl + HClO."),
    C(2, "Sovuq NaOH eritmasi xlor bilan reaksiyaga kirishsa, qaysi tuzlar hosil bo'ladi?", "NaCl va NaClO", ["NaCl va NaClO₃", "NaClO₃ va NaClO₄", "Faqat NaCl"], "Cl₂ + 2NaOH → NaCl + NaClO + H₂O (Javel suvi)."),
    C(2, "Issiq (qizdirilgan) NaOH eritmasi xlor bilan reaksiyaga kirishsa, qaysi tuzlar hosil bo'ladi?", "NaCl va NaClO₃", ["NaCl va NaClO", "NaClO va NaClO₄", "NaCl va NaClO₂"], "3Cl₂ + 6NaOH → 5NaCl + NaClO₃ + 3H₂O."),
    M(2, [("HClO", "gipoxlorit kislota"), ("HClO₃", "xlorat kislota"), ("HClO₄", "perxlorat kislota")], "Xlorning kislorodli kislotalari."),
    C(3, "HClO dan HClO₄ ga o'tganda kislotalar xossalari qanday o'zgaradi?", "Oksidlovchilik kamayadi, kislotalik kuchi ortadi", ["Oksidlovchilik ortadi, kislotalik kamayadi", "Ikkalasi ham ortadi", "Ikkalasi ham kamayadi"], "HClO₄ — eng kuchli kislota."),
    C(3, "0,4 mol KMnO₄ konsentrlangan HCl bilan reaksiyaga kirishsa, n.sh. da necha litr Cl₂ ajraladi? (2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O)", "22,4 l", ["44,8 l", "11,2 l", "56 l"], "n(Cl₂) = 0,4 · 5 / 2 = 1 mol."),
    O(3, "0,2 mol KMnO₄ dan HCl bilan reaksiyada necha mol Cl₂ hosil bo'ladi? (faqat son)", ["0,5", "0.5", "0,5 mol", "0.5 mol"], "0,2 · 5 / 2 = 0,5 mol."),
]

Q["K9.6"] = [
    C(1, "Xalkogenlar atomining tashqi qavatida nechta elektron bor?", "6", ["4", "5", "7"], "ns²np⁴."),
    C(1, "Ozon va kislorod bir-biriga qanday munosabatda?", "Bir elementning allotropik shakllari", ["Izotoplar", "Biri ikkinchisining oksidi", "Biri ikkinchisining peroksidi"], "O₂ va O₃ — kislorodning allotropik shakllari; ozon kuchli oksidlovchi."),
    C(1, "Vodorod sulfid (H₂S) qanday hidga ega?", "Chirigan tuxum hidi", ["Anis hidi", "Hidsiz", "Sirka hidi"], "H₂S — zaharli gaz."),
    C(2, "Oltingugurt birikmalarida qanday oksidlanish darajalarini namoyon qiladi?", "−2, 0, +4, +6", ["−1, 0, +1, +7", "−3, 0, +3, +5", "0, +2, +4"], "S: H₂S, S, SO₂, SO₃."),
    C(2, "Ozonni kisloroddan qaysi reaksiya bilan farqlash mumkin?", "KI eritmasidan yod ajratib chiqaradi", ["Ohakli suvni loyqalatadi", "Fenolftaleinni qizartiradi", "Cho'g'langan cho'pni alangalatadi"], "2KI + O₃ + H₂O → 2KOH + I₂ + O₂."),
    C(2, "Laboratoriyada H₂S olishning to'g'ri reaksiyasi qaysi?", "FeS + 2HCl → FeCl₂ + H₂S↑", ["FeS + O₂ → FeO + SO₂", "H₂ + S → H₂S (yuqori bosimda)", "Na₂S + NaOH → ..."], "Sulfidga kuchli kislota ta'sir ettiriladi."),
    C(2, "Kislorod yetarli bo'lganda H₂S yonishidan qanday mahsulotlar hosil bo'ladi?", "SO₂ va H₂O", ["S va H₂O", "SO₃ va H₂", "H₂SO₄"], "2H₂S + 3O₂ → 2SO₂ + 2H₂O."),
    M(2, [("H₂S dagi oltingugurt", "−2"), ("SO₂ dagi oltingugurt", "+4"), ("SO₃ dagi oltingugurt", "+6")], "Oltingugurtning oksidlanish darajalari."),
    C(3, "0,5 mol FeS ortiqcha HCl bilan reaksiyaga kirishsa, n.sh. da necha litr H₂S ajraladi?", "11,2 l", ["22,4 l", "5,6 l", "44,8 l"], "n(H₂S) = n(FeS) = 0,5 mol."),
    C(3, "2H₂S + O₂ → 2S + 2H₂O. 3,4 g H₂S dan necha gramm oltingugurt hosil bo'ladi? (M(H₂S) = 34)", "3,2 g", ["1,6 g", "6,4 g", "3,4 g"], "n(H₂S) = 0,1 mol → n(S) = 0,1 mol → 3,2 g."),
    O(3, "SO₂ dagi oltingugurtning oksidlanish darajasini yozing (ishora bilan).", ["+4", "4"], "S⁺⁴O₂²⁻."),
]

Q["K9.7"] = [
    C(1, "Sanoatda sulfat kislota qanday usulda olinadi?", "Kontakt usulida", ["Gaber usulida", "Sodali usulda", "Elektroliz usulida"], "Kontakt usuli: SO₂ → SO₃ → H₂SO₄."),
    C(1, "Konsentrlangan H₂SO₄ ning qaysi xossasi uni quritgich sifatida ishlatishga imkon beradi?", "Suv tortuvchanligi", ["Uchuvchanligi", "Reaksiyaga kirishmasligi", "Rangsizligi"], "U gazlarni va moddalarni quritadi."),
    C(1, "Oleum nima?", "SO₃ ning H₂SO₄ dagi eritmasi", ["H₂SO₄ ning suvdagi eritmasi", "Natriy sulfat", "Sulfit kislota"], "H₂SO₄·xSO₃."),
    C(2, "Kontakt usulida SO₂ ni SO₃ ga oksidlashda qaysi katalizator ishlatiladi?", "V₂O₅", ["Fe", "Pt", "MnO₂"], "Vanadiy(V) oksid."),
    C(2, "Kontakt usulining birinchi bosqichi qaysi?", "Pirit (FeS₂) ni kuydirish", ["SO₃ ni suvda eritish", "Oleumni suyultirish", "SO₂ ni ishqorga yuttirish"], "4FeS₂ + 11O₂ → 2Fe₂O₃ + 8SO₂."),
    C(2, "Cu qizdirilganda konsentrlangan H₂SO₄ bilan reaksiyaga kirishsa, qanday gaz ajraladi?", "SO₂", ["H₂", "SO₃", "H₂S"], "Cu + 2H₂SO₄(kons) → CuSO₄ + SO₂ + 2H₂O."),
    C(2, "Sovuq konsentrlangan H₂SO₄ da qaysi metall passivlanadi?", "Alyuminiy", ["Rux", "Mis", "Magniy"], "Fe, Cr, Al passivlanadi."),
    M(2, [("Cu + H₂SO₄ (kons)", "SO₂"), ("Zn + H₂SO₄ (suyultirilgan)", "H₂"), ("Zn + H₂SO₄ (kons)", "H₂S")], "Reaksiya mahsulotlari."),
    C(3, "2SO₂ + O₂ ⇌ 2SO₃ + Q muvozanatini SO₃ hosil bo'lish tomonga siljitish uchun nima qilish kerak?", "Bosimni oshirish va haroratni pasaytirish", ["Bosimni kamaytirish va haroratni oshirish", "Faqat katalizator qo'shish", "Haroratni ham, bosimni ham kamaytirish"], "Reaksiya ekzotermik va hajm kamayishi bilan boradi."),
    C(3, "6,4 g Cu konsentrlangan H₂SO₄ bilan qizdirilganda n.sh. da necha litr SO₂ ajraladi?", "2,24 l", ["4,48 l", "1,12 l", "6,72 l"], "n(Cu) = 0,1 mol = n(SO₂)."),
    O(3, "4FeS₂ + 11O₂ → 2Fe₂O₃ + 8SO₂. 1 mol FeS₂ dan necha mol SO₂ hosil bo'ladi? (faqat son)", ["2", "2 mol"], "8 : 4 = 2."),
]

Q["K9.8"] = [
    C(1, "Azot molekulasida atomlar orasida qanday bog' bor?", "Uchlamchi kovalent qutbsiz", ["Ikkilamchi kovalent", "Ion", "Vodorod"], "N≡N juda mustahkam."),
    C(1, "Ammiak molekulasining fazoviy shakli qanday?", "Piramidal", ["Chiziqli", "Tetraedrik", "Tekis uchburchak"], "Azot atomida bitta juft elektron bor."),
    C(1, "Ammiak sanoatda qaysi usulda olinadi?", "Gaber usulida (N₂ + H₂)", ["Kontakt usulida", "Solve usulida", "Kolbe usulida"], "Katalizator — temir."),
    C(2, "Oddiy sharoitda azot qaysi metall bilan reaksiyaga kirishadi?", "Litiy", ["Natriy", "Mis", "Temir"], "6Li + N₂ → 2Li₃N."),
    C(2, "Pt katalizatori ishtirokida ammiak kislorodda yonsa, qanday mahsulotlar hosil bo'ladi?", "NO va H₂O", ["N₂ va H₂O", "NO₂ va H₂", "N₂O va H₂O"], "4NH₃ + 5O₂ → 4NO + 6H₂O."),
    C(2, "Katalizatorsiz ammiak kislorodda yonsa, qanday mahsulotlar hosil bo'ladi?", "N₂ va H₂O", ["NO va H₂O", "NO₂ va H₂O", "N₂O₅ va H₂"], "4NH₃ + 3O₂ → 2N₂ + 6H₂O."),
    C(2, "Ammiak va xlorovodorod bir-biriga yaqinlashganda nima hosil bo'ladi?", "NH₄Cl (oq tutun)", ["NH₂Cl", "N₂ va HCl", "NCl₃"], "NH₃ + HCl → NH₄Cl."),
    M(2, [("4NH₃ + 3O₂ →", "2N₂ + 6H₂O"), ("4NH₃ + 5O₂ (Pt) →", "4NO + 6H₂O"), ("6Li + N₂ →", "2Li₃N")], "Azot va ammiak reaksiyalari."),
    C(3, "10 l N₂ va 30 l H₂ aralashmasidan (reaksiya to'liq ketsa) necha litr NH₃ hosil bo'ladi?", "20 l", ["40 l", "10 l", "30 l"], "N₂ + 3H₂ → 2NH₃: hajmlar 1 : 3 : 2."),
    C(3, "2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃ + 2H₂O. 0,5 mol NH₄Cl dan n.sh. da necha litr NH₃ olinadi?", "11,2 l", ["22,4 l", "5,6 l", "44,8 l"], "n(NH₃) = n(NH₄Cl) = 0,5 mol."),
    O(3, "4NH₃ + 5O₂ → 4NO + 6H₂O. 2 mol NH₃ dan necha mol NO hosil bo'ladi? (faqat son)", ["2", "2 mol"], "Nisbat 1 : 1."),
]

Q["K9.9"] = [
    C(1, "Nitrat kislota metallar bilan reaksiyada vodorod ajratadimi?", "Yo'q, vodorod ajratmaydi", ["Ha, har doim ajratadi", "Faqat suyultirilganda ajratadi", "Faqat Cu bilan ajratadi"], "HNO₃ oksidlovchi, azot oksidlari hosil bo'ladi."),
    C(1, "Zar suvi qanday aralashma?", "1 hajm HNO₃ va 3 hajm HCl", ["3 hajm HNO₃ va 1 hajm HCl", "H₂SO₄ va HCl", "HNO₃ va H₂SO₄"], "Oltin va platinani eritadi."),
    C(1, "Cu ga konsentrlangan HNO₃ ta'sir ettirilganda ajraladigan gaz rangi qanday?", "Qo'ng'ir", ["Rangsiz", "Yashil", "Sariq-yashil"], "NO₂ — qo'ng'ir gaz."),
    C(2, "Cu ga suyultirilgan HNO₃ ta'sir ettirilganda qaysi gaz ajraladi?", "NO", ["NO₂", "N₂O₅", "NH₃"], "3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO + 4H₂O."),
    C(2, "Sovuq konsentrlangan HNO₃ da qaysi metall passivlanadi?", "Temir", ["Mis", "Rux", "Kumush"], "Fe, Cr, Al passivlanadi."),
    C(2, "Cu + 4HNO₃(kons) → Cu(NO₃)₂ + 2NO₂ + 2H₂O tenglamada koeffitsiyentlar yig'indisi nechaga teng?", "10", ["9", "12", "8"], "1 + 4 + 1 + 2 + 2 = 10."),
    C(2, "Zar suvi qaysi metallni eritadi?", "Oltin", ["Faqat natriy", "Faqat alyuminiy", "Hech qaysi metallni"], "Au + HNO₃ + 3HCl → AuCl₃ + NO + 2H₂O."),
    M(2, [("Cu + HNO₃ (kons)", "NO₂"), ("Cu + HNO₃ (suyultirilgan)", "NO"), ("Mg + HNO₃ (juda suyultirilgan)", "NH₄NO₃")], "Nitrat kislotaning qaytarilish mahsulotlari."),
    C(3, "0,3 mol Cu suyultirilgan HNO₃ bilan reaksiyaga kirishsa, n.sh. da necha litr NO ajraladi? (3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO + 4H₂O)", "4,48 l", ["6,72 l", "2,24 l", "8,96 l"], "n(NO) = 0,3 · 2 / 3 = 0,2 mol."),
    C(3, "12,8 g Cu konsentrlangan HNO₃ bilan reaksiyaga kirishsa, n.sh. da necha litr NO₂ ajraladi?", "8,96 l", ["4,48 l", "17,92 l", "2,24 l"], "n(Cu) = 0,2 mol → n(NO₂) = 0,4 mol."),
    O(3, "Zar suvida HNO₃ va HCl hajmiy nisbatini «X:Y» ko'rinishida yozing.", ["1:3", "1 : 3", "1/3"], "1 hajm HNO₃ : 3 hajm HCl."),
]

Q["K9.10"] = [
    C(1, "Oq fosforning molekulyar formulasi qaysi?", "P₄", ["P₂", "P₈", "P"], "Oq fosfor — molekulyar kristall panjarali, zaharli."),
    C(1, "Qaysi fosfor allotropi zaharsiz?", "Qizil fosfor", ["Oq fosfor", "Sariq fosfor", "Faqat bug' holatdagi"], "Qizil fosfor polimer tuzilishli."),
    C(1, "Quyidagilardan qaysi biri fosforli o'g'it?", "Superfosfat", ["Ammiakli selitra", "Kaliy xlorid", "Karbamid"], "Superfosfat — fosforli o'g'it."),
    C(2, "Qo'sh superfosfatning tarkibi qaysi?", "Ca(H₂PO₄)₂", ["Ca₃(PO₄)₂", "CaHPO₄ + CaSO₄", "NH₄H₂PO₄"], "Qo'sh superfosfat — CaSO₄ siz."),
    C(2, "Oddiy superfosfat tarkibi qaysi?", "Ca(H₂PO₄)₂ + 2CaSO₄", ["Ca(H₂PO₄)₂", "Ca₃(PO₄)₂", "(NH₄)₂HPO₄"], "Tarkibida gips (CaSO₄) bor."),
    C(2, "Ammofos qanday moddalar aralashmasi?", "NH₄H₂PO₄ va (NH₄)₂HPO₄", ["Ca(H₂PO₄)₂ va CaSO₄", "KCl va NaCl", "NH₄NO₃ va KNO₃"], "Ammofos tarkibida N ham, P ham bor."),
    C(2, "P₂O₅ dagi fosforning oksidlanish darajasi qancha?", "+5", ["+3", "+2", "−3"], "2x + 5·(−2) = 0 → x = +5."),
    M(2, [("Oq fosfor", "molekulyar panjara, o'ta zaharli"), ("Qizil fosfor", "polimer tuzilish, zaharsiz"), ("Qora fosfor", "metallsimon, yarim o'tkazgich")], "Fosfor allotroplari."),
    C(3, "Quyidagi o'g'itlardan qaysi biri tarkibida ham azot, ham fosfor bor?", "Ammofos", ["Qo'sh superfosfat", "Kaliy xlorid", "Ammiakli selitra"], "NH₄H₂PO₄ — murakkab o'g'it."),
    C(3, "Ca₃(PO₄)₂ + 2H₂SO₄ → Ca(H₂PO₄)₂ + 2CaSO₄. 620 g Ca₃(PO₄)₂ dan necha mol Ca(H₂PO₄)₂ olinadi? (M = 310)", "2 mol", ["1 mol", "4 mol", "0,5 mol"], "620 : 310 = 2 mol; nisbat 1 : 1."),
    O(3, "NH₄H₂PO₄ da azotning massa ulushi necha foiz? (butun songacha yaxlitlang; M = 115)", ["12", "12%"], "14 : 115 = 0,1217."),
]

Q["K9.11"] = [
    C(1, "CO (is gazi) nega zaharli?", "Gemoglobin bilan mustahkam birikma hosil qiladi", ["Suvda eriydi", "Ohakli suvni loyqalatadi", "Havodan og'ir"], "Karboksigemoglobin hosil bo'ladi."),
    C(1, "CO₂ ni qaysi reagent bilan aniqlash mumkin?", "Ohakli suv Ca(OH)₂", ["Fenolftalein", "NaCl eritmasi", "KOH kristali"], "CO₂ + Ca(OH)₂ → CaCO₃↓ + H₂O."),
    C(1, "SiO₂ tabiatda qanday moddalar sifatida uchraydi?", "Qum va kvars", ["Ohaktosh", "Gips", "Dolomit"], "SiO₂ — atom kristall panjarali."),
    C(2, "SiO₂ qaysi kislota bilan reaksiyaga kirishadi?", "Plavik (HF)", ["HCl", "H₂SO₄", "HNO₃"], "SiO₂ + 4HF → SiF₄↑ + 2H₂O."),
    C(2, "Suvda erimaydigan yagona anorganik kislota qaysi?", "H₂SiO₃", ["H₂SO₃", "H₂CO₃", "H₃PO₄"], "Silikat kislota — jelesimon cho'kma."),
    C(2, "Oddiy oynaning tarkibi qaysi?", "Na₂O·CaO·6SiO₂", ["K₂O·PbO·SiO₂", "CaO·Al₂O₃", "Na₂CO₃·10H₂O"], "Natriy-kalsiy silikat oynasi."),
    C(2, "CO qaysi oksidlar turiga kiradi?", "Tuz hosil qilmaydigan oksid", ["Kislotali oksid", "Asosli oksid", "Amfoter oksid"], "CO suv va ishqor bilan reaksiyaga kirishmaydi."),
    M(2, [("CO", "tuz hosil qilmaydigan oksid"), ("CO₂", "kislotali oksid"), ("SiO₂", "atom kristall panjarali oksid")], "Uglerod va kremniy oksidlari."),
    C(3, "100 g CaCO₃ termik parchalanganda n.sh. da necha litr CO₂ ajraladi? (M(CaCO₃) = 100)", "22,4 l", ["11,2 l", "44,8 l", "100 l"], "n(CaCO₃) = 1 mol = n(CO₂)."),
    C(3, "Na₂SiO₃ + 2HCl → 2NaCl + H₂SiO₃↓. 0,5 mol Na₂SiO₃ dan necha gramm H₂SiO₃ hosil bo'ladi? (M(H₂SiO₃) = 78)", "39 g", ["78 g", "19,5 g", "156 g"], "n(H₂SiO₃) = 0,5 mol → 39 g."),
    O(3, "SiO₂ + 2NaOH → Na₂SiO₃ + H₂O. 6 g SiO₂ dan necha mol Na₂SiO₃ hosil bo'ladi? (M(SiO₂) = 60; faqat son)", ["0,1", "0.1", "0,1 mol", "0.1 mol"], "6 : 60 = 0,1 mol."),
]

Q["K9.12"] = [
    C(1, "Metallarning faollik (elektrod potensiallar) qatorini kim tuzgan?", "N.N. Beketov", ["D.I. Mendeleyev", "A. Butlerov", "M. Faradey"], "Beketov qatori."),
    C(1, "Fe₂O₃ ni CO bilan qaytarish qaysi metallurgiya turiga kiradi?", "Pirometallurgiya", ["Gidrometallurgiya", "Elektrometallurgiya", "Biometallurgiya"], "Yuqori haroratda qaytarish."),
    C(1, "Alyuminotermiya nima?", "Metall oksidlarini alyuminiy bilan qaytarish", ["Alyuminiyni elektroliz qilish", "Alyuminiyni kislotada eritish", "Alyuminiyni oksidlash"], "Cr₂O₃ + 2Al → Al₂O₃ + 2Cr."),
    C(2, "Quyidagi metallardan qaysi biri HCl dan vodorodni siqib chiqarmaydi?", "Cu", ["Zn", "Fe", "Mg"], "Mis vodoroddan o'ngda turadi."),
    C(2, "CuSO₄ + Fe → FeSO₄ + Cu reaksiyasi qaysi usulga asos bo'ladi?", "Gidrometallurgiya", ["Pirometallurgiya", "Elektrometallurgiya", "Alyuminotermiya"], "Tuz eritmasidan faolroq metall bilan siqib chiqarish."),
    C(2, "Temir plastinka CuSO₄ eritmasiga tushirilsa, plastinka massasi qanday o'zgaradi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Avval ortadi, keyin kamayadi"], "64 g Cu cho'kadi, 56 g Fe eriydi."),
    C(2, "Qaysi metall asosan elektroliz yordamida olinadi?", "Alyuminiy", ["Temir", "Mis", "Qalay"], "Al₂O₃ suyuqlanmasi elektrolizi."),
    M(2, [("Pirometallurgiya", "yuqori haroratda oksidlarni qaytarish"), ("Gidrometallurgiya", "eritmadan faolroq metall bilan siqib chiqarish"), ("Elektrometallurgiya", "elektroliz yordamida olish")], "Metallurgiya usullari."),
    C(3, "Fe plastinka CuSO₄ eritmasiga tushirilib, 0,1 mol Cu ajralgan. Plastinka massasi qanchaga o'zgargan?", "0,8 g ortgan", ["0,8 g kamaygan", "8 g ortgan", "O'zgarmagan"], "6,4 − 5,6 = 0,8 g."),
    C(3, "Cr₂O₃ + 2Al → Al₂O₃ + 2Cr. 15,2 g Cr₂O₃ dan necha gramm Cr olinadi? (M(Cr₂O₃) = 152)", "10,4 g", ["5,2 g", "15,2 g", "20,8 g"], "n(Cr₂O₃) = 0,1 mol → n(Cr) = 0,2 mol → 10,4 g."),
    O(3, "Fe₂O₃ + 3CO → 2Fe + 3CO₂. 1 mol Fe₂O₃ dan necha mol Fe hosil bo'ladi? (faqat son)", ["2", "2 mol"], "Nisbat 1 : 2."),
]

Q["K9.13"] = [
    C(1, "Natriy metalli nima ostida saqlanadi?", "Kerosin", ["Suv", "Spirt", "Havo"], "Na havo va suv bilan shiddatli reaksiyaga kirishadi."),
    C(1, "Ishqoriy metallar davriy jadvalning qaysi guruhida joylashgan?", "I A", ["II A", "III A", "VII A"], "Li, Na, K, Rb, Cs, Fr."),
    C(1, "Natriy kislorodda yonganda asosan qanday birikma hosil qiladi?", "Na₂O₂", ["Na₂O", "NaO₂", "NaOH"], "2Na + O₂ → Na₂O₂ (peroksid)."),
    C(2, "Litiy kislorodda yonganda qanday oksid hosil bo'ladi?", "Li₂O", ["Li₂O₂", "LiO₂", "LiO"], "Li — oddiy oksid beradi."),
    C(2, "Suvning vaqtinchalik qattiqligi qaysi tuzlar hisobiga bo'ladi?", "Ca(HCO₃)₂ va Mg(HCO₃)₂", ["CaSO₄ va MgCl₂", "NaCl va KCl", "CaCl₂ va MgSO₄"], "Qaynatilganda yo'qoladi."),
    C(2, "Suvning doimiy qattiqligini yo'qotish uchun nima qo'shiladi?", "Soda (Na₂CO₃)", ["Faqat qaynatiladi", "NaCl", "HCl"], "CaSO₄ + Na₂CO₃ → CaCO₃↓ + Na₂SO₄."),
    C(2, "Ca(HCO₃)₂ qaynatilganda qanday reaksiya boradi?", "Ca(HCO₃)₂ → CaCO₃↓ + CO₂↑ + H₂O", ["Ca(HCO₃)₂ → CaO + 2CO₂ + H₂O", "Ca(HCO₃)₂ → Ca + 2CO₂ + H₂", "Ca(HCO₃)₂ → CaCl₂"], "CaCO₃ cho'kmasi (nakipi) hosil bo'ladi."),
    M(2, [("Li", "Li₂O"), ("Na", "Na₂O₂"), ("K", "KO₂")], "Ishqoriy metallarning kislorodda yonishi."),
    C(3, "0,23 g Na suv bilan reaksiyaga kirishsa, n.sh. da necha litr H₂ ajraladi?", "0,112 l", ["0,224 l", "1,12 l", "0,056 l"], "n(Na) = 0,01 mol → n(H₂) = 0,005 mol."),
    C(3, "Ca(HCO₃)₂ + Ca(OH)₂ → 2CaCO₃↓ + 2H₂O. 0,5 mol Ca(HCO₃)₂ dan necha gramm CaCO₃ hosil bo'ladi?", "100 g", ["50 g", "200 g", "25 g"], "n(CaCO₃) = 1 mol → 100 g."),
    O(3, "4,6 g Na suvda erishidan necha gramm NaOH hosil bo'ladi? (faqat son)", ["8", "8 g"], "n(Na) = 0,2 mol = n(NaOH); 0,2 · 40 = 8 g."),
]

Q["K9.14"] = [
    C(1, "Alyuminiy yuzasi qaysi modda parda bilan himoyalangan?", "Al₂O₃", ["Al(OH)₃", "AlCl₃", "Al₂S₃"], "Oksid pardasi metallni suv va havodan saqlaydi."),
    C(1, "Alyuminiy qanday xossali metall?", "Amfoter", ["Faqat asosli", "Faqat kislotali", "Inert"], "Kislota va ishqor bilan reaksiyaga kirishadi."),
    C(1, "Alyuminiy ishqor eritmasi bilan reaksiyaga kirishsa, qaysi gaz ajraladi?", "Vodorod", ["Kislorod", "Azot", "Xlor"], "2Al + 6NaOH + 6H₂O → 2Na₃[Al(OH)₆] + 3H₂↑."),
    C(2, "Alyuminiy oddiy sharoitda nega suv bilan reaksiyaga kirishmaydi?", "Yuzasida zich oksid parda bor", ["Juda sust metall", "Suvda erimaydi", "Vodoroddan o'ngda turadi"], "Parda olib tashlansa, reaksiya shiddatli ketadi."),
    C(2, "Sovuq konsentrlangan HNO₃ ga alyuminiy solinsa nima bo'ladi?", "Passivlanadi (reaksiya ketmaydi)", ["Shiddatli yonadi", "NO₂ ajraladi", "H₂ ajraladi"], "Al, Fe, Cr passivlanadi."),
    C(2, "Al(OH)₃ ning amfoterligi nimada ko'rinadi?", "Ham kislota, ham ishqor bilan reaksiyaga kirishadi", ["Faqat kislota bilan", "Faqat suv bilan", "Faqat ishqor bilan"], "Al(OH)₃ + 3HCl → AlCl₃ + 3H₂O; Al(OH)₃ + NaOH → Na[Al(OH)₄]."),
    C(2, "Quyidagi reaksiyalardan qaysi biri alyuminotermiyaga misol?", "Fe₂O₃ + 2Al → Al₂O₃ + 2Fe", ["2Al + 3Cl₂ → 2AlCl₃", "4Al + 3O₂ → 2Al₂O₃", "2Al + 6HCl → 2AlCl₃ + 3H₂"], "Al oksiddan metallni qaytaradi."),
    M(2, [("Al + HCl", "AlCl₃ + H₂"), ("Al + NaOH + H₂O", "Na₃[Al(OH)₆] + H₂"), ("Al + O₂", "Al₂O₃")], "Alyuminiy reaksiyalari."),
    C(3, "5,4 g Al HCl bilan reaksiyaga kirishsa, n.sh. da necha litr H₂ ajraladi?", "6,72 l", ["4,48 l", "3,36 l", "13,44 l"], "n(Al) = 0,2 mol → n(H₂) = 0,3 mol."),
    C(3, "51 g Al₂O₃ dan (to'liq elektroliz) necha gramm Al olish mumkin? (M(Al₂O₃) = 102)", "27 g", ["54 g", "13,5 g", "51 g"], "n(Al₂O₃) = 0,5 mol → n(Al) = 1 mol."),
    O(3, "10,8 g Al kislota bilan reaksiyaga kirishsa, necha mol H₂ ajraladi? (faqat son)", ["0,6", "0.6", "0,6 mol", "0.6 mol"], "n(Al) = 0,4 mol → n(H₂) = 0,6 mol."),
]

Q["K9.15"] = [
    C(1, "Temir birikmalarida asosan qanday oksidlanish darajalarini namoyon qiladi?", "+2 va +3", ["+1 va +4", "+4 va +6", "+5 va +7"], "FeO, Fe₂O₃."),
    C(1, "Zang (temirning korroziyasi) tarkibi qaysi?", "Fe₂O₃·xH₂O", ["FeS", "FeCl₂", "Fe(NO₃)₃"], "Nam havoda hosil bo'ladi."),
    C(1, "KMnO₄ qanday xossaga ega?", "Kuchli oksidlovchi", ["Kuchli qaytaruvchi", "Inert", "Faqat asos"], "Mn⁺⁷ qaytariladi."),
    C(2, "Fe xlor atmosferasida yonganda qaysi tuz hosil bo'ladi?", "FeCl₃", ["FeCl₂", "FeCl₄", "Fe₂Cl₃"], "Xlor kuchli oksidlovchi — Fe ni +3 gacha oksidlaydi."),
    C(2, "Fe + 2HCl reaksiyasida qaysi mahsulotlar hosil bo'ladi?", "FeCl₂ va H₂", ["FeCl₃ va H₂", "FeCl₃ va H₂O", "FeCl₂ va Cl₂"], "Kislota bilan Fe⁺² beradi."),
    C(2, "Temir kuydirindisi Fe₃O₄ tarkibi qanday?", "FeO·Fe₂O₃", ["2FeO·Fe₂O₃", "FeO·2Fe₂O₃", "Fe₂O₃·3H₂O"], "Aralash oksid."),
    C(2, "CrO₃ qanday xossali oksid?", "Kislotali", ["Asosli", "Amfoter", "Inert"], "Cr⁺⁶ — kislotali oksid."),
    M(2, [("CrO", "asosli oksid"), ("Cr₂O₃", "amfoter oksid"), ("CrO₃", "kislotali oksid")], "Xrom oksidlari."),
    C(3, "11,2 g Fe xlorda yonganda necha gramm FeCl₃ hosil bo'ladi? (M(FeCl₃) = 162,5)", "32,5 g", ["25,4 g", "16,25 g", "65 g"], "n(Fe) = 0,2 mol → 0,2 · 162,5 = 32,5 g."),
    C(3, "Fe₃O₄ da temirning massa ulushi qancha? (M = 232)", "72,4%", ["70%", "77,8%", "63,6%"], "168 : 232 = 0,724."),
    O(3, "5,6 g Fe HCl bilan reaksiyaga kirishsa, n.sh. da necha litr H₂ ajraladi? (faqat son, vergul bilan)", ["2,24", "2.24"], "n(Fe) = 0,1 mol = n(H₂)."),
]
