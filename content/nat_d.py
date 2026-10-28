"""Ona tili va adabiyot: qo'shimcha mavzular."""
from ._dsl import C, O, M

Q = {}

Q["N6.9"] = [
    C(1, "So'z bir qatordan ikkinchi qatorga qanday ko'chiriladi?", "Bo'g'inlarga ajratib", ["Harflarga ajratib", "Ixtiyoriy joydan", "Faqat oxirgi harfdan"], "Ko'chirish bo'g'in chegarasida bajariladi."),
    C(1, "Qatorda bitta harf qoldirib yoki ko'chirib bo'ladimi?", "Yo'q", ["Ha, har doim", "Faqat unlilarni", "Faqat undoshlarni"], "Bitta harf qatorda qoldirilmaydi ham, ko'chirilmaydi ham."),
    C(2, "Quyidagilardan qaysi so'zni qatordan ko'chirish mumkin emas?", "ona", ["maktab", "kitob", "daftar"], "o-na bo'lganda bitta harf qatorda qoladi."),
    C(2, "«Maktab» so'zining to'g'ri ko'chirilishi?", "mak-tab", ["ma-ktab", "makt-ab", "m-aktab"], "Bo'g'in chegarasi: mak-tab."),
    C(2, "«Ma'no» so'zi to'g'ri ko'chirilgan qatorni toping.", "ma'-no", ["ma-'no", "m-a'no", "ma'n-o"], "Tutuq belgisi oldingi bo'g'inda qoladi."),
    C(3, "«O'zbek» so'zi to'g'ri ko'chirilgan qatorni toping.", "o'z-bek", ["o'-zbek", "o'zb-ek", "o-'zbek"], "O' — bitta harf (digraf emas), o'z-bek."),
    O(3, "«Qalam» so'zi nechta bo'g'indan iborat? (son)", ["2", "ikki", "ikkita"], "qa-lam."),
]

Q["N7.8"] = [
    C(1, "«Ovchi» so'zidagi -chi qo'shimchasi nima yasagan?", "Kasb-hunar bildiruvchi ot", ["Sifat", "Fe'l", "Ravish"], "-chi — kasb egasi."),
    C(1, "«Do'stlik» so'zidagi -lik qo'shimchasi nima yasagan?", "Mavhum ot", ["Sifat", "Fe'l", "Son"], "Mavhum tushuncha."),
    C(2, "«Gulzor» so'zidagi -zor qo'shimchasi qanday ma'no beradi?", "Joy-o'rin", ["Kasb", "Kichraytirish", "Mansublik"], "Ko'p narsa o'sadigan joy."),
    C(2, "«Kutubxona» so'zidagi -xona qanday ma'no beradi?", "Joy-o'rin", ["Kasb", "Mavhumlik", "Kichraytirish"], "Kitob saqlanadigan joy."),
    C(2, "«Paxtakor» so'zidagi -kor qo'shimchasi nimani bildiradi?", "Kasb egasini", ["Joyni", "Mavhumlikni", "Kichraytirishni"], "Paxta bilan shug'ullanuvchi."),
    C(3, "«Sinfdosh» so'zida ot yasovchi qo'shimcha qaysi?", "-dosh", ["-sh", "-in", "-d"], "-dosh — hamfikr, hamkor ma'nosi."),
    O(3, "«Kitobxon» so'zidagi ot yasovchi qo'shimchani yozing.", ["-xon", "xon"], "Kitob + xon."),
]

Q["N8.10"] = [
    C(1, "Axborot berish uchun aytilgan gap qanday ataladi?", "Darak gap", ["So'roq gap", "Buyruq gap", "Undov gap"], "Darak gap voqea haqida xabar beradi."),
    C(1, "So'roq gap oxirida qaysi tinish belgisi qo'yiladi?", "So'roq belgisi", ["Nuqta", "Vergul", "Ikki nuqta"], "?"),
    C(2, "Quyidagilardan qaysi biri buyruq-istak gap?", "Darsingni tayyorla.", ["Darsing tayyormi?", "Dars qanchalik qiziq!", "Dars boshlandi."], "Buyruq mazmunli gap."),
    C(2, "His-hayajon bilan aytilgan gap ohangiga ko'ra qanday ataladi?", "Undov (his-hayajonli) gap", ["Darak gap", "So'roq gap", "Buyruq gap"], "Ohangga ko'ra undov gap."),
    C(2, "«Bugun havo juda issiq!» gapi maqsadiga ko'ra qanday?", "Darak gap", ["So'roq gap", "Buyruq gap", "Istak gap"], "Maqsadi xabar berish."),
    C(3, "So'roq gapning belgilari qaysi qatorda to'g'ri berilgan?", "So'roq ohangi, so'roq olmoshlari yoki -mi yuklamasi", ["Faqat nuqta", "Faqat vergul", "Undov so'zlar"], "Shu vositalar so'roq mazmunini beradi."),
    O(3, "So'roq gap oxiriga qaysi tinish belgisi qo'yiladi? (belgining o'zini yozing)", ["?", "so'roq belgisi"], "?"),
]

Q["N9.11"] = [
    C(1, "Darak gap oxiriga qaysi tinish belgisi qo'yiladi?", "Nuqta", ["Vergul", "Tire", "Ikki nuqta"], "Odatda nuqta."),
    C(1, "Uyushiq bo'laklar orasida qanday belgi qo'yiladi?", "Vergul", ["Nuqta", "Tire", "Qavs"], "Sanash ohangida vergul."),
    C(2, "Muallif gapi ko'chirma gapdan oldin kelsa, qaysi belgi qo'yiladi?", "Ikki nuqta", ["Vergul", "Nuqtali vergul", "Qavs"], "Ko'chirma gap qo'shtirnoq ichida."),
    C(2, "Undalmadan keyin qanday belgi qo'yiladi?", "Vergul", ["Tire", "Nuqta", "Ikki nuqta"], "«Do'stlar, ...»."),
    C(2, "Kiritma so'zlar gapda qanday ajratiladi?", "Vergul bilan", ["Tire bilan", "Nuqta bilan", "Ajratilmaydi"], "Aftidan, albatta kabilar."),
    C(3, "Quyidagi gaplardan qaysi birida tinish belgisi to'g'ri qo'yilgan?", "Navoiy: «Ilm — saodat kaliti» degan.", ["Navoiy, «Ilm — saodat kaliti» degan.", "Navoiy «Ilm saodat kaliti», degan.", "Navoiy; «Ilm — saodat kaliti» degan."], "Ikki nuqta ishlatiladi."),
    O(3, "Ko'chirma gap muallif gapidan oldin kelganda gap oxiriga qaysi belgi qo'yiladi? (so'z bilan yozing)", ["ikki nuqta", "ikkita nuqta"], "Ikki nuqta."),
]

Q["N10.13"] = [
    C(1, "«Navoiy» romanining muallifi?", "Oybek", ["Cho'lpon", "Abdulla Qodiriy", "Abdulla Qahhor"], "Oybek (Muso Toshmuhammad o'g'li)."),
    C(1, "Oybekning asl ismi?", "Muso Toshmuhammad o'g'li", ["Abdulla Qodirov", "Julqunboy", "Maqsud Shayxzoda"], "Oybek — taxallus."),
    C(2, "«Qutlug' qon» romanining muallifi?", "Oybek", ["Cho'lpon", "G'afur G'ulom", "Hamza"], "Oybek asari."),
    C(2, "Quyidagilardan qaysi asar Oybekka tegishli?", "«Navoiy»", ["«Kecha va kunduz»", "«O'tkan kunlar»", "«Mehrobdan chayon»"], "«Kecha va kunduz» — Cho'lpon."),
    C(2, "Oybek tug'ilgan yil?", "1905", ["1900", "1910", "1895"], "1905-yil, Toshkent."),
    C(3, "«Navoiy» romani qaysi buyuk shaxsga bag'ishlangan?", "Alisher Navoiy", ["Zahiriddin Bobur", "Amir Temur", "Mirzo Ulug'bek"], "Mutafakkir shoir hayotiga."),
    O(3, "Oybekning tarixiy romani qaysi shoir haqida? (familiyasini yozing)", ["Navoiy", "Alisher Navoiy"], "Alisher Navoiy."),
]
