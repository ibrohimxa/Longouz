"""Fizika: mexanika (6–9-sinf) — kinematika, dinamika, statika, gidrostatika, saqlanish qonunlari."""
import math
from ._dsl import C, O, M
from ._ph import N, ON, fmt
from . import figs_phys as F

g = 10
Q = {}

Q["P6.1"] = [
    C(1, "Xalqaro birliklar sistemasida (SI) uzunlikning asosiy birligi nima?", "metr", ["santimetr", "kilometr", "fut"], "SI da uzunlik birligi — metr (m)."),
    C(1, "Quyidagilardan qaysi biri vektor kattalik?", "Tezlik", ["Vaqt", "Massa", "Temperatura"], "Tezlik yo'nalishga ega, qolganlari skalyar."),
    C(1, "1 km necha metr?", "1000 m", ["100 m", "10 000 m", "10 m"], "kilo- = 10³."),
    C(1, "Massaning SI dagi birligi qaysi?", "kilogramm", ["gramm", "tonna", "nyuton"], "SI da massa birligi — kg."),
    C(2, "«Nano» old qo'shimcha qaysi ko'paytuvchiga mos?", "10⁻⁹", ["10⁻⁶", "10⁻³", "10⁹"], "nano = 10⁻⁹, mikro = 10⁻⁶, milli = 10⁻³."),
    C(2, "Lineyka shkalasida 0 dan 1 sm gacha 5 ta teng bo'linma bor. Bo'linma qiymati qancha?", "0,2 sm", ["0,5 sm", "0,1 sm", "0,02 sm"], "1 sm : 5 = 0,2 sm."),
    C(2, "Quyidagilardan qaysi biri SI ning asosiy birligi emas?", "nyuton", ["kelvin", "amper", "sekund"], "Nyuton — hosilaviy birlik (kg·m/s²)."),
    C(2, "Chizmadagi shkalada raqamli belgilar orasi 2,5 birlik bo'lib, har biri 5 ta teng bo'linmaga ajratilgan. Bo'linma qiymati qancha? (Asosiy belgilar orasi 5 ta bo'linma)", "0,5 birlik", ["0,2 birlik", "1 birlik", "2,5 birlik"], "Raqamlar 0; 2,5; 5; ... Orasi 2,5 birlik, 5 bo'linma: 2,5 : 5 = 0,5.", fig=F.scale_reading(0, 10, 0.5, 6.5, "birlik", major_every=5, title="")),
    M(2, [("Uzunlik", "metr"), ("Vaqt", "sekund"), ("Elektr toki kuchi", "amper")], "SI asosiy birliklari."),
    ON(3, "3 km necha santimetr? (oddiy son bilan yozing)", 300000, "3 km = 3000 m = 300 000 sm."),
]

Q["P6.2"] = [
    C(1, "Diffuziya hodisasi nima?", "Moddalarning o'z-o'zidan aralashib ketishi", ["Jismning qizishi", "Suyuqlikning bug'lanishi", "Qattiq jismning erishi"], "Molekulalar betartib harakati tufayli moddalar aralashadi."),
    C(1, "Brovn harakati nimani isbotlaydi?", "Molekulalarning uzluksiz betartib harakatda ekanini", ["Molekulalar bo'lmasligini", "Atomlar bo'linishini", "Moddaning uzluksizligini"], "Zarracha molekulalar zarbalari ta'sirida harakatlanadi."),
    C(1, "Zichlik formulasi qaysi?", "ρ = m / V", ["ρ = m · V", "ρ = V / m", "ρ = m / g"], "Zichlik massaning hajmga nisbati."),
    C(2, "Temperatura ortganda diffuziya tezligi qanday o'zgaradi?", "Ortadi", ["Kamayadi", "O'zgarmaydi", "Avval kamayib, keyin ortadi"], "Molekulalar tezligi oshadi."),
    C(2, "1 g/sm³ necha kg/m³?", "1000 kg/m³", ["100 kg/m³", "10 kg/m³", "10 000 kg/m³"], "1 g/sm³ = 10⁻³ kg / 10⁻⁶ m³ = 10³ kg/m³."),
    N(2, "Hajmi 0,5 m³ va massasi 3900 kg bo'lgan jism zichligi qancha?", 3900 / 0.5, [3900 * 0.5, 7800 / 2 + 1950, 390], "kg/m³", "ρ = 3900 : 0,5 = 7800 kg/m³ (po'lat)."),
    C(2, "Qaysi agregat holatda molekulalar orasidagi masofa eng katta?", "Gaz", ["Suyuq", "Qattiq", "Barchasida bir xil"], "Gazlarda molekulalar bir-biridan uzoq."),
    N(3, "Massasi 540 g alyuminiy bo'lagining hajmi (ρ = 2,7 g/sm³) qancha?", 200, [145.8, 1458, 20], "sm³", "V = m/ρ = 540 : 2,7 = 200 sm³."),
    M(2, [("Gaz", "shakli va hajmi o'zgaruvchan"), ("Suyuqlik", "hajmi saqlanadi, shakli o'zgaradi"), ("Qattiq jism", "shakli va hajmi saqlanadi")], "Agregat holatlar."),
    ON(3, "Bir xil massali ikki jism: birining zichligi 2700 kg/m³, ikkinchisiniki 900 kg/m³. Ikkinchisining hajmi birinchisiga nisbatan necha marta katta?", 3, "V = m/ρ, nisbat 2700/900 = 3."),
]

Q["P7.1"] = [
    C(1, "Jismning boshlang'ich va oxirgi nuqtalarini tutashtiruvchi vektor nima deyiladi?", "Ko'chish", ["Yo'l", "Tezlik", "Trayektoriya"], "Ko'chish — vektor kattalik."),
    C(1, "Qaysi holatda jismni moddiy nuqta deb hisoblash mumkin?", "Jism o'lchamlari u bosib o'tgan masofadan juda kichik bo'lganda", ["Jism aylanayotganda", "Jism katta bo'lganda", "Jism tinch turganda"], "O'lchamlar e'tiborga olinmaydi."),
    C(2, "Doira bo'ylab bir to'liq aylanishda ko'chish moduli nimaga teng?", "0", ["2πR", "R", "πR"], "Boshlang'ich va oxirgi nuqta mos tushadi."),
    N(2, "Jism 3 m sharqqa, so'ng 4 m shimolga yurdi. Ko'chish moduli qancha?", 5, [7, 1, 12], "m", "√(3²+4²) = 5 m."),
    N(2, "Shu jism bosib o'tgan yo'l qancha?", 7, [5, 1, 12], "m", "Yo'l = 3 + 4 = 7 m."),
    C(2, "Sanoq sistemasi nimalardan iborat?", "Sanoq jismi, koordinatalar sistemasi va vaqtni o'lchash asbobi", ["Faqat sanoq jismi", "Faqat soat", "Trayektoriya va yo'l"], "Ta'rif."),
    C(2, "Poyezddagi yo'lovchi uchun stol tinch, yer uchun esa harakatda. Bu nimani bildiradi?", "Harakatning nisbiyligini", ["Inersiyani", "Jism massasini", "Yo'lning musbatligini"], "Harakat sanoq sistemasiga bog'liq."),
    N(3, "Radiusi 10 m aylananing yarmini bosib o'tganda ko'chish moduli qancha?", 20, [10, 31.4, 15.7], "m", "Diametr = 2R = 20 m."),
    ON(3, "Radiusi 10 m bo'lgan aylana bo'ylab yarim aylanada bosib o'tilgan yo'l necha metr? (π = 3,14, javobni son bilan yozing)", math.pi * 10 if False else 31.4, "s = πR = 3,14·10 = 31,4 m."),
]

Q["P7.2"] = [
    C(1, "Tekis harakat tezligi formulasi qaysi?", "v = s / t", ["v = s · t", "v = t / s", "v = s + t"], "Yo'l vaqtga bo'linadi."),
    N(1, "Avtomobil 2 soatda 120 km yo'l yurdi. Tezligi qancha?", 60, [240, 30, 120], "km/soat", "120 : 2 = 60 km/soat."),
    N(1, "72 km/soat tezlik necha m/s?", 20, [72, 25, 259], "m/s", "72 : 3,6 = 20 m/s."),
    N(2, "Poyezd 15 m/s tezlik bilan 2 minutda qancha yo'l bosadi?", 1800, [30, 180, 900], "m", "s = 15 · 120 = 1800 m."),
    N(2, "Velosipedchi yo'lning birinchi yarmini 10 m/s, ikkinchi yarmini 15 m/s tezlikda bosdi. O'rtacha tezligi qancha?", 12, [12.5, 25, 5], "m/s", "v = 2v₁v₂/(v₁+v₂) = 2·10·15/25 = 12 m/s."),
    N(2, "Jism vaqtning birinchi yarmida 4 m/s, ikkinchi yarmida 8 m/s tezlik bilan harakatlandi. O'rtacha tezligi qancha?", 6, [5.33, 12, 4], "m/s", "Vaqtlar teng: (4+8)/2 = 6 m/s."),
    C(2, "Quyidagilardan qaysi birida o'rtacha tezlik tushunchasi o'rinli?", "Notekis harakatda", ["Faqat tekis harakatda", "Faqat tinch holatda", "Faqat aylanada"], "Notekis harakatda s_jami/t_jami."),
    M(2, [("36 km/soat", "10 m/s"), ("54 km/soat", "15 m/s"), ("90 km/soat", "25 m/s")], "km/soat : 3,6 = m/s."),
    ON(3, "A va B shaharlar orasi 240 km. Mashina A dan B ga 80 km/soat, qaytishda 60 km/soat tezlik bilan yurdi. Butun yo'ldagi o'rtacha tezlik necha km/soat? (Yaxlitlab, 1 xona verguldan keyin)", 68.6, "t = 3 + 4 = 7 soat; v = 480/7 ≈ 68,6."),
    ON(3, "Ikki jism bir-biriga qarab 3 m/s va 5 m/s tezlik bilan harakatlanyapti, orasidagi masofa 160 m. Necha sekunddan keyin uchrashadi?", 20, "t = 160 : (3+5) = 20 s."),
]

Q["P7.3"] = [
    C(1, "Kuchning SI dagi birligi qaysi?", "nyuton (N)", ["joul (J)", "vatt (W)", "paskal (Pa)"], "1 N = 1 kg·m/s²."),
    N(1, "Bir to'g'ri chiziq bo'ylab bir yo'nalishda 30 N va 50 N kuchlar ta'sir qiladi. Teng ta'sir etuvchi qancha?", 80, [20, 40, 1500], "N", "Yo'nalishlar bir xil — yig'indi."),
    N(1, "Qarama-qarshi yo'nalgan 70 N va 45 N kuchlarning teng ta'sir etuvchisi qancha?", 25, [115, 3150, 12], "N", "70 − 45 = 25 N."),
    N(2, "O'zaro perpendikulyar 6 N va 8 N kuchlarning teng ta'sir etuvchisi?", 10, [14, 2, 48], "N", "√(36+64) = 10 N."),
    C(2, "Kuch qaysi uchta xususiyat bilan to'liq aniqlanadi?", "Moduli, yo'nalishi, qo'yilish nuqtasi", ["Faqat moduli", "Massasi, tezligi, vaqti", "Zichligi, hajmi, massasi"], "Kuch — vektor."),
    C(2, "Quyidagi chizmada F₁ va F₂ kuchlar o'zaro perpendikulyar. Teng ta'sir etuvchi qanday yo'nalgan?", "Ikkala kuch orasida, parallelogramm diagonali bo'ylab", ["F₁ bilan bir xil", "F₂ ga qarama-qarshi", "Tinch holat (0)"], "Parallelogramm qoidasi.", fig=F.vectors([(90, 0, "F₁", F.RED), (0, 70, "F₂", F.BLUE)])),
    N(2, "Jism massasi 4 kg bo'lsa (g = 10 m/s²), og'irlik kuchi qancha?", 40, [4, 0.4, 14], "N", "F = mg."),
    N(3, "Ikki kuch 12 N va 12 N, ular orasidagi burchak 120°. Teng ta'sir etuvchi qancha?", 12, [24, 0, 17], "N", "F² = 12²+12²+2·144·cos120° = 144 → F = 12 N."),
    ON(3, "Ikki kuch 3 N va 5 N bir to'g'ri chiziqda ta'sir qiladi. Teng ta'sir etuvchining eng katta moduli necha N?", 8, "Bir tomonga: 3 + 5 = 8 N."),
]

Q["P7.4"] = [
    C(1, "Guk qonuni formulasi qaysi?", "F = kx", ["F = mg", "F = μN", "F = ma²"], "Elastiklik kuchi deformatsiyaga to'g'ri proporsional."),
    C(1, "Og'irlik kuchi qaysi jismga qo'yilgan?", "Jismning o'ziga (Yer tortadi)", ["Tayanchga", "Osmaga", "Havoga"], "Og'irlik kuchi mg — jismga qo'yiladi; og'irlik P esa tayanchga."),
    N(2, "Prujina qattiqligi 200 N/m. 5 sm cho'zish uchun qancha kuch kerak?", 10, [1000, 40, 4], "N", "F = kx = 200·0,05 = 10 N."),
    N(2, "Gorizontal sirtda massasi 20 kg yashikni tekis siljitish uchun 60 N kuch kerak. Ishqalanish koeffitsiyenti?", 0.3, [0.03, 3, 1.2], "", "μ = F/(mg) = 60/200 = 0,3."),
    C(2, "Ishqalanish kuchi qaysi kattalikka bog'liq EMAS?", "Tegib turgan sirt yuzasiga", ["Bosim kuchiga", "Sirt materiallariga", "Sirt ishlov berilishiga"], "F = μN; yuzaga bog'liq emas."),
    N(2, "Prujinaga 2 N kuch qo'yilganda 4 sm cho'ziladi. Qattiqligi qancha?", 50, [0.5, 8, 5], "N/m", "k = 2 : 0,04 = 50."),
    N(3, "Massasi 5 kg jism tekis tezlikda gorizontal yuzada μ = 0,2 bilan harakatlanmoqda. Ishqalanish kuchi?", 10, [1, 25, 100], "N", "F = μmg = 0,2·5·10 = 10 N."),
    C(2, "Tinchlikdagi ishqalanish kuchi qanday o'zgaradi?", "Tashqi kuchga teng bo'lib 0 dan F_max gacha", ["Doim F_max", "Doim nolga teng", "Faqat tezlikka bog'liq"], "Tashqi kuchni muvozanatlaydi."),
    ON(3, "Prujina 8 N kuchda 2 sm cho'ziladi. 5 sm cho'zilganda hosil bo'ladigan kuch necha N?", 20, "k = 400 N/m; F = 400·0,05 = 20 N."),
]

Q["P7.5"] = [
    C(1, "Bosim formulasi qaysi?", "p = F / S", ["p = F · S", "p = S / F", "p = m / V"], "Kuchning yuzaga nisbati."),
    C(1, "Bosimning SI dagi birligi?", "paskal (Pa)", ["nyuton (N)", "joul (J)", "vatt (W)"], "1 Pa = 1 N/m²."),
    N(2, "Yuzasi 0,5 m² polga 200 N kuch bilan bosim berildi. Bosim qancha?", 400, [100, 0.0025, 40], "Pa", "200/0,5 = 400 Pa."),
    N(2, "Suvning 5 m chuqurligidagi gidrostatik bosim (ρ = 1000 kg/m³, g = 10)?", 50000, [5000, 500000, 500], "Pa", "p = ρgh = 1000·10·5."),
    C(2, "Gidrostatik bosim idish shakliga bog'liqmi?", "Yo'q, faqat ρ va h ga bog'liq", ["Ha, keng idishda ko'p", "Ha, tor idishda ko'p", "Faqat hajmga"], "Gidrostatik paradoks.", fig=F.vessels()),
    N(2, "Gidravlik pressda kichik porshen yuzi 10 sm², katta porshen yuzi 200 sm². Kichigiga 50 N kuch qo'yilsa, kattasida kuch?", 1000, [2500, 100, 10], "N", "F₂ = F₁·S₂/S₁ = 50·20 = 1000 N.", fig=F.hydraulic("10 sm²", "200 sm²")),
    N(3, "Simob ustuni balandligi 760 mm bo'lsa atmosfera bosimi taxminan qancha? (ρ = 13600, g = 10)", 103360, [10336, 76000, 1013250], "Pa", "p = 13600·10·0,76 = 103 360 Pa ≈ 10⁵ Pa."),
    C(2, "Birlashgan idishlarda bir xil suyuqlik sathlari qanday bo'ladi?", "Bir xil balandlikda", ["Keng idishda baland", "Tor idishda baland", "Idish hajmiga qarab"], "Birlashgan idishlar qonuni."),
    ON(3, "U-simon naychada suv (ρ=1000) va yog' (ρ=800) bor. Suv ustuni 20 sm bo'lsa, yog' ustuni balandligi necha sm? (chegara bir sathda)", 25, "ρ₁h₁ = ρ₂h₂ → 1000·20/800 = 25 sm.", ) if False else ON(3, "U-simon naychada suv (ρ=1000) va yog' (ρ=800) turibdi, chegara bir sathda. Suv ustuni 20 sm bo'lsa yog' ustuni necha sm?", 25, "ρ₁h₁ = ρ₂h₂ → h₂ = 1000·20/800 = 25 sm."),
]

Q["P7.6"] = [
    C(1, "Arximed kuchi formulasi qaysi?", "F_A = ρ_s · g · V_botgan", ["F_A = ρ_j · g · h", "F_A = m · a", "F_A = p · S"], "Suyuqlik zichligi, g va botgan qism hajmi."),
    C(1, "Jism suyuqlikda cho'kadi, qachonki...", "jism zichligi suyuqlik zichligidan katta bo'lsa", ["jism zichligi kichik bo'lsa", "jism hajmi katta bo'lsa", "jism yengil bo'lsa"], "ρ_j > ρ_s."),
    N(2, "Hajmi 0,002 m³ jism to'liq suvga botirilgan. Arximed kuchi (ρ = 1000, g = 10)?", 20, [2, 200, 0.2], "N", "F = 1000·10·0,002 = 20 N."),
    N(2, "Muz (ρ = 900) suvda suzmoqda. Botgan qismining ulushi?", 0.9, [0.1, 0.5, 1.1], "", "ρ_muz/ρ_suv = 0,9."),
    C(2, "Suzayotgan jism uchun Arximed kuchi nimaga teng?", "Jism og'irligiga", ["Nolga", "Jism hajmiga", "Suv massasiga ko'paytirilgan g ga"], "Muvozanat: F_A = mg.", fig=F.floating(0.6)),
    N(2, "Havoda 5 N, suvda 3 N ni ko'rsatayotgan jismga ta'sir qiluvchi Arximed kuchi?", 2, [8, 15, 3], "N", "5 − 3 = 2 N."),
    N(3, "Shu jism hajmi qancha? (suv ρ = 1000, g = 10; F_A = 2 N)", 0.0002, [0.002, 0.02, 0.00002], "m³", "V = F/(ρg) = 2/10⁴ = 2·10⁻⁴ m³."),
    C(2, "Kema po'latdan yasalgan bo'lsa ham suzadi, chunki...", "ichi bo'sh bo'lgani uchun o'rtacha zichligi suvnikidan kichik", ["po'lat suvdan yengil", "suv kemani itaradi", "havo bosimi ushlab turadi"], "O'rtacha zichlik < ρ_suv."),
    ON(3, "Zichligi 600 kg/m³ bo'lgan yog'och brusok suvda suzmoqda. Hajmining necha foizi suvda? (faqat son)", 60, "600/1000 = 0,6 → 60%."),
]

Q["P7.7"] = [
    C(1, "Richag muvozanat sharti qaysi?", "F₁·l₁ = F₂·l₂", ["F₁ + F₂ = 0", "F₁·l₂ = F₂·l₂", "F₁/F₂ = l₁·l₂"], "Momentlar teng."),
    N(2, "Richagning chap yelkasi 2 m, o'ng yelkasi 6 m (chizmaga qarang). Chapga 90 N qo'yilsa, muvozanat uchun o'ngga qancha kuch kerak?", 30, [270, 10, 45], "N", "90·2 = F·6 → F = 30 N.", fig=F.lever(2, 6, "90 N", "F")),
    C(1, "Qo'zg'almas blok nima beradi?", "Kuchning yo'nalishini o'zgartiradi, kuchdan yutuq bermaydi", ["Kuchdan 2 marta yutuq", "Yo'ldan yutuq", "Ishdan yutuq"], "Ish yutug'i yo'q."),
    N(2, "Qo'zg'aluvchan blok yordamida 80 N li yukni tekis ko'tarish uchun (ishqalanishsiz) qancha kuch kerak?", 40, [80, 160, 20], "N", "Kuchdan 2 marta yutuq.", fig=F.movable_block("F", "80 N")),
    C(2, "«Mexanikaning oltin qoidasi»ga ko'ra...", "Kuchdan necha marta yutsak, yo'ldan shuncha marta yutqazamiz", ["Ishdan yutamiz", "Yo'ldan yutamiz", "Quvvatdan yutamiz"], "Oddiy mexanizmlar ishdan yutuq bermaydi."),
    N(2, "FIK 80% bo'lgan mexanizm 500 J ish bajardi (to'liq ish). Foydali ish?", 400, [625, 100, 40], "J", "A_f = η·A = 0,8·500."),
    N(3, "Qiya tekislik uzunligi 5 m, balandligi 1 m. Ishqalanishsiz 100 N yukni tortish uchun kuch?", 20, [500, 100, 50], "N", "F = P·h/l = 100·1/5."),
    N(3, "Shu qiya tekislikda FIK 80% bo'lsa, tortish kuchi? (100 N yuk, h = 1 m, l = 5 m)", 25, [20, 16, 40], "N", "A_f = 100·1 = 100 J; A_t = 125 J; F = 125/5 = 25 N."),
    ON(3, "Yengil richagning uchlariga 6 N va 10 N yuk osildi. Uning uzunligi 80 sm. Muvozanat uchun tayanch kichik yukdan necha sm masofada bo'lishi kerak?", 50, "6·x = 10·(80−x) → x = 50 sm."),
]

Q["P7.8"] = [
    C(1, "Mexanik ish formulasi qaysi?", "A = F · s · cosα", ["A = F / s", "A = m · v", "A = F · t"], "Ish kuch, ko'chish va ular orasidagi burchak kosinusi."),
    N(1, "50 N kuch ta'sirida jism kuch yo'nalishida 4 m ko'chdi. Ish?", 200, [12.5, 54, 46], "J", "A = Fs."),
    N(2, "Quvvati 2 kW dvigatel 30 s da qancha ish bajaradi?", 60000, [60, 15, 6000], "J", "A = Nt = 2000·30."),
    N(2, "Massasi 2 kg jism 5 m/s tezlik bilan harakatlanmoqda. Kinetik energiya?", 25, [10, 50, 5], "J", "mv²/2 = 2·25/2."),
    N(2, "3 kg jism 4 m balandlikda (g = 10) potensial energiyasi?", 120, [12, 7, 30], "J", "mgh."),
    C(2, "Qachon kuchning bajargan ishi manfiy bo'ladi?", "Kuch ko'chishga qarama-qarshi yo'nalganda", ["Kuch ko'chishga perpendikulyar bo'lganda", "Kuch nolga teng bo'lganda", "Hech qachon"], "cosα < 0."),
    N(3, "Avtomobil 20 m/s tezlikda, tortish kuchi 3000 N. Dvigatel quvvati?", 60000, [150, 600, 6000], "W", "N = Fv."),
    N(3, "Kinetik energiyasi 200 J, massasi 4 kg jism tezligi?", 10, [50, 100, 7.07], "m/s", "v = √(2E/m) = √100."),
    ON(3, "Quvvati 1,5 kW bo'lgan nasos 20 m chuqurlikdan necha litr suv (1 l = 1 kg) chiqaradi 40 s ichida? (g = 10, FIK = 100%)", 300, "A = 1500·40 = 60000 J; m = A/(gh) = 60000/200 = 300 kg."),
    M(2, [("Ish", "joul"), ("Quvvat", "vatt"), ("Bosim", "paskal")], "SI birliklari."),
]

Q["P9.1"] = [
    C(1, "Tezlanishning SI dagi birligi?", "m/s²", ["m/s", "N", "m²/s"], "a = Δv/t."),
    N(1, "Jism 2 s da tezligini 4 m/s dan 10 m/s gacha oshirdi. Tezlanishi?", 3, [7, 14, 1.5], "m/s²", "(10−4)/2."),
    N(2, "Tinch holatdan 2 m/s² tezlanish bilan 5 s harakatlangan jismning yo'li?", 25, [10, 50, 12.5], "m", "s = at²/2."),
    N(2, "Boshlang'ich tezligi 10 m/s, tezlanishi −2 m/s² bo'lgan jism necha sekunddan so'ng to'xtaydi?", 5, [20, 10, 2.5], "s", "t = v₀/|a|."),
    N(2, "v₀ = 4 m/s, a = 2 m/s², t = 3 s. Yo'l?", 21, [18, 30, 12], "m", "s = 4·3 + 2·9/2 = 21."),
    N(3, "Tinchlikdan yurgan jism 4 s da 32 m yo'l bosdi. Tezlanishi?", 4, [8, 2, 16], "m/s²", "a = 2s/t²."),
    N(3, "Poyezd tezligi 20 m/s dan 10 m/s gacha 100 m yo'lda kamaydi. Tezlanish moduli?", 1.5, [3, 0.75, 1], "m/s²", "a = (v₀²−v²)/(2s) = 300/200."),
    C(2, "Tekis tezlanuvchan harakatda tezlik-vaqt grafigi qanday chiziq?", "Qiya to'g'ri chiziq", ["Gorizontal to'g'ri chiziq", "Parabola", "Giperbola"], "v = v₀ + at."),
    ON(3, "Jism tinchlikdan a = 2 m/s² bilan harakat boshladi. 4-sekundda (faqat to'rtinchi sekund davomida) bosib o'tgan yo'li necha metr?", 7, "s₄ = a(2·4−1)/2 = 2·7/2 = 7 m."),
    ON(3, "Mashina tormozlanishda 36 km/soat dan to'xtaguncha 4 s harakatlandi. Tormoz yo'li necha metr? (tekis sekinlanuvchan)", 20, "v₀ = 10 m/s; s = v₀t/2 = 20 m."),
]

_g1 = F.graph([(0, 0), (4, 8), (10, 8), (14, 0)], [2, 4, 6, 8, 10, 12, 14], [2, 4, 6, 8])
Q["P9.2"] = [
    C(1, "v–t grafigida gorizontal chiziq nimani bildiradi?", "Tekis harakat (v = const)", ["Tinch holat", "Tezlanuvchan harakat", "Aylanma harakat"], "Tezlik o'zgarmas."),
    C(2, "v–t grafigi ostidagi yuza nimani ifodalaydi?", "Bosib o'tilgan yo'lni", ["Tezlanishni", "Kuchni", "Vaqtni"], "∫v dt = s."),
    N(2, "Chizmada v–t grafigi berilgan. 0–4 s oralig'idagi tezlanish?", 2, [8, 4, 0.5], "m/s²", "(8−0)/4 = 2.", fig=_g1),
    N(2, "Shu grafik bo'yicha 4–10 s oralig'ida bosib o'tilgan yo'l?", 48, [8, 32, 64], "m", "8·6 = 48.", fig=_g1),
    N(3, "Shu grafik bo'yicha 14 s davomida umumiy yo'l (trapetsiya yuzi)?", 88, [112, 64, 56], "m", "Asoslar 14 va 6, balandlik 8: (14+6)/2·8 = 80?? 0–4: 16; 4–10: 48; 10–14: 16 → 80.", fig=_g1) if False else N(3, "Shu grafik bo'yicha 14 s davomida umumiy yo'l?", 80, [112, 64, 56], "m", "0–4 s: 16 m; 4–10 s: 48 m; 10–14 s: 16 m → 80 m.", fig=_g1),
    C(2, "x–t grafigida qiya to'g'ri chiziqning og'ishi nimani bildiradi?", "Tezlikni", ["Tezlanishni", "Kuchni", "Massani"], "Burchak koeffitsiyenti = tezlik."),
    N(2, "x–t grafigida jism 2 s da koordinatasini 4 m dan 12 m ga o'zgartirdi. Tezligi?", 4, [8, 6, 16], "m/s", "(12−4)/2."),
    C(2, "v–t grafigi OX o'qidan pastda (v < 0) turgan to'g'ri chiziq bo'lsa, jism...", "koordinata o'qiga qarama-qarshi tomonga harakatlanmoqda", ["tinch turibdi", "tezlanish nolga teng", "Yerga yaqinlashmoqda"], "Tezlik proyeksiyasi manfiy."),
    ON(3, "v–t grafigi: 0 dan 6 s gacha tezlik 0 dan 12 m/s gacha chiziqli ortadi, keyin 4 s o'zgarmas. Jami necha metr yo'l bosildi?", 84, "36 + 48 = 84 m."),
    M(2, [("v–t da gorizontal chiziq", "tekis harakat"), ("v–t da qiya to'g'ri chiziq", "tekis tezlanuvchan harakat"), ("x–t da gorizontal chiziq", "tinch turish")], "Grafiklar ma'nosi."),
]

Q["P9.3"] = [
    C(1, "Erkin tushish tezlanishi Yer sirtida taxminan?", "9,8 m/s²", ["1 m/s²", "98 m/s²", "0,98 m/s²"], "g ≈ 9,8 (≈10)."),
    N(1, "Jism 20 m balandlikdan erkin tushsa (g=10), tushish vaqti?", 2, [4, 1, 10], "s", "t = √(2h/g) = √4."),
    N(2, "Yuqoriga 30 m/s tezlik bilan otilgan jism maksimal balandligi (g = 10)?", 45, [90, 30, 15], "m", "v²/(2g)."),
    N(2, "Shu jism ko'tarilish vaqti?", 3, [6, 30, 1.5], "s", "t = v₀/g."),
    N(2, "Erkin tushayotgan jismning 3 s dagi tezligi (g=10)?", 30, [15, 3, 90], "m/s", "v = gt."),
    N(3, "Jism 80 m balandlikdan erkin tushmoqda. Oxirgi sekundda bosib o'tgan yo'li?", 35, [40, 45, 30], "m", "t = 4 s; h(4) − h(3) = 80 − 45 = 35 m."),
    C(2, "Vakuumda qush pati va tosh bir balandlikdan tushsa...", "Bir vaqtda tushadi", ["Tosh oldin tushadi", "Pat oldin tushadi", "Ikkalasi ham to'xtab qoladi"], "Barcha jismlar bir xil g bilan tushadi."),
    ON(3, "Jism 5 s davomida erkin tushdi. Bosib o'tgan yo'li necha metr? (g = 10)", 125, "s = gt²/2 = 5·25."),
    ON(3, "Yuqoriga 20 m/s bilan otilgan jism qanday balandlikda (m) tezligi 10 m/s bo'ladi? (g = 10, ko'tarilishda)", 15, "h = (v₀²−v²)/(2g) = 300/20 = 15 m."),
]

Q["P9.4"] = [
    C(1, "Gorizontal otilgan jismning gorizontal tezlik komponenti qanday o'zgaradi?", "O'zgarmaydi", ["Ortadi", "Kamayadi", "Nolga teng"], "Gorizontal yo'nalishda kuch yo'q.", fig=F.horizontal_throw()),
    N(2, "Gorizontal otilgan jism 45 m balandlikdan tushsa (g = 10), uchish vaqti?", 3, [9, 4.5, 6], "s", "t = √(2h/g) = 3 s."),
    N(2, "Shu jism 12 m/s bilan otilgan bo'lsa, gorizontal uchish uzoqligi?", 36, [12, 108, 45], "m", "s = v₀t = 12·3."),
    C(2, "Burchak ostida otilgan jismning uchish uzoqligi qaysi burchakda eng katta (havo qarshiligisiz)?", "45°", ["30°", "60°", "90°"], "L = v₀² sin2α/g."),
    N(2, "v₀ = 20 m/s, α = 30°. Boshlang'ich vertikal tezlik komponenti?", 10, [17.3, 20, 40], "m/s", "v₀ sin30° = 10.", fig=F.projectile(30)),
    N(3, "v₀ = 20 m/s, α = 30° bo'lsa maksimal balandlik (g = 10)?", 5, [10, 20, 2.5], "m", "H = v_y²/(2g) = 100/20 = 5.", fig=F.projectile(30)),
    N(3, "Shu jismning uchish vaqti?", 2, [4, 1, 3.46], "s", "t = 2v_y/g = 2·10/10 = 2 s."),
    N(3, "45° da v₀ = 10 m/s bilan otilgan jism uchish uzoqligi (g=10)?", 10, [20, 5, 7.07], "m", "L = v₀²/g = 10 m."),
    ON(3, "Gorizontal otilgan jism 20 m balandlikdan 15 m/s bilan otildi. Yerga urilish payti tezligi moduli necha m/s? (g = 10)", 25, "v_y = √(2gh) = 20; v = √(225+400) = 25."),
]

Q["P9.5"] = [
    C(1, "Aylanish davri nima?", "Bir marta to'liq aylanishga ketgan vaqt", ["Vaqt birligidagi aylanishlar soni", "Burchak ko'chish", "Chiziqli tezlik"], "T — davr."),
    C(1, "Davr va chastota orasidagi bog'lanish?", "T = 1/ν", ["T = ν", "T = ν²", "T = 2πν"], "Teskari proporsional."),
    N(2, "Radiusi 2 m aylana bo'ylab jism 4 m/s tezlik bilan harakatlanmoqda. Markazga intilma tezlanish?", 8, [2, 16, 4], "m/s²", "a = v²/R = 16/2."),
    N(2, "Aylana radiusi 0,5 m, burchak tezligi 6 rad/s. Chiziqli tezlik?", 3, [12, 0.083, 6.5], "m/s", "v = ωR."),
    N(2, "Soniya mili davri qancha?", 60, [1, 3600, 12], "s", "Bir minut."),
    N(3, "Jism 10 s da 50 marta aylansa, chastotasi?", 5, [0.2, 500, 50], "Hz", "50/10."),
    N(3, "Radiusi 0,2 m g'ildirak chastotasi 5 Hz. Chiziqli tezlik (π=3,14)?", 6.28, [3.14, 1.0, 12.56], "m/s", "v = 2πνR = 2·3,14·5·0,2."),
    C(2, "Aylana bo'ylab tekis harakatda tezlanish qanday yo'nalgan?", "Markazga", ["Urinma bo'ylab", "Markazdan tashqariga", "Nolga teng"], "Markazga intilma."),
    ON(3, "Avtomobil g'ildiragi radiusi 0,4 m, markazi 20 m/s tezlik bilan harakatlanmoqda (sirpanishsiz). Burchak tezligi necha rad/s?", 50, "ω = v/R = 20/0,4."),
    M(2, [("T", "davr"), ("ν", "chastota"), ("ω", "burchak tezlik")], "Belgilar."),
]

Q["P9.6"] = [
    C(1, "Nyutonning ikkinchi qonuni?", "F = ma", ["F = mg", "F = kx", "F = pS"], "Teng ta'sir etuvchi kuch massa va tezlanish ko'paytmasi."),
    C(1, "Inersiya nima?", "Jismning tezligini saqlashga intilishi", ["Kuch turi", "Energiya turi", "Tezlanish"], "Birinchi qonun."),
    N(2, "5 kg massali jismga 20 N kuch ta'sir etsa, tezlanishi?", 4, [100, 0.25, 15], "m/s²", "a = F/m."),
    N(2, "2 kg jismga 6 N va 2 N qarama-qarshi kuch ta'sir etadi. Tezlanish?", 2, [4, 8, 3], "m/s²", "a = (6−2)/2."),
    C(2, "Nyutonning uchinchi qonuniga ko'ra ta'sir va aks ta'sir kuchlari...", "modul jihatdan teng, yo'nalishi qarama-qarshi, turli jismlarga qo'yilgan", ["bir jismga qo'yilgan", "bir-birini muvozanatlaydi", "turli modulga ega"], "Muvozanatlashmaydi."),
    N(3, "Massasi 1200 kg avtomobil 3 m/s² tezlanish bilan harakatlanmoqda, qarshilik kuchi 500 N. Tortish kuchi?", 4100, [3100, 3600, 3000], "N", "F = ma + F_q = 3600 + 500."),
    N(3, "Massasi 0,5 kg jism 10 m/s dan 20 m/s gacha 2 s da tezlashdi. Unga ta'sir etuvchi kuch?", 2.5, [5, 10, 1.25], "N", "a = 5; F = 0,5·5."),
    ON(3, "Tinch turgan 4 kg jismga 12 N kuch 5 s davomida ta'sir etdi. Bu vaqtda uning tezligi necha m/s bo'ladi?", 15, "a = 3; v = 15 m/s."),
    C(2, "Quyidagilardan qaysi sanoq sistemasi inersial?", "Yerga nisbatan tekis to'g'ri chiziqli harakatlanuvchi", ["Tezlanish bilan harakatlanuvchi", "Aylanuvchi karusel", "Tormozlanayotgan mashina"], "Inersial — tekis harakat."),
]

Q["P9.7"] = [
    C(1, "Ishqalanishsiz qiya tekislikda jism tezlanishi formulasi?", "a = g·sinα", ["a = g·cosα", "a = g·tgα", "a = g"], "Nishab bo'ylab komponent mg sinα.", fig=F.incline(30)),
    N(2, "α = 30°, ishqalanishsiz. Tezlanish (g = 10)?", 5, [8.66, 10, 2.5], "m/s²", "g sin30° = 5.", fig=F.incline(30)),
    N(2, "Qiya tekislikda 2 kg jismning normal reaksiya kuchi (α = 60°, g = 10)?", 10, [17.3, 20, 5], "N", "N = mg cosα = 20·0,5 = 10.", fig=F.incline(60, show_forces=True)),
    N(3, "α = 30°, μ = 0,1·√3 bo'lsa, jism pastga tezlanishi (g = 10)?", 3.5, [5, 1.5, 4.5], "m/s²", "a = g(sinα − μcosα) = 10(0,5 − 0,1·√3·√3/2) = 10(0,5−0,15) = 3,5.", fig=F.incline(30, mu=True)),
    C(2, "Qiya tekislikda jism tinch tursa, ishqalanish kuchi nimaga teng?", "mg·sinα", ["mg·cosα", "mg", "μ·mg"], "Tinchlik ishqalanishi nishab komponentini muvozanatlaydi.", fig=F.incline(30, mu=True)),
    N(3, "α = 37° (sin = 0,6, cos = 0,8), μ = 0,5. Jismning pastga tezlanishi (g = 10)?", 2, [6, 4, 1], "m/s²", "a = 10(0,6−0,5·0,8) = 2.", fig=F.incline(37, mu=True)),
    N(3, "Massasi 10 kg jismni α = 30° qiya tekislikda tekis yuqoriga tortish uchun (ishqalanishsiz) qancha kuch kerak?", 50, [86.6, 100, 25], "N", "F = mg sin30° = 50.", fig=F.incline(30)),
    ON(3, "Qiya tekislikda (sinα = 0,6, cosα = 0,8, μ = 0,25) jism tezlanishi bilan pastga sirpanyapti. Tezlanishi necha m/s²? (g = 10)", 4, "a = 10(0,6 − 0,25·0,8) = 4.", ),
    C(2, "Qiya tekislik burchagi ortsa, normal reaksiya kuchi...", "kamayadi", ["ortadi", "o'zgarmaydi", "nolga tengligicha qoladi"], "N = mg cosα, cos kamayadi."),
]

Q["P9.8"] = [
    N(2, "Atvud mashinasi: m₁ = 1 kg, m₂ = 3 kg. Tezlanish (g = 10, ishqalanishsiz)?", 5, [10, 2.5, 7.5], "m/s²", "a = (m₂−m₁)g/(m₁+m₂) = 20/4.", fig=F.atwood("1 kg", "3 kg")),
    N(3, "Shu mashinada ipning taranglik kuchi?", 15, [10, 30, 20], "N", "T = m₁(g + a) = 1·15.", fig=F.atwood("1 kg", "3 kg")),
    N(3, "Stol ustidagi m₁ = 2 kg (ishqalanishsiz) ip orqali osilgan m₂ = 3 kg bilan bog'langan. Tezlanish (g = 10)?", 6, [10, 5, 3], "m/s²", "a = m₂g/(m₁+m₂) = 30/5.", fig=F.table_pulley("2 kg", "3 kg")),
    N(3, "Shu holda ip tarangligi?", 12, [30, 18, 6], "N", "T = m₁a = 12.", fig=F.table_pulley("2 kg", "3 kg")),
    C(2, "Og'irlanmaydigan ip va blok uchun ipning ikkala uchidagi taranglik kuchlari...", "teng", ["turlicha", "nolga teng", "massaga proporsional"], "Ishqalanishsiz blokda."),
    C(1, "Bog'langan jismlar bir ip bilan harakatlanganda ularning tezlanishlari...", "teng modulli", ["har xil", "nolga teng", "massaga teskari"], "Ip cho'zilmaydi."),
    N(3, "Atvud mashinasida m₁ = 4 kg, m₂ = 6 kg. Tezlanish (g = 10)?", 2, [4, 1, 10], "m/s²", "a = 2·10/10.", fig=F.atwood("4 kg", "6 kg")),
    ON(3, "Stol ustida μ = 0,2 bilan m₁ = 3 kg jism, ip orqali osilgan m₂ = 2 kg bilan bog'langan. Tezlanish necha m/s²? (g = 10)", 2.8, "a = (m₂g − μm₁g)/(m₁+m₂) = (20−6)/5 = 2,8.", ),
    ON(3, "Atvud mashinasida m₁ = 2 kg, m₂ = 3 kg. Ipdagi taranglik necha N? (g = 10)", 24, "a = 2; T = 2(10+2) = 24 N."),
]

Q["P9.9"] = [
    C(1, "Butun olam tortishish qonuni formulasi?", "F = G·m₁m₂/r²", ["F = G·m₁m₂·r", "F = m·g/r", "F = G·m/r"], "Massalar ko'paytmasiga to'g'ri, masofa kvadratiga teskari."),
    C(1, "Birinchi kosmik tezlik taxminan?", "7,9 km/s", ["11,2 km/s", "16,7 km/s", "3 km/s"], "Yer sirtiga yaqin doiraviy orbita."),
    C(1, "Ikkinchi kosmik tezlik taxminan?", "11,2 km/s", ["7,9 km/s", "16,7 km/s", "9,8 km/s"], "Yer tortishidan chiqib ketish."),
    C(2, "Jismlar orasidagi masofa 2 marta ortsa, tortishish kuchi...", "4 marta kamayadi", ["2 marta kamayadi", "2 marta ortadi", "o'zgarmaydi"], "1/r²."),
    N(2, "Yer radiusi R. Yer sirtidan R balandlikda g qancha (g₀ = 10)?", 2.5, [5, 10, 1.25], "m/s²", "g = g₀/(1+h/R)² = 10/4."),
    N(3, "Sayyorada g = 4 m/s², radiusi Yer radiusining yarmiga teng. Uning massasi Yer massasining qanday ulushi? (g_Yer = 10 m/s²)", 0.1, [0.4, 0.2, 2.5], "", "g = GM/R²: M/M_Yer = (g/g_Yer)(R/R_Yer)² = 0,4·0,25 = 0,1."),
    C(2, "Sun'iy yo'ldosh Yer atrofida aylanishi uchun markazga intilma tezlanishni nima beradi?", "Tortishish kuchi", ["Dvigatel tortish kuchi", "Havo bosimi", "Inersiya"], "Gravitatsiya."),
    ON(3, "Yerdan R balandlikdagi doiraviy orbitada (r = 2R) sun'iy yo'ldosh tezligi birinchi kosmik tezlikdan necha marta kichik? (kvadrat ildiz 1,41 ga teng, 2 xona)", 1.41, "v = v₁/√2 → √2 ≈ 1,41 marta."),
    N(3, "Yer sirtida 60 kg odamga Yerdan R balandlikda ta'sir etuvchi tortishish kuchi (g₀ = 10)?", 150, [600, 300, 75], "N", "F = mg₀/4 = 150 N."),
]

Q["P9.10"] = [
    C(1, "Vaznsizlik holatida jism og'irligi...", "nolga teng", ["ikki baravar ortadi", "mg ga teng", "o'zgarmaydi"], "Tayanchga bosim yo'q."),
    N(2, "Lift 2 m/s² bilan tezlanib yuqoriga ketmoqda. 50 kg odam og'irligi (g = 10)?", 600, [500, 400, 100], "N", "P = m(g+a)."),
    N(2, "Lift 2 m/s² bilan tezlanib pastga ketmoqda. 50 kg odam og'irligi (g = 10)?", 400, [500, 600, 100], "N", "P = m(g−a)."),
    C(2, "O'ta og'irlik holatida tezlanish qanday yo'nalgan?", "Yuqoriga", ["Pastga", "Gorizontal", "Nolga teng"], "P > mg."),
    N(3, "Lift tekis tezlikda harakatlanmoqda, 70 kg odam og'irligi (g = 10)?", 700, [0, 770, 630], "N", "a = 0."),
    N(3, "Lift erkin tushmoqda: 80 kg odam og'irligi?", 0, [800, 80, 400], "N", "a = g → P = 0."),
    ON(3, "Lift yuqoriga a tezlanish bilan harakatlanganda 60 kg odam og'irligi 720 N bo'ldi. Tezlanish necha m/s²? (g = 10)", 2, "720 = 60(10 + a) → a = 2."),
    C(2, "Yer sun'iy yo'ldoshida kosmonavt vaznsiz, chunki...", "ular erkin tushish holatida (tortishish tezlanish beradi)", ["Yerning tortishishi yo'q", "havo yo'q", "massasi nolga teng"], "Tayanch ham, jism ham bir xil tezlanishda."),
    ON(3, "Prujinali tarozida odam 600 N ni ko'rsatdi, lift tezlanishsiz harakatlanmoqda. Odam massasi necha kg? (g = 10)", 60, "m = P/g."),
]

Q["P9.11"] = [
    C(1, "Jism impulsi formulasi?", "p = m·v", ["p = m·a", "p = F·s", "p = m/v"], "Massa va tezlik ko'paytmasi."),
    C(1, "Impulsning SI birligi?", "kg·m/s", ["N·m", "kg·m/s²", "J"], "p = mv."),
    N(2, "5 kg jism 4 m/s tezlik bilan harakatlanmoqda. Impulsi?", 20, [1.25, 9, 0.8], "kg·m/s", "5·4."),
    N(2, "Jismga 10 N kuch 3 s ta'sir qildi. Kuch impulsi?", 30, [3.3, 13, 7], "N·s", "FΔt."),
    N(2, "2 kg jism impulsi 12 kg·m/s ga o'zgardi. Tezligi qancha o'zgardi?", 6, [24, 3, 14], "m/s", "Δv = Δp/m."),
    N(3, "Massasi 60 kg odam 2 m/s bilan yurib, 40 kg aravachaga (tinch) sakrab chiqdi. Birgalikda tezlik?", 1.2, [2, 0.8, 3], "m/s", "60·2 = 100·v."),
    N(3, "Tinch turgan 100 kg qayiqdan 50 kg yuk bo'lgan 60 kg odam 5 m/s bilan sakradi (qayiq 100 kg, odam 60 kg). Qayiq tezligi (qayiq odamsiz massasi 100 kg)?", 3, [5, 2, 1.67], "m/s", "60·5 = 100·v → 3 m/s.") if False else N(3, "Tinch qayiq (100 kg) dan 60 kg odam 5 m/s tezlik bilan sakradi. Qayiq tezligi?", 3, [5, 2, 1.67], "m/s", "60·5 = 100·v → 3 m/s."),
    C(2, "Impulsning saqlanish qonuni qaysi sistemada bajariladi?", "Yopiq sistemada", ["Har qanday sistemada", "Faqat ochiq sistemada", "Faqat tinch jismlarda"], "Tashqi kuchlar yo'q yoki muvozanatda."),
    ON(3, "0,2 kg koptok 10 m/s tezlik bilan devorga tik uchib borib, xuddi shu tezlik bilan qaytdi. Impuls o'zgarishi moduli necha kg·m/s?", 4, "Δp = 0,2·(10+10) = 4."),
    ON(3, "Massasi 4 kg qurol­dan 10 g o'q 400 m/s tezlik bilan otildi. Qurolning orqaga tepish tezligi necha m/s?", 1, "0,01·400 = 4·v → v = 1."),
]

Q["P9.12"] = [
    C(1, "To'liq mexanik energiyaning saqlanish qonuni qachon bajariladi?", "Faqat konservativ kuchlar ishlaganda", ["Ishqalanish bo'lganda", "Har doim", "Jism tinch bo'lganda"], "Ishqalanishsiz."),
    N(2, "5 m balandlikdan erkin tushayotgan jism yerga urilish tezligi (g = 10)?", 10, [50, 25, 5], "m/s", "v = √(2gh)."),
    N(2, "Prujina qattiqligi 400 N/m, 5 sm siqilgan. Potensial energiya?", 0.5, [1, 20, 10], "J", "kx²/2 = 400·0,0025/2 = 0,5."),
    N(3, "2 kg jism 10 m/s bilan, tormozlanishda 20 m masofada to'xtadi. Ishqalanish kuchi?", 5, [10, 2.5, 20], "N", "mv²/2 = F·s → 100 = F·20."),
    N(3, "Matematik mayatnik 0,8 m balandlikdan qo'yib yuborildi. Pastki nuqtada tezligi (g = 10)?", 4, [8, 2, 16], "m/s", "v = √(2·10·0,8)."),
    C(2, "Ish-energiya teoremasi: kuchlarning bajargan ishi...", "kinetik energiya o'zgarishiga teng", ["potensial energiyaga teng", "impulsga teng", "quvvatga teng"], "A = ΔEk."),
    N(3, "3 kg jism 4 m/s dan 8 m/s gacha tezlashdi. Bajarilgan ish?", 72, [24, 96, 48], "J", "3(64−16)/2."),
    ON(3, "Jism 20 m balandlikdan erkin tushmoqda. Qaysi balandlikda (m) kinetik energiya potensialga teng bo'ladi? (yerdan hisoblang)", 10, "mgh = mg(H−h) → h = H/2."),
    ON(3, "Massasi 1 kg jism 10 m balandlikdan tushib, yerga 12 m/s bilan urildi. Havo qarshiligi bajargan ish moduli necha J? (g = 10)", 28, "mgh − mv²/2 = 100 − 72 = 28."),
]

Q["P9.13"] = [
    C(1, "Mutlaq noelastik to'qnashuvda...", "jismlar birgalikda harakatlanadi", ["energiya saqlanadi", "jismlar bir xil tezlik bilan qaytadi", "impuls yo'qoladi"], "Impuls saqlanadi, kinetik energiya qisman yo'qoladi."),
    N(2, "2 kg va 3 kg jismlar mos ravishda 5 m/s va 0 tezlik bilan harakatlanib, mutlaq noelastik to'qnashdi. Umumiy tezlik?", 2, [5, 1, 2.5], "m/s", "10/5."),
    C(1, "Mutlaq elastik to'qnashuvda saqlanadi...", "impuls va kinetik energiya", ["faqat impuls", "faqat energiya", "hech biri"], "Ikkalasi."),
    C(2, "Teng massali ikki shar markaziy elastik to'qnashganda, biri tinch bo'lsa...", "tezliklar almashadi", ["birgalikda harakat qiladi", "ikkalasi to'xtaydi", "ikkala shar bir tomonga qaytadi"], "Teng massalar."),
    N(3, "Mutlaq noelastik to'qnashuvda 2 kg (6 m/s) va 4 kg (0) jism. Yo'qolgan kinetik energiya?", 24, [36, 12, 48], "J", "Boshida 36 J; v = 2; keyin 12 J; yo'qotish 24 J."),
    N(3, "1 kg jism 4 m/s bilan tinch 3 kg ga mutlaq elastik urildi. 1 kg jismning urilishdan keyingi tezligi?", -2, [2, 4, -4], "m/s", "v₁ = (m₁−m₂)v/(m₁+m₂) = −2."),
    ON(3, "Mutlaq noelastik to'qnashuvda 3 kg (4 m/s) va 1 kg (−4 m/s) qarshi harakat. Umumiy tezlik necha m/s?", 2, "(12−4)/4 = 2."),
    N(3, "Shu to'qnashuvdagi issiqlikka aylangan energiya (3 kg 4 m/s, 1 kg −4 m/s)?", 48, [24, 16, 32], "J", "Boshida 24+8 = 32? 3·16/2=24, 1·16/2=8 → 32; keyin 4·4/2 = 8; Δ = 24.") if False else N(3, "Shu to'qnashuvda issiqlikka aylangan energiya?", 24, [48, 16, 32], "J", "Boshida 24+8 = 32 J; keyin 4·2²/2 = 8 J; yo'qotish 24 J."),
    C(2, "To'qnashuvda impuls saqlanishi uchun sistema...", "yopiq bo'lishi kerak", ["ochiq bo'lishi kerak", "tinch bo'lishi kerak", "elastik bo'lishi kerak"], "Tashqi kuchlar ta'sir etmasligi kerak."),
]

Q["P9.14"] = [
    C(1, "Harakatning nisbiyligi nimani anglatadi?", "Tezlik va trayektoriya sanoq sistemasiga bog'liq", ["Harakat mavjud emas", "Hamma jismlar tinch", "Tezlik hamma uchun bir xil"], "Galiley nisbiylik."),
    N(2, "Daryo oqimi 2 m/s, kema suvga nisbatan 5 m/s oqim bo'ylab. Qirg'oqqa nisbatan tezlik?", 7, [3, 10, 2.5], "m/s", "5 + 2."),
    N(2, "Shu kema oqimga qarshi. Qirg'oqqa nisbatan tezligi?", 3, [7, 10, 2.5], "m/s", "5 − 2."),
    N(3, "Kema oqimga perpendikulyar yo'nalishda suvga nisbatan 4 m/s, oqim 3 m/s. Qirg'oqqa nisbatan tezlik moduli?", 5, [7, 1, 3.5], "m/s", "√(16+9)."),
    N(3, "Eni 120 m daryoni kema oqimga perpendikulyar 4 m/s (suvga nisbatan) bilan kesib o'tishi uchun vaqt?", 30, [40, 24, 17], "s", "120/4."),
    N(3, "Shu holatda (oqim 3 m/s) oqim kemani qancha masofaga siljitadi?", 90, [120, 60, 30], "m", "3·30."),
    C(2, "Bir-biriga qarab harakatlanayotgan ikki poyezd tezliklari 20 va 30 m/s. Birinchisiga nisbatan ikkinchining tezligi?", "50 m/s", ["10 m/s", "25 m/s", "600 m/s"], "Yig'indi."),
    ON(3, "Eskalator tinch turganda odam 60 s da yuqoriga chiqadi, odam turib olsa eskalator 30 s da olib chiqadi. Ikkalasi birgalikda harakatlansa necha sekundda chiqadi?", 20, "1/t = 1/60 + 1/30 = 3/60 → t = 20."),
    ON(3, "Poyezd 54 km/soat, uning yonidagi yo'lovchi poyezd yo'nalishiga qarshi 1,5 m/s yuradi. Yo'lovchining yerga nisbatan tezligi necha m/s?", 13.5, "54 km/s = 15 m/s; 15 − 1,5 = 13,5 m/s."),
]

Q["P9.15"] = [
    C(1, "Uzluksizlik tenglamasi qaysi?", "S₁v₁ = S₂v₂", ["S₁v₂ = S₂v₁", "S₁ + v₁ = S₂ + v₂", "S₁/v₁ = S₂/v₂ ga teng"], "Suyuqlik hajmi sarfi saqlanadi."),
    C(1, "Quvur torayganda suyuqlik tezligi...", "ortadi", ["kamayadi", "o'zgarmaydi", "nolga teng"], "S kichik, v katta."),
    C(2, "Bernulli tenglamasiga ko'ra, gorizontal quvurda tezlik katta joyda statik bosim...", "kichik bo'ladi", ["katta bo'ladi", "o'zgarmaydi", "nolga teng"], "p + ρv²/2 = const."),
    N(2, "Quvur kesimi 20 sm² dan 5 sm² gacha torayadi. Birinchi kesimda tezlik 1 m/s. Ikkinchisida?", 4, [0.25, 2, 1], "m/s", "S₁v₁ = S₂v₂."),
    N(3, "Suv ρ = 1000, tezlik 2 m/s dan 4 m/s ga oshdi (gorizontal). Bosim farqi?", 6000, [2000, 12000, 3000], "Pa", "Δp = ρ(v₂²−v₁²)/2 = 500·12."),
    N(3, "Ochiq idish tubidagi teshikdan suv oqib chiqish tezligi (h = 0,8 m, g=10)?", 4, [8, 2, 1.6], "m/s", "v = √(2gh)."),
    ON(3, "Idishdagi suv sathi teshikdan 5 m yuqorida. Teshikdan oqish tezligi necha m/s? (g = 10)", 10, "v = √(2·10·5) = 10."),
    C(2, "Samolyot qanoti ko'tarish kuchi qaysi qonunga asoslangan?", "Bernulli", ["Paskal", "Arximed", "Guk"], "Yuqorida tezlik katta, bosim kichik."),
]

Q["P9.16"] = [
    C(1, "Ikkita prujina ketma-ket ulanganda ekvivalent qattiqlik?", "1/k = 1/k₁ + 1/k₂", ["k = k₁ + k₂", "k = k₁ k₂", "k = k₁ − k₂"], "Ketma-ket.", fig=F.spring_system("series")),
    C(1, "Parallel ulangan prujinalar ekvivalent qattiqligi?", "k = k₁ + k₂", ["1/k = 1/k₁ + 1/k₂", "k = k₁/k₂", "k = k₁ − k₂"], "Parallel.", fig=F.spring_system("parallel")),
    N(2, "k₁ = 100 N/m va k₂ = 100 N/m prujinalar ketma-ket. k_ekv?", 50, [200, 100, 25], "N/m", "100·100/200.", fig=F.spring_system("series")),
    N(2, "k₁ = 300 va k₂ = 200 N/m parallel. k_ekv?", 500, [120, 100, 250], "N/m", "Yig'indi.", fig=F.spring_system("parallel")),
    N(3, "k₁ = 60 va k₂ = 40 N/m ketma-ket. k_ekv?", 24, [100, 50, 20], "N/m", "60·40/100.", fig=F.spring_system("series")),
    N(3, "Parallel prujinalarga 10 N kuch qo'yilganda cho'zilish (k₁ = 30, k₂ = 20 N/m)?", 0.2, [0.5, 2, 0.12], "m", "x = F/(k₁+k₂) = 10/50.", fig=F.spring_system("parallel")),
    C(2, "Jism muvozanatda bo'lishi uchun kuchlarning vektor yig'indisi...", "nolga teng bo'lishi kerak", ["maksimal bo'lishi kerak", "massaga teng", "doim 10 N"], "∑F = 0."),
    ON(3, "Yengil sterjen ikki uchida 4 N va 6 N yuk bor. Sterjen uzunligi 1 m. Qaysi nuqtaga qo'yilgan tayanch muvozanat beradi: katta yukdan necha sm masofada?", 40, "4·x₁ = 6·x₂; x₁ + x₂ = 100 → x₂ = 40 sm."),
    ON(3, "k₁ = 200 N/m va k₂ = 300 N/m prujinalar ketma-ket, ularga 12 N kuch ta'sir etadi. Umumiy cho'zilish necha sm?", 10, "k = 120; x = 12/120 = 0,1 m = 10 sm."),
]
