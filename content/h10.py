"""10-sinf: XIX asr ikkinchi yarmi – XX asr boshlari — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["10.1.1"] = [
    C(1, "XIX asr o'rtalarida O'rta Osiyo xonliklari holati qanday edi?", "Siyosiy tarqoqlik va o'zaro urushlar", ["Kuchli birlashgan davlat", "Rus ittifoqi", "Hindiston bilan ittifoq"], "Zaiflashuv.", b="siyosiy"),
    C(1, "Rossiya O'rta Osiyoni nima uchun egallashga intildi?", "Paxta xomashyosi va bozorlar uchun", ["Din tarqatish uchun", "Dengiz yo'llari uchun", "Tog' qazilmalari uchun faqat"], "Iqtisodiy manfaat.", b="siyosiy"),
    C(1, "Qrim urushidagi mag'lubiyatdan keyin Rossiya nimani kuchaytirdi?", "Markaziy Osiyoga yurishlarni", ["Yevropaga yurishlarni", "Afrikaga yurishlarni", "Amerikaga yurishlarni"], "1853–56.", b="siyosiy"),
    C(2, "Rossiya Sirdaryo chizig'ini qurishni qaysi qal'a egallashdan boshlagan?", "Oq masjid (1853)", ["Toshkent", "Samarqand", "Xiva"], "Ak-Mechet.", b="siyosiy"),
    C(2, "Rossiya mustamlakachilari bilan raqobatlashgan davlat?", "Angliya", ["Fransiya", "Xitoy", "Yaponiya"], "Buyuk o'yin.", b="siyosiy"),
    C(2, "«Buyuk o'yin» deb qaysi ikki davlat raqobati ataladi?", "Rossiya va Angliya", ["Rossiya va Fransiya", "Angliya va Xitoy", "Xitoy va Yaponiya"], "Buyuk o'yin.", b="siyosiy"),
    C(3, "Qrim urushi qaysi yillarda?", "1853–1856", ["1812", "1877", "1914"], "Qrim urushi.", b="siyosiy"),
    O(3, "Rossiya qaysi imperiya (Angliya) bilan Markaziy Osiyo ustidan raqobat qilgan? Davlat nomini yozing.", ["Angliya", "Buyuk Britaniya", "Britaniya"], "Angliya.", b="siyosiy"),
]

Q["10.1.2-3"] = [
    C(1, "Toshkent qachon bosib olingan?", "1865-yil iyun", ["1853", "1868", "1873"], "1865.", b="siyosiy"),
    C(1, "Toshkentni bosib olgan rus generali?", "M.G. Chernyayev", ["Kaufman", "Skobelev", "Perovskiy"], "Chernyayev.", b="siyosiy"),
    C(1, "Toshkent himoyasida halok bo'lgan Qo'qon sarkardasi?", "Mullo Alimqul", ["Xudoyorxon", "Po'latxon", "Madaminbek"], "Alimqul.", b="siyosiy"),
    C(2, "Mullo Alimqul qachon halok bo'ldi?", "1865-yil may", ["1864", "1868", "1876"], "1865.", b="siyosiy"),
    C(2, "Chernyayev 1864-yilda egallagan shaharlar?", "Avliyo ota, Turkiston, Chimkent", ["Samarqand, Buxoro", "Xiva, Urganch", "Qo'qon, Andijon"], "1864.", b="siyosiy"),
    C(2, "Turkiston viloyati qaysi yili tuzilgan?", "1867", ["1865", "1873", "1876"], "1867.", b="siyosiy"),
    C(3, "Chernyayev «Toshkent fotihi» nomini olgach...", "Peterburg uni chaqirib oldi", ["Shahar hokimi bo'ldi", "Sibirga ketdi", "Amirga qo'shildi"], "Chernyayev.", b="siyosiy"),
    O(3, "Toshkent rus qo'shini tomonidan qaysi yilda bosib olingan? (raqam)", ["1865", "1865-yil"], "1865.", b="siyosiy"),
    O(3, "Toshkentni 1865-yilda egallagan rus generalining familiyasini yozing (C...).", ["Chernyayev", "Chernyaev", "Chernayev"], "Chernyayev.", b="siyosiy"),
]

Q["10.1.4"] = [
    C(1, "Ziyovuddin shartnomasi qaysi yilda tuzilgan?", "1868-yil 23-iyun", ["1873-yil 12-avgust", "1865-yil", "1876-yil"], "1868.", b="siyosiy"),
    C(1, "Zirabuloq jangi qaysi yilda?", "1868", ["1865", "1873", "1876"], "Zirabuloq.", b="siyosiy"),
    C(1, "Ziyovuddin shartnomasi qaysi davlat bilan tuzilgan?", "Buxoro amirligi", ["Xiva xonligi", "Qo'qon xonligi", "Eron"], "Buxoro.", b="siyosiy"),
    C(2, "Buxoro amirligi Rossiyaga qancha tovon to'ladi?", "500 ming rubl", ["2,2 million rubl", "100 ming rubl", "10 million rubl"], "500 ming.", b="siyosiy"),
    C(2, "Samarqand va Kattaqo'rg'on okrugi qaysi tarkibga o'tdi?", "Rossiya imperiyasi", ["Xiva xonligi", "Qo'qon xonligi", "Eron"], "Zarafshon okrugi.", b="siyosiy"),
    C(2, "Ziyovuddin shartnomasidan keyin Buxoro?", "Protektoratga aylandi", ["Mustaqil bo'ldi", "Tugatildi", "Xivaga qo'shildi"], "Protektorat.", b="siyosiy"),
    C(3, "Zirabuloq jangida Kaufman kim qo'shinini mag'lub etdi?", "Amir Muzaffar", ["Amir Nasrullo", "Xudoyorxon", "Olimxon"], "Muzaffar.", b="siyosiy"),
    O(3, "Ziyovuddin shartnomasi qaysi yilda tuzilgan? (raqam)", ["1868", "1868-yil"], "1868.", b="siyosiy"),
    O(3, "Ziyovuddin shartnomasi bo'yicha Buxoro amirligi qancha (ming rubl) harbiy tovon to'lagan? (raqam)", ["500", "500 ming"], "500 ming rubl.", b="siyosiy"),
]

Q["10.1.5"] = [
    C(1, "Gandimiyon shartnomasi qaysi yilda?", "1873-yil 12-avgust", ["1868-yil 23-iyun", "1865-yil", "1876-yil"], "1873.", b="siyosiy"),
    C(1, "Gandimiyon shartnomasi qaysi davlat bilan?", "Xiva xonligi", ["Buxoro amirligi", "Qo'qon xonligi", "Eron"], "Xiva.", b="siyosiy"),
    C(1, "Xiva xonligining tovon summasi?", "2,2 million rubl", ["500 ming rubl", "100 ming rubl", "10 million rubl"], "2,2 mln.", b="siyosiy"),
    C(2, "Xiva xoni Rossiyaning kimi bo'ldi?", "Vassali", ["Ittifoqdoshi", "Raqibi", "Do'sti"], "Vassal.", b="siyosiy"),
    C(2, "Xiva xonligi Amudaryoning qaysi qirg'oqlaridan voz kechdi?", "O'ng qirg'oq", ["Chap qirg'oq", "Ikkalasi", "Hech qaysi"], "O'ng qirg'oq.", b="siyosiy"),
    C(2, "Xiva xonligining 1873-yildagi xoni?", "Muhammad Rahimxon II (Feruz)", ["Olloqulixon", "Muhammad Aminxon", "Eltuzar"], "Feruz.", b="siyosiy"),
    C(3, "Tovon necha yilga bo'lib to'lanadigan?", "20 yil", ["5 yil", "100 yil", "1 yil"], "20 yil.", b="siyosiy"),
    O(3, "Xiva xonligi bilan tuzilgan shartnoma nomi: G... (Gandimiyon).", ["Gandimiyon", "gandimiyon"], "Gandimiyon.", b="siyosiy"),
]

Q["10.1.6"] = [
    C(1, "Qo'qon xonligi qaysi yilda tugatilgan?", "1876", ["1865", "1868", "1873"], "1876.", b="siyosiy"),
    C(1, "Qo'qon xonligidagi qo'zg'olon rahbari?", "Po'latxon", ["Madaminbek", "Do'kchi eshon", "Mullo Alimqul"], "Po'latxon.", b="siyosiy"),
    C(1, "Qo'qon xonligi o'rnida qaysi viloyat tuzildi?", "Farg'ona viloyati", ["Zarafshon okrugi", "Sirdaryo viloyati", "Yettisuv viloyati"], "Farg'ona.", b="siyosiy"),
    C(2, "Qo'qon xonligi oxirgi xoni?", "Xudoyorxon (Nosiriddin)", ["Olimxon", "Umarxon", "Po'latxon"], "Xudoyor.", b="siyosiy"),
    C(2, "Qo'qon xonligini bosib olishga rahbarlik qilgan rus generali?", "M.D. Skobelev", ["Kaufman", "Chernyayev", "Perovskiy"], "Skobelev.", b="siyosiy"),
    C(2, "Po'latxon qo'zg'oloni qaysi yillarda?", "1875–1876", ["1865", "1892", "1898"], "1875–76.", b="siyosiy"),
    C(3, "Skobelev Qo'qonda qanday lavozim oldi?", "Farg'ona viloyati harbiy gubernatori", ["Bosh vazir", "Xon", "Elchi"], "Skobelev.", b="siyosiy"),
    O(3, "Qo'qon xonligining 1875–76-yillardagi qo'zg'olon rahbari ismini yozing (P...).", ["Po'latxon", "Pulatxon", "Polatxon"], "Po'latxon.", b="siyosiy"),
]

Q["10.1.7"] = [
    C(1, "Turkiston general-gubernatorligi qachon tuzilgan?", "1867", ["1865", "1873", "1886"], "1867.", b="siyosiy"),
    C(1, "Turkiston general-gubernatorligining markazi?", "Toshkent", ["Samarqand", "Qo'qon", "Buxoro"], "Toshkent.", b="siyosiy"),
    C(1, "Birinchi general-gubernator?", "K.P. fon Kaufman", ["Chernyayev", "Skobelev", "Perovskiy"], "Kaufman.", b="siyosiy"),
    C(2, "«Turkiston o'lkasini boshqarish to'g'risida»gi Nizom qaysi yil?", "1886", ["1867", "1873", "1898"], "1886.", b="siyosiy"),
    C(2, "General-gubernator qaysi vazirlikka bo'ysungan?", "Harbiy vazirlikka", ["Moliya", "Din", "Maorif"], "Harbiy.", b="siyosiy"),
    C(2, "Turkiston general-gubernatorligiga qaysi viloyatlar kirgan?", "Sirdaryo, Farg'ona, Samarqand", ["Xiva, Buxoro", "Moskva, Peterburg", "Kavkaz"], "Viloyatlar.", b="siyosiy"),
    C(3, "Turkiston general-gubernatorligi qaysi voqea natijasida tugatildi?", "Fevral inqilobi (1917)", ["Qrim urushi", "Rus-yapon urushi", "Birinchi rus inqilobi (1905)"], "1917-yilda tugagan.", b="siyosiy"),
    O(3, "Turkiston general-gubernatorligining birinchi general-gubernatori familiyasini yozing (K...).", ["Kaufman", "fon Kaufman", "Kauffman"], "Kaufman.", b="siyosiy"),
]

Q["10.1.8"] = [
    C(1, "Mustamlaka ma'muriyatining boshlig'i?", "General-gubernator", ["Xon", "Amir", "Qozi"], "Gubernator.", b="ijtimoiy"),
    C(1, "Viloyat harbiy gubernatorlariga tobe bo'lgan bo'linma?", "Uyezd (tuman)", ["Satrapiya", "Ulus", "Nom"], "Uyezd.", b="ijtimoiy"),
    C(1, "Mahalliy aholi qaysi qonunlar bo'yicha sud qilingan?", "Qozi va biylar sudlari (shariat va odat)", ["Faqat rus qonunlari", "Rim huquqi", "Fransuz kodeksi"], "Qozi sudi.", b="ijtimoiy"),
    C(2, "Mahalliy boshqaruvda qishloq oqsoqoli?", "Saylanuvchi amaldor", ["Rus ofitseri", "Xon vakili", "Amir"], "Oqsoqol.", b="ijtimoiy"),
    C(2, "Mustamlaka ma'muriyatining asosiy maqsadi?", "Aholini nazorat qilish va soliq yig'ish", ["Maorifni rivojlantirish", "Savdoni cheklash", "Din tarqatish"], "Nazorat.", b="ijtimoiy"),
    C(2, "Volost boshqaruvchisi kim tomonidan saylangan?", "Aholi vakillari", ["Gubernator", "Xon", "Amir"], "Saylov.", b="ijtimoiy"),
    O(2, "Turkiston general-gubernatorligini boshqargan oliy mansabdor shaxs qanday unvonda atalgan? (ikki so'z)", ["general-gubernator", "General-gubernator", "general gubernator"], "General-gubernator.", b="ijtimoiy"),
    C(3, "1886-yil Nizomida mahalliy aholining huquqlari qanday edi?", "Cheklangan, imtiyozlar rus aholisiga berilgan", ["Teng huquq", "Kengaytirilgan", "Mustaqil"], "Nizom.", b="ijtimoiy"),
]

Q["10.1.9"] = [
    C(1, "Ko'chirish siyosati nima?", "Rossiyadan dehqonlarni Turkistonga ko'chirish", ["Mahalliy aholini Rossiyaga ko'chirish", "Ziyolilarni chiqarish", "Qullarni ozod qilish"], "Ko'chirish.", b="ijtimoiy"),
    C(1, "Ko'chirish siyosatining maqsadi?", "Mustamlakani mustahkamlash", ["Yer berish", "Savdo", "Maorif"], "Mustahkamlash.", b="ijtimoiy"),
    C(1, "Ko'chirilgan rus dehqonlari qanday yerlarni olgan?", "Eng yaxshi unumdor yerlarni", ["Cho'l yerlarni", "Tog' yerlarni", "Bog' yerlarni"], "Eng yaxshisi.", b="ijtimoiy"),
    C(2, "Stolipin islohoti qaysi yildan?", "1906", ["1865", "1886", "1917"], "1906.", b="ijtimoiy"),
    C(2, "Qozi sudi qaysi masalalarda faoliyat yuritgan?", "Oilaviy va mulkiy kelishmovchiliklar", ["Siyosiy ishlar", "Jinoyat ishlari", "Harbiy ishlar"], "Qozi.", b="ijtimoiy"),
    C(2, "Mustamlaka sud tizimida jiddiy siyosiy ishlar kimning vakolatida edi?", "Rus sudlari", ["Qozilar", "Biylar", "Oqsoqollar"], "Rus sudi.", b="ijtimoiy"),
    C(3, "Ko'chirish natijasida mahalliy aholining ahvoli?", "Yer tanqisligi kuchaydi", ["Yaxshilandi", "O'zgarmadi", "Boyidi"], "Yer.", b="ijtimoiy"),
    O(2, "Rossiyadan Turkistonga dehqonlarni joylashtirish siyosatining nomini yozing (K... siyosati).", ["Ko'chirish", "ko'chirish", "Kochirish"], "Ko'chirish siyosati.", b="ijtimoiy"),
]

Q["10.1.10"] = [
    C(1, "Turkistonda mustamlaka iqtisodiyotining asosiy yo'nalishi?", "Paxta yakkahokimligi", ["Neft", "Ko'mir", "Ipak"], "Paxta.", b="ijtimoiy"),
    C(1, "Turkistonda paxtaning qaysi navi ekila boshlandi?", "Amerika (Upland) navi", ["Misr navi", "Hind navi", "Xitoy navi"], "Upland.", b="ijtimoiy"),
    C(1, "Paxta nima uchun ekilgan?", "Rus to'qimachilik fabrikalari uchun xomashyo", ["Eksport uchun Xitoyga", "Mahalliy ehtiyoj", "Yoqilg'i"], "Rossiya.", b="ijtimoiy"),
    C(2, "Mustamlaka davrida Turkiston iqtisodiyoti?", "Xomashyo bazasi bo'lib qoldi", ["Sanoat markazi bo'ldi", "Mustaqil bo'ldi", "Rivojlandi"], "Xomashyo.", b="ijtimoiy"),
    C(2, "Paxta ekin maydonlarining kengayishi nimaga olib keldi?", "G'alla ekinlari kamayib, oziq-ovqat tanqisligi paydo bo'ldi", ["Narxlar tushdi", "Farovonlik", "Aholi kamaydi"], "Yakkahokimlik.", b="ijtimoiy"),
    C(2, "Paxta tozalash zavodlari qachondan ko'paydi?", "XIX asr oxiri – XX asr boshi", ["XV asr", "XVIII asr", "XXI asr"], "Zavodlar.", b="ijtimoiy"),
    O(2, "Turkistonda mustamlakachilik davrida asosiy xomashyo ekini nomini yozing.", ["paxta", "Paxta"], "Paxta.", b="ijtimoiy"),
    C(3, "Paxta yakkahokimligining oqibati?", "Mahalliy aholining qaramligi kuchaydi", ["Boylik", "Tenglik", "Ozodlik"], "Qaramlik.", b="ijtimoiy"),
]

Q["10.1.11"] = [
    C(1, "Zakaspiy temir yo'li qaysi dengiz bo'yidan boshlangan?", "Kaspiy (Krasnovodsk)", ["Orol", "Qora", "Baltik"], "Krasnovodsk.", b="ijtimoiy"),
    C(1, "Zakaspiy temir yo'li Samarqandga qaysi yili yetib keldi?", "1888", ["1865", "1899", "1906"], "1888.", b="ijtimoiy"),
    C(1, "Toshkentga temir yo'l qaysi yili yetib keldi?", "1899", ["1888", "1906", "1914"], "1899.", b="ijtimoiy"),
    C(2, "Orenburg–Toshkent temir yo'li qaysi yili ishga tushgan?", "1906", ["1888", "1899", "1917"], "1906.", b="ijtimoiy"),
    C(2, "Temir yo'l qurilishining maqsadi?", "Paxtani Rossiyaga tashish va harbiy maqsad", ["Faqat sayohat", "Faqat ta'lim", "Faqat din"], "Maqsad.", b="ijtimoiy"),
    C(2, "Temir yo'l qurilishi mahalliy aholiga qanday ta'sir qildi?", "Savdoni kengaytirdi, lekin qaramlikni kuchaytirdi", ["Faqat foyda", "Hech ta'sir", "Faqat zarar"], "Ikki ta'sir.", b="ijtimoiy"),
    O(2, "Zakaspiy temir yo'li Samarqandga yetgan yilni yozing. (raqam)", ["1888", "1888-yil"], "1888.", b="ijtimoiy"),
    C(3, "Zakaspiy temir yo'li qurilishiga boshchilik qilgan rus generali kim?", "M.N. Annenkov", ["K.P. Kaufman", "M.G. Chernyayev", "V.A. Perovskiy"], "Qurilish rahbari M.N. Annenkov.", b="ijtimoiy"),
]

Q["10.1.12-13"] = [
    C(1, "Toshkentdagi vabo isyoni qaysi yilda?", "1892", ["1865", "1898", "1916"], "1892.", b="siyosiy"),
    C(1, "Andijon qo'zg'oloni rahbari (Do'kchi eshon) qaysi yil?", "1898", ["1892", "1916", "1865"], "1898.", b="siyosiy"),
    C(1, "Do'kchi eshonning asl ismi?", "Muhammadali Sobirov (Madali eshon)", ["Po'latxon", "Madaminbek", "Shermuhammad"], "Madali.", b="siyosiy"),
    C(2, "Vabo isyoni sababi?", "Shahar sanitar qoidalari (karantin) va zo'ravonlik", ["Soliq oshishi", "Maorif", "Din"], "Vabo.", b="siyosiy"),
    C(2, "Andijon qo'zg'oloni qachon boshlangan?", "1898-yil 17-may", ["1892-yil", "1916-yil", "1865-yil"], "17 may.", b="siyosiy"),
    C(2, "Do'kchi eshon qo'zg'oloni qaysi shiorlarda?", "Mustamlakachilarga qarshi (gazavot)", ["Rus bilan ittifoq", "Amirga qarshi", "Qo'qonni qayta tiklash faqat"], "Gazavot.", b="siyosiy"),
    C(3, "Do'kchi eshon qo'zg'olonidan keyin?", "Jazolandi, qatl etildi", ["Mukofotlandi", "Gubernator bo'ldi", "Ozod qilindi"], "Jazo.", b="siyosiy"),
    O(3, "Andijon qo'zg'olonini boshlagan Do'kchi eshon qaysi yili qo'zg'olon ko'targan? (raqam)", ["1898", "1898-yil"], "1898.", b="siyosiy"),
]

Q["10.1.14"] = [
    C(1, "«Jadid» so'zi nimani bildiradi?", "Yangi", ["Eski", "Katta", "Qadimiy"], "Yangi.", b="siyosiy"),
    C(1, "Jadidchilik harakatining asoschisi (Qrimda)?", "Ismoil Gaspirali", ["Behbudiy", "Munavvarqori", "Fitrat"], "Gaspirali.", b="siyosiy"),
    C(1, "Gaspirali nashr etgan gazeta?", "«Tarjimon»", ["«Turkiston viloyati»", "«Taraqqiy»", "«Oyna»"], "Tarjimon.", b="madaniyat"),
    C(2, "Jadidlar nimani talab qilgan?", "Yangi usul maktablar, ma'rifat, islohot", ["Rus ta'limi", "Shariatni bekor qilish", "Qo'zg'olon"], "Ma'rifat.", b="siyosiy"),
    C(2, "Munavvarqori Toshkentda yangi usul maktabini qaysi yili ochgan?", "1901", ["1865", "1886", "1917"], "1901-yil.", b="siyosiy"),
    C(2, "«Tarjimon» gazetasi qaysi yildan chiqa boshlagan?", "1883", ["1906", "1913", "1917"], "1883.", b="madaniyat"),
    C(3, "Jadidlar harakatining asosiy g'oyasi?", "Milliy uyg'onish va ma'rifat orqali ozodlik", ["Armiya tuzish", "Savdo", "Muxtoriyat"], "Uyg'onish.", b="siyosiy"),
    O(3, "Jadidchilik harakatining asoschisi, «Tarjimon» muharriri ismini yozing (I... G...).", ["Ismoil Gaspirali", "Gaspirali", "Ismoilbek Gaspirali", "Gasprinskiy"], "Gaspirali.", b="siyosiy"),
]

Q["10.1.15"] = [
    C(1, "Mahmudxo'ja Behbudiy qaysi shaharda tug'ilgan?", "Samarqand", ["Toshkent", "Buxoro", "Qo'qon"], "Samarqand.", b="madaniyat"),
    C(1, "«Padarkush» dramasi muallifi?", "Mahmudxo'ja Behbudiy", ["Fitrat", "Cho'lpon", "Qodiriy"], "Behbudiy.", b="madaniyat"),
    C(1, "«Padarkush» qaysi yilda yozilgan?", "1911", ["1906", "1917", "1924"], "1911.", b="madaniyat"),
    C(2, "«Padarkush» qanday asar?", "Birinchi o'zbek dramasi", ["Birinchi roman", "Birinchi she'r", "Birinchi qissa"], "Drama.", b="madaniyat"),
    C(2, "Behbudiy nashr etgan jurnal?", "«Oyna»", ["«Taraqqiy»", "«Xurshid»", "«Sadoi Turkiston»"], "1913–1915.", b="madaniyat"),
    C(2, "Behbudiy nashr etgan gazeta?", "«Samarqand»", ["«Taraqqiy»", "«Xurshid»", "«Sadoi Turkiston»"], "1913.", b="madaniyat"),
    M(2, [("«Taraqqiy» (1906)", "Ismoil Obidov"), ("«Xurshid» (1906)", "Munavvarqori"), ("«Sadoi Turkiston» (1914)", "Ubaydulla Asadullaxo'jayev")], "Matbuot."),
    C(3, "Behbudiy qaysi yilda halok bo'lgan?", "1919", ["1911", "1917", "1924"], "Qarshi.", b="madaniyat"),
    O(3, "«Oyna» jurnali qaysi shaharda chiqqan? (S...)", ["Samarqand", "samarqand"], "Samarqand.", b="madaniyat"),
]

Q["10.1.16"] = [
    C(1, "Munavvarqori Abdurashidxonov qaysi yilda tug'ilgan?", "1878", ["1865", "1892", "1906"], "1878.", b="siyosiy"),
    C(1, "Munavvarqori muharrirlik qilgan gazeta?", "«Xurshid»", ["«Samarqand»", "«Oyna»", "«Taraqqiy»"], "Xurshid.", b="siyosiy"),
    C(1, "Munavvarqori Toshkentda qaysi yili usuli jadid maktabini ochgan?", "1901", ["1886", "1917", "1924"], "1901.", b="siyosiy"),
    C(2, "«Turon» jamiyati nima?", "Jadidlarning ma'rifiy-siyosiy jamiyati", ["Rus partiyasi", "Harbiy tashkilot", "Diniy tashkilot"], "Turon.", b="siyosiy"),
    C(2, "«Turon» teatr truppasi muassisi?", "Abdulla Avloniy (Munavvarqori bilan)", ["Behbudiy", "Fitrat", "Cho'lpon"], "Turon.", b="madaniyat"),
    C(2, "Munavvarqori qaysi yilda qatl etilgan?", "1931", ["1917", "1937", "1938"], "1931.", b="siyosiy"),
    C(3, "Munavvarqori ishtirok etgan siyosiy tashkilot?", "«Sho'roi Islomiya»", ["«Alash»", "Bolsheviklar partiyasi", "Eserlar"], "Sho'ro.", b="siyosiy"),
    O(3, "Munavvarqori 1906-yilda Toshkentda qaysi gazetani nashr etgan? Gazeta nomini yozing.", ["Xurshid", "«Xurshid»", "xurshid"], "«Xurshid» gazetasi.", b="siyosiy"),
]

Q["10.1.17"] = [
    C(1, "«Yosh buxoroliklar» harakati rahbarlaridan biri?", "Fayzulla Xo'jayev", ["Munavvarqori", "Behbudiy", "Cho'lpon"], "Xo'jayev.", b="siyosiy"),
    C(1, "Fitrat qaysi shaharda tug'ilgan?", "Buxoro", ["Toshkent", "Samarqand", "Xiva"], "Buxoro.", b="siyosiy"),
    C(1, "«Yosh xivaliklar» qaysi xonlikda?", "Xiva xonligi", ["Buxoro", "Qo'qon", "Turkiston"], "Xiva.", b="siyosiy"),
    C(2, "«Yosh buxoroliklar» partiyasi qachon tuzilgan?", "1909", ["1865", "1917", "1924"], "1909.", b="siyosiy"),
    C(2, "Fitratning «Munozara» asari qaysi yilda?", "1911", ["1906", "1917", "1924"], "1911.", b="madaniyat"),
    C(2, "«Yosh buxoroliklar»ning maqsadi?", "Amirlikda islohotlar o'tkazish", ["Rus bilan birlashish", "Din o'zgartirish", "Savdo"], "Islohot.", b="siyosiy"),
    C(3, "Fayzulla Xo'jayev qaysi yilda qatl etilgan?", "1938", ["1917", "1924", "1931"], "1938.", b="siyosiy"),
    O(3, "Fayzulla Xo'jayev qaysi yosh harakatning rahbari bo'lgan? (Yosh ... — Buxorolik/Buxoroliklar)", ["Yosh buxoroliklar", "buxoroliklar", "yosh buxoroliklar"], "Yosh buxoroliklar.", b="siyosiy"),
]

Q["10.1.18"] = [
    C(1, "Usuli jadid maktablarida qanday o'qitilgan?", "Tovush usuli bilan, dunyoviy fanlar bilan", ["Faqat yod olish", "Faqat arab", "Faqat rus"], "Yangi usul.", b="madaniyat"),
    C(1, "«Taraqqiy» gazetasi qaysi yilda chiqqan?", "1906", ["1913", "1914", "1917"], "1906.", b="madaniyat"),
    C(1, "«Xurshid» gazetasi muharriri?", "Munavvarqori", ["Behbudiy", "Obidov", "Asadullaxo'jayev"], "Munavvarqori.", b="madaniyat"),
    C(2, "«Taraqqiy» gazetasi muharriri?", "Ismoil Obidov", ["Behbudiy", "Munavvarqori", "Avloniy"], "Obidov.", b="madaniyat"),
    C(2, "«Sadoi Turkiston» gazetasi qaysi yilda?", "1914", ["1906", "1913", "1917"], "1914.", b="madaniyat"),
    C(2, "«Sadoi Turkiston» muharriri?", "Ubaydullaxo'ja Asadullaxo'jayev", ["Behbudiy", "Munavvarqori", "Obidov"], "Asadullaxo'jayev.", b="madaniyat"),
    M(2, [("«Samarqand» (1913)", "M. Behbudiy"), ("«Sadoi Turkiston» (1914)", "U. Asadullaxo'jayev"), ("«Xurshid» (1906)", "Munavvarqori")], "Muharrirlar."),
    C(3, "«Oyna» jurnali qaysi yillarda?", "1913–1915", ["1906–1908", "1914–1917", "1917–1920"], "1913–1915.", b="madaniyat"),
    O(3, "«Taraqqiy» gazetasi muharriri familiyasini yozing (O...).", ["Obidov", "Ismoil Obidov"], "Obidov.", b="madaniyat"),
]

Q["10.1.19"] = [
    C(1, "Birinchi jahon urushi qaysi yillarda?", "1914–1918", ["1905–1907", "1939–1945", "1917–1922"], "1914–1918.", b="siyosiy"),
    C(1, "Urush yillarida Turkistonda nima ko'tarildi?", "Soliqlar va narxlar", ["Maosh", "Hosildorlik", "Ta'lim"], "Urush.", b="siyosiy"),
    C(1, "Urush Turkiston paxtasiga talabni?", "Oshirdi", ["Pasaytirdi", "To'xtatdi", "O'zgartirmadi"], "Paxta.", b="siyosiy"),
    C(2, "Urush yillarida Turkistonda aholi ahvoli?", "Og'irlashdi, ocharchilik", ["Yaxshilandi", "O'zgarmadi", "Boyidi"], "Ahvol.", b="siyosiy"),
    C(2, "Urush davrida mahalliy aholidan nimalar olingan?", "Ot-ulov, oziq-ovqat, soliq", ["Hech narsa", "Faqat pul", "Faqat kitob"], "Rekvizitsiya.", b="siyosiy"),
    C(2, "Rossiyada Birinchi jahon urushiga sabab bo'lgan blok?", "Antanta", ["NATO", "Varshava", "BMT"], "Antanta.", b="siyosiy"),
    C(3, "1916-yilgi mardikorlik farmoni qaysi yoshdagilarni qamragan?", "19–43 yosh", ["10–20", "50–60", "5–15"], "Farmon.", b="siyosiy"),
    O(3, "Birinchi jahon urushi boshlangan yilni yozing.", ["1914", "1914-yil"], "1914.", b="siyosiy"),
]

Q["10.1.20"] = [
    C(1, "Umumturkiston qo'zg'oloni qaysi yilda?", "1916", ["1898", "1917", "1914"], "1916.", b="siyosiy"),
    C(1, "1916-yil qo'zg'olon sababi?", "Mardikorlikka olish haqidagi podsho farmoni", ["Soliq kamayishi", "Din", "Til"], "Farmon.", b="siyosiy"),
    C(1, "Mardikorlik farmoni sanasi?", "1916-yil 25-iyun", ["1916-yil 25-yanvar", "1917-yil 25-iyun", "1914-yil"], "25 iyun.", b="siyosiy"),
    C(2, "Qo'zg'olon dastlab qaysi shaharda boshlangan?", "Xo'jand", ["Toshkent", "Samarqand", "Andijon"], "4 iyul.", b="siyosiy"),
    C(2, "Qo'zg'olon qaysi shaharlarga ham tarqaldi?", "Jizzax, Samarqand, Toshkent", ["Moskva", "Istanbul", "Tehron"], "Tarqalish.", b="siyosiy"),
    C(2, "Qozog'istonda qo'zg'olon rahbari?", "Amangeldi Imanov", ["Madaminbek", "Po'latxon", "Kenesari"], "Turg'ay.", b="siyosiy"),
    C(3, "Qo'zg'olon natijasi?", "Shafqatsiz bostirildi", ["G'alaba", "Sulh", "Rus chekindi"], "Bostirildi.", b="siyosiy"),
    O(3, "Mardikorlik farmoni e'lon qilingan va qo'zg'olon boshlangan yil (raqam).", ["1916", "1916-yil"], "1916.", b="siyosiy"),
]

Q["10.1.21"] = [
    C(1, "Fevral inqilobi qaysi mamlakatda?", "Rossiya", ["Fransiya", "Xitoy", "Turkiya"], "1917.", b="siyosiy"),
    C(1, "Fevral inqilobidan keyin Nikolay II nima qildi?", "Taxtdan voz kechdi", ["Qochdi", "Qatl etildi", "G'alaba qildi"], "Mart.", b="siyosiy"),
    C(1, "Fevral inqilobi qaysi yilda?", "1917", ["1905", "1914", "1924"], "1917.", b="siyosiy"),
    C(2, "Turkistonda Fevral inqilobi xabari qachon tarqaldi?", "Mart 1917", ["Iyun 1917", "Noyabr 1917", "Fevral 1918"], "Mart.", b="siyosiy"),
    C(2, "Fevral inqilobidan keyin hokimiyat kimning qo'liga o'tdi?", "Muvaqqat hukumat", ["Bolsheviklar", "Amir", "Xon"], "Muvaqqat.", b="siyosiy"),
    C(2, "Turkistonda Muvaqqat hukumat organi?", "Turkiston qo'mitasi", ["Ko'mita", "Sovet", "Parlament"], "Qo'mita.", b="siyosiy"),
    C(3, "Fevral inqilobi mahalliy aholiga nima berdi?", "Siyosiy faollik uchun imkon", ["To'liq mustaqillik", "Yer", "Hech narsa"], "Faollik.", b="siyosiy"),
    O(3, "1917-yil martida Rossiyada podsho hokimiyatini ag'dargan inqilob qaysi oy nomi bilan ataladi?", ["Fevral", "Fevral inqilobi", "fevral"], "Fevral inqilobi.", b="siyosiy"),
]

Q["10.1.22"] = [
    C(1, "Ikki hokimiyatchilik nima?", "Muvaqqat hukumat va Sho'rolarning parallel hokimiyati", ["Xon va amir", "Prezident va parlament", "Podsho va papa"], "Ikki hokimiyat.", b="siyosiy"),
    C(1, "Toshkent Sho'rosi qaysi tarkibdan iborat edi?", "Asosan ruslardan (ishchi va askarlar)", ["Mahalliy musulmonlardan", "Ziyolilardan", "Dehqonlardan"], "Sho'ro.", b="siyosiy"),
    C(1, "Mahalliy aholining Sho'rolarda ishtiroki?", "Deyarli yo'q edi", ["Ko'p edi", "To'liq edi", "Yarim edi"], "Past.", b="siyosiy"),
    C(2, "Muvaqqat hukumat tarafdorlari kimlar edi?", "Burjua va oqsuyaklar", ["Ishchilar", "Dehqonlar", "Askarlar"], "Burjua.", b="siyosiy"),
    C(2, "Toshkent Sho'rosi hokimiyatni qaysi sanada egalladi?", "1917-yil oktyabr oxiri", ["1917-yil mart", "1918-yil fevral", "1924-yil"], "Oktyabr.", b="siyosiy"),
    C(2, "Bolsheviklar ta'siri Turkistonda nimaga tayanadi?", "Rus ishchilari va garnizonlar", ["Dehqonlar", "Ruhoniylar", "Amir"], "Ishchilar.", b="siyosiy"),
    C(3, "Ikki hokimiyatchilik qanday tugadi?", "Bolsheviklar to'ntarishi bilan", ["Referendum", "Kelishuv", "Urush"], "To'ntarish.", b="siyosiy"),
    O(3, "1917-yilda Muvaqqat hukumat bilan birga ikkinchi hokimiyat bo'lgan, ishchi va askar deputatlari organlari nima deb atalgan?", ["Sho'rolar", "Sho'ro", "Sovet", "Sovetlar"], "Sho'rolar (sovetlar).", b="siyosiy"),
]

Q["10.1.23"] = [
    C(1, "Turkistonda 1917-yil mart oyida tuzilgan jadidlar tashkiloti?", "Sho'roi Islomiya", ["Alash", "Turon", "Sho'roi Ulamo"], "Mart.", b="siyosiy"),
    C(1, "«Sho'roi Ulamo» kimlarning tashkiloti?", "Ruhoniylarning (ulamolar)", ["Ishchilar", "Savdogarlar", "Askarlar"], "Ulamo.", b="siyosiy"),
    C(1, "«Sho'roi Islomiya» rahbarlaridan biri?", "Munavvarqori", ["Cho'lpon", "Fitrat", "Qodiriy"], "Munavvarqori.", b="siyosiy"),
    C(2, "«Sho'roi Ulamo» qachon tuzilgan?", "1917 yil (iyun)", ["1906", "1913", "1925"], "Iyun.", b="siyosiy"),
    C(2, "«Sho'roi Islomiya» va «Sho'roi Ulamo» orasida?", "Siyosiy qarashlar farqi bo'lgan", ["Farq yo'q", "Bir tashkilot", "Dushman"], "Farq.", b="siyosiy"),
    C(2, "«Ittifoqi Muslimin» partiyasi?", "Musulmonlar ittifoqi", ["Rus", "Bolshevik", "Eser"], "Ittifoq.", b="siyosiy"),
    C(3, "«Turon» partiyasi qachon?", "1917", ["1906", "1913", "1924"], "Turon.", b="siyosiy"),
    O(3, "1917-yil martda tuzilgan jadidlarning siyosiy tashkiloti nomini yozing («Sho'roi ...»).", ["Islomiya", "Sho'roi Islomiya", "Shoroi Islomiya"], "Sho'roi Islomiya.", b="siyosiy"),
]
