"""Biologiya: 6-sinf (Botanika, 5–6-sinf mazmuni) va 7-sinf (Zoologiya) savollari."""
from ._dsl import C, O, M

Q = {}

Q["B6.1"] = [
    C(1, "«Hujayra» (cellula) terminini birinchi bo'lib kim va qachon fanga kiritgan?", "Robert Guk, 1665-yil", ["Antoni van Levenguk, 1674-yil", "Robert Braun, 1831-yil", "S.G. Navashin, 1898-yil"], "Guk po'kak daraxti kesmasini mikroskopda ko'rib, «hujayra» atamasini kiritgan."),
    C(1, "Tirik bir hujayrali organizmlarni (bakteriya, infuzoriya) birinchi bo'lib kim ko'rgan?", "Antoni van Levenguk", ["Robert Guk", "Robert Braun", "I.I. Mechnikov"], "Levenguk 1674-yilda tirik bir hujayralilarni kuzatgan."),
    C(1, "O'simlik hujayrasida yadroni kim kashf etgan?", "Robert Braun", ["Robert Guk", "Antoni van Levenguk", "S.G. Navashin"], "Braun yadroni 1831-yilda kashf etgan."),
    M(2, [("Robert Guk", "Hujayra terminini kiritgan (1665)"), ("Levenguk", "Tirik bir hujayralilarni ko'rgan (1674)"), ("Robert Braun", "Yadroni kashf etgan (1831)")], "Kashfiyotlar xronologiyasi: Guk → Levenguk → Braun."),
    C(2, "O'simlik hujayra devori asosan nimadan iborat?", "Tsellyuloza (kletchatka)", ["Xitin", "Glikogen", "Murein"], "Tsellyuloza hujayraga qattiq ramka beradi."),
    C(2, "Guk hujayrani qaysi obyektda ko'rgan?", "Po'kak daraxti kesmasida", ["Piyoz tangachasida", "Baliq qonida", "Zamburug' mitseliyasida"], "Po'kak kesmasi mayda katakchalar (hujayralar)dan iborat ko'ringan."),
    C(2, "Quyidagi kashfiyotlar to'g'ri xronologik tartibda berilgan javobni toping.", "Guk → Levenguk → Braun → Navashin", ["Levenguk → Guk → Braun → Navashin", "Braun → Guk → Levenguk → Navashin", "Guk → Braun → Levenguk → Navashin"], "1665 → 1674 → 1831 → 1898."),
    C(2, "Levenguk mikroskopda qaysi organizmlarni kuzatgan?", "Bakteriya va infuzoriyalarni", ["Faqat o'simlik hujayralarini", "Viruslarni", "Faqat yadro va ribosomalarni"], "U birinchi bo'lib tirik mikroorganizmlarni ko'rgan."),
    C(3, "Guk hujayrani kashf etgan yil va Braun yadroni kashf etgan yil orasida necha yil farq bor?", "166 yil", ["156 yil", "176 yil", "224 yil"], "1831 − 1665 = 166."),
    C(3, "Levenguk bir hujayralilarni ko'rgan yildan Navashin qo'sh urug'lanishni kashf etgan yilgacha necha yil o'tgan?", "224 yil", ["214 yil", "234 yil", "166 yil"], "1898 − 1674 = 224."),
    O(3, "Braun yadroni kashf etgan yildan Navashin qo'sh urug'lanishni kashf etgan yilgacha necha yil o'tgan? (faqat son)", ["67"], "1898 − 1831 = 67."),
]

Q["B6.2"] = [
    C(1, "Rangsiz plastida qanday ataladi?", "Leykoplast", ["Xloroplast", "Xromoplast", "Lizosoma"], "Leykoplast — rangsiz plastida."),
    C(1, "Yashil rangli plastida qaysi?", "Xloroplast", ["Leykoplast", "Xromoplast", "Vakuola"], "Xloroplastda xlorofill bor, fotosintez shu yerda boradi."),
    C(1, "Hujayra shirasi bilan to'lgan bo'shliq qanday ataladi?", "Vakuola", ["Plastida", "Yadrocha", "Sitoplazma"], "Vakuola hujayra shirasini saqlaydi."),
    M(2, [("Leykoplast", "Rangsiz plastida"), ("Xloroplast", "Yashil plastida"), ("Xromoplast", "Sariq va qizil plastida")], "Plastidalar rangi bo'yicha farqlanadi."),
    C(2, "Gulga ko'k va binafsha rang beruvchi pigment qaysi?", "Antosian", ["Xlorofill", "Karotin", "Gemoglobin"], "Antosian hujayra shirasida erigan pigment."),
    C(2, "Qarigan hujayrada vakuola qanday bo'ladi?", "Bitta yirik markaziy vakuola", ["Ko'p mayda vakuolalar", "Vakuola yo'qoladi", "Yadro ichida joylashadi"], "Yosh hujayrada mayda ko'p, qarigan hujayrada bitta yirik vakuola bo'ladi."),
    C(2, "Kuzda barglarning sarg'ayishiga sabab plastidalarning qaysi o'zgarishi?", "Xloroplastning xromoplastga aylanishi", ["Leykoplastning xloroplastga aylanishi", "Xromoplastning xloroplastga aylanishi", "Xloroplastning leykoplastga aylanishi"], "Kuzda/pishganda xloroplast xromoplastga aylanadi."),
    C(2, "Plastidalar orasida qaysi birining o'zgarishi qaytmaydi (istisno)?", "Xromoplast qayta xloroplastga aylana olmaydi", ["Leykoplast xloroplastga aylana olmaydi", "Xloroplast xromoplastga aylana olmaydi", "Barcha plastidalar o'zaro erkin aylanadi"], "Istisno: xromoplastdan xloroplast hosil bo'lmaydi."),
    C(3, "Plastidalar o'zgarishining to'g'ri zanjirini toping.", "Leykoplast → xloroplast → xromoplast", ["Xromoplast → xloroplast → leykoplast", "Xloroplast → leykoplast → xromoplast", "Xromoplast → leykoplast → xloroplast"], "Yorug'likda leykoplast yashillanadi, pishganda xromoplastga aylanadi."),
    O(3, "Pomidor pishganda qizarishiga sabab bo'luvchi plastida nomini yozing.", ["xromoplast", "xromoplastlar"], "Pishganda xloroplastlar xromoplastga aylanadi."),
    O(3, "Hujayra shirasi bilan to'lgan va yoshligida mayda ko'p bo'ladigan organoid nomini yozing.", ["vakuola", "vakuolalar"], "Vakuola."),
]

Q["B6.3"] = [
    C(1, "Doim bo'linib turadigan, yupqa devorli va yirik yadroli hujayralardan iborat to'qima qaysi?", "Meristema (hosil qiluvchi)", ["Qoplovchi", "Mexanik", "O'tkazuvchi"], "Meristema hujayralari doimo bo'linadi."),
    C(1, "Suv va mineral moddalarni ildizdan bargga tashiydigan to'qima qaysi?", "Ksilema (yog'ochlik naylari)", ["Floema", "Epiderma", "Kollenxima"], "Ksilema — ko'tariluvchi oqim."),
    C(1, "Og'izchalar qaysi to'qimada joylashgan?", "Epidermada", ["Po'kakda", "Sklerenximada", "Kambiyda"], "Epiderma — barg va poya ustini qoplovchi tirik hujayralar."),
    M(2, [("Ksilema", "Suv va minerallarni yuqoriga tashiydi"), ("Floema", "Organik moddalarni pastga tashiydi"), ("Meristema", "Doim bo'linadigan hujayralar")], "To'qimalar vazifasi."),
    C(2, "Floema hujayralarining xususiyati qaysi?", "Tirik, yo'ldosh hujayralarga ega", ["O'lik, yo'ldosh hujayrasiz", "O'lik, qalin devorli", "Faqat fotosintez qiladi"], "Floema — tirik elaksimon naylar."),
    C(2, "Kambiy qaysi turdagi meristemaga kiradi va nimani ta'minlaydi?", "Lateral; poyaning eniga o'sishini", ["Apikal; bo'yiga o'sishni", "Lateral; bo'yiga o'sishni", "Apikal; eniga o'sishni"], "Kambiy — yon meristema."),
    C(2, "Po'kak to'qimasi hujayralari qanday?", "O'lik, qishki himoyani ta'minlaydi", ["Tirik, fotosintez qiladi", "Tirik, doim bo'linadi", "O'lik, suv tashiydi"], "Po'kak — qoplovchi to'qima, o'lik hujayralar."),
    C(2, "Sklerenxima qanday to'qima?", "O'lik, qattiq mexanik to'qima", ["Tirik, cho'ziluvchan mexanik to'qima", "Tirik meristema", "Tirik o'tkazuvchi to'qima"], "Cho'ziluvchan tirik mexanik to'qima — kollenxima."),
    C(3, "Quyidagi tasdiqlardan qaysi biri to'g'ri?", "Ksilema o'lik, floema tirik hujayralardan iborat", ["Ksilema tirik, floema o'lik hujayralardan iborat", "Ikkalasi ham tirik hujayralardan iborat", "Ikkalasi ham o'lik hujayralardan iborat"], "Ksilema — o'lik, floema — tirik."),
    O(3, "Poya va ildizni bo'yiga o'stiruvchi meristema turini yozing (bir so'z).", ["apikal", "uchki", "apikal meristema", "uchki meristema"], "Apikal (uchki) meristema bo'yiga o'stiradi."),
    O(3, "Organik moddalarni bargdan ildizga tashuvchi to'qima nomini yozing.", ["floema", "lub", "elaksimon naylar"], "Floema — tushuvchi oqim."),
]

Q["B6.4"] = [
    C(1, "Urug' murtagidan chiqadigan ildiz qaysi?", "Asosiy ildiz", ["Yon ildiz", "Qo'shimcha ildiz", "Ildiz tukchasi"], "Asosiy ildiz urug' murtagidan rivojlanadi."),
    C(1, "Ikki pallali o'simliklarda qanday ildiz tizimi bo'ladi?", "O'q ildiz", ["Popuk ildiz", "Faqat qo'shimcha ildiz", "Ildiz bo'lmaydi"], "Asosiy ildiz yaqqol ko'rinadi."),
    C(1, "Bir pallali o'simliklarda ildiz tizimi qanday?", "Popuk ildiz", ["O'q ildiz", "Faqat yon ildiz", "Ildiz tuyumi"], "Asosiy ildiz o'smay qoladi, qo'shimcha ildizlar ko'p."),
    M(2, [("Ildizmeva", "Sabzi"), ("Ildiz-tuyum", "Georgina"), ("Popuk ildiz", "Bug'doy")], "Ildiz shakl o'zgarishlari va tizimlari."),
    C(2, "Ildiz zonalarining to'g'ri ketma-ketligini toping.", "Qincha → bo'linuvchi → o'suvchi → so'ruvchi → o'tkazuvchi", ["Qincha → so'ruvchi → o'suvchi → bo'linuvchi → o'tkazuvchi", "Bo'linuvchi → qincha → o'suvchi → so'ruvchi → o'tkazuvchi", "Qincha → o'suvchi → bo'linuvchi → o'tkazuvchi → so'ruvchi"], "Uchidan boshlab shu tartibda joylashadi."),
    C(2, "Ildiz tukchalari qaysi zonada joylashgan?", "So'ruvchi zonada", ["Bo'linuvchi zonada", "O'suvchi zonada", "Ildiz qinchasida"], "Suv va minerallarni so'rish tukchalar orqali boradi."),
    C(2, "Qo'shimcha ildizlar o'simlikning qaysi qismidan chiqadi?", "Poya yoki bargdan", ["Faqat urug' murtagidan", "Faqat asosiy ildizdan", "Faqat gulidan"], "Qo'shimcha ildiz poya yoki bargdan hosil bo'ladi."),
    C(3, "Qaysi juftlik ildizning o'zgargan shakllariga to'g'ri misol?", "Sabzi — ildizmeva, batat — ildiz-tuyum", ["Sabzi — ildiz-tuyum, batat — ildizmeva", "Georgina — ildizmeva, turp — ildiz-tuyum", "Lavlagi — ildiz-tuyum, georgina — ildizmeva"], "Sabzi, turp, lavlagi — ildizmeva; georgina, batat — ildiz-tuyum."),
    O(3, "Ildiz qinchasidan keyin keladigan zona nomini yozing.", ["bo'linuvchi", "bo'linuvchi zona"], "Qincha → bo'linuvchi zona."),
    O(3, "Ildiz tizimida asosiy ildiz yaqqol ko'rinmaydigan, ko'p qo'shimcha ildizli turi qanday ataladi?", ["popuk", "popuk ildiz"], "Popuk ildiz — bir pallalilarda."),
]

Q["B6.5"] = [
    C(1, "Ichida faqat barg va poya murtagi bo'lgan kurtak qaysi?", "Vegetativ kurtak", ["Generativ kurtak", "Gul kurtak", "Ildiz kurtagi"], "Vegetativ kurtak — barg va poya murtagi."),
    C(1, "Ichida gul murtagi bo'lgan kurtak qanday ataladi?", "Generativ (gul) kurtak", ["Vegetativ kurtak", "Yon kurtak", "Uchki kurtak"], "Gul kurtak yirikroq va yumaloq bo'ladi."),
    C(1, "Oddiy bargda bitta bargbandda nechta barg plastinkasi bo'ladi?", "1 ta", ["2 ta", "3 ta", "Bir nechta"], "Murakkab bargda bir nechta bargcha bo'ladi."),
    M(2, [("Ketma-ket joylashish", "Olma"), ("Qarama-qarshi joylashish", "Yalpiz"), ("Xalqasimon joylashish", "Qirqbo'g'im")], "Barg joylashish turlari."),
    C(2, "Poya qatlamlarining tashqaridan ichkariga to'g'ri tartibini toping.", "Po'stloq → lub → kambiy → yog'ochlik → o'zak", ["Po'stloq → yog'ochlik → kambiy → lub → o'zak", "O'zak → kambiy → lub → yog'ochlik → po'stloq", "Po'stloq → kambiy → lub → o'zak → yog'ochlik"], "Kambiy lub va yog'ochlik orasida."),
    C(2, "Kashtan bargi qanday murakkab barg turiga kiradi?", "Panjasimon", ["Juft-patli", "Uchburchakli", "Oddiy"], "Kashtan — panjasimon murakkab barg."),
    C(2, "Poyaning eng markaziy qatlami qaysi va u qanday to'qimadan?", "O'zak; g'amlovchi parenxima", ["Lub; elaksimon naylar", "Kambiy; meristema", "Po'stloq; po'kak"], "O'zak g'amlovchi parenximadan iborat."),
    C(3, "Baqatosh (Plantago) haqida qaysi tasdiq to'g'ri?", "Ikki pallali, lekin bargi yoyli tomirlangan", ["Bir pallali, bargi yoyli tomirlangan", "Ikki pallali, bargi to'rsimon tomirlangan", "Bir pallali, bargi to'rsimon tomirlangan"], "Baqatosh — tomirlanish istisnosi."),
    O(3, "Qarg'ako'z (Paris) bir pallali o'simlik, lekin bargi qanday tomirlangan? (bir so'z)", ["to'rsimon", "to'rsimon tomirlangan"], "Qarg'ako'z bargi to'rsimon tomirlangan (istisno)."),
    O(3, "Bitta bargbandda bir nechta bargchalar bo'lgan barg qanday ataladi?", ["murakkab", "murakkab barg"], "Murakkab barg."),
]

Q["B6.6"] = [
    C(1, "Gulli o'simliklarda qo'sh urug'lanishni kim kashf etgan?", "S.G. Navashin", ["R. Braun", "R. Guk", "Ch. Darvin"], "Navashin 1898-yilda kashf etgan."),
    C(1, "Gulkosa nimadan iborat?", "Kosabarglardan", ["Tojbarglardan", "Changchi va urug'chidan", "Faqat urug'chidan"], "Gultoj — tojbarglardan."),
    C(1, "Lola gulqo'rg'oni qanday turga kiradi?", "Oddiy gulqo'rg'on", ["Murakkab gulqo'rg'on", "Gulkosasiz gul", "Gultojsiz gul"], "Kosa va tojbarglarga ajralmagan."),
    M(2, [("Zigota", "2n"), ("Endosperm", "3n"), ("Spermiy", "n")], "Qo'sh urug'lanishda hosil bo'ladigan hujayralar xromosoma to'plami."),
    C(2, "Spermiy tuxum hujayra bilan qo'shilganda nima hosil bo'ladi?", "Zigota (2n)", ["Endosperm (3n)", "Spermiy (n)", "Markaziy hujayra (2n)"], "Zigotadan urug' murtagi rivojlanadi."),
    C(2, "Endosperm hujayralari xromosoma to'plami qanday?", "3n", ["n", "2n", "4n"], "Spermiy (n) + markaziy hujayra (2n) = 3n."),
    C(2, "Na'matak guli qanday gulqo'rg'onga ega?", "Murakkab (kosa va tojbarglari aniq ajralgan)", ["Oddiy", "Gulqo'rg'onsiz", "Faqat tojbargli"], "Na'matak — murakkab gulqo'rg'on."),
    C(3, "Endospermni hosil qilishda ikkinchi spermiy qaysi hujayra bilan qo'shiladi?", "Markaziy hujayra (2n)", ["Tuxum hujayra (n)", "Zigota (2n)", "Yo'ldosh hujayra (n)"], "Natijada g'amlovchi endosperm (3n) hosil bo'ladi."),
    C(3, "Somatik hujayrasida 16 ta xromosoma bo'lgan o'simlik spermiyida nechta xromosoma bo'ladi?", "8", ["16", "4", "24"], "Spermiy gaploid (n): 16/2 = 8."),
    O(3, "O'simlikning somatik hujayrasida 24 ta xromosoma bor. Uning endosperm hujayrasida nechta xromosoma bo'ladi? (son)", ["36"], "n = 12, endosperm 3n = 36."),
]

Q["B6.7"] = [
    C(1, "Karam va turp qaysi oilaga kiradi?", "Karamguldoshlar", ["Ra'noguldoshlar", "Burchoqdoshlar", "Loladoshlar"], "Karam, turp, rediska — Karamguldoshlar."),
    C(1, "Kungaboqar qaysi oilaga mansub?", "Murakkabguldoshlar", ["Ituzumdoshlar", "Bug'doydoshlar", "Karamguldoshlar"], "Kungaboqar, qoqi, astra — Murakkabguldoshlar."),
    C(1, "Bug'doy mevasi qaysi turga kiradi?", "Don", ["Dukkak", "Pishta", "Rezavor"], "Bug'doydoshlar mevasi — don."),
    M(2, [("Ra'noguldoshlar", "Olma"), ("Burchoqdoshlar", "No'xat"), ("Bug'doydoshlar", "Makkajo'xori")], "Oilalar va vakillar."),
    C(2, "Karamguldoshlar mevasi qaysi?", "Qo'zoq yoki qo'zoqcha", ["Dukkak", "Don", "Pishta"], "Karamguldoshlar mevasi qo'zoq, qo'zoqcha."),
    C(2, "Dukkak mevali oila qaysi?", "Burchoqdoshlar", ["Ituzumdoshlar", "Ra'noguldoshlar", "Loladoshlar"], "Loviya, no'xat, mosh — Burchoqdoshlar."),
    C(2, "Pomidor, baqlajon va kartoshka qaysi oilaga kiradi?", "Ituzumdoshlar", ["Burchoqdoshlar", "Karamguldoshlar", "Bug'doydoshlar"], "Ituzumdoshlar mevasi rezavor yoki ko'sakcha."),
    C(2, "Murakkabguldoshlar mevasi qanday ataladi?", "Pishta (ayri urug'li)", ["Qo'zoq", "Dukkak", "Don"], "Pishta — Murakkabguldoshlar mevasi."),
    C(3, "K4 L4 O4+2 U(2) gul formulasi qaysi oilaga xos?", "Karamguldoshlar", ["Ra'noguldoshlar", "Burchoqdoshlar", "Ituzumdoshlar"], "4 kosa, 4 toj, 6 (4+2) changchi, bitta urug'chi."),
    O(3, "*K5 L5 O∞ U∞ yoki 1 gul formulasi qaysi oilaga xos? (oila nomini yozing)", ["ra'noguldoshlar", "ra'noguldosh", "ra'nogullar", "rosaceae"], "Ra'noguldoshlar: 5 kosa, 5 toj, ko'p changchi."),
    O(3, "P2 O3 U1 gul formulasi qaysi oilaga xos? (oila nomini yozing)", ["bug'doydoshlar", "bug'doydosh", "poaceae"], "Bug'doydoshlar: gul qobig'i 2, changchi 3, urug'chi 1."),
]

# ---------------------------------------------------------------- 7-SINF
Q["B7.1"] = [
    C(1, "Oddiy amyoba qanday harakatlanadi?", "Soxta oyoqlar (psevdopodiya) yordamida", ["Kirpikchalar yordamida", "Xivchin yordamida", "Qanotlar yordamida"], "Amyoba qobiqsiz, soxta oyoq hosil qiladi."),
    C(1, "Yashil evglena qaysi organoid yordamida harakatlanadi?", "Xivchin (hif)", ["Kirpikchalar", "Soxta oyoq", "Qisqaruvchi vakuola"], "Evglena xivchinli."),
    C(1, "Amyoba noqulay sharoitda nima hosil qiladi?", "Tsista", ["Spora", "Gameta", "Urug'"], "Tsista — himoya holati."),
    M(2, [("Amyoba", "Soxta oyoq"), ("Evglena", "Stigma (qizil ko'zcha)"), ("Qisqaruvchi vakuola", "Osmoregulyatsiya va ayirish")], "Bir hujayralilar tuzilishi."),
    C(2, "Evglena qanday oziqlanadi?", "Miksotrof (yorug'likda fotosintez, qorong'ida tayyor organik modda)", ["Faqat avtotrof", "Faqat geterotrof", "Xemosintez qiladi"], "Miksotrof oziqlanish."),
    C(2, "Evglenadagi stigma qanday vazifani bajaradi?", "Yorug'likni sezib, fototaksisni ta'minlaydi", ["Oziqani hazm qiladi", "Ortiqcha suvni chiqaradi", "Ko'payishni boshqaradi"], "Stigma — qizil ko'zcha."),
    C(2, "Qisqaruvchi vakuolaning vazifasi qaysi?", "Osmoregulyatsiya va ayirish", ["Fotosintez", "Fagotsitoz", "Harakatlanish"], "Ortiqcha suv va zararli moddalarni chiqaradi."),
    C(2, "Amyoba qattiq oziqani qanday qabul qiladi?", "Fagotsitoz orqali", ["Pinotsitoz orqali", "Fotosintez orqali", "Xemosintez orqali"], "Suyuqlik yutilishi — pinotsitoz."),
    C(3, "Evglena qorong'ulikda qanday oziqlanadi?", "Tayyor organik moddalar bilan (geterotrof)", ["Fotosintez bilan", "Xemosintez bilan", "Oziqlanmaydi"], "Xloroplast ishlamasa tayyor moddani oladi."),
    O(3, "Amyobaning suyuq oziqani yutish jarayoni nomini yozing.", ["pinotsitoz"], "Pinotsitoz — suyuqlik yutish."),
    O(3, "Evglenaning fotosintez qiluvchi organoidi nomini yozing.", ["xromatofor", "xromatoforalar", "xromatofora", "xloroplast"], "Xromatoforalar (xloroplastlar)."),
]

Q["B7.2"] = [
    C(1, "Infuzoriya-tufelka qanday harakatlanadi?", "Kirpikchalar yordamida", ["Xivchin yordamida", "Soxta oyoq yordamida", "Qanotlar yordamida"], "Infuzoriyalar kirpikchali."),
    C(1, "Tufelkada nechta yadro bor?", "Ikkita", ["Bitta", "Uchta", "Yadrosiz"], "Makro- va mikronukleus."),
    C(1, "Tufelkaning chiqarish teshigi qanday ataladi?", "Poroshitsa", ["Tsitostom", "Stigma", "Pellikula"], "Poroshitsa — chiqarish teshigi."),
    M(2, [("Makronukleus", "Moddalar almashinuvini boshqaradi"), ("Mikronukleus", "Ko'payishni boshqaradi"), ("Poroshitsa", "Chiqarish teshigi")], "Tufelka tuzilishi."),
    C(2, "Makronukleus qanday vazifani bajaradi?", "Vegetativ — moddalar almashinuvini boshqaradi", ["Generativ — ko'payishni boshqaradi", "Harakatni ta'minlaydi", "Fotosintez qiladi"], "Makronukleus vegetativ yadro."),
    C(2, "Mikronukleus qanday yadro?", "Generativ — ko'payishni boshqaradi", ["Vegetativ — metabolizmni boshqaradi", "Ayirish yadrosi", "Harakat yadrosi"], "Mikronukleus — generativ."),
    C(2, "Tufelkada hujayra og'zi qanday ataladi?", "Tsitostom", ["Poroshitsa", "Stigma", "Hif"], "Tsitostom — hujayra og'zi."),
    C(2, "Kon'yugatsiya natijasida nima o'zgaradi?", "Yadro almashinadi, irsiy xilma-xillik ortadi", ["Organizmlar soni ikki baravar ko'payadi", "Spora hosil bo'ladi", "Tsista hosil bo'ladi"], "Kon'yugatsiya — jinsiy jarayon, ko'payish emas."),
    C(3, "Kon'yugatsiya haqida qaysi tasdiq to'g'ri?", "Individlar soni ko'paymaydi, irsiy xilma-xillik ortadi", ["Individlar soni ortadi, irsiy xilma-xillik ortmaydi", "Individlar soni ortadi va xilma-xillik ortadi", "Faqat makronukleus almashinadi"], "Yadro almashinuvi bo'ladi."),
    O(3, "Tufelkaning jinsiy jarayoni nomini yozing.", ["kon'yugatsiya", "konyugatsiya", "kon`yugatsiya"], "Kon'yugatsiya."),
    O(3, "Tufelkada ko'payishni boshqaradigan yadro nomini yozing.", ["mikronukleus"], "Mikronukleus — generativ yadro."),
]

Q["B7.3"] = [
    C(1, "Jigar qurtining oraliq xo'jayini kim?", "Kichik hovuz shillig'i", ["Qoramol", "Odam", "Cho'chqa"], "Oraliq xo'jayin — shilliq."),
    C(1, "Ho'kiz tasmasining oraliq xo'jayini kim?", "Qoramol", ["Odam", "Kichik hovuz shillig'i", "It"], "Qoramol — oraliq xo'jayin."),
    C(1, "Ho'kiz tasmasining finnasi qayerda joylashadi?", "Qoramol mushaklarida", ["Odam ichagida", "Shilliq jigarida", "Suvda"], "Finna — mushaklarda."),
    M(2, [("Miratsidiy", "Kirpikli lichinka"), ("Tsarkariy", "Dumli lichinka"), ("Onkosfera", "6 ilgakli lichinka")], "Gijja lichinkalari."),
    C(2, "Jigar qurtining suvda tuxumdan chiqadigan kirpikli lichinkasi qaysi?", "Miratsidiy", ["Tsarkariy", "Onkosfera", "Finna"], "Miratsidiy shilliqqa kiradi."),
    C(2, "Jigar qurti tsarkariysi qayerda tsistaga aylanadi?", "O'simlik (o't) ustida", ["Odam jigarida", "Shilliq ichida", "Qoramol qonida"], "Tsista o'tda hosil bo'ladi."),
    C(2, "Onkosfera qanday lichinka?", "6 ilgakli lichinka", ["Dumli lichinka", "Kirpikli lichinka", "Qanotli lichinka"], "Onkosfera ichakda bo'ladi."),
    C(2, "Ho'kiz tasmasining asosiy xo'jayini kim?", "Odam (ichagida imago)", ["Qoramol", "Shilliq", "It"], "Imago odam ichagida yashaydi."),
    C(3, "Ho'kiz tasmasi rivojlanish zanjirining to'g'ri tartibini toping.", "Proglottida → tuxum → qoramol → onkosfera → finna → odam", ["Tuxum → odam → finna → onkosfera → qoramol", "Proglottida → finna → tuxum → qoramol → odam", "Tuxum → finna → onkosfera → qoramol → odam"], "Yetilgan bo'g'in tashqi muhitga tushadi, qoramol yutadi."),
    O(3, "Jigar qurti sikli: murtakli tuxumdan suvda chiqadigan kirpikli lichinka nomini yozing.", ["miratsidiy"], "Miratsidiy."),
    O(3, "Jigar qurtining tsistasi qayerda hosil bo'ladi? (bir-ikki so'z)", ["o'tda", "o't", "o'simlikda", "o'simlik"], "O'tda tsista hosil qiladi."),
]

Q["B7.4"] = [
    C(1, "Hasharotlarning yurish oyoqlari nechta juft?", "3 juft", ["4 juft", "5 juft", "2 juft"], "Hasharotlar — 6 ta oyoq."),
    C(1, "Qaysi sinfda mo'ylov bo'lmaydi?", "O'rgimchaksimonlar", ["Hasharotlar", "Qisqichbaqasimonlar", "Barchasida bor"], "O'rgimchaksimonlarda mo'ylov yo'q."),
    C(1, "Qisqichbaqasimonlar qanday nafas oladi?", "Jabra bilan", ["Traxeya bilan", "O'pka bilan", "Teri bilan"], "Jabra — suv bilan nafas."),
    M(2, [("Qisqichbaqasimonlar", "5 juft yurish oyog'i"), ("O'rgimchaksimonlar", "4 juft yurish oyog'i"), ("Hasharotlar", "3 juft yurish oyog'i")], "Yurish oyoqlari soni."),
    C(2, "Hasharotlar tanasi nechta bo'limdan iborat?", "3 (bosh, ko'krak, qorin)", ["2 (bosh-ko'krak, qorin)", "4", "1"], "Hasharotlar — 3 bo'lim."),
    C(2, "O'rgimchaksimonlarning ayirish a'zosi qaysi?", "Malpigi naychalari", ["Yashil bezlar", "Buyrak", "Nefridiy"], "Qisqichbaqasimonlarda — yashil bezlar."),
    C(2, "Hasharotlarning nafas olish a'zosi qaysi?", "Traxeya", ["Jabra", "O'pka", "Teri"], "Traxeyalar tizimi."),
    C(2, "Kapalak qanday o'zgarish bilan rivojlanadi?", "To'liq o'zgarish (tuxum → lichinka → g'umbak → imago)", ["Chala o'zgarish (tuxum → lichinka → imago)", "O'zgarishsiz", "Faqat tuxum → imago"], "Kapalak — to'liq o'zgarish."),
    C(3, "Hasharotlarning ayirish tizimiga nimalar kiradi?", "Malpigi naychalari va yog' tanachalari", ["Yashil bezlar", "Faqat buyrak", "Faqat jabra"], "Malpigi naychalari va yog' tanachalari."),
    O(3, "Qisqichbaqasimonlarning yurish oyoqlari jami nechta? (son)", ["10", "10 ta"], "5 juft = 10 ta."),
    O(3, "To'liq o'zgarish bilan rivojlanuvchi hasharotda lichinkadan keyingi bosqich nomini yozing.", ["g'umbak", "gumbak"], "Lichinka → g'umbak → imago."),
]

Q["B7.5"] = [
    C(1, "Baliq yuragi necha kamerali?", "2 kamerali", ["3 kamerali", "4 kamerali", "1 kamerali"], "1 bo'lmacha va 1 qorincha."),
    C(1, "Amfibiyalar yuragi necha kamerali?", "3 kamerali", ["2 kamerali", "4 kamerali", "1 kamerali"], "2 bo'lmacha, 1 qorincha."),
    C(1, "Qushlar yuragi necha kamerali?", "4 kamerali", ["3 kamerali", "2 kamerali", "5 kamerali"], "To'liq ajralgan."),
    M(2, [("Baliqlar", "2 kamerali yurak"), ("Amfibiyalar", "3 kamerali yurak"), ("Qushlar", "4 kamerali yurak")], "Yurak kameralari soni."),
    C(2, "Baliq yuragidan qanday qon oqadi?", "Faqat venoz qon", ["Faqat arterial qon", "Aralash qon", "Qon oqmaydi"], "Baliqlarda 1 qon aylanish doirasi."),
    C(2, "Amfibiyalarda nechta qon aylanish doirasi bor?", "2 ta", ["1 ta", "3 ta", "4 ta"], "Qorinchada qon aralashadi."),
    C(2, "Reptiliyalar yuragi qanday tuzilgan?", "3 kamerali, qorinchasida chala to'siq bor", ["2 kamerali", "4 kamerali, to'liq to'siqli", "3 kamerali, to'siqsiz"], "Timsoh bundan istisno."),
    C(2, "Timsohlar yuragida qon qayerda aralashadi?", "Panis teshigida (yurakdan tashqarida)", ["Bo'lmachada", "Qorinchada", "O'pkada"], "Yurak 4 kamerali, lekin qon Panis teshigida aralashadi."),
    C(3, "Qaysi aorta yoyi qushlarda, qaysi biri sutemizuvchilarda rivojlangan?", "Qushlarda o'ng, sutemizuvchilarda chap", ["Qushlarda chap, sutemizuvchilarda o'ng", "Ikkalasida ham o'ng", "Ikkalasida ham chap"], "Qush — o'ng yoy, sutemizuvchi — chap yoy."),
    O(3, "Timsohlar yuragida qon aralashadigan teshik nomini yozing.", ["panis", "panis teshigi", "panis teshigida"], "Panis teshigi."),
    O(3, "Baliqlarda nechta qon aylanish doirasi bor? (son)", ["1"], "Baliqlarda faqat bitta doira."),
]

Q["B7.6"] = [
    C(1, "Baliqlarning suv oqimini sezuvchi a'zosi qaysi?", "Yon chiziq", ["Ichki quloq", "Ko'z", "Burun"], "Yon chiziq suv oqimi va bosimini aniqlaydi."),
    C(1, "Reptiliyalar qanday ayirish mahsuloti chiqaradi?", "Siydik kislotasi", ["Mochevina", "Ammiak", "Glyukoza"], "Suvni tejash uchun."),
    C(1, "Qaysi sinfda diafragma mavjud?", "Sutemizuvchilar", ["Qushlar", "Reptiliyalar", "Amfibiyalar"], "Diafragma ko'krak va qorin bo'shlig'ini ajratadi."),
    M(2, [("Yon chiziq", "Baliqlar"), ("Havo xaltachalari", "Qushlar"), ("Diafragma", "Sutemizuvchilar")], "Sinfga xos belgilar."),
    C(2, "Qushlardagi ikki yoqlama nafas olish nima yordamida amalga oshadi?", "Havo xaltachalari", ["Diafragma", "Jabralar", "Nam teri"], "Parvoz paytida ham nafas oladi."),
    C(2, "Amfibiyalar teri orqali nafas olishi qancha foizgacha yetadi?", "50% gacha", ["10% gacha", "100%", "Teri nafas olmaydi"], "O'pka va nam teri orqali nafas oladi."),
    C(2, "Qushlarning suyaklari qanday?", "Pnevmatik (ichi havo bilan to'lgan)", ["Og'ir, to'la", "Xaftagaldan", "Yumshoq"], "Yengillik uchun."),
    C(2, "Reptiliyalar qanday organizmlar?", "Sovuqqonli", ["Issiqqonli (gomoyoterm)", "Doimiy harorat saqlaydi", "Faqat suvda yashaydi"], "Reptiliyalar — poykiloterm."),
    C(3, "Sutemizuvchilarga xos belgilar to'g'ri berilgan javobni toping.", "Chap aorta yoyi, diafragma, sut, ter va yog' bezlari", ["O'ng aorta yoyi, havo xaltachalari", "3 kamerali yurak, siydik kislotasi", "Yon chiziq va jabralar"], "Sutemizuvchilar belgilari."),
    O(3, "Reptiliyalarda suvni tejash uchun ajratiladigan modda nomini yozing.", ["siydik kislotasi"], "Siydik kislotasi."),
    O(3, "Qushlarning issiqqonligi uchun qo'llaniladigan termin nima? (bir so'z)", ["gomoyoterm", "gomoyotermlik", "gomoyoterm hayvonlar"], "Qushlar — gomoyoterm."),
]
