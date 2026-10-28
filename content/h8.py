"""8-sinf: Rivojlangan o'rta asrlar (XI–XV asrlar) — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["8.1.1"] = [
    C(1, "G'aznaviylar davlatining poytaxti qaysi shahar?", "G'azna", ["Buxoro", "Marv", "Nishopur"], "Hozirgi Afg'onistonda.", b="siyosiy"),
    C(1, "G'aznaviylar davlatiga asos solgan Somoniylar sarkardasi kim?", "Alp Tegin", ["Mahmud", "Mas'ud", "Tug'rulbek"], "Alp Tegin (962).", b="siyosiy"),
    C(1, "G'aznaviylarning eng mashhur hukmdori kim?", "Mahmud G'aznaviy", ["Subuktegin", "Mas'ud", "Alp Arslon"], "998–1030.", b="siyosiy"),
    C(2, "Mahmud G'aznaviy Hindistonga necha marta yurish qilgan?", "17 marta", ["3 marta", "7 marta", "30 marta"], "17 yurish.", b="siyosiy"),
    C(2, "Abu Rayhon Beruniy Hindistonga qaysi hukmdor bilan borgan?", "Mahmud G'aznaviy", ["Alp Arslon", "Ulug'bek", "Temur"], "«Hindiston» asari.", b="madaniyat"),
    C(2, "Firdavsiy «Shohnoma»ni kimga bag'ishlagan?", "Mahmud G'aznaviyga", ["Malikshohga", "Ismoil Somoniyga", "Nasr ibn Ahmadga"], "1010.", b="madaniyat"),
    C(3, "G'aznaviylar davlati qaysi yilda Dandanaqanda mag'lub bo'lgan?", "1040-yilda", ["1017-yilda", "1141-yilda", "1220-yilda"], "Mas'ud.", b="siyosiy"),
    O(3, "G'aznaviylar davlati asoschisining ismini yozing (A... T...).", ["Alp Tegin", "Alptegin", "Alp tegin"], "Alp Tegin.", b="siyosiy"),
]

Q["8.1.2"] = [
    C(1, "Saljuqiylar imperiyasining asoschilari qaysi aka-uka?", "Tug'rulbek va Chag'ribek", ["Alp Arslon va Malikshoh", "Mahmud va Mas'ud", "Atsiz va Tekesh"], "Tug'rulbek va Chag'ribek.", b="siyosiy"),
    C(1, "Dandanaqan jangi qaysi yilda bo'lgan?", "1040-yilda", ["1141-yilda", "1218-yilda", "1365-yilda"], "1040.", b="siyosiy"),
    C(1, "Dandanaqan jangida kim mag'lub bo'lgan?", "G'aznaviylar (Mas'ud)", ["Saljuqiylar", "Qoraxoniylar", "Somoniylar"], "Mas'ud G'aznaviy.", b="siyosiy"),
    C(2, "Malazgirt jangi (1071) da Vizantiya imperatorini asir olgan Saljuqiy sultoni?", "Alp Arslon", ["Malikshoh", "Sanjar", "Tug'rulbek"], "Roman Diogen.", b="siyosiy"),
    C(2, "Saljuqiylar davrida mashhur vazir kim?", "Nizomulmulk", ["Rashididdin", "Maniax", "Muqanna"], "Nizomiya madrasalari.", b="siyosiy"),
    C(2, "Jaloliy taqvimi qaysi hukmdor davrida joriy qilingan?", "Malikshoh", ["Alp Arslon", "Sanjar", "Ulug'bek"], "Umar Xayyom, 1079.", b="madaniyat"),
    C(3, "Saljuqiylar sultoni Tug'rulbek Bag'dodni qaysi yili egallagan?", "1055-yilda", ["1040-yilda", "1071-yilda", "1141-yilda"], "1055.", b="siyosiy"),
    O(3, "Dandanaqan jangi qaysi yilda bo'lgan? (raqam)", ["1040", "1040-yil"], "1040.", b="siyosiy"),
]

Q["8.1.3"] = [
    C(1, "Qatvon dashti jangi qaysi yilda bo'lgan?", "1141-yilda", ["1040-yilda", "1218-yilda", "1370-yilda"], "1141.", b="siyosiy"),
    C(1, "Qatvon jangida Sulton Sanjar va Qoraxoniylar kimdan mag'lub bo'ldi?", "Qoraxitoylar", ["Mo'g'ullar", "G'aznaviylar", "Arablar"], "Gurxon Yelyu Dashi.", b="siyosiy"),
    C(1, "Qatvon dashti qaysi shahar yaqinida?", "Samarqand", ["Buxoro", "Marv", "Termiz"], "Samarqand.", b="siyosiy"),
    C(2, "Qoraxitoylar hukmdorlari qanday unvonda atalgan?", "Gurxon", ["Sulton", "Amir", "Shoh"], "Gurxon.", b="siyosiy"),
    C(2, "Sulton Sanjar qaysi yil vafot etgan?", "1157-yilda", ["1141-yilda", "1040-yilda", "1220-yilda"], "1157.", b="siyosiy"),
    C(2, "Qatvon jangidan keyin Movarounnahr qaysi davlatga vassal bo'ldi?", "Qoraxitoylar", ["Saljuqiylar", "G'aznaviylar", "Xorazmshohlar"], "Vassal.", b="siyosiy"),
    C(3, "Qoraxitoylar davlatiga asos solgan?", "Yelyu Dashi", ["Chingizxon", "Atsiz", "Tekesh"], "Yelyu Dashi.", b="siyosiy"),
    O(3, "Qatvon dashtidagi jang yilini yozing.", ["1141", "1141-yil"], "1141.", b="siyosiy"),
]

Q["8.1.4"] = [
    C(1, "Xorazmshohlar-Anushteginiylar sulolasi qaysi shahar markazida?", "Urganch (Gurganj)", ["Samarqand", "Marv", "Buxoro"], "Gurganj.", b="siyosiy"),
    C(1, "Anushteginiylar sulolasi asoschisi kim?", "Anushtegin G'archai", ["Atsiz", "Tekesh", "Muhammad"], "Anushtegin.", b="siyosiy"),
    C(1, "Anushtegin G'archai kimning amaldori edi?", "Saljuqiylar sultoni", ["G'aznaviy", "Qoraxitoy", "Somoniy"], "Saljuqiy sultonlarining.", b="siyosiy"),
    C(2, "Xorazmshohlar hukmdorlaridan Atsiz qaysi yillarda hukmronlik qilgan?", "1127–1156-yillar", ["1097–1127-yillar", "1172–1200-yillar", "1200–1220-yillar"], "Atsiz.", b="siyosiy"),
    C(2, "Qaysi hukmdor davrida Xorazm saljuqiylardan ajralib chiqdi?", "Atsiz", ["Tekesh", "Muhammad", "Jaloliddin"], "Mustaqillik.", b="siyosiy"),
    C(2, "Xorazmshohlarning ilk yirik hukmdori Qutbiddin Muhammad davri?", "1097–1127-yillar", ["1127–1156", "1172–1200", "1200–1220"], "Qutbiddin.", b="siyosiy"),
    C(3, "Xorazmshohlar poytaxti nechanchi yilda Chingizxon tomonidan egallangan?", "1221-yilda", ["1200-yilda", "1141-yilda", "1365-yilda"], "Urganch.", b="siyosiy"),
    O(3, "Xorazmshohlar sulolasining asoschisi ismini yozing (Anushtegin ...).", ["Anushtegin G'archai", "G'archai", "Anushtegin Garchai"], "Anushtegin G'archai.", b="siyosiy"),
]

Q["8.1.5"] = [
    C(1, "Qutbiddin Muhammad qaysi yillarda hukmdor bo'lgan?", "1097–1127-yillar", ["1127–1156", "1172–1200", "1200–1220"], "1097–1127.", b="siyosiy"),
    C(1, "Atsiz qaysi yillarda hukmdor bo'lgan?", "1127–1156-yillar", ["1097–1127", "1172–1200", "1200–1220"], "1127–1156.", b="siyosiy"),
    C(1, "Atsiz kimdan mustaqil bo'lishga intilgan?", "Sulton Sanjar (Saljuqiylar)", ["Chingizxon", "Qoraxitoylar faqat", "Mahmud G'aznaviy"], "Sanjarga qarshi.", b="siyosiy"),
    C(2, "Atsiz saroyida ijod qilgan mashhur adib?", "Rashididdin Vatvot", ["Navoiy", "Beruniy", "Firdavsiy"], "Vatvot.", b="madaniyat"),
    C(2, "Sulton Sanjar Xorazmni 1138-yilda qamal qilganda...", "Atsiz mag'lub bo'lib, vaqtincha bo'ysundi", ["Sanjar chekindi", "Xorazm Sanjarni mag'lub etdi", "Hech nima bo'lmadi"], "Xorazm qamali.", b="siyosiy"),
    C(2, "Qutbiddin Muhammad Saljuqiylar sultoniga nisbatan qanday maqomda bo'lgan?", "Vassal", ["Hukmdor", "Dushman", "Ittifoqdosh"], "Vassal.", b="siyosiy"),
    C(3, "Atsiz vafotidan (1156) keyin Xorazmni boshqargan hukmdor?", "Il-Arslon", ["Tekesh", "Muhammad", "Jaloliddin"], "Il-Arslon.", b="siyosiy"),
    O(3, "Qutbiddin Muhammadning o'g'li, mustaqillikka intilgan Xorazm hukmdori ismini yozing (A...).", ["Atsiz", "atsiz"], "Atsiz.", b="siyosiy"),
]

Q["8.1.6"] = [
    C(1, "Xorazmshoh Tekesh qaysi yillarda hukm surgan?", "1172–1200-yillar", ["1127–1156", "1097–1127", "1200–1220"], "Tekesh.", b="siyosiy"),
    C(1, "Xorazmshohlar davlatining eng so'nggi buyuk hukmdori?", "Alouddin Muhammad", ["Tekesh", "Atsiz", "Il-Arslon"], "1200–1220.", b="siyosiy"),
    C(1, "Alouddin Muhammad qaysi yilgacha hukmronlik qilgan?", "1220-yilgacha", ["1200-yilgacha", "1141-yilgacha", "1365-yilgacha"], "1220.", b="siyosiy"),
    C(2, "Xorazmshoh Muhammad Samarqandni egallab, qaysi davlatga barham bergan?", "G'arbiy Qoraxoniylar", ["Qoraxitoylar faqat", "Saljuqiylar", "G'aznaviylar"], "1212.", b="siyosiy"),
    C(2, "Muhammadning onasi kim?", "Turkon xotun", ["Uljoy", "Nodira", "Bibixonim"], "Turkon xotun.", b="siyosiy"),
    C(2, "Muhammadning o'g'li, mo'g'ullarga qarshi kurashgan qahramon?", "Jaloliddin Manguberdi", ["Ozloqshoh", "Uzbek", "Tarag'ay"], "Jaloliddin.", b="siyosiy"),
    C(3, "Xorazmshohlar davlati eng keng hududga qaysi hukmdor davrida erishgan?", "Alouddin Muhammad", ["Tekesh", "Atsiz", "Il-Arslon"], "Muhammad.", b="siyosiy"),
    O(3, "Xorazmshohlar davlatining so'nggi buyuk hukmdori Alouddin ... ismini yozing.", ["Muhammad", "Alouddin Muhammad"], "Muhammad.", b="siyosiy"),
]

Q["8.1.7"] = [
    C(1, "Chingizxonning asl ismi?", "Temujin", ["Tug'rul", "Batu", "Qubilay"], "Temujin.", b="siyosiy"),
    C(1, "Chingizxon 1206-yilda qayerda xon deb e'lon qilingan?", "Onon daryosi bo'yidagi qurultoyda", ["Samarqandda", "Buxoroda", "Bag'dodda"], "Qurultoy.", b="siyosiy"),
    C(1, "Mo'g'ul davlatining poytaxti?", "Qoraqurum", ["Samarqand", "Pekin", "Urganch"], "Qoraqurum.", b="siyosiy"),
    C(2, "Chingizxon qonunlar to'plami?", "Yasa (Yassa)", ["Tuzuklar", "Hammurapi", "Avesto"], "Yasa.", b="siyosiy"),
    C(2, "Mo'g'ullar bilan birga kurashgan qabilalardan biri?", "Naymanlar, kereitlar, tatarlar", ["Xionitlar", "Eftaliylar", "Kidariylar"], "Qabilalar.", b="siyosiy"),
    C(2, "Chingizxon qo'shini qaysi sistema bo'yicha tuzilgan?", "O'nlik (10, 100, 1000, 10000)", ["Beshlik", "Yuzlik faqat", "Yigirmalik"], "O'nlik.", b="siyosiy"),
    C(3, "Chingizxon qurultoyi qaysi yilda bo'lgan?", "1206-yilda", ["1218-yilda", "1220-yilda", "1227-yilda"], "1206.", b="siyosiy"),
    O(3, "Mo'g'ullarning Chingizxon qonunlari to'plami nomini yozing (Y...).", ["Yasa", "Yassa", "yasa"], "Yasa.", b="siyosiy"),
]

Q["8.1.8"] = [
    C(1, "O'tror fojeasi qaysi yilda sodir bo'lgan?", "1218-yilda", ["1206-yilda", "1220-yilda", "1227-yilda"], "1218.", b="siyosiy"),
    C(1, "O'tror hokimi kim edi?", "Inolchiq (Gayirxon)", ["Jaloliddin", "Tekesh", "Qutayba"], "Inolchiq.", b="siyosiy"),
    C(1, "O'tror fojeasida nima sodir bo'ldi?", "Chingizxonning savdo karvoni qirib tashlandi", ["Shahar yondirildi", "Hokim o'ldirildi", "Qo'shin mag'lub bo'ldi"], "Karvon.", b="siyosiy"),
    C(2, "Chingizxon karvoni a'zolari qanday ayblangan?", "Josuslikda", ["Talonchilikda", "Dinsizlikda", "Qaroqchilikda"], "Josuslik.", b="siyosiy"),
    C(2, "Mo'g'ul elchilari qanday jazolangan?", "Birini o'ldirib, boshqalarini sochi-soqolini qirib qaytarishgan", ["Hammasi ozod qilindi", "Mukofot berildi", "Qamoqqa olindi"], "Haqorat.", b="siyosiy"),
    C(2, "O'tror fojeasining oqibati nima bo'ldi?", "Mo'g'ullarning Xorazmshohlar davlatiga yurishi", ["Mo'g'ullar chekindi", "Ittifoq tuzildi", "Tinchlik"], "1219–1221.", b="siyosiy"),
    C(3, "O'tror qamali necha oy davom etgan?", "Taxminan 5 oy", ["1 hafta", "2 yil", "10 yil"], "Qamal.", b="siyosiy"),
    O(3, "O'tror hokimi Inolchiq yana qanday nom bilan ataladi? (Gayir... )", ["Gayirxon", "Gayir xon", "G'oyirxon"], "Gayirxon.", b="siyosiy"),
]

Q["8.1.9"] = [
    C(1, "Chingizxonning Movarounnahrga yurishi qaysi yildan boshlandi?", "1219-yildan", ["1206-yildan", "1227-yildan", "1365-yildan"], "1219.", b="siyosiy"),
    C(1, "Buxoro mo'g'ullar tomonidan qaysi yili egallandi?", "1220-yilda", ["1218-yilda", "1221-yilda", "1227-yilda"], "1220.", b="siyosiy"),
    C(1, "Samarqand mo'g'ullar tomonidan qaysi yili egallandi?", "1220-yilda", ["1206-yilda", "1219-yilda", "1221-yilda"], "1220.", b="siyosiy"),
    C(2, "Xo'jand mudofaasiga kim rahbarlik qilgan?", "Temur Malik", ["Jaloliddin", "Inolchiq", "Tekesh"], "Temur Malik.", b="siyosiy"),
    C(2, "Buxoro jome masjidi minbaridan Chingizxon nima degan?", "«Men Xudoning jazosiman»", ["«Men xalq xizmatchisiman»", "«Men sizlarni himoya qilaman»", "«Tinchlik»"], "Rivoyat.", b="siyosiy"),
    C(2, "Xorazmshoh Muhammad qayerda vafot etgan?", "Kaspiy dengizidagi orolda", ["Samarqandda", "Urganchda", "Buxoroda"], "1220/1221.", b="siyosiy"),
    C(3, "Chingizxon qo'shini qaysi yilda Termizni egallagan?", "1220-yilda", ["1206-yilda", "1365-yilda", "1141-yilda"], "1220.", b="siyosiy"),
    O(3, "Chingizxonning Movarounnahrga yurishi qaysi yilda boshlangan? (raqam)", ["1219", "1219-yil"], "1219.", b="siyosiy"),
]

Q["8.1.10"] = [
    C(1, "Gurganj (Urganch) qamali necha oy davom etgan?", "Taxminan 7 oy", ["1 oy", "2 hafta", "2 yil"], "1221.", b="siyosiy"),
    C(1, "Gurganj mudofaasida halok bo'lgan mashhur shayx?", "Najmiddin Kubro", ["Ahmad Yassaviy", "Imom Buxoriy", "Bahouddin Naqshband"], "Kubroviya.", b="siyosiy"),
    C(1, "Najmiddin Kubro qaysi tariqat asoschisi?", "Kubroviya", ["Naqshbandiya", "Yassaviya", "Xojagon"], "Kubroviya.", b="madaniyat"),
    C(2, "Gurganjni mo'g'ullar qaysi yilda egallagan?", "1221-yilda", ["1218-yilda", "1220-yilda", "1227-yilda"], "1221.", b="siyosiy"),
    C(2, "Gurganj egallanganda mo'g'ullar nima qilgan?", "Daryo to'g'onini buzib, shaharni suv bosgan", ["Shaharni ayab qolganlar", "Tinch kirganlar", "Qal'ani tark etganlar"], "Amudaryo.", b="siyosiy"),
    C(2, "Najmiddin Kubro vafot etgan yil?", "1221-yil", ["1141-yil", "1370-yil", "1405-yil"], "1221.", b="siyosiy"),
    C(3, "Gurganj mudofaasini boshqargan harbiy rahbar?", "Xumor-tegin", ["Jaloliddin", "Temur Malik", "Inolchiq"], "Xumor-tegin.", b="siyosiy"),
    O(3, "Gurganjda mo'g'ullarga qarshi jang qilib halok bo'lgan kubroviya tariqati asoschisi ismini yozing (Najmiddin ...).", ["Najmiddin Kubro", "Kubro", "Najmuddin Kubro"], "Najmiddin Kubro.", b="siyosiy"),
]

Q["8.1.11-12"] = [
    C(1, "Jaloliddin Manguberdi qaysi jangda mo'g'ullarni mag'lub etdi?", "Parvon jangida (1221)", ["Dandanaqan", "Loy", "Anqara"], "1221 Afg'oniston.", b="siyosiy"),
    C(1, "Jaloliddin Manguberdi qaysi daryo bo'yida Chingizxon bilan jang qildi?", "Sind", ["Nil", "Volga", "Dajla"], "Sind.", b="siyosiy"),
    C(1, "Jaloliddin Manguberdi qaysi hukmdorning o'g'li?", "Alouddin Muhammad", ["Tekesh", "Atsiz", "Il-Arslon"], "Muhammad.", b="siyosiy"),
    C(2, "Jaloliddin Manguberdi qaysi yilda halok bo'lgan?", "1231-yilda", ["1221-yilda", "1220-yilda", "1227-yilda"], "1231.", b="siyosiy"),
    C(2, "Jaloliddin Manguberdi hayotini bayon qilgan tarixchi?", "Muhammad Nasaviy", ["Shomiy", "Yazdiy", "Behbudiy"], "Nasaviy.", b="madaniyat"),
    C(2, "Sind daryosi jangi (1221) dan keyin Jaloliddin qayerga o'tgan?", "Hindistonga", ["Misrga", "Xitoyga", "Rusiyaga"], "Hindiston.", b="siyosiy"),
    C(3, "Parvon jangida mo'g'ul qo'shinini kim boshqargan?", "Shiki-Xutuxu", ["Chingizxon", "Ogaday", "Batu"], "Shiki-Xutuxu.", b="siyosiy"),
    O(3, "Jaloliddin Manguberdi qaysi daryo bo'yidagi jangda (1221) Chingizxon bilan to'qnashgan? Daryo nomini yozing (S...).", ["Sind", "sind"], "Sind.", b="siyosiy"),
]

Q["8.1.13"] = [
    C(1, "Chingizxon qaysi yilda vafot etgan?", "1227-yilda", ["1206-yilda", "1220-yilda", "1231-yilda"], "1227.", b="siyosiy"),
    C(1, "Chig'atoy ulusiga qaysi hududlar kirgan?", "Movarounnahr va Yettisuv", ["Rusiya", "Eron", "Xitoy"], "Chig'atoy.", b="siyosiy"),
    C(1, "Jo'ji ulusi qanday nom bilan mashhur?", "Oltin O'rda", ["Chig'atoy ulusi", "Ilxonlar", "Yuan"], "Oltin O'rda.", b="siyosiy"),
    C(2, "Chingizxonning o'g'illari qaysilar?", "Jo'ji, Chig'atoy, O'gaday, Tuli", ["Batu, Hulagu, Qubilay, Mengu", "Temur, Shohruh", "Alp, Subuk"], "To'rt o'g'il.", b="siyosiy"),
    C(2, "Chig'atoy ulusi 1346-yildan keyin nechta qismga bo'lindi?", "Ikki (Movarounnahr va Mo'g'uliston)", ["Uch", "To'rt", "Besh"], "1346.", b="siyosiy"),
    C(2, "Mo'g'ul imperiyasi buyuk xonining markazi?", "Qoraqurum", ["Samarqand", "Urganch", "Bag'dod"], "Qoraqurum.", b="siyosiy"),
    C(3, "1346-yilda Chig'atoy xoni Doniyolo'g'lonni mag'lub etgan amir kim?", "Amir Qozog'on", ["Amir Temur", "Amir Husayn", "Tug'luq Temur"], "Qozog'on.", b="siyosiy"),
    O(3, "Chingizxon qaysi yilda vafot etgan? (raqam)", ["1227", "1227-yil"], "1227.", b="siyosiy"),
]

Q["8.1.14-15"] = [
    C(1, "Mahmud Torobiy qo'zg'oloni qaysi yilda bo'lgan?", "1238-yilda", ["1221-yilda", "1365-yilda", "1220-yilda"], "1238.", b="ijtimoiy"),
    C(1, "Mahmud Torobiy qaysi hunar egasi edi?", "Elak yasovchi hunarmand", ["Temirchi", "Kulol", "Mirzo"], "Torob qishlog'i.", b="ijtimoiy"),
    C(1, "Mas'udbek kim edi?", "Movarounnahr hokimi (Mahmud Yalavochning o'g'li)", ["Mo'g'ul xoni", "Qoraxitoy gurxoni", "Saljuq sultoni"], "Mas'udbek.", b="ijtimoiy"),
    C(2, "Mas'udbek islohotlaridan biri?", "Soliq tizimini tartibga solish, pul tangalarini zarb etish", ["Yangi dinni joriy qilish", "Qo'shinni tarqatish", "Savdoni taqiqlash"], "Islohot.", b="ijtimoiy"),
    C(2, "Mahmud Torobiy qo'zg'oloni qaysi shahar yaqinida bo'lgan?", "Buxoro", ["Samarqand", "Urganch", "Marv"], "Torob.", b="ijtimoiy"),
    C(2, "Torobiy qo'zg'olonining sabablaridan biri?", "Og'ir soliqlar va mo'g'ul amaldorlarining zulmi", ["Dinga qarshi qaror", "Qurg'oqchilik faqat", "Savdoning rivoji"], "Soliq.", b="ijtimoiy"),
    C(3, "Torobiy qo'zg'oloni qanday tugadi?", "Mo'g'ul qo'shinlari tomonidan bostirildi", ["Muvaffaqiyatli bo'ldi", "Kelishuv bilan", "Amaldorlar qo'shildi"], "Bostirildi.", b="ijtimoiy"),
    O(2, "Torobiy qo'zg'oloni qaysi yilda bo'lgan? (raqam)", ["1238", "1238-yil"], "1238.", b="ijtimoiy"),
]

Q["8.1.16"] = [
    C(1, "XIV asrning o'rtalarida Movarounnahrda qanday vaziyat hukm surgan?", "Tarqoqlik va o'zaro urushlar", ["Markazlashgan kuchli davlat", "Rim hukmronligi", "Arab xalifaligi"], "Tarqoqlik.", b="siyosiy"),
    C(1, "1346-yilda hokimiyatni qo'lga olgan amir?", "Amir Qozog'on", ["Amir Temur", "Amir Husayn", "Tug'luq Temur"], "Qozog'on.", b="siyosiy"),
    C(1, "Amir Qozog'on qaysi yilda o'ldirilgan?", "1358-yilda", ["1346-yilda", "1365-yilda", "1370-yilda"], "1358.", b="siyosiy"),
    C(2, "Mo'g'uliston xoni Tug'luq Temur Movarounnahrga qaysi yillarda yurish qilgan?", "1360–1361-yillar", ["1219–1221", "1398–1399", "1219"], "Yurishlar.", b="siyosiy"),
    C(2, "Movarounnahrning bekliklar bo'linishi sababi?", "Mo'g'ul xonlari zaifligi va zodagonlar kurashi", ["Arab bosqini", "Rus yurishi", "Yunon yurishi"], "Zodagonlar.", b="siyosiy"),
    C(2, "Kesh viloyati hokimi bo'lgan amir?", "Hojji Barlos", ["Amir Husayn", "Temur Malik", "Mas'udbek"], "Hojji Barlos.", b="siyosiy"),
    C(3, "Amir Qozog'onning nabirasi, keyinchalik Temurning raqibi?", "Amir Husayn", ["Ilyosxo'ja", "Tug'luq Temur", "Hojji Barlos"], "Husayn.", b="siyosiy"),
    O(3, "Amir Qozog'on qaysi yilda hokimiyatni qo'lga oldi? (raqam)", ["1346", "1346-yil"], "1346.", b="siyosiy"),
]

Q["8.1.17"] = [
    C(1, "Loy jangi qaysi yilda bo'lgan?", "1365-yilda", ["1370-yilda", "1391-yilda", "1402-yilda"], "1365.", b="siyosiy"),
    C(1, "Loy jangi sanasi?", "1365-yil 22-may", ["1365-yil 9-aprel", "1370-yil 22-may", "1402-yil 28-iyul"], "22-may.", b="siyosiy"),
    C(1, "Loy jangida qaysi tomon g'olib bo'ldi?", "Mo'g'uliston (Ilyosxo'ja)", ["Temur va Husayn", "Sarbadorlar", "Xorazmshohlar"], "Mag'lubiyat.", b="siyosiy"),
    C(2, "Samarqand mudofaasi (1365)ni kimlar boshqargan?", "Sarbadorlar", ["Arablar", "Rimliklar", "G'aznaviylar"], "Sarbadorlar.", b="siyosiy"),
    C(2, "Sarbadorlar rahbarlaridan biri?", "Mavlonozoda", ["Amir Husayn", "Tug'luq Temur", "Ilyosxo'ja"], "Mavlonozoda.", b="siyosiy"),
    C(2, "Sarbadorlar nomi nimani anglatadi?", "«Boshi dorga!» — jon fido qilishga tayyor", ["Qora kiyimlilar", "Oq o'tov", "Zargarlar"], "Sarbador.", b="siyosiy"),
    C(3, "Loy jangida Amir Temur va Amir Husayn kim bilan jang qilgan?", "Ilyosxo'ja", ["Tug'luq Temur", "Qozog'on", "Tarag'ay"], "Ilyosxo'ja.", b="siyosiy"),
    O(3, "Loy jangi qaysi yilda bo'lgan? (raqam)", ["1365", "1365-yil"], "1365.", b="siyosiy"),
]

Q["8.1.18"] = [
    C(1, "Amir Temur qaysi yilda tug'ilgan?", "1336-yilda", ["1365-yilda", "1370-yilda", "1405-yilda"], "1336.", b="siyosiy"),
    C(1, "Amir Temur tug'ilgan qishloq?", "Xo'ja Ilg'or (Kesh yaqinida)", ["Ark", "Shahrisabz shahri markazi", "Samarqand"], "Xo'ja Ilg'or.", b="siyosiy"),
    C(1, "Amir Temurning otasi kim?", "Amir Tarag'ay", ["Amir Husayn", "Hojji Barlos", "Qozog'on"], "Tarag'ay.", b="siyosiy"),
    C(2, "Amir Temur qaysi qabiladan?", "Barlos", ["Jaloir", "Qiyot", "Tatar"], "Barlos.", b="siyosiy"),
    C(2, "Amir Temur 1360–1361-yillarda kimning xizmatiga o'tgan?", "Tug'luq Temur", ["Ilyosxo'ja", "Amir Husayn", "Chingizxon"], "Tug'luq Temur.", b="siyosiy"),
    C(2, "Amir Husayn Amir Temurga kim bo'lgan?", "Qaynog'a (Uljoy Turkon og'aning akasi)", ["Otasi", "O'g'li", "Ustozi"], "Qaynog'a.", b="siyosiy"),
    C(3, "Amir Temur va Amir Husayn ittifoqi qaysi yildan keyin parchalandi?", "1366–1370-yillarda", ["1219-yilda", "1402-yilda", "1500-yilda"], "Raqobat.", b="siyosiy"),
    O(3, "Amir Temur tug'ilgan yilini yozing. (raqam)", ["1336", "1336-yil"], "1336.", b="siyosiy"),
]

Q["8.1.19"] = [
    C(1, "Balx qurultoyi qaysi yilda bo'lgan?", "1370-yilda", ["1365-yilda", "1391-yilda", "1402-yilda"], "1370.", b="siyosiy"),
    C(1, "Balx qurultoyida Amir Temur nima deb e'lon qilindi?", "Movarounnahr hukmdori (Sohibqiron)", ["Faqat sarkarda", "Xon", "Xalifa"], "Hukmdor.", b="siyosiy"),
    C(1, "Amir Temur poytaxti qaysi shahar bo'ldi?", "Samarqand", ["Buxoro", "Kesh", "Balx"], "Samarqand.", b="siyosiy"),
    C(2, "Balx qurultoyidan oldin Amir Husayn kim tomonidan mag'lub etildi?", "Amir Temur", ["Ilyosxo'ja", "Tug'luq Temur", "Qozog'on"], "Husayn halok bo'ldi.", b="siyosiy"),
    C(2, "Amir Temur davlat tepasiga kelgan yil?", "1370", ["1360", "1380", "1391"], "1370.", b="siyosiy"),
    C(2, "Sohibqiron unvoni qanday ma'noni bildiradi?", "Baxtli yulduzlar egasi", ["Xon xoni", "Sulton", "Imom"], "Sohibqiron.", b="siyosiy"),
    C(3, "Balx qurultoyida mahalliy zodagonlar Temurni qanday qo'llab-quvvatlashgan?", "Uni hukmdor deb tan olishgan", ["Chiqarib yuborishgan", "Kutishgan", "Qo'rqishgan"], "Qurultoy.", b="siyosiy"),
    O(3, "Amir Temur hokimiyat tepasiga kelgan Balx qurultoyi yilini yozing.", ["1370", "1370-yil"], "1370.", b="siyosiy"),
]

Q["8.1.20"] = [
    C(1, "Amir Temur Xorazmni qaysi yillar davomida bo'ysundirgan?", "1373–1388-yillar", ["1360–1370", "1391–1395", "1402–1405"], "Xorazm.", b="siyosiy"),
    C(1, "Amir Temurning 1370-yillardagi yurishlari asosan qaysi yo'nalishlarga qaratilgan edi?", "Mo'g'uliston va Xorazmga", ["Hindiston va Xitoyga", "Misr va Suriyaga", "Rusiya va Yevropaga"], "Davlatni birlashtirish uchun.", b="siyosiy"),
    C(1, "Amir Temur Hirotni qaysi yilda egallagan?", "1381-yilda", ["1365-yilda", "1219-yilda", "1500-yilda"], "1381.", b="siyosiy"),
    C(2, "Xorazm hukmdori kim edi (Temurga qarshi)?", "Yusuf Sufi", ["Husayn", "Ilyosxo'ja", "To'xtamish"], "Yusuf Sufi.", b="siyosiy"),
    C(2, "Temurning dastlabki yirik yurishlari qaysi yo'nalishda bo'lgan?", "Mo'g'uliston, Xorazm va Xuroson", ["Hindiston", "Rusiya", "Misr"], "Birlashtirish.", b="siyosiy"),
    C(2, "Xorazm yakuniy bo'ysundirilgan yil?", "1388-yil", ["1373-yil", "1381-yil", "1395-yil"], "1388.", b="siyosiy"),
    C(3, "«Uch yillik yurish» qaysi yillarda?", "1386–1388", ["1392–1396", "1399–1404", "1370–1373"], "Uch yillik.", b="siyosiy"),
    O(3, "Xorazm yakuniy bo'ysundirilgan yilni yozing.", ["1388", "1388-yil"], "1388.", b="siyosiy"),
]

Q["8.1.21"] = [
    C(1, "Amir Temur To'xtamishxonga qarshi birinchi yurishi qachon?", "1391-yil", ["1395-yil", "1402-yil", "1398-yil"], "Qunduzcha.", b="siyosiy"),
    C(1, "Qunduzcha jangi qaysi yilda?", "1391", ["1395", "1402", "1365"], "1391.", b="siyosiy"),
    C(1, "Terek jangi qaysi yilda?", "1395", ["1391", "1402", "1398"], "1395.", b="siyosiy"),
    C(2, "To'xtamishxon qaysi davlat xoni edi?", "Oltin O'rda", ["Chig'atoy ulusi", "Ilxonlar", "Xorazmshohlar"], "Oltin O'rda.", b="siyosiy"),
    C(2, "To'xtamishxon qaysi hukmdorga qarshi yurish qilgan?", "Amir Temur", ["Chingizxon", "Boyazid", "Shohruh"], "Temur.", b="siyosiy"),
    C(2, "Oltin O'rda xoni To'xtamish dastlab kimning yordamida taxtga o'tirgan?", "Amir Temur yordami bilan", ["Ilyosxo'ja", "Tug'luq", "Shohruh"], "Temur.", b="siyosiy"),
    M(2, [("Qunduzcha", "1391-yil"), ("Terek", "1395-yil"), ("Anqara", "1402-yil")], "Janglar."),
    C(3, "Terek jangidan keyin To'xtamish...", "Butunlay hokimiyatdan mahrum bo'ldi", ["G'alaba qildi", "Taxtni qaytarib oldi", "Temurga qo'shildi"], "Mag'lub.", b="siyosiy"),
    O(3, "Terek daryosi bo'yidagi jang qaysi yilda bo'lgan? (raqam)", ["1395", "1395-yil"], "1395.", b="siyosiy"),
]

Q["8.1.22-23"] = [
    C(1, "Anqara jangi qaysi yilda?", "1402-yil", ["1391-yil", "1395-yil", "1405-yil"], "28-iyul 1402.", b="siyosiy"),
    C(1, "Anqara jangida Amir Temur kimni asir oldi?", "Boyazid I Yildirim", ["To'xtamish", "Muhammad", "Faraj"], "Boyazid.", b="siyosiy"),
    C(1, "Boyazid I qaysi davlat sultoni?", "Usmonli", ["Mamluk", "Saljuqiy", "Fors"], "Usmonli.", b="siyosiy"),
    C(2, "Amir Temurning «yetti yillik yurishi» qaysi yillarda?", "1399–1404", ["1386–1388", "1392–1396", "1370–1373"], "Yetti yillik.", b="siyosiy"),
    C(2, "Amir Temurning «besh yillik yurishi» qaysi yillarda?", "1392–1396", ["1386–1388", "1399–1404", "1370–1373"], "Besh yillik.", b="siyosiy"),
    C(2, "Anqara jangidan keyin Amir Temurga minnatdorchilik xati yuborgan davlatlar?", "Yevropa davlatlari (Fransiya, Angliya, Vizantiya)", ["Hindiston", "Xitoy", "Misr"], "Yevropa.", b="siyosiy"),
    C(3, "Kastiliya elchisi Klavixo Samarqandda qaysi yillarda bo'lgan?", "1404", ["1399", "1391", "1370"], "1404.", b="siyosiy"),
    O(3, "Anqara jangi qaysi yilda bo'lgan? (raqam)", ["1402", "1402-yil"], "1402.", b="siyosiy"),
]

Q["8.1.24"] = [
    C(1, "Amir Temurning Hindiston yurishi qaysi yillarda?", "1398–1399", ["1386–1388", "1402", "1405"], "Hindiston.", b="siyosiy"),
    C(1, "Amir Temur qaysi shaharda vafot etgan?", "O'trorda", ["Samarqandda", "Keshda", "Hirotda"], "1405.", b="siyosiy"),
    C(1, "Amir Temur vafot yili?", "1405", ["1402", "1398", "1370"], "1405.", b="siyosiy"),
    C(2, "Hindistondan ustalar nima qurilishi uchun keltirilgan?", "Samarqanddagi Bibixonim masjidi va boshqa inshootlar", ["Kemasozlik", "Qal'a devori", "Sug'orish"], "Ustalar.", b="madaniyat"),
    C(2, "Hindistonda Amir Temur egallagan shahar?", "Dehli", ["Agra", "Kobul", "Lahor"], "1398.", b="siyosiy"),
    C(2, "Temur qaysi davlatga yurish uchun chiqqan va vafot etgan?", "Xitoy", ["Misr", "Rusiya", "Vizantiya"], "1404-yil dekabr.", b="siyosiy"),
    C(3, "Amir Temurning Xitoyga yurishi qaysi yilda boshlangan?", "1404-yil", ["1398", "1402", "1391"], "1404.", b="siyosiy"),
    O(3, "Amir Temur vafot etgan shahar nomini yozing (O'...).", ["O'tror", "Otror", "Utror"], "O'tror.", b="siyosiy"),
]

Q["8.1.25"] = [
    C(1, "Amir Temur davlat boshqaruvi haqidagi asari?", "«Temur tuzuklari»", ["«Zafarnoma»", "«Boburnoma»", "«Avesto»"], "Tuzuklar.", b="siyosiy"),
    C(1, "Tuzuklarda davlat tayanadigan nechta tabaqa sanab o'tilgan?", "12", ["7", "9", "20"], "12 tabaqa.", b="siyosiy"),
    C(1, "Amir Temurda bosh devon qanday atalgan?", "Devoni buzurg", ["Devoni vazir", "Devoni mushrif", "Devoni jandar"], "Buzurg.", b="siyosiy"),
    C(2, "Temur qo'shinida mingboshi qaysi?", "1000 kishilik bo'linma boshlig'i", ["10 kishilik", "100 kishilik", "10 000 kishilik"], "Mingboshi.", b="siyosiy"),
    C(2, "Temur shiori?", "«Kuch — adolatda»", ["«Kuch — qilichda»", "«Kuch — oltinda»", "«Kuch — kitobda»"], "Rosti rusti.", b="siyosiy"),
    C(2, "Temur qo'shinida tumanboshi nechta askarga rahbarlik qilgan?", "10 000", ["10", "100", "1000"], "Tuman.", b="siyosiy"),
    C(3, "«Temur tuzuklari»ni forsiychaga o'girgan tarjimon/qayd etuvchi?", "Abu Tolib Husayniy", ["Nizomiddin Shomiy", "Yazdiy", "Navoiy"], "Husayniy.", b="siyosiy"),
    O(3, "Amir Temurda bosh devon nima deb atalgan? (Devoni ...)", ["Devoni buzurg", "buzurg"], "Devoni buzurg.", b="siyosiy"),
]

Q["8.1.26"] = [
    C(1, "Shohruh Mirzo qaysi shaharda hukmronlik qilgan?", "Hirotda", ["Samarqandda", "Buxoroda", "Kesh"], "Hirot.", b="siyosiy"),
    C(1, "Shohruh Mirzo hukmronlik yillari?", "1409–1447", ["1370–1405", "1447–1449", "1469–1506"], "1409–1447.", b="siyosiy"),
    C(1, "Mirzo Ulug'bek Samarqand hokimi bo'lgan yil?", "1409", ["1370", "1417", "1449"], "1409.", b="siyosiy"),
    C(2, "Temur vafotidan so'ng Samarqand taxtiga o'tirgan nabirasi?", "Xalil Sulton", ["Pir Muhammad", "Ulug'bek", "Abu Said"], "1405–1409.", b="siyosiy"),
    C(2, "Shohruh Mirzo hokimiyatni Samarqandda qaysi yili qo'lga oldi?", "1409", ["1405", "1417", "1447"], "1409.", b="siyosiy"),
    C(2, "Temur taxtiga nomzodlardan Pir Muhammad qaysi hududni boshqargan?", "Qandahor (Afg'oniston janubi)", ["Samarqand", "Xorazm", "Buxoro"], "Qandahor.", b="siyosiy"),
    C(3, "Shohruh Mirzo davrida Hirot qanday markaz bo'lib qoldi?", "Fan va madaniyat markazi", ["Savdo yo'li", "Harbiy lager", "Port shahar"], "Ilm.", b="siyosiy"),
    O(3, "Shohruh Mirzo hukmronlik qilgan shahar nomini yozing (H...).", ["Hirot", "hirot"], "Hirot.", b="siyosiy"),
]

Q["8.1.27"] = [
    C(1, "Mirzo Ulug'bekning mashhur astronomik asari?", "«Ziji Ko'ragoniy»", ["«Qonun»", "«Zafarnoma»", "«Hidoya»"], "Zij.", b="madaniyat"),
    C(1, "Ulug'bek madrasasi (Samarqand) qaysi yillarda qurilgan?", "1417–1420", ["1127", "1619–1636", "1646–1660"], "1417–1420.", b="madaniyat"),
    C(1, "Ulug'bek rasadxonasi qaysi yillarda qurilgan?", "1424–1429", ["1409–1417", "1437–1449", "1500–1510"], "Rasadxona.", b="madaniyat"),
    C(2, "«Ziji Ko'ragoniy»da nechta yulduz kiritilgan?", "1018", ["365", "500", "2000"], "1018.", b="madaniyat"),
    C(2, "Ulug'bek akademiyasi a'zolaridan biri?", "Ali Qushchi", ["Beruniy", "Ibn Sino", "Navoiy"], "Ali Qushchi.", b="madaniyat"),
    C(2, "Ulug'bek qaysi yilda qatl etilgan?", "1449", ["1417", "1437", "1447"], "1449.", b="siyosiy"),
    M(2, [("Samarqand madrasasi", "1417–1420"), ("Buxoro madrasasi", "1417"), ("G'ijduvon madrasasi", "1433")], "Ulug'bek madrasalari.", ),
    C(3, "Ulug'bekni qatl ettirgan o'g'li?", "Abdullatif", ["Abu Said", "Pir Muhammad", "Sultonali"], "Abdullatif.", b="siyosiy"),
    O(3, "Mirzo Ulug'bek tuzgan yulduzlar jadvali nomini yozing («Ziji ...»).", ["Ziji Ko'ragoniy", "Ko'ragoniy", "Ziji Koragoniy", "Zij Ko'ragoniy"], "Ko'ragoniy.", b="madaniyat"),
]

Q["8.1.28"] = [
    C(1, "Sulton Abu Said qaysi yillarda hukmronlik qilgan?", "1451–1469", ["1409–1447", "1469–1506", "1370–1405"], "Abu Said.", b="siyosiy"),
    C(1, "Sulton Husayn Boyqaro qaysi yillarda hukmronlik qilgan?", "1469–1506", ["1451–1469", "1409–1447", "1370–1405"], "Boyqaro.", b="siyosiy"),
    C(1, "Husayn Boyqaro poytaxti?", "Hirot", ["Samarqand", "Buxoro", "Qandahor"], "Hirot.", b="siyosiy"),
    C(2, "Sulton Abu Said qaysi jangda halok bo'lgan?", "Qorabog' (1469)", ["Anqara", "Loy", "Terek"], "1469.", b="siyosiy"),
    C(2, "Husayn Boyqaro taxallusi?", "Husayniy", ["Foniy", "Navoiy", "Bobur"], "Husayniy.", b="madaniyat"),
    C(2, "Husayn Boyqaro saroyida yashagan mashhur mudarris va shoir?", "Abdurahmon Jomiy", ["Gerodot", "Beruniy", "Ibn Sino"], "Jomiy.", b="madaniyat"),
    C(3, "Hirot miniatyura maktabining mashhur vakili?", "Kamoliddin Behzod", ["Ali Qushchi", "Bobur", "Mirzo Ulug'bek"], "Behzod.", b="madaniyat"),
    O(3, "Husayn Boyqaro qaysi yilda vafot etgan? (raqam)", ["1506", "1506-yil"], "1506.", b="siyosiy"),
]

Q["8.1.29"] = [
    C(1, "Alisher Navoiy qaysi yilda tug'ilgan?", "1441", ["1336", "1483", "1500"], "1441, Hirot.", b="madaniyat"),
    C(1, "Navoiyning «Xamsa»si nechta dostondan iborat?", "Beshta", ["Uchta", "Yettita", "To'qqizta"], "Xamsa — besh doston.", b="madaniyat"),
    C(1, "Navoiy turkiy tilni forsiy bilan solishtirgan asari?", "«Muhokamat ul-lug'atayn»", ["«Xamsa»", "«Boburnoma»", "«Zafarnoma»"], "1499.", b="madaniyat"),
    C(2, "Navoiyning tazkirasi?", "«Majolis un-nafois»", ["«Sab'ai sayyor»", "«Farhod va Shirin»", "«Lison ut-tayr»"], "Tazkira.", b="madaniyat"),
    C(2, "Navoiy qaysi yilda vafot etgan?", "1501", ["1441", "1469", "1506"], "1501.", b="madaniyat"),
    M(2, [("«Hayrat ul-abror»", "Xamsaning 1-dostoni"), ("«Farhod va Shirin»", "Xamsaning 2-dostoni"), ("«Layli va Majnun»", "Xamsaning 3-dostoni")], "Xamsa."),
    C(3, "Navoiy «Xamsa»ni qaysi yillarda yozgan?", "1483–1485", ["1441–1450", "1499–1500", "1501"], "Xamsa.", b="madaniyat"),
    O(3, "Navoiyning turkiy tilda yozilgan she'rlar devoni «Xazoyin ul-...» nomini davom ettiring (maoniy).", ["maoniy", "Xazoyin ul-maoniy", "Xazoyin ul maoniy"], "Xazoyin ul-maoniy.", b="madaniyat"),
]

Q["8.1.30"] = [
    C(1, "Zahiriddin Muhammad Bobur tug'ilgan shahar?", "Andijon", ["Samarqand", "Buxoro", "Kobul"], "1483.", b="siyosiy"),
    C(1, "Bobur tug'ilgan yil?", "1483", ["1441", "1500", "1526"], "1483.", b="siyosiy"),
    C(1, "Bobur Farg'ona taxtiga necha yoshda o'tirgan?", "12 yoshda", ["20 yoshda", "30 yoshda", "5 yoshda"], "1494.", b="siyosiy"),
    C(2, "Bobur Hindistonda qaysi jangda Ibrohim Lodiyni mag'lub etgan?", "Panipat (1526)", ["Xanva", "Loy", "Anqara"], "1526.", b="siyosiy"),
    C(2, "Bobur Kobulni qaysi yili egallagan?", "1504", ["1494", "1526", "1530"], "1504.", b="siyosiy"),
    C(2, "Bobur asos solgan sulola?", "Boburiylar", ["Temuriylar", "Shayboniylar", "Ashtarxoniylar"], "Boburiylar.", b="siyosiy"),
    M(2, [("«Boburnoma»", "Zahiriddin Bobur"), ("«Zafarnoma» (Shomiy)", "Nizomiddin Shomiy"), ("«Tarixi Rashidiy»", "Mirzo Muhammad Haydar")], "Asarlar muallifi."),
    C(3, "Bobur qaysi yilda vafot etgan?", "1530", ["1526", "1504", "1483"], "Agra.", b="siyosiy"),
    O(3, "Bobur Panipat jangida Ibrohim Lodiyni qaysi yilda mag'lub etgan? (raqam)", ["1526", "1526-yil"], "Panipat 1526.", b="siyosiy"),
]

Q["8.1.31"] = [
    C(1, "Algebra fanining asoschisi?", "Al-Xorazmiy", ["Ibn Sino", "Beruniy", "Forobiy"], "Al-Xorazmiy.", b="madaniyat"),
    C(1, "«Tib qonunlari» muallifi?", "Ibn Sino", ["Beruniy", "Forobiy", "Al-Xorazmiy"], "Ibn Sino.", b="madaniyat"),
    C(1, "«Hadis»larning ishonchli to'plami muallifi?", "Imom Buxoriy", ["Termiziy", "Beruniy", "Zamaxshariy"], "«Al-Jome as-sahih».", b="madaniyat"),
    C(2, "Beruniy tug'ilgan yil?", "973", ["780", "873", "980"], "973.", b="madaniyat"),
    C(2, "«Ikkinchi muallim» nomi berilgan olim?", "Forobiy", ["Ibn Sino", "Beruniy", "Farg'oniy"], "Forobiy.", b="madaniyat"),
    M(2, [("Al-Xorazmiy", "Algebra"), ("Ibn Sino", "Tibbiyot"), ("Beruniy", "Astronomiya va geodeziya")], "Olimlar."),
    M(2, [("«Qutadg'u bilig»", "Yusuf Xos Hojib"), ("«Devonu lug'otit turk»", "Mahmud Qoshg'ariy"), ("«Devoni hikmat»", "Ahmad Yassaviy")], "Asarlar."),
    C(3, "Imom Buxoriy tug'ilgan yil va vafot yili?", "810 va 870", ["973 va 1048", "780 va 850", "1441 va 1501"], "Buxoriy.", b="madaniyat"),
    O(3, "Mahmud Qoshg'ariy «Devonu lug'otit turk»ni qaysi yillarda yozgan? (1072 yoki 1074 dan birini yozing)", ["1072", "1074", "1072–1074", "1072-1074"], "1072–1074.", b="madaniyat"),
]


# ---- Chizmali savollar (SVG) ----
from . import figs  # noqa: E402

Q["8.1.25"] += [
    C(2, "Rasmda Amir Temur qo'shinining jang tartibi ko'rsatilgan (yuqori tomon — dushman). «B» harfi bilan belgilangan o'ng qanot qanday ataladi?", "Barong'or", ["Javong'or", "Chandovul", "Ilg'or"], "O'ng qanot — barong'or, chap qanot — javong'or.", b="siyosiy", fig=figs.army_formation("B")),
    C(2, "Rasmda Amir Temur qo'shini jang tartibi ko'rsatilgan (yuqori tomon — dushman). «C» harfi bilan belgilangan markaziy qism qanday ataladi?", "Qalb", ["Ilg'or", "Barong'or", "Chandovul"], "Qo'shin markazi — qalb.", b="siyosiy", fig=figs.army_formation("C")),
    C(3, "Rasmda Amir Temur qo'shinining jang tartibi ko'rsatilgan (yuqori tomon — dushman). «A» harfi bilan belgilangan, dushmanga eng yaqin turgan old qism qanday ataladi?", "Ilg'or", ["Qalb", "Javong'or", "Chandovul"], "Oldingi qism — ilg'or.", b="siyosiy", fig=figs.army_formation("A")),
    C(3, "Rasmdagi piramidada Amir Temur qo'shinining bo'linmalari ko'rsatilgan. 3-pog'onadagi (100 kishilik) bo'linma boshlig'i qanday atalgan?", "Yuzboshi", ["O'nboshi", "Mingboshi", "Tumanboshi"], "100 kishilik bo'linma boshlig'i — yuzboshi.", b="siyosiy", fig=figs.hierarchy()),
]

Q["8.1.22-23"] += [
    C(2, "Rasmdagi xronologik chiziqda Amir Temurning yurishlari yillari ko'rsatilgan. 1402-yilga to'g'ri kelgan voqea qaysi?", "Anqara jangi", ["Qunduzcha jangi", "Terek jangi", "Amir Temurning vafoti"], "1402-yil 28-iyul — Anqara jangi.", b="siyosiy", fig=figs.timeline()),
    C(3, "Rasmdagi xronologik chiziqda 1395-yil nuqtasi (B) qaysi voqeaga mos keladi?", "Terek daryosi bo'yidagi jang", ["Qunduzcha jangi", "Anqara jangi", "Dehlining egallanishi"], "1395-yil — Terek jangi.", b="siyosiy", fig=figs.timeline()),
]
