"""7-sinf: Ilk o'rta asrlar (V–XI asrlar) — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["7.1.1"] = [
    C(1, "V–VIII asrlarda Movarounnahrda «dehqonlar» kimlar edi?", "Yirik yer egalari, qasr va qal'a sohiblari", ["Oddiy ekinchilar", "Hunarmandlar", "Qullar"], "Dehqonlar — hukmron tabaqa.", b="ijtimoiy"),
    C(1, "Kadivlar kimlar edi?", "Dehqonlarga qaram, ularning yerida ishlovchi qishloq aholisi", ["Harbiy sarkardalar", "Savdogarlar", "Ruhoniylar"], "Kadivlar — qaram dehqonlar.", b="ijtimoiy"),
    C(1, "Chokarlar kimlar edi?", "Dehqonlarning professional harbiy gvardiyasi (soqchilari)", ["Savdogarlar", "Hunarmandlar", "Mirshablar"], "Chokarlar — shaxsiy harbiy otryad.", b="ijtimoiy"),
    C(2, "Buxoro hukmdorining unvoni qanday atalgan?", "Buxorxudot", ["Ixshid", "Afshin", "Xorazmshoh"], "Buxorxudot.", b="ijtimoiy"),
    C(2, "Farg'ona hukmdori qanday unvonda atalgan?", "Ixshid", ["Buxorxudot", "Afshin", "Xorazmshoh"], "Ixshid.", b="ijtimoiy"),
    C(2, "Ustrushona hukmdori unvoni qaysi?", "Afshin", ["Ixshid", "Buxorxudot", "Tudun"], "Afshin.", b="ijtimoiy"),
    C(3, "Quyidagi hukmdor-unvon juftliklaridan qaysi biri to'g'ri?", "Xorazm — xorazmshoh", ["Buxoro — afshin", "Farg'ona — buxorxudot", "Ustrushona — ixshid"], "Xorazm hukmdori xorazmshoh.", b="ijtimoiy"),
    O(3, "Buxoro hukmdorining V–VIII asrlardagi unvonini yozing.", ["buxorxudot", "Buxorxudot"], "Buxorxudot.", b="ijtimoiy"),
]

Q["7.1.2"] = [
    C(1, "Xionitlar O'rta Osiyoga qaysi asrda kirib kelgan?", "IV asr o'rtalarida", ["I asrda", "VII asrda", "X asrda"], "IV asrda.", b="siyosiy"),
    C(1, "Xionitlar qaysi davlat bilan uzoq kurashgan?", "Sosoniylar (Eron)", ["Rim", "Xitoy", "Arab xalifaligi"], "Sosoniylar bilan urushlar.", b="siyosiy"),
    C(1, "Kidariylar qaysi asrda Baqtriyada hokimiyatni qo'lga olgan?", "V asrda", ["II asrda", "VIII asrda", "XI asrda"], "Kidara boshchiligida.", b="siyosiy"),
    C(2, "Kidariylar davlatining asoschisi kim?", "Kidara", ["Kujula", "Bumin", "Peroz"], "Kidara.", b="siyosiy"),
    C(2, "Kidariylarni siqib chiqargan kuch kim?", "Eftaliylar", ["Arablar", "Mo'g'ullar", "Saljuqiylar"], "Eftaliylar.", b="siyosiy"),
    C(2, "Xionitlar jamiyatining asosiy mashg'uloti qaysi?", "Ko'chmanchi chorvachilik va harbiy yurishlar", ["Dengiz savdosi", "Dehqonchilik", "Hunarmandchilik"], "Jangovar ko'chmanchilar.", b="siyosiy"),
    C(3, "Xionitlar bilan bog'liq voqea qaysi?", "Eron bilan urush va keyinchalik ittifoq", ["Aleksandr yurishi", "Chingizxon yurishi", "Arab bosqini"], "IV asr urushi.", b="siyosiy"),
    O(3, "Baqtriyada V asrda davlat qurgan, Kidara nomi bilan ataladigan xalq nomini yozing (K...).", ["Kidariylar", "kidariylar", "Kidariy"], "Kidariylar.", b="siyosiy"),
]

Q["7.1.3"] = [
    C(1, "Eftaliylar davlati qaysi asrlarda mavjud bo'lgan?", "V asr 2-yarmi – VI asr o'rtalari", ["I–III asrlar", "IX–X asrlar", "XIII asr"], "V–VI asrlar.", b="siyosiy"),
    C(1, "Eftaliylar qaysi davlat bilan urushgan?", "Sosoniylar", ["Rim", "Kushon", "Arab xalifaligi"], "Peroz 484.", b="siyosiy"),
    C(1, "Sosoniy shohi Peroz eftaliylar bilan jangda qaysi yili halok bo'lgan?", "484-yilda", ["355-yilda", "552-yilda", "751-yilda"], "484.", b="siyosiy"),
    C(2, "Eftaliylar davlatini barham toptirgan kuch?", "Turk xoqonligi va Sosoniylar ittifoqi", ["Arab xalifaligi", "Qoraxitoylar", "Mo'g'ullar"], "VI asr o'rtalari.", b="siyosiy"),
    C(2, "Eftaliylar davrida tangalarni ko'proq nimaga taqlid qilib zarb etganlar?", "Sosoniy tangalariga", ["Rim tangalariga", "Xitoy tangalariga", "Hind tangalariga"], "Taqlid.", b="siyosiy"),
    C(2, "Eftaliylar davlatining hududi qaysi hududlarni qamragan?", "Tojikiston, Surxondaryo, Afg'oniston, So'g'diyona", ["Misr va Suriya", "Hindiston janubi", "Rossiya shimoli"], "Markaziy Osiyoning katta qismi.", b="siyosiy"),
    C(3, "Eftaliylar hukmdorlari Sosoniylar shohini nima uchun mag'lub etgan?", "Sosoniylar ichki kurashlarga botgan, eftaliy otliqlari kuchli bo'lgan", ["Yunon floti kuchli bo'lgan", "Ular temir yo'l qurgan", "Ular qurol-yarog'ga ega bo'lmagan"], "Harbiy ustunlik.", b="siyosiy"),
    O(3, "Sosoniy shohi Peroz qaysi yilda eftaliylar bilan jangda halok bo'lgan? (yilni yozing)", ["484", "484-yil"], "484-yil.", b="siyosiy"),
]

Q["7.1.4"] = [
    C(1, "Turk xoqonligi qaysi yili tashkil topgan?", "552-yilda", ["484-yilda", "603-yilda", "712-yilda"], "552.", b="siyosiy"),
    C(1, "Turk xoqonligining asoschisi kim?", "Bumin (Tumin)", ["Istami", "Qutayba", "Kidara"], "Bumin xoqon.", b="siyosiy"),
    C(1, "Turk xoqonligining g'arbiy qismini boshqargan Bumin ukasi kim?", "Istami", ["Bilga", "Kul Tigin", "Tardu"], "Istami yabg'u.", b="siyosiy"),
    C(2, "Turk xoqonligi qaysi yili G'arbiy va Sharqiy qismlarga bo'lindi?", "583-yil atrofida", ["552-yil", "751-yil", "712-yil"], "VI asr oxiri.", b="siyosiy"),
    C(2, "Qadimgi turkiy yozuv yodgorliklari qaysi daryolar yaqinida topilgan?", "Orxon va Enasoy", ["Nil", "Dajla", "Xuanxe"], "Orxon–Enasoy bitiklari.", b="siyosiy"),
    C(2, "Orxon–Enasoy bitiklarida qaysi xoqon va sarkardalar madh etilgan?", "Bilga xoqon va Kul Tigin", ["Chingizxon", "Mahmud G'aznaviy", "Alp Tegin"], "VIII asr.", b="siyosiy"),
    C(3, "Turk xoqonligining boshqaruv unvonlaridan qaysi biri «viloyat hokimi»ga yaqin ma'noda ishlatilgan?", "Yabg'u", ["Satrap", "Ixshid", "Imperator"], "Yabg'u.", b="siyosiy"),
    O(3, "Turk xoqonligiga asos solgan xoqon ismini yozing (B...).", ["Bumin", "bumin", "Tumin"], "Bumin.", b="siyosiy"),
]

Q["7.1.5"] = [
    C(1, "Eftaliylar davlati qaysi ittifoq tomonidan tor-mor etilgan?", "Turk–Sosoniy ittifoqi", ["Arab–Xitoy ittifoqi", "Rim–Yunon ittifoqi", "Hind–Kushon ittifoqi"], "VI asr o'rtalari.", b="siyosiy"),
    C(1, "Turk xoqonligi Eftaliylar bilan kurashda kim bilan ittifoq tuzgan?", "Sosoniylar", ["Vizantiya", "Kushonlar", "Xitoy"], "Xusrav I Anushervon.", b="siyosiy"),
    C(1, "Turk–Sosoniy ittifoqini mustahkamlagan nikoh kimning qizi bilan?", "Xoqonning qizi Xusrav I ga turmushga berilgan", ["Xusravning qizi xoqonga", "Peroz qizi Istamiga", "Kidara qizi Buminga"], "Siyosiy nikoh.", b="siyosiy"),
    C(2, "Turk xoqonligi Vizantiya bilan aloqada kimni elchi qilib yuborgan?", "So'g'd elchisi Maniaxni", ["Qutaybani", "Chjan Szyanni", "Spitamenni"], "568-yil.", b="siyosiy"),
    C(2, "Maniax qaysi davlatga elchi bo'lib borgan?", "Vizantiya", ["Xitoy", "Rim", "Hindiston"], "568.", b="siyosiy"),
    C(2, "Turk xoqonligi va Sosoniylar o'rtasidagi kelishmovchilik nimadan kelib chiqdi?", "Ipak savdosi yo'llari va tovarlar nazorati", ["Dinning farqi", "Dengiz chegaralari", "Til"], "Ipak yo'li.", b="siyosiy"),
    C(3, "Eftaliylar mag'lubiyatidan keyin ularning hududi...", "Turk xoqonligi va Sosoniylar o'rtasida bo'lib olindi", ["Arablarga o'tdi", "Xitoyga qo'shildi", "Rimga qo'shildi"], "Amudaryo chegara bo'lgan.", b="siyosiy"),
    O(3, "568-yilda Vizantiyaga elchi bo'lib borgan so'g'dlik elchi ismini yozing (M...).", ["Maniax", "maniax"], "Maniax.", b="siyosiy"),
]

Q["7.1.6"] = [
    C(1, "G'arbiy Turk xoqonligi qaysi yildan mustaqil davlatga aylandi?", "603-yildan", ["552-yildan", "712-yildan", "751-yildan"], "603.", b="siyosiy"),
    C(1, "G'arbiy Turk xoqonligining poytaxti qaysi?", "Suyob", ["Samarqand", "Bityan", "Marv"], "Chu vodiysidagi Suyob.", b="siyosiy"),
    C(1, "G'arbiy Turk xoqonligi qaysi asrlarda mavjud bo'lgan?", "VI–VIII asrlarda", ["I–III asrlarda", "IX–X asrlarda", "XIII asrda"], "VI–VIII.", b="siyosiy"),
    C(2, "Tong yabg'u xoqon qachon hukmronlik qilgan?", "618–630-yillarda", ["552–582-yillarda", "712–715-yillarda", "999-yilda"], "G'arbiy turk xoqonligi cho'qqisi.", b="siyosiy"),
    C(2, "G'arbiy Turk xoqonligi qaysi imperiya bilan kurashgan?", "Xitoy Tan imperiyasi", ["Rim", "Hind", "Vizantiya"], "VII asr.", b="siyosiy"),
    C(2, "G'arbiy Turk xoqonligi hududida Choch (Toshkent) qanday maqomda edi?", "Vassal (xoqonlikka qaram) viloyat", ["Poytaxt", "Mustaqil imperiya", "Xitoy viloyati"], "Tudun boshqargan.", b="siyosiy"),
    C(3, "G'arbiy Turk xoqonligining zaiflashuviga sabab bo'lgan omil qaysi?", "Ichki kurash va Xitoy hujumlari", ["Zilzila", "Kasallik", "Dengiz toshqini"], "VII asr.", b="siyosiy"),
    O(3, "G'arbiy Turk xoqonligi mustaqil bo'lgan yilni yozing.", ["603", "603-yil"], "603.", b="siyosiy"),
]

Q["7.1.7"] = [
    C(1, "V–VIII asrlarda yirik yer egalari qanday qasr va qal'alarda yashagan?", "Mustahkam qal'a-qasrlarda", ["Chodirlarda", "G'orlarda", "Kulbalarda"], "Dehqonlar qal'asi.", b="ijtimoiy"),
    C(1, "Afrosiyob (Samarqand) devoriy rasmlari qaysi asrga mansub?", "VII asr", ["II asr", "XI asr", "XV asr"], "Elchilar rasmi.", b="madaniyat"),
    C(1, "Afrosiyob devoriy rasmlarida kimning saroyi tasvirlangan?", "So'g'd hukmdori Varxuman", ["Kanishka", "Ulug'bek", "Amir Temur"], "Varxuman.", b="madaniyat"),
    C(2, "Buxoro yaqinidagi VII–VIII asr qasri qaysi?", "Varaxsha", ["Ayritom", "Termiz", "Qo'yqirilgan"], "Buxorxudotlar qasri.", b="madaniyat"),
    C(2, "Quva (Farg'ona) yodgorligi qanday inshoot?", "Buddaviy ibodatxona (VII–VIII asr)", ["Madrasa", "Masjid", "Maqbara"], "Quva.", b="madaniyat"),
    C(2, "V–VIII asrlarda yer egaligining asosiy shakli?", "Dehqonlarning katta xususiy mulki", ["Davlat mulki emas", "Umumiy jamoa", "Faqat shahar mulki"], "Yer egaligi.", b="ijtimoiy"),
    C(3, "Panjikent qasrlarida topilgan devoriy rasmlarda nima aks etgan?", "So'g'd afsonalari va ijtimoiy hayot manzaralari", ["Arab alifbosi", "Hind xudolari faqat", "Rim imperatorlari"], "So'g'd san'ati.", b="madaniyat"),
    O(3, "Samarqanddagi VII asr devoriy rasmlari topilgan tarixiy yodgorlik nomini yozing (A...).", ["Afrosiyob", "afrosiyob"], "Afrosiyob.", b="madaniyat"),
]

Q["7.1.8"] = [
    C(1, "Arab xalifaligi qaysi asrda tashkil topgan?", "VII asrda", ["III asrda", "X asrda", "XIII asrda"], "Xalifalik VII asrda tashkil topgan.", b="siyosiy"),
    C(1, "Umaviylar xalifaligining poytaxti qaysi shahar?", "Damashq", ["Bag'dod", "Madina", "Qohira"], "661–750.", b="siyosiy"),
    C(1, "Abbosiylar xalifaligining poytaxti?", "Bag'dod", ["Damashq", "Makka", "Marv"], "750 dan.", b="siyosiy"),
    C(2, "Abbosiylar sulolasi qaysi yildan hokimiyat tepasiga kelgan?", "750-yil", ["661-yil", "632-yil", "822-yil"], "750.", b="siyosiy"),
    C(2, "751-yildagi Talas jangi kimlar o'rtasida bo'lgan?", "Arablar va Xitoy", ["Arablar va Vizantiya", "Mo'g'ullar va Xorazm", "Turklar va Eron"], "Talas.", b="siyosiy"),
    C(2, "Xurosonda Abbosiylarga yordam bergan sarkarda kim?", "Abu Muslim", ["Qutayba", "Muqanna", "Rofe"], "Abu Muslim.", b="siyosiy"),
    C(3, "Umaviylar xalifaligi qaysi yilda tugatilgan?", "750-yilda", ["661-yilda", "632-yilda", "900-yilda"], "750.", b="siyosiy"),
    O(3, "Arablar va Xitoy o'rtasidagi Talas jangi qaysi yilda bo'lgan? (raqam)", ["751", "751-yil"], "751.", b="siyosiy"),
]

Q["7.1.9-10"] = [
    C(1, "Movarounnahrni bosib olgan arab sarkardasi kim?", "Qutayba ibn Muslim", ["Abu Muslim", "Rofe ibn Lays", "Muqanna"], "Qutayba ibn Muslim.", b="siyosiy"),
    C(1, "Qutayba ibn Muslim qaysi yillarda Xuroson noibi bo'lgan?", "705–715-yillarda", ["552–582-yillarda", "776–783-yillarda", "999–1005-yillarda"], "Xuroson noibi.", b="siyosiy"),
    C(1, "Buxoro Qutayba tomonidan qaysi yili bosib olingan?", "709-yilda", ["706-yilda", "712-yilda", "715-yilda"], "709.", b="siyosiy"),
    C(2, "Samarqand arablar tomonidan qaysi yili bosib olingan?", "712-yilda", ["706-yilda", "709-yilda", "751-yilda"], "712.", b="siyosiy"),
    C(2, "Qutayba yurishlari davomida birinchi bo'lib qaysi shahar bosib olingan?", "Paykend", ["Samarqand", "Xiva", "Termiz"], "706-yil.", b="siyosiy"),
    C(2, "Samarqand so'g'd hukmdori kim edi (arab yurishi paytida)?", "Tarxun", ["Divashtich", "Muqanna", "Abu Muslim"], "Tarxun (keyin G'urak).", b="siyosiy"),
    C(3, "Qutayba qaysi yili halok bo'lgan?", "715-yilda", ["709-yilda", "751-yilda", "776-yilda"], "715.", b="siyosiy"),
    O(3, "Samarqand arablar tomonidan qaysi yilda bosib olingan? (raqam bilan)", ["712", "712-yil"], "712.", b="siyosiy"),
]

Q["7.1.11"] = [
    C(1, "Mug' tog'i arxivi qaysi xalq tilida yozilgan hujjatlardan iborat?", "So'g'd tilida", ["Arab tilida", "Xitoy tilida", "Hind tilida"], "So'g'd hujjatlari.", b="siyosiy"),
    C(1, "Mug' tog'i arxivi qaysi daryo havzasida topilgan?", "Zarafshon", ["Sirdaryo", "Amudaryo", "Chirchiq"], "Zarafshon yuqori.", b="siyosiy"),
    C(1, "Mug' qal'asida arablarga qarshi kurashgan So'g'd hukmdori?", "Divashtich", ["Muqanna", "Tarxun", "Rofe"], "Panjikent hukmdori.", b="siyosiy"),
    C(2, "Divashtich qaysi shahar hukmdori bo'lgan?", "Panjikent", ["Buxoro", "Xorazm", "Kesh"], "Panjikent.", b="siyosiy"),
    C(2, "Divashtich qaysi yilda halok bo'lgan?", "722-yilda", ["712-yilda", "751-yilda", "776-yilda"], "722.", b="siyosiy"),
    C(2, "Mug' arxivi hujjatlari nima haqida?", "Savdo, soliq va siyosiy yozishmalar", ["Faqat she'rlar", "Faqat dinga oid", "Faqat harbiy xaritalar"], "Hujjat arxivi.", b="siyosiy"),
    C(3, "Mug' tog'i arxivi qaysi yili topilgan?", "1933-yilda", ["1850-yilda", "1991-yilda", "1900-yilda"], "1933.", b="siyosiy"),
    O(3, "Mug' tog'i qal'asida arablarga qarshi kurashgan so'g'd hukmdorining ismini yozing (D...).", ["Divashtich", "divashtich"], "Divashtich.", b="siyosiy"),
]

Q["7.1.12"] = [
    C(1, "Sharik ibn Shayx qo'zg'oloni qaysi shaharda boshlangan?", "Buxoroda", ["Samarqandda", "Xivada", "Toshkentda"], "Buxoro.", b="siyosiy"),
    C(1, "Sharik ibn Shayx qo'zg'oloni qaysi yilda bo'lgan?", "750-yilda", ["776-yilda", "806-yilda", "822-yilda"], "750.", b="siyosiy"),
    C(1, "Qo'zg'olonchilar qaysi hukmronlikka qarshi chiqqan?", "Abbosiylar hokimiyatiga", ["Umaviylarga", "Sosoniylarga", "Turk xoqonligiga"], "Abbosiylarga qarshi.", b="siyosiy"),
    C(2, "Qo'zg'olonning ijtimoiy asosi?", "Soliq zulmidan norozi aholi", ["Savdogarlar", "Dengizchilar", "Mo'g'ullar"], "Soliqqa qarshi.", b="siyosiy"),
    C(2, "Sharik ibn Shayx qo'zg'olonini bostirgan Abu Muslimning sarkardasi?", "Ziyod ibn Solih", ["Qutayba", "Rofe", "Tarxun"], "Ziyod ibn Solih.", b="siyosiy"),
    C(2, "Sharik ibn Shayx qo'zg'oloni qaysi shiorlar ostida bo'lgan?", "Abbosiylarga qarshi, adolat uchun", ["Islomga qarshi", "Buddizm uchun", "Zardushtiylik uchun"], "Adolat.", b="siyosiy"),
    C(3, "Sharik ibn Shayx qo'zg'olonidan keyingi yirik qo'zg'olon qaysi?", "Muqanna qo'zg'oloni", ["Spitamen qo'zg'oloni", "Vabo isyoni", "Po'latxon qo'zg'oloni"], "776–783.", b="siyosiy"),
    O(3, "Abbosiylarga qarshi Buxoroda 750-yilda qo'zg'olon ko'targan kishi ismini yozing (Sharik ibn ...).", ["Sharik ibn Shayx", "Shayx", "Sharik"], "Sharik ibn Shayx.", b="siyosiy"),
]

Q["7.1.13"] = [
    C(1, "Muqanna qo'zg'oloni qaysi yillarda bo'lgan?", "776–783-yillarda", ["750-yilda", "806–810-yillarda", "875-yilda"], "776–783.", b="siyosiy"),
    C(1, "Muqanna qo'zg'olonchilari qanday ataladi?", "Oq kiyimlilar", ["Qizil bayroqlilar", "Qora kiyimlilar", "Yashil sarbozlar"], "Oq kiyimlilar.", b="siyosiy"),
    C(1, "Muqanna qo'zg'olonining markazi qaysi qal'a?", "Sanom qal'asi", ["Ark", "Raboti Malik", "Ichan Qal'a"], "Qashqadaryo.", b="siyosiy"),
    C(2, "Qo'zg'olonni bostirish uchun qo'shin yuborgan xalifa kim?", "Al-Mahdiy", ["Horun ar-Rashid", "Al-Ma'mun", "Abu Muslim"], "Al-Mahdiy.", b="siyosiy"),
    C(2, "Muqanna qo'zg'olonining boshlangan joyi?", "Kesh (Qashqadaryo) va Sug'd yerlari", ["Xorazm", "Farg'ona", "Toshkent"], "Kesh.", b="siyosiy"),
    C(2, "Muqannaning asl ismi?", "Hoshim ibn Hakim", ["Rofe ibn Lays", "Abu Muslim", "Sharik ibn Shayx"], "Hoshim.", b="siyosiy"),
    C(3, "Muqanna nima uchun shunday nom olgan?", "Yuzini niqob («muqanna») bilan yopib yurgani uchun", ["Qo'shini oq bo'lgani uchun", "Qal'a nomidan", "Shahar nomidan"], "Niqobdor.", b="siyosiy"),
    O(3, "Muqanna qo'zg'oloni qaysi yilda tugagan? (raqam)", ["783", "783-yil"], "783.", b="siyosiy"),
]

Q["7.1.14"] = [
    C(1, "Rofe ibn Lays qo'zg'oloni qaysi yillarda bo'lgan?", "806–810-yillarda", ["776–783-yillarda", "750-yilda", "900-yilda"], "806–810.", b="siyosiy"),
    C(1, "Rofe ibn Lays qo'zg'oloni qaysi shaharda boshlangan?", "Samarqandda", ["Buxoroda", "Xivada", "Marvda"], "Samarqand.", b="siyosiy"),
    C(1, "Rofe qo'zg'oloni davrida xalifa kim edi?", "Horun ar-Rashid", ["Al-Mahdiy", "Abu Muslim", "Al-Ma'mun"], "Horun ar-Rashid.", b="siyosiy"),
    C(2, "Qo'zg'olonni bostirishda yordam bergan Somonxudotning nabiralari?", "Nuh, Ahmad, Yahyo, Ilyos", ["Nasr va Ismoil", "Ali va Husayn", "Tohir va Ya'qub"], "Somoniylar.", b="siyosiy"),
    C(2, "Somoniylarga qaysi shaharlar boshqaruvi berilgan?", "Samarqand, Farg'ona, Shosh, Hirot", ["Marv, Xiva, Termiz, Qo'qon", "Buxoro, Xiva, Marv, Hirot", "Samarqand, Buxoro, Termiz, Marv"], "Mukofot.", b="siyosiy"),
    C(2, "Xalifa Ma'munning Xurosondagi vaqtinchalik markazi?", "Marv", ["Samarqand", "Damashq", "Madina"], "Ma'mun Marvda turgan.", b="siyosiy"),
    C(3, "Rofe qo'zg'oloni qaysi yilda tugagan?", "810-yilda", ["806-yilda", "783-yilda", "822-yilda"], "810.", b="siyosiy"),
    O(3, "Rofe ibn Lays qo'zg'oloni boshlangan shahar nomini yozing.", ["Samarqand", "samarqand"], "Samarqand.", b="siyosiy"),
]

Q["7.1.15"] = [
    C(1, "Yer solig'i qanday atalgan?", "Xiroj", ["Zakot", "Jizya", "Begor"], "Xiroj.", b="ijtimoiy"),
    C(1, "Musulmon bo'lmaganlardan olingan jon solig'i?", "Jizya", ["Zakot", "Xiroj", "Ushr"], "Jizya.", b="ijtimoiy"),
    C(1, "Mulk solig'i — zakot odatda qancha miqdorda?", "Mulkning 1/40 qismi (2,5%)", ["1/10", "1/3", "1/2"], "2,5%.", b="ijtimoiy"),
    C(2, "Musulmon yer egalaridan olinadigan yer solig'i?", "Ushr", ["Jizya", "Xiroj faqat", "Begor"], "Ushr 1/10.", b="ijtimoiy"),
    C(2, "Davlat ishlari uchun bepul majburiy mehnat?", "Begor", ["Hashar", "Tanob puli", "Zakot"], "Begor.", b="ijtimoiy"),
    C(2, "Hosilning 1/3–1/5 gacha qismini tashkil qilgan soliq?", "Xiroj", ["Zakot", "Ushr", "Jizya"], "Xiroj.", b="ijtimoiy"),
    C(3, "Arab xalifaligi davrida aholining ko'p qismi qaysi soliqdan g'azablangan?", "Xiroj va jizya", ["Faqat zakot", "Faqat ushr", "Hashar"], "Qo'zg'olon sababi.", b="ijtimoiy"),
    O(3, "Musulmon bo'lmaganlardan olinadigan jon solig'ining nomini yozing (J...).", ["Jizya", "jizya"], "Jizya.", b="ijtimoiy"),
]

Q["7.1.16-17"] = [
    C(1, "Tohiriylar davlati qaysi yillarda hukmronlik qilgan?", "821–873-yillarda", ["750–776-yillarda", "875–999-yillarda", "1040–1157-yillarda"], "821–873.", b="siyosiy"),
    C(1, "Tohiriylar sulolasining asoschisi kim?", "Tohir ibn Husayn", ["Ya'qub ibn Lays", "Ismoil Somoniy", "Nuh ibn Asad"], "Tohir.", b="siyosiy"),
    C(1, "Safforiylar sulolasining asoschisi kim?", "Ya'qub ibn Lays as-Saffor", ["Tohir ibn Husayn", "Nasr ibn Ahmad", "Qutayba"], "Ya'qub.", b="siyosiy"),
    C(2, "«Saffor» so'zining ma'nosi?", "Misgar (mis idish yasovchi)", ["Dehqon", "Savdogar", "Qozi"], "Misgar.", b="siyosiy"),
    C(2, "Safforiylar davlatining poytaxti qaysi shahar?", "Zaranj", ["Samarqand", "Nishopur", "Marv"], "Zaranj.", b="siyosiy"),
    C(2, "Tohiriylarning poytaxti qaysi shahar?", "Nishopur (Marvdan keyin)", ["Samarqand", "Bag'dod", "Buxoro"], "Nishopur.", b="siyosiy"),
    C(3, "Safforiylarni mag'lub etgan hukmdor?", "Ismoil Somoniy (Balx jangi, 900)", ["Nasr ibn Ahmad", "Mahmud G'aznaviy", "Alp Tegin"], "900.", b="siyosiy"),
    O(3, "Safforiylar sulolasi qaysi yilda Ismoil Somoniy tomonidan Balx jangida mag'lub etilgan? (raqam)", ["900", "900-yil"], "900.", b="siyosiy"),
]

Q["7.1.18"] = [
    C(1, "Somoniylar davlati qaysi yillarda mavjud bo'lgan?", "875–999-yillar", ["821–873", "1040–1157", "1370–1507"], "875–999.", b="siyosiy"),
    C(1, "Somoniylar sulolasi nomi kimdan kelib chiqqan?", "Somonxudot", ["Ismoil", "Nasr", "Ahmad"], "Somonxudot.", b="siyosiy"),
    C(1, "Samarqand hokimi sifatida Somoniylar davlatiga asos solgan Ahmadning o'g'li?", "Nasr ibn Ahmad", ["Ismoil", "Nuh", "Yahyo"], "Nasr.", b="siyosiy"),
    C(2, "Nasr ibn Ahmad qaysi yilda Samarqand hokimi bo'lgan?", "875-yilda", ["900-yilda", "750-yilda", "999-yilda"], "875.", b="siyosiy"),
    C(2, "Nasr ibn Ahmadning ukasi, keyinchalik davlat boshlig'i kim?", "Ismoil ibn Ahmad", ["Nuh ibn Asad", "Yahyo ibn Asad", "Ilyos"], "Ismoil.", b="siyosiy"),
    C(2, "Somoniylar poytaxti qaysi shahar?", "Buxoro", ["Samarqand", "Marv", "Termiz"], "Buxoro.", b="siyosiy"),
    C(3, "Nasr ibn Ahmad qaysi yilgacha hukmronlik qilgan?", "892-yilgacha", ["900-yilgacha", "875-yilgacha", "907-yilgacha"], "874–892.", b="siyosiy"),
    O(3, "Somoniylar davlati poytaxtini yozing.", ["Buxoro", "buxoro"], "Buxoro.", b="siyosiy"),
]

Q["7.1.19"] = [
    C(1, "Ismoil Somoniy qaysi yillarda hukmronlik qilgan?", "892–907-yillar", ["874–892", "907–914", "914–943"], "892–907.", b="siyosiy"),
    C(1, "Ismoil Somoniy qaysi jangda Amr ibn Lays Safforiyni mag'lub etgan?", "Balx jangida (900)", ["Dandanaqan jangi", "Loy jangi", "Anqara jangi"], "900.", b="siyosiy"),
    C(1, "Ismoil Somoniy maqbarasi qaysi shaharda?", "Buxoroda", ["Samarqandda", "Xivada", "Termizda"], "Buxoro.", b="madaniyat"),
    C(2, "Ismoil Somoniy Taroz (Ota) shahrini qachon egallagan?", "893-yilda", ["900-yilda", "875-yilda", "907-yilda"], "893.", b="siyosiy"),
    C(2, "Ismoil Somoniy maqbarasi qanday qurilgan?", "Pishgan g'ishtdan", ["Marmardan", "Yog'ochdan", "Tosh-qumdan"], "G'isht naqsh.", b="madaniyat"),
    C(2, "Ismoil Somoniy davrida Somoniylar davlati poytaxti?", "Buxoro", ["Marv", "Nishopur", "Samarqand"], "Buxoro.", b="siyosiy"),
    C(3, "Balx jangida asirga olingan safforiy hukmdor?", "Amr ibn Lays", ["Ya'qub ibn Lays", "Tohir ibn Husayn", "Nasr ibn Ahmad"], "Amr.", b="siyosiy"),
    O(3, "Ismoil Somoniy Safforiylarni mag'lub etgan jang qaysi yilda bo'lgan? (raqam)", ["900", "900-yil"], "900.", b="siyosiy"),
]

Q["7.1.20"] = [
    C(1, "Somoniylarda hukmdor saroyi qanday ataladi?", "Dargoh", ["Devon", "Madrasa", "Rabot"], "Dargoh.", b="ijtimoiy"),
    C(1, "Somoniylarda barcha devonlarni muvofiqlashtiruvchi bosh devon qaysi?", "Devoni vazir", ["Devoni mustavfiy", "Devoni mushrif", "Devoni jandar"], "Vazir.", b="ijtimoiy"),
    C(1, "Davlat xazinasi, daromad va xarajatlar devoni?", "Devoni mustavfiy", ["Devoni vazir", "Devoni mushrif", "Devoni jandar"], "Moliya.", b="ijtimoiy"),
    C(2, "Maxfiy xizmat, ichki nazorat va axborot yig'ish devoni?", "Devoni mushrif", ["Devoni mustavfiy", "Devoni vazir", "Devoni jandar"], "Mushrif.", b="ijtimoiy"),
    C(2, "Hukmdor saroyi xavfsizligi va soqchilar xizmati devoni?", "Devoni jandar", ["Devoni mushrif", "Devoni vazir", "Devoni mustavfiy"], "Jandar.", b="ijtimoiy"),
    C(2, "Somoniylar davlati boshqaruvi nimaga asoslangan?", "Devonlar tizimiga", ["Satrapliklarga", "Polislarga", "Nomlarga"], "Devonlar.", b="ijtimoiy"),
    C(3, "Quyidagi devon-vazifa juftliklaridan qaysi biri noto'g'ri?", "Devoni vazir — soqchilar xizmati", ["Devoni mustavfiy — moliya", "Devoni mushrif — nazorat", "Devoni jandar — saroy xavfsizligi"], "Vazir — bosh devon.", b="ijtimoiy"),
    O(3, "Somoniylarda moliya (xazina)ga mas'ul devon nomini yozing (Devoni ...).", ["Devoni mustavfiy", "mustavfiy"], "Mustavfiy.", b="ijtimoiy"),
]

Q["7.1.21"] = [
    C(1, "Somoniylar davrida qaysi tangalar zarb etilgan?", "Kumush dirhamlar", ["Oltin dariqlar", "Mis chaqalar faqat", "Bronza tangalar"], "Dirham.", b="ijtimoiy"),
    C(1, "IX–X asrlarda qaysi shaharda qog'oz ishlab chiqarilgan?", "Samarqandda", ["Rimda", "Afinada", "Parijda"], "Samarqand qog'ozi.", b="ijtimoiy"),
    C(1, "Somoniylar davrida savdo ko'proq qayerlar bilan olib borilgan?", "Sharq va G'arb mamlakatlari bilan", ["Faqat ichki bozorda", "Amerika bilan", "Avstraliya bilan"], "Karvon yo'llari.", b="ijtimoiy"),
    C(2, "Samarqand qog'ozi sirini arablar kimlardan o'rganganlar?", "Xitoylik asirlardan (Talas jangidan keyin)", ["Yunonlardan", "Hindlardan", "Misrliklardan"], "751 dan keyin.", b="ijtimoiy"),
    C(2, "Somoniylar davrida qaysi mintaqa tangalari ko'p zarb etilgan?", "Samarqand, Buxoro, Shosh, Termiz", ["Nil bo'yi", "Hind vodiysi", "Shimoliy Yevropa"], "Zarbxonalar.", b="ijtimoiy"),
    C(2, "Somoniylar davrida hunarmandchilikning rivojlangan turlari?", "Kulolchilik, shishasozlik, to'qimachilik", ["Kemasozlik", "Avtomobil", "Radio"], "Hunarmandlar.", b="ijtimoiy"),
    C(3, "Somoniylar davrida pul tizimi nimaga qarab tartibga solindi?", "Yagona kumush dirham og'irligi bo'yicha", ["Oltin faqat", "Mis chaqa faqat", "Tovar ayirboshlash faqat"], "Pul islohoti.", b="ijtimoiy"),
    O(3, "Somoniylar davrida zarb etilgan kumush tanganing arabcha nomini yozing (D...).", ["dirham", "Dirham"], "Dirham.", b="ijtimoiy"),
]

Q["7.1.22"] = [
    C(1, "Qoraxoniylar davlatining tashkil topishi qaysi asr bilan bog'liq?", "X asr", ["IV asr", "XV asr", "XVIII asr"], "X asr.", b="siyosiy"),
    C(1, "Qoraxoniylar hukmdorlarining unvoni?", "Xon (ilak, xoqon)", ["Sulton faqat", "Amir faqat", "Podsho faqat"], "Ilak xon.", b="siyosiy"),
    C(1, "Qoraxoniylar Somoniylar poytaxti Buxoroni qaysi yili egallagan?", "999-yilda", ["900-yilda", "1040-yilda", "1370-yilda"], "999.", b="siyosiy"),
    C(2, "Qoraxoniylar davlatining poytaxti qaysi shahar edi?", "Balasog'un va Qashg'ar", ["Buxoro va Samarqand", "Marv va Nishopur", "Xiva va Urganch"], "Dastlabki markazlar.", b="siyosiy"),
    C(2, "Qoraxoniylar o'zlarini kimlarning avlodi deb hisoblagan?", "Turk xoqonlarining", ["Arablarning", "Eronliklarning", "Yunonlarning"], "Turkiy sulola.", b="siyosiy"),
    C(2, "Qoraxoniylardan islomni qabul qilgan ilk hukmdor?", "Satuq Bug'roxon", ["Nasr ibn Ahmad", "Ismoil Somoniy", "Mahmud G'aznaviy"], "Satuq.", b="siyosiy"),
    C(3, "Somoniylar poytaxti Buxoroni 999-yilda egallagan Qoraxoniy hukmdor?", "Nasr ibn Ali (Ilakxon)", ["Satuq Bug'roxon", "Mahmud", "Alp Tegin"], "Nasr ibn Ali.", b="siyosiy"),
    O(3, "Qoraxoniylar Buxoroni qaysi yilda egallagan? (raqam)", ["999", "999-yil"], "999.", b="siyosiy"),
]

Q["7.1.23"] = [
    C(1, "Somoniylar davlati qachon tugatilgan?", "999-yilda", ["900-yilda", "875-yilda", "1040-yilda"], "999.", b="siyosiy"),
    C(1, "Somoniylar davlatining inqiroziga ichki sabablardan biri?", "Turk harbiy sarkardalarining kuchayishi", ["Aholining ko'payishi", "Savdoning yuksalishi", "Dehqonchilikning rivoji"], "Harbiy zodagonlar.", b="siyosiy"),
    C(1, "G'aznaviylar davlati asoschisi sifatida mashhur bo'lgan Somoniylar sarkardasi?", "Alp Tegin", ["Subuktegin", "Mahmud", "Mas'ud"], "Alp Tegin.", b="siyosiy"),
    C(2, "Somoniylarning so'nggi hukmdori kim?", "Ismoil Muntasir", ["Nuh ibn Mansur", "Ismoil Somoniy", "Nasr ibn Ahmad"], "Muntasir.", b="siyosiy"),
    C(2, "Somoniylar davlatining qulashiga tashqi sabab?", "Qoraxoniylar va G'aznaviylar hujumi", ["Arablar hujumi", "Rim hujumi", "Mo'g'ullar hujumi"], "999.", b="siyosiy"),
    C(2, "Muntasir qaysi yili halok bo'lgan?", "1005-yilda", ["999-yilda", "900-yilda", "1040-yilda"], "1005.", b="siyosiy"),
    C(3, "Somoniylar o'rniga Movarounnahrda qaysi davlat hukmronlik qildi?", "Qoraxoniylar davlati", ["G'aznaviylar davlati", "Xorazmshohlar davlati", "Saljuqiylar"], "Movarounnahr.", b="siyosiy"),
    O(3, "Somoniylar davlati tugatilgan yilni yozing.", ["999", "999-yil"], "999.", b="siyosiy"),
]

Q["7.1.24"] = [
    C(1, "Qoraxoniylar davlati qaysi XI asr o'rtasida ikkiga bo'linadi?", "Sharqiy va G'arbiy", ["Shimoliy va Janubiy", "Katta va Kichik", "Eron va Turon"], "Ikki xonlik.", b="siyosiy"),
    C(1, "Iqto nima?", "Harbiy xizmat evaziga berilgan yer (daromad olish huquqi)", ["Davlat ma'muriy bo'limi", "Soliq turi", "Sud tizimi"], "Iqto.", b="ijtimoiy"),
    C(1, "Iqto egasi qanday ataladi?", "Iqtodor", ["Dehqon", "Kadiv", "Chokar"], "Iqtodor.", b="ijtimoiy"),
    C(2, "Raboti Malik karvonsaroyi qaysi yili qurilgan?", "1078-yilda", ["1127-yilda", "1417-yilda", "1646-yilda"], "1078.", b="madaniyat"),
    C(2, "Raboti Malik karvonsaroyini kim qurdirgan?", "Shams al-Mulk", ["Arslonxon", "Ulug'bek", "Yalangto'sh"], "Shams al-Mulk.", b="madaniyat"),
    C(2, "Kalon minorasi kim tomonidan qurilgan?", "Arslonxon Muhammad (me'mor Baqo)", ["Shams al-Mulk", "Abdulaziz", "Amir Temur"], "1127.", b="madaniyat"),
    C(3, "Iqto tizimining oqibati qanday bo'ldi?", "Markaziy hokimiyat zaiflashdi, mahalliy hokimlar kuchaydi", ["Davlat kuchaydi", "Dehqonlar boydi", "Savdo to'xtadi"], "Tarqoqlik.", b="ijtimoiy"),
    O(3, "Kalon minorasi qaysi yilda qurilgan? (raqam)", ["1127", "1127-yil"], "1127.", b="madaniyat"),
]
