"""v268: KIMYO va BIOLOGIYA — eng kam savolli mavzularga DTM / milliy sertifikat uslubidagi yangi savollar.
Kimyo hisoblari kod bilan tekshirilgan; biologiya savollari darslik faktlariga tayanadi."""
from __future__ import annotations

from ._dsl import C, O

CHEM: dict[str, list] = {
    "Birikmalar turi va bog'lanishga qarab xossalari": [
        C(2, "Qaysi modda ion bog'lanishli bo'lgani uchun yuqori temperaturada eriydi va eritmasi tok o'tkazadi?", "NaCl", ["CH₄", "I₂", "CO₂"], "Ion kristall panjara — kuchli elektrostatik tortishish."),
        C(3, "Quyidagi moddalardan qaysi biri molekulyar kristall panjaraga ega?", "Muz (H₂O)", ["Olmos", "Kvars (SiO₂)", "Osh tuzi"], "Molekulalar orasida kuchsiz vodorod va van-der-Vaals bog'lar."),
        C(3, "Atom kristall panjarali moddalarning umumiy xossasi?", "Juda qattiq, qiyin suyuqlanadi", ["Yumshoq, uchuvchan", "Elektr tokini yaxshi o'tkazadi", "Suvda oson eriydi"], "Olmos, kvars — kovalent tarmoq."),
    ],
    "Metallarning faollik qatori": [
        C(2, "Mis(II) sulfat eritmasiga qaysi metall tushirilsa, mis ajralib chiqadi?", "Temir", ["Kumush", "Oltin", "Platina"], "Fe faollik qatorida Cu dan chapda."),
        C(3, "5,6 g temir CuSO₄ eritmasiga to'liq reaksiyaga kirishdi. Plastinka massasi qanchaga o'zgaradi?", "0,8 g ga ortadi", ["0,8 g ga kamayadi", "6,4 g ga ortadi", "O'zgarmaydi"], "0,1 mol Fe (5,6 g) erib, 0,1 mol Cu (6,4 g) o'tiradi: +0,8 g."),
        C(2, "Qaysi metall suyultirilgan xlorid kislotadan vodorodni siqib chiqarmaydi?", "Mis", ["Rux", "Magniy", "Temir"], "Cu vodoroddan o'ngda."),
        O(3, "13 g rux mo'l sulfat kislota bilan reaksiyaga kirishdi. Necha litr vodorod (n.sh.) ajraladi?", ["4,48", "4.48"], "0,2 mol Zn → 0,2 mol H₂ → 4,48 L."),
    ],
    "Korroziya va himoya": [
        C(2, "Temir buyumni rux bilan qoplash (galvanizatsiya) temirni qanday himoya qiladi?", "Rux faolroq bo'lib, o'zi oksidlanadi", ["Rux temirdan kam faol", "Rux temirni qattiqlashtiradi", "Rux suvni o'tkazmaydi, xolos"], "Protektor himoya: faolroq metall «qurbon» bo'ladi."),
        C(3, "Qaysi juftlikda temir tezroq korroziyaga uchraydi?", "Temir–mis kontakti nam havoda", ["Temir–rux kontakti", "Temir–magniy kontakti", "Quruq havodagi temir"], "Mis kam faol — temir anod bo'lib yemiriladi."),
        C(2, "Temir zanglashi uchun qaysi moddalar zarur?", "Kislorod va suv", ["Faqat kislorod", "Faqat azot", "Karbonat angidrid"], "4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃."),
    ],
    "Kristall panjara turlari": [
        C(2, "Mis qanday kristall panjaraga ega?", "Metall", ["Ion", "Atom", "Molekulyar"], "Erkin elektronlar «gazi»."),
        C(3, "Olmos va grafitning qattiqligi turlicha bo'lishining sababi?", "Atomlarning kristallda joylashishi turlicha", ["Turli elementlardan tuzilgan", "Grafitda ion bog' bor", "Olmosda molekulalar bor"], "Allotropiya."),
        C(2, "Qaysi modda ion kristall panjaraga ega?", "KCl", ["H₂O", "SiO₂", "N₂"], "Metall va metallmas ionlari."),
    ],
    "Mineral o'g'itlar": [
        C(2, "Ammiakli selitra (NH₄NO₃) tarkibidagi azotning massa ulushi?", "35%", ["17,5%", "46,7%", "28%"], "2·14/80 = 0,35."),
        C(3, "Qaysi o'g'itda azotning massa ulushi eng katta?", "Karbamid CO(NH₂)₂", ["NH₄NO₃", "(NH₄)₂SO₄", "KNO₃"], "Karbamidda 46,7%."),
        C(2, "Kaliy o'g'itlarining qimmati qaysi oksid hisobida ifodalanadi?", "K₂O", ["KOH", "K₂O₂", "KCl"], "Fosforli — P₂O₅, kaliyli — K₂O hisobida."),
    ],
    "Atrof-muhit kimyosi: kislotali yomg'ir, issiqxona effekti": [
        C(2, "Kislotali yomg'irlarning asosiy sababchisi?", "SO₂ va azot oksidlari", ["CO va O₂", "N₂ va Ar", "CH₄ va H₂"], "Suvda H₂SO₃, H₂SO₄, HNO₃ hosil qiladi."),
        C(2, "Issiqxona effektini kuchaytiruvchi asosiy gaz?", "CO₂", ["O₂", "N₂", "He"], "Infraqizil nurlarni yutadi."),
        C(3, "Ozon qatlamini yemiruvchi moddalar?", "Freonlar (xlorftoruglevodorodlar)", ["Karbonat angidrid", "Azot", "Suv bug'i"], "Cl radikallari O₃ ni parchalaydi."),
    ],
    "Neft va tabiiy gaz": [
        C(2, "Tabiiy gazning asosiy tarkibiy qismi?", "Metan", ["Etan", "Propan", "Butan"], "Tabiiy gaz 90% gacha CH₄."),
        C(3, "Kreking jarayonida nima sodir bo'ladi?", "Uzun zanjirli uglevodorodlar parchalanadi", ["Uglevodorodlar polimerlanadi", "Neft haydaladi", "Benzol hosil bo'ladi, xolos"], "Benzin unumini oshirish uchun."),
        C(2, "Neftni haydash qaysi xossaga asoslangan?", "Fraksiyalarning qaynash temperaturalari turlicha", ["Zichliklari turlicha", "Rangi turlicha", "Erishi turlicha"], "Rektifikatsiya."),
    ],
    "Yonish reaksiyalari bo'yicha hisoblash": [
        C(2, "4 g metan to'liq yonishi uchun necha litr kislorod (n.sh.) kerak?", "11,2 L", ["5,6 L", "22,4 L", "44,8 L"], "CH₄ + 2O₂: 0,25 mol CH₄ → 0,5 mol O₂."),
        C(3, "6 g etan yonganda necha litr CO₂ (n.sh.) hosil bo'ladi?", "8,96 L", ["4,48 L", "13,44 L", "15,68 L"], "0,2 mol C₂H₆ → 0,4 mol CO₂."),
        C(3, "Uglevodorod yonganda 0,1 mol CO₂ va 0,15 mol H₂O hosil bo'ldi. Formulasi?", "C₂H₆", ["CH₄", "C₂H₄", "C₃H₈"], "C : H = 0,1 : 0,3 = 1 : 3 → C₂H₆."),
        O(3, "6 g etanning to'liq yonishi uchun necha litr O₂ (n.sh.) kerak?", ["15,68", "15.68"], "2C₂H₆ + 7O₂: 0,2 mol → 0,7 mol O₂ → 15,68 L."),
    ],
    "Vitaminlar, gormonlar va dori vositalari": [
        C(2, "Askorbin kislota qaysi vitamin?", "C vitamini", ["A vitamini", "D vitamini", "B₁ vitamini"], "Sitrus mevalarda ko'p."),
        C(2, "Aspirinning kimyoviy nomi?", "Atsetilsalitsil kislota", ["Paratsetamol", "Glyukoza", "Askorbin kislota"], "Isitma tushiruvchi va og'riq qoldiruvchi."),
        C(3, "Insulin kimyoviy tabiatiga ko'ra?", "Oqsil (polipeptid)", ["Steroid", "Uglevod", "Lipid"], "Me'da osti bezi gormoni."),
    ],
    "Kislorod, havo va yonish": [
        C(2, "Laboratoriyada kislorod qaysi moddani qizdirib olinadi?", "KMnO₄", ["NaCl", "CaCO₃", "H₂SO₄"], "2KMnO₄ → K₂MnO₄ + MnO₂ + O₂."),
        C(2, "Havoda kislorodning hajmiy ulushi taxminan?", "21%", ["78%", "1%", "50%"], "Azot — 78%."),
        C(3, "Yonish uchun qaysi uch shart zarur?", "Yonuvchi modda, kislorod, alangalanish temperaturasi", ["Suv, havo, yorug'lik", "Faqat kislorod", "Bosim va katalizator"], "Birini yo'qotish yonishni to'xtatadi."),
    ],
    "Vodorod va suv": [
        C(2, "Vodorod qaysi xossasi tufayli havo sharlari uchun xavfli?", "Havo bilan portlovchi aralashma hosil qiladi", ["Zaharli", "Og'ir", "Rangli"], "Qaldiroq gaz (2:1)."),
        C(3, "Suv molekulasidagi bog' turi?", "Kovalent qutbli", ["Ion", "Kovalent qutbsiz", "Metall"], "O va H elektromanfiyligi farq qiladi."),
        C(2, "Suvning anomal xossasi qaysi?", "Muzning zichligi suvnikidan kichik", ["Suv 0 °C da qaynaydi", "Suv rangli", "Suv tok o'tkazmaydi"], "Muz suv betida suzadi."),
    ],
    "Kimyoviy bog'lanish turlari": [
        C(2, "Qaysi molekulada kovalent qutbsiz bog' bor?", "Cl₂", ["HCl", "H₂O", "NH₃"], "Bir xil atomlar."),
        C(3, "Qaysi birikmada ham ion, ham kovalent bog' mavjud?", "NH₄Cl", ["NaCl", "HCl", "Cl₂"], "NH₄⁺ ichida kovalent (donor-akseptor ham), NH₄⁺ va Cl⁻ orasida ion bog'."),
        C(3, "Vodorod bog'i qaysi moddalarning qaynash temperaturasini oshiradi?", "H₂O, HF, NH₃", ["CH₄, H₂, N₂", "NaCl, KCl", "Fe, Cu"], "Kuchli elektromanfiy atom va H."),
    ],
    "Davriy jadval tuzilishi: davr va guruhlar": [
        C(2, "Tartib raqami 17 bo'lgan element qaysi davr va guruhda?", "3-davr, VIIA guruh", ["2-davr, VIIA guruh", "3-davr, VA guruh", "4-davr, VIIA guruh"], "Xlor: 2, 8, 7."),
        C(2, "Davr raqami nimani bildiradi?", "Energetik pog'onalar sonini", ["Valent elektronlar sonini", "Neytronlar sonini", "Atom massasini"], "Elektron qobiqlar soni."),
        C(3, "Guruh bo'yicha yuqoridan pastga metallik xossalari qanday o'zgaradi?", "Kuchayadi", ["Kamayadi", "O'zgarmaydi", "Avval kamayib keyin kuchayadi"], "Atom radiusi ortadi, elektron oson beriladi."),
    ],
    "Kimyoviy tenglamalarni tenglashtirish": [
        C(2, "Al + O₂ → Al₂O₃ tenglamasidagi koeffitsientlar yig'indisi?", "9", ["7", "5", "11"], "4Al + 3O₂ → 2Al₂O₃: 4 + 3 + 2."),
        C(3, "Cu + HNO₃(kons) → Cu(NO₃)₂ + NO₂ + H₂O tenglamasida HNO₃ oldidagi koeffitsient?", "4", ["2", "8", "6"], "Cu + 4HNO₃ → Cu(NO₃)₂ + 2NO₂ + 2H₂O."),
        C(2, "Fe + Cl₂ → FeCl₃ tenglamasidagi koeffitsientlar yig'indisi?", "7", ["5", "4", "9"], "2Fe + 3Cl₂ → 2FeCl₃."),
    ],
    "Elektrolitik dissotsiatsiya nazariyasi": [
        C(2, "Qaysi modda kuchsiz elektrolit?", "Sirka kislota", ["Xlorid kislota", "Natriy gidroksid", "Natriy xlorid"], "CH₃COOH qisman dissotsilanadi."),
        C(3, "1 mol Al₂(SO₄)₃ to'liq dissotsilanganda nechta mol ion hosil bo'ladi?", "5 mol", ["2 mol", "3 mol", "7 mol"], "2Al³⁺ + 3SO₄²⁻."),
        C(2, "Kislotalar dissotsilanganda qaysi kation hosil qiladi?", "H⁺", ["OH⁻", "Na⁺", "Cl⁻"], "Arrenius ta'rifi."),
    ],
    "Ion almashinish reaksiyalari": [
        C(2, "Qaysi juftlik eritmada reaksiya bermaydi (cho'kma, gaz yoki suv hosil bo'lmaydi)?", "NaCl + KNO₃", ["AgNO₃ + NaCl", "Na₂CO₃ + HCl", "NaOH + HCl"], "Barcha ionlar eritmada qoladi."),
        C(3, "Ba²⁺ + SO₄²⁻ → BaSO₄↓ qisqa ionli tenglamasiga qaysi reaksiya mos?", "BaCl₂ + Na₂SO₄", ["BaCO₃ + H₂SO₄", "Ba(OH)₂ + CuSO₄", "BaO + SO₃"], "Boshqalarida qo'shimcha cho'kma yoki boshqa zarralar bor."),
        C(2, "Karbonatlarni aniqlash uchun qaysi reaktiv ishlatiladi?", "Kislota (CO₂ gazi ajraladi)", ["Ishqor", "Suv", "Osh tuzi"], "CO₃²⁻ + 2H⁺ → CO₂↑ + H₂O."),
    ],
    "Tuzlar gidrolizi": [
        C(2, "Qaysi tuz eritmasi ishqoriy muhitga ega?", "Na₂CO₃", ["NaCl", "NH₄Cl", "AlCl₃"], "Kuchli asos + kuchsiz kislota tuzi."),
        C(3, "NH₄Cl eritmasi muhiti?", "Kislotali", ["Ishqoriy", "Neytral", "Muhit yo'q"], "Kuchsiz asos va kuchli kislota tuzi."),
        C(3, "Qaysi tuz gidrolizga uchramaydi?", "K₂SO₄", ["Na₂S", "FeCl₃", "CH₃COONa"], "Kuchli asos va kuchli kislotadan hosil bo'lgan."),
    ],
    "Galogenlar va xlor": [
        C(2, "Galogenlardan qaysi biri eng kuchli oksidlovchi?", "Ftor", ["Xlor", "Brom", "Yod"], "Elektromanfiyligi eng katta."),
        C(3, "KBr eritmasidan xlor o'tkazilganda nima sodir bo'ladi?", "Brom ajraladi", ["Reaksiya bormaydi", "Xlor ajraladi", "KClO₃ hosil bo'ladi"], "Cl₂ + 2KBr → 2KCl + Br₂."),
        C(2, "Yod kraxmal bilan qanday rang beradi?", "Ko'k", ["Qizil", "Sariq", "Rangsiz"], "Sifat reaksiyasi."),
    ],
    "Xalkogenlar: ozon, oltingugurt va vodorod sulfid": [
        C(2, "Ozon kislorodning qaysi shakli?", "Allotropik shakli", ["Izotopi", "Ioni", "Oksidi"], "O₃ va O₂."),
        C(3, "Vodorod sulfid eritmasiga qo'rg'oshin nitrat qo'shilsa?", "Qora cho'kma (PbS) tushadi", ["Oq cho'kma tushadi", "Gaz ajraladi", "O'zgarish bo'lmaydi"], "S²⁻ ioni uchun sifat reaksiyasi."),
        C(2, "Oltingugurtning eng yuqori oksidlanish darajasi?", "+6", ["+4", "−2", "+8"], "VIA guruh."),
    ],
    "Sulfat kislota va kontakt usuli": [
        C(2, "Kontakt usulida SO₂ ni SO₃ ga oksidlashda qaysi katalizator ishlatiladi?", "V₂O₅", ["Fe", "Pt faqat", "MnO₂"], "Vanadiy(V) oksidi."),
        C(3, "Konsentrlangan sulfat kislota mis bilan reaksiyaga kirishganda qaysi gaz ajraladi?", "SO₂", ["H₂", "H₂S", "O₂"], "Cu + 2H₂SO₄ → CuSO₄ + SO₂ + 2H₂O."),
        C(3, "Sulfat kislotani suyultirishning to'g'ri usuli?", "Kislotani suvga ingichka oqimda quyish", ["Suvni kislotaga quyish", "Ikkalasini birdan quyish", "Isitib aralashtirish"], "Ko'p issiqlik ajraladi — sachrashning oldi olinadi."),
    ],
    "Azot va ammiak": [
        C(3, "N₂ + 3H₂ ⇄ 2NH₃ (ekzotermik). Muvozanatni ammiak tomonga siljitadigan omil?", "Bosimni oshirish", ["Temperaturani oshirish", "Bosimni kamaytirish", "Ammiak qo'shish"], "Le-Shatelye: gaz molekulalari soni kamayadi."),
        C(2, "Ammiak suvli eritmasi qanday muhitga ega?", "Ishqoriy", ["Kislotali", "Neytral", "Muhitsiz"], "NH₃ + H₂O ⇄ NH₄⁺ + OH⁻."),
        C(2, "Ammiakni yig'ishda probirka qanday tutiladi?", "Teskari (og'zi pastga)", ["To'g'ri (og'zi yuqoriga)", "Gorizontal", "Suv ostida"], "Ammiak havodan yengil va suvda juda yaxshi eriydi."),
    ],
    "Nitrat kislota va zar suvi": [
        C(3, "Suyultirilgan nitrat kislota mis bilan reaksiyaga kirishganda qaysi gaz ajraladi?", "NO", ["NO₂", "H₂", "N₂O₅"], "3Cu + 8HNO₃(suyul.) → 3Cu(NO₃)₂ + 2NO + 4H₂O."),
        C(2, "Zar suvi qaysi kislotalar aralashmasi?", "1 hajm HNO₃ va 3 hajm HCl", ["3 hajm HNO₃ va 1 hajm HCl", "H₂SO₄ va HNO₃", "HCl va H₂SO₄"], "Oltin va platinani eritadi."),
        C(3, "Konsentrlangan nitrat kislota qaysi metallni passivlaydi?", "Temir", ["Mis", "Kumush", "Rux"], "Temir va alyuminiy sirti oksid parda bilan qoplanadi."),
    ],
    "Fosfor va fosforli o'g'itlar": [
        C(2, "Qaysi fosfor allotropiyasi zaharli va qorong'ida shu'lalanadi?", "Oq fosfor", ["Qizil fosfor", "Qora fosfor", "Barchasi"], "P₄ molekulalari, juda faol."),
        C(3, "Superfosfat tarkibidagi asosiy modda?", "Ca(H₂PO₄)₂", ["Ca₃(PO₄)₂", "NH₄NO₃", "KCl"], "Suvda eriydigan digidrofosfat."),
        C(2, "Gugurt qutisi yon tomoniga qaysi fosfor surtiladi?", "Qizil fosfor", ["Oq fosfor", "Qora fosfor", "Fosfor kislota"], "Zaharsiz va barqarorroq."),
    ],
    "Uglerod va kremniy birikmalari": [
        C(2, "Is gazi (CO) zaharliligining sababi?", "Gemoglobin bilan barqaror birikma hosil qiladi", ["Kislotali", "Yonmaydi", "Og'ir"], "Kislorod tashilishi to'xtaydi."),
        C(3, "Shisha ishlab chiqarishda asosiy xomashyo?", "Qum (SiO₂), soda va ohaktosh", ["Gil va suv", "Ko'mir va temir", "Osh tuzi"], "Na₂O·CaO·6SiO₂."),
        C(2, "Ichimlik sodasining formulasi?", "NaHCO₃", ["Na₂CO₃", "NaOH", "CaCO₃"], "Natriy gidrokarbonat."),
    ],
    "Ishqoriy, ishqoriy-yer metallar va suv qattiqligi": [
        C(2, "Vaqtinchalik qattiqlikni qanday yo'qotish mumkin?", "Qaynatish", ["Muzlatish", "Osh tuzi qo'shish", "Filtrlash"], "Ca(HCO₃)₂ → CaCO₃↓ + CO₂ + H₂O."),
        C(3, "Doimiy qattiqlikni keltirib chiqaruvchi tuzlar?", "CaSO₄ va MgCl₂", ["Ca(HCO₃)₂", "NaCl va KCl", "Na₂CO₃"], "Qaynatilganda cho'kmaydi."),
        C(2, "Natriy qanday saqlanadi?", "Kerosin ostida", ["Suv ostida", "Ochiq havoda", "Spirtda"], "Havo va suv bilan shiddatli reaksiyaga kirishadi."),
    ],
    "Alyuminiy va uning birikmalari": [
        C(2, "5,4 g alyuminiy mo'l xlorid kislota bilan reaksiyaga kirishsa, necha litr H₂ (n.sh.) ajraladi?", "6,72 L", ["4,48 L", "3,36 L", "2,24 L"], "0,2 mol Al → 0,3 mol H₂."),
        C(3, "Alyuminiy gidroksid amfoter ekanini qaysi reaksiyalar isbotlaydi?", "Ham kislota, ham ishqor bilan reaksiyaga kirishadi", ["Faqat kislota bilan", "Faqat suv bilan", "Qizdirilganda parchalanadi"], "Al(OH)₃ + NaOH → Na[Al(OH)₄]."),
        C(2, "Alyuminiy sanoatda qanday olinadi?", "Eritilgan Al₂O₃ ni elektroliz qilib", ["Ko'mir bilan qaytarib", "Suvdan", "Temir bilan siqib chiqarib"], "Kriolit eritmasida."),
    ],
    "Temir, xrom va marganets": [
        C(3, "Fe²⁺ ionini qaysi reaktiv bilan aniqlanadi?", "Qizil qon tuzi K₃[Fe(CN)₆] (ko'k cho'kma)", ["KSCN (qizil rang)", "AgNO₃", "BaCl₂"], "Fe³⁺ — KSCN yoki sariq qon tuzi bilan."),
        C(2, "Kaliy permanganatda marganetsning oksidlanish darajasi?", "+7", ["+2", "+4", "+6"], "KMnO₄: +1 + x + 4·(−2) = 0 → x = +7."),
        C(3, "Cho'yan va po'latning asosiy farqi?", "Cho'yanda uglerod ko'p (2–4%)", ["Po'latda uglerod ko'p", "Cho'yan sof temir", "Po'lat tarkibida temir yo'q"], "Po'latda 2% gacha uglerod."),
    ],
    "Izomeriya turlari": [
        C(2, "C₅H₁₂ nechta struktura izomerga ega?", "3", ["2", "4", "5"], "Pentan, izopentan, neopentan."),
        C(3, "Qaysi juftlik izomerlar?", "Etanol va dimetil efir", ["Etan va eten", "Metan va etan", "Etanol va etanal"], "Ikkalasi ham C₂H₆O."),
        C(3, "C₆H₁₄ nechta struktura izomerga ega?", "5", ["3", "4", "6"], "Geksan, 2- va 3-metilpentan, 2,2- va 2,3-dimetilbutan."),
    ],
    "Alkanlarning olinishi (Vyurs, Dyuma, Kolbe)": [
        C(3, "Vyurs reaksiyasida CH₃Cl va C₂H₅Cl aralashmasi natriy bilan qizdirilsa, qanday alkanlar hosil bo'ladi?", "Etan, propan va butan", ["Faqat propan", "Faqat etan", "Metan va etan"], "Radikallar har xil juftlashadi."),
        C(2, "Natriy atsetatni ishqor bilan qizdirib (Dyuma usuli) qaysi alkan olinadi?", "Metan", ["Etan", "Propan", "Butan"], "CH₃COONa + NaOH → CH₄ + Na₂CO₃."),
        C(3, "Alyuminiy karbid suv bilan reaksiyaga kirishganda?", "Metan ajraladi", ["Atsetilen ajraladi", "Etilen ajraladi", "Vodorod ajraladi"], "Al₄C₃ + 12H₂O → 4Al(OH)₃ + 3CH₄."),
    ],
    "Alkanlarning kimyoviy xossalari": [
        C(2, "Alkanlar uchun xos reaksiya turi?", "O'rin olish (radikal)", ["Birikish", "Polimerlanish", "Gidratlanish"], "To'yingan uglevodorodlar."),
        C(3, "Metan xlor bilan yorug'likda reaksiyaga kirishganda birinchi bosqich mahsuloti?", "CH₃Cl va HCl", ["CCl₄ va H₂", "C va HCl", "CH₂Cl₂ faqat"], "Zanjirli radikal mexanizm."),
        C(2, "Alkanlar kaliy permanganat eritmasini rangsizlantiradimi?", "Yo'q", ["Ha, tez", "Faqat qizdirilganda", "Faqat metan"], "To'yinmagan bog' yo'q."),
    ],
    "Alkenlar: olinishi va xossalari": [
        C(2, "Etilen bromli suvni rangsizlantiradi, chunki?", "Qo'shbog'ga brom birikadi", ["Brom bilan o'rin oladi", "Etilen yonadi", "Brom bug'lanadi"], "C₂H₄ + Br₂ → C₂H₄Br₂."),
        C(3, "Propenga HBr birikkanda asosiy mahsulot?", "2-brompropan", ["1-brompropan", "1,2-dibrompropan", "Propan"], "Markovnikov qoidasi."),
        C(3, "Molyar massasi 56 g/mol bo'lgan alken formulasi?", "C₄H₈", ["C₃H₆", "C₅H₁₀", "C₄H₁₀"], "14n = 56 → n = 4."),
    ],
    "Alkadienlar va kauchuklar": [
        C(2, "Tabiiy kauchukning monomeri?", "Izopren", ["Butadiyen", "Stirol", "Etilen"], "2-metilbutadiyen-1,3."),
        C(3, "Vulkanizatsiya nima?", "Kauchukni oltingugurt bilan qizdirib rezinaga aylantirish", ["Kauchukni eritish", "Polimerni parchalash", "Kauchukni bo'yash"], "Zanjirlar oltingugurt ko'priklari bilan bog'lanadi."),
        C(2, "Lebedev usulida butadiyen qaysi moddadan olinadi?", "Etil spirtdan", ["Metandan", "Benzoldan", "Atsetilendan faqat"], "2C₂H₅OH → C₄H₆ + 2H₂O + H₂."),
    ],
    "Alkinlar (atsetilen qatori)": [
        C(2, "64 g kalsiy karbiddan necha litr atsetilen (n.sh.) olinadi?", "22,4 L", ["11,2 L", "44,8 L", "33,6 L"], "1 mol CaC₂ → 1 mol C₂H₂."),
        C(3, "Kucherov reaksiyasida atsetilen suv bilan qaysi moddani hosil qiladi?", "Sirka aldegidi", ["Etanol", "Sirka kislota", "Etilen"], "Hg²⁺ katalizatorligida."),
        C(2, "Atsetilen molekulasidagi uglerod atomlari gibridlanishi?", "sp", ["sp²", "sp³", "dsp²"], "Uchbog' — chiziqli molekula."),
    ],
    "Arenlar: benzol va toluol": [
        C(2, "Benzol nitrolanganda qanday modda hosil bo'ladi?", "Nitrobenzol", ["Anilin", "Fenol", "Toluol"], "C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O."),
        C(3, "Toluolni benzoldan farqlovchi reaksiya?", "KMnO₄ eritmasini rangsizlantiradi", ["Yonadi", "Bromli suvni rangsizlantiradi", "Suvda eriydi"], "Metil guruh oksidlanib benzoy kislota hosil bo'ladi."),
        C(2, "Benzolning molekulyar formulasi?", "C₆H₆", ["C₆H₁₂", "C₆H₁₄", "C₆H₅OH"], "Aromatik halqa."),
    ],
    "Uglevodorodlar bo'yicha hisoblash masalalari": [
        C(2, "Molyar massasi 72 g/mol bo'lgan alkan formulasi?", "C₅H₁₂", ["C₆H₁₄", "C₄H₁₀", "C₅H₁₀"], "14n + 2 = 72 → n = 5."),
        C(3, "Alkanning vodorodga nisbatan zichligi 22. Formulasi?", "C₃H₈", ["C₂H₆", "C₄H₁₀", "CO₂"], "M = 44 → 14n + 2 = 44 → n = 3."),
        O(3, "11,2 L (n.sh.) etilenga necha gramm brom birikadi?", ["80"], "0,5 mol C₂H₄ + 0,5 mol Br₂ = 80 g."),
    ],
    "Organik moddalar nomenklaturasi": [
        C(2, "CH₃–CH(CH₃)–CH₂–CH₃ nomi?", "2-metilbutan", ["3-metilbutan", "Pentan", "2-etilpropan"], "Eng uzun zanjir 4 ta, o'rinbosar 2-holatda."),
        C(3, "CH₂=CH–CH(CH₃)–CH₃ nomi?", "3-metilbuten-1", ["2-metilbuten-3", "Penten-1", "3-metilbuten-2"], "Qo'shbog'ga yaqin uchidan raqamlanadi."),
        C(2, "–OH funksional guruhli birikmalar sinfi (alifatik)?", "Spirtlar", ["Aldegidlar", "Ketonlar", "Efirlar"], "Gidroksil guruh."),
    ],
    "Spirtlar va fenol": [
        C(3, "Fenolga bromli suv qo'shilganda?", "Oq cho'kma (2,4,6-tribromfenol)", ["Ko'k rang", "Gaz ajraladi", "O'zgarish bo'lmaydi"], "Fenol uchun sifat reaksiyasi."),
        C(2, "Etanol mis(II) oksid bilan qizdirilsa qaysi modda hosil bo'ladi?", "Atsetaldegid", ["Sirka kislota", "Etilen", "Dietil efir"], "Spirt aldegidgacha oksidlanadi."),
        C(3, "Glitserinni aniqlash uchun qaysi reaktiv ishlatiladi?", "Yangi cho'ktirilgan Cu(OH)₂ (ko'k eritma)", ["Bromli suv", "FeCl₃", "AgNO₃"], "Ko'p atomli spirtlar sifat reaksiyasi."),
    ],
    "Aldegidlar va ketonlar": [
        C(2, "«Kumush ko'zgu» reaksiyasi qaysi sinf uchun xos?", "Aldegidlar", ["Ketonlar", "Spirtlar", "Efirlar"], "Ag₂O ning ammiakli eritmasi bilan."),
        C(3, "Atsetonning sistematik nomi?", "Propanon", ["Propanal", "Etanal", "Butanon"], "CH₃–CO–CH₃."),
        C(2, "Formalin — bu?", "Formaldegidning suvdagi 40% eritmasi", ["Sirka kislota eritmasi", "Etanol", "Atseton"], "Dezinfeksiya va saqlash uchun."),
    ],
    "Karbon kislotalar": [
        C(2, "Sirka kislota natriy karbonat bilan reaksiyaga kirishganda qaysi gaz ajraladi?", "CO₂", ["H₂", "O₂", "CO"], "Kislota karbonatlarni parchalaydi."),
        C(3, "Chumoli kislota boshqa karbon kislotalardan qaysi reaksiyasi bilan farq qiladi?", "«Kumush ko'zgu» reaksiyasini beradi", ["Lakmusni qizartiradi", "Ishqor bilan reaksiyaga kirishadi", "Spirt bilan efir hosil qiladi"], "HCOOH molekulasida aldegid guruhi bor."),
        C(2, "Sirka kislotaning molyar massasi?", "60 g/mol", ["46 g/mol", "74 g/mol", "88 g/mol"], "C₂H₄O₂."),
    ],
    "Murakkab efirlar, yog'lar va sovun": [
        C(2, "Etil atsetatning molyar massasi?", "88 g/mol", ["74 g/mol", "102 g/mol", "60 g/mol"], "CH₃COOC₂H₅ = C₄H₈O₂."),
        C(3, "Yog'larning ishqoriy gidrolizi (sovunlanish) mahsulotlari?", "Glitserin va yuqori yog' kislotalarining tuzlari", ["Etanol va sirka kislota", "Glyukoza va fruktoza", "Aminokislotalar"], "Natriyli tuzlar — qattiq sovun."),
        C(3, "Suyuq yog'larni qattiq yog'ga aylantirish usuli?", "Gidrogenlash", ["Gidroliz", "Esterifikatsiya", "Kreking"], "Qo'shbog'larga vodorod biriktiriladi (margarin)."),
    ],
    "Uglevodlar": [
        C(2, "180 g glyukoza spirtli bijg'iganda necha mol etanol hosil bo'ladi?", "2 mol", ["1 mol", "3 mol", "6 mol"], "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂."),
        C(3, "Kraxmal va sellyuloza qanday farqlanadi?", "Glyukoza qoldiqlarining tuzilishi va bog'lanishi bilan (α va β)", ["Biri oqsil", "Tarkibidagi elementlar bilan", "Ikkalasi bir xil modda"], "(C₆H₁₀O₅)ₙ — ikkalasi ham."),
        C(2, "Saxaroza gidrolizlanganda nima hosil bo'ladi?", "Glyukoza va fruktoza", ["Faqat glyukoza", "Kraxmal", "Etanol"], "Disaxarid."),
    ],
    "Aminlar va anilin": [
        C(2, "Anilinning molyar massasi?", "93 g/mol", ["78 g/mol", "94 g/mol", "123 g/mol"], "C₆H₅NH₂."),
        C(3, "Aminlar qanday xossaga ega?", "Asos xossalariga", ["Kislota xossalariga", "Neytral", "Oksidlovchi"], "Azotdagi umumiy elektron jufti proton biriktiradi."),
        C(2, "Zinin reaksiyasi bo'yicha nitrobenzoldan nima olinadi?", "Anilin", ["Fenol", "Benzol", "Toluol"], "Nitroguruh aminoguruhga qaytariladi."),
    ],
    "Aminokislotalar va oqsillar": [
        C(2, "Glitsinning molyar massasi?", "75 g/mol", ["89 g/mol", "60 g/mol", "61 g/mol"], "NH₂CH₂COOH."),
        C(3, "Aminokislotalar amfoter bo'lishining sababi?", "Molekulada aminoguruh va karboksil guruh bor", ["Faqat karboksil guruh bor", "Suvda erimaydi", "Halqali tuzilgan"], "Ham kislota, ham asos bilan reaksiyaga kirishadi."),
        C(2, "Oqsillarning birlamchi tuzilmasi?", "Aminokislotalar ketma-ketligi", ["Spiral shakl", "Globula", "Bir necha zanjir birikmasi"], "Peptid bog'lar bilan."),
    ],
    "Polimerlar": [
        C(2, "Polivinilxlorid (PVX) qaysi monomerdan olinadi?", "Vinilxlorid", ["Etilen", "Stirol", "Propilen"], "CH₂=CHCl."),
        C(3, "Polikondensatsiyaning polimerlanishdan farqi?", "Quyi molekulyar qo'shimcha mahsulot (masalan, suv) ajraladi", ["Faqat bitta monomer ishtirok etadi", "Issiqlik yutiladi", "Katalizator kerak emas"], "Masalan, kapron, lavsan."),
        C(2, "Polietilenning monomeri?", "Etilen", ["Etan", "Atsetilen", "Izopren"], "nCH₂=CH₂ → (–CH₂–CH₂–)ₙ."),
    ],
    "Reaksiya tezligi va kimyoviy muvozanat": [
        C(3, "Temperatura koeffitsienti 3. Temperatura 20 °C ga oshirilsa, reaksiya tezligi necha marta ortadi?", "9 marta", ["6 marta", "3 marta", "27 marta"], "Vant-Goff: 3^(20/10) = 9."),
        C(2, "Katalizator muvozanatga qanday ta'sir qiladi?", "Muvozanatni siljitmaydi, uning qaror topishini tezlashtiradi", ["O'ngga siljitadi", "Chapga siljitadi", "Reaksiyani to'xtatadi"], "To'g'ri va teskari reaksiyani teng tezlashtiradi."),
        C(3, "H₂ + I₂ ⇄ 2HI muvozanatiga bosim ta'sir qiladimi?", "Yo'q, gaz molekulalari soni o'zgarmaydi", ["Ha, o'ngga siljiydi", "Ha, chapga siljiydi", "Reaksiya to'xtaydi"], "2 mol gaz ⇄ 2 mol gaz."),
    ],
    "Oksidlanish-qaytarilish va elektroliz": [
        C(2, "NaCl eritmasi elektroliz qilinganda katodda nima ajraladi?", "Vodorod", ["Natriy", "Xlor", "Kislorod"], "Natriy faol — suv qaytariladi."),
        C(3, "CuSO₄ eritmasi inert elektrodlarda elektroliz qilinganda anodda?", "Kislorod", ["Mis", "Oltingugurt", "Vodorod"], "SO₄²⁻ oksidlanmaydi, suv oksidlanadi."),
        C(2, "Oksidlovchi qaytarilish jarayonida?", "Elektron qabul qiladi", ["Elektron beradi", "Proton beradi", "O'zgarmaydi"], "Oksidlanish darajasi kamayadi."),
    ],
    "Genetik bog'lanish va ketma-ket o'zgarishlar": [
        C(3, "Ca → CaO → Ca(OH)₂ → X. X qaysi modda bo'lishi mumkin (CO₂ bilan)?", "CaCO₃", ["CaCl₂", "Ca", "CaH₂"], "Ca(OH)₂ + CO₂ → CaCO₃ + H₂O."),
        C(3, "CH₄ → X → C₆H₆. X?", "C₂H₂", ["C₂H₄", "C₂H₆", "CH₃Cl"], "2CH₄ → C₂H₂ + 3H₂; 3C₂H₂ → C₆H₆ (trimerlanish)."),
        C(2, "S → SO₂ → SO₃ → X. X?", "H₂SO₄", ["H₂SO₃", "H₂S", "Na₂S"], "SO₃ + H₂O → H₂SO₄."),
    ],
    "Element nomlari va belgilari": [
        C(1, "«Fe» belgisi qaysi element?", "Temir", ["Ftor", "Fosfor", "Fransiy"], "Lotincha Ferrum."),
        C(2, "«Ag» belgisi qaysi element?", "Kumush", ["Oltin", "Alyuminiy", "Argon"], "Lotincha Argentum."),
        C(2, "Simob elementining belgisi?", "Hg", ["Si", "Sm", "Mg"], "Lotincha Hydrargyrum."),
    ],
}

BIO: dict[str, list] = {
    "Ildiz tizimi va ildiz zonalari": [
        C(2, "Ildizning qaysi zonasi suv va mineral tuzlarni shimib oladi?", "So'rish zonasi (ildiz tukchalari)", ["Bo'linish zonasi", "O'sish zonasi", "Ildiz qini"], "Ildiz tukchalari so'rish yuzasini oshiradi."),
        C(2, "Ildiz qinining vazifasi?", "Ildiz uchini shikastlanishdan himoya qiladi", ["Suvni o'tkazadi", "Fotosintez qiladi", "Zahira modda to'playdi"], "Tuproq zarralariga tegib yeyiladi va yangilanadi."),
        C(3, "Bug'doy va makkajo'xorida qanday ildiz tizimi bor?", "Popuk ildiz tizimi", ["O'q ildiz tizimi", "Yer usti ildizlari", "Ildizmeva"], "Bir pallali o'simliklarga xos."),
    ],
    "Poya, kurtak va barg": [
        C(2, "Daraxt poyasi qaysi qatlam hisobiga yo'g'onlashadi?", "Kambiy", ["Po'stloq", "O'zak", "Yog'ochlik"], "Kambiy hujayralari bo'linadi."),
        C(3, "Barg og'izchalarining vazifasi?", "Gaz almashinuvi va suv bug'latish", ["Suv shimish", "Zahira to'plash", "Ko'payish"], "Transpiratsiya va CO₂ kirishi."),
        C(2, "Yillik halqalar qaysi qatlamda hosil bo'ladi?", "Yog'ochlikda", ["Lubda", "Po'stloqda", "O'zakda"], "Bahor va kuz yog'ochligi farqi."),
    ],
    "Gul va qo'sh urug'lanish": [
        C(3, "Qo'sh urug'lanishni kim kashf etgan?", "S. G. Navashin", ["G. Mendel", "Ch. Darvin", "I. Michurin"], "1898-yilda."),
        C(3, "Qo'sh urug'lanishda markaziy hujayra spermiy bilan qo'shilib nima hosil qiladi?", "Endosperm (triploid)", ["Murtak", "Urug' po'sti", "Meva"], "Ikkinchi spermiy tuxum hujayra bilan — zigota."),
        C(2, "Gulning urg'ochi qismi?", "Urug'chi", ["Changchi", "Gultoj", "Kosacha"], "Tumshuqcha, ustuncha, tugunchadan iborat."),
    ],
    "O'simliklarning vegetativ ko'payishi": [
        C(2, "Kartoshka qaysi organ yordamida vegetativ ko'payadi?", "Tuganak", ["Piyozbosh", "Ildizpoya", "Gajak"], "Shakli o'zgargan yer osti poyasi."),
        C(3, "Payvandlashda payvandtag nima?", "Ildizi bor, ustiga boshqa o'simlik qismi ulanadigan o'simlik", ["Ulanadigan qalamcha", "Urug'", "Gul"], "Payvandust — ulanadigan qism."),
        C(2, "Qulupnay qanday ko'payadi?", "Gajaklar (yer usti o'rmalovchi novdalar) bilan", ["Tuganak bilan", "Piyozbosh bilan", "Faqat urug' bilan"], "Vegetativ ko'payish."),
    ],
    "Suv o'tlari": [
        C(2, "Xlamidomonada qanday o'simlik?", "Bir hujayrali yashil suvo'ti", ["Ko'p hujayrali qo'ng'ir suvo'ti", "Mox", "Zamburug'"], "Xivchinlari va qizil ko'zchasi bor."),
        C(3, "Laminariya (dengiz karami) qaysi suvo'tlar bo'limiga kiradi?", "Qo'ng'ir suvo'tlar", ["Yashil suvo'tlar", "Qizil suvo'tlar", "Ko'k-yashil suvo'tlar"], "Yod manbai."),
        C(2, "Suvo'tlarining tanasi nima deb ataladi?", "Tallom (qattana)", ["Poya", "Barg", "Ildizpoya"], "Organlarga bo'linmagan."),
    ],
    "Moxlar, qirqbo'g'imlar va paporotniklar": [
        C(2, "Moxlarda qaysi avlod ustun turadi?", "Gametofit (jinsiy avlod)", ["Sporofit", "Ikkalasi teng", "Faqat urug'"], "Ko'rinadigan yashil o'simlik — gametofit."),
        C(3, "Paporotniklarning sporalari qayerda yetiladi?", "Barglarning orqa tomonidagi sporangiylarda", ["Ildizlarda", "Gullarda", "Mevalarda"], "Sorus guruhlari."),
        C(2, "Qirqbo'g'imlar poyasi tarkibida qaysi modda ko'p bo'lib, uni qattiq qiladi?", "Kremniy (kremnezyom)", ["Kalsiy", "Temir", "Kraxmal"], "Shuning uchun idishlarni tozalashda ishlatilgan."),
    ],
    "Yalang'ochurug'lilar (ignabarglilar)": [
        C(2, "Yalang'ochurug'lilarning urug'i qayerda joylashadi?", "Qubba tangachalarida ochiq holda", ["Meva ichida", "Gul ichida", "Ildizda"], "Tugunchasi yo'q."),
        C(3, "Qarag'ay uchun xos belgi?", "Ignabarglar juft-juft joylashgan, qubba hosil qiladi", ["Gul va meva hosil qiladi", "Barglari keng", "Spora bilan ko'payadi"], "Ninabargli doim yashil daraxt."),
        C(2, "Qaysi o'simlik yalang'ochurug'li emas?", "Olma", ["Archa", "Qarag'ay", "Qoraqarag'ay"], "Olma — yopiqurug'li (gulli)."),
    ],
    "O'simliklarda nafas olish va transpiratsiya": [
        C(2, "Transpiratsiya o'simlik uchun nima beradi?", "Bargni sovitadi va suvning yuqoriga ko'tarilishini ta'minlaydi", ["Fotosintezni to'xtatadi", "Ildizni o'stiradi", "Gulni changlatadi"], "Bug'lanish kuchi suv oqimini tortadi."),
        C(3, "O'simlik nafas olganda qaysi gaz ajraladi?", "Karbonat angidrid", ["Kislorod", "Azot", "Vodorod"], "Organik moddalar oksidlanadi."),
        C(3, "Kechasi yopiq xonada ko'p o'simlik saqlash tavsiya etilmaydi, chunki?", "Qorong'ida faqat nafas oladi — CO₂ chiqaradi", ["Kechasi kislorod ko'p chiqaradi", "Zaharli gaz chiqaradi", "Suv bug'latmaydi"], "Fotosintez yorug'likda boradi."),
    ],
    "Mineral oziqlanish va ildiz so'rishi": [
        C(2, "Azot yetishmaganda o'simlikda qanday belgi kuzatiladi?", "Barglar sarg'ayadi, o'sish sekinlashadi", ["Barglar qizaradi", "Gullar kattalashadi", "Ildiz yo'g'onlashadi"], "Azot oqsil va xlorofill tarkibida."),
        C(3, "Ildiz bosimi nimaga sabab bo'ladi?", "Suvning ildizdan poyaga ko'tarilishiga", ["Barg to'kilishiga", "Gul ochilishiga", "Urug' unishiga"], "«Yig'lash» hodisasi."),
        C(2, "Qaysi element xlorofill tarkibiga kiradi?", "Magniy", ["Temir", "Kaliy", "Kalsiy"], "Mg porfirin halqa markazida."),
    ],
    "Bo'shliqichlilar: gidra va marjonlar": [
        C(2, "Gidraning nerv tizimi qanday tuzilgan?", "Diffuz (to'rsimon)", ["Narvonsimon", "Zanjirsimon", "Markaziy"], "Eng sodda nerv tizimi."),
        C(3, "Gidradagi otuvchi (kuydiruvchi) hujayralar vazifasi?", "Himoya va o'ljani falajlash", ["Ovqat hazm qilish", "Ko'payish", "Nafas olish"], "Ektodermada joylashgan."),
        C(2, "Gidra qanday simmetriyaga ega?", "Radial (nursimon)", ["Ikki tomonlama", "Asimmetrik", "Sferik"], "Bo'shliqichlilarga xos."),
    ],
    "Mollyuskalar tipi": [
        C(2, "Sakkizoyoq qaysi sinfga kiradi?", "Boshoyoqlilar", ["Qorinoyoqlilar", "Ikki pallalilar", "Qisqichbaqasimonlar"], "Eng rivojlangan mollyuskalar."),
        C(3, "Ikki pallali mollyuskalar qanday oziqlanadi?", "Suvni filtrlab", ["Yirtqichlik bilan", "Parazitlik bilan", "Fotosintez bilan"], "Suv tozalovchilar."),
        C(2, "Mollyuskalar tanasini qoplab turuvchi teri burmasi?", "Mantiya", ["Chig'anoq", "Xitin", "Kutikula"], "Chig'anoqni mantiya hosil qiladi."),
    ],
    "Halqali chuvalchanglar": [
        C(2, "Yomg'ir chuvalchangining qon aylanish sistemasi?", "Yopiq", ["Ochiq", "Yo'q", "Aralash"], "Halqali chuvalchanglarda birinchi marta yopiq tizim."),
        C(3, "Yomg'ir chuvalchangi tuproq uchun nima foyda keltiradi?", "Tuproqni yumshatadi va chirindi bilan boyitadi", ["Ildizlarni yeydi", "Tuproqni zichlashtiradi", "Zararkunanda"], "Ch. Darvin tadqiq etgan."),
        C(2, "Zuluk qaysi tipga kiradi?", "Halqali chuvalchanglar", ["Yassi chuvalchanglar", "To'garak chuvalchanglar", "Mollyuskalar"], "So'lagida qon ivishiga to'sqinlik qiluvchi girudin bor."),
    ],
    "Hasharotlar sinfi": [
        C(2, "Hasharotlarning nechta oyog'i bor?", "6 ta", ["8 ta", "10 ta", "4 ta"], "3 juft oyoq."),
        C(3, "To'liq o'zgarish bilan rivojlanadigan hasharot?", "Kapalak", ["Chigirtka", "Suvarak", "Ninachi"], "Tuxum → lichinka → g'umbak → voyaga yetgan."),
        C(3, "Hasharotlarda nafas olish organi?", "Traxeyalar", ["O'pka", "Jabra", "Teri"], "Tana bo'ylab tarmoqlangan naychalar."),
    ],
    "Baliqlar sinfi": [
        C(2, "Baliqlar yuragi necha kamerali?", "2 kamerali", ["3 kamerali", "4 kamerali", "1 kamerali"], "Bo'lmacha va qorincha."),
        C(3, "Yon chiziq organi baliqqa nima uchun kerak?", "Suv oqimi va tebranishlarni sezish uchun", ["Nafas olish uchun", "Suzish uchun", "Ko'rish uchun"], "Maxsus sezgi organi."),
        C(2, "Baliqlarning suzgich pufagi vazifasi?", "Suvda ma'lum chuqurlikda turishni ta'minlaydi", ["Nafas olish", "Ovqat hazm qilish", "Ko'payish"], "Gaz bilan to'ladi."),
    ],
    "Amfibiyalar va reptiliyalar": [
        C(2, "Baqa lichinkasi (itbaliq) nima bilan nafas oladi?", "Jabra bilan", ["O'pka bilan", "Faqat teri bilan", "Traxeya bilan"], "Baliqqa o'xshash rivojlanish."),
        C(3, "Reptiliyalarni amfibiyalardan farqlovchi belgi?", "Tuxumi quruqlikda rivojlanadi, terisi muguz tangachali", ["Sovuqqonli", "Ikki juft oyoqli", "Umurtqali"], "Quruqlikka to'liq moslashgan."),
        C(3, "Amfibiyalar yuragi necha kamerali?", "3 kamerali", ["2 kamerali", "4 kamerali", "1 kamerali"], "Ikki bo'lmacha va bitta qorincha."),
    ],
    "Qushlar sinfi": [
        C(2, "Qushlarning qaysi belgisi uchishga moslashuv?", "Suyaklari bo'shliqli (pnevmatik)", ["Tishlari bor", "Bir kamerali yurak", "Sovuqqonli"], "Tana yengillashadi."),
        C(3, "Qushlarda qo'sh nafas olish nimani bildiradi?", "Nafas olishda ham, chiqarishda ham o'pkada gaz almashinadi", ["Ikkita o'pka bor", "Teri bilan ham nafas oladi", "Jabra bilan ham nafas oladi"], "Havo xaltalari tufayli."),
        C(2, "Qushlar yuragi?", "4 kamerali", ["3 kamerali", "2 kamerali", "5 kamerali"], "Issiqqonli."),
    ],
    "Sutemizuvchilar sinfi": [
        C(2, "Sutemizuvchilarga xos belgi?", "Bolasini sut bilan boqadi", ["Tuxum qo'yadi, xolos", "Tanasi tangachali", "Sovuqqonli"], "Sut bezlari."),
        C(3, "Tuxum qo'yuvchi sutemizuvchi?", "O'rdakburun", ["Kenguru", "Delfin", "Ko'rshapalak"], "Birinchi hayvonlar (Monotremata)."),
        C(2, "Diafragma qaysi hayvonlarda bor?", "Sutemizuvchilarda", ["Qushlarda", "Baliqlarda", "Reptiliyalarda"], "Ko'krak va qorin bo'shlig'ini ajratadi."),
    ],
    "Tayanch-harakat tizimi: suyaklar va bo'g'imlar": [
        C(2, "Kattalar skeletida nechta suyak bor?", "200 dan ortiq (≈206)", ["100", "50", "500"], "Taxminan 206 ta."),
        C(3, "Suyakning uzunasiga o'sishini nima ta'minlaydi?", "O'sish tog'ayi (metafiz plastinkasi)", ["Suyak usti pardasi", "Ilik", "Bo'g'im xaltasi"], "Ustki parda — yo'g'onlashish."),
        C(2, "Suyakka qattiqlik beruvchi moddalar?", "Mineral tuzlar (kalsiy fosfati)", ["Oqsillar", "Yog'lar", "Suv"], "Organik moddalar — elastiklik."),
    ],
    "Hazm tizimi va fermentlar": [
        C(2, "So'lakdagi amilaza fermenti nimani parchalaydi?", "Kraxmalni", ["Oqsilni", "Yog'ni", "Nuklein kislotani"], "Kraxmal → maltoza."),
        C(3, "Me'da shirasidagi pepsin qaysi muhitda faol?", "Kislotali", ["Ishqoriy", "Neytral", "Har qanday"], "HCl muhitida."),
        C(3, "O't suyuqligi qayerda ishlab chiqariladi?", "Jigarda", ["O't pufagida", "Me'da osti bezida", "Ingichka ichakda"], "O't pufagi faqat to'playdi."),
    ],
    "Nafas tizimi va gaz almashinuvi": [
        C(2, "Alveolalarda gaz almashinuvi qanday yo'l bilan boradi?", "Diffuziya", ["Faol transport", "Fagotsitoz", "Filtrlanish"], "Konsentratsiya farqi bo'yicha."),
        C(3, "Nafas markazi qayerda joylashgan?", "Uzunchoq miyada", ["Miyachada", "Bosh miya po'stlog'ida", "Orqa miyada"], "Qondagi CO₂ ga sezgir."),
        C(2, "Hiqildoqni ovqat yutganda berkituvchi tuzilma?", "Hiqildoq usti tog'ayi", ["Kekirdak", "Bronx", "Diafragma"], "Ovqat nafas yo'liga tushmaydi."),
    ],
    "Ayirish tizimi (buyrak, nefron)": [
        C(2, "Buyrakning tuzilish va funksional birligi?", "Nefron", ["Neyron", "Alveola", "Sarkomer"], "Har buyrakda ~1 mln."),
        C(3, "Birlamchi siydik qayerda hosil bo'ladi?", "Nefron kapsulasida (filtratsiya)", ["Siydik pufagida", "Siydik yo'lida", "Buyrak jomida"], "Kunlik ~150–180 L."),
        C(3, "Sog'lom odam ikkilamchi siydigida bo'lmasligi kerak bo'lgan modda?", "Glyukoza", ["Mochevina", "Suv", "Tuzlar"], "Glyukoza qayta so'riladi."),
    ],
    "Teri va termoregulyatsiya": [
        C(2, "Issiqda tana qanday sovitiladi?", "Ter ajralib bug'lanadi va teri tomirlari kengayadi", ["Tomirlar torayadi", "Qaltirash boshlanadi", "Ter ajralishi to'xtaydi"], "Bug'lanish issiqlik oladi."),
        C(3, "Terida melanin qaysi qavatda hosil bo'ladi?", "Epidermisda", ["Derma qavatida", "Teri osti yog' qavatida", "Ter bezlarida"], "Ultrabinafsha nurdan himoya."),
        C(2, "Termoregulyatsiya markazi qayerda?", "Gipotalamusda", ["Miyachada", "Orqa miyada", "Buyrak usti bezida"], "Oraliq miya."),
    ],
    "Sezgi organlari: ko'rish va eshitish": [
        C(2, "Ko'zning qaysi qismi rangni ajratadi?", "To'r pardadagi kolbachalar", ["Tayoqchalar", "Gavhar", "Shishasimon tana"], "Tayoqchalar — qorong'ida ko'rish."),
        C(3, "Yaqindan ko'rish (miopiya)da tasvir qayerda hosil bo'ladi?", "To'r pardaning oldida", ["To'r pardaning orqasida", "To'r pardada", "Gavharda"], "Botiq linzali ko'zoynak tuzatadi."),
        C(3, "Muvozanat saqlash organi qayerda?", "Ichki quloqda (vestibulyar apparat)", ["O'rta quloqda", "Tashqi quloqda", "Miyachada"], "Yarim doira kanallar."),
    ],
    "Immunitet va emlash": [
        C(2, "Emlash qanday immunitet hosil qiladi?", "Sun'iy faol immunitet", ["Tug'ma immunitet", "Sun'iy passiv immunitet", "Tabiiy passiv immunitet"], "Organizm o'zi antitana ishlab chiqaradi."),
        C(3, "Davolash zardobi (tayyor antitanalar) kiritilganda qanday immunitet?", "Sun'iy passiv", ["Sun'iy faol", "Tabiiy faol", "Tug'ma"], "Tez, lekin qisqa muddatli."),
        C(2, "Birinchi vaksinani (chechakka qarshi) kim yaratgan?", "E. Jenner", ["L. Paster", "I. Mechnikov", "R. Kox"], "1796-yilda."),
    ],
    "Fotosintez fazalari (yorug'lik va qorong'ilik)": [
        C(3, "Fotosintezning yorug'lik fazasida kislorod qaysi moddadan ajraladi?", "Suvdan", ["CO₂ dan", "Glyukozadan", "Xlorofilldan"], "Suv fotolizi."),
        C(3, "Qorong'ilik fazasi (Kalvin sikli) qayerda boradi?", "Xloroplast stromasida", ["Tilakoid membranasida", "Mitoxondriyada", "Sitoplazmada"], "CO₂ fiksatsiyasi."),
        C(2, "Yorug'lik fazasida qaysi energiya molekulasi hosil bo'ladi?", "ATF", ["Glyukoza", "Kraxmal", "Oqsil"], "Shuningdek NADF·H₂."),
    ],
    "Fermentlar va ularning xususiyatlari": [
        C(2, "Fermentlar kimyoviy tabiatiga ko'ra?", "Oqsillar", ["Uglevodlar", "Lipidlar", "Mineral tuzlar"], "Biologik katalizatorlar."),
        C(3, "Yuqori temperaturada fermentlar faolligi nima uchun yo'qoladi?", "Oqsil denaturatsiyaga uchraydi", ["Ferment ko'payadi", "Substrat yo'qoladi", "Suv bug'lanadi"], "Faol markaz shakli buziladi."),
        C(2, "Fermentning substratga moslashuvi qanday modelga o'xshatiladi?", "«Kalit–qulf»", ["«Zanjir»", "«Spiral»", "«Nasos»"], "Faol markaz va substrat mosligi."),
    ],
    "Mitoz va meyoz bosqichlari": [
        C(3, "Meyozning qaysi bosqichida krossingover sodir bo'ladi?", "I profazada", ["I metafazada", "II anafazada", "Interfazada"], "Gomologik xromosomalar konyugatsiyasi."),
        C(2, "Mitoz natijasida nechta hujayra hosil bo'ladi?", "2 ta, ona hujayraga o'xshash", ["4 ta gaploid", "1 ta", "8 ta"], "Xromosomalar to'plami saqlanadi."),
        C(3, "Diploid to'plami 46 bo'lgan hujayra meyozidan keyin har bir hujayrada nechta xromosoma bo'ladi?", "23", ["46", "92", "12"], "Gaploid to'plam."),
    ],
    "Mutatsiya va modifikatsiya": [
        C(2, "Modifikatsion o'zgaruvchanlik?", "Irsiylanmaydi, muhit ta'sirida yuzaga keladi", ["Irsiylanadi", "Genlarning o'zgarishi", "Xromosomalar sonining o'zgarishi"], "Reaksiya normasi doirasida."),
        C(3, "Daun sindromi qanday mutatsiya natijasi?", "21-juft xromosoma trisomiyasi (genom mutatsiya)", ["Gen mutatsiyasi", "Modifikatsiya", "Poliploidiya"], "47 ta xromosoma."),
        C(3, "Poliploidiya o'simlikchilikda nima uchun foydali?", "Yirik, hosildor navlar olinadi", ["O'simlik kichrayadi", "Urug' hosil bo'lmaydi", "Kasallik ko'payadi"], "Xromosomalar to'plami karrali ortadi."),
    ],
    "Seleksiya asoslari": [
        C(2, "Geterozis nima?", "Duragaylarning birinchi avlodda ota-onadan kuchli bo'lishi", ["Qarindosh chatishtirish", "Mutatsiya", "Tabiiy tanlanish"], "F₁ da yaqqol."),
        C(3, "Madaniy o'simliklarning kelib chiqish markazlarini kim aniqlagan?", "N. I. Vavilov", ["I. V. Michurin", "G. Mendel", "T. Morgan"], "7 ta asosiy markaz."),
        C(2, "Mikroorganizmlar seleksiyasida ko'p qo'llaniladigan usul?", "Sun'iy mutagenez", ["Payvandlash", "Geterozis", "Vegetativ ko'paytirish"], "Mutantlar orasidan tanlab olinadi."),
    ],
    "Biosfera va Vernadskiy ta'limoti": [
        C(2, "Biosfera ta'limotini yaratgan olim?", "V. I. Vernadskiy", ["E. Zyuss", "Ch. Darvin", "A. Tensli"], "Atama Zyussga tegishli, ta'limot — Vernadskiyga."),
        C(3, "Noosfera nima?", "Inson aqli boshqaradigan biosfera holati", ["Atmosferaning yuqori qatlami", "Okean tubi", "Tirik moddaning massasi"], "«Aql sferasi»."),
        C(2, "Ozon qatlami qaysi qobiqda joylashgan?", "Stratosferada", ["Troposferada", "Gidrosferada", "Litosferada"], "UB nurlardan himoya."),
    ],
    "Plastidalar va vakuola": [
        C(2, "Pomidorning qizil rangi qaysi plastidaga bog'liq?", "Xromoplastlar", ["Xloroplastlar", "Leykoplastlar", "Mitoxondriyalar"], "Karotinoidlar."),
        C(3, "Kartoshka tuganagida kraxmal qayerda to'planadi?", "Leykoplastlarda", ["Xloroplastlarda", "Vakuolada", "Yadroda"], "Rangsiz plastidalar."),
        C(2, "Hujayra shirasi qayerda joylashadi?", "Vakuolada", ["Yadroda", "Ribosomada", "Mitoxondriyada"], "O'simlik hujayrasida yirik."),
    ],
    "O'simlik to'qimalari (gistologiya)": [
        C(2, "Suv va mineral moddalarni yuqoriga o'tkazuvchi to'qima?", "Ksilema (yog'ochlik naylari)", ["Floema", "Epidermis", "Parenxima"], "Floema organik moddalarni o'tkazadi."),
        C(3, "O'simlikning bo'linuvchi (hosil qiluvchi) to'qimasi?", "Meristema", ["Kollenxima", "Sklerenxima", "Epidermis"], "O'sish nuqtalari va kambiy."),
        C(2, "Barg ustini qoplagan to'qima?", "Qoplovchi to'qima (epidermis)", ["O'tkazuvchi to'qima", "Mexanik to'qima", "Hosil qiluvchi to'qima"], "Kutikula bilan qoplangan."),
    ],
    "O'simlik oilalari (taksonomiya)": [
        C(2, "Bug'doy qaysi oilaga mansub?", "Boshoqdoshlar (g'allagullilar)", ["Ra'nodoshlar", "Karamdoshlar", "Ituzumdoshlar"], "Bir pallali."),
        C(3, "Kartoshka, pomidor va baqlajon qaysi oila vakillari?", "Ituzumdoshlar", ["Dukkakdoshlar", "Soyabonguldoshlar", "Qovoqdoshlar"], "Ituzumdoshlar (Solanaceae)."),
        C(2, "Ildizida tuganak bakteriyalar yashaydigan oila?", "Dukkakdoshlar", ["Murakkabguldoshlar", "Lolaguldoshlar", "Boshoqdoshlar"], "Azot to'playdi."),
    ],
    "Meva va urug'lar": [
        C(2, "O'rik mevasi qanday meva?", "Danakli meva", ["Rezavor", "Ko'sakcha", "Dukkak"], "Ichki qatlami qattiq."),
        C(3, "Bir pallali o'simlik urug'ida zahira oziq qayerda?", "Endospermda", ["Urug'pallada", "Urug' po'stida", "Ildizchada"], "Masalan, bug'doy."),
        C(2, "Shamol yordamida tarqaladigan urug'ga misol?", "Qoqio't", ["Olcha", "Yong'oq", "Tarvuz"], "Uchar kokilli."),
    ],
    "Fotosintez (o'simliklarda)": [
        C(2, "Fotosintez qaysi organoidda boradi?", "Xloroplastda", ["Mitoxondriyada", "Ribosomada", "Lizosomada"], "Xlorofill pigmenti."),
        C(3, "Fotosintezning umumiy tenglamasi?", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", ["C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O", "CO₂ + H₂O → CH₄ + O₂", "6O₂ → 2O₃"], "Yorug'lik energiyasi hisobiga."),
        C(2, "Fotosintez uchun qaysi omil shart emas?", "Tuproqdagi azot", ["Yorug'lik", "CO₂", "Suv"], "Bevosita reaksiyada ishtirok etmaydi."),
    ],
    "Bir hujayrali hayvonlar: amyoba va evglena": [
        C(2, "Amyoba qanday harakatlanadi?", "Soxta oyoqlar yordamida", ["Xivchin bilan", "Kiprikchalar bilan", "Muskullar bilan"], "Sitoplazma oqimi."),
        C(3, "Yashil evglenaning o'ziga xosligi?", "Yorug'likda fotosintez qiladi, qorong'ida tayyor organik moddalar bilan oziqlanadi", ["Faqat yirtqich", "Faqat parazit", "Harakatsiz"], "Aralash oziqlanish."),
        C(2, "Amyobadagi qisqaruvchi vakuola vazifasi?", "Ortiqcha suv va moddalarni chiqarish", ["Ovqat hazm qilish", "Harakatlanish", "Ko'payish"], "Osmotik muvozanat."),
    ],
    "Infuzoriya-tufelka va kon'yugatsiya": [
        C(2, "Infuzoriya-tufelka qanday harakatlanadi?", "Kiprikchalar yordamida", ["Soxta oyoqlar", "Xivchin", "Muskullar"], "Tanasi kiprikchalar bilan qoplangan."),
        C(3, "Kon'yugatsiya nima?", "Ikki infuzoriya irsiy axborot almashadigan jinsiy jarayon", ["Bo'linib ko'payish", "Kurtaklanish", "Sporalanish"], "Soni ko'paymaydi."),
        C(3, "Infuzoriyada nechta yadro bor?", "Ikkita (katta va kichik)", ["Bitta", "Yo'q", "Ko'p"], "Makronukleus va mikronukleus."),
    ],
    "Chuvalchanglar: gijjalar rivojlanish sikllari": [
        C(3, "Jigar qurtining oraliq xo'jayini?", "Kichik chuchuk suv shillig'i (mollyuska)", ["Qoramol", "It", "Baliq"], "Asosiy xo'jayin — o'txo'r hayvonlar."),
        C(2, "Odam askaridasi qaysi tipga kiradi?", "To'garak chuvalchanglar", ["Yassi chuvalchanglar", "Halqali chuvalchanglar", "Bo'shliqichlilar"], "Tanasi duksimon."),
        C(3, "Cho'chqa tasmasimon chuvalchangi bilan odam qanday zararlanadi?", "Yaxshi pishirilmagan cho'chqa go'shti orqali", ["Havo orqali", "Hasharot chaqishi orqali", "Suvda cho'milganda"], "Finnalar go'shtda bo'ladi."),
    ],
    "Bo'g'imoyoqlilar tipi": [
        C(2, "O'rgimchaksimonlarning nechta oyog'i bor?", "8 ta", ["6 ta", "10 ta", "Ko'p"], "4 juft yurish oyog'i."),
        C(3, "Bo'g'imoyoqlilarning tashqi skeleti qaysi moddadan iborat?", "Xitin", ["Kalsiy fosfat", "Kraxmal", "Keratin"], "Tullash bilan o'sadi."),
        C(2, "Daryo qisqichbaqasi qaysi sinfga kiradi?", "Qisqichbaqasimonlar", ["Hasharotlar", "O'rgimchaksimonlar", "Ko'poyoqlilar"], "Jabra bilan nafas oladi."),
    ],
    "Xordalilar: yurak va qon aylanishi": [
        C(3, "Arterial va venoz qon to'liq ajralgan hayvonlar?", "Qushlar va sutemizuvchilar", ["Baliqlar", "Amfibiyalar", "Reptiliyalar"], "4 kamerali yurak."),
        C(2, "Lansetnikda yurak?", "Yo'q, qorin aortasi qisqaradi", ["2 kamerali", "3 kamerali", "4 kamerali"], "Xordalilarning eng sodda vakili."),
        C(3, "Timsohda yurak qanday tuzilgan?", "4 kamerali (qorinchalar orasida to'liq to'siq)", ["3 kamerali", "2 kamerali", "Yo'q"], "Reptiliyalardan istisno."),
    ],
    "Xordalilar: nafas, ayirish va boshqa belgilar": [
        C(2, "Xordalilarning umumiy belgisi?", "Xorda, nerv nayi va halqum yoriqlari", ["Tashqi skelet", "Narvonsimon nerv tizimi", "Ochiq qon aylanish"], "Hayotning biror bosqichida."),
        C(3, "Sutemizuvchilarda ayirish organi?", "Tos buyrak", ["Bosh buyrak", "Tana buyrak", "Malpigi naychalari"], "Eng rivojlangan buyrak."),
        C(2, "Reptiliyalar qanday nafas oladi?", "Faqat o'pka bilan", ["Jabra bilan", "Teri va o'pka bilan", "Traxeya bilan"], "Terisi quruq, muguzli."),
    ],
    "Bosh miya bo'limlari": [
        C(2, "Harakatlar muvofiqligini qaysi bo'lim boshqaradi?", "Miyacha", ["Uzunchoq miya", "O'rta miya", "Oraliq miya"], "Muvozanat va koordinatsiya."),
        C(3, "Ko'rish markazi bosh miya po'stlog'ining qaysi bo'lagida?", "Ensa bo'lagida", ["Peshona bo'lagida", "Chakka bo'lagida", "Tepa bo'lagida"], "Eshitish — chakka bo'lagida."),
        C(2, "Yo'tal, aksirish va yutish reflekslarining markazi?", "Uzunchoq miya", ["Miyacha", "Katta yarim sharlar", "Orqa miya"], "Hayotiy muhim markazlar."),
    ],
    "Oqsillar va ularning tuzilmalari": [
        C(2, "Oqsil monomerlari?", "Aminokislotalar", ["Nukleotidlar", "Glyukoza", "Yog' kislotalari"], "20 xil aminokislota."),
        C(3, "Gemoglobin oqsili qaysi tuzilmaga ega?", "To'rtlamchi", ["Birlamchi faqat", "Ikkilamchi faqat", "Uchlamchi faqat"], "To'rtta polipeptid zanjir."),
        C(2, "Oqsilning qaysi funksiyasi antitanalarga xos?", "Himoya", ["Qurilish", "Energetik", "Transport"], "Begona moddalarni bog'laydi."),
    ],
    "Vitaminlar": [
        C(2, "D vitamini yetishmasligi qaysi kasallikka olib keladi?", "Raxit", ["Singa", "Kuraqo'rlik", "Beri-beri"], "Kalsiy almashinuvi buziladi."),
        C(2, "C vitamini yetishmovchiligi?", "Singa (lavsha)", ["Raxit", "Shabko'rlik", "Pellagra"], "Milklar qonaydi."),
        C(3, "Qaysi vitaminlar yog'da eriydi?", "A, D, E, K", ["C va B guruhi", "Faqat C", "Faqat B₁₂"], "Yog' bilan birga so'riladi."),
    ],
    "Jinsga birikkan irsiylanish": [
        C(3, "Gemofiliya bo'yicha tashuvchi ona (XᴴXʰ) va sog'lom otadan tug'ilgan o'g'illarning necha foizi kasal?", "50%", ["25%", "100%", "0%"], "O'g'il X ni onadan oladi."),
        C(2, "Daltonizm geni qaysi xromosomada joylashgan?", "X xromosomada", ["Y xromosomada", "Autosomada", "Mitoxondriyada"], "Retsessiv belgi."),
        C(3, "Nima uchun daltonizm erkaklarda ko'proq uchraydi?", "Erkaklarda bitta X xromosoma bor", ["Erkaklarda ikkita X bor", "Y xromosoma kasallik tug'diradi", "Muhit ta'siri"], "Retsessiv gen yashirinmaydi."),
    ],
    "Evolyutsiyaning harakatlantiruvchi kuchlari": [
        C(2, "Darvin ta'limotiga ko'ra evolyutsiyaning asosiy yo'naltiruvchi omili?", "Tabiiy tanlanish", ["Modifikatsiya", "Sun'iy tanlanish", "Migratsiya"], "Yashash uchun kurash asosida."),
        C(3, "Sanoat melanizmi (qayin parvonasi) qaysi tanlanishga misol?", "Harakatlantiruvchi tanlanish", ["Stabillashtiruvchi", "Uzuvchi", "Jinsiy"], "Muhit o'zgarishi bilan to'q shakllar ustunlik qildi."),
        C(2, "Gomologik organlarga misol?", "Odam qo'li va ko'rshapalak qanoti", ["Kapalak va qush qanoti", "Ko'z va quloq", "Jabra va o'pka"], "Kelib chiqishi umumiy."),
    ],
    "Arxey va Proterozoy (kriptozoy)": [
        C(2, "Yer yuzida birinchi tirik organizmlar qaysi erada paydo bo'lgan?", "Arxey", ["Mezozoy", "Paleozoy", "Kaynozoy"], "Prokariotlar."),
        C(3, "Proterozoy erasining muhim voqeasi?", "Eukariotlar va ko'p hujayralilarning paydo bo'lishi", ["Dinozavrlar paydo bo'lishi", "Odamning paydo bo'lishi", "Gulli o'simliklar"], "Kislorodli atmosfera shakllandi."),
        C(2, "Atmosferani kislorod bilan boyitgan ilk organizmlar?", "Sianobakteriyalar", ["Zamburug'lar", "Hayvonlar", "Viruslar"], "Fotosintez."),
    ],
    "Paleozoy: Kembriy, Ordovik, Silur": [
        C(2, "Silur davrining muhim voqeasi?", "O'simliklar quruqlikka chiqdi (psilofitlar)", ["Sutemizuvchilar paydo bo'ldi", "Gulli o'simliklar paydo bo'ldi", "Odam paydo bo'ldi"], "Ilk quruqlik o'simliklari."),
        C(3, "Kembriy davrida qaysi hayvonlar keng tarqalgan?", "Trilobitlar", ["Dinozavrlar", "Mamontlar", "Qushlar"], "Dengiz bo'g'imoyoqlilari."),
        C(2, "Ilk umurtqalilar (jag'siz) qaysi davrda paydo bo'lgan?", "Ordovikda", ["Bo'rda", "Neogenda", "Permda"], "Qalqondorlar."),
    ],
    "Paleozoy: Devon, Toshko'mir, Perm": [
        C(2, "Amfibiyalar qaysi davrda paydo bo'lgan?", "Devonda", ["Bo'rda", "Triasda", "Neogenda"], "Panjaqanotli baliqlardan."),
        C(3, "Toshko'mir konlari asosan qaysi o'simliklardan hosil bo'lgan?", "Daraxtsimon paporotnik, qirqbo'g'im va plaunlar", ["Gulli o'simliklar", "Suvo'tlari", "Ignabarglilar faqat"], "Karbon davri o'rmonlari."),
        C(2, "Reptiliyalar qaysi davrda paydo bo'lgan?", "Toshko'mir (karbon)da", ["Kembriyda", "Neogenda", "Antropogenda"], "Quruqlikka to'liq moslashish."),
    ],
    "Mezozoy va Kaynozoy": [
        C(2, "Dinozavrlar qaysi erada yashagan?", "Mezozoy", ["Paleozoy", "Kaynozoy", "Arxey"], "«Reptiliyalar erasi»."),
        C(3, "Gulli (yopiqurug'li) o'simliklar qaysi davrda paydo bo'lgan?", "Bo'rda", ["Triasda", "Devonda", "Neogenda"], "Mezozoy oxiri."),
        C(2, "Odam qaysi davrda paydo bo'lgan?", "Antropogenda (to'rtlamchi davr)", ["Bo'rda", "Paleogenda", "Yurada"], "Kaynozoy erasi."),
    ],
}


def extend(packs: list) -> int:
    from .gen_v242 import _add
    added = 0
    for pack in packs:
        if pack.get("subject") == "chemistry":
            added += _add(pack, CHEM)
        elif pack.get("subject") == "biology":
            added += _add(pack, BIO)
    return added
