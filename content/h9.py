"""9-sinf: Xonliklar davri (XVI – XIX asr o'rtalari) — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["9.1.1"] = [
    C(1, "Ko'chmanchi o'zbeklar davlatining asoschisi kim?", "Abulxayrxon", ["Muhammad Shayboniyxon", "Abdullaxon II", "Ubaydullaxon"], "1428-yil.", b="siyosiy"),
    C(1, "Abulxayrxon davlati qaysi yilda tashkil topgan?", "1428", ["1500", "1370", "1599"], "1428.", b="siyosiy"),
    C(1, "Muhammad Shayboniyxon Abulxayrxonning kimi edi?", "Nabirasi", ["O'g'li", "Ukasi", "Ustozi"], "Nabira.", b="siyosiy"),
    C(2, "Shayboniylar sulolasi Samarqandni qaysi yili egallagan?", "1500", ["1428", "1510", "1598"], "1500.", b="siyosiy"),
    C(2, "Abulxayr davlatining dastlabki poytaxti?", "Sig'noq", ["Samarqand", "Buxoro", "Urganch"], "Sig'noq.", b="siyosiy"),
    C(2, "Abulxayrxon qaysi yilda vafot etgan?", "1468", ["1428", "1500", "1510"], "1468.", b="siyosiy"),
    C(3, "Shayboniylar davlati hududi Movarounnahrdan tashqari yana qaysi hududlarni qamragan?", "Xorazm, Xuroson (Hirot), Farg'ona", ["Hindiston", "Misr", "Rusiya"], "Keng hudud.", b="siyosiy"),
    O(3, "Abulxayrxon davlati qaysi yilda tuzilgan? (raqam)", ["1428", "1428-yil"], "1428.", b="siyosiy"),
    O(3, "Shayboniylar sulolasi xonlaridan Samarqandni 1500-yilda egallagan hukmdor ismini yozing (Muhammad ...).", ["Muhammad Shayboniyxon", "Shayboniyxon", "Shayboniy", "Muhammad Shayboniy"], "Muhammad Shayboniyxon.", b="siyosiy"),
]

Q["9.1.2-3"] = [
    C(1, "Saripul jangi qaysi yilda bo'lgan?", "1501", ["1500", "1510", "1598"], "1501.", b="siyosiy"),
    C(1, "Saripul jangida Shayboniyxon kimni mag'lub etdi?", "Zahiriddin Boburni", ["Ulug'bekni", "Husayn Boyqaroni", "Abu Saidni"], "Bobur.", b="siyosiy"),
    C(1, "Marv jangi qaysi yilda bo'lgan?", "1510", ["1501", "1500", "1598"], "1510.", b="siyosiy"),
    C(2, "Marv jangida Shayboniyxon kim bilan jang qilgan?", "Eron shohi Ismoil Safaviy", ["Bobur", "Husayn Boyqaro", "Ubaydulla"], "Safaviy.", b="siyosiy"),
    C(2, "Marv jangidan so'ng Shayboniyxon nima bo'ldi?", "Halok bo'ldi", ["G'alaba qozondi", "Asirga tushdi", "Taxtdan voz kechdi"], "1510.", b="siyosiy"),
    C(2, "Shayboniyxon Xorazmni qaysi yillarda egallagan?", "1505–1506", ["1500–1501", "1510", "1370"], "1505–1506.", b="siyosiy"),
    C(3, "Shayboniylar Hirotni qaysi yili qo'lga kiritgan?", "1507", ["1500", "1510", "1598"], "1507.", b="siyosiy"),
    O(3, "Shayboniyxon halok bo'lgan Marv jangi yilini yozing.", ["1510", "1510-yil"], "1510.", b="siyosiy"),
]

Q["9.1.4"] = [
    C(1, "Shayboniylar davlatining boshlig'i kim edi?", "Xon", ["Satrap", "Imperator", "Prezident"], "Xon.", b="siyosiy"),
    C(1, "Shayboniylarda viloyatlarni kimlar boshqargan?", "Sulton unvonli xon avlodlari", ["Rus gubernatorlari", "Dehqonlar", "Savdogarlar"], "Sultonlar.", b="siyosiy"),
    C(1, "Shayboniylar davlatida katta yer egalarining mulki qanday atalgan?", "Suyurg'ol (xon in'omi)", ["Vaqf", "Mulk", "Xiroj"], "Suyurg'ol.", b="ijtimoiy"),
    C(2, "Shayboniylar davlatining ma'muriy tuzilishi qanday edi?", "Ulus (viloyat)lar sultonlar qo'l ostida edi", ["Yagona markazlashgan", "Konfederatsiya", "Respublika"], "Ulus tizimi.", b="siyosiy"),
    C(2, "Shayboniylar davrida qozikalon qanday vazifa bajargan?", "Oliy sudya", ["Moliya vaziri", "Bosh sarkarda", "Elchi"], "Qozikalon.", b="siyosiy"),
    C(2, "Shayboniylar davrida shayxulislom kim?", "Diniy ishlar boshlig'i", ["Bosh qo'mondon", "Elchi", "Soliqchi"], "Dinoyat.", b="siyosiy"),
    C(3, "Shayboniylar davlatining ichki zaifligi nimada edi?", "Sultonlarning o'zaro kurashi va parchalanish", ["Dengiz urushi", "Dehqonlar yo'qligi", "Soliq yo'qligi"], "Tarqoqlik.", b="siyosiy"),
    O(3, "Shayboniylarda viloyatni boshqaruvchi xon avlodlari qaysi unvonda atalgan? (S...)", ["sulton", "Sulton"], "Sulton.", b="siyosiy"),
]

Q["9.1.5"] = [
    C(1, "Abdullaxon II qaysi yillarda hukmronlik qilgan?", "1583–1598", ["1500–1510", "1601–1611", "1740–1747"], "1583–1598.", b="siyosiy"),
    C(1, "Abdullaxon II davrida poytaxt qaysi shahar edi?", "Buxoro", ["Samarqand", "Toshkent", "Xiva"], "Buxoro.", b="siyosiy"),
    C(1, "Abdullaxon II qaysi sulolaning vakili edi?", "Shayboniylar", ["Ashtarxoniylar", "Mang'itlar", "Minglar"], "Shayboniy.", b="siyosiy"),
    C(2, "Buxorodagi mashhur savdo gumbazlari — toqlar qaysi?", "Toqi Zargaron, Toqi Telpakfurushon, Toqi Sarrofon", ["Registon, Ark, Poyi Kalon", "Kalon, Mir Arab, Ulug'bek", "Sherdor, Tillaqori, Ulug'bek"], "Toqlar.", b="madaniyat"),
    C(2, "Abdullaxon II davrida nima mustahkamlandi?", "Markaziy hokimiyat", ["Sultonlar mustaqilligi", "Dehqonlar yer huquqi", "Arab hokimiyati"], "Markazlashtirish.", b="siyosiy"),
    C(2, "Abdullaxon II qurdirgan karvonsaroyi?", "Sardoba va rabotlar", ["Raboti Malik", "Registon", "Ark"], "Rabotlar.", b="madaniyat"),
    C(3, "Abdullaxon II vafot yili?", "1598", ["1583", "1599", "1601"], "1598.", b="siyosiy"),
    O(3, "Abdullaxon II davrida Buxoro qaysi asr oxirida (raqam bilan yozing, masalan XVI) poytaxt bo'lgan?", ["XVI", "16"], "Abdullaxon II 1583–1598 yillarda — XVI asr.", b="siyosiy"),
]

Q["9.1.6"] = [
    C(1, "Shayboniylar sulolasi qachon tugatilgan?", "1598-yilda", ["1500", "1510", "1740"], "1598.", b="siyosiy"),
    C(1, "Shayboniylar o'rniga Buxoroda qaysi sulola hokimiyatga keldi?", "Ashtarxoniylar (Joniylar)", ["Mang'itlar", "Minglar", "Qo'ng'irotlar"], "Ashtarxoniylar.", b="siyosiy"),
    C(1, "Ashtarxoniylar sulolasi qachon boshlangan?", "1599–1601-yillar", ["1500", "1740", "1785"], "XVII asr boshi.", b="siyosiy"),
    C(2, "Ashtarxoniylar sulolasining asoschisi?", "Boqi Muhammadxon", ["Imomqulixon", "Nodir", "Abdulazizxon"], "Boqi Muhammad.", b="siyosiy"),
    C(2, "Shayboniylar oxirgi xoni?", "Pirmuhammadxon II", ["Abdullaxon", "Ubaydulla", "Shayboniy"], "Pirmuhammad.", b="siyosiy"),
    C(2, "Ashtarxoniylarning boshqa nomi?", "Joniylar", ["Barlos", "Mang'it", "Ming"], "Joniylar.", b="siyosiy"),
    C(3, "Ashtarxoniylar sulolasining tugatilishi sababi?", "Nodirshoh yurishi (1740) va ichki parchalanish", ["Mo'g'ul bosqini", "Arab bosqini", "Rus bosqini"], "Nodirshoh.", b="siyosiy"),
    O(3, "Shayboniylar o'rniga hokimiyatga kelgan sulola nomi (A...) yozing.", ["Ashtarxoniylar", "ashtarxoniylar", "Joniylar"], "Ashtarxoniylar.", b="siyosiy"),
]

Q["9.1.7"] = [
    C(1, "Registon ansamblidagi Sherdor madrasasi qaysi yillarda qurilgan?", "1619–1636", ["1417–1420", "1646–1660", "1127"], "Sherdor.", b="madaniyat"),
    C(1, "Tillaqori madrasasi qaysi yillarda qurilgan?", "1646–1660", ["1619–1636", "1417–1420", "1127"], "Tillaqori.", b="madaniyat"),
    C(1, "Sherdor va Tillaqori madrasalarini kim qurdirgan?", "Yalangto'sh Bahodir", ["Ulug'bek", "Amir Temur", "Shohruh"], "Yalangto'sh.", b="madaniyat"),
    C(2, "Sherdor madrasasi peshtoqidagi tasvir?", "Quyosh va sher (arslon)", ["Fil", "Burgut", "Ajdar"], "Sherdor.", b="madaniyat"),
    C(2, "Sherdor madrasasining bosh me'mori?", "Abduljabbor", ["Baqo", "Ismoil", "Usto Sharif"], "Abduljabbor.", b="madaniyat"),
    C(2, "Imomqulixon qaysi yillarda hukmdor bo'lgan?", "1611–1642", ["1500–1510", "1598–1601", "1740–1747"], "Imomquli.", b="siyosiy"),
    M(2, [("Ulug'bek madrasasi", "1417–1420"), ("Sherdor madrasasi", "1619–1636"), ("Tillaqori madrasasi", "1646–1660")], "Registon.", ),
    C(3, "Tillaqori madrasasi qanday vazifalarni bajargan?", "Ham masjid, ham madrasa", ["Rasadxona", "Karvonsaroy", "Maqbara"], "Tillaqori.", b="madaniyat"),
    O(3, "Registon ansamblini yakunlagan Tillaqori madrasasi qaysi yilda qurib bitkazilgan? (raqam)", ["1660", "1660-yil"], "1660.", b="madaniyat"),
]

Q["9.1.8"] = [
    C(1, "Subhonqulixon qaysi yillarda hukmronlik qilgan?", "1680–1702", ["1611–1642", "1740–1747", "1500–1510"], "Subhonquli.", b="siyosiy"),
    C(1, "Ubaydullaxon II qaysi davlat xoni edi?", "Buxoro xonligi (Ashtarxoniylar)", ["Xiva", "Qo'qon", "Bobur davlati"], "Ashtarxoniy.", b="siyosiy"),
    C(1, "Ashtarxoniylar davrining ikkinchi yarmida nima kuchaydi?", "Mang'it beklari va tarqoqlik", ["Markazlashgan hokimiyat", "Dengiz floti", "Rus ta'siri faqat"], "Tarqoqlik.", b="siyosiy"),
    C(2, "Abulfayzxon qaysi yillarda nominal xon edi?", "1711–1747", ["1500–1510", "1598–1601", "1611–1642"], "Abulfayz.", b="siyosiy"),
    C(2, "Abulfayzxonni o'ldirgan amir?", "Muhammad Rahimbiy", ["Doniyolbiy", "Nodir", "Haydar"], "Rahimbiy.", b="siyosiy"),
    C(2, "Subhonqulixon qurdirgan Buxorodagi inshoot?", "Subhonquli madrasasi (va Chorsu)", ["Ark", "Registon", "Kalon"], "Subhonquli.", b="madaniyat"),
    C(3, "Ashtarxoniylar davrida yirik yer egalari kimlar bo'lgan?", "Mang'it, Qo'ng'irot kabi qabila beklari", ["Rus dvoryanlari", "Hind savdogarlari", "Yunon kolonistlari"], "Qabila beklari.", b="ijtimoiy"),
    O(3, "Abulfayzxon qaysi yili o'ldirilgan? (raqam)", ["1747", "1747-yil"], "1747.", b="siyosiy"),
]

Q["9.1.9"] = [
    C(1, "Nodirshohning Buxoroga yurishi qaysi yilda?", "1740", ["1747", "1598", "1500"], "1740.", b="siyosiy"),
    C(1, "Nodirshoh qaysi davlat hukmdori edi?", "Eron (Afshoriylar)", ["Rusiya", "Hindiston", "Usmonli"], "Eron.", b="siyosiy"),
    C(1, "Nodirshohga qarshi Buxoro xoni kim edi?", "Abulfayzxon", ["Imomqulixon", "Subhonquli", "Abdullaxon"], "Abulfayz.", b="siyosiy"),
    C(2, "Nodirshoh 1740-yilda Xiva xoni kimni mag'lub etdi?", "Elbarsxon", ["Olloquli", "Eltuzar", "Muhammad Rahim"], "Elbars.", b="siyosiy"),
    C(2, "Nodirshoh qachon o'ldirilgan?", "1747", ["1740", "1598", "1500"], "1747.", b="siyosiy"),
    C(2, "Nodirshoh yurishidan keyin Buxoroda kim kuchaydi?", "Mang'it beklari", ["Minglar", "Ashtarxoniylar", "Safaviylar"], "Mang'it.", b="siyosiy"),
    C(3, "Nodirshoh bilan Buxoro o'rtasidagi chegara qaysi daryo?", "Amudaryo", ["Sirdaryo", "Zarafshon", "Volga"], "Amudaryo.", b="siyosiy"),
    O(3, "Nodirshohning Buxoro va Xivaga yurishi yilini yozing.", ["1740", "1740-yil"], "1740.", b="siyosiy"),
]

Q["9.1.10-11"] = [
    C(1, "Xususiy yer egaligi shakli qanday atalgan?", "Mulk", ["Vaqf", "Suyurg'ol", "Amlok"], "Mulk.", b="ijtimoiy"),
    C(1, "Diniy muassasalarga tegishli yer?", "Vaqf", ["Mulk", "Suyurg'ol", "Xiroj"], "Vaqf.", b="ijtimoiy"),
    C(1, "Xon in'omi sifatida berilgan shartli yer egaligi?", "Suyurg'ol", ["Vaqf", "Mulk", "Hashar"], "Suyurg'ol.", b="ijtimoiy"),
    C(2, "Bog'-rog', poliz yerlaridan pul shaklida olingan soliq?", "Tanob puli", ["Xiroj", "Zakot", "Begor"], "Tanob.", b="ijtimoiy"),
    C(2, "Chorva va tijorat molidan olingan mulk solig'i?", "Zakot", ["Xiroj", "Tanob", "Hashar"], "Zakot.", b="ijtimoiy"),
    C(2, "Davlat ishlariga bepul majburiy jalb etish?", "Begor", ["Hashar", "Zakot", "Tanob"], "Begor.", b="ijtimoiy"),
    C(3, "Xirojning miqdori hosilning qancha qismi?", "1/3 yoki 1/5 gacha", ["1/100", "1/2 va undan ko'p", "1/50"], "Xiroj.", b="ijtimoiy"),
    O(2, "Mahalliy inshootlar qurishda xalqning ixtiyoriy-majburiy yordami nima deb ataladi? (H...)", ["Hashar", "hashar"], "Hashar.", b="ijtimoiy"),
    O(3, "Xon tomonidan harbiy xizmat evaziga beriladigan shartli yer egaligi nomini yozing (S...).", ["Suyurg'ol", "suyurgol", "Suyurgol"], "Suyurg'ol.", b="ijtimoiy"),
]

Q["9.1.12"] = [
    C(1, "Mang'itlar sulolasi Buxoroda qaysi yildan hukmronlik qilgan?", "1753-yildan", ["1500", "1599", "1920"], "Mang'itlar.", b="siyosiy"),
    C(1, "Buxoro amirligining rasmiy e'lon qilinishi?", "1785-yil (Shohmurod)", ["1599", "1920", "1500"], "Amirlik.", b="siyosiy"),
    C(1, "Mang'itlar sulolasining asoschisi?", "Muhammad Rahimbiy", ["Haydar", "Nasrullo", "Shohmurod"], "Rahimbiy.", b="siyosiy"),
    C(2, "Muhammad Rahimbiy qaysi yilda xon deb e'lon qilingan?", "1756", ["1740", "1500", "1785"], "1756.", b="siyosiy"),
    C(2, "Doniyolbiy qaysi lavozimda bo'lgan?", "Otaliq", ["Qushbegi", "Parvonachi", "Dodxoh"], "Otaliq.", b="siyosiy"),
    C(2, "Mang'itlar sulolasi qachon tugatildi?", "1920", ["1785", "1868", "1924"], "1920.", b="siyosiy"),
    C(3, "Mang'itlar davrida otaliqlar nufuzi qanday?", "Xon darajasiga yetgan", ["Kamaygan", "Yo'qolgan", "Rus ta'siriga tushgan"], "Otaliqlar.", b="siyosiy"),
    O(3, "Mang'itlar sulolasi asoschisining ismini yozing (Muhammad ...).", ["Muhammad Rahimbiy", "Rahimbiy", "Muhammad Rahim"], "Muhammad Rahimbiy.", b="siyosiy"),
]

Q["9.1.13"] = [
    C(1, "Amir Shohmurod qaysi yillarda hukmdor bo'lgan?", "1785–1800", ["1800–1826", "1827–1860", "1860–1885"], "Shohmurod.", b="siyosiy"),
    C(1, "Shohmurod qanday laqab bilan mashhur?", "Ma'sum", ["Qassob", "Mutavalli", "Adolatli"], "Ma'sum.", b="siyosiy"),
    C(1, "Shohmurod davridan Buxoroda hukmdor qanday unvon oldi?", "Amir", ["Podsho", "Sulton", "Xoqon"], "Amir.", b="siyosiy"),
    C(2, "Shohmurod islohotlaridan biri?", "Pul islohoti va soliq tartibga solish", ["Dengiz floti", "Temir yo'l", "Matbaa"], "Islohot.", b="siyosiy"),
    C(2, "Shohmurod davrida diniy muassasalar bilan munosabat?", "Ruhoniylarga tayanildi", ["Ular tugatildi", "Ular chiqarib yuborildi", "Qamoqqa olindi"], "Din.", b="siyosiy"),
    C(2, "Shohmurod davlatning qaysi nomini mustahkamladi?", "Buxoro amirligi", ["Buxoro xonligi", "Buxoro imperiyasi", "Buxoro sultonligi"], "Amirlik.", b="siyosiy"),
    C(3, "Shohmurod vafotidan keyin taxtga kim o'tirdi?", "Haydar", ["Nasrullo", "Muzaffar", "Doniyol"], "Haydar.", b="siyosiy"),
    O(3, "Amir Shohmurod qanday laqab bilan mashhur? (M...)", ["Ma'sum", "masum", "Amiri Ma'sum"], "Ma'sum.", b="siyosiy"),
]

Q["9.1.14"] = [
    C(1, "Amir Haydar qaysi yillarda hukmdor?", "1800–1826", ["1785–1800", "1827–1860", "1860–1885"], "Haydar.", b="siyosiy"),
    C(1, "Amir Nasrullo qaysi yillarda hukmdor?", "1827–1860", ["1800–1826", "1785–1800", "1860–1885"], "Nasrullo.", b="siyosiy"),
    C(1, "Amir Nasrullo qanday laqab bilan atalgan?", "Qassob amir", ["Ma'sum", "Adolatli", "Buyuk"], "Qassob.", b="siyosiy"),
    C(2, "Buxoroda 1842-yilda qatl etilgan ingliz zobitlari?", "Stoddart va Konolli", ["Beneveni va Jenkinson", "Bekovich-Cherkasskiy", "Chernyayev"], "Ingliz josuslari.", b="siyosiy"),
    C(2, "Amir Nasrullo Qo'qon xonligini qaysi yili bosib oldi?", "1842", ["1800", "1860", "1868"], "1842.", b="siyosiy"),
    C(2, "Nasrullodan keyin Buxoroda kim amir bo'ldi?", "Muzaffar", ["Haydar", "Shohmurod", "Olim"], "Muzaffar.", b="siyosiy"),
    C(3, "Amir Muzaffar qaysi yillarda hukmronlik qilgan?", "1860–1885", ["1827–1860", "1800–1826", "1885–1910"], "Muzaffar.", b="siyosiy"),
    O(3, "1842-yilda Buxoroda qatl etilgan ingliz zobitlaridan biri: Stoddart yoki ... (ikkinchisini yozing).", ["Konolli", "Connolly", "Konnoli"], "Konolli.", b="siyosiy"),
]

Q["9.1.15"] = [
    C(1, "Xiva xonligini kim boshqargan sulolasi XVI asrda?", "Arabshohiylar", ["Mang'itlar", "Minglar", "Qo'ng'irotlar"], "Arabshohiylar.", b="siyosiy"),
    C(1, "Xiva xonligining asoschisi?", "Ilbars", ["Abulg'ozi", "Anusha", "Eltuzar"], "Ilbars.", b="siyosiy"),
    C(1, "Xiva xonligi mustaqil davlat sifatida qaysi yildan?", "1511 (taxm.)", ["1428", "1740", "1920"], "XVI asr.", b="siyosiy"),
    C(2, "Xorazm xoni, tarixchi — «Shajarayi turk» muallifi?", "Abulg'ozi Bahodirxon", ["Elbarsxon", "Anushaxon", "Eltuzar"], "Abulg'ozi.", b="madaniyat"),
    C(2, "Abulg'ozi asarlari?", "«Shajarayi turk» va «Shajarayi tarokima»", ["«Boburnoma»", "«Zafarnoma»", "«Tarixi Rashidiy»"], "Abulg'ozi.", b="madaniyat"),
    C(2, "Xiva xonligining poytaxti 1598-yildan?", "Xiva", ["Urganch", "Qo'qon", "Buxoro"], "Xiva.", b="siyosiy"),
    C(3, "Arabshohiylar sulolasi qachongacha hukmronlik qilgan?", "1695", ["1740", "1920", "1598"], "1695.", b="siyosiy"),
    O(3, "Arabshohiylar sulolasidan Xiva xonligining asoschisi bo'lgan hukmdor ismini yozing (I... yoki E...).", ["Ilbars", "Elbars", "Elbarsxon", "Ilbarsxon"], "Ilbars.", b="siyosiy"),
]

Q["9.1.16"] = [
    C(1, "Xivada Qo'ng'irotlar sulolasi dastlab qanday unvon bilan boshqargan?", "Inoq", ["Xon", "Amir", "Qushbegi"], "Inoq.", b="siyosiy"),
    C(1, "Qo'ng'irotlardan birinchi xon?", "Eltuzarxon", ["Muhammad Aminxon", "Olloqulixon", "Rahimxon"], "Eltuzar.", b="siyosiy"),
    C(1, "Eltuzarxon qaysi yili xon bo'ldi?", "1804", ["1740", "1500", "1920"], "1804.", b="siyosiy"),
    C(2, "Muhammad Rahimxon I qaysi yillarda?", "1806–1825", ["1804–1806", "1825–1842", "1845–1855"], "Rahimxon I.", b="siyosiy"),
    C(2, "Muhammad Rahimxon I islohotlari?", "Soliq va pul islohoti", ["Temir yo'l", "Dengiz floti", "Parlament"], "Islohot.", b="siyosiy"),
    C(2, "Inoq nima?", "Xonning eng ishonchli maslahatchisi", ["Soliqchi", "Qozi", "Elchi"], "Inoq.", b="siyosiy"),
    C(3, "Qo'ng'irotlar sulolasi qachon tugatilgan?", "1920", ["1804", "1873", "1924"], "1920.", b="siyosiy"),
    O(3, "Xiva xonligining birinchi qo'ng'irot xoni ismini yozing (E...).", ["Eltuzarxon", "Eltuzar", "Iltuzar", "Iltuzarxon"], "Eltuzarxon.", b="siyosiy"),
]

Q["9.1.17"] = [
    C(1, "Olloqulixon qaysi yillarda hukmdor bo'lgan?", "1825–1842", ["1806–1825", "1845–1855", "1804–1806"], "Olloquli.", b="siyosiy"),
    C(1, "Muhammad Aminxon qaysi yillarda?", "1845–1855", ["1825–1842", "1806–1825", "1855–1864"], "Muhammad Amin.", b="siyosiy"),
    C(1, "Xivadagi qadimiy ichki qal'a?", "Ichan Qal'a", ["Ark", "Registon", "Sherdor"], "Ichan Qal'a.", b="madaniyat"),
    C(2, "Xivadagi tugallanmagan mashhur minora?", "Kalta Minor", ["Kalon", "Islom Xo'ja", "Ulug'bek"], "Kalta.", b="madaniyat"),
    C(2, "Kalta Minor kim davrida qurila boshlagan?", "Muhammad Aminxon", ["Olloqulixon", "Eltuzar", "Rahim"], "1851.", b="madaniyat"),
    C(2, "Olloqulixon qurdirgan saroyi?", "Tosh Hovli", ["Ko'k saroy", "Oq saroy", "Ark"], "Tosh Hovli.", b="madaniyat"),
    C(3, "Ichan Qal'a qaysi yili YUNESKO Jahon merosiga kiritilgan?", "1990", ["1966", "2000", "1992"], "1990.", b="madaniyat"),
    O(3, "Xiva Ichan Qal'asidagi X asrga oid, yog'och ustunli masjid nomini yozing (J...).", ["Juma masjidi", "Juma", "Juma masjid"], "Juma masjidi.", b="madaniyat"),
]

Q["9.1.18"] = [
    C(1, "Qo'qon xonligi qaysi yilda tashkil topgan?", "1709", ["1500", "1599", "1785"], "1709.", b="siyosiy"),
    C(1, "Qo'qon xonligining asoschisi?", "Shohruhbiy", ["Olimxon", "Umarxon", "Norbo'tabiy"], "Shohruhbiy.", b="siyosiy"),
    C(1, "Qo'qon hukmdorlari qaysi sulolaga mansub?", "Minglar", ["Mang'itlar", "Qo'ng'irotlar", "Shayboniylar"], "Minglar.", b="siyosiy"),
    C(2, "Norbo'tabiy qaysi yillarda?", "1770–1798", ["1709–1721", "1810–1822", "1822–1842"], "Norbo'ta.", b="siyosiy"),
    C(2, "Qo'qon xonligi qaysi vodiyda?", "Farg'ona", ["Zarafshon", "Surxon", "Xorazm"], "Farg'ona.", b="siyosiy"),
    C(2, "Qo'qon xonligining tugatilishi?", "1876", ["1709", "1842", "1865"], "1876.", b="siyosiy"),
    C(3, "Shohruhbiy qaysi yili Qo'qonda mustaqil hokimiyat o'rnatgan?", "1709", ["1740", "1500", "1865"], "1709.", b="siyosiy"),
    O(3, "Qo'qon xonligiga asos solgan Shohruhbiy qaysi sulola (Ming) vakili? Sulola nomini yozing.", ["Minglar", "Ming", "minglar"], "Minglar.", b="siyosiy"),
]

Q["9.1.19"] = [
    C(1, "Olimxon qaysi yillarda?", "1798–1810", ["1709–1721", "1810–1822", "1822–1842"], "Olimxon.", b="siyosiy"),
    C(1, "Olimxon qanday unvonni qabul qildi?", "Xon", ["Amir", "Sulton", "Shoh"], "Xon.", b="siyosiy"),
    C(1, "Olimxon qaysi yili Toshkentni qo'shib oldi?", "1809", ["1709", "1842", "1865"], "1809.", b="siyosiy"),
    C(2, "Olimxon davlatida muhim islohot?", "Qo'shin va ma'muriy islohot", ["Temir yo'l", "Matbaa", "Konstitutsiya"], "Islohot.", b="siyosiy"),
    C(2, "Olimxon qaysi shaharni egallab, davlatni kengaytirdi?", "Toshkent", ["Samarqand", "Xiva", "Marv"], "Toshkent.", b="siyosiy"),
    C(2, "Olimxon qanday halok bo'ldi?", "Fitna natijasida o'ldirildi (1810)", ["Jangda", "Tabiiy o'lim", "Surgun"], "1810.", b="siyosiy"),
    C(3, "Olimxondan keyin Qo'qon xoni bo'lgan ukasi?", "Umarxon", ["Muhammad Alixon", "Xudoyorxon", "Shohruhbiy"], "Umarxon.", b="siyosiy"),
    O(3, "Olimxon Toshkentni qaysi yili Qo'qonga qo'shgan? (raqam)", ["1809", "1809-yil"], "1809.", b="siyosiy"),
]

Q["9.1.20"] = [
    C(1, "Umarxon qaysi yillarda?", "1810–1822", ["1798–1810", "1822–1842", "1709–1721"], "Umarxon.", b="siyosiy"),
    C(1, "Umarxonning xotini, shoira?", "Nodira", ["Uvaysiy", "Zebuniso", "Dilshod"], "Nodira.", b="madaniyat"),
    C(1, "Nodira qanday taxallus bilan ijod qilgan?", "Komila", ["Uvaysiy", "Maknuna", "Dilshod"], "Komila.", b="madaniyat"),
    C(2, "Umarxon qanday unvon oldi?", "Amir ul-muslimin", ["Shahanshoh", "Sohibqiron", "Sulton"], "Amir.", b="siyosiy"),
    C(2, "Muhammad Alixon (Madalixon) qaysi yillarda?", "1822–1842", ["1810–1822", "1798–1810", "1845–1855"], "Madalixon.", b="siyosiy"),
    C(2, "Nodira qaysi yili qatl etilgan?", "1842", ["1810", "1865", "1876"], "1842.", b="siyosiy"),
    C(3, "Nodirani qatl ettirgan amir?", "Amir Nasrullo", ["Amir Haydar", "Muzaffar", "Shohmurod"], "Nasrullo.", b="siyosiy"),
    O(3, "Umarxonning xotini va shoira Nodiraning taxallusini yozing (K...).", ["Komila", "komila"], "Komila.", b="madaniyat"),
]

Q["9.1.21"] = [
    C(1, "Buxoro va Qo'qonda Bosh vazir lavozimi qanday?", "Qushbegi", ["Parvonachi", "Dodxoh", "Inoq"], "Qushbegi.", b="ijtimoiy"),
    C(1, "Xivada Qushbegi o'rniga qaysi lavozim?", "Devonbegi", ["Otaliq", "Inoq", "Shixovul"], "Devonbegi.", b="ijtimoiy"),
    C(1, "Valiahdlarga tarbiyachi?", "Otaliq", ["Qushbegi", "Parvonachi", "Dodxoh"], "Otaliq.", b="ijtimoiy"),
    C(2, "Xonning farmon va yorliqlarini rasmiylashtiruvchi amaldor?", "Parvonachi", ["Dodxoh", "Inoq", "Shixovul"], "Parvonachi.", b="ijtimoiy"),
    C(2, "Fuqarolar arizalarini xonga yetkazuvchi?", "Dodxoh", ["Parvonachi", "Inoq", "Otaliq"], "Dodxoh.", b="ijtimoiy"),
    C(2, "Xonning eng ishonchli maslahatchisi (Xiva)?", "Inoq", ["Shixovul", "Dodxoh", "Qushbegi"], "Inoq.", b="ijtimoiy"),
    M(2, [("Qushbegi", "Bosh vazir"), ("Otaliq", "Valiahd tarbiyachisi"), ("Dodxoh", "Arizalarni xonga yetkazuvchi")], "Lavozimlar."),
    O(2, "Xiva xonligida tashqi ishlar va elchilikka mas'ul lavozim nomini yozing (Sh...).", ["Shixovul", "shixovul"], "Shixovul.", b="ijtimoiy"),
    C(3, "Buxoro amirligida Qushbegi vazifasi?", "Ichki siyosat, soliq va ma'muriy ishlarni boshqarish", ["Faqat sud", "Faqat harbiy", "Faqat din"], "Qushbegi.", b="ijtimoiy"),
    O(3, "Voyaga yetmagan valiahdlarga siyosiy murabbiy lavozim nomi? (O...)", ["Otaliq", "otaliq"], "Otaliq.", b="ijtimoiy"),
]

Q["9.1.22"] = [
    C(1, "XVI asrda Buxoroga kelgan ingliz sayyohi?", "Anton Jenkinson", ["Marko Polo", "Klavixo", "Bekovich"], "1558.", b="siyosiy"),
    C(1, "Pyotr I buyrug'i bilan Xivaga yurishga yuborilgan?", "Bekovich-Cherkasskiy", ["Chernyayev", "Skobelev", "Kaufman"], "1717.", b="siyosiy"),
    C(1, "Bekovich-Cherkasskiy yurishi qaysi yilda?", "1717", ["1865", "1873", "1558"], "1717.", b="siyosiy"),
    C(2, "Rossiya elchisi Florio Beneveni qaysi xonlikka yuborilgan?", "Buxoro", ["Xiva", "Qo'qon", "Bobur"], "1718–1725.", b="siyosiy"),
    C(2, "Bekovich-Cherkasskiy yurishi qanday tugadi?", "Rus qo'shini tor-mor etildi", ["G'alaba qozondi", "Xiva olindi", "Sulh tuzildi"], "Mag'lubiyat.", b="siyosiy"),
    C(2, "Rossiya xonliklar bilan asosan nimani izlagan?", "Savdo yo'llari va xomashyo", ["Faqat din", "Faqat madaniyat", "Faqat turizm"], "Iqtisodiy manfaat.", b="siyosiy"),
    C(3, "Jenkinson Buxoroga qaysi yili kelgan?", "1558", ["1717", "1865", "1500"], "1558.", b="siyosiy"),
    O(3, "Pyotr I topshirig'i bilan Xivaga yurish qilgan rus zobiti familiyasi: Bekovich-... yozing.", ["Cherkasskiy", "Bekovich-Cherkasskiy", "Cherkaskiy"], "Cherkasskiy.", b="siyosiy"),
]


# ---- Chizmali savollar (SVG) ----
from . import figs  # noqa: E402

Q["9.1.7"] += [
    C(1, "Rasmda Samarqand Registon ansamblining sxemasi ko'rsatilgan. G'arbiy tomondagi «A» binosi qaysi madrasa?", "Ulug'bek madrasasi", ["Sherdor madrasasi", "Tillaqori madrasasi", "Abdullaxon madrasasi"], "G'arbda — Ulug'bek, sharqda — Sherdor, shimolda — Tillaqori.", b="madaniyat", fig=figs.registon()),
    C(2, "Rasmda Registon ansamblining sxemasi ko'rsatilgan. Shimol tomondagi «B» binosi qaysi madrasa?", "Tillaqori madrasasi", ["Ulug'bek madrasasi", "Sherdor madrasasi", "Mir Arab madrasasi"], "Tillaqori (1646–1660) maydonning shimolida.", b="madaniyat", fig=figs.registon()),
    C(2, "Rasmda Registon ansamblining sxemasi ko'rsatilgan. Sharq tomondagi «C» binosi peshtoqida quyosh va sher tasviri bor. Bu qaysi madrasa?", "Sherdor madrasasi", ["Ulug'bek madrasasi", "Tillaqori madrasasi", "Kukaldosh madrasasi"], "Sherdor (1619–1636).", b="madaniyat", fig=figs.registon()),
]
