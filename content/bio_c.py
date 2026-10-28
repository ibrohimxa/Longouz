"""Biologiya: qo'shimcha mavzular (botanika, zoologiya, odam, sitologiya, genetika, ekologiya)."""
from ._dsl import C, O, M

Q = {}

Q["B6.8"] = [
    C(1, "Gulning urug'langandan keyin rivojlanishidan hosil bo'ladigan a'zo qaysi?", "Meva", ["Gul kosachasi", "Barg", "Ildizpoya"], "Urug'chi tuguni mevaga, urug'kurtak urug'ga aylanadi."),
    C(1, "Urug'kurtakdan nima hosil bo'ladi?", "Urug'", ["Meva", "Gul", "Kurtak"], "Urug'langan urug'kurtak urug'ga aylanadi."),
    C(1, "Urug'chi tuguni urug'langandan keyin nimaga aylanadi?", "Mevaga", ["Urug'ga", "Changchiga", "Gultojiga"], "Tugun mevani hosil qiladi."),
    C(2, "Mevaning tashqi qismi (po'sti) nima deb ataladi?", "Meva po'stlog'i (perikarp)", ["Endosperm", "Urug' po'sti", "Murtak"], "Perikarp mevaning devori."),
    C(2, "Quyidagilardan qaysi biri quruq meva?", "Loviya", ["Olma", "Uzum", "Shaftoli"], "Loviya dukkaklilarning quruq mevasi."),
    C(2, "Qaysi meva sersuv (mag'izli) meva hisoblanadi?", "Pomidor", ["Bug'doy donagi", "Ko'knori qo'zoq", "Kungaboqar pistasi"], "Pomidor — rezavor meva."),
    C(3, "Urug'ning asosiy qismi — yangi o'simlik boshlang'ichi qaysi?", "Murtak", ["Endosperm", "Urug' po'sti", "Urug' oq"], "Murtak ildizcha, poyacha, kurtakcha va urug'pallalardan iborat."),
    O(3, "Ikki urug'pallali o'simlik urug'ida zaxira oziq moddalar to'planadigan qism nomini yozing (bir so'z).", ["urug'palla", "urug'pallalar", "urugpalla"], "Ikki urug'pallalilarda zaxira oziq urug'pallalarda to'planadi."),
]

Q["B6.9"] = [
    C(1, "Kartoshka tuganagi bilan ko'payish ko'payishning qaysi turi?", "Vegetativ", ["Jinsiy", "Sporalar bilan", "Urug' bilan"], "Vegetativ ko'payish — o'simlik vegetativ a'zolari yordamida."),
    C(1, "Qulupnay qaysi vegetativ a'zo orqali ko'payadi?", "Mo'ylov (ustun poya)", ["Tuganak", "Piyozbosh", "Ildizpoya"], "Qulupnay mo'ylovlar bilan ko'payadi."),
    C(2, "Piyoz qanday modifikatsiyalashgan yer osti poyasi orqali ko'payadi?", "Piyozbosh", ["Tuganak", "Ildizpoya", "Mo'ylov"], "Piyozbosh — qisqargan poya va etli barglar."),
    C(2, "Tok va gilosni ko'paytirishda qo'llanadigan usul qaysi?", "Qalamcha", ["Sporalar", "Urug'", "Tuganak"], "Qalamcha — poyaning kesilgan bo'lagi."),
    C(2, "Mevali daraxt navini saqlab ko'paytirishda ishlatiladigan usul qaysi?", "Payvandlash", ["Urug'dan ekish", "Sporalar", "Chang bilan changlatish"], "Payvand — nav xususiyatlarini saqlaydi."),
    C(3, "Vegetativ ko'payishning asosiy afzalligi nima?", "Ona o'simlik belgilari saqlanadi va tez o'sadi", ["Yangi belgilar paydo bo'ladi", "Urug' kerak bo'ladi", "O'simlik changlanadi"], "Genetik jihatdan bir xil nasl olinadi."),
    O(3, "Buta yoki daraxtning novdasini yerga egib ko'mib ko'paytirish usulini nima deymiz? (bir so'z)", ["parxish", "parxishlash"], "Parxish — novdani yerga bosib ildiz oldirish."),
]

Q["B6.10"] = [
    C(1, "Suv o'tlarining tanasi qanday nomlanadi?", "Tallom (tana)", ["Poya", "Ildiz", "Barg"], "Suv o'tlarida haqiqiy ildiz, poya, barg yo'q."),
    C(1, "Xlorella qaysi guruhga kiradi?", "Bir hujayrali yashil suv o'ti", ["Qo'ng'ir suv o'ti", "Qizil suv o'ti", "Zamburug'"], "Xlorella — yashil suv o'ti."),
    C(2, "Spirogira hujayrasidagi xloroplast qanday shaklda?", "Spiral lenta", ["Yulduzsimon", "Dumaloq", "Kosasimon"], "Spirogira nomi spiral xloroplastdan."),
    C(2, "Dengiz karami (laminariya) qaysi guruh vakili?", "Qo'ng'ir suv o'tlari", ["Yashil suv o'tlari", "Qizil suv o'tlari", "Diatom o'tlar"], "Laminariya — qo'ng'ir suv o'ti."),
    C(2, "Suv o'tlari atmosferani qaysi gaz bilan boyitadi?", "Kislorod", ["Karbonat angidrid", "Azot", "Metan"], "Fotosintezda kislorod ajraladi."),
    C(3, "Qizil suv o'tlaridan qaysi mahsulot olinadi?", "Agar-agar", ["Kraxmal", "Selluloza", "Shakar"], "Agar-agar qizil suv o'tlaridan olinadi."),
    O(3, "Suv o'tlarida jinssiz ko'payishni ta'minlovchi harakatchan hujayra nomini yozing.", ["zoospora", "zoosporalar"], "Zoosporalar xivchinli jinssiz hujayralar."),
]

Q["B6.11"] = [
    C(1, "Moxlarning ildizi o'rnini nima bajaradi?", "Ildizsimon o'simtalar (rizoidlar)", ["Haqiqiy ildizlar", "Tuganaklar", "Mo'ylovlar"], "Moxlarda rizoidlar bor."),
    C(1, "Sfagnum mox qayerda ko'p uchraydi?", "Botqoqlikda", ["Cho'lda", "Dengizda", "Tog' cho'qqisida"], "Sfagnum botqoqlikda o'sib torf hosil qiladi."),
    C(2, "Qirqbo'g'imning sporalari qayerda yetiladi?", "Sporali boshoqchada", ["Bargda", "Ildizda", "Gulda"], "Sporali boshoqchada sporalar yetiladi."),
    C(2, "Paporotniksimonlarda sporalar barg orqa tomonidagi qaysi tuzilmada yetiladi?", "Sporangiylar to'plamida (so'rus)", ["Gulda", "Mevada", "Urug'da"], "So'rus — sporangiylar to'plami."),
    C(2, "Mox va paporotniklarning o'xshashligi nima?", "Sporalar bilan ko'payadi", ["Urug' bilan ko'payadi", "Gul hosil qiladi", "Meva hosil qiladi"], "Ikkalasi ham sporali o'simlik."),
    C(3, "Paporotniksimonlarda jinsiy nasl (gametofit) qanday nomlanadi?", "O'simtacha", ["Gul", "Sporofit", "Murtak"], "Gametofit — yurak shaklidagi o'simtacha."),
    O(3, "Moxlarda spora yetiladigan qutichani nima deymiz? (bir so'z)", ["qutichasi", "sporogon", "quticha", "spora qutichasi"], "Sporogon — spora qutichasi."),
]

Q["B6.12"] = [
    C(1, "Qarag'ayning urug'i qayerda joylashadi?", "Qubba tangachalarida ochiq holda", ["Meva ichida", "Ildizda", "Bargda"], "Yalang'ochurug'lilar urug'i ochiq joylashadi."),
    C(1, "Yalang'ochurug'lilarda gul bormi?", "Yo'q, gul va meva hosil qilmaydi", ["Ha, katta gul", "Ha, mayda gul", "Faqat meva"], "Ularda haqiqiy gul va meva yo'q."),
    C(2, "Qarag'ay changi nima yordamida tarqaladi?", "Shamol", ["Hasharot", "Suv", "Qush"], "Shamol bilan changlanadi."),
    C(2, "Qaysi o'simlik yalang'ochurug'lilarga kiradi?", "Archa", ["Olma", "Bug'doy", "Mol'va"], "Archa — ignabargli."),
    C(2, "Ignabarglar suv yo'qotishini kamaytirishining sababi?", "Barg yuzasi qalin kutikula bilan qoplangan", ["Barglari yirik", "Meva hosil qiladi", "Ildizi yo'q"], "Qalin kutikula bug'lanishni kamaytiradi."),
    C(3, "Archa qaysi sinfga kiradi?", "Ignabarglilar", ["Ginkgolar", "Sikadlar", "Gnetumlar"], "Archa, qarag'ay, qoraqarag'ay — ignabarglilar."),
    O(3, "Qarag'ay qubbasida urug'kurtaklar joylashgan qismni nima deymiz? (bir so'z)", ["tangacha", "urug' tangacha", "urug'tangacha"], "Urug'li tangachalarda urug'kurtaklar joylashadi."),
]

Q["B6.13"] = [
    C(1, "Fotosintez jarayonida qaysi gaz yutiladi?", "Karbonat angidrid", ["Kislorod", "Azot", "Vodorod"], "CO₂ + H₂O + yorug'lik → glyukoza + O₂."),
    C(1, "Fotosintez qaysi hujayra organoidida boradi?", "Xloroplastda", ["Mitoxondriyada", "Yadroda", "Ribosomada"], "Xloroplastda xlorofill bor."),
    C(1, "Fotosintez natijasida qaysi gaz ajraladi?", "Kislorod", ["Karbonat angidrid", "Ammiak", "Metan"], "Kislorod ajraladi."),
    C(2, "Fotosintez uchun zarur bo'lgan energiya manbai?", "Quyosh nuri", ["Issiqlik", "Shamol", "Suv"], "Yorug'lik energiyasi."),
    C(2, "Fotosintez tenglamasida hosil bo'lgan organik modda qaysi?", "Glyukoza", ["Oqsil", "Yog'", "Nuklein kislota"], "C₆H₁₂O₆ hosil bo'ladi."),
    C(2, "Barg og'izchalari fotosintezda qanday vazifa bajaradi?", "Gaz almashinuvini ta'minlaydi", ["Suvni so'radi", "Mineral tuzlarni yutadi", "Urug' hosil qiladi"], "Og'izchalar orqali CO₂ kiradi."),
    C(3, "Fotosintezning umumiy tenglamasida 6CO₂ bilan qancha suv molekulasi qatnashadi?", "6", ["12", "3", "1"], "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂."),
    O(3, "6 molekula CO₂ dan fotosintezda nechta molekula kislorod ajraladi? (raqam)", ["6", "olti"], "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂."),
]

Q["B6.14"] = [
    C(1, "O'simliklarda nafas olish qaysi organoidlarda sodir bo'ladi?", "Mitoxondriyada", ["Xloroplastda", "Vakuolada", "Yadroda"], "Energiya mitoxondriyada ajraladi."),
    C(1, "Transpiratsiya nima?", "O'simlikdan suvning bug'lanishi", ["Suvning ildizga kirishi", "Fotosintez", "Mineral tuzlarning yutilishi"], "Suv bargdagi og'izchalar orqali bug'lanadi."),
    C(2, "Transpiratsiyaning asosiy ahamiyati nima?", "Suvning ildizdan bargga ko'tarilishini ta'minlaydi", ["Kislorod ishlab chiqaradi", "Urug' hosil qiladi", "Poyani yo'g'onlashtiradi"], "So'ruvchi kuch hosil bo'ladi."),
    C(2, "Qaysi omil transpiratsiyani kuchaytiradi?", "Havo harorati ortishi", ["Havo namligi ortishi", "Sovuq", "Bulutli ob-havo"], "Issiq va quruq havoda transpiratsiya kuchayadi."),
    C(2, "O'simlik nafas olganda qaysi gaz ajraladi?", "Karbonat angidrid", ["Kislorod", "Azot", "Argon"], "Nafas olish: glyukoza + O₂ → CO₂ + H₂O + energiya."),
    C(3, "Og'izcha hujayralari (qo'riqchi hujayralar) turgori oshsa nima bo'ladi?", "Og'izcha ochiladi", ["Og'izcha yopiladi", "Barg to'kiladi", "Fotosintez to'xtaydi"], "Turgor ortsa hujayralar egilib, teshik ochiladi."),
    O(3, "O'simlikda suv bug'lanishi uchun asosiy teshiklar nomini yozing (bir so'z).", ["og'izcha", "og'izchalar", "ogizcha"], "Og'izchalar orqali bug'lanadi."),
]

Q["B6.15"] = [
    C(1, "Ildiz suvni va mineral tuzlarni qaysi zona orqali so'radi?", "So'rish zonasi (ildiz tukchalari)", ["Bo'linish zonasi", "O'tkazish zonasi", "Ildiz qini"], "Ildiz tukchalari asosiy so'rish joyi."),
    C(1, "O'simlik uchun eng muhim mineral element oqsil sintezida qaysi?", "Azot", ["Kaliy", "Temir", "Natriy"], "Azot oqsillar va nuklein kislotalar tarkibida."),
    C(2, "Fosfor yetishmasa o'simlik barglari qanday rangga kiradi?", "To'q yashil-binafsha tusga", ["Sarg'ayadi", "Oqaradi", "Qizaradi-sarg'ayadi"], "Fosfor yetishmovchiligi belgisi."),
    C(2, "Kaliy o'simlik hayotida nima vazifani bajaradi?", "Suv almashinuvi va fotosintezni tartibga soladi", ["Oqsil hosil qiladi", "Xlorofill markazi", "Hujayra devorini quradi"], "Kaliy ferment faolligini ta'minlaydi."),
    C(2, "Dukkakli o'simliklar ildizidagi tuganak bakteriyalar nima qiladi?", "Havo azotini o'zlashtiradi", ["Fosfor to'playdi", "Suvni tozalaydi", "Kislorod ajratadi"], "Tuganak bakteriyalar azotni bog'laydi."),
    C(3, "Magniy qaysi organik moddaning tarkibida bor?", "Xlorofill", ["Gemoglobin", "Insulin", "ATF"], "Xlorofill markazida Mg atomi."),
    O(3, "Ildizning so'rish zonasida suv va tuzlarni so'ruvchi o'simtalar nomini yozing.", ["ildiz tukchalari", "ildiz tukchasi", "tukchalar", "ildiz tuklari"], "Ildiz tukchalari."),
]

# ---------------------------------------------------------------- 7-SINF
Q["B7.7"] = [
    C(1, "Gidra qaysi tipga kiradi?", "Bo'shliqichlilar", ["Yassi chuvalchanglar", "Mollyuskalar", "Bo'g'imoyoqlilar"], "Gidra — chuchuk suv bo'shliqichlisi."),
    C(1, "Gidraning ovqat hazm qilish bo'shlig'i qanday ataladi?", "Ichak bo'shlig'i", ["Me'da", "Kloaka", "Tana bo'shlig'i"], "Gidrada yagona ichak bo'shlig'i va og'iz teshigi."),
    C(2, "Gidrada himoya vazifasini bajaruvchi hujayralar qaysi?", "Nashtarli (chaqiruvchi) hujayralar", ["Nerv hujayralar", "Epiteliy-mushak hujayralar", "Jinsiy hujayralar"], "Nashtarli hujayralar zahar chiqaradi."),
    C(2, "Gidra tanasida simmetriya turi qanday?", "Nurli", ["Ikki yoqlama", "Asimmetriya", "Spiral"], "Bo'shliqichlilar nurli simmetriyali."),
    C(2, "Gidra qanday ko'payadi?", "Kurtaklanish va jinsiy yo'l bilan", ["Faqat bo'linish bilan", "Sporalar bilan", "Faqat urug'lanish bilan"], "Kurtaklanish — jinssiz ko'payish."),
    C(3, "Marjon poliplarining skeleti qaysi moddadan?", "Ohak (CaCO₃)", ["Xitin", "Kremniy", "Selluloza"], "Marjon rifalari ohakdan iborat."),
    O(3, "Gidrada tanani qoplovchi, nerv va mushak xususiyatlariga ega hujayralar nomini yozing (epiteliy-...)", ["epiteliy-mushak", "epiteliy mushak"], "Epiteliy-mushak hujayralar."),
]

Q["B7.8"] = [
    C(1, "Mollyuskalar tanasi qaysi qismlardan iborat?", "Tana, oyoq, mantiya", ["Bosh, ko'krak, qorin", "Faqat bosh", "Tana, dum"], "Mollyuskalar yumshoq tanali."),
    C(1, "Gastropodlar (qorinoyoqlilar) vakili?", "Uzum shilliqqurti", ["Midiya", "Kalmar", "Sakkizoyoq"], "Shilliqqurt — qorinoyoqli."),
    C(2, "Ikki pallali mollyuskalarda nafas olish organi?", "Jabra", ["O'pka", "Traxeya", "Teri"], "Midiya jabralari bilan nafas oladi."),
    C(2, "Bosh oyoqli mollyuskaga qaysi hayvon kiradi?", "Kalmar", ["Midiya", "Shilliqqurt", "Gulbaxor"], "Kalmar, sakkizoyoq — bosh oyoqlilar."),
    C(2, "Tabiiy marvarid qaysi mollyuskalarda hosil bo'ladi?", "Ikki pallalilarda (marvarid sadafi)", ["Qorinoyoqlilarda", "Bosh oyoqlilarda", "Hasharotlarda"], "Mantiya ajratgan sadaf modda qatlamlar bilan."),
    C(3, "Mollyuskalar qon aylanish tizimi qanday?", "Ochiq (bosh oyoqlilar — yopiq)", ["Hammasida yopiq", "Qon aylanishi yo'q", "Faqat kapillyarlar"], "Ko'pchiligida ochiq, bosh oyoqlilarda yopiq."),
    O(3, "Mollyuska tanasini qoplab, sadaf ajratuvchi teri burmasini nima deymiz? (bir so'z)", ["mantiya"], "Mantiya sadaf hosil qiladi."),
]

Q["B7.9"] = [
    C(1, "Yomg'ir chuvalchangi qaysi tipga kiradi?", "Halqali chuvalchanglar", ["Yassi chuvalchanglar", "Yumaloq chuvalchanglar", "Bo'shliqichlilar"], "Halqali chuvalchang tanasi halqalarga bo'lingan."),
    C(1, "Yomg'ir chuvalchangi tuproq unumdorligiga qanday ta'sir qiladi?", "Tuproqni yumshatadi va chirindi hosil qiladi", ["Tuproqni zaharlaydi", "Mineral tuzni yo'qotadi", "Hech qanday"], "Ular tuproqni aralashtiradi."),
    C(2, "Yomg'ir chuvalchangining qon aylanish tizimi qanday?", "Yopiq", ["Ochiq", "Yo'q", "Aralash"], "Qon tomirlar orqali, yopiq tizim."),
    C(2, "Chuvalchangning nafas olish organi?", "Teri", ["Jabra", "O'pka", "Traxeya"], "Teri orqali gaz almashinuvi."),
    C(2, "Chuvalchang tanasida halqalarning bo'linishi qanday ataladi?", "Metameriya (segmentatsiya)", ["Simmetriya", "Regeneratsiya", "Metamorfoz"], "Metameriya — tana bo'g'imlarga bo'linishi."),
    C(3, "Zuluk halqali chuvalanglarning qaysi sinfiga kiradi?", "Zulukdoshlar", ["Ko'p tukli halqalilar", "Kam tukli halqalilar", "Yassi chuvalanglar"], "Zuluk halqali chuvalanglarning zulukdoshlar sinfiga kiradi."),
    O(3, "Yomg'ir chuvalchangining ayirish organi nomini yozing (bir so'z).", ["nefridiy", "nefridiylar", "metanefridiy"], "Nefridiylar ayirish organi."),
]

Q["B7.10"] = [
    C(1, "Hasharotlarning oyoqlari soni nechta?", "6", ["4", "8", "10"], "Hasharotlarning 3 juft oyog'i bor."),
    C(1, "Hasharotlar tanasi nechta qismdan iborat?", "3 (bosh, ko'krak, qorin)", ["2", "4", "5"], "Bosh, ko'krak, qorin."),
    C(2, "To'liq o'zgarish bilan rivojlanuvchi hasharot qaysi?", "Kapalak", ["Chigirtka", "Suvarak", "Termit"], "Tuxum → lichinka → g'umbak → imago."),
    C(2, "Hasharotlarning nafas olish organi?", "Traxeya", ["Jabra", "O'pka", "Teri"], "Traxeyalar orqali havo bevosita to'qimalarga yetadi."),
    C(2, "Asalarilar oilasida tuxum qo'yuvchi urg'ochi qaysi?", "Ona asalari", ["Ishchi asalari", "Trutenlar", "Qorovul asalari"], "Ona asalari tuxum qo'yadi."),
    C(3, "Chala o'zgarish bilan rivojlanishda qaysi bosqich yo'q?", "G'umbak", ["Tuxum", "Lichinka", "Voyaga yetgan"], "Chala o'zgarishda g'umbak yo'q."),
    O(3, "Hasharotlarning qon aylanish tizimi turi qanday? (ochiq yoki yopiq)", ["ochiq"], "Qon tomirlardan to'qima oraliqlariga quyiladi."),
]

Q["B7.11"] = [
    C(1, "Baliqlar nafas olish organi?", "Jabra", ["O'pka", "Teri", "Traxeya"], "Baliqlar jabra bilan nafas oladi."),
    C(1, "Baliqlar yuragi nechta kameradan iborat?", "2 (bitta bo'lmacha, bitta qorincha)", ["3", "4", "1"], "Ikki kamerali yurak, bitta qon aylanish doirasi."),
    C(2, "Baliqlarda yon chiziq organi nima vazifani bajaradi?", "Suv oqimi va bosimini sezadi", ["Ovqat hazm qiladi", "Nafas oladi", "Ko'payadi"], "Yon chiziq mexanik sezgi organi."),
    C(2, "Suzgich pufagi nima uchun kerak?", "Suvda muvozanatni ushlab turadi", ["Nafas olish uchun", "Ovqat hazm uchun", "Ko'payish uchun"], "Suzish chuqurligini boshqaradi."),
    C(2, "Baliqlarda qon aylanish doirasi nechta?", "1", ["2", "3", "4"], "Bitta doira."),
    C(3, "Tuxum qo'yish uchun dengizdan daryolarga ko'tariladigan baliq qaysi?", "Losos", ["Ugor", "Karp", "Treska"], "Losos anadrom baliq."),
    O(3, "Baliqlar tanasini qoplovchi suyak plastinkalar nomini yozing (bir so'z).", ["tangacha", "tangachalar"], "Tangachalar."),
]

Q["B7.12"] = [
    C(1, "Amfibiyalarga kiruvchi hayvon?", "Baqa", ["Kaltakesak", "Timsoh", "Toshbaqa"], "Baqa — amfibiya."),
    C(1, "Reptiliyalarning terisi qanday?", "Quruq, shox tangachalar bilan qoplangan", ["Nam va silliq", "Pat bilan", "Jun bilan"], "Reptiliyalar teri nafasi olmaydi."),
    C(2, "Amfibiyalar yuragi nechta kameradan iborat?", "3", ["2", "4", "1"], "Ikki bo'lmacha va bitta qorincha."),
    C(2, "Baqa lichinkasi qanday ataladi?", "Itbaliq", ["Lichinka-nimfa", "G'umbak", "Gusenitsa"], "Itbaliq jabra bilan nafas oladi."),
    C(2, "Reptiliyalarda tuxum nimasi bilan himoyalangan?", "Qattiq yoki charm po'st", ["Hech narsa", "Suv", "Yog'"], "Quruqlikda rivojlanishga moslashgan."),
    C(3, "Qaysi reptiliyalarning yuragi 4 kamerali?", "Timsohlar", ["Ilonlar", "Kaltakesaklar", "Toshbaqalar"], "Timsohlarda to'liq to'siq mavjud."),
    O(3, "Reptiliya tuxumida homila oziqlanadigan zaxira modda qaysi qismda to'planadi? (bir so'z)", ["sarig'i", "sarig'", "sariq", "sarig'lik"], "Zaxira oziq tuxum sarig'ida to'planadi."),
]

Q["B7.13"] = [
    C(1, "Qushlarning old oyoqlari nimaga aylangan?", "Qanotga", ["Panjaga", "Dumga", "Tumshuqqa"], "Qanotlar uchish uchun."),
    C(1, "Qushlar yuragi nechta kamerali?", "4", ["3", "2", "1"], "To'liq 4 kamerali, ikki qon aylanish doirasi."),
    C(2, "Qushlarda issiqlik muvozanati qanday?", "Doimiy tana harorati (issiqqonli)", ["O'zgaruvchan", "Muhit haroratiga bog'liq", "Qish uyqusida"], "Qushlar gomoyotermli."),
    C(2, "Qush skeletining uchishga moslashuvi nima?", "Suyaklar yengil, ichi havo bilan to'lgan", ["Suyaklari og'ir", "Skelet yo'q", "Suyaklari yo'g'on"], "Pnevmatik suyaklar."),
    C(2, "Qushlarda ovqat mayda toshchalar bilan maydalanadigan bo'lim?", "Muskulli oshqozon", ["Jig'ildon", "Bezli oshqozon", "To'g'ri ichak"], "Muskulli oshqozon tosh yordamida."),
    C(3, "Qushlarda chap aorta yoyi o'rniga qaysi yoy saqlanadi?", "O'ng aorta yoyi", ["Chap aorta yoyi", "Ikkalasi ham", "Hech biri"], "Qushlarda o'ng yoy qolgan."),
    O(3, "Qushlar azotli almashinuvning qaysi mahsulotini ajratadi? (ikki so'z)", ["siydik kislotasi"], "Qushlar siydik kislotasini ajratadi."),
]

Q["B7.14"] = [
    C(1, "Sutemizuvchilar bolasini nima bilan oziqlantiradi?", "Sut bilan", ["Tuxum bilan", "Hasharot bilan", "O'simlik bilan"], "Sut bezlari bor."),
    C(1, "Sutemizuvchilar tanasi nima bilan qoplangan?", "Jun", ["Pat", "Tangacha", "Shilliq"], "Jun — teri hosilasi."),
    C(2, "Tuxum qo'yuvchi sutemizuvchi qaysi?", "Ornitorink", ["Kenguru", "Delfin", "Quyon"], "Ornitorink tuxum qo'yadi."),
    C(2, "Sutemizuvchilar yuragi?", "4 kamerali", ["3 kamerali", "2 kamerali", "1 kamerali"], "Ikki qon aylanish doirasi."),
    C(2, "Sutemizuvchilar miyasining eng rivojlangan bo'limi?", "Katta yarim sharlar po'stlog'i", ["Miyacha", "Uzunchoq miya", "O'rta miya"], "Po'stloq egatlar bilan."),
    C(3, "Kenguru qaysi guruhga kiradi?", "Xaltalilar", ["Yo'ldoshlilar", "Kloakalilar", "Hasharotxo'rlar"], "Xaltalilar bolasini xaltada ko'taradi."),
    O(3, "Sutemizuvchi homila onasi bilan qaysi organ orqali bog'lanadi? (bir so'z)", ["yo'ldosh", "yoldosh", "platsenta"], "Yo'ldosh orqali ovqat va kislorod."),
]

# ---------------------------------------------------------------- 8-SINF
Q["B8.6"] = [
    C(1, "Suyakning uzunasiga o'sishi qaysi qatlam hisobiga bo'ladi?", "Tog'ay (o'sish zonasi)", ["Suyak usti pardasi", "Ilik", "Kompakt modda"], "Naychasimon suyak uchida tog'ay."),
    C(1, "Suyakning eniga o'sishini ta'minlaydi?", "Suyak usti pardasi", ["Qizil ilik", "Sariq ilik", "G'ovak modda"], "Periost."),
    C(2, "Qon hosil bo'ladigan ilik?", "Qizil ilik", ["Sariq ilik", "Suyak usti pardasi", "Tog'ay"], "Qizil ilikda qon yaratiladi."),
    C(2, "Bo'g'imning harakatchanligini nima ta'minlaydi?", "Bo'g'im moyi va tog'ay", ["Sarig' ilik", "Mushak", "Teri"], "Ishqalanishni kamaytiradi."),
    C(2, "Odam skeletidagi suyaklar soni taxminan?", "206", ["106", "306", "406"], "Kattalarda 206 ta."),
    C(3, "Bo'yin umurtqalari soni?", "7", ["5", "12", "9"], "Umurtqa pog'onasi: 7 bo'yin, 12 ko'krak, 5 bel."),
    O(3, "Odamda ko'krak umurtqalari nechta? (raqam)", ["12", "o'n ikki"], "12 ta ko'krak umurtqasi."),
]

Q["B8.7"] = [
    C(1, "Oziq hazm bo'lishi qaysi a'zoda boshlanadi?", "Og'iz bo'shlig'ida", ["Oshqozonda", "O'n ikki barmoqli ichakda", "Qizilo'ngachda"], "so'lak amilazasi kraxmalni parchalaydi."),
    C(1, "Oshqozon shirasida qaysi kislota bor?", "Xlorid kislota", ["Sulfat kislota", "Sirka kislota", "Nitrat kislota"], "HCl."),
    C(2, "Jigar ajratadigan modda?", "O't suyuqligi", ["Insulin", "Pepsin", "Amilaza"], "O't yog'larni emulsiyalaydi."),
    C(2, "Oziq moddalar asosan qaysi ichakda so'riladi?", "Ingichka ichak", ["Yo'g'on ichak", "To'g'ri ichak", "Qizilo'ngach"], "Vorsinkalar orqali."),
    C(2, "Oqsilni parchalovchi oshqozon fermenti?", "Pepsin", ["Amilaza", "Lipaza", "Ptialin"], "Pepsin kislotali muhitda ishlaydi."),
    C(3, "Me'da osti bezi qaysi gormonni ishlab chiqaradi?", "Insulin", ["Adrenalin", "Tiroksin", "Gastrin"], "Insulin qand miqdorini pasaytiradi."),
    O(3, "Yo'g'on ichakda asosan qaysi modda so'riladi? (bir so'z)", ["suv"], "Yo'g'on ichakda suv so'riladi."),
]

Q["B8.8"] = [
    C(1, "Gaz almashinuvi o'pkaning qaysi qismida bo'ladi?", "Alveolalarda", ["Bronxlarda", "Traxeyada", "Hiqildoqda"], "Alveolalar devori yupqa."),
    C(1, "Nafas yo'llarining to'g'ri ketma-ketligi?", "Burun → halqum → hiqildoq → traxeya → bronx", ["Burun → bronx → traxeya", "Halqum → burun → bronx", "Traxeya → burun → bronx"], "Havo shu yo'l bilan o'tadi."),
    C(2, "Nafas olishda diafragma qanday holatda bo'ladi?", "Qisqaradi va pastga tushadi", ["Bo'shashadi va ko'tariladi", "O'zgarmaydi", "Yo'qoladi"], "Ko'krak qafasi kengayadi."),
    C(2, "Qonda kislorodni tashuvchi modda?", "Gemoglobin", ["Fibrinogen", "Albumin", "Insulin"], "Eritrositlardagi gemoglobin."),
    C(2, "Tinch holatda katta odam bir daqiqada necha marta nafas oladi?", "16–18 marta", ["5–6", "30–40", "60"], "O'rtacha 16–18."),
    C(3, "Hiqildoqdagi tovush hosil qiluvchi tuzilma?", "Ovoz boylamlari", ["Epiglottis", "Traxeya halqalari", "Bronxlar"], "Ovoz paychalari."),
    O(3, "O'pkani o'rab turuvchi parda nomini yozing (bir so'z).", ["plevra"], "Plevra."),
]

Q["B8.9"] = [
    C(1, "Odamning asosiy ayirish organi?", "Buyrak", ["Jigar", "Me'da osti bezi", "Yurak"], "Buyrak qonni filtrlaydi."),
    C(1, "Siydik hosil bo'ladigan buyrakning tuzilish birligi?", "Nefron", ["Neyron", "Alveola", "Vorsinka"], "Nefron — buyrak birligi."),
    C(2, "Siydik pufagidan tashqariga chiqaruvchi kanal?", "Siydik chiqarish kanali", ["Siydik yo'li", "Buyrak jomi", "Kapillyar"], "Uretra."),
    C(2, "Birlamchi siydik qayerda hosil bo'ladi?", "Buyrak kapsulasida (filtratsiya)", ["Siydik pufagida", "Jigarda", "O'pkada"], "Boumen–Shumlyanskiy kapsulasi."),
    C(2, "Siydik tarkibida odatda bo'lmaydigan modda?", "Glyukoza va oqsil", ["Mochevina", "Suv", "Tuzlar"], "Sog'lom odamda glyukoza va oqsil bo'lmaydi."),
    C(3, "Ikkilamchi siydik hosil bo'lishida nima sodir bo'ladi?", "Suv va kerakli moddalar qayta so'riladi", ["Qon filtrlanadi", "Siydik pufagi to'ladi", "Jigarda zararsizlanadi"], "Reabsorbsiya."),
    O(3, "Birlamchi siydik bir kecha-kunduzda taxminan necha litr hosil bo'ladi? (raqam)", ["150", "150 l", "150 litr"], "Ikkilamchi siydik esa taxminan 1,5 litr."),
]

Q["B8.10"] = [
    C(1, "Teri qatlamlari?", "Epidermis, dermis, teri osti yog' kletchatkasi", ["Faqat epidermis", "Epiteliy va suyak", "Dermis va mushak"], "Teri uch qatlamdan iborat."),
    C(1, "Terining pigment moddasi?", "Melanin", ["Keratin", "Kollagen", "Gemoglobin"], "Melanin rang beradi."),
    C(2, "Teri orqali tana haroratini boshqarishda qaysi bezlar qatnashadi?", "Ter bezlari", ["Yog' bezlari", "So'lak bezlari", "Qalqonsimon bez"], "Ter bug'lanib sovutadi."),
    C(2, "Quyosh nuri ta'sirida terida qaysi vitamin hosil bo'ladi?", "D vitamini", ["C vitamini", "A vitamini", "B₁ vitamini"], "D vitamini ultrabinafsha ta'sirida."),
    C(2, "Soch va tirnoq asosan qaysi oqsildan iborat?", "Keratin", ["Kollagen", "Albumin", "Gemoglobin"], "Keratin."),
    C(3, "Qaysi qatlamda qon tomirlar va retseptorlar joylashgan?", "Dermada", ["Epidermisda", "Teri osti yog'ida", "Shox qavatda"], "Derma — haqiqiy teri."),
    O(3, "Epidermisning eng yuza, o'lgan hujayralar qavati nomi? (shox ...)", ["shox qavat", "shox"], "Shox qavat."),
]

Q["B8.11"] = [
    C(1, "Ko'z yorug'lik nurini sezadigan qismi?", "To'r parda", ["Shox parda", "Qorachiq", "Rangdor parda"], "To'r pardada tayoqcha va kolbachalar."),
    C(1, "Kechasi ko'rishni ta'minlaydigan hujayralar?", "Tayoqchalar", ["Kolbachalar", "Neyronlar", "Pigmentlar"], "Tayoqchalar xira yorug'likni sezadi."),
    C(2, "Linza egriligini o'zgartirib, tasvirni to'r pardaga fokuslash?", "Akkomodatsiya", ["Adaptatsiya", "Refleks", "Assimilyatsiya"], "Akkomodatsiya."),
    C(2, "Eshitish retseptorlari joylashgan qism?", "Ichki quloqdagi chig'anoq", ["O'rta quloq", "Tashqi eshitish yo'li", "Eshitish nayi"], "Kortiy a'zosi."),
    C(2, "O'rta quloqdagi suyakchalar?", "Bolg'acha, sandon, uzangi", ["Jag', til, bosh", "Uzangi, ilik, tirsak", "Tirsak, bolg'a, pichoq"], "Uchta suyakcha."),
    C(3, "Yaqindan ko'ra olmaslik nima deb ataladi?", "Uzoqni ko'rish (gipermetropiya)", ["Miopiya", "Astigmatizm", "Daltonizm"], "Uzoqni ko'ruvchi odam yaqinni aniq ko'rmaydi."),
    O(3, "Ranglarni sezuvchi to'r parda hujayralari nomini yozing (bir so'z).", ["kolbachalar", "kolbacha"], "Kolbachalar."),
]

Q["B8.12"] = [
    C(1, "Immunitet nima?", "Organizmning kasallik qo'zg'atuvchilariga chidamliligi", ["Qon guruhi", "Suyak mustahkamligi", "Mushak kuchi"], "Himoya tizimi."),
    C(1, "Emlashning (vaksina) maqsadi?", "Sun'iy faol immunitet hosil qilish", ["Antibiotik berish", "Qon quyish", "Operatsiya"], "Vaksina antigenlar kiritadi."),
    C(2, "Antitelolarni ishlab chiqaradigan hujayralar?", "B-limfotsitlar (plazmatik)", ["Eritrositlar", "Trombotsitlar", "Neytrofillar"], "Plazmatik hujayralar antitelo yaratadi."),
    C(2, "Fagotsitoz nimani anglatadi?", "Leykotsitlarning mikroblarni yutishi", ["Qon ivishi", "Suv almashinuvi", "Gormon ishlab chiqarish"], "I. Mechnikov kashf etgan."),
    C(2, "Zardob (zilol) qaysi immunitetni beradi?", "Sun'iy passiv", ["Sun'iy faol", "Tabiiy faol", "Tug'ma"], "Tayyor antitelolar."),
    C(3, "OITS virusi qaysi hujayralarga hujum qiladi?", "T-xelper limfotsitlarga", ["Eritrositlarga", "Neyronlarga", "Mushak hujayralariga"], "CD4+ T-limfotsitlar."),
    O(3, "Fagotsitoz hodisasini kashf etgan olim familiyasini yozing.", ["Mechnikov", "Мечников", "Mechnikov I.I."], "I. I. Mechnikov."),
]

# ---------------------------------------------------------------- 9-SINF
Q["B9.5"] = [
    C(1, "Fotosintezning yorug'lik fazasi xloroplastning qaysi qismida boradi?", "Tilakoid membranalarida", ["Stromada", "Yadroda", "Sitoplazmada"], "Grana tilakoidlarida."),
    C(1, "Fotosintezning qorong'ilik fazasi qaerda boradi?", "Stromada", ["Tilakoidda", "Mitoxondriyada", "Ribosomada"], "Kalvin sikli stromada."),
    C(2, "Yorug'lik fazasida suv fotolizi natijasida nima ajraladi?", "Kislorod", ["Glyukoza", "CO₂", "Azot"], "H₂O → O₂ ↑."),
    C(2, "Yorug'lik fazasida energiya qaysi molekulalarda to'planadi?", "ATF va NADPH", ["ADF", "DNK", "RNK"], "Qorong'ilik fazasida ishlatiladi."),
    C(2, "Qorong'ilik fazasida CO₂ dan nima hosil bo'ladi?", "Glyukoza", ["Kislorod", "Suv", "ATF"], "Kalvin sikli."),
    C(3, "Fotosintezning yorug'lik fazasi uchun zarur pigment?", "Xlorofill", ["Gemoglobin", "Melanin", "Karotin faqat"], "Xlorofill a."),
    O(3, "Fotosintezda suvning yorug'lik ta'sirida parchalanishi nima deyiladi? (bir so'z)", ["fotoliz"], "Suv fotolizi."),
]

Q["B9.6"] = [
    C(1, "Transkripsiya nima?", "DNK dan RNK sintezlanishi", ["RNK dan oqsil", "DNK replikatsiyasi", "Glikoliz"], "DNK matritsasida RNK."),
    C(1, "Translyatsiya qayerda boradi?", "Ribosomada", ["Yadroda", "Mitoxondriyada faqat", "Golji apparatida"], "Oqsil sintezi ribosomada."),
    C(2, "DNK da qaysi azot asosi uchramaydi?", "Uratsil", ["Adenin", "Timin", "Sitozin"], "Uratsil faqat RNK da."),
    C(2, "Bitta aminokislotani kodlovchi nukleotidlar soni?", "3 (triplet)", ["1", "2", "4"], "Kodon uch nukleotid."),
    C(2, "Aminokislotalarni ribosomaga keltiruvchi RNK?", "tRNK", ["mRNK", "rRNK", "DNK"], "Transport RNK."),
    C(3, "DNK dagi A–T–G–C ketma-ligiga komplementar mRNK ketma-ketligi?", "U–A–C–G", ["T–A–C–G", "A–U–G–C", "U–T–C–G"], "A→U, T→A, G→C, C→G."),
    O(3, "mRNK da A–U–G kodon qaysi aminokislotani kodlaydi? (qisqa nom)", ["metionin", "Met", "met"], "AUG — start kodon, metionin."),
]

Q["B9.7"] = [
    C(1, "Ko'z uchun muhim vitamin?", "A vitamini", ["C vitamini", "D vitamini", "K vitamini"], "A yetishmasa shabko'rlik."),
    C(1, "Singa (sinqa) kasalligi qaysi vitamin yetishmovchiligidan?", "C vitamini", ["B₁", "D", "A"], "Askorbin kislota."),
    C(2, "Raxit kasalligi qaysi vitamin yetishmasligidan?", "D vitamini", ["C", "B₁₂", "E"], "D vitamini kalsiy almashinuvini boshqaradi."),
    C(2, "Yog'da eriydigan vitaminlar guruhi?", "A, D, E, K", ["B, C", "B₁, B₆", "C, PP"], "Yog'da eruvchi."),
    C(2, "Qon ivishida ishtirok etuvchi vitamin?", "K vitamini", ["A", "E", "D"], "Protrombin sintezi."),
    C(3, "B₁₂ vitamini yetishmasa qaysi kasallik rivojlanadi?", "Kamqonlik (zararli anemiya)", ["Raxit", "Singa", "Shabko'rlik"], "Eritrotsitlar yetilishi buziladi."),
    O(3, "Beriberi kasalligi qaysi B guruhi vitamini yetishmasligidan? (B va raqamni yozing)", ["B1", "B₁", "b1"], "Tiamin."),
]

Q["B9.8"] = [
    C(1, "Fermentlar kimyoviy tabiati bo'yicha asosan?", "Oqsillar", ["Yog'lar", "Uglevodlar", "Nuklein kislotalar"], "Biokatalizatorlar."),
    C(1, "Ferment ta'sir etadigan modda nima deb ataladi?", "Substrat", ["Mahsulot", "Katalizator", "Inhibitor"], "Substrat."),
    C(2, "Fermentlarning xususiyati?", "Substratga o'ta tanlab ta'sir qiladi", ["Har qanday reaksiyani tezlashtiradi", "Reaksiyada sarflanadi", "Haroratga bog'liq emas"], "Spetsifiklik."),
    C(2, "Oshqozon fermenti pepsin qaysi muhitda ishlaydi?", "Kuchli kislotali", ["Ishqoriy", "Neytral", "Hamma muhitda"], "pH ≈ 2."),
    C(2, "Yuqori haroratda ferment faolligi nima bo'ladi?", "Denaturatsiya tufayli yo'qoladi", ["Ortadi", "O'zgarmaydi", "Ikki baravar"], "Oqsil strukturasi buziladi."),
    C(3, "Kraxmalni maltozagacha parchalaydigan ferment?", "Amilaza", ["Pepsin", "Lipaza", "Tripsin"], "So'lak amilazasi."),
    O(3, "Yog'larni glitserin va yog' kislotalarigacha parchalovchi ferment nomini yozing (bir so'z).", ["lipaza"], "Lipaza."),
]

Q["B9.9"] = [
    C(1, "Mitoz natijasida bitta ona hujayradan nechta qiz hujayra hosil bo'ladi?", "2", ["4", "1", "8"], "Genetik jihatdan bir xil."),
    C(1, "Meyoz yakunida bitta ona hujayradan nechta hujayra hosil bo'ladi?", "4", ["2", "1", "8"], "Xromosoma soni ikki marta kamayadi."),
    C(2, "Mitozda xromosomalar ekvator tekisligida qaysi fazada joylashadi?", "Metafaza", ["Profaza", "Anafaza", "Telofaza"], "Metafazada ekvatorda."),
    C(2, "Krossingover qaysi jarayonda sodir bo'ladi?", "Meyoz I profazasi", ["Mitoz anafazasi", "Interfaza", "Meyoz II telofazasi"], "Gomologik xromosomalar almashinadi."),
    C(2, "Interfazaning S davrida nima sodir bo'ladi?", "DNK replikatsiyasi", ["Xromosomalar ajralishi", "Hujayra bo'linishi", "RNK parchalanishi"], "DNK ikki hissa ortadi."),
    C(3, "Odam somatik hujayrasida 46 xromosoma bo'lsa, gametada necha xromosoma bor?", "23", ["46", "92", "12"], "Gaploid to'plam."),
    O(3, "Odam tana hujayrasi mitozdan keyin qiz hujayrada necha xromosoma bo'ladi? (raqam)", ["46"], "Mitozda xromosoma soni saqlanadi."),
]

# ---------------------------------------------------------------- 10-SINF
Q["B10.5"] = [
    C(1, "Mendelning birinchi qonuni qanday ataladi?", "Birinchi avlod duragaylarining bir xilligi qonuni", ["Belgilarning ajralishi qonuni", "Mustaqil birikish qonuni", "Birikkan irsiylanish qonuni"], "F₁ bir xil."),
    C(1, "Aa × Aa chatishtirishda F₂ da fenotip bo'yicha nisbat?", "3:1", ["1:1", "1:2:1", "9:3:3:1"], "Mendelning ikkinchi qonuni."),
    C(2, "Aa × Aa chatishtirishda genotip bo'yicha nisbat?", "1:2:1", ["3:1", "1:1", "9:3:3:1"], "AA:Aa:aa."),
    C(2, "Digeterozigotani (AaBb) AaBb bilan chatishtirsak fenotip nisbati?", "9:3:3:1", ["3:1", "1:1:1:1", "1:2:1"], "Mustaqil birikish."),
    C(2, "Tahliliy chatishtirishda Aa × aa dan F₁ nisbat?", "1:1", ["3:1", "1:2:1", "9:3:3:1"], "Gametalar 1:1."),
    C(3, "AaBb × aabb dan hosil bo'ladigan genotip sinflari soni?", "4", ["2", "8", "16"], "AaBb, Aabb, aaBb, aabb."),
    O(3, "Aa × Aa chatishtirishda F₂ da retsessiv gomozigota ulushi qancha? (kasr yoki foiz)", ["1/4", "25%", "0,25", "0.25"], "aa — 1/4."),
]

Q["B10.6"] = [
    C(1, "Mutatsiya nima?", "Genotipning to'satdan o'zgarishi", ["Fenotipning vaqtincha o'zgarishi", "Qon guruhi", "Tashqi muhit ta'siri"], "Irsiy o'zgarish."),
    C(1, "Xromosomalar sonining o'zgarishi qaysi mutatsiya?", "Genom mutatsiya", ["Gen mutatsiyasi", "Xromosoma mutatsiyasi", "Modifikatsiya"], "Poliploidiya, anevloidiya."),
    C(2, "Daun sindromi qanday mutatsiya natijasi?", "21-juftlikda trisomiya", ["X-xromosoma yo'qligi", "Gen mutatsiyasi", "Poliploidiya"], "47 xromosoma."),
    C(2, "Irsiy bo'lmagan o'zgarish nima deb ataladi?", "Modifikatsiya", ["Mutatsiya", "Rekombinatsiya", "Krossingover"], "Fenotipik, me'yor chegarasida."),
    C(2, "Mutagen omillarga qaysi biri kiradi?", "Rentgen nurlari", ["Vitaminlar", "Suv", "Kislorod"], "Ionlashtiruvchi nurlar."),
    C(3, "Doimiy ravishda 1 juft nukleotid o'rnini bosuvchi mutatsiya qanday ataladi?", "Nuqtaviy mutatsiya", ["Delesiya", "Duplikatsiya", "Inversiya"], "Gen mutatsiyasi turi."),
    O(3, "Shaxarcha (Shereshevskiy–Terner) sindromida kariotip (xromosomalar soni)? (raqam)", ["45"], "XO — 45 xromosoma."),
]

Q["B10.7"] = [
    C(1, "Seleksiya nima?", "Yangi nav, zot va shtammlar yaratish fani", ["Qazilma o'rganish", "Hujayra tuzilishi", "Ekologiya bo'limi"], "Amaliy biologiya sohasi."),
    C(1, "Seleksiya markazlari nazariyasini kim yaratgan?", "N. I. Vavilov", ["Mendel", "Darvin", "Lamark"], "Vavilov."),
    C(2, "Poliploid navlarni olishda qaysi modda ishlatiladi?", "Kolxitsin", ["Penitsillin", "Insulin", "Gibberellin"], "Bo'linish urchug'ini buzadi."),
    C(2, "Geterozis effektini olish uchun qanday chatishtirish qo'llanadi?", "Qarindosh bo'lmagan liniyalarni chatishtirish", ["Faqat o'z-o'zini changlatish", "Yaqin qarindoshlarni doimiy chatishtirish", "Vegetativ ko'paytirish"], "Geterozis: F₁ ning hayotchanligi ortadi."),
    C(2, "Geterozis hodisasi nima?", "F₁ duragaylarning ota-onadan kuchli bo'lishi", ["Bolalarning kasalligi", "Nasl bermaslik", "Jinsning o'zgarishi"], "Duragay kuch."),
    C(3, "Mol zotlarini yaxshilashda sun'iy urug'lantirish nima beradi?", "Bitta zotdor buqadan ko'p nasl olish", ["Mutatsiyani oshirish", "Nasl bermaslik", "Ovqat hazmi"], "Zotdor naslni tarqatish."),
    O(3, "Madaniy o'simliklar kelib chiqish markazlari ta'limoti muallifining familiyasini yozing.", ["Vavilov", "Вавилов"], "N. I. Vavilov."),
]

Q["B10.8"] = [
    C(1, "Ekotizim nima?", "Tirik organizmlar va ularning yashash muhiti birligi", ["Faqat o'simliklar", "Faqat hayvonlar", "Faqat tuproq"], "Biogeotsenoz."),
    C(1, "Ozuqa zanjirida ishlab chiqaruvchilar kimlar?", "Yashil o'simliklar", ["O't yeyuvchilar", "Yirtqichlar", "Bakteriyalar"], "Produtsentlar."),
    C(2, "Konsumentlarga kiradi?", "Hayvonlar", ["Yashil o'simliklar", "Tuproq bakteriyalari", "Zamburug'lar emas"], "Iste'molchilar."),
    C(2, "Reduktsentlar (parchalovchilar) vazifasi?", "Organik moddalarni mineral moddalargacha parchalash", ["Fotosintez", "Ov qilish", "O'simlik changlatish"], "Bakteriya, zamburug'."),
    C(2, "Ekologik piramida qoidasiga ko'ra har bir keyingi trofik darajada energiya qancha qoladi?", "Taxminan 10%", ["50%", "90%", "100%"], "10% qoidasi."),
    C(3, "Quyidagilardan qaysi biri ozuqa zanjiri to'g'ri?", "O'simlik → kemiruvchi → ilon → burgut", ["Burgut → ilon → kemiruvchi → o'simlik", "Ilon → o'simlik → burgut", "Kemiruvchi → burgut → o'simlik"], "Yo'nalish energiya oqimi."),
    O(3, "Ozuqa zanjirida organik modda yaratuvchi organizmlarning ilmiy nomini yozing (bir so'z).", ["produtsent", "produtsentlar", "avtotrof", "avtotroflar"], "Produtsentlar."),
]

Q["B10.9"] = [
    C(1, "Biosfera haqidagi ta'limot muallifi?", "V. I. Vernadskiy", ["Ch. Darvin", "Mendel", "Lamark"], "Biosfera ta'limoti."),
    C(1, "Biosferaning tirik moddasi?", "Barcha tirik organizmlar yig'indisi", ["Faqat o'simliklar", "Faqat odamlar", "Suv va havo"], "Tirik modda."),
    C(2, "Atmosferada eng ko'p gaz?", "Azot (≈78%)", ["Kislorod", "Karbonat angidrid", "Argon"], "N₂."),
    C(2, "Havodagi karbonat angidrid miqdori ortishi nimaga olib keladi?", "Issiqxona effektiga", ["Ozon qatlami kengayishiga", "Kislorod ortishiga", "Muz davrining boshlanishiga"], "Global isish."),
    C(2, "Ozon qatlami nimadan himoya qiladi?", "Ultrabinafsha nurlardan", ["Shamoldan", "Yomg'irdan", "Radioto'lqinlardan"], "Stratosferada."),
    C(3, "Biosferadagi moddalar aylanishi harakatlantiruvchi kuchi?", "Quyosh energiyasi va tirik organizmlar", ["Faqat shamol", "Faqat vulqonlar", "Faqat yer osti suvi"], "Biogeokimyoviy sikllar."),
    O(3, "Inson faoliyati ta'sirida paydo bo'lgan biosfera bosqichi nomi (Vernadskiy): \"... sferasi\" (bir so'z).", ["noosfera", "Noosfera"], "Noosfera — aql sferasi."),
]
