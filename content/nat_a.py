"""Ona tili va adabiyot: 5–6-sinf — leksikologiya, fonetika, orfografiya, morfemika, xalq og'zaki ijodi."""
from ._dsl import C, O, M

Q = {}

Q["N5.1"] = [
    C(1, "Faqat bitta ma'noga ega bo'lgan so'zlar qanday ataladi?", "Monosemantik (bir ma'noli)", ["Polisemantik", "Omonim", "Sinonim"], "Bir ma'noli so'zlar — monosemantik."),
    C(1, "Bir necha ma'noga ega bo'lgan so'z qanday ataladi?", "Ko'p ma'noli (polisemantik)", ["Bir ma'noli", "Shakldosh", "Zid ma'noli"], "Polisemiya."),
    C(2, "«Tilning ma'nosi» birikmasidagi «til» so'zining qaysi ma'nosi asl (tub) ma'no?", "Og'iz bo'shlig'idagi a'zo", ["Nutq", "Madaniyat", "Mamlakat tili"], "Asl ma'no — predmetning o'zini bildiradi."),
    C(2, "So'zning grammatik ma'nosi nimani ifodalaydi?", "So'z shakli orqali bildiriluvchi ma'no (son, kelishik, shaxs va b.)", ["So'zning lug'atdagi ma'nosini", "So'zning kelib chiqishini", "So'zning ohangini"], "Qo'shimchalar beradi."),
    C(2, "Qaysi qatorda faqat monosemantik so'zlar berilgan?", "olma, daftar, kosmonavt", ["bosh, til, ko'z", "yuz, qo'l, tosh", "ochiq, og'ir, qattiq"], "Bu so'zlar bitta ma'noni bildiradi."),
    C(2, "«Qo'l» so'zi qaysi gapda ko'chma ma'noda?", "Bu ishda uning qo'li bor.", ["Qo'lim sovuq qotdi.", "Qo'lini yuvdi.", "U qo'lini ko'tardi."], "«Ishtirok etmoq» ma'nosi — ko'chma."),
    C(3, "«Sovuq» so'zi qaysi birikmada ko'chma ma'noda ishlatilgan?", "sovuq munosabat", ["sovuq suv", "sovuq havo", "sovuq shamol"], "Kayfiyat/munosabat — ko'chma."),
    O(3, "«Ko'z» so'zi «Ignaning ko'zi» birikmasida qanday ma'noda qo'llangan? (asl yoki ko'chma deb yozing)", ["ko'chma", "ko'chma ma'no", "ko'chma ma'noda"], "Ignaning teshigi — o'xshashlik asosida ko'chma ma'no."),
    M(2, [("bir ma'noli so'z", "monosemantik"), ("ko'p ma'noli so'z", "polisemantik"), ("so'zning ma'no ko'chishi", "metafora, metonimiya, sinekdoxa")], "Leksik ma'no terminlari."),
]

Q["N5.2"] = [
    C(1, "O'xshashlik asosida ma'no ko'chishi qanday ataladi?", "Metafora", ["Metonimiya", "Sinekdoxa", "Omonimiya"], "Shakl, rang, harakat o'xshashligi."),
    C(1, "Qism orqali butunni ifodalash qanday ataladi?", "Sinekdoxa", ["Metafora", "Metonimiya", "Antiteza"], "«Besh qo'l barobar emas»."),
    C(2, "«Auditoriya kuldi» gapida qaysi ma'no ko'chishi bor?", "Metonimiya", ["Metafora", "Sinekdoxa", "Funksionallik"], "Joy nomi odamlar o'rnida (makon bog'liqligi)."),
    C(2, "«Oltin qo'llar» iborasida qaysi ma'no ko'chishi bor?", "Metafora", ["Metonimiya", "Sinekdoxa", "Omonimiya"], "Mohirlik «oltin» bilan o'xshatilgan."),
    C(2, "«Navoiyni o'qidim» gapida qaysi ma'no ko'chishi bor?", "Metonimiya", ["Metafora", "Sinekdoxa", "Funksionallik"], "Muallif nomi asar o'rnida."),
    C(2, "«Qozon qaynab chiqdi» jumlasida «qozon» so'zi...", "ichidagi ovqat ma'nosida (metonimiya)", ["shakl o'xshashligi bilan (metafora)", "qism-butun (sinekdoxa)", "asl ma'noda faqat"], "Idish nomi mazmun o'rnida."),
    C(3, "«Shahar tinch uxladi» gapida qaysi ma'no ko'chishi bor?", "Sinekdoxa (butun orqali qism)", ["Metafora", "Metonimiya faqat", "Funksionallik"], "Shahar — aholi."),
    O(3, "«Yer yutsin» dagi emas; «Daryo shovqin soldi» — «yosh dehqon qo'lini oldi»... Quyidagi ma'no ko'chishini yozing: «Bola burgutday uchdi» (so'z: metafora/metonimiya/sinekdoxa)", ["metafora"], "O'xshatishga asoslangan.") if False else O(3, "«Oltin kuz» birikmasidagi «oltin» so'zida qaysi ma'no ko'chishi bor? (bir so'z bilan)", ["metafora"], "Rang o'xshashligi asosida ko'chish."),
    M(2, [("Metafora", "o'xshashlik asosida ko'chish"), ("Metonimiya", "bog'liqlik asosida ko'chish"), ("Sinekdoxa", "qism-butun munosabati")], "Ma'no ko'chish turlari."),
]

Q["N5.3"] = [
    C(1, "Shakli bir xil, ma'nosi har xil so'zlar...", "omonimlar", ["sinonimlar", "antonimlar", "paronimlar"], "Shakldosh so'zlar."),
    C(1, "Qaysi qatorda omonimlar berilgan?", "o't (olov) — o't (o'simlik)", ["katta — kichik", "yurmoq — bormoq", "baland — past"], "Bir xil yoziladi, ma'nosi boshqa."),
    C(2, "«Ot» (hayvon) va «ot» (so'z turkumi) so'zlari...", "omonim", ["sinonim", "antonim", "paronim"], "Shakldosh."),
    C(2, "Talaffuzi bir xil, imlosi farqli so'zlar...", "gomofonlar", ["gomograflar", "sinonimlar", "antonimlar"], "Masalan: «tonna — tanna»."),
    C(2, "Yozilishi bir xil, urg'usi bilan farqlanadigan so'zlar...", "gomograflar", ["gomofonlar", "omofonlar faqat", "paronimlar"], "Masalan: «olma» (meva) — «olma» (olmoq fe'li)."),
    C(2, "«Tuz» so'zi turli ma'noda ishlatilgan gapni toping (omonim).", "Tuz ovqatga ta'm beradi. — Tuz, to'g'ri chiziq chiz.", ["Ota keldi. — Ona keldi.", "Katta uy — kichik uy.", "Qora qalam — oq qalam."], "«Tuz» (tuzmoq) fe'li va ot omonimi."),
    C(3, "Nisbiy omonimlar...", "turli so'z turkumlariga mansub shakldosh so'zlar", ["bir turkumga mansub shakldosh so'zlar", "ma'nodosh so'zlar", "qarama-qarshi so'zlar"], "Mutloq omonimlar — bir turkum."),
    C(3, "Mutloq omonimlar...", "bir so'z turkumiga mansub shakldosh so'zlar", ["turli so'z turkumlarida", "faqat ot va sifat", "faqat fe'llar"], "Masalan: o't — o't (ikkalasi ot)."),
    O(3, "Shakli bir xil, ma'nolari esa turlicha bo'lgan so'zlar nima deb ataladi? (bir so'z)", ["omonimlar", "omonim", "shakldosh"], "Omonimlar."),
]

Q["N5.4"] = [
    C(1, "Ma'nosi yaqin so'zlar qanday ataladi?", "Sinonimlar", ["Antonimlar", "Omonimlar", "Paronimlar"], "Ma'nodosh so'zlar."),
    C(1, "Zid ma'noli so'zlar qanday ataladi?", "Antonimlar", ["Sinonimlar", "Omonimlar", "Paronimlar"], "Qarama-qarshi."),
    C(1, "«Katta» so'zining antonimi?", "kichik", ["ulkan", "yirik", "bahaybat"], "Kichik — zid."),
    C(2, "Qaysi qator sinonimik uyani tashkil qiladi?", "chiroyli, go'zal, ko'rkam, xushro'y", ["chiroyli, xunuk, kelishgan", "uy, imorat, toshbo'ron", "katta, kichik, qisqa"], "Ma'nodosh so'zlar."),
    C(2, "Sinonimik qatordagi asosiy (etakchi) so'z nima deyiladi?", "Dominanta", ["Epitet", "Metafora", "Antonim"], "Ma'nosi eng umumiy, uslubiy betaraf."),
    C(2, "Qaysi juftlik antonim emas?", "tez — shiddatli", ["tez — sekin", "issiq — sovuq", "kecha — bugun? (kecha — ertaga)"], "«Tez — shiddatli» sinonim.") if False else C(2, "Qaysi juftlik antonim emas?", "tez — shiddatli", ["tez — sekin", "issiq — sovuq", "ochiq — yopiq"], "«Tez — shiddatli» sinonimlar."),
    C(2, "«Ko'tarmoq — olmoq — tutmoq» qatori so'z turkumiga ko'ra...", "fe'llar", ["otlar", "sifatlar", "ravishlar"], "Fe'l sinonimlari."),
    O(3, "«Yaxshi» so'zining antonimini yozing.", ["yomon"], "Yaxshi — yomon."),
    O(3, "«Do'st» so'zining antonimini yozing.", ["dushman", "yov"], "Do'st — dushman."),
    M(2, [("keng", "tor"), ("baland", "past"), ("to'g'ri", "egri")], "Antonimlar."),
]

Q["N5.5"] = [
    C(1, "Talaffuzi yaqin, lekin ma'nosi va imlosi farqli so'zlar...", "paronimlar", ["omonimlar", "sinonimlar", "antonimlar"], "Paronim — «yaqin nom»."),
    C(2, "«Surat» va «sur'at» so'zlari...", "paronimlar: surat — rasm, sur'at — tezlik", ["sinonimlar", "omonimlar", "bir so'zning variantlari"], "Ma'nolari farqli."),
    C(2, "«Shoir» va «shior» ma'nolari?", "shoir — she'r yozuvchi; shior — chaqiriq", ["ikkalasi bir ma'noda", "shoir — chaqiriq; shior — yozuvchi", "ikkalasi she'r yozuvchi"], "Paronimlar."),
    C(2, "Qaysi gapda «muallif» so'zi to'g'ri qo'llangan?", "Bu kitobning muallifi mashhur yozuvchi.", ["Muallifimiz darsga keldi, bizni o'qitdi.", "Maktabda muallif dars beradi.", "Muallif sinfimizga kirdi, matematikadan dars o'tdi."], "Muallif — asar egasi, muallim — o'qituvchi."),
    C(2, "«Qadam» va «qadim» so'zlari...", "paronimlar", ["omonimlar", "sinonimlar", "antonimlar"], "Qadam — oyoq tashlash, qadim — juda eski."),
    C(3, "Bo'sh joyga mos so'zni tanlang: «Bu ... shahar asrlar davomida saqlanib kelgan.»", "qadimiy", ["qadamiy", "qadamdosh", "qadimchilik"], "Qadimiy — eski, qadimdan qolgan."),
    C(3, "«Ma'rifat» so'zining ma'nosi?", "bilimdonlik, ilm-fan va madaniyatni egallash", ["tezlik", "hurmat", "mehnat"], "Ma'rifat — ilm, ziyo."),
    O(3, "«Sur'at» so'zining ma'nosini bir so'z bilan yozing (tezlik ma'nosida).", ["tezlik"], "Sur'at — tezlik, surat — rasm."),
    O(3, "Gapni to'ldiring: «Poyezd katta ... bilan harakatlandi» (surat yoki sur'at).", ["sur'at", "sur’at", "sur`at"], "Tezlik ma'nosida — sur'at."),
]

Q["N5.6"] = [
    C(1, "O'zbek tili leksikasining asosiy (o'z) qatlami qaysi tillardan kelib chiqqan?", "Turkiy tillar", ["Arab tili", "Fors tili", "Rus tili"], "O'z qatlam — turkiy ildiz."),
    C(1, "Qaysi so'z arabcha o'zlashma?", "kitob", ["maktab? (arabcha)", "daftar (forscha)", "ona"], "«Kitob» arab tilidan kirgan.") if False else C(1, "Qaysi so'z arabcha o'zlashma?", "kitob", ["ona", "qo'y", "ko'z"], "«Kitob» — arabcha."),
    C(2, "Qaysi so'z forscha-tojikcha o'zlashma?", "daftar", ["bola", "tosh", "tog'"], "«Daftar» — fors tilidan."),
    C(2, "Qaysi qatorda faqat o'z qatlamga oid so'zlar berilgan?", "tosh, suv, ot, tog'", ["maktab, kitob, qalam", "traktor, telefon, radio", "daryo, bozor, dunyo"], "Turkiy ildizli so'zlar."),
    C(2, "«Televizor», «telefon», «radio» so'zlari qaysi qatlamga mansub?", "Baynalmilal (rus tili orqali kirgan) so'zlar", ["O'z qatlam", "Arabcha", "Forscha"], "Yevropa tillaridan."),
    C(3, "Qaysi so'z o'z qatlamga mansub?", "ko'k", ["maktab", "daftar", "olam"], "Ko'k — turkiy so'z."),
    C(3, "O'zlashgan so'z odatda qanday belgi bilan aniqlanadi?", "Ildizi boshqa tildan, fonetik/morfologik belgilari tilimizga moslashgan", ["Hamisha qo'shimchasiz", "Faqat bir bo'g'inli", "Faqat unli bilan boshlanadi"], "Etimologiya."),
    O(3, "«Maktab» so'zi qaysi tildan kirgan? (til nomini yozing)", ["arab", "arab tili", "arabcha"], "Arabcha — maktab."),
    O(3, "«Osmon» so'zi qaysi tildan kirgan? (forscha — fors yoki tojik)", ["fors", "forscha", "fors tili", "tojik", "fors-tojik", "forscha-tojikcha"], "Osmon — forscha."),
]

Q["N5.7"] = [
    C(1, "Ma'nosi eskirgan, lekin predmet nomi o'zgarib qolgan so'zlar...", "arxaizmlar", ["istorizmlar", "neologizmlar", "jargon"], "Predmet bor, nomi o'zgargan."),
    C(1, "Predmetning o'zi hayotdan chiqib ketgani uchun eskirgan so'zlar...", "istorizmlar", ["arxaizmlar", "neologizmlar", "terminlar"], "Masalan: «mingboshi»."),
    C(2, "«Mirzo» (kotib) so'zi qaysi guruhga kiradi?", "Istorizm", ["Arxaizm", "Neologizm", "Jargon"], "Eski mansab — hayotdan chiqqan."),
    C(2, "Yangi paydo bo'lgan so'zlar nima deyiladi?", "Neologizmlar", ["Arxaizmlar", "Istorizmlar", "Frazeologizmlar"], "Masalan: «internet»."),
    C(2, "Qo'pol so'zlar o'rniga ishlatiladigan yumshoq iboralar...", "evfemizmlar", ["tabu", "jargonlar", "arxaizmlar"], "«Vafot etdi» — «o'ldi» o'rnida."),
    C(2, "Qaysi gapda evfemizm bor?", "Bobom vafot etdilar.", ["Bobom o'ldi.", "Bobom keldi.", "Bobom yuribdi."], "Yumshatilgan ifoda."),
    C(3, "Muayyan kasb egalariga xos so'zlar...", "professionalizmlar", ["jargonlar", "arxaizmlar", "evfemizmlar"], "Masalan: «kardiogramma» (shifokorlar)."),
    O(3, "«Bek» so'zi qaysi turdagi eskirgan so'z (istorizm yoki arxaizm)?", ["istorizm"], "Mansab nomi — hayotdan chiqqan."),
    O(3, "«Mehmonxona» ma'nosida eskirgan «sarob?» emas: «Ko'ngilsiz xabarni yumshoq aytish» usuli nima? (bir so'z)", ["evfemizm"], "Evfemizm.") if False else O(3, "Yumshatib aytilgan ifodalar nima deb ataladi? (bir so'z)", ["evfemizm", "evfemizmlar"], "Evfemizm."),
]

Q["N5.8"] = [
    C(1, "Frazeologizm (ibora) nima?", "Ko'chma ma'noli, barqaror so'z birikmasi", ["Erkin so'z birikmasi", "Gap", "Bir so'z"], "Yaxlit ma'no beradi."),
    C(1, "«Ko'z yummoq» iborasi qanday ma'noda?", "e'tibor bermaslik, kechirmoq", ["uxlamoq (aniq ma'no)", "ko'rmoq", "yig'lamoq"], "Ko'chma."),
    C(2, "«Og'zi qulog'ida» iborasining ma'nosi?", "juda xursand", ["jahli chiqqan", "uyqusi kelgan", "och qolgan"], "Frazeologizm."),
    C(2, "Maqol va ibora o'rtasidagi farq?", "Maqol — tugal fikr beruvchi gap; ibora — gap bo'lagi", ["Farq yo'q", "Ibora — gap, maqol — so'z", "Maqol ko'chma ma'noli emas"], "Ibora gapning bir bo'lagi bo'lib keladi."),
    C(2, "Frazeologizmning gapdagi vazifasi...", "gapda odatda bitta bo'lak bo'lib keladi", ["har doim ega bo'ladi", "bog'lovchi bo'ladi", "faqat kesim bo'ladi"], "Yaxlit."),
    C(3, "«Ko'ngli ochildi» iborasining sinonimi?", "xursand bo'ldi", ["jahli chiqdi", "xafa bo'ldi", "uxlab qoldi"], "Ma'nodosh ibora."),
    C(3, "«Qo'li ochiq» iborasining antonimi?", "qo'li qisiq (xasis)", ["qo'li gul", "qo'li uzun", "qo'li egri"], "Saxiy — xasis."),
    O(3, "«Yetti o'lchab, bir kes» — bu nima (maqol yoki ibora)?", ["maqol"], "Tugal fikr — maqol."),
    O(3, "«Boshi osmonga yetdi» — nima? (ibora yoki maqol)", ["ibora"], "Ibora."),
]

Q["N5.9"] = [
    C(1, "Xalq og'zaki ijodining janrlaridan biri?", "Ertak", ["Roman", "Qissa", "Drama"], "Ertak — og'zaki janr."),
    C(1, "Ertaklarning asosiy turlari?", "Hayvonlar haqidagi, sehrli va maishiy ertaklar", ["Faqat sehrli ertaklar", "Faqat tarixiy ertaklar", "Lirik ertaklar faqat"], "Uch xil tasnif."),
    C(2, "Maqol — bu...", "xalq donoligini ifodalovchi, tugallangan fikrni beruvchi qisqa ibora", ["uzun hikoya", "she'riy asar", "drama"], "Janr."),
    C(2, "Topishmoq nima?", "Predmet yoki hodisa yashirin tasvirlangan, topish talab qilinadigan janr", ["Doston", "Qo'shiq", "Latifa"], "Savol-javob."),
    C(2, "Latifa nima?", "Qisqa, kulgili hikoya", ["Uzun doston", "Qasida", "Fojia"], "Hajviy janr."),
    C(2, "Rivoyat va afsona orasidagi umumiy belgi?", "Xalq orasida og'zaki tarqalgan, haqiqatga o'xshash hikoyalar", ["Hammasi she'r bilan yozilgan", "Faqat hayvonlar haqida", "Mualliflari ma'lum"], "Og'zaki."),
    C(3, "«Yaxshi so'z — jon ozig'i» qaysi janrga mansub?", "Maqol", ["Topishmoq", "Ertak", "Aytim"], "Tugal fikr."),
    O(3, "«Oltin tojli qush» qanday ertak — hayvonlar haqidagimi yoki sehrlimi? (bir so'z: sehrli)", ["sehrli"], "Sehrli ertak.") if False else O(3, "Xalq og'zaki ijodi asarlari bir so'z bilan qanday ataladi? (folklor)", ["folklor", "xalq og'zaki ijodi"], "Folklor."),
    M(2, [("Maqol", "tugal fikr beruvchi qisqa gap"), ("Topishmoq", "yashirin tasvirlangan savol"), ("Doston", "qahramonlik haqida yirik epik asar")], "Folklor janrlari."),
]

Q["N6.1"] = [
    C(1, "O'zbek tilida nechta unli tovush bor?", "6 ta", ["5 ta", "8 ta", "10 ta"], "a, o, u, e, i, o'."),
    C(1, "Faol nutq a'zolariga qaysilar kiradi?", "til, lablar, ovoz pardalari", ["tishlar, tanglay", "burun, tish", "tanglay, milk"], "Harakatlanuvchi a'zolar."),
    C(2, "Lablangan unlilar qaysi qatorda?", "o, o', u", ["a, e, i", "i, e, a", "a, i, u"], "Lab dumaloqlanadi."),
    C(2, "Til oldi unlilari qaysilar?", "i, e", ["u, o'", "a, o", "o, u"], "Til oldiga siljiydi."),
    C(2, "Yuqori (tor) unlilarni toping.", "i, u", ["a, o", "e, o'", "a, e"], "Til yuqoriga ko'tariladi."),
    C(2, "Quyi (keng) unlilarni toping.", "a, o", ["i, u", "e, o'", "i, e"], "Og'iz keng ochiladi."),
    C(3, "Quyidagi so'zlarning qaysi birida barcha unlilar lablangan?", "bo'lmoq? (o', o)", ["sinf", "kitob", "olma"], "o'zbek? — qiyosiy savol.") if False else C(3, "Qaysi so'zda faqat lablangan unlilar qatnashgan?", "to'p", ["bola", "kitob", "oila"], "«To'p» — o' lablangan; «bola» — o va a (a lablanmagan)."),
    O(3, "«Bo'g'in» so'zida nechta unli tovush bor? (raqam bilan)", ["2"], "o', i — ikkita."),
    O(3, "«Ona» so'zida nechta unli bor? (raqam)", ["2"], "o, a — ikkita."),
]

Q["N6.2"] = [
    C(1, "Jarangli undoshlar qaysi qatorda?", "b, d, g, z", ["p, t, k, s", "s, sh, x, f", "q, h, ch, p"], "Ovoz ishtirokida."),
    C(1, "Jarangsiz undoshlar qaysi qatorda?", "p, t, k, s", ["b, d, g, z", "m, n, l, r", "v, y, j, z"], "Shovqin ko'p."),
    C(2, "Sonor undoshlar qaysilar?", "m, n, l, r, ng", ["b, d, g", "s, sh, x", "p, t, k"], "Ovoz ko'p, shovqin kam."),
    C(2, "«B» undoshining jarangsiz jufti?", "p", ["t", "k", "s"], "b–p."),
    C(2, "«D» undoshining jarangsiz jufti?", "t", ["p", "k", "s"], "d–t."),
    C(2, "Hosil bo'lish usuliga ko'ra portlovchi undoshlar?", "b, p, d, t, g, k, q", ["s, z, sh", "m, n, ng", "l, r"], "Yopiq to'siq portlaydi."),
    C(3, "Qaysi undosh juftsiz jarangsiz?", "h", ["p", "t", "s"], "H — juftsiz."),
    C(3, "«Ng» harf birikmasi nechta tovush?", "1 ta (bitta tovush)", ["2 ta", "3 ta", "unli"], "Sonor undosh."),
    O(3, "«Sh» tovushi qaysi harf birikmasi? Savol: «tong» so'zida nechta undosh tovush bor? (raqam)", ["2"], "t, ng — ikkita.") if False else O(3, "«Tong» so'zida nechta tovush bor? (raqam)", ["3"], "t, o, ng — 3 ta tovush."),
]

Q["N6.3"] = [
    C(1, "So'zdagi tovushning tushib qolishi hodisasi...", "eliziya", ["epenteza", "assimilyatsiya", "metateza"], "Tovush tushishi."),
    C(1, "So'zda tovush orttirilishi hodisasi...", "epenteza", ["eliziya", "assimilyatsiya", "metateza"], "Tovush ortishi."),
    C(2, "«Singil + i → singli» da qanday hodisa?", "Unli tovush tushishi (eliziya)", ["Tovush ortishi", "Undosh almashishi", "Tovush o'rin almashishi"], "i tushgan."),
    C(2, "«Fikr → fikir» da...", "epenteza (tovush ortishi)", ["eliziya", "assimilyatsiya", "metateza"], "Unli orttirilgan."),
    C(2, "«Ketdi → ketti» da...", "assimilyatsiya (jarangsizlanish)", ["eliziya", "epenteza", "metateza"], "d → t."),
    C(2, "«Tuzsiz → tussiz» da...", "assimilyatsiya", ["eliziya", "epenteza", "g'ayri tovush"], "z → s."),
    C(3, "Qaysi so'zda tovush tushishi bor?", "og'zi", ["kitobi", "qalamda", "daftar"], "og'iz → og'zi."),
    O(3, "«Parvo» so'ziga egalik qo'shimchasi qo'shilganda «parvoyi» shakli hosil bo'ladi. Bu qanday fonetik hodisa? (bir so'z)", ["epenteza", "tovush ortishi", "undosh ortishi"], "Undosh tovush ortgan."),
    O(3, "«Burun» so'ziga -i egalik qo'shimchasi qo'shilganda «burni» bo'ladi. Bu qanday fonetik hodisa? (bir so'z)", ["eliziya", "unli tushishi", "tovush tushishi"], "Unli tushgan."),
]

Q["N6.4"] = [
    C(1, "Bo'g'in nima?", "Bir nafasda aytiladigan tovush yoki tovushlar guruhi", ["Faqat undosh", "So'z", "Ikki so'z"], "Unli bo'g'in hosil qiladi."),
    C(1, "Unli bilan tugagan bo'g'in qanday ataladi?", "Ochiq bo'g'in", ["Yopiq bo'g'in", "O'ta yopiq bo'g'in", "Sof bo'g'in"], "Masalan: o-na."),
    C(2, "«Maktab» so'zi nechta bo'g'inga bo'linadi?", "2 ta (mak-tab)", ["3 ta", "1 ta", "4 ta"], "mak-tab."),
    C(2, "«Kitob» so'zini bo'g'inga ajrating.", "ki-tob", ["kit-ob", "k-itob", "kito-b"], "Ochiq + yopiq."),
    C(2, "Urg'u o'zbek tilida odatda qayerga tushadi?", "Oxirgi bo'g'inga", ["Birinchi bo'g'inga", "Ikkinchi bo'g'inga", "Har xil"], "Odatda so'zning oxirgi bo'g'ini."),
    C(2, "Urg'u qabul qilmaydigan qo'shimchalar?", "Kelishik, shaxs-son, yuklama va ba'zi shakl qo'shimchalari", ["Hamma qo'shimcha", "Faqat so'z yasovchilar", "Hech qaysi"], "Urg'u qo'shimchaga o'tmaydi."),
    C(3, "Satrdan satrga ko'chirishda to'g'ri variant?", "mak-tab", ["m-aktab", "makt-ab", "ma-ktab"], "Bo'g'in bo'yicha."),
    O(3, "«Maktabimiz» so'zi nechta bo'g'inga ega? (raqam)", ["4"], "mak-ta-bi-miz."),
    O(3, "«Uyqu» so'zi nechta bo'g'in? (raqam)", ["2"], "uy-qu."),
    M(2, [("ochiq bo'g'in", "unli bilan tugaydi"), ("yopiq bo'g'in", "undosh bilan tugaydi"), ("urg'u", "bo'g'inning kuchli aytilishi")], "Bo'g'in va urg'u."),
]

Q["N6.5"] = [
    C(1, "Bosh harf bilan yoziladigan so'z?", "Toshkent", ["maktab", "ko'cha", "daryo (umumiy)"], "Atoqli otlar."),
    C(1, "Juft so'z to'g'ri yozilgan qatorni toping.", "ota-ona", ["ota ona", "otaona", "ota_ona"], "Juft so'z chiziqcha bilan."),
    C(2, "Geografik nom to'g'ri yozilgan variantni toping.", "Qizilqum cho'li", ["Qizilqum-cho'li", "Qizilqumcho'li", "Qizil qum cho'li"], "Geografik nomning o'zagi bosh harf, turdosh qismi kichik."),
    C(2, "Takroriy so'z qaysi qatorda to'g'ri yozilgan?", "asta-asta", ["asta asta", "astaasta", "asta,asta"], "Chiziqcha bilan."),
    C(2, "Qo'shma so'z qo'shib yozilgan variantni toping.", "kitobxon", ["kitob xon", "kitob-xon", "kitob_xon"], "-xon komponentli qo'shma."),
    C(2, "«nim-» qismli so'zning to'g'ri yozilishini toping.", "nimqorong'i", ["nim-qorong'i", "nim qorong'i", "nimqorongi"], "nim- qo'shib yoziladi (nimqorong'i)."),
    C(3, "Qaysi qatorda barcha so'zlar to'g'ri yozilgan?", "kecha-kunduz, bog'bon, Navoiy ko'chasi", ["kecha kunduz, bog' bon, navoiy ko'chasi", "kechakunduz, bog'-bon, Navoiy Ko'chasi", "kecha-kunduz, bog' bon, Navoiy Ko'chasi"], "Juft — chiziqcha; qo'shma — qo'shib; ko'cha nomi kichik."),
    C(2, "Quyidagi so'zlardan qaysi biri doim bosh harf bilan yoziladi?", "Samarqand", ["shahar", "viloyat", "daryo"], "Atoqli ot (joy nomi) bosh harf bilan yoziladi."),
    O(3, "«ota ona» juft so'zini imlo qoidasiga ko'ra to'g'ri yozing.", ["ota-ona"], "Juft so'z chiziqcha bilan yoziladi."),
    O(3, "«tez tez» takroriy so'zini imlo qoidasiga ko'ra to'g'ri yozing.", ["tez-tez"], "Takroriy so'z chiziqcha bilan yoziladi."),
]

Q["N6.6"] = [
    C(1, "Qaysi so'z to'g'ri yozilgan?", "ma'no", ["mano", "ma'no? (to'g'ri)", "ma`no yoki"], "Tutuq belgisi kerak.") if False else C(1, "Tutuq belgisi to'g'ri qo'yilgan so'zni toping (1).", "ma'no", ["mano", "ma-no", "ma'-no"], "«ma'no» — tutuq belgisi bilan."),
    C(1, "Tutuq belgisi to'g'ri qo'yilgan so'zni toping (2).", "she'r", ["sher", "shi'r", "she-r"], "«she'r» — tutuq belgisi bilan."),
    C(2, "Qaysi so'z h harfi bilan to'g'ri yozilgan?", "hayot", ["xayot", "xaiot", "ayot"], "Hayot."),
    C(2, "Qaysi so'z x harfi bilan to'g'ri yozilgan?", "xalq", ["halq", "alq", "xalk"], "Xalq."),
    C(2, "«Javobgar» ma'nosidagi so'zning to'g'ri yozilishi qaysi?", "mas'ul", ["masul", "mas-ul", "mas'ul'"], "Mas'ul."),
    C(2, "«O'qitish» ma'nosidagi so'zning to'g'ri yozilishi qaysi?", "ta'lim", ["talim", "ta-lim", "ta'lim'"], "Ta'lim."),
    C(3, "h va x harflari to'g'ri qo'llangan qatorni toping.", "hurmat, xursand, mahalla, tahlil", ["xurmat, hursand, maxalla, taxlil", "hurmat, hursand, mahalla, taxlil", "xurmat, xursand, mahalla, tahlil"], "h/x."),
    O(3, "«Xursand» so'zi qaysi harf bilan boshlanadi? (x yoki h)", ["x"], "Xursand — x bilan."),
    O(3, "Quyidagi so'zni to'g'ri yozing: «mo''jiza» yoki «mojiza»? To'g'ri shaklini yozing.", ["mo''jiza", "moʼʼjiza"], "Tutuq belgisi ikki marta (mo''jiza)."),
]

Q["N6.7"] = [
    C(1, "Morfema nima?", "So'zning ma'noli eng kichik qismi", ["Gap", "So'z birikmasi", "Bo'g'in"], "Tub va qo'shimcha."),
    C(1, "So'zning asosiy ma'nosini ifodalovchi qismi...", "o'zak (tub morfema)", ["qo'shimcha", "affiks", "kesim"], "O'zak."),
    C(2, "«Kitobxon» so'zida o'zak nima?", "kitob va xon", ["faqat kitob", "faqat xon", "ki"], "Qo'shma so'z — ikki o'zak."),
    C(2, "So'z yasovchi qo'shimcha qaysi so'zda?", "ishchi", ["ishlar", "ishim", "ishga"], "-chi — yangi so'z yasaydi."),
    C(2, "Shakl yasovchi qo'shimcha qaysi so'zda?", "kitoblar", ["kitobchi", "kitobxon", "kitobot"], "-lar — son shakli."),
    C(2, "«Dehqonchilik» so'zining tarkibi?", "dehqon + chilik", ["deh + qonchilik", "dehqonchi + lik", "de + hqon"], "O'zak + so'z yasovchi."),
    C(3, "«Maktabdoshlarimizning» so'zida nechta qo'shimcha bor?", "4 ta (-dosh, -lar, -imiz, -ning)", ["2 ta", "3 ta", "5 ta"], "maktab-dosh-lar-imiz-ning."),
    O(3, "«Yozuvchilar» so'zining o'zagini yozing.", ["yoz"], "yoz-uv-chi-lar."),
    O(3, "«O'qituvchilarimiz» so'zining o'zagini yozing.", ["o'qi", "o'q"], "o'qi-t-uvchi-lar-imiz (o'zak o'qi)."),
]

Q["N6.8"] = [
    C(1, "«Alpomish» qanday asar?", "Xalq qahramonlik dostoni", ["Roman", "Drama", "Hikoya"], "Qo'shiqchi-baxshilar aytadi."),
    C(1, "Alpomishning oti?", "Boychibor", ["Ko'kdo'lan", "Qorabayir", "Girko'k"], "Boychibor."),
    C(1, "Alpomishning rafiqasi kim?", "Barchin", ["Gulbahor", "Oysuluv", "Zebi"], "Barchinoy."),
    C(2, "Alpomish dostoni asosan qaysi mavzuni tarannum etadi?", "Vatanparvarlik, qahramonlik, sadoqat", ["Tijorat", "Sayohat", "Faqat sevgi"], "El-yurt birligi."),
    C(2, "Dostonlarni xalqqa kuylab beruvchilar kimlar?", "Baxshilar", ["Hofizlar", "Kotiblar", "Dramaturglar"], "Xalq baxshilari."),
    C(2, "«Go'ro'g'li» turkumiga kiruvchi doston?", "Yovvoyi kiyik", ["Alpomish", "Layli va Majnun", "Xamsa"], "«Yovvoyi kiyik» — Go'ro'g'li turkumi."),
    C(3, "Alpomishning o'g'li kim?", "Yodgor", ["Hasan", "Qultoy", "Qorajon"], "Yodgor."),
    O(3, "Alpomishning otining nomini yozing.", ["boychibor"], "Boychibor."),
    O(3, "«Alpomish» dostonida Barchinning otasi kim? Savol: «Alpomish» qaysi xalq doston turiga kiradi? (qahramonlik — bir so'z)", ["qahramonlik"], "Qahramonlik dostoni.") if False else O(3, "«Alpomish» qaysi turdagi doston: qahramonlik yoki ishqiy? (bir so'z)", ["qahramonlik"], "Qahramonlik dostoni."),
]
