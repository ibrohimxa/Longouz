"""v247: BIOLOGIYA va ONA TILI-ADABIYOT — kam savolli mavzularga yangi savollar (DTM 2026 / sertifikat uslubi)."""
from __future__ import annotations

from ._dsl import C

BIO: dict[str, list] = {
    "B6.8": [
        C(1, "Olcha mevasi qanday meva turiga kiradi?", "Danakli meva", ["Ko'sak", "Dukkak", "Don"], "Olcha, o'rik, shaftoli — danakli mevalar."),
        C(2, "Qaysi o'simlikning urug'i shamol yordamida tarqaladi?", "Qoqio't", ["Olcha", "Yong'oq", "Qovun"], "Qoqio't urug'ida parashyutsimon uchma bor."),
        C(2, "Bug'doy mevasi qanday ataladi?", "Don", ["Rezavor", "Ko'sak", "Danak"], "Boshoqdoshlar mevasi — don."),
    ],
    "B6.9": [
        C(2, "Bargidan ko'payadigan xona o'simligi?", "Begoniya", ["Kartoshka", "Piyoz", "Qulupnay"], "Begoniya, senpoliya barg qalamchasidan ko'payadi."),
        C(2, "Kartoshka tuganagi qaysi a'zoning shakli o'zgargani?", "Yer osti poyasi", ["Ildiz", "Barg", "Meva"], "Tuganakda kurtaklar (ko'zchalar) bor — bu poya belgisi."),
        C(3, "Hujayra va to'qimalardan sun'iy muhitda yangi o'simlik o'stirish usuli?", "To'qima kulturasi (mikroklonal ko'paytirish)", ["Payvandlash", "Parxish", "Urug'dan ekish"], "Bir hujayradan butun o'simlik tiklanadi."),
    ],
    "B6.10": [
        C(1, "Suv o'ti hujayrasida fotosintez qiladigan organoid?", "Xromatofor (xloroplast)", ["Mitoxondriya", "Yadro", "Vakuola"], "Suv o'tlarida xloroplast xromatofor deb ham ataladi."),
        C(2, "Xlamidomonadaning harakatlanish organoidi?", "Xivchinlar", ["Soxta oyoqlar", "Kiprikchalar", "Mo'ylovlar"], "Ikkita xivchin yordamida suzadi."),
        C(2, "Laminariyadan qaysi muhim element olinadi?", "Yod", ["Temir", "Kalsiy", "Natriy"], "Dengiz karami yodga boy."),
    ],
    "B6.11": [
        C(1, "Moxlar, qirqbo'g'imlar va paporotniklar qanday ko'payadi?", "Sporalar yordamida", ["Urug' yordamida", "Faqat qalamcha bilan", "Meva yordamida"], "Ular sporali o'simliklar."),
        C(2, "Toshko'mir qatlamlari qaysi qadimgi o'simliklar qoldiqlaridan hosil bo'lgan?", "Daraxtsimon paporotnik, qirqbo'g'im va plaunlardan", ["Gulli o'simliklardan", "Suv o'tlaridan", "Moxlardan"], "Toshko'mir davrida ular ulkan o'rmonlar hosil qilgan."),
        C(2, "Kukushkin zig'iri (politrix) qaysi guruhga kiradi?", "Moxlar", ["Paporotniklar", "Qirqbo'g'imlar", "Suv o'tlari"], "Yashil mox."),
    ],
    "B6.12": [
        C(2, "Qaysi ignabargli daraxt qishda bargini to'kadi?", "Tilog'och", ["Qarag'ay", "Archa", "Pixta"], "Tilog'och — ignabarglarini to'kadigan ignabargli."),
        C(2, "Qarag'ayda changlanishdan urug'lanishgacha taxminan qancha vaqt o'tadi?", "Bir yilga yaqin", ["Bir kun", "Bir hafta", "10 yil"], "Urug' ikkinchi yili yetiladi."),
        C(1, "Yalang'ochurug'lilar qaysi o'simliklar guruhiga mansub?", "Yuksak o'simliklar", ["Tuban o'simliklar", "Zamburug'lar", "Bakteriyalar"], "To'qima va organlari rivojlangan."),
    ],
    "B6.13": [
        C(2, "Bargdagi fotosintez qiluvchi asosiy to'qima?", "Ustunsimon (asosiy) to'qima", ["Po'kak", "Yog'ochlik", "Qoplovchi to'qima"], "Hujayralarida xloroplastlar ko'p."),
        C(2, "Fotosintezda hosil bo'lgan glyukoza o'simlikda qanday zaxira moddaga aylanadi?", "Kraxmal", ["Oqsil", "Yog'", "Osh tuzi"], "Kraxmal yod bilan ko'karadi."),
        C(3, "O'simliklar «buzilgan» havoni tozalashini tajribada ko'rsatgan ingliz olimi?", "J. Pristli", ["Ch. Darvin", "G. Mendel", "R. Guk"], "Pristli 1771-yilda yalpiz va sichqon bilan tajriba o'tkazgan."),
    ],
    "B6.14": [
        C(1, "O'simlikning qaysi qismi eng ko'p transpiratsiya qiladi?", "Barglar", ["Ildiz", "Gul", "Urug'"], "Og'izchalar asosan bargda joylashgan."),
        C(2, "O'simlik nafas olganda organik moddalar parchalanib nima ajraladi?", "Energiya", ["Kislorod", "Xlorofill", "Kraxmal"], "Energiya hayotiy jarayonlarga sarflanadi."),
        C(3, "Cho'l o'simliklarida transpiratsiyani kamaytiruvchi moslanish?", "Barglarning tikanga aylanishi", ["Barglarning juda yirik bo'lishi", "Og'izchalar sonining ortishi", "Ildizning qisqa bo'lishi"], "Bug'latuvchi yuza kamayadi."),
    ],
    "B6.15": [
        C(1, "Ildiz uchini shikastlanishdan himoya qiluvchi tuzilma?", "Ildiz qini", ["Ildiz tukchalari", "Kambiy", "Po'kak"], "Ildiz qini o'sish nuqtasini yopib turadi."),
        C(2, "Azotli o'g'it yetishmasa barglar qanday bo'ladi?", "Mayda va och yashil-sarg'ish", ["To'q yashil", "Qizil", "Yirik va yaltiroq"], "Xlorofill sintezi kamayadi."),
        C(2, "Ildizdan bargga suv va mineral moddalar qaysi to'qima orqali ko'tariladi?", "Yog'ochlik (ksilema) naylari", ["Lub (floema)", "Po'kak", "Kambiy"], "Organik moddalar esa lub orqali harakatlanadi."),
    ],
    "B7.7": [
        C(1, "Meduzalar qaysi tipga kiradi?", "Bo'shliqichlilar", ["Mollyuskalar", "Bo'g'imoyoqlilar", "Halqali chuvalchanglar"], "Nashtarli hujayralari bor."),
        C(2, "Gidra qayerda yashaydi?", "Chuchuk suv havzalarida", ["Dengizda", "Tuproqda", "Boshqa hayvonlar ichida"], "Ko'l va hovuzlarda suv o'simliklariga yopishib yashaydi."),
        C(2, "Marjon riflari qaysi hayvonlar faoliyatidan hosil bo'ladi?", "Marjon poliplari", ["Mollyuskalar", "Baliqlar", "Dengiz yulduzlari"], "Ohakli skeletlar to'planadi."),
    ],
    "B7.8": [
        C(2, "Mollyuskalarning qaysi sinfi eng yuksak rivojlangan nerv tizimiga ega?", "Boshoyoqlilar", ["Qorinoyoqlilar", "Ikki pallalilar", "Barchasi bir xil"], "Kalmar va sakkizoyoqlarning miyasi rivojlangan."),
        C(2, "Ikki pallali mollyuskalar qanday oziqlanadi?", "Suvni filtrlab", ["Yirtqichlik qilib", "O'simlik bargini kemirib", "Parazitlik qilib"], "Suvni filtrlab mayda organizmlarni ushlaydi."),
        C(1, "Sakkizoyoq qaysi mollyuskalar sinfiga kiradi?", "Boshoyoqlilar", ["Qorinoyoqlilar", "Ikki pallalilar", "Qisqichbaqasimonlar"], "Oyog'i paypaslagichlarga aylangan."),
    ],
    "B7.9": [
        C(2, "Yomg'ir chuvalchangi qanday ko'payadi?", "Germafrodit, chetdan urug'lanadi", ["Faqat bo'linib", "Ayri jinsli, ichki urug'lanadi", "Kurtaklanib"], "Ikki individ urug' hujayralari bilan almashadi."),
        C(2, "Tibbiyotda qon ivishini kamaytirish uchun qo'llanadigan halqali chuvalchang?", "Tibbiy zuluk", ["Nereida", "Yomg'ir chuvalchangi", "Askarida"], "So'lagida girudin moddasi bor."),
        C(3, "Halqali chuvalchanglarda qanday tana bo'shlig'i bor?", "Ikkilamchi (selom)", ["Birlamchi", "Tana bo'shlig'i yo'q", "Faqat ichak bo'shlig'i"], "Selom epiteliy bilan qoplangan."),
    ],
    "B7.10": [
        C(2, "Chala o'zgarish bilan rivojlanuvchi hasharot?", "Chigirtka", ["Kapalak", "Asalari", "Qo'ng'iz"], "Tuxum → lichinka → voyaga yetgan hasharot."),
        C(2, "Hasharotlarning ayirish a'zolari?", "Malpigi naychalari", ["Nefridiylar", "Buyraklar", "Yashil bezlar"], "Ichakka ochiladi."),
        C(1, "Ipak qurti qaysi turkumga kiradi?", "Tangachaqanotlilar (kapalaklar)", ["Qattiqqanotlilar", "Pardaqanotlilar", "To'g'riqanotlilar"], "Tut ipak qurti — kapalak lichinkasi."),
    ],
    "B7.11": [
        C(2, "Akulalar skeleti qanday to'qimadan iborat?", "Tog'ay", ["Suyak", "Xitin", "Ohak"], "Akula va skatlar — tog'ayli baliqlar."),
        C(2, "Ko'pchilik baliqlarda urug'lanish qanday?", "Tashqi", ["Ichki", "Urug'lanmaydi", "Faqat partenogenez"], "Uvildiriq suvda urug'lanadi."),
        C(3, "Baliq yuragi orqali qanday qon oqadi?", "Venoz qon", ["Arterial qon", "Aralash qon", "Qon oqmaydi"], "Yurak venoz qonni jabralarga haydaydi."),
    ],
    "B7.12": [
        C(2, "Amfibiyalar terisi qanday?", "Yalang'och, shilliq, nafas olishda qatnashadi", ["Shox tangachali", "Jun bilan qoplangan", "Pat bilan qoplangan"], "Teri orqali ham gaz almashinadi."),
        C(1, "Kaltakesaklar qaysi sinfga kiradi?", "Reptiliyalar (sudralib yuruvchilar)", ["Amfibiyalar", "Sutemizuvchilar", "Baliqlar"], "Terisi quruq, shox tangachali."),
        C(2, "O'zbekiston cho'llarida yashovchi eng yirik kaltakesak?", "Kulrang echkemar (varan)", ["Gekkon", "Yashil kaltakesak", "Sariq ilon"], "Uzunligi 1,5 m gacha yetadi."),
    ],
    "B7.13": [
        C(2, "Qushlarda qo'sh nafas olishni ta'minlovchi tuzilma?", "Havo xaltalari", ["Jabralar", "Traxeyalar", "Teri"], "Havo o'pkadan nafas olishda ham, chiqarishda ham o'tadi."),
        C(1, "Qushlar tanasi nima bilan qoplangan?", "Patlar", ["Jun", "Tangacha", "Yalang'och teri"], "Pat — teri hosilasi."),
        C(2, "Uchish mushaklari birikadigan to'sh suyagi o'simtasi?", "To'sh toji (kil)", ["Kurak", "Umurtqa", "Chanoq"], "Uchuvchi qushlarda yaxshi rivojlangan."),
    ],
    "B7.14": [
        C(1, "Sutemizuvchilarda ko'krak va qorin bo'shlig'ini ajratuvchi mushak?", "Diafragma", ["Plevra", "Qovurg'alar", "Qorin pressi"], "Nafas olishda qatnashadi."),
        C(2, "Ko'rshapalak qaysi turkumga kiradi?", "Qo'lqanotlilar", ["Kemiruvchilar", "Hasharotxo'rlar", "Yirtqichlar"], "Uchishga moslashgan yagona sutemizuvchilar."),
        C(2, "Kemiruvchilar tishlariga xos belgi?", "Kurak tishlari umrbod o'sadi", ["Qoziq tishlari yirik", "Tishlari yo'q", "Barcha tishlari bir xil"], "Doimiy kemirish bilan yeyilib turadi."),
    ],
    "B8.6": [
        C(2, "Bosh suyagida harakatchan birikkan yagona suyak?", "Pastki jag'", ["Peshona", "Tepa", "Ensa"], "Chakka-pastki jag' bo'g'imi orqali."),
        C(2, "Suyakka qattiqlik beruvchi anorganik moddalar asosan?", "Kalsiy tuzlari", ["Oqsillar", "Yog'lar", "Glyukoza"], "Organik moddalar esa egiluvchanlik beradi."),
        C(1, "Son suyagi qanday suyak turiga kiradi?", "Naysimon (uzun)", ["Yassi", "G'ovak (kalta)", "Aralash"], "Odamning eng uzun suyagi."),
    ],
    "B8.7": [
        C(2, "So'lakdagi kraxmalni parchalovchi ferment?", "Amilaza (ptialin)", ["Pepsin", "Lipaza", "Tripsin"], "Og'izda kraxmal maltozagacha parchalana boshlaydi."),
        C(2, "O't suyuqligi yog'larga qanday ta'sir qiladi?", "Ularni emulsiyalaydi (mayda tomchilarga ajratadi)", ["Ularni oqsilga aylantiradi", "Ularni so'rib oladi", "Ta'sir qilmaydi"], "Lipaza ishini yengillashtiradi."),
        C(2, "Ingichka ichakda so'rish yuzasini oshiruvchi tuzilmalar?", "Vorsinkalar (so'rg'ichlar)", ["Alveolalar", "Nefronlar", "Neyronlar"], "Ichak devoridagi barmoqsimon o'simtalar."),
    ],
    "B8.8": [
        C(2, "Nafas markazi bosh miyaning qaysi qismida joylashgan?", "Uzunchoq miya", ["Miyacha", "Katta yarim sharlar", "O'rta miya"], "Qondagi CO₂ miqdoriga javob beradi."),
        C(2, "Chiqarilgan havoda qaysi gaz miqdori nafasga olingan havodagidan ko'p?", "Karbonat angidrid", ["Kislorod", "Ozon", "Vodorod"], "Taxminan 0,03% dan 4% gacha ortadi."),
        C(2, "Hiqildoq usti tog'ayi qanday vazifani bajaradi?", "Yutishda hiqildoqqa ovqat tushishidan saqlaydi", ["Tovush hosil qiladi", "Havoni isitadi", "Gaz almashinuvini ta'minlaydi"], "Yutish paytida hiqildoq kirish qismini yopadi."),
    ],
    "B8.9": [
        C(2, "Nefron kapsulasidagi kapillyarlar chigali nima deyiladi?", "Koptokcha (glomerula)", ["Alveola", "Vorsinka", "Sinaps"], "Unda qon plazmasi filtrlanadi."),
        C(3, "Buyrakda suvning qayta so'rilishini kuchaytiruvchi gormon?", "Antidiuretik gormon (vazopressin)", ["Insulin", "Adrenalin", "Tiroksin"], "Gipofiz orqa bo'lagidan ajraladi."),
        C(1, "Odamda nechta buyrak bor?", "2", ["1", "3", "4"], "Bel sohasida, umurtqa pog'onasining ikki yonida."),
    ],
    "B8.10": [
        C(2, "Issiq havoda teri qon tomirlari qanday o'zgaradi?", "Kengayadi", ["Torayadi", "O'zgarmaydi", "Yopiladi"], "Ko'proq issiqlik tashqariga beriladi."),
        C(2, "Terining yog' bezlari vazifasi?", "Teri va sochni yumshatib, himoya qiladi", ["Ter ajratadi", "Qon hosil qiladi", "A vitaminini hosil qiladi"], "Yog' terini qurishdan saqlaydi."),
        C(1, "Teri qanday asosiy vazifani bajaradi?", "Organizmni tashqi ta'sirlardan himoya qiladi", ["Ovqat hazm qiladi", "Qon hosil qiladi", "Gormonlarni ishlab chiqaradi"], "Himoya, termoregulyatsiya, ayirish va sezish vazifalari."),
    ],
    "B8.11": [
        C(1, "Ko'zning rangini belgilovchi qismi?", "Rangdor parda", ["Shox parda", "To'r parda", "Gavhar"], "Rangdor parda markazida qorachiq joylashgan."),
        C(2, "Muvozanat organi qayerda joylashgan?", "Ichki quloqda (vestibulyar apparat)", ["Tashqi quloqda", "O'rta quloqda", "Burunda"], "Yarim doira kanallar va dahlizda."),
        C(2, "Uzoqni yomon, yaqinni yaxshi ko'rish qanday ataladi?", "Yaqindan ko'rish (miopiya)", ["Uzoqdan ko'rish", "Astigmatizm", "Daltonizm"], "Tasvir to'r parda oldida hosil bo'ladi; botiq linzali ko'zoynak tuzatadi."),
    ],
    "B8.12": [
        C(2, "Chechakka qarshi emlashni birinchi qo'llagan olim?", "E. Jenner", ["L. Paster", "I. Mechnikov", "R. Kox"], "1796-yilda sigir chechagi bilan emlagan."),
        C(2, "Kasallikni o'tkazgandan keyin hosil bo'ladigan immunitet?", "Tabiiy faol", ["Sun'iy passiv", "Tabiiy passiv", "Sun'iy faol"], "Organizm antitelolarni o'zi ishlab chiqaradi."),
        C(3, "Onadan homilaga yo'ldosh orqali o'tgan antitelolar beradigan immunitet?", "Tabiiy passiv", ["Tabiiy faol", "Sun'iy faol", "Sun'iy passiv"], "Tayyor antitelolar onadan olinadi."),
    ],
    "B9.5": [
        C(2, "Fotosintez qorong'ilik fazasi reaksiyalari majmuasi kimning nomi bilan ataladi?", "Kalvin sikli", ["Krebs sikli", "Mendel sikli", "Karno sikli"], "M. Kalvin ochgan."),
        C(2, "Fotosintezda ajraladigan kislorod qaysi moddadan hosil bo'ladi?", "Suvdan", ["CO₂ dan", "Glyukozadan", "Xlorofilldan"], "Suv fotolizi natijasida."),
        C(3, "Qorong'ilik fazasida CO₂ ni biriktiruvchi ferment?", "Rubisko (RuBF-karboksilaza)", ["Amilaza", "ATF-sintaza", "Pepsin"], "Yer yuzidagi eng ko'p tarqalgan oqsil."),
    ],
    "B9.7": [
        C(1, "Suvda eriydigan vitamin?", "C vitamini", ["A vitamini", "D vitamini", "E vitamini"], "B guruhi va C vitamini suvda eriydi."),
        C(2, "Organizmda vitamin yetishmasligidan kelib chiqadigan kasallik umumiy holda qanday ataladi?", "Avitaminoz", ["Gipervitaminoz", "Allergiya", "Mutatsiya"], "Ortiqchaligi — gipervitaminoz."),
    ],
    "B9.8": [
        C(2, "Ferment va substrat «qulf va kalit» kabi mos kelishi g'oyasi muallifi?", "E. Fisher", ["L. Paster", "Ch. Darvin", "G. Mendel"], "1894-yilda taklif etilgan."),
        C(1, "Odam fermentlarining ko'pchiligi uchun optimal harorat?", "Taxminan 37 °C", ["0 °C", "70 °C", "100 °C"], "Tana harorati."),
        C(2, "Katalaza fermenti qaysi moddani parchalaydi?", "Vodorod peroksid", ["Kraxmal", "Oqsil", "Yog'"], "H₂O₂ → H₂O + O₂."),
    ],
    "B9.9": [
        C(2, "Mitozning qaysi fazasida xromatidalar qutblarga tarqaladi?", "Anafaza", ["Profaza", "Metafaza", "Telofaza"], "Xromatidalar bir-biridan ajraladi."),
        C(2, "Meyozning biologik ahamiyati?", "Gametalarda xromosomalar sonini ikki baravar kamaytiradi", ["Xromosomalar sonini oshiradi", "Faqat o'sishni ta'minlaydi", "Mutatsiyalarni to'xtatadi"], "Urug'lanishda diploid to'plam tiklanadi."),
        C(3, "Hayvon hujayrasida bo'linish urchug'i qaysi organoid ishtirokida hosil bo'ladi?", "Hujayra markazi (sentriolalar)", ["Ribosoma", "Lizosoma", "Golji apparati"], "Sentriolalar qutblarga tarqaladi."),
    ],
    "B10.6": [
        C(2, "Xromosoma bo'lagining yo'qolishi qanday mutatsiya?", "Deletsiya (xromosom mutatsiya)", ["Poliploidiya", "Gen mutatsiya", "Modifikatsiya"], "Xromosoma tuzilishi o'zgaradi."),
        C(2, "Belgining muhit ta'sirida o'zgarish chegarasi nima deyiladi?", "Reaksiya normasi", ["Genotip", "Mutagen", "Kariotip"], "Reaksiya normasi genotip bilan belgilanadi."),
        C(2, "Poliploidiya nima?", "Xromosomalar to'plamining karrali ortishi", ["Bitta genning o'zgarishi", "Xromosoma bo'lagining yo'qolishi", "Faqat fenotipning o'zgarishi"], "Masalan, triploid, tetraploid o'simliklar."),
    ],
    "B10.7": [
        C(3, "Karam va turp duragayida nasl bermaslikni poliploidiya yordamida birinchi yenggan olim?", "G. D. Karpechenko", ["N. I. Vavilov", "I. V. Michurin", "G. Mendel"], "1924-yilda serhosil duragay olgan."),
        C(2, "Hayvonlar seleksiyasida qarindosh organizmlarni chatishtirish nima deb ataladi?", "Inbriding", ["Autbriding", "Geterozis", "Mutagenez"], "Gomozigotalikni oshiradi."),
        C(2, "Mikroorganizmlar seleksiyasida ko'p qo'llanadigan usul?", "Sun'iy mutagenez va tanlash", ["Faqat duragaylash", "Payvandlash", "Parxish"], "Masalan, antibiotik ishlab chiqaruvchi zamburug' shtammlari."),
    ],
    "B10.9": [
        C(2, "Biosferaning yuqori chegarasi nima bilan belgilanadi?", "Ozon qatlami (taxminan 20–25 km)", ["Bulutlar (1 km)", "Tog' cho'qqilari", "Kosmos (1000 km)"], "Ozon qatlamidan yuqorida UB nurlar hayotga to'sqinlik qiladi."),
        C(3, "Vernadskiy bo'yicha tirik organizmlar ishtirokida hosil bo'lgan jonsiz modda (tuproq, il)?", "Biokos modda", ["Inert modda", "Tirik modda", "Radioaktiv modda"], "Tirik va jonsiz tabiat birgalikda hosil qiladi."),
        C(2, "Biosferada CO₂ ni o'zlashtiruvchi asosiy organizmlar?", "Fotosintezlovchi organizmlar", ["Faqat hayvonlar", "Faqat zamburug'lar", "Vulqonlar"], "O'simliklar, suv o'tlari, sianobakteriyalar."),
    ],
}

NATIVE: dict[str, list] = {
    "N5.1": [
        C(2, "Qaysi juftlikda «yuz» so'zi ko'p ma'noli so'z sifatida (asl va ko'chma ma'noda) qo'llangan?", "odamning yuzi — stolning yuzi", ["yuz (son) — yuz (bet)", "yuzta — yuzlab", "yuzma-yuz — yuzlamoq"], "Yuz (bet) va stol yuzi — bir so'zning ma'nolari; yuz (son) esa omonim."),
        C(1, "Ko'p ma'noli so'zning dastlabki, asosiy ma'nosi qanday ataladi?", "Bosh (asl) ma'no", ["Ko'chma ma'no", "Grammatik ma'no", "Omonim ma'no"], "Boshqa ma'nolar undan kelib chiqadi."),
    ],
    "N5.2": [
        C(2, "«Choynak qaynadi» gapida qanday ma'no ko'chishi bor?", "Metonimiya", ["Metafora", "Sinekdoxa", "Vazifadoshlik"], "Choynak ichidagi suv nazarda tutilgan — bog'liqlik asosida ko'chish."),
        C(2, "«Uyda besh jon bor» gapida qanday ma'no ko'chishi bor?", "Sinekdoxa", ["Metafora", "Metonimiya", "Vazifadoshlik"], "Qism (jon) orqali butun (odam) ifodalangan."),
    ],
    "N5.3": [
        C(1, "«Yoz» (fasl) va «yoz» (yozmoq fe'li) so'zlari qanday hodisa?", "Omonimlar", ["Sinonimlar", "Antonimlar", "Paronimlar"], "Shakli bir xil, ma'nolari bog'liq emas."),
        C(2, "Omonimlar ko'p ma'noli so'zlardan nimasi bilan farq qiladi?", "Ma'nolari o'rtasida bog'liqlik yo'q", ["Yozilishi farqli", "Talaffuzi farqli", "Faqat bitta ma'noga ega"], "Ko'p ma'noli so'zda ma'nolar bir-biridan kelib chiqadi."),
    ],
    "N5.5": [
        C(1, "«Asr» va «asir» so'zlari qanday so'zlar?", "Paronimlar", ["Omonimlar", "Sinonimlar", "Antonimlar"], "Talaffuzi yaqin, ma'nosi farqli."),
        C(2, "Gapni to'ldiring: «Urushda … tushgan askar uyiga qaytdi.»", "asir", ["asr", "asar", "asl"], "asir — tutqun."),
    ],
    "N5.6": [
        C(2, "Qaysi so'z rus tili orqali kirgan baynalmilal so'z?", "gazeta", ["daraxt", "kitob", "bola"], "gazeta — baynalmilal so'z; daraxt — forscha, kitob — arabcha, bola — o'z qatlam."),
        C(2, "«Daraxt» so'zi qaysi tildan o'zlashgan?", "Fors-tojik", ["Arab", "Rus", "Mo'g'ul"], "Fors-tojik qatlamiga oid."),
    ],
    "N5.7": [
        C(2, "«Kompyuter», «internet» so'zlari tilga endi kirgan paytda qanday so'z hisoblangan?", "Neologizm", ["Arxaizm", "Istorizm", "Evfemizm"], "Yangi tushuncha bilan birga kirgan so'z."),
        C(2, "«Qalqon», «sovut» so'zlari qaysi guruhga kiradi?", "Istorizmlar", ["Neologizmlar", "Evfemizmlar", "Dialektizmlar"], "Predmetning o'zi iste'moldan chiqqan."),
    ],
    "N5.8": [
        C(2, "«Qulog'iga lag'mon ilmoq» iborasining ma'nosi?", "aldamoq", ["ovqatlantirmoq", "maqtamoq", "tinglamoq"], "Yolg'on gap bilan ishontirmoq."),
        C(2, "«Tarvuzi qo'ltig'idan tushdi» iborasining ma'nosi?", "umidi puchga chiqib, ruhi tushdi", ["juda xursand bo'ldi", "boyib ketdi", "ishni tez bitirdi"], "Kutilgan narsa bo'lmay, hafsalasi pir bo'ldi."),
    ],
    "N5.9": [
        C(1, "Qisqa kulgili hikoyalar — latifalar qaysi qahramon bilan mashhur?", "Nasriddin Afandi", ["Alpomish", "Go'ro'g'li", "Barchin"], "Afandi latifalari."),
        C(2, "Qo'shiq, lapar, yor-yor — folklorning qaysi turiga kiradi?", "Lirik tur", ["Epik tur", "Dramatik tur", "Maqollar"], "His-tuyg'uni ifodalovchi qo'shiqlar."),
    ],
    "N6.1": [
        C(2, "«O'» unlisi qanday tasniflanadi?", "Lablangan, til orqa, o'rta keng", ["Lablanmagan, til oldi, tor", "Lablanmagan, til orqa, keng", "Lablangan, til oldi, tor"], "o' — orqa qator, o'rta keng, lablangan unli."),
        C(1, "O'zbek tilida so'zdagi bo'g'inlar soni nimaning soniga teng?", "Unli tovushlar soniga", ["Undosh tovushlar soniga", "Harflar soniga", "Qo'shimchalar soniga"], "Har bir bo'g'inda bitta unli bor."),
    ],
    "N6.2": [
        C(1, "O'zbek lotin alifbosida nechta harf bor?", "29", ["26", "33", "35"], "26 ta harf va sh, ch, ng harf birikmalari; tutuq belgisi alohida."),
        C(2, "«Sh» va «ch» qanday ifodalanadi?", "Ikki harf birikmasi bilan, lekin bitta tovushni bildiradi", ["Bitta maxsus harf bilan", "Tutuq belgisi bilan", "Uch harf bilan"], "Harf birikmasi bitta undoshni bildiradi."),
    ],
    "N6.3": [
        C(2, "«O'rin + i → o'rni» shaklida qanday fonetik hodisa bor?", "Tovush tushishi (eliziya)", ["Tovush orttirilishi", "Assimilyatsiya", "Dissimilyatsiya"], "Ikkinchi bo'g'indagi «i» tushib qolgan."),
        C(2, "«Yurak + i → yuragi» shaklida qanday o'zgarish yuz bergan?", "k undoshi g ga almashgan", ["Unli tovush tushgan", "Tovush orttirilgan", "Hech qanday o'zgarish yo'q"], "Jarangsiz undosh unli oldida jaranglashgan."),
    ],
    "N6.7": [
        C(1, "«Gulzor» so'zidagi «-zor» qanday qo'shimcha?", "So'z yasovchi", ["Shakl yasovchi", "Kelishik qo'shimchasi", "Egalik qo'shimchasi"], "Joy oti yasaydi."),
        C(2, "«Kitoblarimdan» so'zida qo'shimchalar qanday tartibda kelgan?", "ko'plik + egalik + kelishik", ["egalik + ko'plik + kelishik", "kelishik + egalik + ko'plik", "ko'plik + kelishik + egalik"], "kitob + lar + im + dan."),
    ],
    "N6.8": [
        C(2, "Alpomish qaysi el (urug') qahramoni?", "Qo'ng'irot", ["Mang'it", "Qipchoq", "Nayman"], "Doston qo'ng'irot urug'i qahramonlari haqida."),
        C(2, "«Go'ro'g'li» turkumida Go'ro'g'lining asrandi o'g'li?", "Avazxon", ["Yodgor", "Qultoy", "Boychibor"], "«Avazxon» dostoni turkumning mashhur qismi."),
    ],
    "N7.1": [
        C(1, "Qaysi so'z turdosh ot?", "daryo", ["Toshkent", "Amudaryo", "Navoiy"], "Turdosh ot bir turdagi narsalarning umumiy nomi."),
        C(2, "Ot qanday grammatik kategoriyalarga ega?", "Son, egalik, kelishik", ["Zamon, mayl", "Daraja", "Nisbat"], "Otlar ko'plik, egalik va kelishik qo'shimchalarini oladi."),
    ],
    "N7.3": [
        C(1, "«Eng chiroyli» qaysi darajada?", "Orttirma daraja", ["Oddiy daraja", "Qiyosiy daraja", "Ozaytirma daraja"], "«eng» so'zi orqali orttirma daraja."),
        C(2, "«Bilimli» so'zi qanday yasalgan?", "bilim + -li (sifat yasovchi)", ["bil + -im + -li (fe'l)", "tub so'z", "bilim + -li (ot yasovchi)"], "-li qo'shimchasi otdan sifat yasaydi."),
    ],
    "N7.4": [
        C(1, "Qaysi qatorda faqat tartib sonlar berilgan?", "birinchi, uchinchi, o'ninchi", ["bir, uch, o'n", "birinchi, uchta, o'nlab", "ikkov, uchov, to'rtov"], "-(i)nchi qo'shimchali sonlar."),
        C(2, "«Yigirma besh» soni tuzilishiga ko'ra qanday son?", "Qo'shma son", ["Sodda son", "Juft son", "Takroriy son"], "Ikki sodda sonning birikuvidan tuzilgan."),
    ],
    "N7.5": [
        C(2, "«Kimdir», «nimadir» qaysi olmosh turi?", "Gumon olmoshi", ["So'roq olmoshi", "Belgilash olmoshi", "Kishilik olmoshi"], "-dir qo'shimchasi gumon ma'nosini beradi."),
        C(2, "«Har kim», «barcha» qaysi olmosh turi?", "Belgilash olmoshi", ["Gumon olmoshi", "Ko'rsatish olmoshi", "O'zlik olmoshi"], "Umumlashtirish, belgilash ma'nosi."),
    ],
    "N7.6": [
        C(2, "«Ataylab» so'zi qaysi turdagi ravish?", "Maqsad ravishi", ["Payt ravishi", "O'rin ravishi", "Miqdor-daraja ravishi"], "Harakatning maqsadini bildiradi."),
        C(3, "«Noiloj» so'zi qaysi turdagi ravish?", "Sabab ravishi", ["Payt ravishi", "O'rin ravishi", "Holat ravishi"], "Harakatning sababini bildiradi."),
    ],
    "N7.7": [
        C(1, "«Devonu lug'otit turk» asari muallifi?", "Mahmud Koshg'ariy", ["Yusuf Xos Hojib", "Ahmad Yugnakiy", "Ahmad Yassaviy"], "XI asrda yozilgan turkiy tillar lug'ati."),
        C(2, "«Hibatul-haqoyiq» qaysi asrda yaratilgan?", "XII asr", ["X asr", "XV asr", "XVIII asr"], "Ahmad Yugnakiyning pand-nasihat dostoni."),
    ],
    "N8.2": [
        C(1, "«Kelib» so'zi fe'lning qaysi vazifa shakli?", "Ravishdosh", ["Sifatdosh", "Harakat nomi", "Buyruq mayli"], "-ib qo'shimchasi ravishdosh yasaydi."),
        C(2, "Harakat nomi qaysi so'roqqa javob beradi?", "nima qilish?", ["qanday?", "qachon?", "kim?"], "O'qish, yozish — nima qilish?"),
    ],
    "N8.3": [
        C(1, "«Boraman» fe'li qaysi zamonda?", "Hozirgi-kelasi zamon", ["O'tgan zamon", "Buyruq mayli", "Shart mayli"], "-a/-y + shaxs qo'shimchasi."),
        C(2, "Fe'l nisbatlari qaysilar?", "Aniq, o'zlik, majhul, birgalik, orttirma", ["Oddiy, qiyosiy, orttirma", "Sodda, qo'shma, juft", "Bosh, qaratqich, tushum"], "Fe'lning nisbat kategoriyasi."),
    ],
    "N8.4": [
        C(1, "«Faqat», «hatto», «-gina» qaysi turkumga kiradi?", "Yuklama", ["Ko'makchi", "Bog'lovchi", "Modal so'z"], "Qo'shimcha ma'no nozikligi beradi."),
        C(2, "«Sababli», «tufayli» qaysi turkumga kiradi?", "Ko'makchi", ["Bog'lovchi", "Yuklama", "Ravish"], "Ot bilan sabab munosabatini bildiradi."),
    ],
    "N8.5": [
        C(2, "«Shubhasiz», «albatta» modal so'zlari qanday ma'noni bildiradi?", "Tasdiq, ishonch", ["Gumon", "Taassuf", "Inkor"], "So'zlovchining qat'iy ishonchi."),
        C(2, "«Taq-tuq», «sharaq-shuruq» qanday so'zlar?", "Tovushga taqlid so'zlar", ["Holatga taqlid so'zlar", "Undov so'zlar", "Modal so'zlar"], "Tovushni ifodalaydi."),
    ],
    "N8.6": [
        C(1, "«Maktabga bormoq» birikmasida tobe so'z qaysi?", "maktabga", ["bormoq", "ikkalasi ham hokim", "birikma emas"], "Hokim so'z — bormoq."),
        C(2, "Qaysi birikmada bitishuv aloqasi bor?", "tez yugurmoq", ["kitobni o'qimoq", "maktabning hovlisi", "men keldim"], "Tobe so'z qo'shimchasiz, tartib va ohang bilan bog'langan."),
    ],
    "N8.7": [
        C(2, "«Bizning maqsadimiz — bilim olish» gapida tire nima uchun qo'yilgan?", "Ega va kesim ot (harakat nomi) bilan ifodalangan", ["Undalmadan keyin", "Kiritmani ajratish uchun", "Ko'chirma gapda"], "Kesim bog'lamasiz otdan iborat."),
        C(1, "Gapda ega odatda qaysi kelishikda bo'ladi?", "Bosh kelishikda", ["Qaratqich kelishigida", "Tushum kelishigida", "Jo'nalish kelishigida"], "Kim? nima? so'roqlariga javob bo'ladi."),
    ],
    "N8.9": [
        C(2, "Bobur Hindistonda qaysi jangdan so'ng saltanatga asos soldi (1526)?", "Panipat jangi", ["Qatvon jangi", "Talas jangi", "Anqara jangi"], "Ibrohim Lo'diy ustidan g'alaba."),
        C(1, "Boburning lirik she'rlari jamlangan to'plam?", "Devon", ["«Xamsa»", "«Qutadg'u bilig»", "«Mahbub ul-qulub»"], "Bobur devonida g'azal va ruboiylar bor."),
    ],
    "N9.2": [
        C(2, "«Qorong'i tushdi» gapi qanday gap?", "Ikki tarkibli gap", ["Atov gap", "Shaxsi noma'lum gap", "Shaxsi umumlashgan gap"], "Ega — qorong'i, kesim — tushdi."),
        C(1, "«Yoz. Issiq kunlar.» gaplari qanday gaplar?", "Atov gaplar", ["Shaxsi aniq gaplar", "Qo'shma gaplar", "Undov gaplar"], "Predmetning borligini bildiradi."),
    ],
    "N9.3": [
        C(2, "Qaysi gapda ajratilgan hol bor?", "Yo'lda, uyga qaytayotib, do'stimni uchratdim.", ["Do'stim, keling.", "Albatta, u keladi.", "Men uyga qaytdim."], "Ravishdoshli birikma ajratilgan."),
        C(2, "Kiritma qurilma gapda qanday ajratiladi?", "Qavs yoki tire bilan", ["Faqat nuqta bilan", "So'roq belgisi bilan", "Ikki nuqta bilan"], "Qo'shimcha izoh beruvchi qurilma."),
    ],
    "N9.4": [
        C(2, "«Goh yomg'ir yog'adi, goh quyosh chiqadi» gapida qanday bog'lovchi bor?", "Ayiruv bog'lovchisi", ["Zidlov bog'lovchisi", "Biriktiruv bog'lovchisi", "Inkor bog'lovchisi"], "goh...goh — ayiruv."),
        C(2, "«Na u keldi, na men bordim» gapidagi «na...na» qanday bog'lovchi?", "Inkor bog'lovchisi", ["Zidlov", "Ayiruv", "Biriktiruv"], "Ikkala harakatni inkor etadi."),
    ],
    "N9.5": [
        C(2, "«Qayerda mehnat bo'lsa, o'sha yerda baraka bo'ladi» gapida ergash gap turi?", "O'rin ergash gap", ["Payt ergash gap", "Sabab ergash gap", "Shart ergash gap"], "Qayerda? so'rog'iga javob beradi."),
        C(2, "«Men qaytmagunimcha, kutib tur» gapida ergash gap turi?", "Payt ergash gap", ["Sabab ergash gap", "O'rin ergash gap", "To'siqsiz ergash gap"], "Qachongacha? so'rog'iga javob."),
    ],
    "N9.6": [
        C(2, "«Bahor keldi — dalalar yashardi» gapida tire qanday munosabatni bildiradi?", "Natija, tez almashinuv", ["Zidlash", "Ayirish", "Inkor"], "Ikkinchi qism birinchisining natijasi."),
        C(1, "Bog'lovchisiz qo'shma gap qismlari sanash ohangi bilan aytilsa, qaysi belgi qo'yiladi?", "Vergul", ["Ikki nuqta", "Tire", "So'roq belgisi"], "Sanash munosabati."),
    ],
    "N9.7": [
        C(1, "Badiiy asarlar qaysi nutq uslubida yoziladi?", "Badiiy uslub", ["Rasmiy-idoraviy", "Ilmiy", "So'zlashuv"], "Obrazli, ta'sirchan til."),
        C(2, "Ko'chirma gapni o'zlashtirma gapga aylantirganda nima o'zgaradi?", "Shaxs va olmoshlar muallif nuqtai nazariga moslanadi", ["Hech narsa o'zgarmaydi", "Faqat tinish belgilari qo'shiladi", "Gap she'rga aylanadi"], "Masalan: «Men boraman», — dedi → U borishini aytdi."),
    ],
    "N9.8": [
        C(1, "Mahmudxo'ja Behbudiy qaysi shaharda tug'ilgan?", "Samarqand", ["Buxoro", "Toshkent", "Qo'qon"], "1875-yilda Samarqand yaqinida tug'ilgan."),
        C(2, "«Padarkush» dramasi necha pardadan iborat?", "3", ["1", "5", "7"], "Uch pardali, to'rt ko'rinishli drama."),
    ],
    "N9.10": [
        C(2, "Cho'lponning «Yorqinoy» asari qaysi janrda?", "Drama", ["Roman", "Doston", "Hikoya"], "Cho'lpon dramaturg sifatida ham ijod qilgan."),
        C(2, "Cho'lpon qaysi yili qatag'on qurboni bo'lgan?", "1938", ["1924", "1956", "1945"], "1937-yil hibsga olinib, 1938-yilda otilgan."),
    ],
    "N10.1": [
        C(2, "Matnda ifodalangan asosiy fikr qanday ataladi?", "G'oya (asosiy fikr)", ["Sarlavha", "Xatboshi", "Epigraf"], "Muallif aytmoqchi bo'lgan asosiy fikr."),
        C(2, "Matnning nutq turlari qaysilar?", "Tasvir, hikoya, mulohaza", ["Ega, kesim, aniqlovchi", "Monolog, dialog, polilog", "Ot, sifat, son"], "Tasviriy, hikoya va mulohaza matnlari."),
    ],
    "N10.3": [
        C(2, "Aruz vaznining asosi nima?", "Cho'ziq va qisqa hijolarning tartibli kelishi", ["Bo'g'inlar soni", "Urg'u", "Qofiya soni"], "Barmoqda — bo'g'inlar soni."),
        C(1, "Ruboiy necha misradan iborat?", "4", ["2", "5", "14"], "To'rt misrali she'r."),
    ],
    "N10.5": [
        C(2, "Abdulla Qahhorning «O'g'ri» hikoyasidagi qahramon?", "Qobil bobo", ["Saida", "Otabek", "Zebi"], "Ho'kizi o'g'irlangan chol."),
        C(2, "Abdulla Qahhorning komediyasi?", "«Shohi so'zana»", ["«Padarkush»", "«Mirzo Ulug'bek»", "«Yorqinoy»"], "Mashhur komediya."),
    ],
    "N10.6": [
        C(2, "Maqsud Shayxzodaning yana bir tarixiy dramasi?", "«Jaloliddin Manguberdi»", ["«Sinchalak»", "«Kecha va kunduz»", "«Ufq»"], "She'riy tarixiy drama."),
        C(3, "Maqsud Shayxzoda qayerda tug'ilgan?", "Og'dash (Ozarbayjon)", ["Toshkent", "Samarqand", "Buxoro"], "1908-yilda Ozarbayjonda tug'ilib, Toshkentda ijod qilgan."),
    ],
    "N10.7": [
        C(2, "Said Ahmadning «Ufq» trilogiyasining ikkinchi kitobi?", "«Hijron kunlari»", ["«Qirq besh kun»", "«Ufq bo'sag'asida»", "«Jimjitlik»"], "Trilogiya: «Qirq besh kun», «Hijron kunlari», «Ufq bo'sag'asida»."),
        C(2, "Said Ahmadning «Jimjitlik» asari qaysi janrda?", "Roman", ["Doston", "Ruboiy", "Komediya"], "Yozuvchining romani."),
    ],
    "N10.8": [
        C(2, "«Ulug'bek xazinasi» romanida Ulug'bek kitoblarini saqlab qolishga harakat qilgan shogird?", "Ali Qushchi", ["Abdullatif", "Bobur", "Navoiy"], "Ali Qushchi — Ulug'bekning shogirdi va hamkori."),
        C(2, "Odil Yoqubovning «Ko'hna dunyo» romani qaysi allomalar haqida?", "Ibn Sino va Beruniy", ["Navoiy va Jomiy", "Bobur va Humoyun", "Ulug'bek va Ali Qushchi"], "Tarixiy roman."),
    ],
    "N10.9": [
        C(2, "«Yulduzli tunlar» romanida Bobur qaysi vodiydan chiqqan shahzoda sifatida tasvirlanadi?", "Farg'ona", ["Zarafshon", "Xorazm", "Surxon"], "Bobur Andijonda tug'ilgan, Farg'ona hokimi bo'lgan."),
    ],
    "N10.10": [
        C(2, "Erkin Vohidovning «Oltin devor» asari qaysi janrda?", "Komediya", ["Doston", "Roman", "Ruboiy"], "Sahnada mashhur komediya."),
        C(2, "Abdulla Oripovning ilk she'riy to'plami?", "«Mening yulduzim»", ["«Nido»", "«Uyg'onish»", "«Tong nafasi»"], "1965-yilda nashr etilgan."),
    ],
    "N10.11": [
        C(2, "«Otamdan qolgan dalalar» romanining bosh qahramoni?", "Dehqonqul", ["Akbarali", "Otabek", "Qobil bobo"], "Surxon dehqoni Dehqonqul taqdiri."),
        C(2, "Tog'ay Murodning asl ism-sharifi?", "Tog'aymurod Mengnorov", ["Abdulhamid Sulaymon o'g'li", "Musa Toshmuhammad o'g'li", "Abdulla Qodiriy"], "1948-yilda Surxondaryoda tug'ilgan."),
    ],
}
