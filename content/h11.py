"""11-sinf: XX asrdan bugungi kungacha — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["11.1.1"] = [
    C(1, "Oktyabr to'ntarishi Petrogradda qaysi yilda bo'lgan?", "1917", ["1905", "1914", "1924"], "25 oktyabr (7 noyabr) 1917.", b="siyosiy"),
    C(1, "Oktyabr to'ntarishidan keyin Rossiyada hokimiyatga kim keldi?", "Bolsheviklar (V.I. Lenin)", ["Muvaqqat hukumat", "Podsho", "Kadetlar"], "Bolsheviklar.", b="siyosiy"),
    C(1, "Toshkentda hokimiyat bolsheviklarga qachon o'tdi?", "1917-yil oktyabr oxiri", ["1917-yil mart", "1918-yil fevral", "1924"], "Oktyabr oxiri.", b="siyosiy"),
    C(2, "Toshkentdagi bolsheviklar rahbari?", "F. Kolesov", ["Kaufman", "Kerenskiy", "Chernyayev"], "Kolesov.", b="siyosiy"),
    C(2, "Toshkentda hokimiyat qaysi organ qo'liga o'tdi?", "Toshkent Sho'rosi", ["Turkiston qo'mitasi", "Muxtoriyat", "Xalq majlisi"], "Sho'ro.", b="siyosiy"),
    C(2, "Turkistonda bolsheviklar hokimiyatining ijtimoiy tayanchi?", "Rus ishchilari va askarlari", ["Dehqonlar", "Ruhoniylar", "Zodagonlar"], "Rus ishchilari.", b="siyosiy"),
    C(3, "Oktyabr to'ntarishidan so'ng Turkiston hokimiyatidan mahalliy xalq?", "Chetlashtirildi", ["Ko'tarildi", "Teng", "Bosh"], "Chetlashtirish.", b="siyosiy"),
    O(3, "Toshkentda bolsheviklar hokimiyati o'rnatilgan yilni yozing.", ["1917", "1917-yil"], "1917.", b="siyosiy"),
]

Q["11.1.2"] = [
    C(1, "Turkiston muxtoriyati qaysi shaharda e'lon qilingan?", "Qo'qon", ["Toshkent", "Samarqand", "Buxoro"], "Qo'qon.", b="siyosiy"),
    C(1, "Turkiston muxtoriyati qachon e'lon qilingan?", "1917-yil 27-noyabr", ["1917-yil oktyabr", "1918-yil fevral", "1924-yil"], "27 noyabr.", b="siyosiy"),
    C(1, "Muxtoriyat qaysi qurultoyda e'lon qilingan?", "IV Umumturkiston musulmonlar qurultoyi", ["I Qurultoy", "II Qurultoy", "V Qurultoy"], "IV.", b="siyosiy"),
    C(2, "Muxtoriyat hukumatining dastlabki bosh vaziri?", "Muhammadjon Tinishboyev", ["Mustafo Cho'qayev", "Munavvarqori", "Behbudiy"], "Tinishboyev.", b="siyosiy"),
    C(2, "Keyinchalik muxtoriyat hukumati boshlig'i?", "Mustafo Cho'qayev", ["Tinishboyev", "Fitrat", "Madaminbek"], "Cho'qayev.", b="siyosiy"),
    C(2, "Muxtoriyat nima edi?", "Turkistonning o'zini o'zi boshqarishi", ["Mustaqil davlat", "Rus gubernatorligi", "Amirlik"], "Muxtoriyat.", b="siyosiy"),
    C(3, "IV Umumturkiston qurultoyi nechanchi noyabrda?", "26–28-noyabr", ["1–3", "10–12", "20–22"], "Qurultoy.", b="siyosiy"),
    O(3, "Turkiston muxtoriyati e'lon qilingan shahar nomini yozing (Q...).", ["Qo'qon", "Qokand", "Qoqon"], "Qo'qon.", b="siyosiy"),
]

Q["11.1.3"] = [
    C(1, "Turkiston muxtoriyati qachon tugatilgan?", "1918-yil fevral", ["1917-yil noyabr", "1920", "1924"], "Fevral 1918.", b="siyosiy"),
    C(1, "Muxtoriyatni tugatish uchun Qo'qonga qaysi qo'shin kirgan?", "Kolesov va Osipov boshchiligidagi qizil askarlar", ["Amir qo'shini", "Xiva qo'shini", "Rus kazaklari"], "Qizil armiya.", b="siyosiy"),
    C(1, "Qo'qon fojeasida qancha aholi halok bo'lgan?", "O'n minglab", ["O'nlab", "Yuzlab", "Ming"], "Qo'qon.", b="siyosiy"),
    C(2, "Muxtoriyatni qo'llab-quvvatlagan qurolli kuch?", "Milliy militsiya va qo'rboshilar", ["Rus polki", "Amir qo'shini", "Kazaklar"], "Militsiya.", b="siyosiy"),
    C(2, "Qo'qonda fevral oylarida qaysi voqea bo'lgan?", "Qo'qon qirg'ini (1918)", ["Anqara jangi", "Loy jangi", "Dandanaqan"], "Qirg'in.", b="siyosiy"),
    C(2, "Muxtoriyat tugatilgach, Cho'qayev?", "Chet elga ketdi", ["Hukumatga qo'shildi", "Qatl qilindi", "Amirga xizmat qildi"], "Muhojir.", b="siyosiy"),
    C(3, "Muxtoriyatning tugatilishi sababi?", "Sho'rolarning mustaqil milliy hukumatni tan olmasligi", ["Moliyaviy inqiroz", "Xalq noroziligi", "Tabiiy ofat"], "Siyosiy.", b="siyosiy"),
    O(3, "Turkiston muxtoriyati qaysi yilda tugatilgan? (raqam)", ["1918", "1918-yil"], "1918.", b="siyosiy"),
]

Q["11.1.4-5"] = [
    C(1, "Farg'ona vodiysidagi yirik qo'rboshi?", "Madaminbek", ["Po'latxon", "Do'kchi eshon", "Fitrat"], "Madaminbek.", b="siyosiy"),
    C(1, "Madaminbek muvaqqat hukumatni qaysi yili tuzgan?", "1919", ["1917", "1918", "1924"], "1919.", b="siyosiy"),
    C(1, "Istiqlolchilik harakati ishtirokchilari qanday ataladi?", "Qo'rboshilar (bosmachi — sovet atamasi)", ["Qizil armiyachilar", "Jadidlar", "Muxtoriyatchilar"], "Qo'rboshi.", b="siyosiy"),
    C(2, "Madaminbek harakatiga qaysi qo'rboshilar qo'shilgan?", "Katta Ergash, Shermuhammadbek (Qo'rshermat)", ["Boburmirzo", "Alimqul", "Po'latxon"], "Qo'rboshilar.", b="siyosiy"),
    C(2, "Buxoro hududida qarshilik harakatiga kim rahbarlik qilgan?", "Ibrohimbek", ["Madaminbek", "Shermuhammad", "Ergash"], "Ibrohimbek.", b="siyosiy"),
    C(2, "Turk generali Anvar posho qaysi yili halok bo'ldi?", "1922", ["1917", "1920", "1924"], "1922.", b="siyosiy"),
    C(3, "Madaminbek qachon halok bo'ldi?", "1920-yil", ["1919", "1922", "1924"], "1920.", b="siyosiy"),
    O(3, "Farg'ona vodiysidagi qo'rboshilarning eng mashhuri bo'lgan Madaminbek harakati qaysi yilda muvaqqat hukumat tuzdi? (raqam)", ["1919", "1919-yil"], "1919.", b="siyosiy"),
]

Q["11.1.6"] = [
    C(1, "Buxoro amirligi qachon ag'darilgan?", "1920-yil", ["1917", "1924", "1868"], "1920.", b="siyosiy"),
    C(1, "Buxoro hujumiga qaysi sarkarda rahbarlik qilgan?", "M.V. Frunze", ["Kolesov", "Skobelev", "Kaufman"], "Frunze.", b="siyosiy"),
    C(1, "Buxorodagi oxirgi amir?", "Sayid Olimxon", ["Muzaffar", "Nasrullo", "Haydar"], "Olimxon.", b="siyosiy"),
    C(2, "Buxoroga hujum qachon bo'ldi?", "1920-yil 2-sentyabr", ["1917-yil 7-noyabr", "1918-yil fevral", "1924-yil oktyabr"], "Sentyabr.", b="siyosiy"),
    C(2, "Xiva xonligi qachon ag'darilgan?", "1920-yil fevral", ["1917-yil", "1924-yil", "1873-yil"], "Xiva.", b="siyosiy"),
    C(2, "Xivaning oxirgi xoni?", "Sayid Abdullaxon", ["Feruz", "Muhammad Rahimxon", "Olloquli"], "Abdulla.", b="siyosiy"),
    C(3, "Amir Olimxon qayerga qochgan?", "Afg'onistonga (Kobul)", ["Eronga", "Rusiyaga", "Xitoyga"], "Kobul.", b="siyosiy"),
    O(3, "Buxoro amirligini ag'dargan 1920-yilgi hujum boshlig'i familiyasini yozing (F...).", ["Frunze", "frunze"], "Frunze.", b="siyosiy"),
]

Q["11.1.7"] = [
    C(1, "Buxoro Xalq Sho'ro Respublikasi (BXSR) qachon e'lon qilingan?", "1920-yil oktyabr", ["1917", "1924", "1925"], "BXSR.", b="siyosiy"),
    C(1, "Xorazm Xalq Sho'ro Respublikasi (XXSR) qachon?", "1920-yil aprel", ["1917", "1924", "1925"], "XXSR.", b="siyosiy"),
    C(1, "BXSR va XXSR qaysi yilda tugatilgan?", "1924", ["1920", "1925", "1930"], "1924.", b="siyosiy"),
    C(2, "BXSR hukumatining raisi?", "Fayzulla Xo'jayev", ["Polvonniyoz Yusupov", "Fitrat", "Munavvarqori"], "Xo'jayev.", b="siyosiy"),
    C(2, "XXSR hukumat boshlig'i?", "Polvonniyoz Yusupov", ["Fayzulla Xo'jayev", "Fitrat", "Behbudiy"], "Yusupov.", b="siyosiy"),
    C(2, "BXSR va XXSR hududlari 1924 yildan keyin nimaning tarkibiga kirdi?", "O'zbekiston SSR va boshqa respublikalar", ["Yangi imperiya", "Xiva", "Eron"], "Chegaralanish.", b="siyosiy"),
    C(3, "BXSR qaysi shaharda poytaxt bo'lgan?", "Buxoro", ["Toshkent", "Xiva", "Samarqand"], "Buxoro.", b="siyosiy"),
    O(3, "Xorazm Xalq Sho'ro Respublikasi hukumat boshlig'i familiyasini yozing (Y...).", ["Yusupov", "Polvonniyoz Yusupov"], "Yusupov.", b="siyosiy"),
]

Q["11.1.8"] = [
    C(1, "O'zbekiston SSR qachon tuzilgan?", "1924-yil 27-oktyabr", ["1920", "1925", "1936"], "1924.", b="siyosiy"),
    C(1, "O'zbekiston SSRning dastlabki poytaxti?", "Samarqand", ["Toshkent", "Buxoro", "Qo'qon"], "Samarqand.", b="siyosiy"),
    C(1, "O'zbekiston SSR poytaxti Toshkentga qachon ko'chirilgan?", "1930", ["1924", "1925", "1936"], "1930.", b="siyosiy"),
    C(2, "O'zbekiston SSR ning birinchi Ta'sis qurultoyi qayerda?", "Buxoroda (1925 fevral)", ["Toshkentda", "Samarqandda", "Xivada"], "Qurultoy.", b="siyosiy"),
    C(2, "O'zbekiston SSR qaysi yilda SSSR tarkibiga qabul qilingan?", "1925", ["1924", "1930", "1936"], "1925.", b="siyosiy"),
    C(2, "Qoraqalpog'iston O'zbekiston tarkibiga qaysi yilda kirgan?", "1936", ["1924", "1925", "1930"], "1936.", b="siyosiy"),
    C(3, "Tojikiston ASSR qaysi yili tuzilgan?", "1924", ["1920", "1929", "1936"], "1924.", b="siyosiy"),
    O(3, "O'zbekiston SSR tuzilgan yilni yozing.", ["1924", "1924-yil"], "1924.", b="siyosiy"),
]

Q["11.1.9"] = [
    C(1, "NEP nima?", "Yangi iqtisodiy siyosat", ["Yangi eski siyosat", "Milliy ozodlik harakati", "Mehnat armiyasi"], "NEP.", b="ijtimoiy"),
    C(1, "NEP qaysi yillarda?", "1921–1928", ["1917–1920", "1930–1940", "1945–1950"], "NEP.", b="ijtimoiy"),
    C(1, "Harbiy kommunizm davrida qanday siyosat olib borilgan?", "Oziq-ovqat razverstkasi", ["Soliq", "Savdo erkinligi", "Xususiy mulk"], "Razverstka.", b="ijtimoiy"),
    C(2, "Harbiy kommunizm qaysi yillarda?", "1918–1921", ["1921–1928", "1930–1940", "1945–1950"], "1918–1921.", b="ijtimoiy"),
    C(2, "NEP davrida razverstka nima bilan almashtirildi?", "Oziq-ovqat solig'i", ["Mehnat armiyasi", "Kolxoz", "Sovxoz"], "Soliq.", b="ijtimoiy"),
    C(2, "NEP davrida xususiy savdo?", "Ruxsat etildi", ["Taqiqlandi", "Davlat qo'lida", "Yo'q"], "Ruxsat.", b="ijtimoiy"),
    O(2, "1921–1928 yillardagi siyosat qisqa nomini yozing (3 harf).", ["NEP", "nep"], "NEP.", b="ijtimoiy"),
    C(3, "NEP siyosati nima uchun to'xtatildi?", "Stalin sanoatlashtirish va kolxozlashtirishni boshladi", ["Savdo yo'qoldi", "Urush boshlandi", "Aholi qarshi chiqdi"], "Stalin.", b="ijtimoiy"),
]

Q["11.1.10"] = [
    C(1, "Kolxozlashtirish qachon boshlangan?", "1929–1930-yillar", ["1917", "1921", "1941"], "30-yillar.", b="ijtimoiy"),
    C(1, "Kolxoz nima?", "Jamoa xo'jaligi", ["Davlat xo'jaligi", "Xususiy fermer", "Aktsiyadorlik"], "Kolxoz.", b="ijtimoiy"),
    C(1, "Quloqlashtirish nima?", "Boy dehqonlarni tugatish siyosati", ["Yer berish", "Soliq kamaytirish", "Mukofot"], "Quloq.", b="ijtimoiy"),
    C(2, "1925–1926 yillardagi yer-suv islohoti maqsadi?", "Boy yer egalaridan yerni olib, kam yerlilarga berish", ["Yer sotish", "Yer sotib olish", "Yer ijaraga"], "Islohot.", b="ijtimoiy"),
    C(2, "Kolxozlashtirish oqibati?", "Dehqonlar mulksizlanishi, ocharchilik", ["Boylik", "Erkinlik", "Ishlab chiqarish ko'payishi"], "Oqibat.", b="ijtimoiy"),
    C(2, "Quloq qilinganlar qayerga surgun qilingan?", "Sibir va Qozog'istonga", ["Yevropaga", "Hindistonga", "Afrikaga"], "Surgun.", b="ijtimoiy"),
    O(2, "Jamoa xo'jaligining qisqa nomini yozing (K...).", ["Kolxoz", "kolxoz"], "Kolxoz.", b="ijtimoiy"),
    C(3, "Kolxozlashtirishga qarshi kurashgan harakat?", "Qo'rboshilar va dehqonlar noroziligi", ["Faqat jadidlar", "Faqat ziyolilar", "Faqat savdogarlar"], "Qarshilik.", b="ijtimoiy"),
]

Q["11.1.11"] = [
    C(1, "Industrializatsiya nima?", "Sanoatlashtirish", ["Kolxozlashtirish", "Urbanizatsiya", "Elektrlashtirish"], "Sanoat.", b="ijtimoiy"),
    C(1, "Katta Farg'ona kanali qaysi yilda qazilgan?", "1939", ["1917", "1924", "1950"], "1939.", b="ijtimoiy"),
    C(1, "Katta Farg'ona kanali necha kunda qazilgan?", "45 kunda", ["10 kunda", "100 kunda", "1 yilda"], "45 kun.", b="ijtimoiy"),
    C(2, "Beshyillik rejalar nima?", "Iqtisodiyotni 5 yillik rejalar asosida boshqarish", ["Qishloq xo'jaligi bayrami", "Soliq tizimi", "Saylov"], "Reja.", b="ijtimoiy"),
    C(2, "O'zbekistonda qurilgan yirik zavod?", "Toshkent qishloq mashinasozlik zavodi", ["Samarqand", "Xiva", "Nukus"], "Zavod.", b="ijtimoiy"),
    C(2, "Chirchiq elektrokimyo kombinati?", "1940-yillarda qurilgan", ["XIX asrda", "XXI asrda", "1980"], "Chirchiq.", b="ijtimoiy"),
    O(2, "Beshyillik rejalar asosida mamlakatni sanoatlashtirishni nima deb ataladi? (I...)", ["Industrializatsiya", "industrializatsiya"], "Industrializatsiya.", b="ijtimoiy"),
    C(3, "Katta Farg'ona kanali qazishda qancha dehqon qatnashgan?", "Taxminan 180 ming", ["5 ming", "50 ming", "1 million"], "Hashar.", b="ijtimoiy"),
]

Q["11.1.12"] = [
    C(1, "«Katta terror» qaysi yillarda?", "1937–1938", ["1917–1918", "1941–1945", "1953–1956"], "Terror.", b="siyosiy"),
    C(1, "«Xalq dushmani» deb kimlarni ayblashgan?", "Hukumat siyosatiga qarshi chiqqanlarni", ["Faqat josuslarni", "Faqat o'g'rilarni", "Faqat chet elliklarni"], "Aybnoma.", b="siyosiy"),
    C(1, "Qatag'on qurboni bo'lgan jadidlardan biri?", "Fayzulla Xo'jayev", ["Mirziyoyev", "Karimov", "Rashidov"], "Qatl.", b="siyosiy"),
    C(2, "Fayzulla Xo'jayev qaysi yili qatl etilgan?", "1938", ["1930", "1941", "1945"], "1938.", b="siyosiy"),
    C(2, "Akmal Ikromov kim?", "O'zbekiston KP birinchi kotibi (1937 qamalgan)", ["Prezident", "Shoir", "General"], "Ikromov.", b="siyosiy"),
    C(2, "Qatag'on organi?", "NKVD", ["KGB", "FSB", "CIA"], "NKVD.", b="siyosiy"),
    C(3, "1937–1938 yillarda O'zbekistonda necha ming kishi qatag'on qilingan?", "Yuz minglab", ["O'nlab", "Yuzlab", "Minglab"], "Ommaviy.", b="siyosiy"),
    O(3, "«Katta terror» boshlangan yilni yozing.", ["1937", "1937-yil"], "1937.", b="siyosiy"),
]

Q["11.1.13"] = [
    C(1, "Cho'lpon qaysi yilda qatl etilgan?", "1938", ["1917", "1924", "1945"], "1938.", b="madaniyat"),
    C(1, "«O'tgan kunlar» romani muallifi?", "Abdulla Qodiriy", ["Cho'lpon", "Fitrat", "G'afur G'ulom"], "Qodiriy.", b="madaniyat"),
    C(1, "Fitrat qaysi yilda qatl etilgan?", "1938", ["1917", "1924", "1945"], "1938.", b="madaniyat"),
    C(2, "«Kecha va kunduz» romani muallifi?", "Cho'lpon", ["Qodiriy", "Fitrat", "Oybek"], "Cho'lpon.", b="madaniyat"),
    C(2, "«O'tgan kunlar» o'zbek adabiyotida nima?", "Birinchi o'zbek romani", ["Birinchi doston", "Birinchi she'r", "Birinchi drama"], "Roman.", b="madaniyat"),
    C(2, "Milliy ziyolilarni qatag'on qilishdan maqsad?", "Milliy ong va o'zlikni yo'q qilish", ["Iqtisodni yaxshilash", "Maorifni rivojlantirish", "Ilmni targ'ib qilish"], "Maqsad.", b="madaniyat"),
    M(2, [("Cho'lpon", "«Kecha va kunduz»"), ("Abdulla Qodiriy", "«O'tgan kunlar»"), ("Hamza", "«Boy ila xizmatchi»")], "Asarlar."),
    C(3, "Hamza Hakimzoda qanday halok bo'lgan?", "Shohimardonda toshbo'ron qilingan (1929)", ["Qatl", "Kasallik", "Avtohalokat"], "1929.", b="madaniyat"),
    O(3, "«O'tgan kunlar» romani muallifi familiyasini yozing (Q...).", ["Qodiriy", "Abdulla Qodiriy"], "Qodiriy.", b="madaniyat"),
]

Q["11.1.14"] = [
    C(1, "Ikkinchi jahon urushi qaysi yillarda?", "1939–1945", ["1914–1918", "1917–1922", "1950–1953"], "1939–1945.", b="siyosiy"),
    C(1, "Germaniya SSSRga qachon hujum qildi?", "1941-yil 22-iyun", ["1939-yil 1-sentyabr", "1945-yil 9-may", "1917-yil"], "22 iyun.", b="siyosiy"),
    C(1, "Urush yillarida O'zbekiston iqtisodiyoti?", "Harbiy izga o'tkazildi", ["Mustaqil bo'ldi", "Sust qoldi", "Inqirozga uchradi"], "Harbiy.", b="siyosiy"),
    C(2, "G'alaba kuni?", "9-may", ["22-iyun", "1-sentyabr", "8-dekabr"], "9 may.", b="siyosiy"),
    C(2, "Urush davrida O'zbekistonda nima ishlab chiqarildi?", "Aviatsiya, qurol-yarog'", ["Faqat paxta", "Faqat meva", "Faqat gilam"], "Harbiy mahsulot.", b="siyosiy"),
    C(2, "SSSRning urushdagi nomi?", "Ulug' Vatan urushi", ["Birinchi jahon", "Qrim urushi", "Sovuq urush"], "Vatan urushi.", b="siyosiy"),
    O(3, "Germaniya SSSRga hujum qilgan yilni yozing.", ["1941", "1941-yil"], "1941.", b="siyosiy"),
    C(3, "Ikkinchi jahon urushi qaysi voqea bilan boshlangan?", "Germaniyaning Polshaga hujumi (1939-yil 1-sentyabr)", ["Germaniyaning SSSRga hujumi", "Perl-Xarbor hujumi", "Berlinning olinishi"], "1939.", b="siyosiy"),
]

Q["11.1.15"] = [
    C(1, "O'zbekistonlik jangchilar urushda qanday qatnashgan?", "Frontning turli yo'nalishlarida jang qilgan", ["Qatnashmagan", "Faqat orqada", "Faqat tibbiyotda"], "Front.", b="siyosiy"),
    C(1, "Urushga ketgan o'zbekistonliklar soni taxminan?", "1,5 million", ["15 ming", "150 ming", "10 million"], "Taxm.", b="siyosiy"),
    C(1, "O'zbekistonlik jangchilar ichida «Sovet Ittifoqi Qahramoni» unvonini olganlar?", "Yuzlab", ["Ikkita", "Hech kim", "Ellik ming"], "Qahramonlar.", b="siyosiy"),
    C(2, "Urushda halok bo'lgan o'zbekistonliklar soni?", "Yarim milliondan ortiq", ["Ming", "O'n ming", "Ellik"], "Taxm.", b="siyosiy"),
    C(2, "Jangchilarni Berlin ostonasigacha yetkazgan?", "Qizil armiya", ["Vermaxt", "Amerika armiyasi", "Inglizlar"], "Qizil.", b="siyosiy"),
    C(2, "Ikkinchi jahon urushi yillarida O'zbekiston frontga nimalar yetkazib bergan?", "Qurol-yarog', oziq-ovqat, kiyim-kechak va minglab jangchi", ["Faqat paxta", "Faqat meva", "Hech narsa"], "Front uchun hamma narsa.", b="siyosiy"),
    O(2, "Ikkinchi jahon urushi Evropada qaysi yil 9-mayda tugagan? (raqam)", ["1945", "1945-yil"], "1945.", b="siyosiy"),
    C(3, "Berlin qachon olingan?", "1945-yil may", ["1941", "1939", "1943"], "May 1945.", b="siyosiy"),
]

Q["11.1.16"] = [
    C(1, "Evakuatsiya nima?", "Aholi va korxonalarni xavfsiz joyga ko'chirish", ["Urushga chaqirish", "Soliq", "Qamoq"], "Evakuatsiya.", b="ijtimoiy"),
    C(1, "Urush yillarida O'zbekistonga ko'chirilgan?", "Yuzlab zavod va minglab etim bolalar", ["Faqat bolalar", "Faqat zavodlar", "Hech narsa"], "Evakuatsiya.", b="ijtimoiy"),
    C(1, "Etim bolalarni o'z uyiga olgan o'zbek oilalari?", "Ko'plab oilalar", ["Hech biri", "Bitta", "Ikkita"], "Mehr.", b="ijtimoiy"),
    C(2, "Shoahmad va Bahri Shomahmudovlar oilasi mashhur bo'lgan?", "Ko'p etim bolalarni tarbiyalagani bilan", ["Zavod qurgani bilan", "Qahramonligi bilan", "Kashfiyoti bilan"], "Mehr.", b="ijtimoiy"),
    C(2, "Evakuatsiya paytida Toshkentga ko'chirilgan?", "Sanoat korxonalari va ilmiy muassasalar", ["Faqat qo'shin", "Faqat bolalar", "Faqat paxta"], "Evakuatsiya.", b="ijtimoiy"),
    C(2, "Etim bolalarni qabul qilish?", "Insoniy fazilat namunasi", ["Majburiyat", "Jazo", "Soliq"], "Mehr.", b="ijtimoiy"),
    O(2, "Aholi va korxonalarni urush xavfidan xavfsiz joyga ko'chirish nima deyiladi? (E...)", ["Evakuatsiya", "evakuatsiya"], "Evakuatsiya.", b="ijtimoiy"),
    C(3, "Urush yillarida Toshkent qanday nom bilan mashhur bo'ldi?", "«Non shahri»", ["«Oltin shahar»", "«Ipak shahri»", "«Tinch shahar»"], "Toshkent.", b="ijtimoiy"),
]

Q["11.1.17"] = [
    C(1, "Sharof Rashidov qaysi yillarda O'zbekiston KP birinchi kotibi?", "1959–1983", ["1937–1939", "1983–1989", "1989–1991"], "Rashidov.", b="siyosiy"),
    C(1, "Rashidov davrida respublika iqtisodiyoti?", "Paxta yakkahokimligi kuchaydi", ["Neft", "Ko'mir", "Elektronika"], "Paxta.", b="siyosiy"),
    C(1, "Rashidov vafot etgan yili?", "1983", ["1959", "1989", "1991"], "1983.", b="siyosiy"),
    C(2, "Urushdan keyin O'zbekiston tiklanishida muhim?", "Sanoat va qishloq xo'jaligi", ["Faqat madaniyat", "Faqat harbiy", "Faqat savdo"], "Tiklanish.", b="siyosiy"),
    C(2, "Rashidov davrida qurilgan?", "Toshkent metrosi (1977)", ["Samarqand metro", "Nukus metro", "Buxoro metro"], "Metro.", b="siyosiy"),
    C(2, "Toshkent metrosi qachon ochilgan?", "1977", ["1966", "1983", "1991"], "1977.", b="siyosiy"),
    C(3, "Rashidov yozuvchi sifatida ham mashhur — asari?", "«G'oliblar»", ["«O'tgan kunlar»", "«Kecha va kunduz»", "«Navoiy»"], "Rashidov.", b="madaniyat"),
    O(3, "Toshkent metropoliteni ochilgan yilni yozing.", ["1977", "1977-yil"], "1977.", b="siyosiy"),
]

Q["11.1.18"] = [
    C(1, "Toshkent zilzilasi qachon bo'lgan?", "1966-yil 26-aprel", ["1917", "1983", "1991"], "26 aprel.", b="siyosiy"),
    C(1, "Zilzila oqibatida?", "Toshkent shahri ko'p qismi vayron bo'ldi", ["Hech narsa", "Faqat qishloqlar", "Faqat tog'lar"], "Vayronagarlik.", b="siyosiy"),
    C(1, "Toshkentni qayta tiklashga kim yordam bergan?", "SSSR respublikalari", ["Faqat Rossiya", "Faqat Amerika", "Faqat Xitoy"], "Birodarlik.", b="siyosiy"),
    C(2, "Zilzila markazi?", "Toshkent shahri", ["Samarqand", "Andijon", "Termiz"], "Toshkent.", b="siyosiy"),
    C(2, "Zilzila kuchi taxminan?", "8 ball", ["3 ball", "5 ball", "12 ball"], "8 ball.", b="siyosiy"),
    C(2, "Zilzilaga bardosh yangi quriladigan binolar?", "Seysmik bardoshli", ["Yog'och", "G'ishtdan", "Tomi tekis"], "Qurilish.", b="siyosiy"),
    C(3, "Zilzila yodgorligi?", "«Jasorat» (Mardlik) monumenti", ["Mustaqillik", "Amir Temur", "Navoiy"], "Mardlik.", b="madaniyat"),
    O(3, "Toshkent zilzilasi qaysi yilda sodir bo'lgan? (raqam)", ["1966", "1966-yil"], "1966.", b="siyosiy"),
]

Q["11.1.19"] = [
    C(1, "«Paxta ishi» qaysi yillarda?", "1983–1989", ["1937–1938", "1941–1945", "1991–1992"], "Paxta ishi.", b="siyosiy"),
    C(1, "«Paxta ishi»ni olib borgan tergovchilar?", "Gdlyan va Ivanov", ["Rashidov", "Karimov", "Gorbachev"], "Gdlyan.", b="siyosiy"),
    C(1, "«Paxta ishi» oqibati?", "O'zbek rahbarlari va ziyolilari qatag'on qilindi", ["Iqtisod ko'tarildi", "Tinchlik", "Mustaqillik"], "Qatag'on.", b="siyosiy"),
    C(2, "«Paxta ishi»ning boshqa nomi?", "«O'zbeklar ishi»", ["«Yer ishi»", "«Neft ishi»", "«Temir ishi»"], "O'zbeklar ishi.", b="siyosiy"),
    C(2, "«Paxta ishi» davrida Moskvaning maqsadi?", "O'zbekistonni nazorat ostiga olish", ["Yordam", "Hamkorlik", "Mustaqillik berish"], "Nazorat.", b="siyosiy"),
    C(2, "«Paxta ishi» yillarida o'zbek rahbarlari nima uchun ayblangan?", "Paxta hosilini oshirib ko'rsatish va poraxo'rlikda", ["Davlat to'ntarishida", "Josuslikda", "Dinni targ'ib qilishda"], "Soxta ayblovlar.", b="siyosiy"),
    C(3, "«Paxta ishi» qachon to'xtatilgan?", "1989", ["1983", "1991", "1937"], "1989.", b="siyosiy"),
    O(3, "Tergovchilar Gdlyan va Ivanov olib borgan ish nomini yozing («Paxta ...»).", ["Paxta ishi", "ishi", "paxta ishi"], "Paxta ishi.", b="siyosiy"),
]

Q["11.1.20"] = [
    C(1, "Islom Karimov qachon tug'ilgan?", "1938-yil 30-yanvar", ["1917", "1925", "1953"], "30 yanvar.", b="siyosiy"),
    C(1, "Islom Karimov qayerda tug'ilgan?", "Samarqand", ["Toshkent", "Buxoro", "Qarshi"], "Samarqand.", b="siyosiy"),
    C(1, "Islom Karimov O'zbekiston KP birinchi kotibi bo'lgan yil?", "1989", ["1983", "1991", "1938"], "1989.", b="siyosiy"),
    C(2, "I. Karimov O'zbekiston SSR Prezidenti bo'lgan yil?", "1990-yil 24-mart", ["1989", "1991", "1992"], "24 mart.", b="siyosiy"),
    C(2, "I. Karimov birinchi Prezident saylovi?", "1991-yil 29-dekabr", ["1990", "1992", "1995"], "Saylov.", b="siyosiy"),
    C(2, "Karimov vafot etgan yil?", "2016", ["2010", "1991", "2020"], "2016.", b="siyosiy"),
    C(3, "I. Karimov nechanchi sentyabrda vafot etdi?", "2-sentyabr", ["1-sentyabr", "31-avgust", "8-dekabr"], "2016.", b="siyosiy"),
    O(3, "I. Karimov O'zbekiston KP birinchi kotibi saylangan yilni yozing.", ["1989", "1989-yil"], "1989.", b="siyosiy"),
]

Q["11.1.21-22"] = [
    C(1, "Davlat tili haqidagi qonun qaysi yilda?", "1989-yil 21-oktyabr", ["1990", "1991", "1992"], "Oktyabr.", b="siyosiy"),
    C(1, "Mustaqillik deklaratsiyasi qachon qabul qilingan?", "1990-yil 20-iyun", ["1991-yil 31-avgust", "1992-yil 8-dekabr", "1989"], "Deklaratsiya.", b="siyosiy"),
    C(1, "Mustaqillik e'lon qilingan sana?", "1991-yil 31-avgust", ["1990-yil 20-iyun", "1992", "1989"], "Mustaqillik.", b="siyosiy"),
    C(2, "Mustaqillik kuni qachon nishonlanadi?", "1-sentyabr", ["31-avgust", "8-dekabr", "21-oktyabr"], "1 sentyabr.", b="siyosiy"),
    C(2, "Mustaqillik e'lon qilingan sessiya?", "O'zbekiston SSR Oliy Kengashining navbatdan tashqari sessiyasi", ["Xalq qurultoyi", "Referendum", "Prezident farmoni"], "Sessiya.", b="siyosiy"),
    C(2, "Davlat tili qonuni bo'yicha davlat tili?", "O'zbek tili", ["Rus tili", "Ingliz tili", "Tojik tili"], "O'zbek.", b="siyosiy"),
    C(3, "Mustaqillik haqida referendum qachon?", "1991-yil 29-dekabr", ["1990", "1992", "1995"], "Referendum.", b="siyosiy"),
    O(3, "Mustaqillik e'lon qilingan yilni yozing.", ["1991", "1991-yil"], "1991.", b="siyosiy"),
    O(3, "Mustaqillik deklaratsiyasi qabul qilingan yilni yozing.", ["1990", "1990-yil"], "1990.", b="siyosiy"),
]

Q["11.1.23"] = [
    C(1, "O'zbekiston Konstitutsiyasi qachon qabul qilingan?", "1992-yil 8-dekabr", ["1991-yil 31-avgust", "1990", "1995"], "8 dekabr.", b="siyosiy"),
    C(1, "Konstitutsiya kuni qachon?", "8-dekabr", ["1-sentyabr", "31-avgust", "21-oktyabr"], "8 dekabr.", b="siyosiy"),
    C(1, "Konstitutsiyani qabul qilgan organ?", "Oliy Kengash", ["Prezident", "Referendum", "Senat"], "Oliy Kengash.", b="siyosiy"),
    C(2, "1992-yilgi Konstitutsiya nechta moddadan iborat?", "128", ["100", "155", "200"], "128.", b="siyosiy"),
    C(2, "Konstitutsiya nechanchi sessiyada qabul qilingan?", "XI sessiya (XII chaqiriq)", ["I", "V", "XX"], "XI sessiya.", b="siyosiy"),
    C(2, "Konstitutsiya asosiy qoidasi?", "Xalq davlat hokimiyatining yagona manbai", ["Prezident hokimiyati", "Oliy kengash", "Partiya"], "Xalq.", b="siyosiy"),
    C(3, "Konstitutsiya boblari soni?", "26 bob, 6 bo'lim", ["10 bob", "100 bob", "5 bo'lim"], "Tuzilma.", b="siyosiy"),
    O(3, "Konstitutsiya qabul qilingan yilni yozing.", ["1992", "1992-yil"], "1992.", b="siyosiy"),
]

Q["11.1.24"] = [
    C(1, "O'zbekiston davlat bayrog'i qachon qabul qilingan?", "1991-yil 18-noyabr", ["1992", "1994", "1995"], "Bayroq.", b="siyosiy"),
    C(1, "Davlat gerbi qachon?", "1992-yil 2-iyul", ["1991", "1994", "1995"], "Gerb.", b="siyosiy"),
    C(1, "Davlat madhiyasi qachon?", "1992-yil 10-dekabr", ["1991", "1994", "1995"], "Madhiya.", b="siyosiy"),
    C(2, "Gerbdagi qush?", "Semurg' (Humo)", ["Burgut", "Qarg'a", "Laylak"], "Humo.", b="siyosiy"),
    C(2, "Madhiya so'zlari muallifi?", "Abdulla Oripov", ["Erkin Vohidov", "G'afur G'ulom", "Oybek"], "Oripov.", b="madaniyat"),
    C(2, "Madhiya musiqasi muallifi?", "Mutal Burhonov", ["Hamza", "Ulug'bek", "Navoiy"], "Burhonov.", b="madaniyat"),
    C(3, "Milliy valyuta «so'm» qachon muomalaga kirgan?", "1994-yil 1-iyul", ["1991", "1992", "1993"], "So'm.", b="siyosiy"),
    O(3, "Milliy valyuta so'm muomalaga kiritilgan yilni yozing.", ["1994", "1994-yil"], "1994.", b="siyosiy"),
]

Q["11.1.25"] = [
    C(1, "O'zbekiston iqtisodiy modeli kimning nomi bilan bog'liq?", "Islom Karimov", ["Mirziyoyev", "Rashidov", "Ulug'bek"], "Karimov.", b="ijtimoiy"),
    C(1, "«O'zbek modeli» tamoyillari soni?", "5", ["3", "7", "10"], "Besh tamoyil.", b="ijtimoiy"),
    C(1, "Birinchi tamoyil?", "Iqtisodiyotning siyosatdan ustunligi", ["Davlat — bosh islohotchi", "Qonun ustuvorligi", "Bosqichma-bosqich"], "Birinchi.", b="ijtimoiy"),
    C(2, "Qaysi biri o'zbek modeli tamoyili emas?", "Iqtisod harbiy ustuvorligi", ["Davlat — bosh islohotchi", "Qonun ustuvorligi", "Kuchli ijtimoiy siyosat"], "Tamoyil.", b="ijtimoiy"),
    C(2, "Iqtisodiyotni bosqichma-bosqich o'tkazish?", "Tamoyillardan biri", ["Shart emas", "Xalqaro bosim", "Ta'qiqlangan"], "Bosqich.", b="ijtimoiy"),
    O(2, "«O'zbek modeli»ning nechta tamoyili bor? (raqam)", ["5", "besh"], "5.", b="ijtimoiy"),
    C(3, "Mustaqillik yillarida iqtisodiyotda xususiylashtirish?", "Mulkdorlar sinfini shakllantirdi", ["Davlat mulkini ko'paytirdi", "Boylikni kamaytirdi", "Savdoni taqiqladi"], "Xususiylashtirish.", b="ijtimoiy"),
    C(3, "Iqtisodiy islohotlarda davlat roli?", "Bosh islohotchi", ["Kuzatuvchi", "Ishtirok yo'q", "Raqib"], "Davlat.", b="ijtimoiy"),
]

Q["11.1.26"] = [
    C(1, "O'zbekiston BMTga qachon a'zo bo'lgan?", "1992-yil 2-mart", ["1991", "1993", "2001"], "BMT.", b="siyosiy"),
    C(1, "O'zbekiston YUNESKOga qachon a'zo bo'lgan?", "1993-yil 29-oktyabr", ["1992", "1991", "2001"], "YUNESKO.", b="siyosiy"),
    C(1, "BMTga a'zo bo'lganida?", "Bayroq ko'tarildi", ["Qo'shin kirdi", "Prezident ketdi", "Referendum"], "BMT.", b="siyosiy"),
    C(2, "O'zbekiston MDHga qaysi yili a'zo?", "1991-yil dekabr", ["1992", "1993", "2001"], "MDH.", b="siyosiy"),
    C(2, "O'zbekiston qaysi shahrida BMT bayrog'i?", "Nyu-York", ["Jeneva", "Parij", "Moskva"], "Nyu-York.", b="siyosiy"),
    C(2, "O'zbekiston xalqaro maydondagi siyosati?", "Neytral va hamkorlik", ["Harbiy blok", "Yopiq", "Bosqinchi"], "Siyosat.", b="siyosiy"),
    C(3, "O'zbekistonga YUNESKO nima beradi?", "Madaniy meros himoyasi", ["Qurol", "Kredit", "Soliq"], "Meros.", b="siyosiy"),
    O(3, "O'zbekiston BMTga a'zo bo'lgan yilni yozing.", ["1992", "1992-yil"], "1992.", b="siyosiy"),
]

Q["11.1.27"] = [
    C(1, "Shavkat Mirziyoyev qaysi yili Prezident bo'lgan?", "2016", ["2010", "2020", "1991"], "Dekabr 2016.", b="siyosiy"),
    C(1, "Mirziyoyev qasamyod qilgan sana?", "2016-yil 14-dekabr", ["2016-yil 4-dekabr", "2017", "2020"], "14 dekabr.", b="siyosiy"),
    C(1, "Prezident saylovi qachon bo'lgan?", "2016-yil 4-dekabr", ["2016-yil 14-dekabr", "2017", "2020"], "Saylov.", b="siyosiy"),
    C(2, "«Yangi O'zbekiston» siyosati?", "Islohotlar va ochiqlik", ["Yopiqlik", "Mustamlaka", "Harbiy"], "Yangi.", b="siyosiy"),
    C(2, "Mirziyoyev avval qanday lavozimda edi?", "Bosh vazir", ["Vazir", "Hokim", "Elchi"], "Bosh vazir.", b="siyosiy"),
    C(2, "2016-yil prezident saylovida g'olib?", "Shavkat Mirziyoyev", ["Karimov", "Rashidov", "Usmonxo'jayev"], "Saylov.", b="siyosiy"),
    C(3, "Mirziyoyev qaysi yili qayta saylangan?", "2021", ["2017", "2020", "2022"], "Oktyabr 2021.", b="siyosiy"),
    O(3, "Mirziyoyev Prezident bo'lgan yilni yozing.", ["2016", "2016-yil"], "2016.", b="siyosiy"),
]

Q["11.1.28"] = [
    C(1, "Harakatlar strategiyasi qaysi yillarga mo'ljallangan?", "2017–2021", ["2022–2026", "2023–2030", "2010–2015"], "Harakatlar.", b="siyosiy"),
    C(1, "Taraqqiyot strategiyasi qaysi yillarga mo'ljallangan?", "2022–2026", ["2017–2021", "2023–2030", "2010–2015"], "Taraqqiyot.", b="siyosiy"),
    C(1, "Harakatlar strategiyasida nechta ustuvor yo'nalish?", "5", ["3", "7", "10"], "Besh.", b="siyosiy"),
    C(2, "Taraqqiyot strategiyasida ustuvor yo'nalishlar soni?", "7", ["5", "3", "10"], "Yetti.", b="siyosiy"),
    C(2, "Taraqqiyot strategiyasida nechta maqsad?", "100", ["50", "10", "200"], "100.", b="siyosiy"),
    C(2, "Strategiyalar maqsadi?", "Mamlakatni rivojlantirish va inson manfaati", ["Harbiy", "Din", "Yopiqlik"], "Rivoj.", b="siyosiy"),
    C(3, "Taraqqiyot strategiyasi qaysi yili qabul qilindi?", "2022 (yanvar)", ["2016", "2018", "2020"], "2022.", b="siyosiy"),
    O(3, "Harakatlar strategiyasi nechta ustuvor yo'nalishdan iborat? (raqam)", ["5", "besh"], "5.", b="siyosiy"),
]

Q["11.1.29"] = [
    C(1, "Konstitutsiyaviy referendum qachon bo'lgan?", "2023-yil 30-aprel", ["2016", "2021", "2022"], "30 aprel.", b="siyosiy"),
    C(1, "Yangi tahrirdagi Konstitutsiya nechta moddadan iborat?", "155", ["128", "100", "200"], "155.", b="siyosiy"),
    C(1, "Yangi Konstitutsiya qachon kuchga kirgan?", "2023-yil 1-may", ["2016", "2021", "2022"], "1 may.", b="siyosiy"),
    C(2, "Yangi Konstitutsiyada Prezident muddati?", "7 yil", ["4 yil", "5 yil", "10 yil"], "7 yil.", b="siyosiy"),
    C(2, "Yangi tahrirda O'zbekiston?", "Ijtimoiy davlat sifatida belgilangan", ["Monarxiya", "Harbiy", "Teokratiya"], "Ijtimoiy.", b="siyosiy"),
    C(2, "Referendumda qatnashganlar?", "Fuqarolar", ["Faqat deputatlar", "Faqat prezident", "Chet elliklar"], "Referendum.", b="siyosiy"),
    C(3, "Yangi Konstitutsiyaning bo'limlari soni?", "6", ["3", "10", "12"], "Bo'lim.", b="siyosiy"),
    O(3, "Konstitutsiyaviy referendum bo'lgan yilni yozing.", ["2023", "2023-yil"], "2023.", b="siyosiy"),
]

Q["11.1.30"] = [
    C(1, "«O'zbekiston – 2030» strategiyasi qaysi yilda qabul qilingan?", "2023", ["2016", "2017", "2021"], "2023.", b="siyosiy"),
    C(1, "Strategiyaning bosh g'oyasi?", "Inson qadri va xalq farovonligi", ["Harbiy", "Din", "Yopiqlik"], "Inson.", b="siyosiy"),
    C(1, "Strategiya qaysi yilgacha?", "2030", ["2025", "2035", "2040"], "2030.", b="siyosiy"),
    C(2, "Strategiya yo'nalishlari soni?", "5", ["3", "7", "10"], "Besh.", b="siyosiy"),
    C(2, "Strategiya maqsadlari?", "Daromadni oshirish, ta'lim va sog'liqni rivojlantirish", ["Faqat harbiy", "Faqat din", "Faqat savdo"], "Maqsad.", b="siyosiy"),
    C(2, "Strategiyada qaysi yo'nalish bor?", "Adolat, ta'lim va iqtisodiy o'sish", ["Faqat iqlim", "Faqat sport", "Faqat sayyohlik"], "Yo'nalish.", b="siyosiy"),
    C(3, "Strategiyani qabul qilgan?", "Prezident farmoni bilan", ["Referendum", "Senat", "Qurultoy"], "Farmon.", b="siyosiy"),
    O(3, "«O'zbekiston – 2030» strategiyasi qaysi yilgacha mo'ljallangan? (raqam)", ["2030", "2030-yil"], "2030.", b="siyosiy"),
]

Q["11.1.31"] = [
    C(1, "ShHT (Shanxay hamkorlik tashkiloti) qaysi yili tuzilgan?", "2001-yil 15-iyun", ["1991", "1992", "2017"], "2001.", b="siyosiy"),
    C(1, "O'zbekiston ShHTga qaysi shaharda qo'shilgan?", "Shanxay", ["Pekin", "Moskva", "Toshkent"], "Shanxay.", b="siyosiy"),
    C(1, "Turkiy Davlatlar Tashkiloti qaysi yili nomlangan?", "2021", ["2001", "2009", "2017"], "TDT.", b="siyosiy"),
    C(2, "Turkiy Kengash qachon tuzilgan?", "2009 (Naxichevan)", ["2001", "2017", "2021"], "2009.", b="siyosiy"),
    C(2, "O'zbekiston Turkiy Kengashga qaysi yili qo'shilgan?", "2019", ["2009", "2017", "2021"], "2019.", b="siyosiy"),
    C(2, "ShHT asoschilari qatorida?", "Xitoy, Rossiya, Qozog'iston, Qirg'iziston, Tojikiston, O'zbekiston", ["AQSh", "Yaponiya", "Hindiston faqat"], "ShHT.", b="siyosiy"),
    C(3, "TDT sammiti 2021 yilda qaysi shaharda?", "Istanbul", ["Toshkent", "Boku", "Astana"], "Istanbul.", b="siyosiy"),
    O(3, "ShHT tuzilgan yilni yozing.", ["2001", "2001-yil"], "2001.", b="siyosiy"),
]
