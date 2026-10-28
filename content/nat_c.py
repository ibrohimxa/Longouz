"""Ona tili va adabiyot: 9–11-sinf — murakkab sintaksis, nutq uslublari, adabiyot nazariyasi va asarlar."""
from ._dsl import C, O, M

Q = {}

Q["N9.1"] = [
    C(1, "Predmet belgisini bildiruvchi ikkinchi darajali bo'lak?", "Aniqlovchi", ["To'ldiruvchi", "Hol", "Ega"], "Qanday? qaysi? kimning?"),
    C(1, "Ish-harakat predmetini bildiruvchi ikkinchi darajali bo'lak?", "To'ldiruvchi", ["Aniqlovchi", "Hol", "Kesim"], "Kimni? nimani? kimga?"),
    C(1, "Ish-harakatning o'rni, payti, tarzini bildiruvchi bo'lak?", "Hol", ["Aniqlovchi", "To'ldiruvchi", "Ega"], "Qachon? qayerda? qanday?"),
    C(2, "«Do'stimning kitobi» da «do'stimning» qaysi bo'lak?", "Qaratqich aniqlovchi", ["Sifatlovchi aniqlovchi", "To'ldiruvchi", "Hol"], "Kimning? — qaratqich."),
    C(2, "«Chiroyli gul» da «chiroyli» qaysi bo'lak?", "Sifatlovchi aniqlovchi", ["Qaratqich aniqlovchi", "Hol", "Kesim"], "Qanday?"),
    C(2, "«Kitobni o'qidi» da «kitobni» qaysi bo'lak?", "Vositasiz to'ldiruvchi", ["Vositali to'ldiruvchi", "Hol", "Aniqlovchi"], "Tushum kelishigida."),
    C(2, "«Ukamga kitob berdi» da «ukamga» qaysi bo'lak?", "Vositali to'ldiruvchi", ["Vositasiz to'ldiruvchi", "Hol", "Ega"], "Boshqa kelishikda."),
    C(3, "«Bahorda ariqlarda suv shildirab oqdi» gapida «bahorda» qaysi hol?", "Payt holi", ["O'rin holi", "Ravish holi", "Sabab holi"], "Qachon?"),
    O(3, "«U tez yuguradi» gapida «tez» qaysi gap bo'lagi?", ["hol", "ravish holi"], "Qanday? — hol."),
    O(3, "«Daraxtda qush sayradi» gapida «daraxtda» qaysi turdagi hol?", ["o'rin holi", "o'rin"], "Qayerda?"),
]

Q["N9.2"] = [
    C(1, "Bir tarkibli gap nima?", "Faqat bitta bosh bo'lagi (ega yoki kesim) bo'lgan gap", ["Ikkita ega", "Faqat bitta so'z", "Kesimsiz gap"], "Ega yoki kesim."),
    C(1, "Atov gap nima?", "Faqat ega bilan ifodalanib, predmetning borligini bildiruvchi gap", ["Kesim bilan tuzilgan gap", "Savol gap", "Hol bilan"], "Masalan: «Tun.»"),
    C(2, "Qaysi gap atov gap?", "Kuz.", ["Kuz keldi.", "Kuzda yomg'ir yog'di.", "Kuz yaxshi fasl."], "Faqat ega."),
    C(2, "Shaxsi aniq gap qaysi?", "Kitob o'qiyman.", ["Eshik qoqishdi.", "Kitob o'qiladi.", "Kuz."], "Kesim shaxs ko'rsatkichi bilan egani aniqlaydi."),
    C(2, "Shaxsi noma'lum gap qaysi?", "Eshik qoqishdi.", ["Kitob o'qiyman.", "Kuz.", "U keldi."], "Ish bajaruvchi noma'lum."),
    C(2, "Shaxsi umumlashgan gapni toping.", "Mehnat qilsang, rohat ko'rasan.", ["Eshik qoqishdi.", "Kuz.", "Men keldim."], "Kesim II shaxsda, ammo fikr hamma uchun umumiy."),
    C(3, "«Havo isidi» qanday gap?", "Ikki tarkibli (ega: havo)", ["Atov gap", "Shaxssiz gap", "Shaxsi noma'lum"], "Egasi bor."),
    O(3, "«Bahor.» gapi qaysi turdagi bir tarkibli gap? (atov yoki shaxsi aniq)", ["atov", "atov gap"], "Faqat ega."),
    O(3, "«Eshikni ochishdi» gapi shaxsi aniq gapmi yoki noma'lum gapmi? (bir so'z)", ["noma'lum", "noma`lum", "noma’lum"], "Ochuvchi kim ekani noma'lum."),
]

Q["N9.3"] = [
    C(1, "Murojaat bildiruvchi so'z (birikma) gapda qaysi bo'lak?", "Undalma", ["Kiritma", "Ega", "Hol"], "Kimga murojaat."),
    C(1, "Gapda so'zlovchining munosabatini bildiruvchi so'z (aytganday, shubhasiz)?", "Kiritma", ["Undalma", "Ega", "To'ldiruvchi"], "Kiritma so'z."),
    C(2, "Undalmadan keyin qaysi tinish belgisi qo'yiladi (gap o'rtasida)?", "Vergul", ["Nuqta", "Ikki nuqta", "Tire"], "«Ali, bu yoqqa kel!»"),
    C(2, "Qaysi gapda undalma bor?", "Do'stlar, birga ishlaymiz.", ["Ular keldi.", "Kitob stolda turibdi.", "Bugun havo ochiq."], "Murojaat."),
    C(2, "Qaysi gapda kiritma so'z bor?", "Aytganday, u ham keladi.", ["Ali keldi.", "Kitobni oldim.", "Bahor keldi."], "Aytganday — kiritma."),
    C(2, "Kiritma so'z gapda qanday ajratiladi?", "Vergul bilan", ["Nuqta bilan", "Hech qanday", "Ikki nuqta bilan"], "Odatda vergul."),
    C(3, "Ajratilgan bo'lakli gap qaysi?", "Ali, mening do'stim, bugun keldi.", ["Ali keldi.", "Ali va Vali keldi.", "Bahor keldi."], "Izohlovchi ajratilgan."),
    O(3, "«Do'stim, yordam bering!» gapida «do'stim» qaysi sintaktik birlik?", ["undalma"], "Murojaat."),
    O(3, "«Ehtimol, u kelar» gapida «ehtimol» qaysi birlik?", ["kiritma", "kiritma so'z"], "Gumon bildiradi."),
]

Q["N9.4"] = [
    C(1, "Teng bog'langan qo'shma gap qismlari...", "teng huquqli, bog'lovchi yoki ohang bilan bog'lanadi", ["bosh va ergash", "bir-biriga tobe", "faqat bog'lovchisiz"], "Teng aloqa."),
    C(2, "Zidlov bog'lovchili qo'shma gapni toping.", "U keldi, lekin men ketdim.", ["U keldi va men ketdim.", "U keldi yoki men ketdim.", "U keldi, men ketdim."], "Lekin."),
    C(2, "Ayiruv bog'lovchili qo'shma gapni toping.", "Yo ishla, yo dam ol.", ["Ishladi, lekin charchadi.", "Ishladi va dam oldi.", "Ishladi, chunki kerak edi."], "Yo...yo."),
    C(2, "Biriktiruv bog'lovchili qo'shma gap?", "Quyosh chiqdi va tong otdi.", ["Quyosh chiqdi, ammo sovuq edi.", "Yo quyosh, yo yomg'ir.", "Quyosh chiqdi, chunki tong otdi."], "Va, hamda."),
    C(3, "Peshma-peshlik ma'nosi qaysi gapda?", "Avval yomg'ir yog'di, so'ng quyosh chiqdi.", ["U kelmadi, lekin xat yubordi.", "Yo kel, yo ketma.", "U kelsa, boraman."], "Ketma-ket voqea."),
    C(3, "«Garchi...ammo» qaysi turga kiradi?", "Ergash gapli (to'siqsiz)", ["Teng bog'langan", "Bog'lovchisiz", "Sodda gap"], "Garchi — ergashtiruvchi."),
    C(2, "Teng bog'langan qo'shma gap qismlari orasida odatda qaysi belgi qo'yiladi?", "Vergul", ["Ikki nuqta", "Tire doim", "Qavs"], "Vergul."),
    O(3, "«U keldi, ammo men ketgan edim» gapi qaysi ma'noviy turga kiradi (biriktiruv, zidlov, ayiruv)?", ["zidlov"], "Ammo — zidlov."),
    O(3, "«Yo uyda o'tir, yo kutubxonaga bor» gapidagi bog'lovchi qaysi? (bir so'z)", ["yo"], "Yo...yo — ayiruv."),
]

Q["N9.5"] = [
    C(1, "Ergash gapli qo'shma gap qismlari?", "Bosh gap va ergash gap", ["Faqat bosh gap", "Ikki teng gap", "Faqat ergash gap"], "Tobe bog'lanish."),
    C(1, "Ergash gapni bosh gapga bog'lovchi vositalar?", "-ki, chunki, agar, garchi, qachon...", ["va, hamda", "lekin, ammo", "yo, yoki"], "Ergashtiruvchi bog'lovchilar."),
    C(2, "«Agar vaqtim bo'lsa, kelaman» da ergash gap turi?", "Shart ergash gap", ["Payt ergash gap", "Sabab ergash gap", "Maqsad ergash gap"], "Agar — shart."),
    C(2, "«Men kechikdim, chunki yomg'ir yog'di» da ergash gap turi?", "Sabab ergash gap", ["Payt ergash gap", "Shart ergash gap", "O'rin ergash gap"], "Chunki."),
    C(2, "«U shunday keldiki, hamma xursand bo'ldi» ergash gap turi?", "Natija ergash gap", ["Sabab ergash gap", "Shart ergash gap", "Payt ergash gap"], "-ki — natija."),
    C(2, "«Dars boshlanganda, hamma o'tirdi» da ergash gap turi?", "Payt ergash gap", ["Shart", "Sabab", "O'rin"], "-ganda — payt."),
    C(3, "«Garchi charchagan bo'lsa-da, ishlashda davom etdi» da ergash gap turi?", "To'siqsiz ergash gap", ["Shart", "Sabab", "Maqsad"], "Garchi."),
    O(3, "«Kim ishlasa, shu yeydi» da ergash gap qismi turi? (ega ergash gap)", ["ega", "ega ergash gap"], "Kim? — egani izohlaydi."),
    O(3, "«Sen ko'rgan odamni men ham ko'rdim» — ergash qismi qaysi bo'lak vazifasida? (aniqlovchi)", ["aniqlovchi", "aniqlovchi ergash gap"], "Qanday odamni?") if False else O(3, "«Men bilamanki, u kelmaydi» gapida ergash qism qaysi ergash gap turiga kiradi? (bir so'z)", ["to'ldiruvchi", "to'ldiruvchi ergash gap"], "Nimani bilaman? — to'ldiruvchi."),
]

Q["N9.6"] = [
    C(1, "Bog'lovchisiz qo'shma gap qismlari qaysi vosita bilan bog'lanadi?", "Ohang va tinish belgilari", ["Bog'lovchi", "Ko'makchi", "Yuklama"], "Ohang."),
    C(2, "Sabab-natija munosabatidagi bog'lovchisiz gapda qaysi belgi qo'yiladi (tushuntirish)?", "Ikki nuqta", ["Vergul doim", "Nuqta-vergul", "Qavs"], "Tushuntirish — ikki nuqta."),
    C(2, "Qaysi gapda tinish to'g'ri qo'yilgan?", "Kech qoldim: poyezd ketib bo'lgan edi.", ["Kech qoldim; poyezd ketib bo'lgan edi.", "Kech qoldim – poyezd ketib bo'lgan edi,", "Kech qoldim. poyezd ketib bo'lgan edi."], "Sabab tushuntirilmoqda."),
    C(2, "Zidlash ma'nosidagi bog'lovchisiz gapda qaysi belgi qo'yiladi?", "Tire", ["Ikki nuqta", "Qavs", "Ko'p nuqta"], "Gap qismlari qarama-qarshi."),
    C(2, "Shart-natija ma'nosida qaysi belgi qo'yiladi?", "Tire (yoki vergul)", ["Ikki nuqta", "Qavs", "Qo'shtirnoq"], "Kelsang — boraman."),
    C(3, "Payt ma'nosidagi bog'lovchisiz gapni toping.", "Quyosh botdi, qorong'i tushdi.", ["U keldi, lekin ketdi.", "Agar yog'sa, kelmayman.", "U keldi va ketdi."], "Voqealar ketma-ket."),
    C(3, "Qo'shma gap qismlari orasidagi vergulning vazifasi?", "Qismlarni ajratish", ["Gapni tugatish", "Savol berish", "Ko'chirma ko'rsatish"], "Tinish belgisi."),
    O(3, "«Men dedim: kel. U keldi» — ikki nuqta qaysi ma'nodagi gapda qo'yilgan? (tushuntirish yoki sabab)", ["tushuntirish"], "Ikkinchi qism birinchisini tushuntiradi.") if False else O(3, "«Yaxshi o'qisang — yutasan» gapida tire qaysi munosabatda qo'yilgan? (shart yoki zidlash: bir so'z)", ["shart"], "Shart-natija."),
    O(3, "«U kechikdi: yo'lda tirbandlik bor edi.» gapdagi ikki nuqta qaysi ma'noni bildiradi? (sabab yoki payt)", ["sabab"], "Sabab tushuntiriladi."),
]

Q["N9.7"] = [
    C(1, "Ko'chirma gap nima?", "Boshqa kishining so'zini aynan keltirish", ["O'z fikrini aytish", "Savol gap", "Hol"], "Aynan keltiriladi."),
    C(1, "O'zlashtirma gap nima?", "Boshqa kishining so'zini mazmunan, ko'chirma belgilarisiz keltirish", ["Aynan keltirish", "Tushuntirish gap", "Undalma"], "Mazmunan."),
    C(2, "Nutq uslublari qaysi?", "So'zlashuv, rasmiy-idoraviy, ilmiy, publitsistik, badiiy", ["Faqat badiiy", "Og'zaki va yozma", "Qisqa va uzun"], "Beshta uslub."),
    C(2, "Ariza, buyruq, bayonnoma qaysi uslubga mansub?", "Rasmiy-idoraviy", ["Ilmiy", "Badiiy", "Publitsistik"], "Ish yuritish."),
    C(2, "Qaysi uslub gazeta-jurnal maqolalarida uchraydi?", "Publitsistik", ["Badiiy", "Rasmiy", "So'zlashuv"], "Ommaviy axborot."),
    C(2, "Ko'chirma gapda muallif so'zi oldin kelsa, qaysi belgi qo'yiladi?", "Ikki nuqta va tire yoki qo'shtirnoq", ["Faqat nuqta", "Qavs", "Hech nima"], "Ali dedi: — Kel."),
    C(3, "Qaysi gap ko'chirma gap?", "Ona: «Barvaqt qayt», — dedi.", ["Ona barvaqt qaytishni aytdi.", "Ona barvaqt qaytsin.", "Ona dedi."], "Aynan keltirilgan."),
    O(3, "«Ali menga: «Men borganman», — dedi» — bu qanday gap turi? (ko'chirma yoki o'zlashtirma)", ["ko'chirma", "ko'chirma gap"], "Aynan keltirilgan."),
    O(3, "Ilmiy maqolalar qaysi uslubda yoziladi? (bir so'z: ilmiy)", ["ilmiy"], "Ilmiy uslub."),
]

Q["N9.8"] = [
    C(1, "«Padarkush» dramasining muallifi?", "Mahmudxo'ja Behbudiy", ["Abdulla Qodiriy", "Cho'lpon", "Hamza Hakimzoda"], "Behbudiy."),
    C(1, "«Padarkush» qaysi yilda yozilgan?", "1911-yil", ["1920-yil", "1905-yil", "1930-yil"], "1911."),
    C(2, "«Padarkush» o'zbek adabiyotida nimaning birinchi namunasi?", "Dramaturgiya (birinchi o'zbek dramasi)", ["Romani", "Dostoni", "Qissasi"], "Milliy drama."),
    C(2, "«Padarkush» dagi asosiy g'oya?", "Ilmsizlik va jaholatning fojiali oqibati", ["Tijorat foydasi", "Qahramonlik", "Sevgi"], "Ma'rifat chaqirig'i."),
    C(2, "Dramada ota o'ldirilishiga sabab?", "Farzandning ilmsizligi va tarbiyasizligi", ["Urush", "Mol-mulk nizosi faqat", "Tabiiy ofat"], "Toshmurod fojiasi."),
    C(3, "Behbudiy chiqargan jadid gazetasi/jurnali?", "«Oyna» jurnali", ["«Turkiston» faqat", "«Sharq yulduzi»", "«Guliston»"], "1913–1915."),
    O(3, "«Padarkush» dramasining bosh qahramoni (o'g'il) kim? (ismini yozing)", ["toshmurod"], "Toshmurod."),
    O(3, "Behbudiy qaysi harakat vakili (ma'rifatparvar tarmoq nomi)?", ["jadid", "jadidchilik", "jadidlar"], "Jadidchilik."),
    M(2, [("Padarkush", "Behbudiy"), ("O'tkan kunlar", "Abdulla Qodiriy"), ("Kecha va kunduz", "Cho'lpon")], "Asar va muallif."),
]

Q["N9.9"] = [
    C(1, "«O'tkan kunlar» romani muallifi?", "Abdulla Qodiriy", ["Cho'lpon", "Abdulla Qahhor", "Oybek"], "Qodiriy."),
    C(1, "«O'tkan kunlar» o'zbek adabiyotida...", "birinchi o'zbek romani", ["birinchi dostoni", "birinchi dramasi", "birinchi hikoyasi"], "1922 yilda yozilgan."),
    C(1, "«O'tkan kunlar» romanining bosh qahramoni?", "Otabek", ["Homid", "Rahmat", "Hasanali"], "Otabek."),
    C(2, "Otabekning sevgilisi (birinchi rafiqasi)?", "Kumush", ["Zaynab", "Oysha", "Gulnor"], "Kumush."),
    C(2, "Otabekning ikkinchi rafiqasi?", "Zaynab", ["Kumush", "Oysha", "Zebi"], "Zaynab."),
    C(2, "Otabekning otasi?", "Yusufbek hoji", ["Mirzakarim qutidor", "Normuhammad qushbegi", "Azizbek"], "Yusufbek hoji."),
    C(2, "Kumushning otasi?", "Mirzakarim qutidor", ["Yusufbek hoji", "Homid", "Rahmat"], "Mirzakarim qutidor."),
    C(3, "Romandagi asosiy raqib, Kumushga oshiq bo'lgan va fitna uyushtirgan shaxs?", "Homid", ["Rahmat", "Azizbek", "Hasanali"], "Homid."),
    C(3, "Kumushning fojiali o'limiga sabab?", "Zaharlanish (fitna oqibati)", ["Kasallik", "Urush", "Yong'in"], "Zahar."),
    O(3, "«O'tkan kunlar» romanining muallifi familiyasini yozing (Abdulla ...)", ["qodiriy"], "Abdulla Qodiriy."),
    O(3, "Romandagi Toshkent hokimi (Azizbek) kim hukmdor edi? Savol: romanda voqealar qaysi xonlikda boshlanadi? (Marg'ilon yoki Toshkent: 'Marg'ilon')", ["marg'ilon", "margilon", "marg`ilon"], "Marg'ilon.") if False else O(3, "Otabek Toshkentdan qaysi shaharga uylanish uchun boradi? (shahar nomi)", ["marg'ilon", "margilon", "marg`ilon"], "Marg'ilon."),
]

Q["N9.10"] = [
    C(1, "«Kecha va kunduz» romani muallifi?", "Cho'lpon", ["Abdulla Qodiriy", "Oybek", "Fitrat"], "Abdulhamid Cho'lpon."),
    C(1, "Cho'lponning asl ismi?", "Abdulhamid Sulaymon o'g'li", ["Abdulla Qodiriy", "Abdurauf Fitrat", "Hamza"], "Cho'lpon — taxallus."),
    C(2, "«Kecha va kunduz» romani qachon nashr etilgan?", "1936-yil", ["1922-yil", "1950-yil", "1911-yil"], "1936."),
    C(2, "«Kecha va kunduz» dagi bosh qahramon qiz?", "Zebi", ["Kumush", "Barchin", "Oysha"], "Zebi."),
    C(2, "Cho'lponning she'rlar to'plami?", "«Uyg'onish»", ["«Hayrat ul-abror»", "«Boburnoma»", "«Mirzo Ulug'bek»"], "1922."),
    C(3, "Cho'lponning mashhur she'ri?", "«Go'zal»", ["«Anor»", "«Ruhlar isyoni»", "«Jannatga yo'l»"], "Go'zal."),
    C(3, "Romandagi Akbarali mingboshi qanday obraz?", "Zolim, ochko'z amaldor", ["Adolatli hokim", "Olim", "Savdogar do'st"], "Salbiy obraz."),
    O(3, "Cho'lponning mashhur tarjima/she'riy to'plami nomi emas: «Kecha va kunduz» qanday turdagi asar? (roman, doston yoki drama: bir so'z)", ["roman"], "Roman.") if False else O(3, "«Kecha va kunduz» qanday asar turi? (bir so'z)", ["roman"], "Roman."),
    O(3, "«Kecha va kunduz» romanidagi Miryoqub qaysi qizning eri (ismini yozing)?", ["zebi"], "Zebi."),
]

Q["N10.1"] = [
    C(1, "Matn nima?", "Mazmunan bog'langan gaplar yig'indisi", ["Bitta gap", "Bitta so'z", "Faqat she'r"], "Butunlik."),
    C(2, "Matnda gaplarni bog'lovchi vositalar?", "Leksik, morfologik va sintaktik vositalar", ["Faqat tinish belgilari", "Faqat bog'lovchi", "Faqat sarlavha"], "Aloqa."),
    C(2, "Takror, sinonim, olmosh — qaysi bog'lanish vositasi?", "Leksik va morfologik", ["Faqat sintaktik", "Faqat fonetik", "Faqat grafik"], "Zanjirli aloqa."),
    C(2, "Matnning bosh fikrini ifodalovchi qismi?", "Mikromavzu emas — asosiy g'oya (mavzu)", ["Imlo xatolari", "Tinish belgilari", "Sarlavha emas"], "G'oya.") if False else C(2, "Matnning asosiy mazmunini qisqa ifodalovchi nomi?", "Sarlavha", ["Imlo", "Bo'g'in", "Urg'u"], "Sarlavha."),
    C(3, "Zanjirli bog'lanishda keyingi gap oldingi gapning qaysi qismiga tayanadi?", "Oxiridagi so'zga (yangi axborotga)", ["Faqat birinchi so'zga", "Hech qaysiga", "Faqat sarlavhaga"], "Ketma-ketlik."),
    C(3, "Parallel bog'lanishda gaplar...", "bir xil qurilishda keladi", ["bir-biriga bog'liq emas", "faqat savol bo'ladi", "faqat bog'lovchisiz"], "Parallelizm."),
    C(2, "Matn bo'laklari qanday ataladi?", "Abzas (xatboshi)", ["Rukn", "Misra", "Band? faqat she'rda"], "Xatboshi.") if False else C(2, "Matn bo'laklari yozuvda qanday ataladi?", "Xatboshi (abzas)", ["Rukn", "Misra", "Turoq"], "Qizil satr."),
    O(3, "Matndagi asosiy g'oyani ifodalovchi umumiy nom (bir so'z: mavzu yoki g'oya — «g'oya»)", ["g'oya", "goya", "g`oya"], "G'oya.") if False else O(3, "Matnning boshlanishida joylashgan, mazmunini bildiruvchi nomni yozing (bir so'z)", ["sarlavha"], "Sarlavha."),
    O(3, "Mazmunan bog'langan gaplar yig'indisi nima deyiladi? (bir so'z)", ["matn"], "Matn."),
]

Q["N10.2"] = [
    C(1, "Aruz nima?", "She'riy o'lchov tizimi (bo'g'inlarning cho'ziq-qisqa tartibiga asoslangan)", ["Nasr turi", "Janr", "Qofiya turi"], "Aruz — vazn."),
    C(1, "Aruzda bo'g'in turlari?", "qisqa, cho'ziq, o'ta cho'ziq", ["ochiq, yopiq", "unli, undosh", "bosh, oxir"], "Uch turi."),
    C(2, "Aruz bahrlaridan biri?", "Hazaj", ["Tajnis", "Tazod", "Mubolag'a"], "Hazaj, ramal, rajaz, mutaqorib."),
    C(2, "Hazaj bahrining asosiy rukni?", "mafoiylun", ["foilotun", "fa'ulun", "mustaf'ilun"], "Hazaj — mafoiylun."),
    C(2, "Ramal bahrining asosiy rukni?", "foilotun", ["mafoiylun", "fa'ulun", "mustaf'ilun"], "Ramal."),
    C(2, "Mutaqorib bahrining asosiy rukni?", "fa'ulun", ["foilotun", "mafoiylun", "mustaf'ilun"], "Mutaqorib."),
    C(2, "Rajaz bahrining asosiy rukni?", "mustaf'ilun", ["fa'ulun", "foilotun", "mafoiylun"], "Rajaz."),
    C(3, "She'rni aruz bo'yicha bo'g'inlarga ajratib, vaznini aniqlash?", "Taqti'", ["Tajnis", "Tazod", "Iyhom"], "Taqti'."),
    O(3, "Aruz tizimini ishlab chiqqan olim ismini yozing (Xalil ibn ...)", ["ahmad", "xalil ibn ahmad"], "Xalil ibn Ahmad.") if False else O(3, "«Mafoiylun» qaysi bahrning asosiy rukni? (bahr nomi)", ["hazaj"], "Hazaj."),
    O(3, "«Foilotun» qaysi bahrning asosiy rukni? (bahr nomi)", ["ramal"], "Ramal."),
]

Q["N10.3"] = [
    C(1, "Barmoq vaznida asos nima?", "Bo'g'inlar soni", ["Bo'g'inning cho'ziq-qisqaligi", "Qofiya turi", "Rukn"], "Bo'g'inlar tengligi."),
    C(1, "Barmoq vazni qaysi poeziyaga xos?", "Xalq og'zaki ijodi va yangi o'zbek she'riyati", ["Faqat klassik aruz", "Faqat nasr", "Drama"], "Barmoq."),
    C(2, "Turoq nima?", "Misradagi bo'g'inlar guruhi", ["Qofiya", "Radif", "Bayt"], "Misrada bo'laklar."),
    C(2, "Qofiya nima?", "Misra oxiridagi tovush uyg'unligi", ["Bo'g'in soni", "Ritm", "Takror"], "Uyg'un tovushlar."),
    C(2, "Radif nima?", "Qofiyadan keyin takrorlanuvchi so'z yoki so'zlar", ["Misra boshi", "Bayt", "Rukn"], "Takror."),
    C(2, "Ravy nima?", "Qofiyadagi asosiy takrorlanuvchi undosh", ["Radif", "Bayt", "Misra"], "Ravy."),
    C(3, "7+7 qolipli barmoq misrasida bo'g'inlar soni?", "14", ["7", "11", "10"], "Yetti + yetti."),
    O(3, "She'rdagi ikki qatorli birlik (aruzda) nima deyiladi? (bir so'z: bayt)", ["bayt"], "Ikki misra — bayt.") if False else O(3, "Aruz she'rida ikki misradan iborat birlik nima deyiladi? (bir so'z)", ["bayt"], "Ikki misra — bayt."),
    O(3, "«Qalam, daftar»... Misra oxiridagi uyg'un tovushlar nima deyiladi? (bir so'z)", ["qofiya"], "Qofiya.") if False else O(3, "Misralar oxiridagi uyg'un tovushlar nima deyiladi? (bir so'z)", ["qofiya"], "Qofiya."),
]

Q["N10.4"] = [
    C(1, "Tashbeh nima?", "O'xshatish", ["Ikki ma'nolilik", "Mubolag'a", "Zid qo'yish"], "Tashbeh."),
    C(1, "Istiora nima?", "Ko'chma ma'noda qo'llash (metafora)", ["O'xshatish", "Chegaradan oshirish", "Qarama-qarshilik"], "Metafora."),
    C(2, "Mubolag'a nima?", "Bo'rttirish (giperbola)", ["O'xshatish", "Ikki ma'nolilik", "Zid qo'yish"], "Oshirib tasvirlash."),
    C(2, "Tazod nima?", "Zid qo'yish (antiteza)", ["Bo'rttirish", "Jonlantirish", "O'xshatish"], "Zidlik."),
    C(2, "Tajnis nima?", "Shakldosh so'zlarning o'yini (omonimlar san'ati)", ["Zid so'zlar", "Takror", "O'xshatish"], "Tajnis."),
    C(2, "Iyhom nima?", "So'zning ikki ma'noda ishlatilishi", ["Chegaradan oshirish", "Qarama-qarshi qo'yish", "Rang tasviri"], "Ikki ma'no."),
    C(3, "«Yuzing oydek» — qaysi san'at?", "Tashbeh", ["Tazod", "Mubolag'a", "Tajnis"], "O'xshatish."),
    C(3, "«Ming yil kutdim seni» da qaysi san'at?", "Mubolag'a", ["Tazod", "Tashbeh", "Iyhom"], "Bo'rttirish."),
    O(3, "«Kunduz — oq, tun — qora» qaysi san'atga misol? (bir so'z)", ["tazod"], "Zid qo'yish."),
    M(2, [("Tashbeh", "o'xshatish"), ("Mubolag'a", "bo'rttirish"), ("Tazod", "zid qo'yish")], "Badiiy san'atlar."),
]

Q["N10.5"] = [
    C(1, "«Sinchalak» qissasi muallifi?", "Abdulla Qahhor", ["Said Ahmad", "Oybek", "Cho'lpon"], "Qahhor."),
    C(1, "Quyidagilardan qaysi biri Abdulla Qahhorning hikoyasi?", "«Anor»", ["«Alpomish»", "«Ruhlar isyoni»", "«Padarkush»"], "Anor."),
    C(2, "«Sinchalak» dagi bosh qahramon qiz?", "Saida", ["Kumush", "Zebi", "Barchin"], "Saida."),
    C(2, "Qahhorning boshqa hikoyalari?", "«Bemor», «O'g'ri»", ["«Yulduzli tunlar», «Boburnoma»", "«Alpomish», «Go'ro'g'li»", "«Padarkush», «Layli»"], "Hikoyalar."),
    C(2, "Qahhorning romani?", "«Qo'shchinor chiroqlari»", ["«Yulduzli tunlar»", "«Ufq»", "«O'tkan kunlar»"], "1951."),
    C(3, "Qahhor asarlariga xos uslub?", "Ixcham, hajviy va psixologik tasvir", ["Faqat qasidalar", "Ko'p tavsif", "Aruz she'riyati"], "Mohir hikoyanavis."),
    C(3, "«O'tmishdan ertaklar» kimning asari?", "Abdulla Qahhor", ["Oybek", "Said Ahmad", "Odil Yoqubov"], "Qahhor."),
    O(3, "«Sinchalak» da qiz ismini yozing (bosh qahramon).", ["saida"], "Saida."),
    O(3, "«Anor» hikoyasining muallifi familiyasini yozing (Abdulla ...)", ["qahhor"], "Qahhor."),
]

Q["N10.6"] = [
    C(1, "«Mirzo Ulug'bek» fojiasi muallifi?", "Maqsud Shayxzoda", ["Odil Yoqubov", "Cho'lpon", "Oybek"], "Shayxzoda."),
    C(1, "Mirzo Ulug'bek kim?", "Temuriy hukmdor va buyuk astronom", ["Faqat jangchi", "Shoir faqat", "Savdogar"], "Samarqand rasadxonasi."),
    C(2, "Fojiada Ulug'bekka xiyonat qilgan o'g'li?", "Abdullatif", ["Abdurazzoq", "Boysunqur", "Umarshayx"], "Abdullatif."),
    C(2, "Ulug'bekning hamkori — olim?", "Ali Qushchi", ["Qozizoda Rumiy", "Abdullatif", "Navoiy"], "Ali Qushchi."),
    C(2, "Asardagi asosiy mojaro?", "Ilm-fan va jaholat o'rtasida", ["Sevgi va nafrat", "Urush-sulh", "Boylik-qashshoqlik"], "Olim fojiasi."),
    C(3, "Fojianing janri qaysi tur?", "Dramatik asar", ["Epik doston", "Lirik she'r", "Nasriy qissa"], "Drama."),
    O(3, "Ulug'bekning rasadxonasi qaysi shaharda? (shahar nomi)", ["samarqand"], "Samarqand."),
    O(3, "Shayxzodaning boshqa mashhur dramasi: «Jaloliddin ...» (Manguberdi) — familiyasini yozing: Maqsud ...", ["shayxzoda"], "Shayxzoda.") if False else O(3, "«Mirzo Ulug'bek» fojiasining muallifi familiyasini yozing (Maqsud ...).", ["shayxzoda"], "Shayxzoda."),
    O(3, "Ulug'bekning xiyonat qilgan o'g'li ismi?", ["abdullatif"], "Abdullatif."),
]

Q["N10.7"] = [
    C(1, "«Ufq» trilogiyasi muallifi?", "Said Ahmad", ["Odil Yoqubov", "Pirimqul Qodirov", "Abdulla Qahhor"], "Said Ahmad."),
    C(2, "Said Ahmadning urush mavzusidagi asari?", "«Qirq besh kun»", ["«Sinchalak»", "«Ruhlar isyoni»", "«Padarkush»"], "Qirq besh kun."),
    C(2, "«Ufq» da qahramonlar qaysi tarixiy davrni aks ettiradi?", "Ikkinchi jahon urushi davri", ["Temuriylar davri", "XIX asr xonliklar", "Mustaqillik yillari"], "Front va orqa."),
    C(3, "«Ufq» trilogiyasi qismlaridan biri?", "«Hijron kunlari»", ["«Yulduzli tunlar»", "«Diyonat»", "«Kecha va kunduz»"], "Hijron kunlari."),
    C(3, "Said Ahmadning mashhur komediyasi?", "«Kelinlar qo'zg'aloni»", ["«Mirzo Ulug'bek»", "«Padarkush»", "«Alpomish»"], "Kelinlar qo'zg'aloni."),
    C(3, "Said Ahmad asarlari uslubi?", "Hayotiy, xalqona, hajviy ohangli", ["Faqat tarixiy", "Faqat falsafiy", "Faqat fantastik"], "Xalqona."),
    O(3, "Said Ahmad trilogiyasi nomini yozing: «...» (bir so'z: Ufq)", ["ufq"], "Ufq."),
    O(3, "«Qirq besh kun» qaysi urush haqida? (bir so'z yoki ibora: ikkinchi jahon urushi — «jahon»)", ["jahon", "ikkinchi jahon", "ikkinchi jahon urushi"], "Ikkinchi jahon urushi."),
    O(3, "«Ufq» muallifining familiyasini yozing: Said ...", ["ahmad"], "Said Ahmad."),
]

Q["N10.8"] = [
    C(1, "«Ulug'bek xazinasi» romani muallifi?", "Odil Yoqubov", ["Said Ahmad", "Pirimqul Qodirov", "Oybek"], "Odil Yoqubov."),
    C(2, "Romanda markaziy obraz?", "Mirzo Ulug'bek", ["Alisher Navoiy", "Amir Temur", "Bobur"], "Ulug'bek."),
    C(2, "Odil Yoqubovning boshqa romani?", "«Diyonat»", ["«Yulduzli tunlar»", "«Ufq»", "«Sinchalak»"], "Diyonat."),
    C(2, "«Ulug'bek xazinasi» da xazina nima?", "Ilm, kutubxona va bilimlar xazinasi", ["Oltin-kumush", "Qurol", "Yer"], "Ma'naviy xazina."),
    C(3, "Romandagi asosiy g'oya?", "Ilm va ziyoning qadri; olim fojiasi", ["Savdo foydasi", "Urush qudrati", "Sayohat"], "Ma'naviyat."),
    C(3, "Roman janri?", "Tarixiy roman", ["Hajviy hikoya", "Lirik she'r", "Doston"], "Tarixiy."),
    O(3, "«Ulug'bek xazinasi» muallifi familiyasini yozing: Odil ...", ["yoqubov"], "Yoqubov."),
    O(3, "Romanda tasvirlangan buyuk olim-shoh ismini yozing (Mirzo ...)", ["ulug'bek", "ulugbek", "ulug`bek"], "Ulug'bek."),
    O(3, "Odil Yoqubovning mashhur romanlaridan birini yozing: «Diyonat» yoki «Muqaddas». (ikkalasidan biri)", ["diyonat", "muqaddas"], "Yoqubov romanlari.") if False else O(3, "Odil Yoqubovning «Diyonat» romani qanday tur? (roman yoki doston)", ["roman"], "Roman."),
]

Q["N10.9"] = [
    C(1, "«Yulduzli tunlar» romani muallifi?", "Pirimqul Qodirov", ["Odil Yoqubov", "Said Ahmad", "Abdulla Qahhor"], "Pirimqul Qodirov."),
    C(1, "«Yulduzli tunlar» romanining bosh qahramoni?", "Zahiriddin Muhammad Bobur", ["Amir Temur", "Alisher Navoiy", "Mirzo Ulug'bek"], "Bobur."),
    C(2, "Boburning o'g'li (romanda ko'rinadigan)?", "Humoyun", ["Akbar", "Abdullatif", "Otabek"], "Humoyun."),
    C(2, "Bobur opasi (romanda)?", "Xonzoda begim", ["Zebi", "Kumush", "Barchin"], "Xonzoda."),
    C(3, "Romandagi muhim tarixiy mavzu?", "Temuriylar saltanatining inqirozi va Bobur hayoti", ["Amir Temur yurishlari", "Mustaqillik davri", "Sovet davri"], "Tarixiy."),
    C(3, "Pirimqul Qodirovning boshqa asari?", "«Humoyun va Akbar»", ["«Ufq»", "«Diyonat»", "«Sinchalak»"], "Humoyun va Akbar."),
    O(3, "«Yulduzli tunlar» qahramoni ismini yozing: Zahiriddin Muhammad ...", ["bobur"], "Bobur."),
    O(3, "Pirimqul Qodirov familiyasi bilan tugaydigan ism: Pirimqul ...", ["qodirov"], "Qodirov."),
    O(3, "«Yulduzli tunlar» janri? (bir so'z)", ["roman", "tarixiy roman"], "Tarixiy roman."),
]

Q["N10.10"] = [
    C(1, "«Ruhlar isyoni» dostoni muallifi?", "Erkin Vohidov", ["Abdulla Oripov", "Cho'lpon", "Oybek"], "Erkin Vohidov."),
    C(1, "«Jannatga yo'l» dostoni muallifi?", "Abdulla Oripov", ["Erkin Vohidov", "Muhammad Yusuf", "Usmon Nosir"], "Oripov."),
    C(2, "O'zbekiston Respublikasi Davlat madhiyasi so'zlari muallifi?", "Abdulla Oripov", ["Erkin Vohidov", "Cho'lpon", "Oybek"], "Oripov."),
    C(2, "«Ruhlar isyoni» qaysi turdagi asar?", "Falsafiy doston", ["Roman", "Drama", "Hikoya"], "Falsafiy doston."),
    C(2, "Abdulla Oripovning she'riy to'plami?", "«Yurak»", ["«Uyg'onish»", "«Nido»", "«Qo'shchinor chiroqlari»"], "«Yurak» — 1980-yillar boshi? To'plam nomi.") if False else C(2, "Abdulla Oripovning Amir Temur haqidagi dostoni?", "«Sohibqiron»", ["«Ruhlar isyoni»", "«Palatkada yozilgan doston»", "«Jannatga yo'l»"], "Sohibqiron."),
    C(3, "Erkin Vohidovning she'riy to'plami?", "«Nido»", ["«Sohibqiron»", "«Jannatga yo'l»", "«Padarkush»"], "Nido."),
    C(3, "«Ruhlar isyoni» dagi bosh g'oya?", "Insonning ozodlikka intilishi va ma'naviy erk", ["Faqat sevgi", "Qahramonlik", "Tabiat tasviri"], "Falsafiy."),
    O(3, "«Ruhlar isyoni» muallifi familiyasini yozing: Erkin ...", ["vohidov"], "Vohidov."),
    O(3, "«Jannatga yo'l» muallifi familiyasini yozing: Abdulla ...", ["oripov"], "Oripov."),
]

Q["N10.11"] = [
    C(1, "«Bu dunyoda o'lib bo'lmaydi» romani muallifi?", "Tog'ay Murod", ["Said Ahmad", "Odil Yoqubov", "Oybek"], "Tog'ay Murod."),
    C(2, "«Bu dunyoda o'lib bo'lmaydi» romanining bosh qahramoni?", "Botir dehqon", ["Otabek", "Bobur", "Saida"], "Botir."),
    C(2, "Tog'ay Murodning boshqa romani?", "«Otamdan qolgan dalalar»", ["«Ufq»", "«Diyonat»", "«Yulduzli tunlar»"], "Otamdan qolgan dalalar."),
    C(2, "«Yulduzlar mangu yonadi» qanday asar?", "Qissa/roman, polvonlar hayoti haqida", ["Doston", "Drama", "She'riy to'plam"], "Kurash va milliy g'urur."),
    C(3, "«Bu dunyoda o'lib bo'lmaydi» da tasvir?", "Tuzum o'zgarishi, xalq hayoti va tarixiy burilish", ["Kosmik sayohat", "Faqat sevgi", "Tabiat"], "Ijtimoiy-tarixiy."),
    C(3, "Tog'ay Murod asarlari uslubi?", "Xalqona til, ravon hikoya, hayotiy tasvir", ["Faqat aruz", "Qofiyali nasr", "Telegram uslubi"], "Xalqona."),
    O(3, "«Bu dunyoda o'lib bo'lmaydi» muallifi familiyasini yozing: Tog'ay ...", ["murod"], "Murod."),
    O(3, "Romandagi bosh qahramon kasbi: dehqon — yozing: (bir so'z)", ["dehqon"], "Botir dehqon.") if False else O(3, "«Botir dehqon» qaysi asarning qahramoni? (asardagi roman muallifi: familiya Murod; asar nomining birinchi so'zi: «Bu»)", ["bu"], "«Bu dunyoda...»") if False else O(3, "«Bu dunyoda o'lib bo'lmaydi» qanday turdagi asar? (roman yoki doston: bir so'z)", ["roman"], "Roman."),
    O(3, "Tog'ay Murodning «Otamdan qolgan dalalar» qanday asar turi? (roman, qissa)", ["roman", "qissa"], "Roman/qissa.") if False else O(3, "«Yulduzlar mangu yonadi» asarida polvonlarning kurashi nima uchun tasvirlangan? Qanday xususiyat? (bir so'z: g'urur)", ["g'urur", "gurur", "g`urur"], "Milliy g'urur.") if False else O(3, "«Otamdan qolgan dalalar» muallifi familiyasini yozing: Tog'ay ...", ["murod"], "Murod."),
]

Q["N10.12"] = [
    C(1, "Adabiy turlar?", "Epos, lirika, dramatik", ["Faqat nazm", "Faqat nasr", "She'r va hikoya"], "Uch tur."),
    C(1, "Lirik tur nima bilan xarakterlanadi?", "Shoirning kechinma va tuyg'ulari", ["Voqea hikoyasi", "Sahnaviy dialog", "Tarixiy hujjat"], "Lirika."),
    C(1, "Dramatik asar xususiyati?", "Sahnada ijro uchun yozilgan, dialoglarga asoslangan", ["Faqat tabiat tasviri", "Faqat monolog", "Qofiyasiz"], "Drama."),
    C(2, "Epik janrlarga kiradi?", "Roman, qissa, hikoya, doston", ["G'azal, ruboiy", "Fojia, komediya", "Qasida, marsiya"], "Epos."),
    C(2, "Lirik janrlar?", "G'azal, ruboiy, qasida, tuyuq", ["Roman, qissa", "Drama, fojia", "Hikoya"], "Lirika."),
    C(2, "G'azal necha baytdan iborat bo'lishi mumkin?", "Odatda 5–12 bayt", ["Faqat 1 bayt", "100 bayt", "Faqat 2 bayt"], "G'azal."),
    C(2, "Ruboiy necha misradan iborat?", "4 misra", ["2 misra", "6 misra", "8 misra"], "To'rtlik."),
    C(3, "Obraz nima?", "Badiiy asardagi hayot tasviri/qahramon", ["Imlo qoidasi", "Gap bo'lagi", "So'z turkumi"], "Badiiy obraz."),
    C(3, "Asardagi voqealar rivoji tartibida: ekspozitsiya, tugun, ...?", "Avj, yechim", ["Nuqta, vergul", "Sarlavha, nom", "Bayt, misra"], "Syujet tarkibi."),
    O(3, "Asarning bosh g'oyasi, ya'ni muallif aytmoqchi bo'lgan fikr nima deyiladi? (bir so'z: g'oya)", ["g'oya", "goya", "g`oya"], "G'oya."),
    O(3, "To'rt misrali she'riy janr nomini yozing (ruboiy).", ["ruboiy", "to'rtlik"], "Ruboiy."),
]
