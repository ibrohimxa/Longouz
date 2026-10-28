"""Ona tili va adabiyot: 7–8-sinf — so'z turkumlari, fe'l, yordamchi so'zlar, sintaksis asoslari, adabiyot."""
from ._dsl import C, O, M

Q = {}

Q["N7.1"] = [
    C(1, "Predmetni bildirib, «kim?», «nima?» so'rog'iga javob bo'lgan so'z turkumi?", "Ot", ["Sifat", "Fe'l", "Ravish"], "Ot."),
    C(1, "Qaysi so'z atoqli ot?", "Zarafshon", ["daryo", "tog'", "shahar"], "Atoqli ot — yakka predmet nomi."),
    C(2, "Qaysi qatorda faqat mavhum otlar berilgan?", "baxt, do'stlik, yaxshilik", ["kitob, qalam, daftar", "Toshkent, Samarqand, Buxoro", "uy, devor, eshik"], "Mavhum — sezgi a'zolari bilan idrok etilmaydi."),
    C(2, "«-chi» qo'shimchasi bilan yasalgan shaxs oti qaysi?", "baliqchi", ["baliqlar", "baliqni", "baliqdan"], "Kasb-kor oti."),
    C(2, "Joy oti yasovchi qo'shimchani toping.", "-zor (gulzor)", ["-chi", "-lik faqat", "-dosh"], "Gulzor, paxtazor."),
    C(2, "«-dosh» qo'shimchasi qaysi ot yasaydi?", "Shaxs oti (sinfdosh)", ["Joy oti", "Narsa oti", "Mavhum ot"], "Hamfikr, hamkasb."),
    C(3, "«Do'stlik» so'zi qaysi turdagi ot?", "Mavhum ot", ["Atoqli ot", "Joy oti", "Shaxs oti"], "Sezgi a'zolari bilan idrok etilmaydigan tushuncha."),
    O(3, "«Kuz keldi» gapida «kuz» qaysi so'z turkumi? (bir so'z)", ["ot"], "Ot."),
    M(2, [("shaxs oti", "o'qituvchi"), ("joy oti", "paxtazor"), ("mavhum ot", "yaxshilik")], "Ot turlari."),
]

Q["N7.2"] = [
    C(1, "O'zbek tilida nechta kelishik bor?", "6 ta", ["4 ta", "5 ta", "7 ta"], "Bosh, qaratqich, tushum, jo'nalish, o'rin-payt, chiqish."),
    C(1, "Qaratqich kelishigi qo'shimchasi?", "-ning", ["-ni", "-ga", "-dan"], "Kimning? nimaning?"),
    C(1, "Tushum kelishigi qo'shimchasi?", "-ni", ["-ning", "-ga", "-da"], "Kimni? nimani?"),
    C(2, "Jo'nalish kelishigi so'rog'i?", "Kimga? nimaga? qayerga?", ["Kimdan?", "Kimni?", "Qayerda?"], "-ga, -ka, -qa."),
    C(2, "Chiqish kelishigi qo'shimchasi?", "-dan", ["-da", "-ga", "-ni"], "Qayerdan? kimdan?"),
    C(2, "O'rin-payt kelishigi qo'shimchasi?", "-da", ["-dan", "-ga", "-ning"], "Qayerda? qachon?"),
    C(2, "Egalik qo'shimchasi qaysi so'zda?", "kitobim", ["kitoblar", "kitobga", "kitobchi"], "-im — I shaxs egalik."),
    C(3, "«Kitob o'qidim» gapida «kitob» qaysi kelishikda?", "Tushum (belgisiz)", ["Bosh", "Qaratqich", "Jo'nalish"], "-ni tushib qolgan (belgisiz tushum)."),
    O(3, "«Maktabga bordim» gapida «maktabga» qaysi kelishikda? (kelishik nomini yozing)", ["jo'nalish", "jo'nalish kelishigi"], "-ga — jo'nalish."),
    O(3, "«Do'stimning kitobi» birikmasida «do'stimning» qaysi kelishikda?", ["qaratqich", "qaratqich kelishigi"], "-ning."),
]

Q["N7.3"] = [
    C(1, "Predmet belgisini bildirib «qanday?» so'rog'iga javob bo'ladigan so'z turkumi?", "Sifat", ["Ot", "Fe'l", "Son"], "Sifat."),
    C(1, "Qaysi so'z sifat?", "chiroyli", ["chiroyda", "chiroy", "chiroylar"], "Chiroyli — belgi bildiradi."),
    C(2, "Asliy sifat qaysi qatorda?", "katta, qizil, shirin", ["tilla, temir, yog'och", "kitobiy, ilmiy, adabiy", "oltin, kumush"], "Mustaqil belgi bildiradi."),
    C(2, "Nisbiy sifat qaysi so'z?", "ilmiy", ["katta", "chiroyli", "baland"], "Boshqa predmetga nisbat."),
    C(2, "Qiyosiy daraja qo'shimchasi?", "-roq", ["-gina", "-ish", "-lar"], "Balandroq."),
    C(2, "Ozaytirma daraja qaysi so'zda?", "qizg'ish", ["qizil", "qip-qizil", "juda qizil"], "-ish, -imtir, -mtul."),
    C(3, "Orttirma daraja hosil qiluvchi usul?", "Ayrim bo'lak takrori yoki «eng, juda» so'zlari (qip-qizil, eng chiroyli)", ["-roq qo'shimchasi", "-ish qo'shimchasi", "-lik qo'shimchasi"], "Orttirma."),
    O(3, "«Yaxshi» so'zining oddiy darajasi; «yaxshiroq» qaysi darajada? (qiyosiy yoki orttirma)", ["qiyosiy", "qiyosiy daraja"], "-roq — qiyosiy."),
    O(3, "«Sarg'imtir» so'zi sifatning qaysi darajasi?", ["ozaytirma", "ozaytirma daraja", "kamaytirma"], "-imtir — ozaytirma."),
]

Q["N7.4"] = [
    C(1, "Predmetning miqdorini yoki tartibini bildiruvchi so'z turkumi?", "Son", ["Ot", "Sifat", "Olmosh"], "Son."),
    C(1, "Sanoq sonni toping.", "besh", ["beshinchi", "beshta", "beshov"], "Sanoq son — «besh»."),
    C(2, "«Uchinchi» qaysi son turi?", "Tartib son", ["Sanoq son", "Dona son", "Jamlovchi son"], "-inchi/-nchi."),
    C(2, "«Ikkov» qaysi son turi?", "Jamlovchi son", ["Dona son", "Chamalash son", "Taqsim son"], "-ov, -ala, -ovlon."),
    C(2, "«O'ntacha» qaysi son turi?", "Chamalash son", ["Dona son", "Taqsim son", "Tartib son"], "Taxminiy miqdor."),
    C(2, "«Beshtadan» qaysi son turi?", "Taqsim son", ["Dona son", "Jamlovchi son", "Tartib son"], "-tadan, -ar."),
    C(3, "Raqam bilan yozilgan tartib sonning to'g'ri yozilishi?", "5-sinf", ["5 sinf", "5sinf", "5-chi sinf"], "Raqamdan keyin chiziqcha va -nchi qisqartirilgan holda."),
    O(3, "«Uchta daftar» birikmasida «uchta» qaysi son turi?", ["dona son", "dona"], "-ta."),
    O(3, "«Yarim» so'zi son turkumining qaysi turiga kiradi? (bir tur nomi)", ["kasr", "kasr son"], "Kasr sonlar: yarim, chorak, uchdan bir."),
]

Q["N7.5"] = [
    C(1, "Ot, sifat, son o'rnida kelib, ularga ishora qiluvchi so'z turkumi?", "Olmosh", ["Ravish", "Fe'l", "Yuklama"], "Olmosh."),
    C(1, "Kishilik olmoshi qaysi?", "men", ["bu", "kim", "hech kim"], "Men, sen, u, biz, siz, ular."),
    C(2, "Ko'rsatish olmoshi qaysi?", "bu", ["kim", "o'zim", "hamma"], "Bu, shu, u, o'sha."),
    C(2, "So'roq olmoshi qaysi?", "nima", ["hech kim", "o'z", "men"], "Kim? nima? qayer?"),
    C(2, "Bo'lishsizlik olmoshi qaysi?", "hech kim", ["har kim", "kim", "biz"], "Hech kim, hech narsa."),
    C(2, "Belgilash olmoshi qaysi?", "hamma", ["kim", "bu", "men"], "Hamma, har bir, barcha."),
    C(3, "«O'z» so'zi qaysi olmosh turi?", "O'zlik olmoshi", ["Kishilik olmoshi", "Ko'rsatish olmoshi", "Belgilash olmoshi"], "O'zim, o'zing."),
    O(3, "«Sen» so'zi qaysi olmosh turi? (bir tur nomi)", ["kishilik", "kishilik olmoshi"], "Kishilik olmoshi."),
    O(3, "«Hech narsa» so'zi qaysi olmosh turi?", ["bo'lishsizlik", "bo'lishsizlik olmoshi"], "Bo'lishsizlik olmoshi."),
]

Q["N7.6"] = [
    C(1, "Harakat yoki belgining belgisini bildiruvchi so'z turkumi?", "Ravish", ["Sifat", "Ot", "Son"], "Ravish."),
    C(1, "Qaysi so'z ravish?", "tez", ["tezlik", "tezkor", "tezlashmoq"], "Tez — harakat tarzi (agar fe'lga bog'lansa)."),
    C(2, "Payt ravishi qaysi?", "kecha", ["tez", "ko'p", "yaxshi"], "Qachon?"),
    C(2, "O'rin ravishi qaysi?", "yuqori", ["bugun", "tez", "juda"], "Qayerda?"),
    C(2, "Miqdor-daraja ravishi qaysi?", "juda", ["bugun", "past", "sekin"], "Qancha? qay darajada?"),
    C(2, "Holat ravishi qaysi?", "sekin", ["bugun", "juda", "quyi"], "Qanday?"),
    C(3, "«Yolg'iz yashayman» gapida «yolg'iz» qaysi so'z turkumi?", "Ravish", ["Sifat", "Ot", "Fe'l"], "Qanday yashayman? — holat ravishi."),
    O(3, "«Ertaga keladi» gapida «ertaga» qaysi turkum?", ["ravish"], "Payt ravishi."),
    O(3, "«Juda» so'zi qaysi turdagi ravish? (miqdor-daraja yoki payt)", ["miqdor-daraja", "miqdor-daraja ravishi", "miqdor daraja"], "Miqdor-daraja ravishi."),
]

Q["N7.7"] = [
    C(1, "«Qutadg'u bilig» asari muallifi kim?", "Yusuf Xos Hojib", ["Mahmud Koshg'ariy", "Ahmad Yugnakiy", "Alisher Navoiy"], "Yusuf Xos Hojib, XI asr."),
    C(1, "«Qutadg'u bilig» nima ma'noni anglatadi?", "Saodatga eltuvchi bilim", ["Bilimlar bog'i", "Haqiqatlar tuhfasi", "Qahramonlar tarixi"], "Ma'no."),
    C(2, "«Qutadg'u bilig» da adolatni ifodalovchi obraz?", "Kuntug'di", ["O'gdulmish", "O'zg'urmish", "Oytoldi"], "Kuntug'di — adolat."),
    C(2, "«Qutadg'u bilig» da aqlni ifodalovchi obraz?", "O'gdulmish", ["Kuntug'di", "O'zg'urmish", "Oytoldi"], "O'gdulmish — aql."),
    C(2, "«Hibatul-haqoyiq» muallifi?", "Ahmad Yugnakiy", ["Yusuf Xos Hojib", "Rabg'uziy", "Xorazmiy"], "XII asr."),
    C(2, "«Qisasi Rabg'uziy» qanday asar?", "Payg'ambarlar qissalari to'plami", ["Tarixiy roman", "Lirik devon", "Qahramonlik dostoni"], "XIV asr."),
    C(3, "Xorazmiyning «Muhabbatnoma» asari qaysi mavzuga bag'ishlangan?", "Muhabbat", ["Tarix", "Jang", "Tabiat"], "Ishqiy-didaktik asar."),
    O(3, "«Qutadg'u bilig» muallifining ismini yozing (to'liq: Yusuf Xos Hojib). Familiya emas, ikki so'z: qaysi asrda yashagan? (rim raqami bilan yoki raqam: XI)", ["xi", "11", "xi asr", "11-asr"], "XI asr (1069–70).") if False else O(3, "«Qutadg'u bilig» qaysi asrda yozilgan? (rim raqami bilan)", ["xi", "11", "xi asr", "11-asr"], "1069–1070-yillar, XI asr."),
    M(2, [("Qutadg'u bilig", "Yusuf Xos Hojib"), ("Hibatul-haqoyiq", "Ahmad Yugnakiy"), ("Muhabbatnoma", "Xorazmiy")], "Qadimgi yodgorliklar."),
]

Q["N8.1"] = [
    C(1, "Ish-harakat va holatni bildirib «nima qildi?» so'rog'iga javob bo'lgan so'z turkumi?", "Fe'l", ["Ot", "Sifat", "Ravish"], "Fe'l."),
    C(1, "Qaysi so'z fe'l?", "o'qimoq", ["o'qish", "o'quvchi", "o'qituvchi"], "-moq — fe'l; boshqalar ot."),
    C(2, "Orttirma nisbat qo'shimchasi qaysi so'zda?", "yozdirdi", ["yozildi", "yozishdi", "yozindi"], "-dir."),
    C(2, "Majhul nisbat qaysi so'zda?", "yozildi", ["yozdirdi", "yozishdi", "yozdi"], "-il."),
    C(2, "Birgalik nisbat qaysi so'zda?", "yozishdi", ["yozildi", "yozdirdi", "yozdi"], "-ish."),
    C(2, "O'zlik nisbat qaysi so'zda?", "yuvindi", ["yuvdi", "yuvildi", "yuvdirdi"], "-in/-n."),
    C(3, "Nisbat qo'shimchasi qo'shilmagan (aniq nisbatdagi) fe'lni toping.", "yozdi", ["yozildi", "yozdirdi", "yozishdi"], "Bosh (aniq) nisbat qo'shimchasiz bo'ladi."),
    O(3, "«Ishlatdi» fe'li qaysi nisbatda? (nisbat nomini yozing)", ["orttirma", "orttirma nisbat"], "-t — orttirma nisbat."),
    O(3, "«Kuldirdi» fe'li qaysi nisbatda?", ["orttirma", "orttirma nisbat"], "-dir."),
    M(2, [("-il", "majhul nisbat"), ("-dir", "orttirma nisbat"), ("-ish", "birgalik nisbat")], "Nisbat qo'shimchalari."),
]

Q["N8.2"] = [
    C(1, "Harakat nomi qo'shimchasi?", "-ish, -moq, -uv", ["-gan, -ar", "-b, -gach", "-di"], "Fe'lning otlashgan shakli."),
    C(1, "Sifatdosh qo'shimchasi?", "-gan, -ayotgan, -ar", ["-ish", "-moq", "-ib"], "Aniqlovchi bo'lib keladi."),
    C(1, "Ravishdosh qo'shimchasi?", "-b (-ib), -gach, -guncha", ["-gan", "-ish", "-moq"], "Hol vazifasida."),
    C(2, "«Kelgan odam» birikmasida «kelgan» nima?", "Sifatdosh", ["Harakat nomi", "Ravishdosh", "Sifat"], "Aniqlovchi."),
    C(2, "«O'qib chiqdi» da «o'qib» nima?", "Ravishdosh", ["Sifatdosh", "Harakat nomi", "Ot"], "-ib."),
    C(2, "«Kitob o'qish foydali» da «o'qish» nima?", "Harakat nomi", ["Sifatdosh", "Ravishdosh", "Fe'l kesim"], "-ish."),
    C(3, "Qaysi gapda ravishdosh hol vazifasida kelgan?", "U kulib gapirdi.", ["Kelgan odam ketdi.", "O'qish yaxshi.", "Bu — kitob."], "«Kulib» — hol."),
    O(3, "«Yozayotgan bola» birikmasida «yozayotgan» nima? (bir so'z)", ["sifatdosh"], "-ayotgan."),
    O(3, "«Borguncha» so'zi fe'lning qaysi shakli?", ["ravishdosh"], "-guncha."),
]

Q["N8.3"] = [
    C(1, "Fe'l mayllari soni?", "3 ta (xabar, buyruq-istak, shart)", ["2 ta", "4 ta", "5 ta"], "Ijro/xabar, buyruq-istak, shart."),
    C(1, "Shart mayli qo'shimchasi?", "-sa", ["-gin", "-di", "-moqda"], "Kelsa, bo'lsa."),
    C(2, "Buyruq-istak maylidagi fe'lni toping.", "keling", ["keldi", "kelsa", "kelgan"], "II shaxs hurmat shakli."),
    C(2, "O'tgan zamon qo'shimchasi?", "-di", ["-yapti", "-ajak", "-sa"], "Keldi."),
    C(2, "Hozirgi zamon shakli qaysi?", "kelyapti", ["keldi", "keladi? emas", "kelgan"], "-yapti.") if False else C(2, "Hozirgi zamon davom fe'li qaysi?", "kelyapti", ["keldi", "kelgan", "kelsa"], "-yapti."),
    C(2, "Bo'lishsiz fe'l qo'shimchasi?", "-ma", ["-moq", "-ish", "-gan"], "Bormadi."),
    C(3, "«Bormagan» fe'li qanday shaklda?", "Bo'lishsiz sifatdosh/o'tgan zamon", ["Bo'lishli buyruq", "Shart mayli", "Harakat nomi"], "-ma + -gan."),
    O(3, "«Borsam edi» — qaysi mayl? (xabar, buyruq yoki shart: bir so'z)", ["shart"], "-sa."),
    O(3, "«Keldi» fe'li qaysi zamon shakli?", ["o'tgan", "o'tgan zamon"], "-di."),
]

Q["N8.4"] = [
    C(1, "«Bilan», «uchun», «kabi» qaysi turkumga mansub?", "Ko'makchi", ["Bog'lovchi", "Yuklama", "Undov"], "Ko'makchilar."),
    C(1, "«Va», «hamda» qaysi turkum?", "Bog'lovchi", ["Ko'makchi", "Yuklama", "Ravish"], "Teng bog'lovchi."),
    C(2, "Zidlov bog'lovchisi qaysi?", "lekin", ["va", "yoki", "chunki"], "Lekin, ammo, biroq."),
    C(2, "Ayiruv bog'lovchisi?", "yoki", ["va", "ammo", "chunki"], "Yoki, yo, goh."),
    C(2, "Sabab ergashtiruvchi bog'lovchisi?", "chunki", ["agar", "garchi", "toki"], "Chunki, shuning uchun."),
    C(2, "Shart bog'lovchisi?", "agar", ["chunki", "garchi", "lekin"], "Agar, agarda."),
    C(2, "Yuklama qaysi so'z?", "-mi (kelasanmi)", ["va", "bilan", "uchun"], "So'roq yuklamasi."),
    O(3, "«Kitob uchun keldim» gapida «uchun» qaysi turkum?", ["ko'makchi"], "Maqsad bildiruvchi ko'makchi."),
    O(3, "«Ammo» so'zi qaysi turdagi bog'lovchi? (zidlov, biriktiruv yoki ayiruv)", ["zidlov"], "Ammo — zidlov."),
]

Q["N8.5"] = [
    C(1, "Gumon, ishonch kabi munosabatni bildiruvchi so'zlar?", "Modal so'zlar", ["Undov so'zlar", "Taqlid so'zlar", "Yuklamalar"], "Albatta, balki."),
    C(1, "Hissiyotni bildiruvchi so'zlar?", "Undov so'zlar", ["Modal so'zlar", "Taqlid so'zlar", "Ko'makchilar"], "Oh, voy, ey."),
    C(1, "Tovush va holatga taqlid so'zlar qaysi?", "gurs-gurs, yaltir-yultur", ["albatta, balki", "oh, voy", "bilan, uchun"], "Taqlid."),
    C(2, "Modal so'zni toping.", "balki", ["voy", "shaldir", "yaltir"], "Gumon."),
    C(2, "Undov so'zni toping.", "voy", ["albatta", "shaldir", "balki"], "Hissiy."),
    C(2, "Taqlid so'zni toping.", "shaldir", ["albatta", "voy", "ham"], "Tovushga taqlid."),
    C(3, "«Aftidan» so'zi qaysi turkum?", "Modal so'z", ["Ravish", "Undov", "Yuklama"], "Taxmin."),
    O(3, "«Afsuski» qaysi modal ma'no? (taassuf, gumon yoki ishonch)", ["taassuf"], "Afsuslanish."),
    O(3, "«Hurra!» qaysi turkum? (bir so'z)", ["undov", "undov so'z"], "Undov."),
]

Q["N8.6"] = [
    C(1, "So'z birikmasida boshqa so'zga bog'lanib, uni izohlovchi so'z?", "Tobe so'z", ["Hokim so'z", "Kesim", "Ega"], "Tobe."),
    C(1, "So'z birikmasida boshqa so'zlarni o'ziga bog'lagan asosiy so'z?", "Hokim so'z", ["Tobe so'z", "To'ldiruvchi", "Hol"], "Hokim."),
    C(2, "«Chiroyli gul» birikmasida bog'lanish usuli?", "Bitishuv", ["Moslashuv", "Boshqaruv", "Teng bog'lanish"], "Qo'shimchasiz, tartib bilan."),
    C(2, "«Kitobni o'qimoq» birikmasida bog'lanish usuli?", "Boshqaruv", ["Bitishuv", "Moslashuv", "Teng"], "Kelishik qo'shimchasi talab qiladi."),
    C(2, "«Men o'qiyman» da bog'lanish usuli?", "Moslashuv", ["Boshqaruv", "Bitishuv", "Teng"], "Shaxs-sonda moslashgan."),
    C(2, "Tobe aloqaning turlari?", "Moslashuv, boshqaruv, bitishuv", ["Biriktiruv, zidlov, ayiruv", "Ega, kesim, to'ldiruvchi", "Sabab, natija, shart"], "Tobe bog'lanish."),
    C(3, "«Yaxshi bola» birikmasi...", "so'z birikmasi", ["gap", "ega", "kesim"], "Hokim «bola», tobe «yaxshi»."),
    O(3, "«Bola kitob o'qidi» gapida «kitob» qaysi bo'lak? (gap bo'lagi)", ["to'ldiruvchi", "vositasiz to'ldiruvchi"], "Tushum kelishigidagi (belgisiz)."),
    O(3, "«Quvnoq bolalar» birikmasida hokim so'zni yozing.", ["bolalar"], "Hokim — bolalar."),
]

Q["N8.7"] = [
    C(1, "Gapning asosiy bo'laklari?", "Ega va kesim", ["Aniqlovchi va hol", "To'ldiruvchi va hol", "Ega va to'ldiruvchi"], "Ega, kesim."),
    C(1, "«Kim?», «nima?» so'rog'iga javob bo'lib, gapda ish bajaruvchi bo'lak?", "Ega", ["Kesim", "To'ldiruvchi", "Hol"], "Ega."),
    C(2, "Ega bilan kesim orasiga qachon tire qo'yiladi?", "Ikkalasi ot (yoki sanoq son) bilan ifodalanib, kesim ega haqida ma'lumot bersa", ["Har doim", "Faqat fe'l kesimda", "Hech qachon"], "Toshkent — poytaxt."),
    C(2, "Qaysi gapda tire to'g'ri qo'yilgan?", "Navoiy — buyuk shoir.", ["Navoiy buyuk — shoir.", "Navoiy buyuk shoir —.", "— Navoiy buyuk shoir."], "Ega va ot kesim orasida."),
    C(2, "Kesim qanday so'z turkumlari bilan ifodalanadi?", "Fe'l, ot, sifat va b.", ["Faqat fe'l", "Faqat ot", "Faqat ravish"], "Ot va fe'l kesimlar."),
    C(2, "«Men — talaba» gapida tire?", "Ega va ot kesim orasida qo'yilgan", ["Ortiqcha", "Hol bilan kesim orasida", "To'ldiruvchi o'rnida"], "Tire."),
    C(3, "Qaysi gapda tire qo'yilmaydi?", "Bola keldi.", ["Samarqand — qadimiy shahar.", "Bu — kitob.", "Ona — Vatan."], "Fe'l kesimdan oldin tire qo'yilmaydi."),
    O(3, "«Bahor keldi» gapida ega qaysi so'z?", ["bahor"], "Kim? nima keldi? — bahor."),
    O(3, "«Daryo oqdi» gapida kesim qaysi so'z?", ["oqdi"], "Nima qildi? — oqdi."),
]

Q["N8.8"] = [
    C(1, "Alisher Navoiy qachon tug'ilgan?", "1441-yil", ["1483-yil", "1500-yil", "1389-yil"], "1441, Hirot."),
    C(1, "Navoiyning «Xamsa»si nechta dostondan iborat?", "5 ta", ["4 ta", "3 ta", "6 ta"], "Besh doston."),
    C(1, "Navoiyning lirik asarlar to'plami?", "Xazoyin ul-maoniy", ["Xamsa", "Boburnoma", "Lison ut-tayr"], "Xazoyinul-maoniy (4 devon)."),
    C(2, "«Xazoyin ul-maoniy» ga nechta devon kiradi?", "4 ta", ["3 ta", "5 ta", "2 ta"], "G'aroyib us-sig'ar va b."),
    C(2, "«Farhod va Shirin» dostonida Farhodning raqibi kim?", "Xisrav", ["Qays", "Ibn Salom", "Bahrom"], "Xisrav Parvez."),
    C(2, "«Layli va Majnun» dostonida Majnunning haqiqiy ismi?", "Qays", ["Farhod", "Xisrav", "Ibn Salom"], "Qays."),
    C(2, "Navoiyning forsiy taxallusi?", "Foniy", ["Navoiy", "Bobur", "Muqimiy"], "Foniy."),
    C(3, "«Muhokamat ul-lug'atayn» asari nimaga bag'ishlangan?", "Turkiy va forsiy tillarni qiyoslash", ["Tarixga", "Arab tiliga", "Xalq og'zaki ijodiga"], "1499-yil."),
    O(3, "Navoiyning «Xamsa»si tarkibidagi «Hayrat ul-abror» qanday mavzudagi doston? Savol: Navoiy qaysi shaharda tug'ilgan? (shahar nomi)", ["hirot", "herat"], "Hirot.") if False else O(3, "Alisher Navoiy qaysi shaharda tug'ilgan? (shahar nomi)", ["hirot", "herat"], "Hirot (hozirgi Afg'oniston)."),
    O(3, "«Xamsa» ning birinchi dostoni qaysi? (nomini yozing)", ["hayrat ul-abror", "hayratul-abror", "hayrat ul abror", "hayratul abror"], "Hayrat ul-abror."),
]

Q["N8.9"] = [
    C(1, "«Boburnoma» muallifi?", "Zahiriddin Muhammad Bobur", ["Alisher Navoiy", "Mirzo Ulug'bek", "Amir Temur"], "Bobur."),
    C(1, "Bobur qayerda tug'ilgan?", "Andijon", ["Samarqand", "Hirot", "Kobul"], "1483-yil."),
    C(2, "«Boburnoma» qaysi janrda yozilgan?", "Xotira-memuar asar", ["Doston", "Drama", "Roman"], "Tarixiy-biografik."),
    C(2, "Boburning aruz haqidagi asari?", "Aruz risolasi", ["Mubayyin", "Boburnoma", "Xatti Boburiy"], "Aruz."),
    C(2, "Bobur asos solgan davlat?", "Boburiylar saltanati (Hindistonda)", ["Temuriylar", "Shayboniylar", "Xorazmshohlar"], "Hindistonda."),
    C(3, "Bobur yaratgan yozuv?", "Xatti Boburiy", ["Kufiy", "Nasta'liq", "Bobuxon"], "Bobur alifbosi."),
    C(3, "Boburning fiqh (huquq) bo'yicha she'riy asari?", "Mubayyin", ["Boburnoma", "Aruz risolasi", "Xamsa"], "Mubayyin."),
    O(3, "Bobur qayerda dafn etilgan? (shahar nomi)", ["kobul", "qobul"], "Kobul."),
    O(3, "Bobur hukmronlik qilgan Hindistondagi shahar? (poytaxt — Agra yoki Dehli: Agra deb yozing)", ["agra"], "Agra.") if False else O(3, "Bobur vafot etgan shahar qaysi? (Hindistondagi)", ["agra"], "Agra, 1530."),
]
