"""v268: ONA TILI VA ADABIYOT, INGLIZ TILI, TARIX — eng kam savolli mavzularga yangi savollar
(DTM / milliy sertifikat uslubi). Faqat darsliklarda aniq qayd etilgan faktlar olingan."""
from __future__ import annotations

from ._dsl import C, O

NATIVE: dict[str, list] = {
    "Bo'g'in va urg'u": [
        C(2, "«Mustaqillik» so'zida nechta bo'g'in bor?", "4 ta", ["3 ta", "5 ta", "6 ta"], "Mus-ta-qil-lik."),
        C(2, "O'zbek tilida bo'g'in soni nimaga bog'liq?", "Unli tovushlar soniga", ["Undosh tovushlar soniga", "Harflar soniga", "Urg'uga"], "Har bo'g'inda bitta unli."),
    ],
    "Imlo: bosh harf, qo'shib, ajratib va chiziqcha bilan yozish": [
        C(2, "Qaysi so'z chiziqcha bilan yoziladi?", "Ota-ona", ["Kungaboqar", "Belbog'", "Toshbaqa"], "Juft so'zlar chiziqcha bilan."),
        C(3, "Qaysi qo'shma so'z qo'shib yoziladi?", "Bilaguzuk", ["Olib keldi", "Kecha-kunduz", "Oq oltin"], "Narsa nomini bildiruvchi qo'shma ot."),
        C(2, "Qaysi birikmada barcha so'zlar bosh harf bilan yoziladi?", "Birlashgan Millatlar Tashkiloti", ["Toshkent davlat universiteti", "O'zbekiston respublikasi", "Mustaqillik kuni"], "Xalqaro tashkilot nomi."),
    ],
    "Kelishik, egalik va son qo'shimchalari": [
        C(2, "«Maktabdan» so'zidagi kelishik?", "Chiqish kelishigi", ["O'rin-payt kelishigi", "Jo'nalish kelishigi", "Tushum kelishigi"], "-dan qo'shimchasi."),
        C(3, "«Kitoblarimizni» so'zidagi qo'shimchalar tartibi?", "Ko'plik + egalik + kelishik", ["Egalik + ko'plik + kelishik", "Kelishik + ko'plik + egalik", "Ko'plik + kelishik + egalik"], "-lar + -imiz + -ni."),
        C(2, "Qaysi so'zda I shaxs birlik egalik qo'shimchasi bor?", "Ukam", ["Ukang", "Ukasi", "Ukamiz"], "-(i)m qo'shimchasi."),
    ],
    "Fe'l turkumi va fe'l nisbatlari": [
        C(3, "«Yozdirdi» fe'lidagi nisbat?", "Orttirma nisbat", ["Majhul nisbat", "O'zlik nisbat", "Birgalik nisbat"], "-dir qo'shimchasi — ish boshqa shaxs orqali bajariladi."),
        C(3, "«Kitob o'qildi» gapidagi fe'l qaysi nisbatda?", "Majhul nisbat", ["Orttirma nisbat", "Aniq nisbat", "Birgalik nisbat"], "Bajaruvchi ko'rsatilmagan, -il qo'shimchasi."),
        C(2, "«Kulishdi» fe'lidagi -ish qo'shimchasi qaysi nisbatni hosil qilgan?", "Birgalik nisbat", ["O'zlik nisbat", "Majhul nisbat", "Orttirma nisbat"], "Ish bir necha kishi tomonidan."),
    ],
    "Alisher Navoiy hayoti va ijodi": [
        C(2, "«Xamsa» nechta dostondan iborat?", "5 ta", ["4 ta", "6 ta", "7 ta"], "«Hayrat ul-abror», «Farhod va Shirin», «Layli va Majnun», «Sab'ai sayyor», «Saddi Iskandariy»."),
        C(3, "Navoiyning turkiy tilning fors tilidan qolishmasligini isbotlagan asari?", "«Muhokamat ul-lug'atayn»", ["«Mahbub ul-qulub»", "«Lison ut-tayr»", "«Majolis un-nafois»"], "1499-yilda yozilgan."),
        C(2, "Navoiyning turkiy devonlari jamlanmasi nomi?", "«Xazoyin ul-maoniy»", ["«Devoni Foniy»", "«Xamsa»", "«Nazm ul-javohir»"], "To'rt devondan iborat."),
    ],
    "Ikkinchi darajali bo'laklar": [
        C(2, "«Bolalar maktabga shoshilib ketishdi» gapida «shoshilib» qanday bo'lak?", "Holat holi", ["Payt holi", "Aniqlovchi", "To'ldiruvchi"], "Qanday? savoliga javob."),
        C(3, "«Ukam kitobni stolga qo'ydi» gapida vositali to'ldiruvchi?", "stolga", ["kitobni", "Ukam", "qo'ydi"], "Jo'nalish kelishigidagi to'ldiruvchi — vositali."),
        C(2, "Aniqlovchi qaysi so'roqqa javob beradi?", "Qanday? Qaysi? Kimning?", ["Qayerda? Qachon?", "Kimni? Nimani?", "Nima qildi?"], "Ot bilan ifodalangan bo'lakni izohlaydi."),
    ],
    "Aruz vazni": [
        C(2, "Aruz vazni nimaga asoslanadi?", "Cho'ziq va qisqa hijolarning almashinuviga", ["Bo'g'inlar soniga", "Qofiyaga", "Urg'uga"], "Arab she'riyatidan kirgan."),
        C(3, "Aruzda cho'ziq hijo qanday belgilanadi?", "«—»", ["«V»", "«/»", "«+»"], "Qisqa hijo — «V»."),
        C(3, "Aruz ilmiga oid «Mezon ul-avzon» asari muallifi?", "Alisher Navoiy", ["Bobur", "Lutfiy", "Ogahiy"], "Bobur ham aruzga oid risola yozgan."),
    ],
    "Barmoq vazni, qofiya va radif": [
        C(2, "Barmoq vazni nimaga asoslanadi?", "Misralardagi bo'g'inlar soni tengligiga", ["Hijolar cho'ziqligiga", "Urg'uga", "Radifga"], "Xalq og'zaki ijodiga xos."),
        C(3, "Radif nima?", "Qofiyadan keyin takrorlanadigan so'z yoki so'zlar", ["Misraning boshidagi so'z", "She'r sarlavhasi", "Bandlar soni"], "Masalan, g'azallarda."),
        C(2, "To'rtlikda a-a-b-a tartibida qofiyalanish qaysi janrga xos?", "Ruboiy", ["Tuyuq", "G'azal", "Masnaviy"], "Ruboiy aruzning hazaj bahrida."),
    ],
    "Badiiy san'atlar": [
        C(3, "Jonsiz narsaga jonli xususiyat berish qaysi san'at?", "Tashxis (jonlantirish)", ["Tashbeh", "Mubolag'a", "Tazod"], "Masalan: «Tog'lar xo'rsindi»."),
        C(2, "Zid ma'noli so'zlarni qo'llash san'ati?", "Tazod", ["Tashbeh", "Iyhom", "Talmeh"], "Masalan: oq va qora."),
        C(3, "Mashhur tarixiy voqea yoki asarga ishora qiluvchi san'at?", "Talmeh", ["Tajnis", "Ruju", "Tashxis"], "Masalan, Farhod, Majnun nomlari orqali."),
    ],
    "Pirimqul Qodirov: «Yulduzli tunlar»": [
        C(2, "«Yulduzli tunlar» romani kimning hayotiga bag'ishlangan?", "Zahiriddin Muhammad Bobur", ["Mirzo Ulug'bek", "Alisher Navoiy", "Amir Temur"], "Tarixiy roman."),
        C(3, "Pirimqul Qodirovning yana bir tarixiy romani?", "«Ona lochin vidosi»", ["«O'tkan kunlar»", "«Navoiy»", "«Ulug'bek xazinasi»"], "Bobur va Humoyun davri haqida."),
        C(2, "«Yulduzli tunlar» qaysi janrdagi asar?", "Tarixiy roman", ["Qissa", "Doston", "Drama"], "Katta epik asar."),
    ],
    "So'zning ma'nolari: monosemiya va polisemiya": [
        C(2, "Bir necha ma'noga ega so'z?", "Ko'p ma'noli (polisemantik)", ["Omonim", "Sinonim", "Antonim"], "Ma'nolar o'zaro bog'liq."),
        C(3, "«Ko'z» so'zi qaysi birikmada ko'chma ma'noda?", "Buloqning ko'zi", ["Ko'zi og'riydi", "Ko'zini yumdi", "Ko'z yoshi"], "Ma'no ko'chishi — o'xshashlik asosida."),
        C(2, "Faqat bitta ma'noga ega atamalar qanday so'zlar?", "Bir ma'noli (monosemantik)", ["Ko'p ma'noli", "Omonim", "Paronim"], "Masalan: «gipotenuza»."),
    ],
    "Ma'no ko'chishi: metafora, metonimiya, sinekdoxa": [
        C(3, "«Zal qarsak chaldi» gapida qaysi ko'chim bor?", "Metonimiya", ["Metafora", "Sinekdoxa", "Vazifadoshlik"], "Zal o'rnida undagi odamlar — aloqadorlik asosida."),
        C(3, "«Uyda besh jon bor» gapida qaysi ko'chim?", "Sinekdoxa", ["Metafora", "Metonimiya", "Kinoya"], "Butun o'rnida qism (jon — odam)."),
        C(2, "O'xshashlik asosida ma'no ko'chishi?", "Metafora", ["Metonimiya", "Sinekdoxa", "Antiteza"], "Masalan: «choynakning tumshug'i»."),
    ],
    "Omonimlar, gomofonlar va gomograflar": [
        C(2, "Shakli bir xil, ma'nolari bog'liq bo'lmagan so'zlar?", "Omonimlar", ["Sinonimlar", "Antonimlar", "Paronimlar"], "Masalan: «o't» (olov) va «o't» (ko'kat)."),
        C(3, "«Tut» so'zi qaysi juftlikda omonim sifatida qo'llangan?", "Tut daraxti — qo'lini tut", ["Tut mevasi — tut barglari", "Tut daraxti — tut yog'ochi", "Tut shoxi — tut tanasi"], "Biri ot, biri fe'l — ma'nolari bog'liq emas."),
        C(3, "Yozilishi bir xil, talaffuzi (urg'usi) har xil so'zlar?", "Omograflar", ["Omofonlar", "Sinonimlar", "Paronimlar"], "Masalan: «atlas» (mato) va «atlas» (xaritalar to'plami)."),
    ],
    "Paronimlar (talaffuzdosh so'zlar)": [
        C(3, "Qaysi juftlik paronimlar?", "Asr — asir", ["Ota — dada", "Katta — kichik", "O't — o't"], "Talaffuzi yaqin, ma'nosi har xil."),
        C(2, "Paronimlarni noto'g'ri qo'llash qanday xatoga olib keladi?", "Ma'no buzilishiga", ["Urg'u o'zgarishiga", "Imlo me'yori saqlanishiga", "Gap qisqarishiga"], "Masalan: «amr» va «amir»."),
        C(3, "«Shox» va «shoh» so'zlari qaysi hodisaga misol?", "Paronimiya", ["Sinonimiya", "Antonimiya", "Polisemiya"], "Bitta tovush farqi bilan."),
    ],
    "Leksika qatlamlari: o'z va o'zlashgan so'zlar": [
        C(2, "Qaysi so'z arab tilidan o'zlashgan?", "Kitob", ["Non", "Qo'l", "Ot"], "Arabcha «kitāb»."),
        C(3, "Qaysi so'z rus tili orqali o'zlashgan?", "Avtobus", ["Daftar", "Shahar", "Bog'"], "Rus tili orqali Yevropa tillaridan."),
        C(2, "«Daftar» so'zining kelib chiqishi?", "Fors-tojik tilidan", ["Arab tilidan", "Turkiy (o'z qatlam)", "Ingliz tilidan"], "Fors-tojik qatlam."),
    ],
    "Arxaizm, istorizm, neologizm, tabu va evfemizm": [
        C(3, "Bugungi kunda iste'moldan chiqqan narsa nomini bildiruvchi so'z?", "Istorizm", ["Arxaizm", "Neologizm", "Evfemizm"], "Masalan: «arava» emas, «sovut», «dorug'a»."),
        C(3, "«Vafot etdi» iborasi «o'ldi» so'zi o'rnida qo'llansa — bu?", "Evfemizm", ["Tabu", "Arxaizm", "Neologizm"], "Qo'pol ma'noni yumshatish."),
        C(2, "Yangi paydo bo'lgan so'zlar?", "Neologizmlar", ["Arxaizmlar", "Dialektizmlar", "Istorizmlar"], "Masalan, texnika atamalari."),
    ],
    "Frazeologizmlar va maqollar": [
        C(2, "«Qulog'iga quyib olmoq» frazeologizmining ma'nosi?", "Yaxshi eslab qolmoq", ["Eshitmaslik", "Xafa bo'lmoq", "Shoshilmoq"], "Ko'chma ma'no."),
        C(3, "«Tarvuzi qo'ltig'idan tushdi» iborasining ma'nosi?", "Umidi puchga chiqib, hafsalasi pir bo'ldi", ["Juda xursand bo'ldi", "Charchadi", "Boyib ketdi"], "Frazeologik birlik."),
        C(2, "Frazeologizmning asosiy belgisi?", "Tarkibi turg'un, ma'nosi yaxlit", ["Har safar yangidan tuziladi", "Faqat bitta so'zdan iborat", "Faqat she'rda uchraydi"], "So'zlarini almashtirib bo'lmaydi."),
    ],
    "Xalq og'zaki ijodi janrlari": [
        C(2, "Qaysi janr xalq og'zaki ijodiga kirmaydi?", "Roman", ["Doston", "Ertak", "Topishmoq"], "Roman — yozma adabiyot janri."),
        C(3, "Mehnat qo'shiqlariga misol?", "«Mayda-yo mayda» (o'rim)", ["«Alla»", "«Yor-yor»", "«Ramazon»"], "O'rim-yig'im paytida aytilgan."),
        C(2, "To'y marosimida aytiladigan qo'shiq?", "«Yor-yor»", ["«Alla»", "«Yo'qlov»", "«Sust xotin»"], "Kelin kuzatilganda."),
    ],
    "Unli tovushlar tasnifi va nutq a'zolari": [
        C(2, "O'zbek adabiy tilida nechta unli tovush bor?", "6 ta", ["5 ta", "9 ta", "8 ta"], "i, e, a, o, u, o'."),
        C(3, "Lablangan unlilar qaysilar?", "o, u, o'", ["i, e, a", "a, o, i", "e, u, i"], "Talaffuzda lablar cho'chchayadi."),
        C(2, "Til oldi unlilari?", "i, e, a", ["o, u, o'", "a, o, u", "u, o', i"], "Til oldinga suriladi."),
    ],
    "Undosh tovushlar tasnifi": [
        C(2, "O'zbek tilida nechta undosh tovush bor?", "24 ta", ["23 ta", "26 ta", "20 ta"], "Adabiy tilda."),
        C(3, "Qaysi undoshlar faqat jarangsiz?", "p, t, k, f, s, sh, ch, x, h, q", ["b, d, g, v, z", "m, n, l, r", "y, ng"], "Ovoz paychalari tebranmaydi."),
        C(2, "Sonor undoshlar?", "m, n, l, r, ng, y", ["p, t, k", "b, d, g", "s, sh, ch"], "Ovozdan iborat, shovqin kam."),
    ],
    "Fonetik hodisalar: eliziya, epenteza, assimilyatsiya": [
        C(3, "«Ishsiz» so'zi «ishshiz» deb talaffuz qilinishi qaysi hodisa?", "Assimilyatsiya (tovush moslashuvi)", ["Eliziya", "Epenteza", "Metateza"], "s tovushi sh ga moslashadi."),
        C(3, "«Burun + i → burni» o'zgarishi qaysi hodisa?", "Unli tushishi", ["Undosh orttirilishi", "Assimilyatsiya", "Dissimilyatsiya"], "Ikkinchi bo'g'indagi unli tushadi."),
        C(2, "So'z boshida unli orttirilishi (masalan, «stakan → istakan») qaysi hodisa?", "Proteza", ["Eliziya", "Metateza", "Reduksiya"], "So'z boshiga tovush qo'shiladi."),
    ],
    "Morfemika va so'z yasalishi": [
        C(2, "«Paxtakor» so'zining yasovchi qo'shimchasi?", "-kor", ["-paxta", "-or", "-ka"], "Shaxs oti yasovchi."),
        C(3, "Qaysi so'z qo'shma usulda yasalgan?", "Gultojixo'roz", ["Gulchi", "Gulzor", "Gullar"], "Ikki va undan ortiq asosdan."),
        C(2, "So'zning lug'aviy ma'noni bildiruvchi qismi?", "O'zak", ["Qo'shimcha", "Kelishik", "Yuklama"], "Morfemaning asosiy turi."),
    ],
    "«Alpomish» va «Go'ro'g'li» dostonlari": [
        C(2, "«Alpomish» dostoni qaysi turdagi doston?", "Qahramonlik dostoni", ["Ishqiy doston", "Tarixiy doston", "Kitobiy doston"], "Xalq og'zaki ijodi."),
        C(3, "«Alpomish»ning eng mashhur variantini kim aytgan?", "Fozil Yo'ldosh o'g'li", ["Ergash Jumanbulbul o'g'li", "Islom shoir", "Po'lkan shoir"], "1922-yilda yozib olingan."),
        C(2, "«Go'ro'g'li» turkumidagi bosh qahramonning ot nomi?", "G'irot", ["Boychibor", "Duldul", "Rahsh"], "Boychibor — Alpomishning oti."),
    ],
    "So'z ko'chirish qoidalari": [
        C(2, "Qaysi so'z to'g'ri bo'g'inga ajratib ko'chirilgan?", "mak-tab", ["ma-ktab", "makt-ab", "m-aktab"], "Bo'g'in chegarasida ko'chiriladi."),
        C(3, "Qaysi so'z qatordan qatorga ko'chirilmaydi?", "BMT", ["Respublika", "O'zbekiston", "Kitob"], "Qisqartmalar ko'chirilmaydi."),
        C(2, "Bitta harfni qatorda qoldirish yoki keyingi qatorga o'tkazish mumkinmi?", "Yo'q", ["Ha, har doim", "Faqat unlini", "Faqat undoshni"], "Masalan, «a-ka» emas."),
    ],
    "Ot turkumi": [
        C(2, "Atoqli otga misol?", "Samarqand", ["Shahar", "Daryo", "Kitob"], "Bosh harf bilan yoziladi."),
        C(3, "Mavhum otga misol?", "Baxt", ["Stol", "Daraxt", "Qalam"], "Ko'z bilan ko'rib bo'lmaydigan tushuncha."),
        C(2, "Ot qaysi so'roqlarga javob beradi?", "Kim? Nima? Qayer?", ["Qanday? Qaysi?", "Qancha? Nechta?", "Nima qildi?"], "Predmet nomini bildiradi."),
    ],
    "Sifat va sifat darajalari": [
        C(2, "«Oqish» so'zi sifatning qaysi darajasi?", "Ozaytirma daraja", ["Orttirma daraja", "Oddiy daraja", "Qiyosiy daraja"], "-ish qo'shimchasi."),
        C(3, "«Eng chiroyli» birikmasi qaysi darajada?", "Orttirma daraja", ["Qiyosiy daraja", "Ozaytirma daraja", "Oddiy daraja"], "«eng» so'zi bilan."),
        C(2, "«Kattaroq» so'zi qaysi daraja?", "Qiyosiy daraja", ["Orttirma daraja", "Ozaytirma daraja", "Oddiy daraja"], "-roq qo'shimchasi."),
    ],
    "Son turkumi": [
        C(2, "«Beshinchi» qaysi son turi?", "Tartib son", ["Sanoq son", "Jamlovchi son", "Taqsim son"], "-(i)nchi qo'shimchasi."),
        C(3, "«Ikkovlon» qaysi son turi?", "Jamlovchi son", ["Tartib son", "Kasr son", "Chama son"], "-ov, -ovlon qo'shimchalari."),
        C(2, "«O'ntadan» qaysi son turi?", "Taqsim son", ["Chama son", "Tartib son", "Jamlovchi son"], "-tadan qo'shimchasi."),
    ],
    "Olmosh turkumi": [
        C(2, "«Kim?», «Nima?» qaysi olmosh turi?", "So'roq olmoshi", ["Kishilik olmoshi", "Ko'rsatish olmoshi", "Belgilash olmoshi"], "So'roq gaplarda."),
        C(3, "«Hamma», «barcha» qaysi olmosh turi?", "Belgilash-jamlash olmoshi", ["Bo'lishsizlik olmoshi", "Ko'rsatish olmoshi", "O'zlik olmoshi"], "Jamlik ma'nosi."),
        C(2, "«Hech kim» qaysi olmosh turi?", "Bo'lishsizlik olmoshi", ["So'roq olmoshi", "Gumon olmoshi", "Kishilik olmoshi"], "Inkor ma'nosi."),
    ],
    "Ravish turkumi": [
        C(2, "«Tez» so'zi «tez yurdi» birikmasida qaysi turkum?", "Ravish", ["Sifat", "Fe'l", "Ot"], "Harakat belgisini bildiradi."),
        C(3, "Payt ravishiga misol?", "Kecha", ["Sekin", "Ko'p", "Atayin"], "Qachon? so'rog'iga javob."),
        C(2, "Ravish gapda ko'pincha qaysi bo'lak vazifasida keladi?", "Hol", ["Ega", "To'ldiruvchi", "Kesim"], "Harakat belgisini bildirgani uchun."),
    ],
    "«Qutadg'u bilig» va qadimgi adabiy yodgorliklar": [
        C(2, "«Qutadg'u bilig» muallifi?", "Yusuf Xos Hojib", ["Mahmud Koshg'ariy", "Ahmad Yassaviy", "Adib Ahmad Yugnakiy"], "1069-yilda yozilgan."),
        C(3, "«Devonu lug'otit turk» asarining muallifi?", "Mahmud Koshg'ariy", ["Yusuf Xos Hojib", "Rabg'uziy", "Ahmad Yugnakiy"], "Turkiy so'zlar lug'ati."),
        C(3, "«Hibat ul-haqoyiq» asari muallifi?", "Adib Ahmad Yugnakiy", ["Yusuf Xos Hojib", "Ahmad Yassaviy", "Sulaymon Boqirg'oniy"], "Pand-nasihat asari."),
    ],
    "Ot yasovchi qo'shimchalar": [
        C(2, "Qaysi so'z ot yasovchi qo'shimcha bilan yasalgan?", "Bilim", ["Bildi", "Bilgan", "Bilib"], "-im qo'shimchasi."),
        C(3, "-zor qo'shimchasi qanday ma'no hosil qiladi?", "Joy (makon) oti", ["Shaxs oti", "Mavhum ot", "Qurol oti"], "Masalan: gulzor, olmazor."),
        C(2, "-chi qo'shimchasi bilan yasalgan so'z?", "Ishchi", ["Ishsiz", "Ishli", "Ishxona"], "Kasb-hunar egasi."),
    ],
    "Fe'lning vazifa shakllari: harakat nomi, sifatdosh, ravishdosh": [
        C(3, "«O'qigan kitob» birikmasidagi «o'qigan» qaysi shakl?", "Sifatdosh", ["Ravishdosh", "Harakat nomi", "Shart mayli"], "-gan qo'shimchasi, predmet belgisi."),
        C(3, "«Kulib gapirdi» birikmasidagi «kulib» qaysi shakl?", "Ravishdosh", ["Sifatdosh", "Harakat nomi", "Buyruq mayli"], "-ib qo'shimchasi, harakat belgisi."),
        C(2, "«O'qish — bilim manbai» gapidagi «o'qish»?", "Harakat nomi", ["Sifatdosh", "Ravishdosh", "Ot"], "-ish qo'shimchasi."),
    ],
    "Fe'l mayllari va zamonlari": [
        C(2, "«Bormoqchiman» qaysi maylda?", "Maqsad mayli", ["Buyruq mayli", "Shart mayli", "Ijro mayli"], "-moqchi qo'shimchasi."),
        C(3, "«Kelsang» fe'li qaysi maylda?", "Shart mayli", ["Buyruq-istak mayli", "Ijro mayli", "Maqsad mayli"], "-sa qo'shimchasi."),
        C(2, "«Yozyapman» qaysi zamon?", "Hozirgi zamon (davomli)", ["O'tgan zamon", "Kelasi zamon", "Uzoq o'tgan zamon"], "-yap qo'shimchasi."),
    ],
    "Ko'makchi, bog'lovchi va yuklama": [
        C(2, "«Sen bilan» birikmasidagi «bilan» qaysi turkum?", "Ko'makchi", ["Bog'lovchi", "Yuklama", "Ravish"], "Ot bilan birikib munosabat bildiradi."),
        C(3, "«Hatto bolalar ham bildi» gapidagi «hatto»?", "Yuklama", ["Bog'lovchi", "Ko'makchi", "Modal so'z"], "Kuchaytiruv ma'nosi."),
        C(2, "Zidlov bog'lovchisi?", "Ammo", ["Va", "Hamda", "Yoki"], "Shuningdek: lekin, biroq."),
    ],
    "Modal, undov va taqlid so'zlar": [
        C(2, "«Shubhasiz» so'zi qaysi turkum?", "Modal so'z", ["Undov so'z", "Taqlid so'z", "Ravish"], "So'zlovchining munosabati."),
        C(3, "«Taq-tuq» qaysi turkum?", "Taqlid so'z", ["Undov", "Modal so'z", "Ravish"], "Tovushga taqlid."),
        C(2, "«Voy!», «Eh!» qaysi turkum?", "Undov so'z", ["Taqlid so'z", "Yuklama", "Modal so'z"], "His-hayajon."),
    ],
    "So'z birikmasi va sintaktik aloqa": [
        C(3, "«Kitobni o'qimoq» birikmasidagi tobe so'z qanday bog'langan?", "Boshqaruv", ["Moslashuv", "Bitishuv", "Teng aloqa"], "Kelishik qo'shimchasi orqali."),
        C(3, "«Tez yugurmoq» birikmasida qaysi aloqa?", "Bitishuv", ["Boshqaruv", "Moslashuv", "Teng aloqa"], "Qo'shimchasiz, tartib va ohang orqali."),
        C(2, "«Mening kitobim» birikmasida qaysi aloqa?", "Moslashuv", ["Bitishuv", "Boshqaruv", "Teng aloqa"], "Shaxs-son bo'yicha moslashadi."),
    ],
    "Ega, kesim va ular orasidagi tire": [
        C(3, "Qaysi gapda ega va kesim orasiga tire qo'yiladi?", "Toshkent — poytaxt.", ["Men talabaman.", "U keldi.", "Kitob stolda."], "Ikkalasi ot bilan ifodalanganda."),
        C(2, "Gapning grammatik asosi?", "Ega va kesim", ["To'ldiruvchi va hol", "Aniqlovchi va ega", "Hol va kesim"], "Bosh bo'laklar."),
        C(3, "«Vazifamiz — o'qish» gapida tire qo'yilishining sababi?", "Ega ot, kesim harakat nomi bilan ifodalangan", ["Gap so'roq gap", "Undalma bor", "Kesim fe'l bilan ifodalangan"], "Bog'lamasiz kesim."),
    ],
    "Zahiriddin Muhammad Bobur va «Boburnoma»": [
        C(2, "«Boburnoma» qaysi janrdagi asar?", "Memuar (esdalik)", ["Doston", "G'azal", "Roman"], "Tarixiy-memuar asar."),
        C(3, "Bobur aruz haqida yozgan risola?", "«Mufassal» («Aruz risolasi»)", ["«Mezon ul-avzon»", "«Mahbub ul-qulub»", "«Xamsa»"], "Bobur aruz nazariyasini ham yoritgan."),
        C(2, "Bobur asos solgan davlat?", "Boburiylar davlati (Hindistonda)", ["Temuriylar davlati", "Shayboniylar davlati", "Qo'qon xonligi"], "1526-yil Panipat jangidan so'ng."),
    ],
    "Gap turlari: maqsad va ohangga ko'ra": [
        C(2, "«Darsni yaxshi o'qing!» qaysi gap turi?", "Buyruq gap", ["Darak gap", "So'roq gap", "His-hayajon gap"], "Undash, buyruq."),
        C(3, "Ritorik so'roq gap nima?", "Javob talab qilmaydigan so'roq gap", ["Faqat «ha» yoki «yo'q» javobli", "Undalmali gap", "Buyruq gap"], "Fikrni ta'kidlash uchun."),
        C(2, "Darak gap oxiriga qanday tinish belgisi qo'yiladi?", "Nuqta", ["So'roq", "Undov", "Ko'p nuqta"], "Xabar beradi."),
    ],
    "Bir tarkibli gaplar": [
        C(3, "«Kuz. Yaproqlar to'kilmoqda.» — birinchi gap qaysi tur?", "Atov gap", ["Shaxsi noma'lum gap", "Shaxsi topilmas gap", "To'liqsiz gap"], "Faqat bitta bosh bo'lak — ot."),
        C(3, "«Kitobni o'qish kerak» qaysi bir tarkibli gap?", "Shaxsi topilmas gap", ["Atov gap", "Shaxsi aniq gap", "Shaxsi umumlashgan gap"], "Ish bajaruvchini topib bo'lmaydi."),
        C(2, "Shaxsi aniq gapda ega qanday tiklanadi?", "Kesimdagi shaxs-son qo'shimchasidan", ["Kontekstdan", "Aniqlovchidan", "Tiklanmaydi"], "Masalan: «Keldim» — men."),
    ],
    "Undalma, kiritma va ajratilgan bo'lakli gaplar": [
        C(2, "«Do'stlar, darsga kechikmang!» gapida undalma?", "Do'stlar", ["Darsga", "Kechikmang", "Gapda yo'q"], "Murojaat qilinayotgan shaxs."),
        C(3, "«Afsuski, u kelmadi» gapidagi «afsuski» qanday bo'lak?", "Kirish so'z", ["Undalma", "Hol", "Ega"], "Munosabat bildiradi, vergul bilan ajratiladi."),
        C(2, "Undalma gap bo'lagi hisoblanadimi?", "Yo'q", ["Ha, ega", "Ha, hol", "Ha, to'ldiruvchi"], "Grammatik bog'lanmaydi."),
    ],
    "Teng bog'langan qo'shma gaplar": [
        C(2, "Teng bog'langan qo'shma gap qismlari qanday bog'lanadi?", "Teng bog'lovchilar orqali", ["Ergashtiruvchi bog'lovchilar orqali", "Faqat ohang bilan", "Nisbiy so'zlar orqali"], "va, ammo, yoki..."),
        C(3, "«Quyosh chiqdi, ammo havo sovuq edi» gapi qaysi tur?", "Zidlov munosabatli teng bog'langan qo'shma gap", ["Ergash gapli qo'shma gap", "Sodda gap", "Bog'lovchisiz qo'shma gap"], "«ammo» zidlov bog'lovchisi."),
        C(2, "Teng bog'langan qo'shma gap qismlari orasiga odatda nima qo'yiladi?", "Vergul", ["Tire", "Ikki nuqta", "Qavs"], "Bog'lovchidan oldin."),
    ],
    "Ergash gapli qo'shma gaplar": [
        C(3, "«Agar vaqt bo'lsa, kelaman» gapidagi ergash gap turi?", "Shart ergash gap", ["Sabab ergash gap", "Payt ergash gap", "To'siqsiz ergash gap"], "-sa qo'shimchasi va «agar»."),
        C(3, "«Yomg'ir yog'gani uchun o'yin qoldirildi» ergash gap turi?", "Sabab ergash gap", ["Maqsad ergash gap", "Natija ergash gap", "Shart ergash gap"], "«uchun» ko'makchisi."),
        C(2, "Ergash gap bosh gapga qanday munosabatda?", "Bosh gapga tobe bo'ladi", ["Teng huquqli", "Bog'liq emas", "Bosh gapni boshqaradi"], "Biror bo'lagini izohlaydi."),
    ],
    "Bog'lovchisiz qo'shma gaplar va tinish belgilari": [
        C(3, "«Kuz keldi: daraxtlar sarg'aydi» gapida ikki nuqta nima uchun qo'yilgan?", "Ikkinchi qism birinchisini izohlaydi", ["Sanash bor", "Zidlov ma'nosi bor", "Undalma bor"], "Izoh munosabati."),
        C(3, "Qismlar o'rtasida zidlov yoki keskin natija ma'nosi bo'lsa, qanday belgi qo'yiladi?", "Tire", ["Vergul", "Nuqtali vergul", "Qavs"], "Masalan: «Mehnat qilding — natija bor»."),
        C(2, "Bog'lovchisiz qo'shma gap qismlari nima orqali bog'lanadi?", "Ohang orqali", ["Bog'lovchilar orqali", "Ko'makchilar orqali", "Nisbiy so'zlar orqali"], "Bog'lovchi yo'q."),
    ],
    "Ko'chirma va o'zlashtirma gap, nutq uslublari": [
        C(2, "Ko'chirma gap qanday belgilar ichida yoziladi?", "Qo'shtirnoq", ["Qavs", "Tire", "Vergul"], "Muallif gapidan ajratiladi."),
        C(3, "Ko'chirma gapni o'zlashtirma gapga aylantirganda nima o'zgaradi?", "Shaxs olmoshlari va qo'shimchalar muallif nuqtayi nazariga moslashadi", ["Hech narsa", "Faqat tinish belgilari", "Faqat so'z tartibi"], "Ko'pincha «deb», «ekanini» qo'shiladi."),
        C(2, "Ilmiy uslubning asosiy belgisi?", "Atamalarning ko'pligi, aniqlik", ["Hissiylik", "So'zlashuv iboralari", "Badiiy tasvir"], "Mantiqiy va aniq."),
    ],
    "Behbudiy va «Padarkush» dramasi": [
        C(2, "«Padarkush» qaysi yilda yozilgan?", "1911-yilda", ["1901-yilda", "1920-yilda", "1937-yilda"], "Birinchi o'zbek dramasi."),
        C(3, "«Padarkush» dramasining asosiy g'oyasi?", "Ilmsizlik fojiaga olib keladi", ["Sevgi har narsadan ustun", "Boylik — baxt", "Urushning dahshati"], "Ma'rifatparvarlik."),
        C(2, "Behbudiy qaysi harakat yetakchilaridan?", "Jadidchilik", ["Bosmachilik", "Sarbadorlar", "Muqanna"], "Turkiston jadidlarining otasi."),
    ],
    "Abdulla Qodiriy va «O'tkan kunlar»": [
        C(2, "«O'tkan kunlar» romanining bosh qahramonlari?", "Otabek va Kumush", ["Anvar va Ra'no", "Farhod va Shirin", "Yusuf va Zulayho"], "Birinchi o'zbek romani."),
        C(3, "Abdulla Qodiriyning ikkinchi romani?", "«Mehrobdan chayon»", ["«Kecha va kunduz»", "«Navoiy»", "«Qutlug' qon»"], "Anvar va Ra'no haqida."),
        C(2, "«O'tkan kunlar» romani voqealari qaysi davrda kechadi?", "XIX asr o'rtalari, Qo'qon xonligi davri", ["Temuriylar davri", "Mustaqillik yillari", "Ikkinchi jahon urushi"], "Tarixiy roman."),
    ],
    "Cho'lpon: lirikasi va «Kecha va kunduz»": [
        C(2, "Cho'lponning haqiqiy ismi?", "Abdulhamid Sulaymon o'g'li", ["Abdulla Avloniy", "Abdurauf Fitrat", "Hamza Hakimzoda"], "Taxallusi «tong yulduzi» ma'nosida."),
        C(3, "«Kecha va kunduz» romanining bosh qahramoni?", "Zebi", ["Kumush", "Ra'no", "Gulnor"], "Romanning birinchi qismi «Kecha»."),
        C(2, "Cho'lponning mashhur she'riy to'plamlari?", "«Uyg'onish», «Buloqlar», «Tong sirlari»", ["«Xamsa», «Devon»", "«Boburnoma»", "«Mahbub ul-qulub»"], "1920-yillar."),
    ],
    "Tinish belgilari qoidalari": [
        C(2, "Uyushiq bo'laklar orasiga odatda qanday belgi qo'yiladi?", "Vergul", ["Tire", "Nuqta", "Qavs"], "Bog'lovchisiz bog'langanda."),
        C(3, "Uyushiq bo'laklardan oldin umumlashtiruvchi so'z kelsa, qanday belgi qo'yiladi?", "Ikki nuqta", ["Tire", "Vergul", "Nuqtali vergul"], "Masalan: «Hamma keldi: o'qituvchilar, o'quvchilar...»."),
        C(3, "Umumlashtiruvchi so'z uyushiq bo'laklardan keyin kelsa?", "Tire", ["Ikki nuqta", "Vergul", "Qavs"], "«Olma, nok, uzum — hammasi pishdi»."),
    ],
    "Matn va uning bog'lanish vositalari": [
        C(2, "Matndagi gaplarni bog'lovchi vositalarga misol?", "Olmoshlar va takrorlar", ["Faqat sarlavha", "Rasmlar", "Tinish belgilari"], "Leksik-grammatik vositalar."),
        C(3, "Matnning asosiy belgilaridan biri?", "Mavzu va mazmun yaxlitligi", ["Faqat bitta gapdan iboratligi", "Sarlavhasizligi", "She'riy shakli"], "Yaxlitlik va bog'liqlik."),
        C(2, "Matnning eng kichik mazmuniy qismi?", "Xatboshi (abzats)", ["Kitob", "Bob", "So'z"], "Bir mikromavzuni ifodalaydi."),
    ],
    "Abdulla Qahhor: hikoyalar va «Sinchalak»": [
        C(2, "«Sinchalak» qissasining bosh qahramoni?", "Saida", ["Kumush", "Zebi", "Ra'no"], "Kolxoz raisi."),
        C(3, "«O'g'ri» hikoyasida ho'kizi o'g'irlangan Qobil bobo amaldorlarga murojaat qilgach nima bo'ladi?", "Amaldorlar pora oladi, ho'kiz topilmaydi", ["Ho'kiz darhol topiladi", "O'g'ri sudlanadi", "Qobil boboga yangi ho'kiz beriladi"], "Chor amaldorlarining poraxo'rligi fosh etiladi."),
        C(2, "Abdulla Qahhor ijodida qaysi janr yetakchi?", "Hikoya", ["G'azal", "Doston", "Ruboiy"], "O'zbek hikoyachiligining ustasi."),
    ],
    "Maqsud Shayxzoda: «Mirzo Ulug'bek» fojiasi": [
        C(2, "«Mirzo Ulug'bek» asari qaysi janrda?", "Tragediya (fojia)", ["Roman", "Qissa", "Komediya"], "She'riy drama."),
        C(3, "Fojiada Ulug'bekka xiyonat qilgan o'g'li?", "Abdullatif", ["Abdulaziz", "Shohruh", "Boysunqur"], "Otasini o'ldirtirgan."),
        C(2, "Ulug'bek qaysi fan bilan mashhur?", "Astronomiya", ["Tibbiyot", "Kimyo", "Geografiya"], "«Ziji Ko'ragoniy»."),
    ],
    "Said Ahmad: «Ufq» trilogiyasi": [
        C(2, "«Ufq» trilogiyasi nechta kitobdan iborat?", "3 ta", ["2 ta", "4 ta", "5 ta"], "Trilogiya — uch qismli asar."),
        C(3, "Said Ahmadning mashhur komediyasi?", "«Kelinlar qo'zg'oloni»", ["«Padarkush»", "«Mirzo Ulug'bek»", "«Boy ila xizmatchi»"], "Farmonbibi obrazi."),
        C(2, "Said Ahmad qaysi janrda ham samarali ijod qilgan?", "Hikoya va hajviya", ["Faqat she'r", "Faqat doston", "Ilmiy asar"], "Yumoristik hikoyalari mashhur."),
    ],
    "Odil Yoqubov: «Ulug'bek xazinasi»": [
        C(2, "«Ulug'bek xazinasi» qaysi janrdagi asar?", "Tarixiy roman", ["Komediya", "Doston", "Ruboiy"], "Ulug'bek davri haqida."),
        C(3, "Odil Yoqubovning yana bir mashhur romani?", "«Diyonat»", ["«O'tkan kunlar»", "«Navoiy»", "«Sarob»"], "Zamonaviy ma'naviy muammolar."),
        C(2, "Romandagi «xazina» nimani anglatadi?", "Ulug'bekning ilmiy kitoblari va merosi", ["Oltin-kumush", "Qurol-yarog'", "Yer-mulk"], "Ilm — eng katta boylik."),
    ],
    "Adabiyot nazariyasi: tur, janr va obraz": [
        C(2, "Adabiyotning uch turi?", "Epik, lirik, dramatik", ["Roman, qissa, hikoya", "G'azal, ruboiy, tuyuq", "Ertak, doston, maqol"], "Adabiy turlar."),
        C(3, "Qaysi janr dramatik turga kiradi?", "Tragediya", ["Roman", "G'azal", "Qissa"], "Sahna uchun yoziladi."),
        C(2, "Badiiy asardagi inson tasviri?", "Obraz", ["Syujet", "Kompozitsiya", "Ritm"], "Badiiy timsol."),
    ],
    "Oybek ijodi: «Navoiy» va «Qutlug' qon»": [
        C(2, "«Navoiy» romani muallifi?", "Oybek", ["Abdulla Qodiriy", "Cho'lpon", "G'afur G'ulom"], "1944-yil."),
        C(3, "«Qutlug' qon» romanining bosh qahramoni?", "Yo'lchi", ["Otabek", "Anvar", "Saida"], "1916-yil voqealari fonida."),
        C(2, "Oybekning haqiqiy ismi?", "Muso Toshmuhammad o'g'li", ["Abdulhamid Sulaymon o'g'li", "Hamza Hakimzoda", "Fozil Yo'ldosh o'g'li"], "Taxallusi Oybek."),
    ],
    "Erkin Vohidov va Abdulla Oripov ijodi": [
        C(2, "«O'zbekiston Respublikasining Davlat madhiyasi» so'zlari muallifi?", "Abdulla Oripov", ["Erkin Vohidov", "G'afur G'ulom", "Zulfiya"], "1992-yil."),
        C(3, "Erkin Vohidovning «Ruhlar isyoni» dostoni kimga bag'ishlangan?", "Nazrul Islomga", ["Navoiyga", "Boburga", "Ulug'bekka"], "Bengal shoiri."),
        C(2, "«O'zbegim» qasidasi muallifi?", "Erkin Vohidov", ["Abdulla Oripov", "Cho'lpon", "Oybek"], "1968-yil."),
    ],
    "Tog'ay Murod ijodi": [
        C(2, "«Otamdan qolgan dalalar» romani muallifi?", "Tog'ay Murod", ["Said Ahmad", "O'tkir Hoshimov", "Shukur Xolmirzayev"], "Dehqon hayoti haqida."),
        C(3, "Tog'ay Murodning qissasi?", "«Oydinda yurgan odamlar»", ["«Dunyoning ishlari»", "«Sinchalak»", "«Bahor qaytmaydi»"], "Mashhur qissa."),
        C(2, "Tog'ay Murod ijodining asosiy mavzusi?", "Qishloq va oddiy inson taqdiri", ["Kosmos", "Shahar sanoati", "Tarixiy janglar"], "Xalqona til."),
    ],
}

ENG: dict[str, list] = {
    "Used to / would / be used to": [
        C(2, "When I was a child, I ___ play football every day.", "used to", ["am used to", "use to", "was used to"], "Past habit: used to + V."),
        C(3, "She has lived in London for years, so she ___ driving on the left.", "is used to", ["used to", "would", "uses to"], "be used to + V-ing = accustomed to."),
        C(3, "Which sentence is grammatically correct?", "We would visit our grandparents every summer.", ["We would live in Tashkent in 2010.", "We are used to work late.", "I didn't used to like tea."], "'would' is for repeated past actions, not states."),
    ],
    "Too / enough / so / such": [
        C(2, "The bag is ___ heavy for me to carry.", "too", ["enough", "such", "so much"], "too + adjective + to-infinitive."),
        C(3, "It was ___ a good film that we watched it twice.", "such", ["so", "too", "enough"], "such + a + adjective + noun."),
        C(2, "He isn't old ___ to drive a car.", "enough", ["too", "so", "such"], "adjective + enough."),
    ],
    "Causative: have / get something done": [
        C(2, "I ___ my hair cut yesterday.", "had", ["did", "made", "let"], "have something done."),
        C(3, "She is going to ___ her car repaired next week.", "get", ["make", "let", "do"], "get something done = arrange for someone to do it."),
        C(3, "Which sentence means someone else did the work?", "We had our house painted.", ["We painted our house.", "We have painted our house.", "We were painting our house."], "Causative form."),
    ],
    "Indirect questions va so'z tartibi": [
        C(2, "Could you tell me where ___?", "the station is", ["is the station", "does the station is", "the station does"], "Indirect question: subject + verb."),
        C(3, "I wonder ___ he will come tomorrow.", "whether", ["that", "what", "does"], "yes/no question → if/whether."),
        C(3, "Do you know what time ___?", "the film starts", ["does the film start", "starts the film", "the film does start"], "No auxiliary 'do' in indirect questions."),
    ],
    "Lug'at: ish va iqtisod": [
        C(2, "A person who is paid to work for another person or company is an ___.", "employee", ["employer", "employment", "unemployed"], "employer = the one who hires."),
        C(3, "The money you earn from a job every month is your ___.", "salary", ["profit", "loan", "tax"], "Profit is earned by a business."),
        C(2, "To lose your job because the company no longer needs you: to be made ___.", "redundant", ["promoted", "retired", "hired"], "be made redundant."),
    ],
    "Lug'at: tabiat va hayvonlar": [
        C(2, "An animal that eats only plants is a ___.", "herbivore", ["carnivore", "predator", "omnivore"], "Herb = plant."),
        C(3, "Animals that are in danger of disappearing completely are ___ species.", "endangered", ["extinct", "domestic", "wild"], "Extinct = already gone."),
        C(2, "A large area of land covered with trees is a ___.", "forest", ["desert", "valley", "cliff"], "Basic nature vocabulary."),
    ],
    "Make / do va boshqa kollokatsiyalar": [
        C(2, "Please ___ your homework before you go out.", "do", ["make", "take", "have"], "do homework."),
        C(3, "I'm sorry, I ___ a mistake.", "made", ["did", "took", "had"], "make a mistake."),
        C(3, "Which collocation is correct?", "make a decision", ["do a decision", "take a progress", "do a noise"], "make a decision / make progress / make a noise."),
    ],
    "Qarama-qarshilik: although / despite / unless": [
        C(2, "___ it was raining, we went for a walk.", "Although", ["Despite", "Unless", "Because of"], "although + clause."),
        C(3, "___ the bad weather, the match continued.", "Despite", ["Although", "Unless", "However"], "despite + noun."),
        C(3, "You won't pass the exam ___ you study harder.", "unless", ["although", "despite", "even though"], "unless = if not."),
    ],
    "Reading: asosiy fikr va tafsilot (matn)": [
        C(2, "Read: 'Bees are vital for farming. They pollinate about one third of the crops we eat. Without them, food prices would rise sharply.' What is the main idea?", "Bees are very important for food production.", ["Food prices are rising.", "Farmers dislike bees.", "Bees eat crops."], "The other sentences support this idea."),
        C(3, "In the same text, the word 'vital' is closest in meaning to:", "essential", ["dangerous", "small", "optional"], "vital = extremely important."),
        C(2, "According to the text, about how many of our crops do bees pollinate?", "one third", ["half", "all", "one tenth"], "Detail question."),
    ],
    "Reading: xulosa va kontekstdan ma'no (matn)": [
        C(3, "Read: 'Ali checked his watch again, tapped his foot and kept looking at the door.' How does Ali probably feel?", "impatient", ["relaxed", "bored with his watch", "sleepy"], "Inference from actions."),
        C(3, "'The old bridge was so fragile that only one person could cross at a time.' 'Fragile' means:", "easily broken", ["very long", "beautiful", "new"], "Context clue: only one person at a time."),
        C(2, "'Despite the heavy traffic, Sara arrived early.' What can we infer?", "Sara left home in good time.", ["Sara was late.", "There was no traffic.", "Sara didn't go."], "Inference."),
    ],
    "Gap to'ldirish: zamon tanlash (matn)": [
        C(2, "I ___ in this city since 2019.", "have lived", ["live", "lived", "am living"], "since → Present Perfect."),
        C(3, "When the teacher came in, the students ___ quietly.", "were reading", ["read", "have read", "are reading"], "Past Continuous for an action in progress."),
        C(3, "By the time we arrived, the film ___.", "had already started", ["already started", "has already started", "was starting"], "Past Perfect: earlier past action."),
    ],
}

HIST: dict[str, list] = {
    "Rossiya va O'zbek xonliklari elchilik aloqalari": [
        C(2, "Rossiyaning Buxoroga yuborgan ilk elchisi (1620)?", "Ivan Xoxlov", ["Florio Beneveni", "N. Ignatyev", "M. Chernyayev"], "1620-yilda Buxoroga kelgan."),
        C(3, "Pyotr I yuborgan Bekovich-Cherkasskiy ekspeditsiyasi qaysi xonlikka qarshi edi?", "Xiva xonligi", ["Qo'qon xonligi", "Buxoro amirligi", "Qozon xonligi"], "1717-yilda halokatga uchragan."),
    ],
    "XIX asr o'rtalarida xonliklarning zaiflashuvi va Rossiya rejalari": [
        C(2, "XIX asr o'rtalarida xonliklarning zaiflashishiga asosiy sabab?", "O'zaro urushlar va ichki nizolar", ["Aholining keskin ko'payishi", "Dengizdan uzoqlik emas", "Savdoning to'xtashi faqat"], "Uch xonlik o'zaro kurashda edi."),
        C(3, "Rossiyaning O'rta Osiyoga qiziqishining iqtisodiy sababi?", "Paxta xomashyosi va bozor", ["Neft", "Oltin konlari faqat", "Dengiz portlari"], "AQSHdagi fuqarolar urushi paxta tanqisligini kuchaytirdi."),
    ],
    "Ko'chirish siyosati va mustamlaka sud tizimi": [
        C(2, "Ko'chirish siyosatining maqsadi?", "Turkistonga rus dehqonlarini joylashtirish", ["Mahalliy aholini Rossiyaga ko'chirish", "Shaharlarni kengaytirish", "Savdogarlarni chiqarib yuborish"], "Eng yaxshi yerlar ko'chmanchilarga berildi."),
        C(3, "Mustamlaka davrida qozilar va biylar qanday tanlangan?", "Saylov orqali, ma'muriyat nazoratida", ["Amir tomonidan tayinlangan", "Meros bo'yicha", "Diniy idora tayinlagan"], "Xalq sudlari saqlanib, nazorat kuchaytirildi."),
    ],
    "Harbiy kommunizm va NEP davrida O'zbekiston": [
        C(2, "NEP qaysi yilda joriy etilgan?", "1921-yilda", ["1917-yilda", "1924-yilda", "1929-yilda"], "Yangi iqtisodiy siyosat."),
        C(3, "Harbiy kommunizmning asosiy belgisi?", "Oziq-ovqat razvyorstkasi", ["Erkin savdo", "Oziq-ovqat solig'i", "Xususiy mulkni rag'batlantirish"], "NEP razvyorstkani oziq-ovqat solig'i bilan almashtirdi."),
    ],
    "Evakuatsiya va etim bolalarni asrab olish": [
        C(2, "Ikkinchi jahon urushi yillarida ko'plab bolani asrab olgan toshkentlik oila?", "Shoahmad Shomahmudov oilasi", ["Nodirabegim oilasi", "Karimovlar oilasi", "Rashidovlar oilasi"], "14 nafar turli millat bolalarini asrab olgan."),
        C(3, "Urush yillarida O'zbekistonga qanday ob'ektlar evakuatsiya qilingan?", "Zavod-fabrikalar, ilmiy va madaniy muassasalar", ["Faqat harbiy qismlar", "Faqat kemalar", "Hech narsa"], "100 dan ortiq korxona ko'chirilgan."),
    ],
    "Urushdan keyingi yillar va Sharof Rashidov davri": [
        C(2, "Sharof Rashidov O'zbekiston KP MK birinchi kotibi bo'lgan davr?", "1959–1983-yillar", ["1937–1950-yillar", "1983–1989-yillar", "1950–1955-yillar"], "24 yil."),
        C(3, "Rashidov davrida respublikada eng ko'p e'tibor qaratilgan soha?", "Paxtachilik", ["Neft sanoati", "Dengiz floti", "Atom energetikasi"], "Paxta yakkahokimligi kuchaydi."),
    ],
    "«Paxta ishi» yoki «O'zbeklar ishi» qatag'onlari": [
        C(2, "«Paxta ishi» qatag'onlari qaysi yillarda avjiga chiqqan?", "1980-yillarda", ["1930-yillarda", "1960-yillarda", "1990-yillarda"], "1983–1989-yillar."),
        C(3, "«Paxta ishi» bilan bog'liq tergov guruhi rahbarlari?", "T. Gdlyan va N. Ivanov", ["N. Yejov va L. Beriya", "M. Frunze va V. Kuybishev", "Y. Andropov va M. Gorbachyov"], "Minglab odamlar asossiz jazolangan."),
    ],
    "Tarix fani, tarixiy manbalar va xronologiya": [
        C(2, "Mil. avv. 300-yil va milodiy 300-yil orasida necha yil o'tgan?", "599 yil", ["600 yil", "300 yil", "601 yil"], "Nolinchi yil yo'q: 300 + 300 − 1."),
        C(3, "XV asr qaysi yillarni o'z ichiga oladi?", "1401–1500-yillar", ["1500–1599-yillar", "1400–1499-yillar", "1501–1600-yillar"], "Asr 1-yildan boshlanadi."),
    ],
    "Yer yuzida ilk odamlarning paydo bo'lishi va evolyutsiyasi": [
        C(2, "«Aqlli odam» ilmiy nomi?", "Homo sapiens", ["Homo habilis", "Homo erectus", "Avstralopitek"], "Zamonaviy odam."),
        C(3, "Ilk odamlarning vatani deb qaysi qit'a hisoblanadi?", "Afrika", ["Yevropa", "Avstraliya", "Amerika"], "Eng qadimgi qoldiqlar Afrikadan."),
    ],
    "Ilk paleolit davri: Selungur va Ko'lbuloq makonlari": [
        C(2, "Selungur g'ori qayerda joylashgan?", "Farg'ona vodiysida (So'x yaqinida)", ["Surxondaryoda", "Xorazmda", "Toshkent yaqinida"], "Ilk paleolit makoni."),
        C(3, "Ko'lbuloq makoni qaysi viloyatda?", "Toshkent viloyatida (Ohangaron vodiysi)", ["Samarqand viloyatida", "Qashqadaryoda", "Namanganda"], "Ko'p qatlamli makon."),
    ],
    "So'nggi paleolit davri: Kromanion odami va urug' jamoasi": [
        C(2, "So'nggi paleolitda qanday jamoa shakllangan?", "Urug'chilik jamoasi", ["Davlat", "Qabila ittifoqi", "Feodal jamoa"], "Qon-qarindoshlikka asoslangan."),
        C(3, "So'nggi paleolit odami qanday ataladi?", "Kromanion odami", ["Neandertal", "Pitekantrop", "Avstralopitek"], "Zamonaviy qiyofadagi odam."),
    ],
    "Mezolit davri: kamon va o'qning ixtiro qilinishi": [
        C(2, "Mezolitning eng muhim ixtirosi?", "Kamon va o'q", ["G'ildirak", "Temir omoch", "Yozuv"], "Ovchilik samaradorligi oshdi."),
        C(3, "Zarautsoy qoya suratlari qaysi davrga oid?", "Mezolit–neolit", ["Bronza", "Temir", "O'rta asrlar"], "Ov manzaralari tasvirlangan."),
    ],
    "Kaltaminor va Joytun madaniyatlari": [
        C(2, "Kaltaminor madaniyati aholisining asosiy mashg'uloti?", "Ovchilik va baliqchilik", ["Faqat dehqonchilik", "Savdo", "Metallurgiya"], "Quyi Amudaryo va Zarafshon havzasida."),
        C(3, "Joytun madaniyati qaysi hududda?", "Janubiy Turkmaniston (Kopetdog' etaklari)", ["Farg'ona vodiysi", "Xorazm", "Toshkent vohasi"], "Ilk dehqonchilik madaniyati."),
    ],
    "Eneolit davri: Zamonbobo va Sarazm yodgorliklari": [
        C(2, "Eneolit — bu qaysi davr?", "Mis-tosh davri", ["Bronza davri", "Temir davri", "Yangi tosh davri"], "Misdan dastlabki buyumlar."),
        C(3, "Zamonbobo yodgorligi qayerda?", "Buxoro viloyatida", ["Farg'onada", "Surxondaryoda", "Toshkentda"], "Eneolit davri manzilgohi."),
    ],
    "Bronza davri: Sopollitepa va Jarqo'ton yodgorliklari": [
        C(2, "Sopollitepa qaysi viloyatda joylashgan?", "Surxondaryo viloyatida", ["Xorazmda", "Andijonda", "Buxoroda"], "Bronza davri dehqonchilik manzilgohi."),
        C(3, "Jarqo'ton qanday yodgorlik?", "Bronza davri ilk shahar tipidagi manzilgoh", ["Temuriylar saroyi", "Buddaviylar ibodatxonasi", "Paleolit g'ori"], "Surxondaryoda."),
    ],
    "Ilk temir davri: ishlab chiqarish kuchlari va ijtimoiy tabaqalanish": [
        C(2, "Temirdan qurollar yasalishi nimaga olib keldi?", "Mehnat unumdorligi oshib, mulkiy tengsizlik kuchaydi", ["Dehqonchilik to'xtadi", "Aholi kamaydi", "Savdo yo'qoldi"], "Ijtimoiy tabaqalanish."),
        C(3, "Farg'ona vodiysidagi ilk temir davri madaniyati?", "Chust madaniyati", ["Kaltaminor", "Joytun", "Sarazm"], "Dalvarzintepa."),
    ],
    "Eng qadimgi davlat birlashmalari: Katta Xorazm": [
        C(2, "«Katta Xorazm» haqida ma'lumot beruvchi qadimgi manbalardan biri?", "«Avesto»", ["«Boburnoma»", "«Temur tuzuklari»", "«Shohnoma» faqat"], "Yunon tarixchilari ham yozgan."),
        C(3, "Qadimgi Xorazm yozuvi qaysi yozuv asosida shakllangan?", "Oromiy yozuvi", ["Lotin yozuvi", "Kirill yozuvi", "Arab yozuvi"], "Mil. avv. IV–III asrlar."),
    ],
    "Qadimgi Baqtriya podsholigi": [
        C(2, "Baqtriya podsholigi asosan qaysi daryo havzasida joylashgan?", "Amudaryoning yuqori oqimi", ["Sirdaryo quyi oqimi", "Zarafshon", "Chirchiq"], "Hozirgi Surxondaryo va Afg'oniston shimoli."),
        C(3, "Baqtriyaning poytaxti?", "Baqtra (Balx)", ["Marokand", "Termiz", "Kat"], "«Shaharlar onasi»."),
    ],
    "Spitamen qo'zg'oloni; Makedonskiy imperiyasining parchalanishi va Salavkiylar": [
        C(2, "Spitamen qaysi bosqinchiga qarshi kurashgan?", "Aleksandr Makedonskiy", ["Kir II", "Doro I", "Chingizxon"], "Mil. avv. 329–327-yillar."),
        C(3, "Makedonskiy vafotidan keyin O'rta Osiyo qaysi davlat tarkibiga kirdi?", "Salavkiylar davlati", ["Kushon davlati", "Ahamoniylar davlati", "Arab xalifaligi"], "Salavk I asos solgan."),
    ],
    "Yunon-Baqtriya podsholigi va ellinistik madaniyat": [
        C(2, "Yunon-Baqtriya podsholigiga asos solgan?", "Diodot", ["Kanishka", "Spitamen", "Bess"], "Mil. avv. III asr o'rtalari."),
        C(3, "Ellinistik madaniyat nima?", "Yunon va Sharq madaniyatlarining qorishuvi", ["Faqat Yunon madaniyati", "Arab madaniyati", "Mo'g'ul madaniyati"], "Makedonskiy yurishlaridan so'ng."),
    ],
    "Qadimgi Davon (Farg'ona) davlati va Davon–Xitoy urushlari": [
        C(2, "Xitoyning Davonga qarshi urush olib borishiga asosiy sabab?", "Davonning zotli («samoviy») otlari", ["Davondagi oltin", "Davonning dengiz porti", "Ipak"], "Mil. avv. 104–101-yillar."),
        C(3, "Davon poytaxti?", "Ershi", ["Kat", "Baqtra", "Marokand"], "Xitoy manbalarida."),
    ],
    "Qang' davlati": [
        C(2, "Qang' davlatining markazi qayerda bo'lgan?", "Sirdaryo o'rta oqimi (Toshkent vohasi)", ["Xorazm", "Surxondaryo", "Farg'ona janubi"], "Mil. avv. III asr – milodiy V asr."),
        C(3, "Qang' davlati poytaxtining nomi?", "Bityan", ["Ershi", "Baqtra", "Kat"], "Xitoy manbalariga ko'ra."),
    ],
    "Kushon imperiyasining tashkil topishi: Kujula Kadfiz va Vima Kadfiz": [
        C(2, "Kushon davlatiga asos solgan hukmdor?", "Kujula Kadfiz", ["Kanishka", "Vima Kadfiz", "Diodot"], "Milodiy I asr."),
        C(3, "Kushonlar qaysi qabila ittifoqidan chiqqan?", "Yuechjilar", ["Eftaliylar", "Xioniylar", "Saklar faqat"], "Toxarlar bilan bog'liq."),
    ],
    "Kanishka I davrida Kushon imperiyasi, buddizm va san'at": [
        C(2, "Kushonlar davrida keng tarqalgan din?", "Buddizm", ["Islom", "Xristianlik", "Iudaizm"], "Kanishka buddizmga homiylik qilgan."),
        C(3, "Termiz yaqinidagi buddaviylik yodgorligi?", "Fayoztepa", ["Afrosiyob", "Tuproqqal'a", "Ko'hna Ark"], "Buddaviy monastir."),
    ],
    "Buyuk Ipak yo'li": [
        C(2, "Buyuk Ipak yo'li qaysi asrda faol shakllangan?", "Mil. avv. II asrda", ["Milodiy X asrda", "XV asrda", "XVIII asrda"], "Chjan Szyan sayohatidan so'ng."),
        C(3, "«Buyuk Ipak yo'li» atamasini fanga kiritgan olim?", "F. Rixtgofen", ["A. Vamberi", "N. Prjevalskiy", "Marko Polo"], "1877-yil."),
    ],
    "Qadimgi Misr": [
        C(2, "Qadimgi Misr hukmdori qanday atalgan?", "Fir'avn", ["Imperator", "Xon", "Shoh"], "Ilohiy hukmdor."),
        C(3, "Misr ierogliflarini o'qishga muvaffaq bo'lgan olim?", "J. F. Shampolyon", ["G. Shliman", "A. Evans", "G. Rolinson"], "Rozetta toshi yordamida, 1822-yil."),
    ],
    "Qadimgi Mesopotamiya (Ikki daryo oralig'i)": [
        C(2, "Mesopotamiya qaysi daryolar oralig'ida?", "Dajla va Frot", ["Nil va Kongo", "Hind va Gang", "Amudaryo va Sirdaryo"], "Hozirgi Iroq hududi."),
        C(3, "Eng qadimgi qonunlar to'plamlaridan biri?", "Hammurapi qonunlari", ["Rim qonunlari", "Temur tuzuklari", "Solon qonunlari"], "Bobil podshosi."),
    ],
    "Qadimgi Hindiston": [
        C(2, "Qadimgi Hindistonda jamiyat qanday guruhlarga bo'lingan?", "Varnalar", ["Gildiyalar", "Polislar", "Ulusalar"], "To'rt varna."),
        C(3, "Buddizm asoschisi?", "Siddxartxa Gautama", ["Konfutsiy", "Zardusht", "Ashoka"], "Mil. avv. VI–V asrlar."),
    ],
    "Qadimgi Xitoy": [
        C(2, "Buyuk Xitoy devori qurilishini qaysi imperator boshlagan (birlashtirgan)?", "Sin Shixuandi", ["Konfutsiy", "Chingizxon", "Lao-szi"], "Mil. avv. III asr."),
        C(3, "Qadimgi Xitoy ixtirolaridan biri?", "Qog'oz", ["Temir yo'l", "Bug' mashinasi", "Telefon"], "Shuningdek kompas, porox, kitob bosish."),
    ],
    "Qadimgi Gretsiya": [
        C(2, "Qadimgi Yunonistondagi shahar-davlatlar?", "Polislar", ["Varnalar", "Nomlar", "Satrapiyalar"], "Afina, Sparta."),
        C(3, "Olimpiya o'yinlari birinchi marta qachon o'tkazilgan?", "Mil. avv. 776-yilda", ["Mil. avv. 490-yilda", "Milodiy 1896-yilda", "Mil. avv. 1000-yilda"], "Zevs sharafiga."),
    ],
    "Qadimgi Rim": [
        C(2, "Rim imperiyasining birinchi imperatori?", "Oktavian Avgust", ["Yuliy Sezar", "Neron", "Konstantin"], "Mil. avv. 27-yil."),
        C(3, "G'arbiy Rim imperiyasi qachon qulagan?", "476-yilda", ["395-yilda", "1453-yilda", "800-yilda"], "Odoakr oxirgi imperatorni taxtdan tushirgan."),
    ],
    "Xionitlar va Kidariylar": [
        C(2, "Xionitlar qaysi asrlarda O'rta Osiyoda hukmronlik qilgan?", "IV asr o'rtalari – V asr", ["I–II asrlar", "VIII–IX asrlar", "XI asr"], "Ko'chmanchi qabilalar."),
        C(3, "Kidariylar davlatiga kim asos solgan?", "Kidara", ["Kanishka", "Bumin", "Vaxshunvar"], "V asr boshlari."),
    ],
    "Eftaliylar davlati": [
        C(2, "Eftaliylar davlati qaysi asrlarda mavjud bo'lgan?", "V–VI asrlarda", ["II–III asrlarda", "IX–X asrlarda", "XIII asrda"], "Taxminan 457–567."),
        C(3, "Eftaliylar qaysi davlatdan o'lpon olgan?", "Sosoniylar Eronidan", ["Rim imperiyasidan", "Arab xalifaligidan", "Xitoydan faqat"], "Kuchli harbiy davlat."),
    ],
    "Turk xoqonligining barpo etilishi": [
        C(2, "Turk xoqonligiga kim asos solgan?", "Bumin xoqon", ["Istami", "Muqanna", "Chingizxon"], "552-yil."),
        C(3, "Turk xoqonligi qaysi yilda ikkiga bo'lingan?", "603-yilda", ["552-yilda", "744-yilda", "568-yilda"], "Sharqiy va G'arbiy xoqonliklar."),
    ],
    "Eftaliylarning parchalanishi: Nemis jangi, Turk–Sosoniy ittifoqi": [
        C(2, "Eftaliylarni qaysi ittifoq yengdi?", "Turk xoqonligi va Sosoniylar", ["Arab va Xitoy", "Rim va Eron", "Mo'g'ul va Xitoy"], "563–567-yillar."),
        C(3, "Turklar tomonidan Eftaliylarga qarshi qo'shinni boshqargan?", "Istami", ["Bumin", "Tardu", "Muqanna"], "G'arbiy yerlar hukmdori."),
    ],
    "G'arbiy Turk xoqonligi": [
        C(2, "G'arbiy Turk xoqonligining markazi?", "Yettisuv (Suyob)", ["Samarqand", "Xorazm", "Termiz"], "Qorasuv atrofi."),
        C(3, "G'arbiy Turk xoqonligi gullagan davrdagi xoqon?", "Tun yabg'u xoqon", ["Bumin", "Kul tegin", "Bilga xoqon"], "VII asr boshlari."),
    ],
    "Arab xalifaligining vujudga kelishi": [
        C(2, "Arab xalifaligining poytaxti Umaviylar davrida?", "Damashq", ["Bag'dod", "Makka", "Qohira"], "661–750."),
        C(3, "Abbosiylar poytaxti?", "Bag'dod", ["Damashq", "Madina", "Kufa"], "762-yilda asos solingan."),
    ],
    "Sharik ibn Shayx qo'zg'oloni": [
        C(2, "Sharik ibn Shayx qo'zg'oloni qachon bo'lgan?", "750-yilda", ["776-yilda", "806-yilda", "720-yilda"], "Buxoroda."),
        C(3, "Sharik qo'zg'olonini kim bostirgan?", "Abu Muslim", ["Qutayba ibn Muslim", "Rafi ibn Lays", "Muqanna"], "Ziyod ibn Solih qo'shini bilan."),
    ],
    "Rafi ibn Lays qo'zg'oloni": [
        C(2, "Rafi ibn Lays qo'zg'oloni qaysi yillarda bo'lgan?", "806–810-yillarda", ["750–751-yillarda", "776–783-yillarda", "720–722-yillarda"], "Samarqandda boshlangan."),
        C(3, "Rafi ibn Lays qo'zg'oloni bostirilishida qatnashgan aka-uka (keyinchalik Somoniylar)?", "Nuh, Ahmad, Yahyo va Ilyos", ["Ismoil va Nasr", "Tohir va Talha", "Ya'qub va Amr"], "Asad ibn Somonxudotning o'g'illari."),
    ],
    "Tohiriylar va Safforiylar davlatlari": [
        C(2, "Tohiriylar davlatining poytaxti?", "Nishopur", ["Buxoro", "Samarqand", "Marv"], "821–873."),
        C(3, "Safforiylar sulolasiga kim asos solgan?", "Ya'qub ibn Lays", ["Tohir ibn Husayn", "Ismoil Somoniy", "Alp Tegin"], "Seistondan chiqqan."),
    ],
    "Qoraxoniylar davlatining barpo etilishi": [
        C(2, "Qoraxoniylar Buxoroni qachon egallagan?", "999-yilda", ["840-yilda", "1040-yilda", "1141-yilda"], "Somoniylar davlati tugatildi."),
        C(3, "Islomni qabul qilgan ilk Qoraxoniy hukmdor?", "Sotuq Bug'raxon", ["Nasr Elakxon", "Arslonxon", "Ibrohim Tamg'achxon"], "X asr."),
    ],
    "Saljuqiylar imperiyasi va Dandanaqan jangi (1040)": [
        C(2, "Dandanaqan jangida kim mag'lub bo'ldi?", "G'aznaviylar (Mas'ud)", ["Saljuqiylar", "Qoraxoniylar", "Somoniylar"], "1040-yil."),
        C(3, "Saljuqiylar davlatiga asos solgan aka-uka?", "To'g'rulbek va Chag'ribek", ["Alp Tegin va Sabuktegin", "Nuh va Ahmad", "Kujula va Vima"], "Saljuq nevaralari."),
    ],
    "O'tror fojeasi (1218) va uning oqibatlari": [
        C(2, "O'tror fojeasi kimning buyrug'i bilan sodir bo'lgan?", "O'tror hokimi Inolchiq (G'oyirxon)", ["Chingizxon", "Jaloliddin", "Temur Malik"], "Mo'g'ul savdo karvoni qirib tashlangan."),
        C(3, "O'tror mudofaasi qancha davom etgan?", "Taxminan 5 oy", ["3 kun", "2 yil", "1 hafta"], "1219–1220-yillar."),
    ],
    "Gurganj mudofaasi va Najmiddin Kubro": [
        C(2, "Najmiddin Kubro qaysi tariqat asoschisi?", "Kubraviya", ["Naqshbandiya", "Yassaviya", "Qodiriya"], "Gurganj mudofaasida shahid bo'lgan."),
        C(3, "Gurganj mo'g'ullar tomonidan qachon egallangan?", "1221-yilda", ["1219-yilda", "1238-yilda", "1370-yilda"], "7 oylik mudofaadan so'ng."),
    ],
    "Jaloliddin Manguberdi: Parvon, Sind daryosi va so'nggi yillari": [
        C(2, "Jaloliddin mo'g'ullarni qaysi jangda yengan?", "Parvon jangida", ["Sind daryosi bo'yida", "Anqara jangida", "Dandanaqan jangida"], "1221-yil."),
        C(3, "Jaloliddin Manguberdi qachon vafot etgan?", "1231-yilda", ["1221-yilda", "1240-yilda", "1219-yilda"], "Kurd tog'larida."),
    ],
    "1370-yil Balx qurultoyi": [
        C(2, "1370-yil Balx qurultoyida kim oliy hukmdor deb e'lon qilindi?", "Amir Temur", ["Amir Husayn", "Shohruh", "To'xtamish"], "Movarounnahr hukmdori."),
        C(3, "Amir Temur o'z davlatining poytaxti qilib qaysi shaharni tanladi?", "Samarqand", ["Shahrisabz", "Hirot", "Buxoro"], "1370-yil."),
    ],
    "Oltin O'rda xoni To'xtamishga qarshi urushlar": [
        C(2, "Amir Temur To'xtamishni Terek daryosi bo'yida qachon tor-mor etdi?", "1395-yilda", ["1391-yilda", "1402-yilda", "1370-yilda"], "Oltin O'rda kuchsizlandi."),
        C(3, "Qunduzcha jangi qaysi yilda bo'lgan?", "1391-yilda", ["1395-yilda", "1388-yilda", "1405-yilda"], "To'xtamishga qarshi."),
    ],
    "Abdullaxon II davrida markaziy hokimiyatning mustahkamlanishi": [
        C(2, "Abdullaxon II qachon xon deb e'lon qilingan?", "1583-yilda", ["1501-yilda", "1601-yilda", "1533-yilda"], "Otasi Iskandarxon vafotidan so'ng."),
        C(3, "Abdullaxon II davrida o'tkazilgan pul islohoti?", "Kumush va mis tangalarni yagona tizimga keltirish", ["Qog'oz pul chiqarish", "Oltin tangalarni bekor qilish", "Xitoy pulini joriy etish"], "Savdo rivojlandi."),
    ],
    "Buxoro amirligi va Mang'itlar sulolasi": [
        C(2, "Mang'itlar sulolasiga asos solgan?", "Muhammad Rahimbiy", ["Shohmurod", "Amir Haydar", "Abdullaxon"], "1756-yil."),
        C(3, "Buxoro xonligi qachondan amirlik deb atala boshlagan?", "Mang'itlar davridan (XVIII asr oxiri)", ["Shayboniylar davridan", "Ashtarxoniylar davridan", "Somoniylar davridan"], "Shohmurod «amir» unvonini olgan."),
    ],
    "Qo'qon xonligining tashkil topishi: Shohruhbiy va Minglar": [
        C(2, "Qo'qon xonligiga kim asos solgan?", "Shohruhbiy", ["Olimxon", "Umarxon", "Xudoyorxon"], "1709-yil."),
        C(3, "Qo'qon xonligida hukmronlik qilgan sulola?", "Minglar", ["Mang'itlar", "Qo'ng'irotlar", "Arabshohiylar"], "O'zbek urug'i."),
    ],
    "Turkistonda jadidchilik harakatining vujudga kelishi": [
        C(2, "Jadidchilik harakatining asosiy maqsadi?", "Ma'rifat, yangi usul maktablari va milliy taraqqiyot", ["Qurolli qo'zg'olon", "Diniy urush", "Savdoni taqiqlash"], "XIX asr oxiri – XX asr boshi."),
        C(3, "Yangi usul (usuli jadid) maktablariga Qrimda asos solgan?", "Ismoilbek Gaspirali", ["Behbudiy", "Munavvarqori", "Fitrat"], "«Tarjimon» gazetasi."),
    ],
    "1916-yil umumturkiston qo'zg'oloni": [
        C(2, "1916-yil qo'zg'olonining bevosita sababi?", "Mahalliy aholini mardikorlikka (front orti ishlariga) olish to'g'risidagi farmon", ["Paxta narxi tushishi", "Temir yo'l qurilishi", "Yer solig'i bekor qilinishi"], "25-iyun farmoni."),
        C(3, "1916-yil qo'zg'oloni birinchi bo'lib qayerda boshlangan?", "Xo'jandda", ["Toshkentda", "Jizzaxda", "Andijonda"], "4-iyul."),
    ],
    "1924-yilgi milliy-davlat chegaralanishi va O'zbekiston SSR": [
        C(2, "O'zbekiston SSR qachon tashkil topgan?", "1924-yil 27-oktyabrda", ["1917-yilda", "1929-yilda", "1991-yilda"], "Milliy-davlat chegaralanishi natijasida."),
        C(3, "O'zbekiston SSR ning birinchi poytaxti?", "Samarqand", ["Toshkent", "Buxoro", "Qo'qon"], "1930-yilgacha."),
    ],
    "Toshkent zilzilasi (1966) va qayta tiklash": [
        C(2, "Toshkent zilzilasi qachon sodir bo'lgan?", "1966-yil 26-aprelda", ["1946-yilda", "1976-yilda", "1956-yilda"], "Shahar markazi vayron bo'ldi."),
        C(3, "Zilziladan keyin shaharni tiklashda qatnashganlar?", "Butun ittifoq respublikalari quruvchilari", ["Faqat toshkentliklar", "Chet el davlatlari faqat", "Hech kim"], "Qisqa muddatda yangi mavzelar qurildi."),
    ],
    "Konstitutsiyaning qabul qilinishi (1992)": [
        C(2, "O'zbekiston Respublikasi Konstitutsiyasi qachon qabul qilingan?", "1992-yil 8-dekabrda", ["1991-yil 31-avgustda", "1992-yil 1-sentabrda", "1993-yil 8-dekabrda"], "XII chaqiriq Oliy Kengashning XI sessiyasida."),
        C(3, "1992-yil Konstitutsiyasi nechta moddadan iborat edi?", "128", ["155", "100", "200"], "6 bo'lim, 26 bob."),
    ],
    "2023-yil referendumi va yangi tahrirdagi Konstitutsiya": [
        C(2, "Yangi tahrirdagi Konstitutsiya bo'yicha referendum qachon o'tkazildi?", "2023-yil 30-aprelda", ["2022-yil 8-dekabrda", "2023-yil 1-mayda", "2021-yil 24-oktyabrda"], "Umumxalq referendumi."),
        C(3, "Yangi tahrirdagi Konstitutsiya nechta moddadan iborat?", "155", ["128", "200", "100"], "Moddalar soni oshdi."),
    ],
}


def extend(packs: list) -> int:
    from .gen_v242 import _add
    added = 0
    banks = {"native": NATIVE, "history": HIST}
    for pack in packs:
        subj = pack.get("subject")
        if subj == "english" and pack.get("modes") != ["ielts"]:
            added += _add(pack, ENG)
        elif subj in banks:
            added += _add(pack, banks[subj])
    return added
