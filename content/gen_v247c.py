"""v247: TARIX — 10 tadan kam savolli mavzularga yangi savollar (DTM 2026 / milliy sertifikat uslubi).
Faqat darsliklarda aniq qayd etilgan faktlar olingan."""
from __future__ import annotations

from ._dsl import C

HIST: dict[str, list] = {
    "6.1.1-2": [
        C(1, "Arxeologik qazishmalarda topilgan qurol va idishlar qanday tarixiy manba?", "Moddiy manba", ["Yozma manba", "Og'zaki manba", "Etnografik manba"], "Insoniyat yaratgan buyumlar — moddiy manba."),
        C(1, "Bir asr necha yilga teng?", "100 yil", ["10 yil", "1000 yil", "50 yil"], "Ming yillik — 1000 yil."),
    ],
    "6.1.3": [
        C(2, "Eng qadimgi odam qoldiqlari topilgan Olduvay darasi qaysi qit'ada joylashgan?", "Afrika", ["Osiyo", "Yevropa", "Avstraliya"], "Olduvay darasi Tanzaniyada."),
        C(2, "«Mohir odam»ning ilmiy nomi?", "Homo habilis", ["Homo erectus", "Homo sapiens", "Neandertal"], "Ilk mehnat qurollarini yasagan."),
    ],
    "6.1.5": [
        C(2, "Teshiktosh g'orini 1938-yilda topgan arxeolog?", "A. P. Okladnikov", ["M. M. Gerasimov", "S. P. Tolstov", "Ya. G'. G'ulomov"], "Okladnikov Boysun tog'idagi g'orni o'rgangan."),
        C(2, "Neandertallarda dafn marosimi bo'lganini qaysi topilma tasdiqlaydi?", "Teshiktosh bolasi atrofidagi tog' echkisi shoxlari", ["Zarautsoy qoya suratlari", "Afrosiyob devoriy rasmlari", "Tuproqqal'a arxivi"], "Shoxlar qabr atrofiga terib qo'yilgan."),
    ],
    "6.1.6": [
        C(2, "Samarqand shahri hududida topilgan so'nggi paleolit davri yodgorligi?", "Samarqand makoni", ["Teshiktosh", "Machay", "Kaltaminor"], "Siyob bo'yidagi qadimiy manzilgoh."),
        C(2, "So'nggi paleolitda odamlar qanday yangi turarjoylar qura boshlagan?", "Yerto'la va chaylalar", ["Ko'p qavatli uylar", "Qal'alar", "Faqat g'orlarda yashagan"], "Ochiq joylarda ham manzilgohlar paydo bo'lgan."),
    ],
    "6.1.7": [
        C(2, "Mezolit davri taxminan qachon bo'lgan?", "Bundan 12–7 ming yil avval", ["40–12 ming yil avval", "Mil. avv. I ming yillikda", "Milodiy I asrda"], "Paleolit va neolit oralig'idagi davr."),
    ],
    "6.1.8": [
        C(2, "O'rta Osiyoda neolit davri taxminan qachon bo'lgan?", "Mil. avv. VI–IV ming yilliklarda", ["40–12 ming yil avval", "Mil. avv. I ming yillikda", "Milodiy V asrda"], "Yangi tosh davri."),
        C(1, "Dehqonchilikka o'tish natijasida odamlar qanday hayot tarziga o'tdi?", "O'troq hayot", ["Ko'chmanchi hayot", "Faqat ovchilik", "G'orlarda yashash"], "Ekin maydonlari yonida doimiy manzilgohlar paydo bo'ldi."),
    ],
    "6.1.9": [
        C(2, "Joytun madaniyati aholisi qanday uylarda yashagan?", "Xom g'ishtdan qurilgan uylarda", ["Qamish kulbalarda", "G'orlarda", "O'tovlarda"], "Ilk dehqonchilik manzilgohi."),
        C(1, "Joytun madaniyati qaysi davrga mansub?", "Neolit", ["Paleolit", "Bronza", "Temir"], "Yangi tosh davri."),
    ],
    "6.1.10": [
        C(2, "Sarazm yodgorligi hozirgi qaysi davlat hududida?", "Tojikiston", ["O'zbekiston", "Turkmaniston", "Qirg'iziston"], "Panjikent yaqinida, Zarafshon bo'yida."),
        C(1, "Eneolitdan keyin qaysi davr boshlangan?", "Bronza davri", ["Neolit", "Mezolit", "Paleolit"], "Tosh → mis-tosh → bronza → temir."),
    ],
    "6.1.12": [
        C(2, "Farg'ona vodiysidagi bronza davri oxiri – ilk temir davri madaniyati?", "Chust madaniyati", ["Kaltaminor", "Joytun", "Zamonbobo"], "Dalvarzin va Chust manzilgohlari."),
        C(2, "Ilk temir davrida paydo bo'lgan, mudofaa devorlari bilan o'ralgan aholi manzillari?", "Qal'alar va ilk shaharlar", ["G'orlar", "Yerto'lalar", "Qamish kulbalar"], "Ijtimoiy tabaqalanish va davlatchilik kurtaklari."),
    ],
    "6.1.13": [
        C(1, "Qadimgi Xorazm hududi hozirgi qaysi hududlarga to'g'ri keladi?", "Xorazm viloyati va Qoraqalpog'iston", ["Farg'ona vodiysi", "Surxondaryo", "Toshkent viloyati"], "Amudaryoning quyi oqimi."),
        C(2, "«Katta Xorazm» haqida ilk ma'lumot bergan yunon olimlari?", "Gekatey va Gerodot", ["Platon va Aristotel", "Pifagor va Fales", "Arrian va Plutarx"], "Yunon manbalari asosida."),
    ],
    "6.1.14": [
        C(2, "Baqtriya haqida ma'lumot beruvchi qadimgi muqaddas kitob?", "«Avesto»", ["«Qur'on»", "«Mahabharata»", "«Iliada»"], "«Avesto»da Baqtriya «Baxdi» deb atalgan."),
        C(2, "Ahamoniylarning Baqtriya satrapi bo'lib, Iskandarga qarshi chiqqan?", "Bess", ["Spitamen", "Doro I", "Kir II"], "Bess o'zini shoh deb e'lon qilgan."),
    ],
    "6.1.21": [
        C(2, "Yunon-Baqtriya podsholaridan biri?", "Yevtidem", ["Kanishka", "Kujula Kadfiz", "Bumin"], "Diodotlardan keyin taxtni egallagan."),
        C(2, "Yunon-Baqtriya podsholigi qaysi asrda qulagan?", "Mil. avv. II asrda", ["Milodiy V asrda", "Mil. avv. VI asrda", "Milodiy X asrda"], "Shimoldan kelgan ko'chmanchilar zarbasi bilan."),
    ],
    "6.1.22-23": [
        C(2, "Xitoy manbalariga ko'ra Davonda nechtaga yaqin shahar bo'lgan?", "70 ga yaqin", ["5 ta", "1000 dan ortiq", "2 ta"], "«Shiji» yilnomasida qayd etilgan."),
        C(2, "Davonda qaysi xo'jalik tarmoqlari rivojlangan?", "Dehqonchilik, bog'dorchilik va yilqichilik", ["Faqat baliqchilik", "Faqat ovchilik", "Kemasozlik"], "Uzumchilik va zotli otlar mashhur bo'lgan."),
    ],
    "6.1.24": [
        C(2, "Qang' davlati haqida asosiy ma'lumot beruvchi manbalar?", "Xitoy yilnomalari", ["Arab geograflari asarlari", "Rus yilnomalari", "Yunon dramalari"], "Xitoy elchilari ma'lumotlari."),
        C(2, "Qang' davlati qaysi davrda mavjud bo'lgan?", "Mil. avv. III asr – milodiy V asr", ["Milodiy X–XII asrlar", "Mil. avv. VII–VI asrlar", "XIV–XV asrlar"], "Sirdaryo o'rta oqimidagi davlat."),
    ],
    "6.1.25": [
        C(2, "Kushon podsholigi qaysi asrda tashkil topgan?", "Milodiy I asrda", ["Mil. avv. VI asrda", "Milodiy VI asrda", "Milodiy X asrda"], "Kujula Kadfiz tomonidan."),
        C(1, "Kushonlar davrida O'rta Osiyodan o'tgan xalqaro savdo yo'li?", "Buyuk Ipak yo'li", ["Qahrabo yo'li", "Choy yo'li", "Dengiz yo'li"], "Xitoydan O'rta yer dengizigacha."),
    ],
    "6.1.26": [
        C(2, "Surxondaryodagi kushon davri shahar xarobasi, oltin xazinasi bilan mashhur?", "Dalvarzintepa", ["Afrosiyob", "Tuproqqal'a", "Varaxsha"], "1972-yilda oltin buyumlar xazinasi topilgan."),
        C(2, "Kushon imperiyasi taxminan qachon inqirozga yuz tutgan?", "Milodiy III asrda", ["Mil. avv. III asrda", "Milodiy VII asrda", "Milodiy X asrda"], "Sosoniylar hujumlari natijasida."),
    ],
    "6.1.27": [
        C(2, "Afrig'iylar davrida Xorazmning poytaxti bo'lgan shahar?", "Kat", ["Buxoro", "Samarqand", "Termiz"], "Amudaryoning o'ng sohilida joylashgan."),
        C(2, "Xorazm afrig'iylari haqida ma'lumot qoldirgan buyuk olim?", "Abu Rayhon Beruniy", ["Ibn Sino", "Forobiy", "Al-Xorazmiy"], "«Qadimgi xalqlardan qolgan yodgorliklar» asarida."),
    ],
    "6.1.29": [
        C(1, "Qadimgi Misrda marhumlar jasadini saqlash usuli?", "Mumiyolash", ["Kuydirish", "Suvga tashlash", "Tuzlash"], "Ruh qaytadi degan e'tiqod bilan bog'liq."),
        C(2, "Qadimgi Misrning quyosh xudosi?", "Ra", ["Zevs", "Marduk", "Yupiter"], "Misrliklarning bosh xudosi."),
    ],
    "6.1.30": [
        C(2, "Ossuriya davlatining poytaxti bo'lgan shahar?", "Ninevia", ["Bobil", "Ur", "Memfis"], "Ashshurbanipal kutubxonasi shu yerda bo'lgan."),
        C(2, "Shumerlarning eng qadimgi shaharlaridan biri?", "Ur", ["Afina", "Rim", "Karfagen"], "Frot daryosi bo'yida."),
    ],
    "6.1.31": [
        C(2, "Buddizm qaysi davrda vujudga kelgan?", "Mil. avv. VI–V asrlarda", ["Milodiy I asrda", "Mil. avv. II ming yillikda", "Milodiy V asrda"], "Siddxartxa Gautama ta'limoti."),
        C(1, "Qadimgi hindlarning muqaddas kitoblari?", "Vedalar", ["«Avesto»", "Tavrot", "«Iliada»"], "Eng qadimgisi — «Rigveda»."),
    ],
    "6.1.32": [
        C(2, "Konfutsiy qaysi davrda yashagan?", "Mil. avv. VI–V asrlarda", ["Milodiy X asrda", "Mil. avv. III ming yillikda", "Milodiy XV asrda"], "Mil. avv. 551–479-yillar."),
        C(1, "Xitoydan G'arbga ipak olib boruvchi savdo yo'li?", "Buyuk Ipak yo'li", ["Qirol yo'li", "Appiy yo'li", "Qahrabo yo'li"], "Mil. avv. II asrda shakllangan."),
    ],
    "6.1.33": [
        C(2, "Aleksandr Makedonskiyning ustozi bo'lgan faylasuf?", "Aristotel", ["Platon", "Suqrot", "Gomer"], "Aristotel shahzodaga ta'lim bergan."),
        C(2, "Spartada tarbiyada asosiy e'tibor nimaga qaratilgan?", "Harbiy tayyorgarlikka", ["Savdoga", "Falsafaga", "Dengizchilikka"], "Sparta — harbiy polis."),
    ],
    "6.1.34": [
        C(2, "Rim respublikasida eng yuqori mansabdor shaxslar?", "Konsullar", ["Fir'avnlar", "Arxontlar", "Xoqonlar"], "Har yili ikki konsul saylangan."),
        C(2, "Yuliy Sezar qaysi yili o'ldirilgan?", "Mil. avv. 44-yilda", ["Mil. avv. 509-yilda", "Milodiy 476-yilda", "Mil. avv. 753-yilda"], "Senatdagi fitna natijasida."),
    ],
    "7.1.1": [
        C(2, "V–VIII asrlarda Ustrushona hukmdorlarining qarorgohi bo'lgan shahar?", "Bunjikat", ["Panjikent", "Afrosiyob", "Varaxsha"], "Hozirgi Shahriston yaqinida."),
        C(2, "V–VIII asrlarda erkin jamoachi dehqonlar qanday atalgan?", "Kashovarzlar", ["Chokarlar", "Kadivarlar", "Ixshidlar"], "Kichik yer egalari."),
    ],
    "7.1.2": [
        C(1, "Xionitlar, kidariylar va eftaliylar asosan qanday xo'jalik bilan shug'ullangan?", "Ko'chmanchi chorvachilik", ["Baliqchilik", "Kemasozlik", "Faqat dehqonchilik"], "Ko'chmanchi chorvador qabilalar."),
        C(3, "Xionitlar qaysi Sosoniy shohi bilan ittifoqda Rimga qarshi Amida qamalida qatnashgan (359-yil)?", "Shopur II", ["Xusrav I", "Peroz", "Yazdigard III"], "Xionitlar podshosi Grumbat boshchiligida."),
    ],
    "7.1.3": [
        C(2, "484-yildagi g'alabadan keyin eftaliylar qaysi davlatdan o'lpon olgan?", "Sosoniylar Eroni", ["Rim imperiyasi", "Xitoy Tan imperiyasi", "Arab xalifaligi"], "Sosoniylar uzoq vaqt o'lpon to'lagan."),
        C(2, "Eftaliylar hukmdori sifatida tarixda tilga olinadigan, Sosoniylarni yenggan podsho?", "Vaxshunvar (Axshunvar)", ["Bumin", "Kidara", "Divashtich"], "484-yilda shoh Perozni yenggan."),
    ],
    "7.1.4": [
        C(2, "Turk xoqonligi qaysi davlatga qaram bo'lib, undan ozod bo'lgan?", "Jujanlar (Avarlar) xoqonligi", ["Eftaliylar", "Xitoy", "Sosoniylar"], "552-yilda jujanlar tor-mor etilgan."),
        C(2, "Qadimgi turkiy (Orxon-Enasoy) yozuvi qanday nom bilan ham ataladi?", "Run yozuvi", ["Mixxat", "Ieroglif", "Lotin yozuvi"], "Skandinaviya runlariga o'xshashligi uchun."),
    ],
    "7.1.5": [
        C(2, "Turk xoqonligi bilan ittifoq tuzgan Sosoniy shohi?", "Xusrav I Anushirvon", ["Peroz", "Shopur II", "Yazdigard III"], "Eftaliylarga qarshi ittifoq."),
        C(2, "Turk–Sosoniy ittifoqi eftaliylarni taxminan qachon tor-mor etdi?", "563–567-yillarda", ["484-yilda", "751-yilda", "999-yilda"], "Eftaliylar yerlari ikki davlat o'rtasida bo'lindi."),
    ],
    "7.1.6": [
        C(2, "630-yildan keyin G'arbiy Turk xoqonligini zaiflashtirgan voqea?", "Tong yabg'uning o'ldirilishi va ichki nizolar", ["Arab istilosining tugashi", "Mo'g'ul bosqini", "Rus istilosi"], "Taxt uchun kurash boshlangan."),
        C(3, "630-yilda Suyobda Tong yabg'u xoqon huzurida bo'lgan xitoy rohib-sayyohi?", "Syuan Szan", ["Chjan Szyan", "Li Guangli", "Fa Syan"], "Hindistonga buddaviy kitoblar uchun borayotgan edi."),
    ],
    "7.1.7": [
        C(1, "Panjikent qaysi daryo bo'yida joylashgan qadimiy So'g'd shahri?", "Zarafshon", ["Amudaryo", "Sirdaryo", "Chirchiq"], "Hozirgi Tojikiston hududida."),
        C(2, "V–VIII asrlarda qal'a-qasrlar asosan qanday materialdan qurilgan?", "Paxsa va xom g'isht", ["Marmar", "Temir-beton", "Granit"], "Mahalliy qurilish materiallari."),
    ],
    "7.1.8": [
        C(1, "Islom dini qaysi asrda vujudga kelgan?", "VII asrda", ["V asrda", "IX asrda", "III asrda"], "Arabiston yarimorolida."),
        C(2, "Movarounnahrni bosib olishda faol qatnashgan arab sarkardasi?", "Qutayba ibn Muslim", ["Abu Muslim", "Muqanna", "Ismoil Somoniy"], "705–715-yillarda Xuroson noibi."),
    ],
    "7.1.11": [
        C(1, "Mug' qal'asi hozirgi qaysi davlat hududida?", "Tojikiston", ["O'zbekiston", "Qozog'iston", "Turkmaniston"], "Zarafshon yuqori oqimida."),
        C(3, "722-yilda Divashtichni qatl ettirgan arab noibi?", "Said al-Haroshiy", ["Qutayba ibn Muslim", "Abu Muslim", "Nasr ibn Sayyor"], "Xuroson noibi."),
    ],
    "7.1.12": [
        C(1, "Sharik ibn Shayx qo'zg'oloni qanday yakunlandi?", "Bostirildi", ["G'alaba qozondi", "Xalifalik tugatildi", "Somoniylar davlati tuzildi"], "Abu Muslim qo'shinlari tomonidan."),
        C(3, "Sharik ibn Shayx tarafdorlari qaysi oqim vakillari edi?", "Shia (alaviylar tarafdorlari)", ["Xorijiylar", "Buddaviylar", "Nasroniylar"], "Hokimiyat Ali avlodlariga o'tishini talab qilgan."),
    ],
    "7.1.14": [
        C(3, "Rofe ibn Lays kimning nabirasi edi?", "Nasr ibn Sayyor (Xuroson noibi)", ["Abu Muslim", "Qutayba ibn Muslim", "Muqanna"], "Umaviylarning so'nggi Xuroson noibi."),
        C(2, "Rofe qo'zg'oloni bostirilgandan so'ng kuchaygan sulola?", "Somoniylar", ["Qoraxoniylar", "G'aznaviylar", "Saljuqiylar"], "Somonxudot nabiralari viloyatlarni boshqara boshladi."),
    ],
    "7.1.15": [
        C(1, "Xiroj qanday soliq turi?", "Yer solig'i", ["Jon solig'i", "Bojxona solig'i", "Uy solig'i"], "Hosilning bir qismi olingan."),
        C(2, "Jizya to'lashdan kimlar ozod qilingan?", "Islomni qabul qilganlar", ["Dehqonlar", "Hunarmandlar", "Savdogarlar"], "Jizya — musulmon bo'lmaganlardan olinadigan jon solig'i."),
    ],
    "7.1.20": [
        C(2, "Somoniylarda pochta va aloqa xizmati devoni?", "Devoni barid", ["Devoni mustavfiy", "Devoni qozi", "Devoni muhtasib"], "Chopar va xabarlar xizmati."),
        C(1, "Somoniylar davlatining poytaxti?", "Buxoro", ["Samarqand", "Marv", "Urganch"], "Ismoil Somoniy davridan."),
        C(2, "Somoniylarda bozorlar, o'lchov va tarozilarni nazorat qiluvchi devon?", "Devoni muhtasib", ["Devoni barid", "Devoni vazir", "Devoni jandar"], "Muhtasib — jamoat tartibi nazoratchisi."),
    ],
    "7.1.21": [
        C(2, "Somoniylar davrida zarb etilgan mis tangalar qanday atalgan?", "Fals (pul)", ["Dirham", "Dinor", "Tilla"], "Mayda savdoda ishlatilgan."),
        C(2, "Somoniylar davrida zarb etilgan oltin tanga?", "Dinor", ["Fals", "Dirham", "Pul"], "Kumush — dirham, mis — fals."),
        C(1, "Ismoil Somoniy maqbarasi qaysi shaharda?", "Buxoro", ["Samarqand", "Termiz", "Xiva"], "IX–X asrlar me'moriy yodgorligi."),
    ],
    "7.1.22": [
        C(2, "Qoraxoniylar davlati asosan qaysi qabila ittifoqlari asosida tuzilgan?", "Qarluq, yag'mo, chigil", ["Qipchoq, nayman", "Mang'it, qo'ng'irot", "O'g'uz, saljuq"], "Yettisuv va Sharqiy Turkiston qabilalari."),
        C(2, "Satuq Bug'roxon islomni qaysi asrda qabul qilgan?", "X asrda", ["VIII asrda", "XII asrda", "VI asrda"], "Qoraxoniylardan birinchi musulmon hukmdor."),
    ],
    "7.1.24": [
        C(2, "G'arbiy Qoraxoniylar davlatining poytaxti?", "Samarqand", ["Qashg'ar", "Balasog'un", "O'zgan"], "Movarounnahr markazi."),
        C(2, "Sharqiy Qoraxoniylar davlatining markazi?", "Qashg'ar", ["Samarqand", "Buxoro", "Xiva"], "Sharqiy Turkiston."),
    ],
    "8.1.3": [
        C(2, "Qoraxitoylar asli qaysi xalq edi?", "Kidanlar", ["Arablar", "Turkmanlar", "Ruslar"], "Shimoliy Xitoydan g'arbga ko'chgan kidan qabilalari."),
        C(3, "1153-yilda Sulton Sanjarni asirga olgan qabilalar?", "O'g'uzlar", ["Qoraxitoylar", "Mo'g'ullar", "Xorazmshohlar"], "Sanjar uch yil asirlikda bo'lgan."),
    ],
    "8.1.4": [
        C(2, "Anushteginiylar Xorazmda qanday unvon bilan hukmronlik qilgan?", "Xorazmshoh", ["Xoqon", "Ixshid", "Afshin"], "Qadimiy Xorazm hukmdorlari unvoni."),
        C(2, "Xorazmshohlar davlati eng kuchaygan davrdagi hukmdor?", "Alouddin Muhammad", ["Atsiz", "Il-Arslon", "Qutbiddin Muhammad"], "1200–1220-yillar."),
    ],
    "8.1.5": [
        C(2, "Atsiz davrida Xorazmning poytaxti?", "Gurganj (Urganch)", ["Buxoro", "Marv", "Samarqand"], "Xorazmshohlar poytaxti."),
        C(3, "Rashididdin Vatvot qaysi asar muallifi?", "«Hadoyiq us-sehr»", ["«Qutadg'u bilig»", "«Shohnoma»", "«Devonu lug'otit turk»"], "She'riy san'atlar haqidagi asar."),
    ],
    "8.1.11-12": [
        C(2, "1225-yildan Jaloliddin Manguberdi qaysi hududda davlatini tiklab, kurashni davom ettirdi?", "Ozarbayjon va Kavkaz (markazi Tabriz)", ["Xitoy", "Hindiston janubi", "Rus yerlari"], "Tabrizni poytaxt qilgan."),
        C(3, "Jaloliddin Manguberdi qayerda halok bo'lgan?", "Kurdiston tog'larida (Mayyafariqin yaqinida)", ["Pomir tog'larida", "Tyan-Shan tog'larida", "Hindiqush tog'larida"], "1231-yilda."),
    ],
    "8.1.13": [
        C(2, "Chig'atoy ulusining markazi bo'lgan shahar?", "Olmaliq (Ili vodiysi)", ["Samarqand", "Qoraqurum", "Saroy"], "Yettisuvda joylashgan."),
        C(2, "Kebekxon qanday islohot bilan mashhur?", "Pul va ma'muriy islohot", ["Yozuv islohoti", "Harbiy flot yaratish", "Diniy islohot"], "Kumush «kebek dinor»lari zarb etilgan."),
    ],
    "8.1.16": [
        C(2, "Amir Qozog'on o'ldirilgandan keyin hokimiyatni egallagan o'g'li?", "Abdulla", ["Husayn", "Temur", "Bayon Sulduz"], "Ko'p o'tmay hokimiyatdan ag'darilgan."),
        C(2, "Samarqanddagi sarbadorlar harakati qaysi yilda bo'lgan?", "1365-yilda", ["1370-yilda", "1346-yilda", "1405-yilda"], "Mo'g'ullarga qarshi shahar mudofaasi."),
    ],
    "8.1.20": [
        C(1, "Amir Temur qaysi yili Movarounnahr hukmdori deb e'lon qilindi?", "1370", ["1360", "1405", "1336"], "Balx qurultoyida."),
        C(1, "Amir Temur davlatining poytaxti?", "Samarqand", ["Shahrisabz", "Hirot", "Buxoro"], "Temur Samarqandni bunyod etgan."),
    ],
    "8.1.21": [
        C(2, "Amir Temur 1395-yilgi yurishida qaysi Oltin O'rda poytaxtini vayron qildi?", "Saroy Berka", ["Moskva", "Qozon", "Kiyev"], "Oltin O'rdaning qudrati sindirildi."),
    ],
    "8.1.28": [
        C(1, "Sulton Abu Said Mirzo qaysi sulola vakili?", "Temuriylar", ["Shayboniylar", "Qoraxoniylar", "Ashtarxoniylar"], "Mironshoh avlodidan."),
        C(1, "Husayn Boyqaro davrida Hirotda yashagan buyuk shoir va davlat arbobi?", "Alisher Navoiy", ["Bobur", "Lutfiy", "Fuzuliy"], "Navoiy vazir va amir lavozimlarida bo'lgan."),
    ],
    "8.1.31": [
        C(2, "«Qonuni Mas'udiy» asarining muallifi?", "Abu Rayhon Beruniy", ["Ibn Sino", "Forobiy", "Al-Xorazmiy"], "Astronomiyaga oid yirik asar."),
        C(2, "Mirzo Ulug'bek tuzgan yulduzlar jadvali?", "«Ziji jadidi Ko'ragoniy»", ["«Tib qonunlari»", "«Al-jabr val-muqobala»", "«Hindiston»"], "1018 yulduz koordinatalari."),
    ],
    "9.1.1": [
        C(2, "Muhammad Shayboniyxon qaysi yili Marv yaqinida halok bo'ldi?", "1510", ["1500", "1507", "1526"], "Safaviylar bilan jangda."),
        C(2, "Shayboniyxon qaysi davlat qo'shinlari bilan jangda halok bo'lgan?", "Safaviylar (Shoh Ismoil)", ["Boburiylar", "Usmonlilar", "Qozoqlar"], "1510-yil Marv jangi."),
    ],
    "9.1.4": [
        C(2, "Shayboniylar davlatida oliy xon qanday tanlangan?", "Sulolaning eng keksa a'zosi xon qilib ko'tarilgan", ["Faqat xonning to'ng'ich o'g'li", "Xalq saylovi orqali", "Xalifa tayinlagan"], "Ko'chmanchi an'ana: urug' oqsoqoli."),
        C(2, "Shayboniylar davrida poytaxt qaysi xon davrida Buxoroga ko'chirildi (1557)?", "Abdullaxon II", ["Shayboniyxon", "Ko'chkunchixon", "Abulxayrxon"], "Davlat Buxoro xonligi deb atala boshladi."),
    ],
    "9.1.8": [
        C(2, "Ashtarxoniylar sulolasining asoschisi hisoblangan xon?", "Boqi Muhammad", ["Imomqulixon", "Subhonqulixon", "Abulfayzxon"], "1601-yildan."),
        C(2, "Ashtarxoniylar davrida eng uzoq va barqaror hukmronlik qilgan xon?", "Imomqulixon", ["Abulfayzxon", "Ubaydullaxon II", "Boqi Muhammad"], "1611–1642-yillar."),
    ],
    "9.1.10-11": [
        C(2, "Davlatga tegishli yerlar qanday atalgan?", "Amlok (mulki sultoniy)", ["Vaqf", "Mulki xolis", "Suyurg'ol"], "Davlat yerlari."),
        C(3, "Barcha soliqlardan ozod qilingan xususiy yer?", "Mulki xolis (mulki hur)", ["Amlok", "Vaqf", "Iqto"], "Xon yorlig'i bilan berilgan."),
    ],
    "9.1.13": [
        C(1, "Amir Shohmurod qaysi sulola vakili?", "Mang'itlar", ["Ashtarxoniylar", "Shayboniylar", "Qo'ng'irotlar"], "Buxoro amirligi hukmdorlari."),
        C(2, "Buxoroda Mang'itlar sulolasining asoschisi?", "Muhammad Rahimbiy", ["Shohmurod", "Haydar", "Nasrullo"], "1756-yilda xon deb e'lon qilingan."),
    ],
    "9.1.15": [
        C(2, "Abulg'ozi Bahodirxonning «Shajarayi turk» asari qanday mavzuda?", "Turkiy xalqlar va o'zbek xonlari tarixi", ["Tibbiyot", "Astronomiya", "She'riyat nazariyasi"], "Tarixiy asar."),
        C(2, "Abulg'ozi Bahodirxon qaysi yillarda hukmronlik qilgan?", "1643–1663", ["1511–1518", "1804–1806", "1598–1602"], "Xiva xonining tarixchi sifatida ham mashhur."),
    ],
    "9.1.16": [
        C(2, "Xiva xoni Muhammad Rahimxon II qanday taxallus bilan she'rlar yozgan?", "Feruz", ["Komila", "Husayniy", "Ogahiy"], "Shoir va san'at homiysi."),
        C(2, "Qo'ng'irotlar sulolasining so'nggi xoni?", "Said Abdullaxon", ["Muhammad Rahimxon II", "Isfandiyorxon", "Eltuzarxon"], "1918–1920-yillar."),
    ],
    "9.1.17": [
        C(2, "Xivadagi eng baland minora?", "Islomxo'ja minorasi", ["Kalta Minor", "Kalon minorasi", "Chor minor"], "Balandligi 57 m ga yaqin."),
        C(1, "Olloqulixon madrasasi va karvonsaroyi qaysi shaharda?", "Xiva", ["Buxoro", "Qo'qon", "Samarqand"], "Ichan Qal'a yonida."),
    ],
    "9.1.18": [
        C(2, "Qo'qon xonligi tugatilgach (1876) uning hududida tuzilgan viloyat?", "Farg'ona viloyati", ["Sirdaryo viloyati", "Samarqand viloyati", "Kaspiyorti viloyati"], "Turkiston general-gubernatorligi tarkibida."),
        C(2, "Norbo'tabiy davrida Qo'qonda qurilgan madrasa?", "Norbo'tabiy madrasasi", ["Ulug'bek madrasasi", "Ko'kaldosh madrasasi (Buxoro)", "Sherdor madrasasi"], "XVIII asr oxirida qurilgan."),
    ],
    "9.1.19": [
        C(1, "Olimxon hukmronligi qaysi yili tugagan?", "1810", ["1798", "1822", "1842"], "Fitna natijasida o'ldirilgan."),
        C(1, "Olimxon qaysi sulola vakili?", "Minglar", ["Mang'itlar", "Qo'ng'irotlar", "Ashtarxoniylar"], "Qo'qon xonlari sulolasi."),
    ],
    "9.1.20": [
        C(2, "1842-yilda Qo'qon xonligini bosib olgan davlat?", "Buxoro amirligi", ["Xiva xonligi", "Rossiya", "Xitoy"], "Amir Nasrullo Qo'qonni egallagan."),
        C(2, "Nodira qaysi shoir ijodiga ergashib g'azallar yozgan?", "Alisher Navoiy", ["Bobur", "Fuzuliy", "Furqat"], "Navoiy g'azallariga muxammaslar bog'lagan."),
    ],
    "9.1.22": [
        C(2, "Florio Beneveni Buxoroga qaysi rus podshosi topshirig'i bilan borgan?", "Pyotr I", ["Yekaterina II", "Aleksandr II", "Ivan IV"], "1721–1725-yillarda Buxoroda bo'lgan."),
    ],
    "10.1.1": [
        C(1, "Rossiya Toshkentni qaysi yili bosib oldi?", "1865", ["1868", "1873", "1876"], "General Chernyayev qo'shinlari."),
        C(2, "Toshkentni bosib olgan rus generali?", "M. G. Chernyayev", ["K. P. Kaufman", "M. D. Skobelev", "V. A. Perovskiy"], "1865-yil iyun."),
    ],
    "10.1.8": [
        C(1, "Turkiston general-gubernatorligi qaysi yili tashkil etilgan?", "1867", ["1865", "1876", "1886"], "Markazi — Toshkent."),
        C(2, "Turkistonning birinchi general-gubernatori?", "K. P. fon Kaufman", ["M. G. Chernyayev", "M. D. Skobelev", "A. N. Kuropatkin"], "1867–1882-yillar."),
    ],
    "10.1.9": [
        C(2, "Ko'chib kelgan rus aholisi uchun Turkistonda tashkil etilgan aholi punktlari?", "Rus posyolkalari (qishloqlari)", ["Mahallalar", "Ovullar", "Qishloq-qal'alar"], "Eng unumdor yerlarda barpo etilgan."),
    ],
    "10.1.10": [
        C(2, "Turkistonda temir yo'llar qurilishining asosiy maqsadi?", "Paxta va xomashyoni Rossiyaga tashish", ["Turizmni rivojlantirish", "Faqat pochta tashish", "Harbiy flot uchun"], "Hamda harbiy kuchlarni tez ko'chirish."),
        C(2, "Toshkent–Orenburg temir yo'li qachon qurib bitkazilgan?", "1906", ["1880", "1888", "1930"], "Turkistonni Rossiya markazi bilan bog'lagan."),
    ],
    "10.1.14": [
        C(1, "Turkiston jadidlarining yetakchisi, «Padarkush» muallifi?", "Mahmudxo'ja Behbudiy", ["Ismoil Gaspirali", "Fitrat", "Abdulla Avloniy"], "Samarqandlik jadid."),
        C(2, "Abdulla Avloniyning axloqiy darsligi?", "«Turkiy guliston yoxud axloq»", ["«Munozara»", "«Padarkush»", "«Tarjimon»"], "1913-yilda yozilgan."),
    ],
    "10.1.17": [
        C(2, "«Yosh xivaliklar» harakati rahbari?", "Polvonniyoz Yusupov", ["Fayzulla Xo'jayev", "Munavvarqori", "Behbudiy"], "Keyinchalik XXSR hukumati raisi."),
        C(2, "Fitratning «Hind sayyohi qissasi» asari nimaga bag'ishlangan?", "Buxoro amirligidagi ahvol va islohot zarurligiga", ["Hindiston tarixiga", "Muhabbat mavzusiga", "Tabiat tasviriga"], "Ma'rifatparvarlik g'oyalari."),
    ],
    "10.1.18": [
        C(2, "«Samarqand» gazetasining muharriri?", "Mahmudxo'ja Behbudiy", ["Munavvarqori", "Abdulla Avloniy", "Fitrat"], "1913-yilda chiqa boshlagan."),
    ],
    "10.1.19": [
        C(1, "1916-yilgi qo'zg'olon nimaga qarshi ko'tarilgan?", "Mardikorlikka olish farmoniga", ["Paxta narxiga", "Temir yo'l qurilishiga", "Maktablar ochilishiga"], "Front orqasidagi ishlarga safarbarlik."),
        C(2, "1916-yilgi qo'zg'olon birinchi bo'lib qaysi shaharda boshlangan?", "Xo'jand", ["Toshkent", "Samarqand", "Andijon"], "1916-yil 4-iyulda."),
    ],
    "10.1.22": [
        C(1, "Rossiyada Fevral inqilobi qaysi yili bo'lgan?", "1917", ["1905", "1914", "1918"], "Podsho hokimiyati ag'darildi."),
        C(2, "Muvaqqat hukumat Turkistonni boshqarish uchun tuzgan organ?", "Turkiston qo'mitasi", ["Turkiston Sho'rosi", "Turkiston muxtoriyati", "Xalq komissarlari kengashi"], "1917-yil aprelda tuzilgan."),
    ],
    "10.1.23": [
        C(1, "1917-yil noyabrda Qo'qonda e'lon qilingan davlat?", "Turkiston muxtoriyati", ["BXSR", "Turkiston ASSR", "Xorazm respublikasi"], "Turkiston musulmonlarining IV favqulodda qurultoyida."),
        C(2, "Turkiston muxtoriyati qaysi yili bolsheviklar tomonidan tugatildi?", "1918", ["1920", "1924", "1917"], "1918-yil fevralda."),
    ],
    "11.1.4-5": [
        C(2, "Istiqlolchilik harakatini sovet mafkurasi qanday nom bilan atagan?", "«Bosmachilik»", ["«Jadidchilik»", "«Muxtoriyat»", "«Mardikorlik»"], "Haqoratli nom bilan qoralangan."),
        C(2, "Ergash qo'rboshi harakati qaysi hududda boshlangan?", "Farg'ona vodiysida (Qo'qon atrofida)", ["Xorazmda", "Surxondaryoda", "Toshkentda"], "Turkiston muxtoriyati tor-mor etilgach."),
    ],
    "11.1.7": [
        C(2, "BXSR tashkil topishiga olib kelgan voqea?", "1920-yil sentyabrda Buxoro amirligining ag'darilishi", ["1917-yil Fevral inqilobi", "1924-yil milliy chegaralanish", "1865-yil Toshkent istilosi"], "Qizil Armiya yordamida."),
        C(1, "O'zbekiston SSR qaysi yili tashkil topgan?", "1924", ["1920", "1929", "1936"], "Milliy-hududiy chegaralanish natijasida."),
    ],
    "11.1.9": [
        C(2, "NEP qaysi partiya qurultoyida qabul qilingan?", "RKP(b) X s'ezdi (1921)", ["I s'ezd", "XX s'ezd", "XV s'ezd"], "1921-yil mart."),
    ],
    "11.1.10": [
        C(2, "Kolxozlashtirish qanday tarzda o'tkazilgan?", "Majburiy, yoppasiga jamoalashtirish", ["Ixtiyoriylik va bosqichma-bosqichlik", "Xususiy mulkni kengaytirish", "Bozor iqtisodiyoti asosida"], "Dehqonlar zo'rlik bilan kolxozlarga birlashtirilgan."),
        C(1, "Quloqlashtirilganlarning mol-mulki nima qilingan?", "Musodara qilingan", ["Ularga qaytarilgan", "Sotib olingan", "Meros qoldirilgan"], "Mulki tortib olinib, o'zlari surgun qilingan."),
    ],
    "11.1.11": [
        C(2, "Industrializatsiya yillarida Toshkent viloyatida qurilgan GESlar kaskadi?", "Chirchiq–Bo'zsuv GESlari", ["Norak GES", "Sayano-Shushensk GES", "Rog'un GES"], "Chirchiq daryosi va Bo'zsuv kanalida."),
        C(2, "Toshkent to'qimachilik kombinati qachon ishga tushgan?", "1930-yillarda", ["1900-yillarda", "1960-yillarda", "1990-yillarda"], "1934-yilda birinchi navbati."),
    ],
    "11.1.16": [
        C(2, "Ikkinchi jahon urushi yillarida O'zbekistonga taxminan qancha aholi evakuatsiya qilingan?", "1 milliondan ortiq", ["10 ming", "50 ming", "10 milliondan ortiq"], "Shundan 200 mingdan ortig'i bolalar."),
    ],
    "11.1.17": [
        C(1, "Toshkent zilzilasi qaysi sana va yilda sodir bo'lgan?", "1966-yil 26-aprel", ["1966-yil 1-may", "1977-yil 9-may", "1983-yil 1-sentyabr"], "Shahar markazi vayron bo'lgan va qayta qurilgan."),
    ],
    "11.1.19": [
        C(2, "«Paxta ishi» bo'yicha qatag'on qilinganlarning ko'pchiligi keyinchalik…", "oqlandi", ["mukofotlandi", "hech qachon oqlanmadi", "chet elga chiqarib yuborildi"], "Mustaqillik yillarida oqlash ishlari olib borildi."),
    ],
    "11.1.25": [
        C(1, "O'zbekiston milliy valyutasi — so'm qaysi yili to'liq muomalaga kiritildi?", "1994", ["1991", "1993", "2000"], "1994-yil 1-iyuldan."),
        C(2, "2017-yil sentyabridagi muhim iqtisodiy islohot?", "Valyuta konvertatsiyasining erkinlashtirilishi", ["Milliy valyutaning bekor qilinishi", "Barter tizimiga o'tish", "Xususiy mulkning taqiqlanishi"], "Valyuta bozori liberallashtirildi."),
    ],
    "11.1.30": [
        C(2, "«O'zbekiston – 2030» strategiyasida nechta maqsad belgilangan?", "100", ["50", "30", "200"], "5 ta ustuvor yo'nalish bo'yicha 100 ta maqsad."),
        C(2, "Strategiyaga ko'ra 2030-yilgacha O'zbekiston qaysi davlatlar guruhiga kirishi ko'zda tutilgan?", "Daromadi o'rtachadan yuqori bo'lgan davlatlar", ["Kam daromadli davlatlar", "Eng boy davlatlar", "Rivojlanmagan davlatlar"], "Aholi jon boshiga daromadni oshirish."),
    ],
}
