"""Biologiya: 8-sinf (Odam), 9-sinf (Sitologiya), 10-sinf (Genetika, evolyutsiya), 11-sinf (Geoxronologiya, masalalar)."""
from ._dsl import C, O, M

Q = {}

# ---------------------------------------------------------------- 8-SINF
Q["B8.1"] = [
    C(1, "Impulsni neyron tanasiga olib keluvchi qisqa shoxlangan o'simta qaysi?", "Dendrit", ["Akson", "Sinaps", "Mediator"], "Dendrit impulsni tanaga olib keladi."),
    C(1, "Impulsni neyron tanasidan olib ketuvchi uzun o'simta qaysi?", "Akson", ["Dendrit", "Sinaps", "Reseptor"], "Akson — uzun, mielin qobiqli."),
    C(1, "Sinapsda impuls qanday moddalar yordamida o'tadi?", "Mediatorlar (atsetilxolin, noradrenalin)", ["Gormonlar", "Fermentlar", "Vitaminlar"], "Sinapsda kimyoviy uzatish bo'ladi."),
    M(2, [("Dendrit", "Impulsni tanaga olib keladi"), ("Akson", "Impulsni tanadan olib ketadi"), ("Sinaps", "Neyronlar orasidagi aloqa joyi")], "Neyron va sinaps."),
    C(2, "Sezuvchi neyron boshqacha qanday ataladi?", "Afferent neyron", ["Efferent neyron", "Oraliq neyron", "Effektor"], "Afferent — markazga olib boradi."),
    C(2, "Refleks yoyidagi effektor nima?", "Ishchi a'zo", ["Reseptor", "Oraliq neyron", "Sezuvchi neyron"], "Effektor — javob beruvchi a'zo."),
    C(2, "Refleks yoyining to'g'ri tartibini toping.", "Reseptor → sezuvchi neyron → oraliq neyron → harakatlantiruvchi neyron → effektor", ["Reseptor → harakatlantiruvchi neyron → oraliq neyron → sezuvchi neyron → effektor", "Effektor → sezuvchi neyron → oraliq neyron → reseptor", "Sezuvchi neyron → reseptor → effektor → oraliq neyron"], "Refleks yoyi zanjiri."),
    C(2, "Harakatlantiruvchi neyron boshqacha qanday ataladi?", "Efferent neyron", ["Afferent neyron", "Oraliq neyron", "Reseptor"], "Efferent — markazdan a'zoga."),
    C(3, "Quyidagilardan qaysi biri refleks yoyining markaziy qismi?", "Markaziy nerv tizimidagi oraliq neyron", ["Reseptor", "Effektor", "Sezuvchi neyronning dendriti"], "Markaziy bo'lim oraliq neyrondan iborat."),
    O(3, "Sinapsda impulsni uzatuvchi moddalarning umumiy nomini yozing.", ["mediator", "mediatorlar"], "Mediatorlar."),
    O(3, "Neyron tanasidan impulsni olib ketuvchi o'simta nomini yozing.", ["akson"], "Akson."),
]

Q["B8.2"] = [
    C(1, "Nafas olish va yurak urishini boshqaruvchi hayotiy markazlar qaysi bo'limda?", "Uzunchoq miya", ["Miyacha", "O'rta miya", "Talamus"], "Uzunchoq miya — hayotiy markazlar."),
    C(1, "Tana muvozanati va harakatlar koordinatsiyasini qaysi bo'lim boshqaradi?", "Miyacha", ["Uzunchoq miya", "Gipotalamus", "Miya ko'prigi"], "Miyacha."),
    C(1, "Ko'rish zonasi katta yarimsharlarning qaysi bo'lagida?", "Ensa bo'lagi", ["Chakka bo'lagi", "Tepalik bo'lagi", "Peshtoq bo'lagi"], "Ensa — ko'rish."),
    M(2, [("Uzunchoq miya", "Yo'tal va aks urish reflekslari"), ("Miyacha", "Tana muvozanati"), ("O'rta miya", "Orientatsiya refleksi")], "Miya bo'limlari funksiyalari."),
    C(2, "Eshitish va hid bilish zonalari qaysi bo'lakda?", "Chakka bo'lagi", ["Ensa bo'lagi", "Tepalik bo'lagi", "Peshtoq bo'lagi"], "Chakka bo'lagi."),
    C(2, "Gomeostaz, termoregulyatsiya, chanqash va ochlik markazi qaysi?", "Gipotalamus", ["Talamus", "Miyacha", "Miya ko'prigi"], "Gipotalamus — oraliq miyada."),
    C(2, "Sezgi yo'llarining kollektori vazifasini qaysi struktura bajaradi?", "Talamus", ["Gipotalamus", "Miyacha", "Uzunchoq miya"], "Hid bilishdan tashqari barcha sezgilar talamusda filtrlanadi."),
    C(2, "Fikrlash, ixtiyoriy harakat va nutq markazi qaysi bo'lakda?", "Peshtoq bo'lagi", ["Ensa bo'lagi", "Chakka bo'lagi", "Tepalik bo'lagi"], "Peshtoq bo'lak."),
    C(3, "Qaysi sezgi talamusda filtrlanmaydi?", "Hid bilish", ["Ko'rish", "Eshitish", "Teri sezgisi"], "Hid bilishdan tashqari barcha sezgilar talamusda filtrlanadi."),
    O(3, "Teri-mushak sezgisi zonasi katta yarimsharlarning qaysi bo'lagida joylashgan? (bo'lak nomi)", ["tepalik", "tepalik bo'lagi", "tepa", "tepa bo'lagi"], "Tepalik bo'lagi."),
    O(3, "Keskin tovush yoki yorug'likka boshni burish refleksi nomini yozing.", ["orientatsiya refleksi", "orientatsiya"], "O'rta miyaning birlamchi refleksi."),
]

Q["B8.3"] = [
    C(1, "Qon tarkibida plazma necha foizni tashkil qiladi?", "55%", ["45%", "70%", "90%"], "Shaklli elementlar 45%."),
    C(1, "Gemoglobin qaysi qon hujayrasida bor?", "Eritrotsitda", ["Leykotsitda", "Trombotsitda", "Plazmada"], "Eritrotsit kislorod va CO₂ tashiydi."),
    C(1, "Fagotsitozni kashf etgan olim kim?", "I.I. Mechnikov", ["L. Paster", "I. Pavlov", "R. Guk"], "Mechnikov leykotsitlarning himoya vazifasini kashf etgan."),
    M(2, [("Eritrotsit", "4,5–5 mln ta (1 mm³)"), ("Leykotsit", "6–8 ming ta (1 mm³)"), ("Trombotsit", "200–300 ming ta (1 mm³)")], "Qon hujayralari soni."),
    C(2, "Eritrotsitlar tuzilishi qanday?", "Yadrosiz, ikki tomoni botiq disk", ["Yadroli, amyobasimon", "Yadrosiz plastinka", "Yadroli, sharsimon"], "Yetilganda yadro yo'qoladi."),
    C(2, "Leykotsitlar xususiyati qaysi?", "Yadroli, shakli o'zgaruvchan", ["Yadrosiz, disksimon", "Yadrosiz plastinka", "Gemoglobinli"], "Amyobasimon harakat qiladi."),
    C(2, "Qon ivishida qaysi modda fibrin iplariga aylanadi?", "Fibrinogen", ["Gemoglobin", "Insulin", "Albumin"], "Fibrinogen → fibrin."),
    C(2, "Trombotsitlar nima?", "Yadrosiz plastinkalar; qon ivishida qatnashadi", ["Yadroli himoya hujayralari", "Kislorod tashuvchi hujayralar", "Gormonlar"], "Qon ivishi vazifasi."),
    C(3, "Qonning shaklli elementlari qancha foizni tashkil qiladi?", "45%", ["55%", "30%", "90%"], "Plazma 55%, shaklli elementlar 45%."),
    O(3, "Fagotsitozni kashf etgan olimning familiyasini yozing.", ["mechnikov", "mechnikov i.i.", "i.i. mechnikov", "ilya mechnikov"], "I.I. Mechnikov."),
    O(3, "1 mm³ qonda 5 mln eritrotsit bor. 2 mm³ qonda necha mln eritrotsit bo'ladi? (son)", ["10", "10 mln"], "5 × 2 = 10 mln."),
]

Q["B8.4"] = [
    C(1, "Yurak sikli necha soniya davom etadi?", "0,8 soniya", ["0,4 soniya", "1 soniya", "0,3 soniya"], "0,1 + 0,3 + 0,4 = 0,8."),
    C(1, "Bo'lmachalar sistolasi necha soniya?", "0,1 soniya", ["0,3 soniya", "0,4 soniya", "0,8 soniya"], "Bo'lmachalar sistolasi 0,1 s."),
    C(1, "Umumiy diastola necha soniya?", "0,4 soniya", ["0,1 soniya", "0,3 soniya", "0,8 soniya"], "Umumiy diastola 0,4 s."),
    M(2, [("Bo'lmachalar sistolasi", "0,1 soniya"), ("Qorinchalar sistolasi", "0,3 soniya"), ("Umumiy diastola", "0,4 soniya")], "Yurak sikli fazalari."),
    C(2, "Qorinchalar sistolasi necha soniya davom etadi?", "0,3 soniya", ["0,1 soniya", "0,4 soniya", "0,5 soniya"], "Qorinchalar sistolasi 0,3 s."),
    C(2, "Birinchi ton qaysi klapanlar yopilishidan hosil bo'ladi?", "Tavaqali klapanlar", ["Yarim oysimon klapanlar", "Aorta qopqog'i", "Venalar klapani"], "1-ton — tavaqali klapanlar."),
    C(2, "Qorinchalar sistolasida klapanlar holati qanday?", "Tavaqali yopiq, yarim oysimon ochiq", ["Tavaqali ochiq, yarim oysimon yopiq", "Ikkalasi ham ochiq", "Ikkalasi ham yopiq"], "Qon aorta va o'pka arteriyasiga ketadi."),
    C(2, "Ikkinchi ton qaysi klapanlar yopilishidan hosil bo'ladi?", "Yarim oysimon klapanlar", ["Tavaqali klapanlar", "Venalar klapani", "Bikuspidal"], "2-ton — yarim oysimon klapanlar."),
    C(3, "Umumiy diastolada qon qanday harakatlanadi?", "Venalardan bo'lmacha va qorinchalarga", ["Qorinchalardan aortaga", "Bo'lmachalardan qorinchalarga faqat", "Aortadan venaga"], "Tavaqali ochiq, yarim oysimon yopiq."),
    O(3, "Yurak daqiqasiga 75 marta ursa, bitta sikl necha soniya davom etadi? (son)", ["0,8", "0.8"], "60 : 75 = 0,8 s."),
    O(3, "Bir yurak siklida qorinchalar necha soniya dam oladi? (son)", ["0,5", "0.5"], "0,8 − 0,3 = 0,5 s."),
]

Q["B8.5"] = [
    C(1, "Insulin yetishmasligidan qaysi kasallik kelib chiqadi?", "Diabet", ["Bazedov kasalligi", "Gigantizm", "Kretenizm"], "Insulin qand miqdorini kamaytiradi."),
    C(1, "O'sish gormoni qaysi bezda hosil bo'ladi?", "Gipofizda", ["Qalqonsimon bezda", "Buyrak ustida", "Me'da osti bezida"], "Gipofiz — bosh miyadagi bez."),
    C(1, "Bazedov kasalligi qaysi bez faoliyati bilan bog'liq?", "Qalqonsimon bez (gormoni ko'p)", ["Gipofiz", "Me'da osti bezi", "Buyrak usti bezi"], "Tiroksin ortiqcha."),
    M(2, [("Gigantizm", "Bolalikda o'sish gormoni ortiqcha"), ("Mittilik", "Bolalikda o'sish gormoni kam"), ("Akromegaliya", "Kattalarda o'sish gormoni ortiqcha")], "Gipofiz buzilishlari."),
    C(2, "Gigantizm sababi nima?", "Bolalikda o'sish gormonining ortiqcha ishlanishi", ["Bolalikda o'sish gormoni yetishmasligi", "Kattalarda gormon ortiqcha ishlanishi", "Insulin yetishmasligi"], "Gigantizm — bolalikdagi giperfunksiya."),
    C(2, "Mittilik sababi nima?", "Bolalikda o'sish gormoni yetishmasligi", ["Bolalikda o'sish gormoni ortiqchaligi", "Tiroksin ortiqchaligi", "Insulin ortiqchaligi"], "Gipofiz gipofunksiyasi."),
    C(2, "Akromegaliya qachon rivojlanadi?", "Kattalarda o'sish gormoni ortiqcha ishlanganda", ["Bolalikda gormon kam bo'lganda", "Bolalikda gormon ortiq bo'lganda", "Insulin kam bo'lganda"], "Kattalardagi giperfunksiya."),
    C(2, "Kretenizm sababi nima?", "Bolalikda qalqonsimon bez gormoni yetishmasligi", ["Bolalikda o'sish gormoni ortiqcha", "Insulin yetishmasligi", "Adrenalin ortiqcha"], "Qalqonsimon bez gipofunksiyasi."),
    C(3, "Miksedema qaysi holatda kuzatiladi?", "Kattalarda qalqonsimon bez gormoni yetishmasligida", ["Bolalikda tiroksin ortiqchaligida", "Insulin yetishmasligida", "Kattalarda o'sish gormoni ortiqchaligida"], "Miksedema — kattalardagi gipotireoz."),
    O(3, "Insulin hosil qiluvchi bez nomini yozing.", ["me'da osti bezi", "me'da osti", "oshqozon osti bezi", "oshqozon osti"], "Me'da osti bezi."),
    O(3, "Adrenalin qaysi bezda ishlab chiqariladi?", ["buyrak usti bezi", "buyrak usti", "buyrakusti bezi"], "Buyrak usti bezi."),
]

# ---------------------------------------------------------------- 9-SINF
Q["B9.1"] = [
    C(1, "Oqsil monomeri nima?", "Aminokislota", ["Nukleotid", "Glyukoza", "Yog' kislotasi"], "Oqsil aminokislotalardan tuzilgan."),
    C(1, "Aminokislotalarni bog'lovchi bog' qaysi?", "Peptid bog' (–CO–NH–)", ["Disulfid bog'", "Vodorod bog'", "Efir bog'"], "Peptid bog'."),
    C(1, "Oqsillarda necha xil aminokislota uchraydi?", "20", ["4", "64", "100"], "Standart 20 xil aminokislota."),
    M(2, [("Birlamchi tuzilma", "Peptid zanjir"), ("Ikkilamchi tuzilma", "Spiral (vodorod bog'lar)"), ("Uchlamchi tuzilma", "Globula (disulfid bog'lar)")], "Oqsil tuzilmalari."),
    C(2, "Ikkilamchi tuzilmani qanday bog'lar saqlaydi?", "Vodorod bog'lar", ["Disulfid bog'lar", "Peptid bog'lar", "Efir bog'lar"], "Spiral shakli."),
    C(2, "Disulfid (–S–S–) bog'lari qaysi tuzilmada hosil bo'ladi?", "Uchlamchi", ["Birlamchi", "Ikkilamchi", "Faqat to'rtlamchi"], "Globula/tuyum."),
    C(2, "Gemoglobin oqsili qaysi tuzilmaga misol?", "To'rtlamchi", ["Birlamchi", "Ikkilamchi", "Uchlamchi"], "Bir necha globula kompleksi."),
    C(2, "Denaturatsiya nima?", "Oqsil tabiatining o'zgarishi (qaytar yoki qaytmas)", ["Oqsilning sintezi", "Oqsilning hazmi", "Oqsilning tashilishi"], "Tuzilma buzilishi."),
    C(3, "Disulfid bog'lari buzilganda oqsilning qaysi tuzilmasi dastlab buziladi?", "Uchlamchi", ["Birlamchi", "Peptid zanjir", "Aminokislota tarkibi"], "Disulfid – uchlamchi tuzilma bog'i."),
    O(3, "150 ta aminokislotadan iborat bitta zanjirli oqsilda nechta peptid bog' bor? (son)", ["149"], "n − 1 = 149."),
    O(3, "200 ta aminokislotali oqsilning o'rtacha massasi necha d.m.? (aminokislota = 110 d.m., faqat son)", ["22000", "22 000"], "200 × 110 = 22000."),
]

Q["B9.2"] = [
    C(1, "Nukleotid tarkibi qaysi javobda to'g'ri?", "Azotli asos + uglevod + fosfat qoldig'i", ["Aminokislota + uglevod + fosfat", "Azotli asos + yog' + fosfat", "Uglevod + oqsil + fosfat"], "Nukleotid tarkibi."),
    C(1, "A va T orasida nechta vodorod bog' bor?", "2 ta", ["3 ta", "1 ta", "4 ta"], "A=T."),
    C(1, "G va C orasida nechta vodorod bog' bor?", "3 ta", ["2 ta", "1 ta", "4 ta"], "G≡C."),
    M(2, [("A=T", "2 ta vodorod bog'"), ("G≡C", "3 ta vodorod bog'"), ("DNK uglevodi", "Dezoksiriboza")], "Komplementarlik."),
    C(2, "DNK va RNK uglevodlari to'g'ri berilgan javob qaysi?", "DNK — dezoksiriboza, RNK — riboza", ["DNK — riboza, RNK — dezoksiriboza", "Ikkalasida ham riboza", "Ikkalasida ham glyukoza"], "Uglevodlar farqi."),
    C(2, "Chargaff qoidasiga ko'ra (A+G)/(T+C) nimaga teng?", "1 ga", ["2 ga", "0,5 ga", "3 ga"], "A=T, G=C."),
    C(2, "DNKda adenin 20% bo'lsa, guanin necha foiz?", "30%", ["20%", "40%", "60%"], "A=T=20%, G=C=30%."),
    C(2, "Nuklein kislotalarning monomeri nima?", "Nukleotid", ["Aminokislota", "Monosaxarid", "Yog' kislotasi"], "Nukleotid."),
    C(3, "DNKda 400 ta nukleotid, 60 tasi adenin. Guaninlar soni nechta?", "140", ["60", "100", "280"], "A=T=60, G=C=(400−120)/2=140."),
    O(3, "DNKda jami 400 ta nukleotid, adenin 60 ta. Vodorod bog'lari soni nechta? (H = 2A + 3G, son)", ["540"], "G=140; H = 120 + 420 = 540."),
    O(3, "DNKda jami 600 ta nukleotid va G = 200 ta bo'lsa, vodorod bog'lari soni nechta? (H = N + G, son)", ["800"], "600 + 200 = 800."),
]

Q["B9.3"] = [
    C(1, "Glikoliz hujayraning qayerida boradi?", "Sitoplazmada", ["Mitoxondriyada", "Yadroda", "Ribosomada"], "Kislorodsiz bosqich."),
    C(1, "Aerob bosqich qayerda boradi?", "Mitoxondriya kristalarida", ["Sitoplazmada", "Yadroda", "Lizosomada"], "Kislorodli bosqich."),
    C(1, "Glyukoza to'liq parchalanganda jami nechta ATF hosil bo'ladi?", "38", ["2", "36", "40"], "2 + 36 = 38."),
    M(2, [("Tayyorgarlik bosqichi", "100% issiqlik, ATF hosil bo'lmaydi"), ("Glikoliz", "2 mol ATF"), ("Aerob bosqich", "36 mol ATF")], "Energiya almashinuvi."),
    C(2, "Glikolizda nechta ATF hosil bo'ladi?", "2 ta", ["36 ta", "38 ta", "0 ta"], "Glikoliz — 2 ATF."),
    C(2, "Aerob bosqichda nechta ATF hosil bo'ladi?", "36 ta", ["2 ta", "38 ta", "4 ta"], "Aerob — 36 ATF."),
    C(2, "Tayyorgarlik bosqichida energiya qanday sarflanadi?", "Butunlay issiqlik bo'lib tarqaladi", ["ATFda to'planadi", "Yarmi ATFda to'planadi", "NADHga o'tadi"], "ATF hosil bo'lmaydi."),
    C(2, "Glikolizning mahsuloti qaysi?", "2 mol sut kislotasi", ["6 mol CO₂", "2 mol glyukoza", "36 mol ATF"], "Glikoliz mahsuloti sut kislotasi."),
    C(3, "Glyukozaning to'liq parchalanishida jami qancha energiya ajraladi?", "2800 kJ", ["200 kJ", "2600 kJ", "1440 kJ"], "200 + 2600 = 2800 kJ."),
    O(3, "3 mol glyukoza to'liq parchalanganda necha mol ATF hosil bo'ladi? (son)", ["114"], "3 × 38 = 114."),
    O(3, "2 mol glyukoza to'liq parchalanganda aerob bosqichda necha mol CO₂ hosil bo'ladi? (son)", ["12"], "1 mol glyukozadan 6 mol CO₂; 2 mol dan 12."),
]

Q["B9.4"] = [
    C(1, "Mitoz natijasida nechta hujayra hosil bo'ladi?", "2 ta", ["4 ta", "1 ta", "8 ta"], "Mitoz — 2 ta bir xil hujayra."),
    C(1, "Meyoz natijasida nechta hujayra hosil bo'ladi?", "4 ta", ["2 ta", "1 ta", "8 ta"], "Meyozda 4 ta gaploid hujayra."),
    C(1, "Quyidagilardan qaysi organoid membranasiz?", "Ribosoma", ["Mitoxondriya", "Lizosoma", "Goldji apparati"], "Ribosoma membranasiz."),
    M(2, [("Ribosoma", "Membranasiz"), ("Lizosoma", "Bir membranali"), ("Mitoxondriya", "Ikki membranali")], "Organoidlar membranasi."),
    C(2, "Ikki membranali organoidlar qaysi javobda to'g'ri?", "Mitoxondriya va plastidalar", ["Ribosoma va lizosoma", "EPS va Goldji", "Hujayra markazi va ribosoma"], "Ikki membranali: mitoxondriya, plastida, yadro."),
    C(2, "Mitozning qaysi fazasida xromosomalar ekvator tekisligida joylashadi?", "Metafaza", ["Profaza", "Anafaza", "Telofaza"], "Metafaza."),
    C(2, "Meyoz natijasida hosil bo'ladigan hujayralar xromosoma to'plami qanday?", "Gaploid (n)", ["Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"], "Gametalar gaploid."),
    C(2, "Mitozning qaysi fazasida xromatidalar qutblarga tortiladi?", "Anafaza", ["Profaza", "Metafaza", "Telofaza"], "Anafaza."),
    C(3, "DNK ikki hissa ortishi (replikatsiya) hujayra siklining qaysi davrida bo'ladi?", "Interfazaning S davrida", ["Profazada", "Anafazada", "Telofazada"], "S davri — sintez."),
    O(3, "Odam somatik hujayrasida 46 ta xromosoma bor. Meyoz oxirida hosil bo'lgan gametada nechta xromosoma bo'ladi? (son)", ["23"], "46/2 = 23."),
    O(3, "2n = 8 bo'lgan hujayrada mitoz anafazasida nechta xromosoma bo'ladi? (son)", ["16"], "Xromatidalar ajralib, xromosomalar soni ikki baravar."),
]

# ---------------------------------------------------------------- 10-SINF
Q["B10.1"] = [
    C(1, "Komplementarlikda gullar rangi bo'yicha belgilanish nisbati qaysi?", "9:7", ["13:3", "15:1", "12:3:1"], "Komplementarlik: 9:7, 9:3:4, 9:6:1."),
    C(1, "Kumulyativ polimeriyada F₂ da fenotip nisbati qaysi?", "15:1", ["9:7", "9:3:4", "13:3"], "Polimeriya: 15:1 yoki 63:1."),
    C(1, "Bir genning boshqa allel bo'lmagan gen ta'sirini bostirishi nima deyiladi?", "Epistaz", ["Komplementarlik", "Polimeriya", "Kodominantlik"], "Epistaz."),
    M(2, [("Komplementarlik (gul rangi)", "9:7"), ("Dominant epistaz", "13:3"), ("Kumulyativ polimeriya", "15:1")], "Allel bo'lmagan genlar ta'siri nisbatlari."),
    C(2, "Qovoq shakli bo'yicha komplementar nisbat qaysi?", "9:6:1", ["9:7", "9:3:4", "15:1"], "Qovoq shakli — 9:6:1."),
    C(2, "Sichqonlar yungi rangida komplementar nisbat qaysi?", "9:3:4", ["9:7", "9:6:1", "13:3"], "9:3:4."),
    C(2, "Tovuqlar patining rangi dominant epistaz bo'yicha qaysi nisbat bilan?", "13:3 yoki 12:3:1", ["9:7", "15:1", "9:6:1"], "Dominant epistaz."),
    C(2, "Bombey fenomeni qaysi epistaz turiga kiradi?", "Retsessiv epistaz (9:3:4)", ["Dominant epistaz (13:3)", "Polimeriya (15:1)", "Komplementarlik (9:7)"], "Retsessiv epistaz."),
    C(3, "AaBb × AaBb chatishtirishda 9:7 nisbatdagi komplementarlikda rangli organizmlar ulushi qancha?", "9/16", ["7/16", "3/16", "1/16"], "9 qism rangli."),
    O(3, "Komplementarlik 9:7 nisbat bilan boradi, 160 ta o'simlikdan nechtasi rangli bo'ladi? (son)", ["90"], "160 × 9/16 = 90."),
    O(3, "Polimeriya 15:1 nisbatda 320 ta nasldan nechtasi retsessiv fenotipli? (son)", ["20"], "320/16 = 20."),
]

Q["B10.2"] = [
    C(1, "Odamda erkak jinsining xromosomalari qaysi?", "XY", ["XX", "ZW", "XO"], "Erkak — geterogametali."),
    C(1, "Qushlarda qaysi jins geterogametali?", "Urg'ochi", ["Erkak", "Ikkalasi", "Hech biri"], "Qushlarda urg'ochi ZW."),
    C(1, "Gemofiliya qanday irsiylanadi?", "X-xromosomaga birikkan retsessiv", ["Y-xromosomaga birikkan", "Autosoma dominant", "Sitoplazmatik"], "X^h."),
    M(2, [("Odam erkagi", "XY"), ("Odam ayoli", "XX"), ("Qush urg'ochisi", "ZW")], "Jins xromosomalari."),
    C(2, "Gemofiliyali ota o'g'illariga kasallik genini beradimi?", "Yo'q, o'g'illar otadan Y-xromosoma oladi", ["Ha, hamma o'g'illarga", "Ha, yarmiga", "Faqat qizlariga va o'g'illariga"], "Ota o'g'liga faqat Y beradi."),
    C(2, "Daltonizm qanday irsiylanadi?", "X-xromosomaga birikkan retsessiv", ["Autosoma dominant", "Y-xromosomaga birikkan", "Autosoma retsessiv"], "Daltonizm."),
    C(2, "Kapalaklarda qaysi jins geterogametali?", "Urg'ochi", ["Erkak", "Ikkalasi", "Hech biri"], "Kapalak urg'ochisi."),
    C(2, "Gemofiliyali ota (X^hY) genini qaysi farzandlariga o'tkazadi?", "Faqat qizlariga", ["Faqat o'g'illariga", "Hammasiga", "Hech kimga"], "Qizlar X^h oladi."),
    C(3, "Ona tashuvchi (X^H X^h), ota sog'lom (X^H Y). Farzandlar orasida kasal o'g'il tug'ilish ehtimoli qancha?", "25%", ["50%", "75%", "0%"], "4 xil genotipdan bittasi X^h Y."),
    O(3, "Ota gemofiliyali (X^hY), ona sog'lom homozigota (X^H X^H). Qizlarning necha foizi kasallik genini tashuvchi bo'ladi? (son)", ["100", "100%"], "Hamma qiz X^H X^h."),
    O(3, "Ota gemofiliyali (X^hY), ona sog'lom homozigota. O'g'illarning necha foizi gemofiliyali bo'ladi? (son)", ["0", "0%"], "O'g'illar X^H Y."),
]

Q["B10.3"] = [
    C(1, "Evolyutsiyaning elementar birligi nima?", "Populyatsiya", ["Tur", "Individ", "Jins"], "Populyatsiya."),
    C(1, "Evolyutsiya uchun material bo'lib nimalar xizmat qiladi?", "Mutatsiyalar va kombinativ o'zgaruvchanlik", ["Faqat modifikatsiyalar", "Faqat mashq", "Faqat ona nasl"], "Irsiy o'zgaruvchanlik."),
    C(1, "Barqarorlashtiruvchi tanlanish nazariyasini kim ishlab chiqqan?", "I.I. Shmalgauzen", ["Ch. Darvin", "G. Mendel", "T. Morgan"], "Shmalgauzen."),
    M(2, [("Barqarorlashtiruvchi tanlanish", "Shmalgauzen"), ("Harakatlantiruvchi tanlanish", "Darvin"), ("Dizruptiv tanlanish", "Polimorfizmga olib keladi")], "Tanlanish shakllari."),
    C(2, "Bo'ron paytida faqat o'rtacha qanotli qushlarning omon qolishi qaysi tanlanishga misol?", "Barqarorlashtiruvchi", ["Harakatlantiruvchi", "Dizruptiv", "Sun'iy"], "Chetga chiqishlar yo'qoladi."),
    C(2, "Sanoat melanizmi qaysi tanlanish shakliga misol?", "Harakatlantiruvchi", ["Barqarorlashtiruvchi", "Dizruptiv", "Jinsiy"], "Muhit o'zgarganda."),
    C(2, "Dizruptiv tanlanish nimaga olib keladi?", "Populyatsiya polimorfizmiga", ["Barqarorlikka", "Belgi o'rtachaga yaqinlashishiga", "Yo'q bo'lib ketishga"], "O'rtacha belgi yo'qoladi."),
    C(2, "Nima uchun evolyutsiya birligi tur emas, populyatsiya?", "Tur ichidagi izolyatsiyalangan populyatsiyalar alohida yo'nalishda rivojlanadi", ["Tur o'zgarmaydi", "Turlar bir xil bo'ladi", "Individlar rivojlanadi"], "Izolyatsiya."),
    C(3, "Dizruptiv tanlanishda qaysi belgilar saqlanib qoladi?", "Ekstremal chetki belgilar", ["O'rtacha belgilar", "Hamma belgilar", "Hech qaysi belgi"], "O'rtacha belgi yo'qoladi."),
    O(3, "Kuya kapalaklarining sanoat hududlarida qorayishi hodisasi nomini yozing.", ["sanoat melanizmi"], "Sanoat melanizmi."),
    O(3, "Evolyutsiyaning elementar birligini yozing.", ["populyatsiya"], "Populyatsiya."),
]

Q["B10.4"] = [
    C(1, "Xardi–Vaynberg qonunida allellar chastotasi tenglamasi qaysi?", "p + q = 1", ["p² + q² = 1", "p × q = 1", "p − q = 1"], "Allel chastotalari yig'indisi 1."),
    C(1, "p² qaysi genotip chastotasini bildiradi?", "Dominant gomozigota (AA)", ["Geterozigota (Aa)", "Retsessiv gomozigota (aa)", "Dominant allel (A)"], "p² = AA."),
    C(1, "2pq qaysi genotip chastotasini bildiradi?", "Geterozigota (Aa)", ["Dominant gomozigota (AA)", "Retsessiv gomozigota (aa)", "Retsessiv allel (a)"], "Geterozigota."),
    M(2, [("p²", "AA"), ("2pq", "Aa"), ("q²", "aa")], "Genotip chastotalari."),
    C(2, "aa genotipi chastotasi 0,04 bo'lsa, a allelining chastotasi qancha?", "0,2", ["0,4", "0,02", "0,8"], "q = √0,04 = 0,2."),
    C(2, "p = 0,8 bo'lsa, AA genotipi chastotasi qancha?", "0,64", ["0,16", "0,32", "0,8"], "0,8² = 0,64."),
    C(2, "q = 0,2 bo'lsa, geterozigotalar chastotasi qancha?", "0,32", ["0,16", "0,64", "0,04"], "2 × 0,8 × 0,2 = 0,32."),
    C(2, "q = 0,3 bo'lsa, p qancha?", "0,7", ["0,3", "0,6", "0,9"], "p = 1 − 0,3 = 0,7."),
    C(3, "aa = 0,09 bo'lsa, Aa genotipining chastotasi qancha?", "0,42", ["0,21", "0,49", "0,91"], "q = 0,3, p = 0,7; 2pq = 0,42."),
    O(3, "Populyatsiyada 10000 individ, aa = 1% (0,01). Geterozigotalar soni nechta? (son)", ["1800"], "q = 0,1, p = 0,9; 2pq = 0,18; 1800."),
    O(3, "a allelining chastotasi 0,4 bo'lsa, AA genotipining chastotasi qancha? (o'nlik kasr)", ["0,36", "0.36"], "p = 0,6; p² = 0,36."),
]

# ---------------------------------------------------------------- 11-SINF
Q["B11.1"] = [
    C(1, "Yer yuzida birinchi bo'lib qaysi organizmlar paydo bo'lgan (Arxey)?", "Prokariotlar", ["Evkariotlar", "Qushlar", "Gulli o'simliklar"], "Bakteriya va ko'k-yashil suvo'tlari."),
    C(1, "Fotosintez qaysi erada paydo bo'lgan?", "Arxey", ["Proterozoy", "Paleozoy", "Mezozoy"], "Atmosferada kislorod to'planishi boshlangan."),
    C(1, "Geterotrof evkariotlar qaysi erada paydo bo'lgan?", "Proterozoy", ["Arxey", "Kaynozoy", "Mezozoy"], "Proterozoy."),
    M(2, [("Arxey", "Prokariotlar va fotosintez paydo bo'lishi"), ("Proterozoy", "Evkariotlar va jinsiy jarayon"), ("Kriptozoy", "Arxey va Proterozoy majmui")], "Kriptozoy."),
    C(2, "Jinsiy jarayon qaysi erada paydo bo'lgan?", "Proterozoy", ["Arxey", "Paleozoy", "Mezozoy"], "Proterozoy."),
    C(2, "Barcha umurtqasizlar tiplari dengizda qaysi erada shakllangan?", "Proterozoy", ["Arxey", "Mezozoy", "Kaynozoy"], "Proterozoy."),
    C(2, "Biogen ohaktoshlar qaysi erada hosil bo'la boshlagan?", "Arxey", ["Proterozoy", "Paleozoy", "Mezozoy"], "Arxey."),
    C(2, "Atmosferada erkin kislorod to'planishi qaysi erada boshlangan?", "Arxey", ["Mezozoy", "Kaynozoy", "Paleozoy"], "Fotosintez natijasi."),
    C(3, "Arxeyning tirik organizmlari qaysi javobda to'g'ri?", "Bakteriyalar va ko'k-yashil suvo'tlari", ["Trilobitlar", "Psilofitlar", "Stegosefallar"], "Prokariotlar."),
    O(3, "Arxey va Proterozoyni birlashtiruvchi «yashirin hayot» eoni nomini yozing.", ["kriptozoy"], "Kriptozoy."),
    O(3, "Ko'p hujayralilikka o'tish qaysi erada boshlangan? (era nomi)", ["proterozoy"], "Proterozoy."),
]

Q["B11.2"] = [
    C(1, "Trilobitlar hukmronligi qaysi davrga to'g'ri keladi?", "Kembriy", ["Perm", "Yura", "Bo'r"], "Kembriy portlashi."),
    C(1, "Birinchi umurtqalilar — jag'sizlar qaysi davrda paydo bo'ldi?", "Ordovik", ["Kembriy", "Devon", "Trias"], "Ordovik."),
    C(1, "Quruqlikka chiqqan birinchi o'simliklar qaysi?", "Psilofitlar", ["Gulli o'simliklar", "Ochiq urug'lilar", "Qirqquloqlar"], "Silur davrida."),
    M(2, [("Kembriy", "Trilobitlar hukmronligi"), ("Ordovik", "Jag'sizlar"), ("Silur", "Psilofitlar")], "Erta paleozoy."),
    C(2, "Quruqlikka chiqqan birinchi hayvonlar qaysilar?", "Chayonlar", ["Stegosefallar", "Reptiliyalar", "Qushlar"], "Silur."),
    C(2, "«Kembriy portlashi» nima?", "Tashqi skeletli umurtqasizlar tiplarining paydo bo'lishi", ["Dinozavrlar paydo bo'lishi", "Gulli o'simliklarning paydo bo'lishi", "Odamning paydo bo'lishi"], "Kembriy."),
    C(2, "Jag'li baliqlar qaysi davrda shakllangan?", "Silur", ["Kembriy", "Perm", "Bo'r"], "Silur."),
    C(2, "Ordovik davrida nima jadal rivojlandi?", "Dengiz suvo'tlari", ["Gulli o'simliklar", "Dinozavrlar", "Sutemizuvchilar"], "Dengiz suvo'tlari va mollyuskalar."),
    C(3, "Davrlarning to'g'ri xronologik tartibini toping.", "Kembriy → Ordovik → Silur → Devon", ["Ordovik → Kembriy → Silur → Devon", "Kembriy → Silur → Ordovik → Devon", "Devon → Silur → Ordovik → Kembriy"], "Tartib."),
    O(3, "Quruqlikka chiqqan birinchi o'simliklar guruhi nomini yozing.", ["psilofitlar", "psilofit", "riniofitlar", "riniofit"], "Psilofitlar."),
    O(3, "Birinchi umurtqalilar (jag'sizlar) qaysi davrda paydo bo'lgan? (davr nomi)", ["ordovik"], "Ordovik."),
]

Q["B11.3"] = [
    C(1, "«Baliqlar asri» qaysi davr?", "Devon", ["Silur", "Perm", "Yura"], "Devon."),
    C(1, "Daraxtsimon qirqquloqlar o'rmonlari qaysi davrda?", "Toshko'mir", ["Devon", "Trias", "Bo'r"], "Toshko'mir."),
    C(1, "Perm davrida qaysi o'simliklar tarqaldi?", "Ochiq urug'lilar", ["Gulli o'simliklar", "Psilofitlar", "Yo'sinlar"], "Iqlim quruqlashdi."),
    M(2, [("Devon", "Stegosefallar paydo bo'lgan"), ("Toshko'mir", "Birinchi reptiliyalar"), ("Perm", "Trilobitlar butunlay qirilgan")], "Paleozoy."),
    C(2, "Stegosefallar qaysi sinfga mansub?", "Amfibiyalar", ["Reptiliyalar", "Baliqlar", "Qushlar"], "Devon."),
    C(2, "Birinchi sudralib yuruvchilar qaysi davrda paydo bo'ldi?", "Toshko'mir", ["Devon", "Perm", "Silur"], "Toshko'mir."),
    C(2, "Trilobitlar qaysi davrda butunlay qirilgan?", "Perm", ["Kembriy", "Silur", "Toshko'mir"], "Perm."),
    C(2, "Stegosefallar qaysi hayvonlardan kelib chiqqan?", "Panjabalor baliqlardan", ["Jag'sizlardan", "Reptiliyalardan", "Qushlardan"], "Devon."),
    C(3, "Toshko'mir davriga xos hodisa qaysi javobda berilgan?", "Daraxtsimon sporali o'simliklar o'rmonlari va birinchi reptiliyalar", ["Gulli o'simliklar paydo bo'lishi", "Dinozavrlarning qirilishi", "Odamning paydo bo'lishi"], "Toshko'mir."),
    O(3, "Birinchi sudralib yuruvchilar paydo bo'lgan davrni yozing.", ["toshko'mir", "karbon", "toshkomir"], "Toshko'mir."),
    O(3, "Panjabalor baliqlardan paydo bo'lgan birinchi quruqlik umurtqalilari nomini yozing.", ["stegosefallar", "stegosefal", "stegocefallar"], "Stegosefallar."),
]

Q["B11.4"] = [
    C(1, "Dinozavrlar qaysi davrda paydo bo'lgan?", "Trias", ["Perm", "Yura", "Bo'r"], "Trias."),
    C(1, "Birinchi qush — Arxeopteriks qaysi davrda yashagan?", "Yura", ["Trias", "Bo'r", "Perm"], "Yura."),
    C(1, "Gulli o'simliklar qaysi davrda paydo bo'ldi?", "Bo'r", ["Trias", "Yura", "Perm"], "Bo'r."),
    M(2, [("Trias", "Dinozavrlar paydo bo'lgan"), ("Yura", "Arxeopteriks"), ("Bo'r", "Yopiq urug'lilar paydo bo'lgan")], "Mezozoy davrlari."),
    C(2, "Odam (Homo sapiens) qaysi davrda paydo bo'lgan?", "Antropogen", ["Bo'r", "Perm", "Trias"], "Antropogen."),
    C(2, "Bo'r davri oxirida nima yuz berdi?", "Dinozavrlar va ammonitlar qirildi", ["Gulli o'simliklar paydo bo'ldi", "Birinchi baliqlar paydo bo'ldi", "Trilobitlar hukmron bo'ldi"], "Bo'r oxiri."),
    C(2, "Birinchi sutemizuvchilar qaysi davrda paydo bo'lgan?", "Trias", ["Kembriy", "Devon", "Perm"], "Trias."),
    C(2, "Yo'ldoshli sutemizuvchilar qaysi davrda paydo bo'lgan?", "Bo'r", ["Trias", "Yura", "Perm"], "Bo'r."),
    C(3, "Mezozoy davrlarining to'g'ri xronologik tartibini toping.", "Trias → Yura → Bo'r", ["Yura → Trias → Bo'r", "Bo'r → Yura → Trias", "Trias → Bo'r → Yura"], "Mezozoy."),
    O(3, "Reptiliyalar va qushlar o'rtasidagi o'tish shakli nomini yozing.", ["arxeopteriks"], "Arxeopteriks."),
    O(3, "Gulli o'simliklar va hasharotlarning birgalikda evolyutsiyasi nima deyiladi?", ["koevolyutsiya"], "Koevolyutsiya."),
]

Q["B11.5"] = [
    C(1, "Bitta nukleotidning o'rtacha massasi qancha?", "345 d.m.", ["110 d.m.", "100 d.m.", "34 d.m."], "345."),
    C(1, "Bitta aminokislotaning o'rtacha massasi qancha?", "110 d.m.", ["345 d.m.", "34 d.m.", "220 d.m."], "110."),
    C(1, "DNK zanjirida ikki qo'shni nukleotid orasidagi masofa qancha?", "0,34 nm", ["3,4 nm", "0,034 nm", "34 nm"], "0,34 nm."),
    M(2, [("345 d.m.", "Nukleotid massasi"), ("110 d.m.", "Aminokislota massasi"), ("0,34 nm", "Nukleotidlar orasidagi masofa")], "Molekulyar kattaliklar."),
    C(2, "Bitta aminokislotani nechta nukleotid kodlaydi?", "3 ta (kodon)", ["2 ta", "1 ta", "6 ta"], "i-RNKda kodon."),
    C(2, "Vodorod bog'lari soni qaysi formula bilan topiladi?", "H = 2A + 3G", ["H = 3A + 2G", "H = A + G", "H = 2A + 2G"], "A=T — 2, G≡C — 3."),
    C(2, "Ekologik piramida qoidasiga ko'ra bir trofik darajadan keyingisiga energiyaning qancha qismi o'tadi?", "Taxminan 10%", ["Taxminan 50%", "Taxminan 90%", "Taxminan 1%"], "10% qoidasi."),
    C(2, "100 ta aminokislotali oqsilni kodlovchi qo'sh zanjirli DNKda jami nechta nukleotid bo'ladi?", "600", ["300", "200", "100"], "100 × 6 = 600."),
    C(3, "50 ta aminokislotali oqsilni kodlovchi qo'sh zanjirli DNK qismining massasi taxminan qancha? (345 d.m.)", "103 500 d.m.", ["51 750 d.m.", "17 250 d.m.", "5 500 d.m."], "50 × 6 × 345 = 103 500."),
    O(3, "120 ta aminokislotali oqsil sintezlanadigan gendagi (qo'sh zanjirli DNK) jami nukleotidlar soni nechta? (son)", ["720"], "120 × 6 = 720."),
    O(3, "DNKning bitta zanjirida 500 ta nukleotid bor. Uning uzunligi necha nm? (son)", ["170", "170 nm"], "500 × 0,34 = 170."),
    O(3, "1-trofik daraja biomassasidagi energiya 10000 kJ bo'lsa, 3-daraja (10% qoida) ga necha kJ o'tadi? (son)", ["100", "100 kj"], "10000 → 1000 → 100."),
]
