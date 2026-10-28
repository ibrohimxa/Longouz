"""6-sinf: Qadimgi dunyo tarixi — savollar banki."""
from ._dsl import C, O, M

Q = {}

Q["6.1.1-2"] = [
    C(1, "Tarix fani nimani o'rganadi?", "Insoniyatning o'tmishini", ["Faqat yer qatlamlarini", "Faqat hayvonlar dunyosini", "Osmon jismlarini"], "Tarix — jamiyat va insoniyatning o'tmishini o'rganuvchi fan.", b="madaniyat"),
    C(1, "Quyidagilardan qaysi biri yozma manba hisoblanadi?", "«Avesto» kitobi", ["Tosh bolta", "Sopol idish", "Qadimiy tanga"], "Kitob, xat, solnoma yozma manba; qurol va idishlar moddiy manba.", b="madaniyat"),
    C(1, "Tangalarni o'rganuvchi yordamchi tarixiy fan qaysi?", "Numizmatika", ["Epigrafika", "Etnografiya", "Arxeologiya"], "Numizmatika — tangalar haqidagi fan.", b="madaniyat"),
    C(2, "Toshlar, devor va qabr toshlaridagi yozuvlarni o'rganuvchi fan qaysi?", "Epigrafika", ["Numizmatika", "Genealogiya", "Antropologiya"], "Epigrafika — yozuv (bitik)lar haqidagi fan.", b="madaniyat"),
    C(2, "XV asr qaysi yillarni o'z ichiga oladi?", "1401–1500-yillar", ["1400–1499-yillar", "1501–1600-yillar", "1301–1400-yillar"], "Asr 1-yildan 100-yilgacha hisoblanadi.", b="madaniyat"),
    C(2, "Moddiy tarixiy manbalarni yer qazib, o'rganuvchi fan qaysi?", "Arxeologiya", ["Etnografiya", "Genealogiya", "Numizmatika"], "Arxeologiya qazishmalar orqali moddiy yodgorliklarni o'rganadi.", b="madaniyat"),
    C(3, "Hijriy taqvim qaysi yildan (milodiy) boshlanadi?", "622-yil", ["570-yil", "632-yil", "610-yil"], "Payg'ambarimiz Makkadan Madinaga hijrat qilgan yil — 622.", b="madaniyat"),
    O(3, "Miloddan avvalgi 356-yilda tug'ilgan Aleksandr Makedonskiy hayoti qaysi asrga to'g'ri keladi? (Rim raqami yoki raqam bilan yozing)", ["IV", "4"], "Mil. avv. 301–400-yillar IV asr hisoblanadi.", b="madaniyat"),
]

Q["6.1.3"] = [
    C(1, "Hozirgi tipdagi odam (aql egasi) ilmiy nomi bilan qanday ataladi?", "Homo sapiens", ["Homo habilis", "Neandertal", "Avstralopitek"], "Homo sapiens — «aql egasi».", b="siyosiy"),
    C(1, "Odam evolyutsiyasi nazariyasi muallifi kim?", "Charlz Darvin", ["Isaak Nyuton", "Gerodot", "Mendel"], "Ch. Darvin «Turlarning kelib chiqishi» asarida evolyutsiya nazariyasini yaratgan.", b="siyosiy"),
    C(1, "Ilk odamlarning vatani sifatida qaysi qit'a ko'rsatiladi?", "Afrika", ["Avstraliya", "Shimoliy Amerika", "Antarktida"], "Eng qadimgi odam qoldiqlari Sharqiy Afrikada topilgan.", b="siyosiy"),
    C(2, "Odamning kelib chiqishi va rivojlanishini o'rganuvchi fan qaysi?", "Antropologiya", ["Numizmatika", "Epigrafika", "Geologiya"], "Antropologiya — odamning biologik rivojlanishi haqidagi fan.", b="siyosiy"),
    C(2, "Quyidagi ilk odam turlari qaysi tartibda ketma-ket paydo bo'lgan?", "Mohir odam → tik yuruvchi odam → neandertal → kromanion", ["Kromanion → neandertal → mohir odam → tik yuruvchi odam", "Neandertal → mohir odam → kromanion → tik yuruvchi odam", "Tik yuruvchi odam → kromanion → mohir odam → neandertal"], "Evolyutsiya bosqichlari shu tartibda bo'lgan.", b="siyosiy"),
    C(2, "Ilk odamlar asboblarni asosan qanday materialdan yasagan?", "Tosh, suyak va yog'ochdan", ["Temirdan", "Bronzadan", "Misdan"], "Dastlabki asboblar tosh, suyak va yog'ochdan tayyorlangan.", b="siyosiy"),
    C(3, "Ilk odamlar to'dasining asosiy mashg'uloti qaysi edi?", "Termachilik va ovchilik", ["Dehqonchilik", "Hunarmandchilik", "Savdo"], "O'zlashtiruvchi xo'jalik: tayyor narsani yig'ish va ov qilish.", b="siyosiy"),
    O(3, "Ilk odamlar o'zlashtirgan, ularni sovuq va yirtqichlardan saqlagan tabiat kuchi nima? (bir so'z)", ["olov", "Olov"], "Olovdan foydalanish odamning tabiatga qaramligini kamaytirgan.", b="siyosiy"),
]

Q["6.1.4"] = [
    C(1, "Selungur g'ori qaysi davr yodgorligi?", "Ilk paleolit (Ashel)", ["Mezolit", "Neolit", "Bronza davri"], "Selungur — Ashel davri makoni.", b="siyosiy"),
    C(1, "Selungur g'oridan topilgan odam tishlari antropologlar tomonidan qanday nomlangan?", "Farg'onantrop", ["Teshiktoshlik", "Sinantrop", "Pitekantrop"], "Farg'ona vodiysida topilgan — «Farg'onantrop».", b="siyosiy"),
    C(1, "Ilk paleolit davrida odamlar qanday birlashmada yashagan?", "Ibtidoiy to'da", ["Urug' jamoasi", "Qo'shni jamoa", "Davlat"], "Ilk paleolitda odamlar to'da bo'lib yashagan.", b="siyosiy"),
    C(2, "Ashel davrining eng xarakterli asbobi qaysi?", "Qo'l boltasi", ["Kamon va o'q", "Sopol idish", "Temir o'roq"], "Ashel davrida tosh qo'l boltalari keng tarqalgan.", b="siyosiy"),
    C(2, "Ko'lbuloq makoni qaysi hududda joylashgan?", "Toshkent viloyatida", ["Surxondaryoda", "Xorazmda", "Buxoroda"], "Ko'lbuloq — Toshkent viloyatidagi ilk paleolit makoni.", b="siyosiy"),
    C(2, "Quyidagi yodgorliklardan qaysi biri ilk paleolitga tegishli?", "Selungur", ["Teshiktosh", "Obirahmat", "Sopollitepa"], "Teshiktosh va Obirahmat — o'rta paleolit; Sopollitepa — bronza davri.", b="siyosiy"),
    C(3, "«Ashel» atamasi nimadan kelib chiqqan?", "Fransiyadagi Sent-Ashel makoni nomidan", ["Selungur g'orining nomidan", "Misrdagi shahar nomidan", "Hindistondagi daryo nomidan"], "Davr nomi dastlabki topilma joyidan olingan.", b="siyosiy"),
    O(3, "Ilk paleolit davrida odamlar mehnat qurollarini yasash uchun qaysi materialni (bir so'z) eng ko'p ishlatgan?", ["tosh", "Tosh"], "Ashel davri — tosh qurollar asri.", b="siyosiy"),
]

Q["6.1.5"] = [
    C(1, "O'rta paleolit davri qanday nomlanadi?", "Mustye davri", ["Ashel davri", "Kaltaminor davri", "Sopolli davri"], "Mustye nomi Fransiyadagi Le-Mustye g'oridan.", b="siyosiy"),
    C(1, "Teshiktosh g'ori qaysi viloyatda joylashgan?", "Surxondaryo (Boysun tog'lari)", ["Farg'ona", "Xorazm", "Navoiy"], "Teshiktosh — Boysun tog'laridagi g'or.", b="siyosiy"),
    C(1, "O'rta paleolitda yashagan odam turi qaysi?", "Neandertal", ["Kromanion", "Avstralopitek", "Mohir odam"], "Mustye davrining odami — neandertal.", b="siyosiy"),
    C(2, "Teshiktosh g'oridan topilgan topilma qaysi?", "Neandertal bola suyagi va tog' echkisi shoxlari aylanasi", ["Oltin tanga", "Sopol idish xumdoni", "Temir qurol"], "Bola dafn etilgan joy atrofiga tog' echkisi shoxlari terib qo'yilgan.", b="siyosiy"),
    C(2, "Obirahmat g'ori qaysi hududda joylashgan?", "Toshkent viloyati", ["Surxondaryo", "Xorazm", "Farg'ona"], "Obirahmat — Toshkent viloyati, Chotqol tog'lari.", b="siyosiy"),
    C(2, "Obirahmat g'orini o'rgangan olim kim?", "A.P. Okladnikov", ["S.P. Tolstov", "A. Asqarov", "M. Gerasimov"], "Obirahmatni Okladnikov o'rgangan; bola qiyofasini Gerasimov tiklagan.", b="siyosiy"),
    C(3, "Obirahmat g'orida topilgan bola qiyofasini tiklagan olim kim?", "M.M. Gerasimov", ["A.P. Okladnikov", "S.P. Tolstov", "Ya. Gulomov"], "Gerasimov antropolog-haykaltarosh bo'lib, bosh suyagidan qiyofa tiklagan.", b="siyosiy"),
    O(3, "Teshiktosh g'oridan qaysi hayvonning shoxlari topilgan? (hayvon nomini yozing, masalan: tog' ...)", ["tog' echkisi", "tog' echki", "echki"], "Bola yoniga tog' echkisi shoxlari aylana shaklida qo'yilgan.", b="siyosiy"),
]

Q["6.1.6"] = [
    C(1, "So'nggi paleolit davrida yashagan odam turi qaysi?", "Kromanion (hozirgi tipdagi odam)", ["Neandertal", "Mohir odam", "Tik yuruvchi odam"], "Kromanion — Homo sapiens.", b="ijtimoiy"),
    C(1, "So'nggi paleolitda odamlar qanday jamoada birlashgan?", "Urug' jamoasi", ["Ibtidoiy to'da", "Davlat", "Sinfiy jamiyat"], "Urug' jamoasi shu davrda shakllandi.", b="ijtimoiy"),
    C(1, "Ona urug'i (matriarxat) davrida jamoani kim boshqargan?", "Ayol (ona)", ["Ota", "Harbiy sarkarda", "Shoh"], "Matriarxatda ayol hurmatga ega bo'lgan.", b="ijtimoiy"),
    C(2, "Zarautsoy qoya suratlari qaysi viloyatda joylashgan?", "Surxondaryo", ["Xorazm", "Samarqand", "Namangan"], "Zarautsoy (Sherobod tumani) — qadimgi qoya rasmlari.", b="ijtimoiy"),
    C(2, "Qoya rasmlari qadimgi odamlar hayotining qaysi tomonini aks ettiradi?", "Ov sahnalari va e'tiqodlarini", ["Davlat boshqaruvini", "Savdo yo'llarini", "Yozuvni"], "Rasmlarda ov va marosimlar tasvirlangan.", b="ijtimoiy"),
    C(2, "So'nggi paleolit davri taxminan qachon bo'lgan?", "40–12 ming yil avval", ["1 mln – 100 ming yil avval", "100–40 ming yil avval", "6–5 ming yil avval"], "So'nggi paleolit — taxminan 40–12 ming yil avval.", b="ijtimoiy"),
    C(3, "So'nggi paleolitda odamlar ovda nimalardan foydalana boshlagan?", "Nayza uchi va ov to'rlari kabi takomillashgan qurollardan", ["Temir pichoqlardan", "O'qlardan va xoch kamondan", "Bronza nayzalardan"], "Tosh va suyak qurollari takomillashgan.", b="ijtimoiy"),
    O(3, "Ibtidoiy odamlarning so'nggi paleolitda shakllangan jamoasi nima deb ataladi? (ikki so'z: ... jamoasi)", ["urug' jamoasi", "urug'", "urug jamoasi"], "Qon-qarindoshlik asosidagi birlashma.", b="ijtimoiy"),
]

Q["6.1.7"] = [
    C(1, "Mezolit so'zining ma'nosi nima?", "O'rta tosh davri", ["Eski tosh davri", "Yangi tosh davri", "Mis-tosh davri"], "Mezolit — o'rta tosh davri.", b="siyosiy"),
    C(1, "Mezolit davrida qaysi ovchilik quroli ixtiro qilingan?", "Kamon va o'q", ["Qo'l boltasi", "Temir nayza", "O'roq"], "Kamon-o'q ovni samarali qildi.", b="siyosiy"),
    C(1, "Mezolit davrida qaysi hayvon qo'lga o'rgatilgan?", "It", ["Ot", "Tuya", "Qo'y"], "It ovda yordamchi sifatida qo'lga o'rgatilgan.", b="siyosiy"),
    C(2, "Machay g'ori qayerda joylashgan?", "Surxondaryo (Boysun)", ["Xorazm", "Toshkent", "Farg'ona"], "Machay — Boysundagi mezolit–neolit yodgorligi.", b="siyosiy"),
    C(2, "Mezolit davriga xos asboblar qanday nomlanadi?", "Mayda tosh (mikrolit) asboblar", ["Yirik qo'l boltalar", "Temir qurollar", "Sopol idishlar"], "Mikrolitlar kamon o'qining uchi va pichoq sifatida ishlatilgan.", b="siyosiy"),
    C(2, "Mezolitning boshlanishiga qaysi tabiiy o'zgarish sabab bo'lgan?", "Muz bosishning tugashi va iqlimning isishi", ["Vulqon otilishi", "Yer qit'alarining siljishi", "Dengiz sathining pasayishi"], "Muzlik chekinib, o'simlik va hayvonot dunyosi o'zgardi.", b="siyosiy"),
    C(3, "Kamon va o'q ixtiro qilinishining ahamiyati nima edi?", "Uzoqdan ov qilish imkonini berib, ovni samarali qildi", ["Dehqonchilikni boshlab berdi", "Metallni eritishga imkon berdi", "Yozuvning paydo bo'lishiga olib keldi"], "Ov qurollari takomillashdi.", b="siyosiy"),
    O(3, "Mezolitda ovchilarning insonga ishonchli yordamchisiga aylangan hayvon nomini yozing.", ["it", "It"], "It ovda yordam bergan.", b="siyosiy"),
]

Q["6.1.8"] = [
    C(1, "Neolit so'zining ma'nosi nima?", "Yangi tosh davri", ["Eski tosh davri", "O'rta tosh davri", "Mis davri"], "Neolit — yangi tosh davri.", b="ijtimoiy"),
    C(1, "Neolit davrida odamlar nimaga o'tgan?", "Dehqonchilik va chorvachilikka", ["Faqat termachilikka", "Metall quyishga", "Yozuvga"], "O'zlashtiruvchi xo'jalikdan ishlab chiqaruvchi xo'jalikka o'tish.", b="ijtimoiy"),
    C(1, "Neolit davrida qanday idish paydo bo'ldi?", "Sopol idish", ["Temir qozon", "Oltin kosa", "Chinni piyola"], "Loydan yasab pishirilgan idishlar.", b="ijtimoiy"),
    C(2, "«Neolit inqilobi» nima?", "O'zlashtiruvchi xo'jalikdan ishlab chiqaruvchi xo'jalikka o'tish", ["Metallning kashf etilishi", "Davlatning paydo bo'lishi", "Yozuvning ixtiro qilinishi"], "Odamlar o'zlari oziq yetishtira boshladi.", b="ijtimoiy"),
    C(2, "Neolit davrining asosiy asboblari qanday?", "Sayqallangan va teshib ishlangan tosh qurollar", ["Faqat qo'pol urib yasalgan toshlar", "Bronza qurollar", "Temir qurollar"], "Tosh sayqallash, teshish usullari rivojlandi.", b="ijtimoiy"),
    C(2, "Neolit davrida qaysi hunar paydo bo'lib, rivojlandi?", "To'qimachilik va kulolchilik", ["Metallurgiya", "Shishasozlik", "Qog'oz ishlab chiqarish"], "Mato to'qish va sopol idish yasash.", b="ijtimoiy"),
    C(3, "«Neolit inqilobi» atamasini fanga kim kiritgan?", "Gordon Child", ["Charlz Darvin", "Gerodot", "S.P. Tolstov"], "Ingliz arxeologi G. Child bu atamani qo'llagan.", b="ijtimoiy"),
    O(3, "Neolit davrida yangi paydo bo'lgan va yerga ishlov berishga asoslangan xo'jalik turini yozing (bir so'z).", ["dehqonchilik", "Dehqonchilik"], "Dehqonchilik — ishlab chiqaruvchi xo'jalikning asosi.", b="ijtimoiy"),
]

Q["6.1.9"] = [
    C(1, "Kaltaminor madaniyati qaysi davrga tegishli?", "Neolit", ["Paleolit", "Bronza davri", "Temir davri"], "Kaltaminor — neolit madaniyati.", b="siyosiy"),
    C(1, "Kaltaminor madaniyati qaysi hududda tarqalgan?", "Xorazm va Quyi Zarafshon", ["Farg'ona vodiysi", "Surxondaryo", "Toshkent vohasi"], "Quyi Amudaryo va Quyi Zarafshon bo'ylari.", b="siyosiy"),
    C(1, "Kaltaminor aholisi qanday turarjoyda yashagan?", "Qamish kulbalarda", ["G'ishtdan qurilgan uylarda", "G'orlarda", "Tosh qasrlarda"], "Qamishdan yasalgan kulba-chaylalar.", b="siyosiy"),
    C(2, "Kaltaminor madaniyatini kim o'rgangan?", "S.P. Tolstov", ["A. Asqarov", "A.P. Okladnikov", "M. Gerasimov"], "Xorazm arxeologiya ekspeditsiyasi rahbari S.P. Tolstov.", b="siyosiy"),
    C(2, "Kaltaminor aholisining asosiy mashg'uloti qaysi edi?", "Baliq ovlash, ov va terimchilik", ["Metall quyish", "Savdo-sotiq", "Shahar qurish"], "Daryo bo'yida baliqchilik va ovchilik asos bo'lgan.", b="siyosiy"),
    C(2, "Joytun madaniyati qayerda tarqalgan?", "Janubiy Turkmaniston (Kopetdog etagi)", ["Xorazm", "Farg'ona", "Sirdaryo bo'yi"], "Joytun — Turkmanistondagi ilk dehqonchilik madaniyati.", b="siyosiy"),
    C(3, "Joytun madaniyatining ahamiyati nimada?", "Markaziy Osiyodagi eng qadimgi dehqonchilik manzilgohlaridan biri", ["Ilk temir quyish markazi", "Ilk yozuv markazi", "Ilk shahar-davlat"], "Joytun aholisi bug'doy va arpa ekkan.", b="siyosiy"),
    O(3, "Kaltaminor madaniyati qaysi tarixiy davrga (yangi tosh) mansub? Davr nomini yozing.", ["neolit", "Neolit"], "Yangi tosh davri.", b="siyosiy"),
]

Q["6.1.10"] = [
    C(1, "Eneolit davri qanday ataladi?", "Mis-tosh davri", ["Yangi tosh davri", "Bronza davri", "Temir davri"], "Eneolit — mis-tosh davri.", b="siyosiy"),
    C(1, "Zamonbobo madaniyati qaysi hududda?", "Buxoro (Qorako'l) vohasi", ["Farg'ona vodiysi", "Xorazm", "Toshkent"], "Zamonbobo ko'llari yaqinidagi yodgorlik.", b="siyosiy"),
    C(1, "Eneolitda odamlar qaysi metalldan qurol yasay boshlagan?", "Misdan", ["Temirdan", "Qalaydan", "Oltindan"], "Mis birinchi o'zlashtirilgan metall.", b="siyosiy"),
    C(2, "Sarazm yodgorligi qaysi daryo havzasida joylashgan?", "Zarafshon", ["Sirdaryo", "Surxondaryo", "Chirchiq"], "Sarazm — Zarafshon vodiysi (Panjikent atrofi).", b="siyosiy"),
    C(2, "Zamonbobo madaniyati xo'jaligining xususiyati nima?", "O'tiriqchi dehqonchilik va chorvachilik uyg'unlashgan", ["Faqat ovchilik", "Faqat savdo", "Faqat hunarmandchilik"], "Dehqonchilik va chorvachilik birga olib borilgan.", b="siyosiy"),
    C(2, "Eneolit davrida mehnat taqsimoti qanday o'zgardi?", "Dehqonchilik va chorvachilik ajrala boshladi", ["Savdo butunlay to'xtadi", "Ovchilik yagona kasbga aylandi", "Hunarmandchilik yo'qoldi"], "Mehnat taqsimoti chuqurlashdi.", b="siyosiy"),
    C(3, "Sarazm yodgorligi qaysi tashkilot ro'yxatiga kiritilgan?", "YUNESKO Jahon merosi", ["Faqat milliy ro'yxatga", "NATO ro'yxatiga", "Hech qaysi ro'yxatga"], "Sarazm 2010-yilda YUNESKO ro'yxatiga kiritilgan.", b="siyosiy"),
    O(3, "Eneolit davrida o'zlashtirilgan birinchi metall nomini yozing.", ["mis", "Mis"], "Mis-tosh davri.", b="siyosiy"),
]

Q["6.1.11"] = [
    C(1, "Bronza qaysi metallarning qotishmasi?", "Mis va qalay", ["Temir va mis", "Oltin va kumush", "Qo'rg'oshin va temir"], "Bronza — mis va qalay qotishmasi.", b="siyosiy"),
    C(1, "Sopollitepa va Jarqo'ton yodgorliklari qaysi viloyatda?", "Surxondaryo", ["Xorazm", "Farg'ona", "Navoiy"], "Sopolli madaniyati — Surxondaryo.", b="siyosiy"),
    C(1, "Sopolli madaniyatini o'rgangan olim kim?", "Ahmadali Asqarov", ["S.P. Tolstov", "A.P. Okladnikov", "Ya. Gulomov"], "A. Asqarov Sopollitepa va Jarqo'tonni o'rgangan.", b="siyosiy"),
    C(2, "Jarqo'ton qanday yodgorlik?", "Ilk shahar-ma'bad (shaharga o'xshash yirik manzilgoh)", ["Ovchilar makoni", "Karvonsaroy", "Dafn qilish maydoni"], "O'zbekistondagi ilk shahar tipidagi manzilgoh.", b="siyosiy"),
    C(2, "Bronza davrida qaysi hunarmandchilik turi rivoj topdi?", "Metallsozlik (bronza quyish)", ["Qog'ozsozlik", "Shishasozlik", "Chinnisozlik"], "Bronza qurol va taqinchoqlar yasalgan.", b="siyosiy"),
    C(2, "Bronza davrida jamiyatda qanday o'zgarish yuz berdi?", "Mulkiy tengsizlik va ijtimoiy tabaqalanish kuchaydi", ["Urug' jamoalari yo'qoldi", "Qullik bekor qilindi", "Hamma teng bo'ldi"], "Boy-kambag'allik paydo bo'ldi.", b="siyosiy"),
    C(3, "Jarqo'ton ibodatxonasida nimaga sig'inilgan?", "Olovga", ["Quyoshga yagona xudo sifatida", "Hayvonlarga", "Suvga"], "Olovga sig'inish izlari topilgan.", b="siyosiy"),
    O(3, "Bronza davrida yashagan Sopolli madaniyati Surxondaryoning qaysi eski nomli manzilgohi nomi bilan ataladi? (Sopolli... bilan boshlanadigan yodgorlik nomini yozing)", ["Sopollitepa", "sopollitepa"], "Sopollitepa.", b="siyosiy"),
]

Q["6.1.12"] = [
    C(1, "Ilk temir davri qaysi ming yillikka to'g'ri keladi?", "Miloddan avvalgi I ming yillik", ["Mil. avv. III ming yillik", "Mil. avv. V ming yillik", "Milodiy I ming yillik"], "Temir qurollar mil. avv. I ming yillik boshlarida keng tarqalgan.", b="ijtimoiy"),
    C(1, "Temir qurollarning tarqalishi nimaga olib keldi?", "Mehnat unumdorligining oshishiga", ["Dehqonchilikning to'xtashiga", "Savdoning to'xtashiga", "Aholining kamayishiga"], "Temir bolta, o'roq va omoch ishni yengillashtirdi.", b="ijtimoiy"),
    C(1, "Ilk temir davrida jamiyatda nima kuchaydi?", "Ijtimoiy tabaqalanish", ["Urug' tengligi", "Matriarxat", "Hammaning umumiy mulki"], "Boy-kambag'allik, qullar paydo bo'ldi.", b="ijtimoiy"),
    C(2, "Qadimgi Sharqda dehqonchilik hududlari qanday sug'orilgan?", "Kanallar (ariqlar) orqali", ["Faqat yomg'ir suvi bilan", "Faqat quduqlardan", "Sug'orilmagan"], "Sun'iy sug'orish rivojlandi.", b="ijtimoiy"),
    C(2, "Cho'l va dasht hududlarida yashagan ko'chmanchi chorvador qabilalar qaysilar?", "Saklar va massagetlar", ["Rimliklar", "Misrliklar", "Yunonlar"], "Sak va massaget qabilalari.", b="ijtimoiy"),
    C(2, "Ilk temir davrida o'troq aholi yashagan joylarning asosiy turi qaysi?", "Qal'a va qishloq-vohalar", ["Faqat g'orlar", "Faqat chodirlar", "Faqat daryo kemalari"], "Mudofaa devorli manzilgohlar paydo bo'ldi.", b="ijtimoiy"),
    C(3, "Davlatning paydo bo'lishiga sabab bo'lgan omillardan biri qaysi?", "Mulkiy tengsizlik va ijtimoiy tabaqalanishning kuchayishi", ["Aholining kamayishi", "Savdoning to'xtashi", "Urug' jamoalarining kuchayishi"], "Boshqaruv zaruriyati tug'ildi.", b="ijtimoiy"),
    O(3, "Ilk temir davrida mehnat unumdorligini oshirgan yangi metall nomini yozing.", ["temir", "Temir"], "Temir.", b="ijtimoiy"),
]

Q["6.1.13"] = [
    C(1, "Mil. avv. VII–VI asrlarda Amudaryo quyi oqimida vujudga kelgan qadimiy davlat qaysi?", "Katta Xorazm", ["Kushon", "Davon", "Qang'"], "Katta Xorazm — eng qadimgi davlat birlashmalaridan.", b="siyosiy"),
    C(1, "«Avesto»da Xorazm qanday atalgan?", "Xvairizam", ["Baqtra", "Parfiya", "Marg'iyona"], "Xvairizam — Xorazm.", b="siyosiy"),
    C(1, "Qadimgi Xorazm qaysi daryo bo'yida vujudga kelgan?", "Amudaryo", ["Sirdaryo", "Zarafshon", "Chirchiq"], "Amudaryoning quyi oqimi.", b="siyosiy"),
    C(2, "Qadimgi Xorazmning xo'jaligi nimaga asoslangan edi?", "Sug'orma dehqonchilik va chorvachilik", ["Faqat baliqchilik", "Faqat ovchilik", "Dengiz savdosi"], "Kanallar qazilgan.", b="siyosiy"),
    C(2, "Katta Xorazm davlati tarkibiga kirgan hududlarni toping.", "Xorazm, Marv, Parfiya, So'g'diyona, Hirot", ["Hind vodiysi va Xitoy", "Misr va Mesopotamiya", "Gretsiya va Rim"], "Bu hududlar qadimgi Xorazm bilan bog'liq.", b="siyosiy"),
    C(2, "Quyidagilardan qaysi biri qadimgi Xorazm yodgorligi?", "Qo'yqirilgan qal'a", ["Jarqo'ton", "Selungur", "Teshiktosh"], "Qo'yqirilgan qal'a — Xorazmdagi qadimiy qal'a.", b="siyosiy"),
    C(3, "Katta Xorazm davlati keyinchalik qaysi davlat tarkibiga kirgan?", "Ahamoniylar davlati", ["Rim imperiyasi", "Kushon imperiyasi", "Makedoniya"], "Xorazm Ahamoniylar satrapligiga aylandi.", b="siyosiy"),
    O(3, "Qadimgi Xorazmning «Avesto»dagi nomini yozing.", ["Xvairizam", "xvairizam", "Xvarizm", "Xvarazm"], "Avestoda Xvairizam deb atalgan.", b="siyosiy"),
]

Q["6.1.14"] = [
    C(1, "Baqtriya qaysi daryoning yuqori oqimida joylashgan?", "Amudaryo", ["Sirdaryo", "Zarafshon", "Qashqadaryo"], "Baqtriya — Amudaryoning yuqori oqimi.", b="siyosiy"),
    C(1, "Baqtriyaning asosiy shahri va poytaxti qaysi edi?", "Baqtra (Balx)", ["Samarqand", "Bityan", "Ershi"], "Baqtra hozirgi Balx.", b="siyosiy"),
    C(1, "Baqtriya hududining bir qismi hozirgi qaysi viloyatga to'g'ri keladi?", "Surxondaryo", ["Xorazm", "Farg'ona", "Navoiy"], "Janubiy O'zbekiston, shimoliy Afg'oniston, Tojikiston.", b="siyosiy"),
    C(2, "Baqtriya qaysi davlat tarkibiga kirgandan keyin satrapliklardan biriga aylangan?", "Ahamoniylar", ["Rim", "Kushon", "Yunon-Baqtriya"], "Mil. avv. VI asrda Ahamoniylar tarkibiga kirgan.", b="siyosiy"),
    C(2, "Baqtriya aholisining asosiy mashg'uloti nima edi?", "Sug'orma dehqonchilik, chorvachilik va hunarmandchilik", ["Faqat dengiz savdosi", "Faqat ovchilik", "Faqat terimchilik"], "Rivojlangan dehqonchilik.", b="siyosiy"),
    C(2, "Qadimgi Baqtriya hududida keyinchalik qaysi yirik davlat tashkil topdi?", "Yunon-Baqtriya podsholigi", ["Davon", "Qang'", "Katta Xorazm"], "Mil. avv. III asrda.", b="siyosiy"),
    C(3, "Baqtriyaning Ahamoniylarga qarshi turishida muhim bo'lgan omil nima?", "Mustahkam qal'alar va jangovar otliqlar", ["Dengiz floti", "Fil qo'shini", "Temir yo'l"], "Baqtriya otliqlari mashhur bo'lgan.", b="siyosiy"),
    O(3, "Baqtriyaning qadimgi poytaxti hozirgi qaysi shahar o'rnida bo'lgan? (shahar nomini yozing: B...)", ["Balx", "balx"], "Baqtra — Balx.", b="siyosiy"),
]

Q["6.1.15"] = [
    C(1, "Zardushtiylik dinining muqaddas kitobi qaysi?", "«Avesto»", ["«Injil»", "«Veda»", "«Tavrot»"], "Avesto zardushtiylikning muqaddas kitobi.", b="madaniyat"),
    C(1, "Zardushtiylikning asoschisi kim?", "Zardusht (Zaratushtra)", ["Budda", "Konfutsiy", "Kir II"], "Zardusht — payg'ambar.", b="madaniyat"),
    C(1, "Zardushtiylikda yaxshilik xudosi qanday ataladi?", "Axura Mazda", ["Angra Mayyu", "Ra", "Zevs"], "Axura Mazda — yaxshilik xudosi.", b="madaniyat"),
    C(2, "Zardushtiylikda yomonlik xudosi qaysi?", "Angra Mayyu (Axriman)", ["Axura Mazda", "Mitra", "Anaxita"], "Yomonlik homiysi.", b="madaniyat"),
    C(2, "Zardushtiylik ta'limotining asosiy qoidasi nima?", "Ezgu fikr, ezgu so'z, ezgu amal", ["Faqat urush", "Faqat savdo", "Faqat ro'za"], "Uch ezgulik.", b="madaniyat"),
    C(2, "Zardushtiylikda qaysi tabiat unsuri eng muqaddas hisoblangan?", "Olov", ["Tosh", "Temir", "Qum"], "Olov Axura Mazdaning belgisi.", b="madaniyat"),
    C(3, "«Avesto»ning necha yilligi 2001-yilda O'zbekistonda YUNESKO bilan nishonlangan?", "2700 yillik", ["1000 yillik", "2000 yillik", "3000 yillik"], "2001-yilda 2700 yilligi nishonlandi.", b="madaniyat"),
    O(3, "Zardushtiylikda murdalarning suyaklari solinadigan sopol quti nima deyiladi? (ikki variantdan birini yozing: ostadon yoki ossuariy)", ["ostadon", "ossuariy", "Ostadon", "Ossuariy"], "Dafn udumi.", b="madaniyat"),
]

Q["6.1.16-17"] = [
    C(1, "Ahamoniylar davlatining asoschisi kim?", "Kir II", ["Doro I", "Kambiz", "Kserks"], "Kir II (mil. avv. 558–530).", b="siyosiy"),
    C(1, "Kir II ga qarshi kurashgan massaget malikasi kim?", "To'maris", ["Shiroq", "Spitamen", "Roksana"], "To'maris Kirni mag'lub etgan.", b="siyosiy"),
    C(1, "Doro I (mil. avv. 522–486) ning saklarga qarshi kurashda fidokorlik ko'rsatgan sak qahramoni kim?", "Shiroq", ["Spitamen", "Bess", "Oksiart"], "Shiroq o'z xalqini himoya qilish uchun jon fido qilgan.", b="siyosiy"),
    C(2, "Kir II qaysi yili To'maris bilan jangda halok bo'lgan?", "Mil. avv. 530-yilda", ["Mil. avv. 558-yilda", "Mil. avv. 486-yilda", "Mil. avv. 331-yilda"], "Massagetlarga qarshi yurishda.", b="siyosiy"),
    C(2, "Ahamoniylar davlatida viloyatlar qanday nomlangan?", "Satraplik", ["Nom", "Polis", "Ulus"], "Satrap — viloyat hokimi.", b="siyosiy"),
    C(2, "Doro I islohotlaridan qaysi biri to'g'ri?", "Pul islohoti: oltin «dariq» tangasi joriy qilindi", ["Dengiz floti tuzildi", "Yozuv ixtiro qilindi", "Temir yo'l qurildi"], "Dariq — Ahamoniylar oltin tangasi.", b="siyosiy"),
    C(3, "Ahamoniylar davlatining yirik yo'li va yagona pochta tizimi nima deb atalgan?", "«Shohlar yo'li»", ["«Ipak yo'li»", "«Tuz yo'li»", "«Kehrabo yo'li»"], "Sard–Suza yo'li.", b="siyosiy"),
    O(3, "Ahamoniylar davlatini qaysi shoh (ismini yozing) eng yuksak cho'qqisiga olib chiqqan va Behistun yozuvini qoldirgan? (Doro ... )", ["Doro I", "Doro", "Doro 1"], "Doro I (522–486).", b="siyosiy"),
]

Q["6.1.18"] = [
    C(1, "Aleksandr Makedonskiyning otasi kim edi?", "Filipp II", ["Kir II", "Doro I", "Selevk"], "Makedoniya shohi Filipp II.", b="siyosiy"),
    C(1, "Aleksandr Makedonskiyning ustozi kim bo'lgan?", "Aristotel", ["Platon", "Sokrat", "Gerodot"], "Aristotel Aleksandrni tarbiyalagan.", b="siyosiy"),
    C(1, "Aleksandr Makedonskiy qaysi yili vafot etgan?", "Mil. avv. 323-yilda", ["Mil. avv. 356-yilda", "Mil. avv. 331-yilda", "Mil. avv. 330-yilda"], "Bobilda vafot etgan.", b="siyosiy"),
    C(2, "Aleksandr Fors qo'shinini hal qiluvchi tarzda qaysi jangda yengdi?", "Gavgamela (mil. avv. 331)", ["Marafon", "Termopil", "Kann"], "Doro III mag'lub bo'ldi.", b="siyosiy"),
    C(2, "Aleksandr Amudaryodan o'tib, O'rta Osiyoga qaysi yili kirgan?", "Mil. avv. 329-yilda", ["Mil. avv. 334-yilda", "Mil. avv. 323-yilda", "Mil. avv. 356-yilda"], "329-yilda Baqtriyaga kirgan.", b="siyosiy"),
    C(2, "Aleksandr qaysi So'g'd shahrini egallagan?", "Marokanda (Samarqand)", ["Bityan", "Ershi", "Guyshan"], "Marokanda — qadimgi Samarqand.", b="siyosiy"),
    C(3, "Aleksandr Sirdaryo bo'yida qurgan shahar qanday nomlangan?", "Aleksandriya Eskata (Chekka Aleksandriya)", ["Aleksandriya Misr", "Aleksandriya Hind", "Aleksandriya Baqtra"], "Hozirgi Xo'jand o'rnida.", b="siyosiy"),
    O(3, "Aleksandr Makedonskiy qaysi shaharda vafot etgan? (shahar nomini yozing)", ["Bobil", "bobil", "Vavilon"], "Mil. avv. 323-yil, Bobil.", b="siyosiy"),
]

Q["6.1.19-20"] = [
    C(1, "Makedoniyaliklarga qarshi So'g'diyonadagi qo'zg'olon rahbari kim edi?", "Spitamen", ["Bess", "Shiroq", "Kir"], "Spitamen — so'g'dlik zodagon.", b="siyosiy"),
    C(1, "Spitamen qo'zg'oloni qaysi yillarda bo'lgan?", "Mil. avv. 329–327-yillar", ["Mil. avv. 558–530-yillar", "Mil. avv. 104–102-yillar", "Mil. avv. 250-yil"], "329–327-yillar.", b="siyosiy"),
    C(1, "Aleksandr vafotidan keyin O'rta Osiyo hududi qaysi sulola davlati tarkibida bo'ldi?", "Salavkiylar", ["Ahamoniylar", "Mauryalar", "Ptolemeylar"], "Salavk I asos solgan.", b="siyosiy"),
    C(2, "Spitamen qo'zg'olonining muvaffaqiyatsizligiga sabab nima?", "Massagetlar xiyonati va makedonlarning kuchi", ["Hindlar yordami", "Yunonlar xiyonati", "Dengiz floti"], "Spitamen oxir-oqibat o'ldirilgan.", b="siyosiy"),
    C(2, "Salavkiylar davlatining asoschisi kim?", "Salavk I Nikator", ["Ptolemey", "Diodot", "Demetriy"], "Aleksandrning sarkardalaridan biri.", b="siyosiy"),
    C(2, "Spitamenning qizi Apama kimga turmushga chiqqan?", "Salavk I ga", ["Aleksandrga", "Ptolemeyga", "Kirga"], "Salavk Apamaga uylangan.", b="siyosiy"),
    C(3, "Politimet daryosi bo'yidagi jangda makedon qo'shini...", "Spitamen tomonidan tor-mor etilgan", ["Spitamenni mag'lub etgan", "Hindiston tomon chekingan", "Baqtraga ko'chib o'tgan"], "Zarafshon bo'yidagi jang.", b="siyosiy"),
    O(3, "Aleksandr Makedonskiyning baqtriyalik xotini kim edi? (ism)", ["Roksana", "roksana", "Roxana"], "Oksiartning qizi Roksana.", b="siyosiy"),
]

Q["6.1.21"] = [
    C(1, "Yunon-Baqtriya podsholigi qaysi asrda tashkil topgan?", "Mil. avv. III asrda", ["Mil. avv. VI asrda", "Milodiy I asrda", "Mil. avv. V asrda"], "Mil. avv. 250-yil atrofida.", b="siyosiy"),
    C(1, "Yunon-Baqtriya davlatining asoschisi kim?", "Diodot", ["Salavk", "Doro", "Kujula"], "Diodot Salavkiylardan ajralib chiqqan.", b="siyosiy"),
    C(1, "Ellinizm nima?", "Yunon va Sharq madaniyatining qo'shilishi", ["Rim huquqi", "Misr dini", "Hind kastalari"], "Yunon-sharq sintezi.", b="madaniyat"),
    C(2, "Yunon-Baqtriya tangalaridagi yozuvlar qaysi tilda?", "Yunon tilida", ["Xitoy tilida", "Arab tilida", "Rus tilida"], "Yunon yozuvi.", b="siyosiy"),
    C(2, "Amudaryo bo'yida joylashgan yunon-baqtriya shahri qaysi?", "Ay-Xonum", ["Tuproqqal'a", "Jarqo'ton", "Selungur"], "Ay-Xonum — ellinistik shahar.", b="siyosiy"),
    C(2, "Yunon-Baqtriya qaysi daryo orqali Hindiston bilan bog'langan?", "Hind", ["Nil", "Dajla", "Volga"], "Hindistonning shimoliy-g'arbiy qismi bosib olingan.", b="siyosiy"),
    C(3, "Yunon-Baqtriya podsholigining tugashiga sabab bo'lgan kuch kim?", "Shimoldan kelgan ko'chmanchi qabilalar (Yuechji)", ["Rimliklar", "Arablar", "Xunlar"], "Mil. avv. II asr o'rtalarida.", b="siyosiy"),
    O(3, "Xitoy elchisi Chjan Szyan Baqtriyaga mil. avv. 128-yilda kelgan. Uni yuborgan Xitoy hukmdori Xan sulolasidan (ismini yozing: U-di).", ["Xan U-di", "U-di", "Udi", "Xan Udi"], "Imperator Xan U-di.", b="siyosiy"),
]

Q["6.1.22-23"] = [
    C(1, "Qadimgi Davon (Dovon) davlati qaysi hududda joylashgan?", "Farg'ona vodiysi", ["Surxondaryo", "Xorazm", "Sirdaryo o'rta oqimi"], "Davon — Farg'ona.", b="siyosiy"),
    C(1, "Davonning poytaxti qaysi shahar edi?", "Ershi", ["Bityan", "Marokanda", "Baqtra"], "Ershi — poytaxt.", b="siyosiy"),
    C(1, "Davon davlati mashhur bo'lgan narsa nima?", "«Samoviy tulporlar» (ajoyib otlar)", ["Fillar", "Tuyalar", "Ipak qurti"], "Xitoyliklar «qonli ter to'kuvchi» otlarni xohlagan.", b="siyosiy"),
    C(2, "Xitoy sarkardasi Li Guangli Davonga qaysi yillarda yurish qilgan?", "Mil. avv. 104 va 102-yillar", ["Mil. avv. 329–327-yillar", "Mil. avv. 530-yil", "Mil. avv. 250-yil"], "104-yil muvaffaqiyatsiz, 102-yil g'alaba.", b="siyosiy"),
    C(2, "Davonning ikkinchi yirik markazi qaysi?", "Guyshan", ["Ershi", "Bityan", "Tuproqqal'a"], "Guyshan — Davonning yirik ikkinchi markazi.", b="siyosiy"),
    C(2, "Xitoy elchisi Chjan Szyan Davonga qaysi imperator topshirig'i bilan kelgan?", "Xan U-di", ["Qin Shixuandi", "Cay Lun", "Konfutsiy"], "Xan imperatori.", b="siyosiy"),
    C(3, "Davon–Xitoy urushlarining natijasi nima bo'ldi?", "Davon Xitoyga qaram bo'ldi, savdo aloqalari kengaydi", ["Davon Xitoyni bosib oldi", "Davon yo'q bo'lib ketdi", "Xitoy Davondan chekindi"], "102-yilda Davon taslim bo'ldi.", b="siyosiy"),
    O(3, "Xitoy sarkardasi Li Guangli Davonga muvaffaqiyatli yurishni qaysi yili amalga oshirgan? (yilni raqam bilan yozing, mil. avv.)", ["102", "102-yil", "mil. avv. 102"], "102-yil g'alabali yurish.", b="siyosiy"),
]

Q["6.1.24"] = [
    C(1, "Qang' davlati qaysi hududda joylashgan?", "Sirdaryo o'rta oqimi va Toshkent vohasi", ["Amudaryo quyi oqimi", "Farg'ona", "Zarafshon"], "Sirdaryo havzasi.", b="siyosiy"),
    C(1, "Qang'ning poytaxti qaysi shahar?", "Bityan", ["Ershi", "Baqtra", "Kat"], "Bityan.", b="siyosiy"),
    C(1, "Qang' davlati nechta kichik mulkka bo'lingan?", "Beshta", ["Ikkita", "Uchta", "Yettita"], "Besh mulk.", b="siyosiy"),
    C(2, "Xitoy manbalarida Qang' aholisi qanday ta'riflangan?", "Jangovar va erkin", ["Bo'ysunuvchan", "Faqat dehqon", "Ovchi"], "Jangovar xalq.", b="siyosiy"),
    C(2, "Qang' davlatining hukmron tabaqasi kimlar edi?", "Qang'lilarning ko'chmanchi-chorvador zodagonlari", ["Rim sarkardalari", "Yunon shoirlari", "Hind braxmanlari"], "Chorvador qang'lilar.", b="siyosiy"),
    C(2, "Qang' qaysi ikki yirik davlat o'rtasida joylashgan edi?", "Davon va Kushon (Sharq va G'arb savdo yo'lida)", ["Rim va Misr", "Misr va Hindiston", "Xitoy va Koreya"], "Ipak yo'li ustida.", b="siyosiy"),
    C(3, "Qang' davlatining asosiy mashg'uloti nima edi?", "Chorvachilik va dehqonchilik, shahar hunarmandchiligi", ["Dengizchilik", "Fil boqish", "Faqat ovchilik"], "Aralash xo'jalik.", b="siyosiy"),
    O(3, "Qang' davlatining poytaxti nomini yozing.", ["Bityan", "bityan"], "Bityan.", b="siyosiy"),
]

Q["6.1.25"] = [
    C(1, "Kushon podsholigiga kim asos solgan?", "Kujula Kadfiz", ["Kanishka", "Vima Kadfiz", "Diodot"], "Kujula Kadfiz besh mulkni birlashtirgan.", b="siyosiy"),
    C(1, "Kujula Kadfiz dastlab o'zini qanday atagan?", "Yabg'u (knyaz)", ["Shahanshoh", "Podsho", "Sulton"], "So'ng shahanshoh unvonini olgan.", b="siyosiy"),
    C(1, "Birinchi bo'lib oltin tanga zarb ettirgan kushon hukmdori kim?", "Vima Kadfiz", ["Kujula Kadfiz", "Kanishka", "Vasudeva"], "Oltin tanga.", b="siyosiy"),
    C(2, "Kushon imperiyasi markazi qayerda edi?", "Surxondaryo (Baqtriya)", ["Xorazm", "Farg'ona", "Toshkent"], "Janubiy O'zbekiston.", b="siyosiy"),
    C(2, "Vima Kadfiz davlat hududini qayergacha kengaytirgan?", "Hindistongacha", ["Rimgacha", "Misrgacha", "Yaponiyagacha"], "Shimoliy Hindiston.", b="siyosiy"),
    C(2, "Kushonlar qaysi qabila ittifoqi tarkibidan chiqqan?", "Yuechji qabilalari", ["Sak qabilalari", "Massagetlar", "Xunlar"], "Katta Yuechji ittifoqi.", b="siyosiy"),
    C(3, "Kujula Kadfiz tangalarida qaysi tillar uchraydi?", "Yunon va hind yozuvlari", ["Faqat arab", "Faqat xitoy", "Faqat lotin"], "Madaniy aralashuv.", b="siyosiy"),
    O(3, "Kushon podsholigining asoschisi bo'lgan hukmdorning to'liq ismini yozing (Kujula ...).", ["Kujula Kadfiz", "Kujula Kadfiz", "Kadfiz"], "Kujula Kadfiz.", b="siyosiy"),
]

Q["6.1.26"] = [
    C(1, "Kanishka I qaysi dinning homiysi bo'lgan?", "Buddizm", ["Xristianlik", "Islom", "Zardushtiylik"], "Buddizm davlat dini darajasiga ko'tarilgan.", b="madaniyat"),
    C(1, "Kanishka poytaxtni qayerga ko'chirgan?", "Purushapura (Peshovar)", ["Samarqand", "Baqtra", "Ershi"], "Purushapura.", b="siyosiy"),
    C(1, "«Kanishka erasi» qaysi yildan boshlangan?", "Milodiy 78-yildan", ["Mil. avv. 78-yildan", "Milodiy 622-yildan", "Milodiy 100-yildan"], "78-yil.", b="madaniyat"),
    C(2, "Kanishka chaqirgan buddizmning kengashi nechanchi?", "To'rtinchi", ["Birinchi", "Ikkinchi", "Uchinchi"], "4-kengash.", b="madaniyat"),
    C(2, "Kushonlar davrida mashhur bo'lgan san'at yo'nalishi qaysi?", "Gandxara san'ati", ["Barokko", "Gotika", "Renessans"], "Yunon-hind-baqtriya sintezi.", b="madaniyat"),
    C(2, "Termiz yaqinidagi buddaviy yodgorliklardan qaysi biri kushonlar davriga tegishli?", "Fayoztepa", ["Registon", "Ark", "Ichan Qal'a"], "Fayoztepa va Qoratepa.", b="madaniyat"),
    C(3, "Kanishka davrida Kushon imperiyasi qaysi hududlarni o'z ichiga olgan?", "O'rta Osiyo, Shimoliy Hindiston va Sharqiy Turkiston", ["Rim va Misr", "Xitoy va Koreya", "Eron va Iroq"], "Keng imperiya.", b="siyosiy"),
    O(3, "Kanishka davrida buddizmning to'rtinchi kengashi chaqirilgan va «Kanishka erasi» qaysi (milodiy) yildan boshlangan? (raqam)", ["78", "78-yil", "milodiy 78"], "78-yil.", b="siyosiy"),
]

Q["6.1.27"] = [
    C(1, "Tuproqqal'a qaysi davlat yodgorligi?", "Qadimgi Xorazm", ["Kushon", "Davon", "Qang'"], "Xorazmshohlar saroyi.", b="siyosiy"),
    C(1, "Tuproqqal'a qaysi hududda?", "Qoraqalpog'iston (Xorazm vohasi)", ["Surxondaryo", "Farg'ona", "Toshkent"], "Amudaryo quyi oqimi.", b="siyosiy"),
    C(1, "Tuproqqal'ani o'rgangan olim kim?", "S.P. Tolstov", ["A. Asqarov", "A.P. Okladnikov", "Ya. Gulomov"], "Xorazm ekspeditsiyasi.", b="siyosiy"),
    C(2, "Tuproqqal'a qaysi asrlarga oid?", "Milodiy III–IV asrlar", ["Mil. avv. VII asr", "XV asr", "X asr"], "Qadimgi Xorazm davri.", b="siyosiy"),
    C(2, "Tuproqqal'a saroyidan topilgan arxiv qaysi materialda yozilgan?", "Charm va yog'ochda (xorazmiy yozuv)", ["Papirusda", "Qog'ozda", "Loy lavhalarda mixxat"], "Xorazmiy yozuv.", b="siyosiy"),
    C(2, "Xorazmiy yozuv qaysi yozuv asosida paydo bo'lgan?", "Oromiy (aramey) yozuvi", ["Lotin yozuvi", "Ieroglif", "Arab yozuvi"], "Oromiy yozuvidan.", b="siyosiy"),
    C(3, "Afrig'iylar sulolasi Xorazmda qaysi asrdan hukmronlik qilgan?", "IV asr boshidan (305-yil)", ["I asr", "VIII asr", "XII asr"], "Afrig'iylar sulolasi.", b="siyosiy"),
    O(3, "Qadimgi Xorazmda Tuproqqal'a saroyi egasi bo'lgan hukmdorlar qaysi unvonda atalgan? (Xorazm...)", ["xorazmshoh", "Xorazmshoh"], "Xorazmshoh.", b="siyosiy"),
]

Q["6.1.28"] = [
    C(1, "Buyuk Ipak yo'li qaysi mamlakatlarni bog'lagan?", "Xitoy va Rimni", ["Misr va Hindistonni", "Yaponiya va Amerikani", "Rus va Eronni"], "Sharq–G'arb.", b="ijtimoiy"),
    C(1, "Ipak yo'li orqali Xitoydan nima keltirilgan?", "Ipak, chinni, qog'oz", ["Fil suyagi", "Paxta", "Oltin"], "Xitoy mahsulotlari.", b="ijtimoiy"),
    C(1, "Ipak yo'lining O'rta Osiyodagi yirik savdo shaharlaridan biri qaysi?", "Samarqand", ["Rim", "Afina", "Memfis"], "Samarqand.", b="ijtimoiy"),
    C(2, "«Buyuk Ipak yo'li» atamasini fanga kim kiritgan?", "Ferdinand fon Rixtgofen", ["Chjan Szyan", "Marko Polo", "Gerodot"], "1877-yil.", b="ijtimoiy"),
    C(2, "Ipak yo'lining ochilishiga turtki bergan Xitoy elchisi kim?", "Chjan Szyan", ["Li Guangli", "Spitamen", "Kanishka"], "Mil. avv. II asr.", b="ijtimoiy"),
    C(2, "Ipak yo'li orqali Sharqqa nima tarqalgan?", "Dinlar, g'oyalar, fan yutuqlari", ["Faqat ipak", "Faqat mevalar", "Faqat qurol"], "Madaniy almashinuv.", b="ijtimoiy"),
    C(3, "Ipakchilik sirini Vizantiyaga 552-yilda kim yetkazgan?", "Monaxlar (rohiblar)", ["Savdogarlar", "Sarkardalar", "Elchilar"], "Imperator Yustinian davrida.", b="ijtimoiy"),
    O(3, "«Buyuk Ipak yo'li» Xitoyning qaysi qadimiy poytaxtidan boshlangan? (Chang...)", ["Chang'an", "changan", "Chanan"], "Chang'an (Syan).", b="ijtimoiy"),
]

Q["6.1.29"] = [
    C(1, "Qadimgi Misr qaysi daryo bo'yida vujudga kelgan?", "Nil", ["Dajla", "Hind", "Xuanxe"], "Nil.", b="madaniyat"),
    C(1, "Misr hukmdorlari qanday ataladi?", "Fir'avn", ["Shoh", "Sulton", "Imperator"], "Fir'avn.", b="madaniyat"),
    C(1, "Misrdagi eng mashhur me'moriy obida?", "Piramidalar", ["Kolizey", "Parfenon", "Buyuk Xitoy devori"], "Xeops piramidasi.", b="madaniyat"),
    C(2, "Misr yozuvi qanday nomlanadi?", "Ieroglif", ["Mixxat", "Lotin", "Oromiy"], "Ieroglif.", b="madaniyat"),
    C(2, "Misr ieroglifini 1822-yilda o'qigan olim kim?", "Jan Fransua Shampolyon", ["Govard Karter", "Gerodot", "Gomer"], "Rozetta toshi orqali.", b="madaniyat"),
    C(2, "Misrliklar yozuv uchun nimadan foydalanishgan?", "Papirus", ["Qog'oz", "Pergament", "Loy lavha"], "Papirus.", b="madaniyat"),
    C(3, "Tutanxamon maqbarasi 1922-yilda kim tomonidan topilgan?", "Govard Karter", ["Shampolyon", "Tolstov", "Okladnikov"], "Ingliz arxeologi.", b="madaniyat"),
    O(3, "Misrdagi eng katta piramida kim nomi bilan (Xeops yoki Xufu) ataladi? Biror nomni yozing.", ["Xeops", "Xufu", "Xeops piramidasi"], "Giza.", b="madaniyat"),
]

Q["6.1.30"] = [
    C(1, "Mesopotamiya qaysi ikki daryo oralig'ida joylashgan?", "Dajla va Frot", ["Nil va Kongo", "Hind va Gang", "Amudaryo va Sirdaryo"], "Ikki daryo oralig'i.", b="madaniyat"),
    C(1, "Mesopotamiyada qaysi xalq yozuvni ixtiro qilgan?", "Shumerlar", ["Misrliklar", "Xitoyliklar", "Hindlar"], "Mixxat.", b="madaniyat"),
    C(1, "Mixxat yozuvi nimaga yozilgan?", "Loy lavhalarga", ["Papirusga", "Pergamentga", "Qog'ozga"], "Loy lavhalarga yozilgan.", b="madaniyat"),
    C(2, "Bobil podshosi Hammurapi nima bilan mashhur?", "Qonunlar to'plami bilan", ["Piramidalar bilan", "Olimpiya o'yinlari bilan", "Buyuk devor bilan"], "Hammurapi qonunlari.", b="madaniyat"),
    C(2, "«Gilgamesh» dostoni qaysi xalqning adabiy yodgorligi?", "Shumer–Akkad (Mesopotamiya)", ["Hind", "Xitoy", "Misr"], "Eng qadimgi doston.", b="madaniyat"),
    C(2, "Mesopotamiyaning 60 lik sanoq tizimi nimada saqlanib qolgan?", "Soat va daqiqa, burchak hisobi", ["Pul hisobida", "Og'irlik o'lchovida", "Yil hisobida"], "60 daqiqa, 60 soniya.", b="madaniyat"),
    C(3, "Hammurapi qonunlari qaysi asrga mansub?", "Mil. avv. XVIII asr", ["Mil. avv. VII asr", "Milodiy I asr", "Mil. avv. V asr"], "Taxminan 1792–1750.", b="madaniyat"),
    O(3, "Bobil osma bog'larini mashhur qilgan podsho (Navuxodonosor II). Uning ismini yozing (Navuxodonosor yoki Nabukodonosor).", ["Navuxodonosor", "Nabukodonosor", "Navuxodonosor II", "Nabuxodonosor"], "Bobil.", b="madaniyat"),
]

Q["6.1.31"] = [
    C(1, "Qadimgi Hindiston qaysi daryolar vodiysida vujudga kelgan?", "Hind va Gang", ["Nil va Dajla", "Amudaryo va Sirdaryo", "Xuanxe va Yanszi"], "Hind va Gang.", b="madaniyat"),
    C(1, "Hindistonda jamiyat nechta varnaga bo'lingan?", "To'rtta", ["Ikkita", "Uchta", "Oltita"], "Braxman, kshatriy, vayshiy, shudra.", b="madaniyat"),
    C(1, "Hindistondagi eng yuqori varna kimlar?", "Braxmanlar (ruhoniylar)", ["Shudralar", "Vayshiylar", "Kshatriylar"], "Ruhoniylar.", b="madaniyat"),
    C(2, "Budda ta'limotining asoschisi kim?", "Siddxartxa Gautama", ["Zardusht", "Konfutsiy", "Mahavira"], "Budda.", b="madaniyat"),
    C(2, "Hindiston dostonlari qaysilar?", "«Mahabharata» va «Ramayana»", ["«Iliada» va «Odisseya»", "«Gilgamesh»", "«Avesto»"], "Qadimgi hind dostonlari.", b="madaniyat"),
    C(2, "Hind vodiysidagi qadimgi shaharlar qaysilar?", "Xarappa va Moxenjo-Daro", ["Ur va Uruk", "Afina va Sparta", "Memfis va Fiva"], "Hind sivilizatsiyasi.", b="madaniyat"),
    C(3, "Hindistonda mil. avv. III asrda mashhur bo'lgan Maurya podshosi kim?", "Ashoka", ["Kanishka", "Kir", "Doro"], "Ashoka buddizmni qo'llab-quvvatlagan.", b="madaniyat"),
    O(3, "Raqamlarni va «nol» belgisini dunyoga bergan qadimiy mamlakat nomini yozing.", ["Hindiston", "hindiston"], "Hind raqamlari.", b="madaniyat"),
]

Q["6.1.32"] = [
    C(1, "Qadimgi Xitoy qaysi daryolar bo'yida vujudga kelgan?", "Xuanxe va Yanszi", ["Nil va Zambezi", "Hind va Gang", "Dajla va Frot"], "Sariq daryo va Yanszi.", b="madaniyat"),
    C(1, "Xitoyni birlashtirgan imperator kim?", "Qin Shixuandi", ["Konfutsiy", "Cay Lun", "Xan U-di"], "Mil. avv. 221.", b="madaniyat"),
    C(1, "Buyuk Xitoy devori nima uchun qurilgan?", "Shimoldagi ko'chmanchilardan himoya uchun", ["Savdo uchun", "Sug'orish uchun", "Dengizdan himoya uchun"], "Mudofaa.", b="madaniyat"),
    C(2, "Qog'ozni ixtiro qilgan xitoylik kim?", "Cay Lun", ["Konfutsiy", "Qin Shixuandi", "Chjan Szyan"], "105-yil.", b="madaniyat"),
    C(2, "Konfutsiy ta'limoti nimani targ'ib qiladi?", "Hurmat, odob va tartibni", ["Urushni", "Boylikni", "Ko'chmanchilikni"], "Axloqiy ta'limot.", b="madaniyat"),
    C(2, "Xitoyda ixtiro qilingan narsalarni toping.", "Qog'oz, ipak, kompas, porox", ["Shisha, temir yo'l", "Bosmaxona, telefon", "Paxta, shakar"], "Buyuk ixtirolar.", b="madaniyat"),
    C(3, "Qin Shixuandi maqbarasida nima topilgan?", "Sopol askarlar (terrakota armiyasi)", ["Piramidalar", "Mumiyalar", "Osma bog'lar"], "Terrakota armiyasi.", b="madaniyat"),
    O(3, "Xitoyni mil. avv. 221-yilda birlashtirgan imperator ismini yozing (Qin ...).", ["Qin Shixuandi", "Shixuandi", "Qin Shi Xuandi", "Tsin Shi Xuandi"], "Qin Shixuandi.", b="madaniyat"),
]

Q["6.1.33"] = [
    C(1, "Qadimgi Yunonistonda shahar-davlatlar qanday atalgan?", "Polis", ["Satrapiya", "Nom", "Ulus"], "Polis.", b="madaniyat"),
    C(1, "Demokratiya qaysi polisda rivojlangan?", "Afinada", ["Spartada", "Fivada", "Korinfda"], "Afina.", b="madaniyat"),
    C(1, "Qadimgi Olimpiya o'yinlari qachon boshlangan?", "Mil. avv. 776-yilda", ["Mil. avv. 490-yilda", "Mil. avv. 331-yilda", "Mil. avv. 323-yilda"], "776.", b="madaniyat"),
    C(2, "Yunonlar bilan forslar o'rtasidagi mashhur jang qaysi?", "Marafon jangi (490)", ["Gavgamela", "Kann", "Terek"], "490-yil.", b="madaniyat"),
    C(2, "«Iliada» va «Odisseya» muallifi kim?", "Gomer", ["Gerodot", "Sofokl", "Aristotel"], "Gomer.", b="madaniyat"),
    C(2, "Tarixning otasi hisoblangan yunon tarixchisi kim?", "Gerodot", ["Gomer", "Platon", "Sokrat"], "Gerodot.", b="madaniyat"),
    C(3, "Termopil dovonida 300 spartalik bilan forslarga qarshi turgan podsho kim?", "Leonid", ["Perikl", "Filipp II", "Doro"], "Mil. avv. 480.", b="madaniyat"),
    O(3, "Afina Akropolidagi Afina ibodatxonasining nomini yozing (P...).", ["Parfenon", "parfenon"], "Parfenon.", b="madaniyat"),
]

Q["6.1.34"] = [
    C(1, "Rim shahrining asos solinishi rivoyatda kim nomi bilan bog'lanadi?", "Romul va Rem", ["Sezar va Pompey", "Spartak va Krass", "Neron va Trayan"], "753.", b="madaniyat"),
    C(1, "Rim qaysi yilda respublikaga aylangan?", "Mil. avv. 509-yilda", ["Mil. avv. 753-yilda", "Mil. avv. 27-yilda", "Milodiy 476-yilda"], "509.", b="madaniyat"),
    C(1, "Rim imperiyasining birinchi imperatori kim?", "Oktavian Avgust", ["Yuliy Sezar", "Neron", "Trayan"], "Mil. avv. 27.", b="madaniyat"),
    C(2, "Rimdagi mashhur gladiatorlar qo'zg'olonini kim boshqargan?", "Spartak", ["Gannibal", "Sezar", "Brut"], "73–71.", b="madaniyat"),
    C(2, "Rimning mashhur amfiteatri qaysi?", "Kolizey", ["Parfenon", "Akropol", "Pantheon"], "Kolizey.", b="madaniyat"),
    C(2, "G'arbiy Rim imperiyasi qaysi yili qulagan?", "476-yilda", ["395-yilda", "27-yilda", "1453-yilda"], "476.", b="madaniyat"),
    C(3, "Rim bilan Karfagen o'rtasida bo'lgan urushlar qanday ataladi?", "Puni urushlari", ["Gall urushlari", "Peloponnes urushlari", "Salb yurishlari"], "Gannibal.", b="madaniyat"),
    O(3, "Rim imperiyasi qaysi yilda ikkiga (G'arbiy va Sharqiy) bo'lingan? (yilni raqam bilan yozing)", ["395", "395-yil"], "395.", b="madaniyat"),
]
