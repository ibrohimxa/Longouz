"""v217: tarix (sanalar), ingliz tili (shakllar, lug'at), rus tili va ona tili imlosi uchun qo'shimcha savollar.

Savollar JADVALLARDAN (sana/juftlik/shakl) kod orqali tuziladi: variantlar jadvaldagi boshqa yozuvlardan olinadi,
shuning uchun to'g'ri javob jadvaldagi qiymat bilan bir xil bo'ladi. Faqat darslikdagi ma'lum, bahssiz faktlar kiritilgan.
Mavjud mavzularga qo'shiladi; takror matnlar avtomatik filtrlanadi.
"""
from ._dsl import C, O, expand, _rng

# ---------------------------------------------------------------- TARIX
# (hodisa matni, yil, era)  era: "" — milodiy, "m.a." — miloddan avvalgi
HF = {
    "6.1.1-2": [],
    "6.1.15": [("Avestoning 2700 yilligi YUNESKO ko'magida nishonlangan", 2001, "")],
    "6.1.16-17": [("Kir II massagetlar (malika To'maris) bilan jangda halok bo'ldi", 530, "m.a."),
                  ("Doro I Ahamoniylar taxtiga o'tirdi", 522, "m.a.")],
    "6.1.18": [("Aleksandr Makedonskiy Osiyoga yurishni boshladi", 334, "m.a."),
               ("Gavgamela jangi bo'lib o'tdi", 331, "m.a."),
               ("Aleksandr qo'shinlari Movarounnahrga (So'g'diyonaga) kirdi", 329, "m.a.")],
    "6.1.19-20": [("Spitamen boshchiligidagi qo'zg'olon boshlandi", 329, "m.a.")],
    "6.1.28": [("Chjan Szyan Xitoy elchisi sifatida G'arbga yo'l oldi (Buyuk Ipak yo'li shakllanishining boshlanishi)", 138, "m.a.")],
    "7.1.9-10": [("Qutayba ibn Muslim Buxoroni egalladi", 709, ""), ("Qutayba ibn Muslim Samarqandni egalladi", 712, "")],
    "7.1.13": [("Muqanna qo'zg'oloni boshlandi", 776, "")],
    "7.1.16-17": [("Tohiriylar davlati tuzildi", 821, "")],
    "7.1.18": [("Nasr ibn Ahmad Samarqand hokimi bo'ldi (Somoniylar davlatining boshlanishi)", 875, "")],
    "7.1.19": [("Ismoil Somoniy Amr Safforiyni Balx yaqinida mag'lub etdi", 900, "")],
    "7.1.23": [("Qoraxoniylar Buxoroni egalladi, Somoniylar davlati tugatildi", 999, "")],
    "8.1.1": [("Mahmud G'aznaviy taxtga o'tirdi", 998, "")],
    "8.1.2": [("Dandanaqan jangi bo'ldi", 1040, "")],
    "8.1.6": [("Alouddin Muhammad Xorazmshoh bo'ldi (hukmronligi 1200–1220)", 1200, "")],
    "8.1.7": [("Temuchin «Chingizxon» deb e'lon qilindi (qurultoy)", 1206, "")],
    "8.1.8": [("O'tror fojeasi yuz berdi", 1218, "")],
    "8.1.9": [("Chingizxon qo'shinlari Buxoro va Samarqandni egalladi", 1220, "")],
    "8.1.10": [("Gurganj mudofaasi (mo'g'ullar tomonidan shahar olindi)", 1221, "")],
    "8.1.14-15": [("Mahmud Torobiy qo'zg'oloni bo'ldi", 1238, "")],
    "8.1.17": [("Sarbadorlar harakati va Loy jangi bo'ldi", 1365, "")],
    "8.1.18": [("Amir Temur tug'ildi", 1336, "")],
    "8.1.19": [("Balx qurultoyi o'tkazildi — Amir Temur Movarounnahr hukmdori etib saylandi", 1370, "")],
    "8.1.22-23": [("Anqara jangi bo'lib o'tdi", 1402, ""), ("Amir Temur Hindistonga yurish qildi (Dehli olindi)", 1398, "")],
    "8.1.24": [("Amir Temur O'trorda vafot etdi", 1405, "")],
    "8.1.26": [("Shohruh Mirzo Hirotda hukmronlik qila boshladi (Movarounnahr uning tasarrufiga o'tdi)", 1409, "")],
    "8.1.27": [("Mirzo Ulug'bek tug'ildi", 1394, ""), ("Mirzo Ulug'bek vafot etdi (o'ldirildi)", 1449, ""),
               ("Samarqanddagi Ulug'bek madrasasi qurilishi boshlandi", 1417, "")],
    "8.1.29": [("Alisher Navoiy tug'ildi", 1441, ""), ("Alisher Navoiy vafot etdi", 1501, "")],
    "8.1.30": [("Zahiriddin Muhammad Bobur tug'ildi", 1483, ""), ("Bobur Panipat jangida g'alaba qozondi", 1526, ""),
               ("Bobur Kobulni egalladi", 1504, ""), ("Bobur vafot etdi", 1530, "")],
    "9.1.2-3": [("Shayboniyxon Samarqandni egalladi", 1500, ""), ("Saripul jangi bo'ldi", 1501, ""), ("Marv jangi bo'ldi (Shayboniyxon halok bo'ldi)", 1510, "")],
    "9.1.5": [("Abdullaxon II xon bo'ldi", 1583, "")],
    "9.1.6": [("Ashtarxoniylar sulolasi hokimiyatga keldi", 1601, "")],
    "9.1.9": [("Nodirshoh Buxoro va Xivani egalladi", 1740, "")],
    "9.1.12": [("Buxoro amirligi Rossiyaning himoyasiga (protektoratiga) tushdi", 1868, "")],
    "9.1.14": [("Amir Nasrullo taxtga o'tirdi", 1827, "")],
    "10.1.2-3": [("Chernyayev qo'shinlari Toshkentni egalladi", 1865, "")],
    "10.1.4": [("Zirabuloq jangi bo'ldi", 1868, ""), ("Samarqand rus qo'shinlari tomonidan egallandi", 1868, "")],
    "10.1.5": [("Xiva xonligiga qarshi yurish va Gandimiyon shartnomasi", 1873, "")],
    "10.1.6": [("Qo'qon xonligi tugatildi", 1876, "")],
    "10.1.7": [("Turkiston general-gubernatorligi tuzildi", 1867, "")],
    "10.1.11": [("Kaspiyorti temir yo'li Samarqandga yetib keldi", 1888, "")],
    "10.1.12-13": [("Toshkentda vabo isyoni bo'ldi", 1892, ""), ("Do'kchi eshon (Andijon) qo'zg'oloni bo'ldi", 1898, "")],
    "10.1.15": [("Behbudiyning «Padarkush» dramasi yozildi", 1911, "")],
    "10.1.16": [("«Turon» jamiyati tuzildi", 1913, "")],
    "10.1.20": [("Umumturkiston qo'zg'oloni boshlandi (Xo'jandda)", 1916, "")],
    "10.1.21": [("Fevral inqilobi bo'ldi", 1917, "")],
    "11.1.1": [("Oktyabr to'ntarishi bo'ldi", 1917, "")],
    "11.1.2": [("Qo'qonda Turkiston Muxtoriyati e'lon qilindi", 1917, "")],
    "11.1.3": [("Turkiston Muxtoriyati tugatildi", 1918, "")],
    "11.1.6": [("Xiva xonligi ag'darildi", 1920, ""), ("Buxoro amirligi ag'darildi", 1920, "")],
    "11.1.8": [("Milliy-davlat chegaralanishi o'tkazildi, O'zbekiston SSR tuzildi", 1924, "")],
    "11.1.12": [("«Katta terror» (siyosiy qatag'onlar) avj olgan yillar boshlandi", 1937, "")],
    "11.1.13": [("Cho'lpon, Fitrat va Qodiriy qatl etildi", 1938, "")],
    "11.1.14": [("Ikkinchi jahon urushi SSSR uchun boshlandi (Buyuk Vatan urushi)", 1941, "")],
    "11.1.15": [("Ikkinchi jahon urushi tugadi (G'alaba kuni)", 1945, "")],
    "11.1.18": [("Toshkent zilzilasi yuz berdi", 1966, "")],
    "11.1.20": [("Islom Karimov O'zbekiston Kompartiyasi Markaziy Komiteti birinchi kotibi bo'ldi", 1989, "")],
    "11.1.21-22": [("O'zbek tiliga davlat tili maqomi berildi", 1989, ""), ("O'zbekiston davlat mustaqilligi e'lon qilindi", 1991, "")],
    "11.1.23": [("O'zbekiston Respublikasi Konstitutsiyasi qabul qilindi", 1992, "")],
    "11.1.24": [("Milliy valyuta — so'm to'liq muomalaga kiritildi", 1994, "")],
    "11.1.26": [("O'zbekiston BMTga a'zo bo'ldi", 1992, ""), ("O'zbekiston YUNESKOga a'zo bo'ldi", 1993, "")],
    "11.1.27": [("Shavkat Mirziyoyev Prezident etib saylandi", 2016, "")],
    "11.1.28": [("Harakatlar strategiyasi (2017–2021) qabul qilindi", 2017, ""), ("Taraqqiyot strategiyasi (2022–2026) qabul qilindi", 2022, "")],
    "11.1.29": [("Yangi tahrirdagi Konstitutsiya bo'yicha referendum o'tkazildi", 2023, "")],
    "11.1.31": [("Shanxay hamkorlik tashkiloti (ShHT) tuzildi", 2001, "")],
}

HC = {   # qo'shimcha tayyor savollar: (kod, [C/O ...])
    "6.1.15": [
        C(1, "Zardushtiylikning muqaddas kitobi qanday ataladi?", "Avesto", ["Veda", "Tavrot", "Injil"], "Avesto — zardushtiylikning muqaddas kitobi."),
        C(2, "Zardushtiylikda yaxshilik xudosi kim?", "Axura Mazda", ["Angra Mayniyu", "Mitra", "Anaxita"], "Axura Mazda — yaxshilik va yorug'lik xudosi; Angra Mayniyu — yomonlik boshlig'i."),
        C(2, "Zardushtiylik asoschisi kim hisoblanadi?", "Zardusht (Zaratushtra)", ["Kir II", "Doro I", "Mitra"], "Din asoschisi — payg'ambar Zardusht."),
    ],
    "6.1.4": [
        C(2, "Selungur makoni qaysi davrga oid?", "Ilk paleolit", ["Mezolit", "Neolit", "Bronza davri"], "Farg'onadagi Selungur g'ori — ilk paleolit yodgorligi."),
        C(2, "Selungur g'ori qaysi viloyatda joylashgan?", "Farg'ona", ["Surxondaryo", "Xorazm", "Buxoro"], "Selungur — Farg'ona vodiysida."),
    ],
    "6.1.5": [
        C(1, "Teshiktosh g'orida qaysi davr odami qoldiqlari topilgan?", "O'rta paleolit (neandertal)", ["Neolit", "Bronza davri", "Ilk temir davri"], "Teshiktosh — Surxondaryo (Boysun) dagi o'rta paleolit yodgorligi."),
    ],
    "6.1.7": [
        C(1, "Mezolit davrida qaysi qurol ixtiro qilindi?", "Kamon va o'q", ["Metall bolta", "G'ildirak", "Omoch"], "Mezolit — kamon va o'qning ixtirosi bilan xarakterlanadi."),
    ],
    "6.1.8": [
        C(1, "«Neolit inqilobi» nimani anglatadi?", "O'zlashtiruvchi xo'jalikdan ishlab chiqaruvchi xo'jalikka o'tish", ["Metallning kashf etilishi", "Yozuvning paydo bo'lishi", "Davlatning vujudga kelishi"], "Dehqonchilik va chorvachilikka o'tish neolit inqilobi deyiladi."),
    ],
    "6.1.9": [
        C(2, "Kaltaminor madaniyati qaysi hududda tarqalgan?", "Xorazm", ["Farg'ona", "Surxondaryo", "Toshkent vohasi"], "Kaltaminor — Xorazmdagi neolit madaniyati."),
    ],
    "6.1.11": [
        C(2, "Sopollitepa qaysi viloyatda joylashgan?", "Surxondaryo", ["Xorazm", "Farg'ona", "Navoiy"], "Sopollitepa va Jarqo'ton — Surxondaryodagi bronza davri yodgorliklari."),
        C(2, "Jarqo'ton yodgorligi qaysi davrga oid?", "Bronza davri", ["Paleolit", "Neolit", "O'rta asrlar"], "Jarqo'ton — Surxondaryodagi bronza davri shahar-ibodatxonasi."),
    ],
    "6.1.27": [
        C(2, "Tuproqqal'a qaysi qadimiy davlatning poytaxti bo'lgan?", "Qadimgi Xorazm", ["Kushon", "Qang'", "Davon"], "Tuproqqal'a — Qadimgi Xorazm shohlarining qarorgohi."),
    ],
    "7.1.18": [
        C(1, "Somoniylar davlatining poytaxti qaysi shahar edi?", "Buxoro", ["Samarqand", "Xiva", "Termiz"], "Somoniylar poytaxti — Buxoro."),
    ],
    "8.1.25": [
        C(1, "«Temur tuzuklari» kimning nomi bilan bog'liq?", "Amir Temur", ["Mirzo Ulug'bek", "Shohruh Mirzo", "Zahiriddin Bobur"], "«Temur tuzuklari» — Amir Temur davlat boshqaruvi qoidalari."),
    ],
    "8.1.29": [
        C(1, "Alisher Navoiyning «Xamsa»si nechta dostondan iborat?", "5 ta", ["3 ta", "4 ta", "7 ta"], "«Xamsa» — beshlik, 5 ta doston."),
    ],
    "8.1.30": [
        C(1, "Boburning xotira asari qanday nomlanadi?", "«Boburnoma»", ["«Xamsa»", "«Temurnoma»", "«Zafarnoma»"], "«Boburnoma» — Zahiriddin Muhammad Boburning tarixiy-memuar asari."),
    ],
    "9.1.7": [
        C(2, "Samarqanddagi Registon ansamblida qaysi madrasa Yalangto'sh Bahodir tomonidan qurilgan?", "Sherdor", ["Ulug'bek", "Mir Arab", "Ko'kaldosh"], "Sherdor madrasasi 1619–1636-yillarda qurilgan."),
    ],
    "11.1.24": [
        C(1, "O'zbekiston Respublikasi Davlat bayrog'i qaysi yilda qabul qilingan?", "1991", ["1989", "1992", "1994"], "Davlat bayrog'i 1991-yil 18-noyabrda qabul qilingan."),
        C(1, "O'zbekiston Respublikasi Davlat gerbi qaysi yilda qabul qilingan?", "1992", ["1991", "1994", "1993"], "Davlat gerbi 1992-yil 2-iyulda qabul qilingan."),
    ],
    "11.1.21-22": [
        C(1, "Mustaqillik kuni qachon nishonlanadi?", "1-sentabr", ["31-avgust", "8-dekabr", "21-mart"], "Mustaqillik 1991-yil 31-avgustda e'lon qilingan, 1-sentabr — bayram."),
        C(1, "Konstitutsiya kuni qachon nishonlanadi?", "8-dekabr", ["1-sentabr", "2-iyul", "21-mart"], "Konstitutsiya 1992-yil 8-dekabrda qabul qilingan."),
    ],
}


def _years(year, era, text):
    r = _rng(text)
    offs = [-30, -20, -15, -10, -8, -5, 5, 8, 10, 15, 20, 30]
    if year >= 1900:
        offs = [-10, -8, -6, -5, -4, -3, 3, 4, 5, 6, 8, 10]
    r.shuffle(offs)
    out = []
    for o in offs:
        y = year + o
        if y > 0 and y not in out and not (era == "" and y > 2026):
            out.append(y)
        if len(out) == 3:
            break
    return out


def _ys(y, era):
    return f"{y}-yil" + (" (m.a.)" if era else "")


def history_items(code):
    facts = HF.get(code, [])
    items = []
    for ev, y, era in facts:
        era_txt = " (miloddan avvalgi)" if era else ""
        q = f"{ev} — qaysi yilda{era_txt}?"
        items.append(C(2, q, _ys(y, era), [_ys(w, era) for w in _years(y, era, q)], f"To'g'ri javob: {y}-yil" + (" (m.a.)." if era else ".")))
        acc = [str(y), f"{y}-yil", f"{y} yil"]
        items.append(O(3, f"{ev}. Yilini yozing (faqat raqam{', m.a.' if era else ''}).", acc, f"To'g'ri javob: {y}-yil" + (" (m.a.)." if era else ".")))
    if len(facts) >= 3:
        for i, (ev, y, era) in enumerate(facts):
            others = [f for j, f in enumerate(facts) if j != i and (f[1], f[2]) != (y, era)]
            if len(others) < 3:
                continue
            r = _rng(ev + "rev")
            r.shuffle(others)
            q = f"{y}-yilda{' (miloddan avvalgi)' if era else ''} qaysi voqea yuz bergan?"
            items.append(C(2, q, ev, [o[0] for o in others[:3]], f"{ev} — {y}-yil."))
    items.extend(HC.get(code, []))
    return items


# ---------------------------------------------------------------- INGLIZ TILI
IRR = [("begin", "began", "begun"), ("break", "broke", "broken"), ("bring", "brought", "brought"), ("build", "built", "built"),
       ("buy", "bought", "bought"), ("catch", "caught", "caught"), ("choose", "chose", "chosen"), ("come", "came", "come"),
       ("do", "did", "done"), ("draw", "drew", "drawn"), ("drink", "drank", "drunk"), ("drive", "drove", "driven"),
       ("eat", "ate", "eaten"), ("fall", "fell", "fallen"), ("feel", "felt", "felt"), ("find", "found", "found"),
       ("fly", "flew", "flown"), ("forget", "forgot", "forgotten"), ("get", "got", "got"), ("give", "gave", "given"),
       ("go", "went", "gone"), ("grow", "grew", "grown"), ("have", "had", "had"), ("hear", "heard", "heard"),
       ("hide", "hid", "hidden"), ("keep", "kept", "kept"), ("know", "knew", "known"), ("leave", "left", "left"),
       ("lose", "lost", "lost"), ("make", "made", "made"), ("meet", "met", "met"), ("pay", "paid", "paid"),
       ("ride", "rode", "ridden"), ("ring", "rang", "rung"), ("rise", "rose", "risen"), ("run", "ran", "run"),
       ("say", "said", "said"), ("see", "saw", "seen"), ("sell", "sold", "sold"), ("send", "sent", "sent"),
       ("sing", "sang", "sung"), ("sit", "sat", "sat"), ("sleep", "slept", "slept"), ("speak", "spoke", "spoken"),
       ("spend", "spent", "spent"), ("stand", "stood", "stood"), ("swim", "swam", "swum"), ("take", "took", "taken"),
       ("teach", "taught", "taught"), ("tell", "told", "told"), ("think", "thought", "thought"), ("throw", "threw", "thrown"),
       ("understand", "understood", "understood"), ("wake", "woke", "woken"), ("wear", "wore", "worn"), ("win", "won", "won"),
       ("write", "wrote", "written")]


def _pick_wrong(correct, pool, key):
    r = _rng(key)
    pool = [p for p in dict.fromkeys(pool) if p != correct]
    r.shuffle(pool)
    return pool[:3]


def eng_past():
    out = []
    allv2 = [v[1] for v in IRR]
    for b, v2, v3 in IRR:
        wr = [b + ("d" if b.endswith("e") else "ed")]
        if v3 != v2:
            wr.append(v3)
        wr += _pick_wrong(v2, allv2, "v2" + b)
        wr = [w for w in dict.fromkeys(wr) if w != v2][:3]
        out.append(C(1, f"Choose the Past Simple form of the verb «{b}».", v2, wr, f"{b} – {v2} – {v3}."))
        out.append(O(2, f"Write the Past Simple form of «{b}» (one word).", [v2], f"{b} – {v2} – {v3}."))
        out.append(C(2, f"Yesterday she ___ (" + b + ") it again.", v2, wr, f"Past Simple: {v2}."))
    return out


def eng_participle():
    out = []
    allv3 = [v[2] for v in IRR]
    for b, v2, v3 in IRR:
        wr = [b, b + ("d" if b.endswith("e") else "ed")]
        if v2 != v3:
            wr.append(v2)
        wr += _pick_wrong(v3, allv3, "v3" + b)
        wr = [w for w in dict.fromkeys(wr) if w != v3][:3]
        out.append(C(2, f"Choose the Past Participle (V3) of the verb «{b}».", v3, wr, f"{b} – {v2} – {v3}."))
        out.append(O(2, f"Write the Past Participle (V3) of «{b}» (one word).", [v3], f"{b} – {v2} – {v3}."))
        out.append(C(2, f"I have never ___ (" + b + ") such a thing.", v3, wr, f"Present Perfect: have + V3 = {v3}."))
    return out


def eng_past_perfect():
    out = []
    subs = ["She", "They", "We", "He", "My friends", "The students"]
    allv3 = [v[2] for v in IRR]
    for i, (b, v2, v3) in enumerate(IRR[:48]):
        wr = [b, v2 if v2 != v3 else b + "ing", b + "ing"]
        wr = [w for w in dict.fromkeys(wr) if w != v3]
        wr += _pick_wrong(v3, allv3, "pp" + b)
        wr = [w for w in dict.fromkeys(wr) if w != v3][:3]
        s = subs[i % len(subs)]
        q = f"{s} had already ___ ({b}) when I arrived."
        out.append(C(2, q, v3, wr, f"Past Perfect: had + V3 → had {v3}."))
    return out


VOC = {
    "E21": [("grandfather", "bobo"), ("grandmother", "buvi"), ("breakfast", "nonushta"), ("lunch", "tushlik"), ("dinner", "kechki ovqat"),
            ("neighbour", "qo'shni"), ("wedding", "to'y"), ("birthday", "tug'ilgan kun"), ("kitchen", "oshxona"), ("bedroom", "yotoqxona"),
            ("furniture", "mebel"), ("wallet", "hamyon"), ("key", "kalit"), ("mirror", "ko'zgu"), ("umbrella", "soyabon"), ("soap", "sovun"),
            ("towel", "sochiq"), ("pillow", "yostiq"), ("blanket", "ko'rpa"), ("spoon", "qoshiq"), ("knife", "pichoq"), ("cup", "piyola"),
            ("bread", "non"), ("rice", "guruch"), ("salt", "tuz"), ("sugar", "shakar"), ("milk", "sut"), ("egg", "tuxum"), ("grape", "uzum"),
            ("watermelon", "tarvuz"), ("carrot", "sabzi"), ("onion", "piyoz"), ("potato", "kartoshka"), ("cucumber", "bodring")],
    "E22": [("ticket", "chipta"), ("passport", "pasport"), ("luggage", "yuk (bagaj)"), ("airport", "aeroport"), ("station", "vokzal"),
            ("flight", "parvoz (reys)"), ("passenger", "yo'lovchi"), ("journey", "sayohat (safar)"), ("map", "xarita"), ("hotel", "mehmonxona"),
            ("harbour", "port"), ("border", "chegara"), ("customs", "bojxona"), ("driver", "haydovchi"), ("bridge", "ko'prik"),
            ("tourist", "sayyoh"), ("guide", "yo'lboshchi"), ("delay", "kechikish"), ("arrival", "kelish (yetib kelish)"), ("departure", "jo'nab ketish"),
            ("suitcase", "chamadon"), ("engine", "dvigatel"), ("ship", "kema"), ("bicycle", "velosiped"), ("crossroads", "chorraha"), ("pavement", "yo'lak (trotuar)")],
    "E23": [("headache", "bosh og'rig'i"), ("fever", "isitma"), ("cough", "yo'tal"), ("medicine", "dori"), ("doctor", "shifokor"), ("nurse", "hamshira"),
            ("hospital", "kasalxona"), ("pharmacy", "dorixona"), ("injury", "jarohat"), ("bone", "suyak"), ("heart", "yurak"), ("lung", "o'pka"),
            ("stomach", "oshqozon"), ("liver", "jigar"), ("kidney", "buyrak"), ("throat", "tomoq"), ("shoulder", "yelka"), ("elbow", "tirsak"),
            ("knee", "tizza"), ("ankle", "to'piq"), ("wrist", "bilak"), ("thumb", "bosh barmoq"), ("chin", "iyak"), ("eyebrow", "qosh"),
            ("cheek", "yonoq"), ("tooth", "tish"), ("tongue", "til (a'zo)"), ("blood", "qon"), ("skin", "teri"), ("allergy", "allergiya")],
    "E24": [("teacher", "o'qituvchi"), ("pupil", "maktab o'quvchisi"), ("lesson", "dars"), ("homework", "uy vazifasi"), ("exam", "imtihon"),
            ("scholarship", "stipendiya"), ("lecture", "ma'ruza"), ("subject", "fan"), ("diploma", "diplom"), ("engineer", "muhandis"),
            ("accountant", "buxgalter"), ("architect", "me'mor"), ("farmer", "fermer (dehqon)"), ("pilot", "uchuvchi"), ("dentist", "tish shifokori"),
            ("journalist", "jurnalist"), ("salary", "maosh"), ("career", "kasbiy faoliyat (karyera)"), ("employee", "xodim"), ("employer", "ish beruvchi"),
            ("graduate", "bitiruvchi"), ("dormitory", "yotoqxona (talabalar turar joyi)"), ("timetable", "dars jadvali"), ("qualification", "malaka")],
    "E25": [("pollution", "ifloslanish"), ("environment", "atrof-muhit"), ("climate", "iqlim"), ("drought", "qurg'oqchilik"), ("flood", "toshqin"),
            ("earthquake", "zilzila"), ("recycle", "qayta ishlash"), ("waste", "chiqindi"), ("species", "tur (hayvon/o'simlik turi)"),
            ("endangered", "yo'qolib ketish xavfi ostidagi"), ("forest", "o'rmon"), ("desert", "cho'l"), ("glacier", "muzlik"),
            ("renewable", "qayta tiklanadigan"), ("greenhouse effect", "issiqxona effekti"), ("global warming", "global isish"),
            ("ozone layer", "ozon qatlami"), ("wildlife", "yovvoyi tabiat"), ("conservation", "muhofaza qilish"), ("harmful", "zararli")],
    "E26": [("software", "dasturiy ta'minot"), ("keyboard", "klaviatura"), ("screen", "ekran"), ("website", "veb-sayt"), ("password", "parol"),
            ("download", "yuklab olmoq"), ("upload", "yuklamoq"), ("search engine", "qidiruv tizimi"), ("battery", "batareya"), ("charger", "zaryadlovchi"),
            ("device", "qurilma"), ("invention", "ixtiro"), ("inventor", "ixtirochi"), ("artificial intelligence", "sun'iy intellekt"),
            ("network", "tarmoq"), ("update", "yangilamoq"), ("application", "ilova"), ("link", "havola"), ("folder", "papka"), ("laptop", "noutbuk")],
}


def vocab_items(code):
    pairs = VOC.get(code, [])
    out = []
    for i, (en, uz) in enumerate(pairs):
        others = [p for j, p in enumerate(pairs) if j != i]
        r = _rng("v" + en)
        r.shuffle(others)
        wu = [o[1] for o in others[:3]]
        we = [o[0] for o in others[3:6]]
        out.append(C(1, f"«{en}» so'zining o'zbekcha ma'nosi qaysi?", uz, wu, f"{en} — {uz}."))
        out.append(C(1, f"Which English word means «{uz}»?", en, we, f"{uz} — {en}."))
        out.append(O(2, f"«{uz}» ingliz tilida qanday yoziladi? (bitta so'z yoki ibora)", [en], f"{uz} — {en}."))
    return out


ANT = [("hot", "cold"), ("big", "small"), ("early", "late"), ("fast", "slow"), ("strong", "weak"), ("rich", "poor"), ("clean", "dirty"),
       ("heavy", "light"), ("empty", "full"), ("old", "young"), ("hard", "soft"), ("dark", "bright"), ("wide", "narrow"), ("tall", "short"),
       ("thick", "thin"), ("cheap", "expensive"), ("easy", "difficult"), ("polite", "rude"), ("brave", "cowardly"), ("generous", "mean"),
       ("ancient", "modern"), ("success", "failure"), ("arrive", "depart"), ("accept", "refuse"), ("increase", "decrease"), ("victory", "defeat"),
       ("allow", "forbid"), ("remember", "forget"), ("buy", "sell"), ("borrow", "lend")]
SYN = [("big", "large"), ("quick", "fast"), ("begin", "start"), ("end", "finish"), ("buy", "purchase"), ("smart", "clever"), ("glad", "happy"),
       ("tiny", "very small"), ("difficult", "hard"), ("pretty", "beautiful"), ("rich", "wealthy"), ("choose", "select"), ("angry", "furious"),
       ("tired", "exhausted"), ("silent", "quiet"), ("correct", "right"), ("brave", "courageous"), ("look at", "watch"), ("help", "assist"), ("enough", "sufficient")]


def synant_items():
    out = []
    pool = [a for p in ANT for a in p]
    for i, (a, b) in enumerate(ANT):
        wr = _pick_wrong(b, [x for x in pool if x not in (a, b)], "ant" + a)
        out.append(C(1, f"Choose the antonym (opposite) of «{a}».", b, wr, f"{a} ↔ {b}."))
        out.append(O(2, f"Write the antonym of «{a}» (one word).", [b], f"{a} ↔ {b}."))
    spool = [s for p in SYN for s in p]
    for a, b in SYN:
        wr = _pick_wrong(b, [x for x in spool if x not in (a, b)], "syn" + a)
        out.append(C(2, f"Choose the synonym (similar meaning) of «{a}».", b, wr, f"{a} ≈ {b}."))
    return out


COMP = [("big", "bigger", "the biggest"), ("hot", "hotter", "the hottest"), ("happy", "happier", "the happiest"), ("easy", "easier", "the easiest"),
        ("funny", "funnier", "the funniest"), ("busy", "busier", "the busiest"), ("early", "earlier", "the earliest"), ("tall", "taller", "the tallest"),
        ("long", "longer", "the longest"), ("cheap", "cheaper", "the cheapest"), ("thin", "thinner", "the thinnest"), ("large", "larger", "the largest"),
        ("nice", "nicer", "the nicest"), ("good", "better", "the best"), ("bad", "worse", "the worst"), ("much", "more", "the most"),
        ("little", "less", "the least"), ("beautiful", "more beautiful", "the most beautiful"), ("expensive", "more expensive", "the most expensive"),
        ("interesting", "more interesting", "the most interesting"), ("important", "more important", "the most important"),
        ("dangerous", "more dangerous", "the most dangerous"), ("famous", "more famous", "the most famous"), ("difficult", "more difficult", "the most difficult"),
        ("comfortable", "more comfortable", "the most comfortable"), ("healthy", "healthier", "the healthiest"), ("heavy", "heavier", "the heaviest")]


def comp_items():
    out = []
    for a, c, s in COMP:
        wr = []
        if a in ("good", "bad", "much", "little"):
            wr = [a + "er", "more " + a, "most " + a]
        elif " " in c:
            wr = [a + "er", a + "ier", "most " + a]
        else:
            wr = ["more " + a, c[:-2] + "ier" if not c.endswith("ier") else c[:-3] + "er", a + "est"]
        wr = [w for w in dict.fromkeys(wr) if w != c][:3]
        if len(wr) < 3:
            continue
        out.append(C(1, f"Choose the comparative form of «{a}».", c, wr, f"{a} – {c} – {s}."))
        out.append(O(2, f"Write the comparative form of «{a}».", [c], f"{a} – {c} – {s}."))
        ws = ["the " + w for w in ("more " + a, a + "est", "most " + a)]
        ws = [w for w in dict.fromkeys(ws) if w != s]
        if len(ws) >= 3:
            out.append(C(2, f"Choose the superlative form of «{a}».", s, ws[:3], f"{a} – {c} – {s}."))
    return out


ORD = [(1, "first"), (2, "second"), (3, "third"), (4, "fourth"), (5, "fifth"), (8, "eighth"), (9, "ninth"), (12, "twelfth"), (13, "thirteenth"),
       (20, "twentieth"), (21, "twenty-first"), (22, "twenty-second"), (30, "thirtieth"), (40, "fortieth"), (50, "fiftieth"), (100, "hundredth")]
CARD = [(13, "thirteen"), (14, "fourteen"), (15, "fifteen"), (18, "eighteen"), (40, "forty"), (50, "fifty"), (90, "ninety"), (60, "sixty")]


def numbers_items():
    out = []
    ow = [w for _, w in ORD]
    for n, w in ORD:
        wr = _pick_wrong(w, ow, "ord" + w)
        out.append(C(1, f"Choose the ordinal number for {n}: the {n}th.", w, wr, f"{n} → {w}."))
        out.append(O(2, f"Write the ordinal number «{n}th» in words (e.g. 3rd → third).", [w, "the " + w], f"{n} → {w}."))
    cw = [w for _, w in CARD]
    for n, w in CARD:
        wr = _pick_wrong(w, cw, "card" + w)
        out.append(C(1, f"How do we write the number {n} in words?", w, wr, f"{n} — {w}."))
    return out


PREP = [("We have English classes ___ Monday.", "on", ["in", "at", "by"]), ("My birthday is ___ July.", "in", ["on", "at", "by"]),
        ("The film starts ___ 7 o'clock.", "at", ["in", "on", "by"]), ("I was born ___ 2004.", "in", ["on", "at", "by"]),
        ("She usually gets up early ___ the morning.", "in", ["on", "at", "by"]), ("We sleep ___ night.", "at", ["in", "on", "by"]),
        ("My exam is ___ 5 May.", "on", ["in", "at", "by"]), ("It often snows ___ winter.", "in", ["on", "at", "by"]),
        ("We usually visit our grandparents ___ Navruz.", "at", ["in", "on", "by"]), ("They arrive ___ Friday evening.", "on", ["in", "at", "by"]),
        ("Please finish the project ___ Friday (not later than Friday).", "by", ["at", "in", "on"]), ("The book is ___ the table.", "on", ["in", "at", "by"]),
        ("There is a picture ___ the wall.", "on", ["in", "at", "by"]), ("My mother is ___ the kitchen.", "in", ["on", "at", "by"]),
        ("We are waiting ___ the bus stop.", "at", ["in", "on", "by"]), ("The children are ___ school now.", "at", ["in", "on", "by"]),
        ("He lives ___ Samarkand.", "in", ["on", "at", "by"]), ("There is a bird ___ the tree (sitting on a branch inside the leaves).", "in", ["on", "at", "by"]),
        ("I saw him ___ the door.", "at", ["in", "on", "by"]), ("She lives ___ the second floor.", "on", ["in", "at", "by"]),
        ("The cat is hiding ___ the box.", "in", ["on", "at", "by"]), ("We travelled ___ train.", "by", ["in", "on", "at"]),
        ("Our flat is ___ the third floor.", "on", ["in", "at", "by"]), ("I'll meet you ___ the station.", "at", ["in", "on", "by"]),
        ("The picture of the Registan is ___ page 12.", "on", ["in", "at", "by"]), ("In summer we go swimming ___ the river (at the water's edge)... choose the best: He sat ___ the river.", "by", ["in", "on", "at"])]
PREP = PREP[:-1]


def prep_items():
    out = []
    for q, a, w in PREP:
        out.append(C(1, q + " (at / in / on / by)", a, w, f"To'g'ri: {a}."))
    return out


CONF = [("The weather ___ my mood strongly.", "affects", ["effects", "affect", "effect"]), ("The new law had a great ___ on people's lives.", "effect", ["affect", "affects", "affected"]),
        ("Can you give me some ___ about my future career?", "advice", ["advise", "advices", "advised"]), ("I ___ you to study every day.", "advise", ["advice", "advices", "advicing"]),
        ("Be careful not to ___ your keys.", "lose", ["loose", "lost", "loss"]), ("This shirt is too ___ for me.", "loose", ["lose", "lost", "losing"]),
        ("He is taller ___ his brother.", "than", ["then", "that", "thus"]), ("First we had lunch, ___ we went for a walk.", "then", ["than", "that", "there"]),
        ("Everyone ___ Ali came to the party.", "except", ["accept", "expect", "excepts"]), ("Please ___ my apology.", "accept", ["except", "expect", "excepting"]),
        ("Please be ___ in the library.", "quiet", ["quite", "quit", "quiet's"]), ("The film was ___ interesting.", "quite", ["quiet", "quit", "quote"]),
        ("___ book is this? — It's mine.", "Whose", ["Who's", "Who", "Whos"]), ("___ the girl in the red dress? — She is my cousin.", "Who's", ["Whose", "Who", "Whos"]),
        ("The dog wagged ___ tail.", "its", ["it's", "its'", "it"]), ("___ raining outside. Take an umbrella.", "It's", ["Its", "It", "Its'"]),
        ("Can I ___ your pen, please?", "borrow", ["lend", "lent", "loan out"]), ("Could you ___ me your pen, please?", "lend", ["borrow", "borrowed", "lent out"]),
        ("She ___ me that she was ill.", "told", ["said", "spoke", "talked"]), ("He ___ that he was tired.", "said", ["told", "spoke", "talked"]),
        ("I need to ___ my homework before dinner.", "do", ["make", "get", "have made"]), ("She wants to ___ a cake for the party.", "make", ["do", "does", "doing"]),
        ("I can't ___ you — please speak louder.", "hear", ["listen", "listen to", "hearing to"]), ("___ carefully to the teacher.", "Listen", ["Hear", "Hearing", "Heard"]),
        ("The sun ___ in the east.", "rises", ["raises", "rise", "arises"]), ("They ___ the flag every morning.", "raise", ["rise", "rises", "arise"])]


def conf_items():
    return [C(2, q, a, w, f"To'g'ri javob: {a}.") for q, a, w in CONF]


def english_items(code):
    return {"E2": eng_past, "E3": eng_participle, "E17": eng_past_perfect, "E30": synant_items, "E7": comp_items,
            "E36": numbers_items, "E6": prep_items, "E31": conf_items}.get(code, lambda: [])() if code not in VOC else vocab_items(code)


# ---------------------------------------------------------------- RUS TILI
R_UNSTR = [("в_да", "о", "вода"), ("з_ма", "и", "зима"), ("к_рова", "о", "корова"), ("м_локо", "о", "молоко"), ("с_рока", "о", "сорока"),
           ("б_рёза", "е", "берёза"), ("г_рода", "о", "города"), ("с_бака", "о", "собака"), ("п_сать", "и", "писать"), ("л_сной", "е", "лесной"),
           ("з_лёный", "е", "зелёный"), ("х_рошо", "о", "хорошо"), ("тр_ва", "а", "трава"), ("гр_ниц", "а", "границ"),
           ("с_стра", "е", "сестра"), ("ст_на", "е", "стена"), ("д_рога", "о", "дорога"), ("с_лома", "о", "солома"), ("к_рандаш", "а", "карандаш"),
           ("п_ле", "о", "поле"), ("в_сна", "е", "весна"), ("р_ка", "е", "река"), ("з_мля", "е", "земля"), ("л_сной", "е", "лесной")]


def r_unstressed():
    out = []
    seen = set()
    for w, l, full in R_UNSTR:
        if w in seen:
            continue
        seen.add(w)
        pool = [x for x in "оаеи" if x != l]
        out.append(C(1, f"Вставьте пропущенную безударную гласную: {w}.", l, pool, f"Проверочное слово/правило: {full} (пишется «{l}»)."))
        out.append(O(2, f"Напишите слово «{w}» полностью (с буквой на месте пропуска).", [full], f"{full}"))
    return out


R_SIGN = [("о_ъявление", "ъ", "объявление"), ("по_ъезд", "ъ", "подъезд"), ("с_ёмка", "ъ", "съёмка"), ("с_езд", "ъ", "съезд"), ("в_езд", "ъ", "въезд"),
          ("о_ъём", "ъ", "объём"), ("по_ём", "ъ", "подъём"), ("обе_ьяна", "з", "")]
R_SOFT = [("кон_юшня", "ь", "конюшня"), ("с_емья", "ь", "семья"), ("су_я", "ь", "судья"), ("вор_я", "ь", "")]


def r_signs():
    out = []
    for w, a, full in [("о_ъявление", "ъ", "объявление"), ("по_ъезд", "ъ", "подъезд"), ("с_ёмка", "ъ", "съёмка"), ("с_езд", "ъ", "съезд"),
                       ("в_езд", "ъ", "въезд"), ("о_ъём", "ъ", "объём"), ("по_ём", "ъ", "подъём"), ("о_ъект", "ъ", "объект"), ("ад_ютант", "ъ", "адъютант")]:
        out.append(C(2, f"Какой разделительный знак пишется в слове «{w}»?", "Ъ", ["Ь", "Оба знака", "Знак не нужен"], f"После приставки на согласный перед е, ё, ю, я пишется Ъ: {full}."))
    for w, full in [("с_емья", "семья"), ("су_я", "судья"), ("ко_ё", "копьё"), ("вер_я", "верья"), ("пь_ёс", "пьес"), ("руч_и", "ручьи"), ("ли_я", "лья")]:
        pass
    for w, full in [("семь_я", "семья"), ("судь_я", "судья"), ("копь_ё", "копьё"), ("ручь_и", "ручьи"), ("друзь_я", "друзья"), ("воробь_и", "воробьи"), ("статьи", "статьи")]:
        if "_" in w:
            out.append(C(1, f"Какой разделительный знак пишется в слове «{w}»?", "Ь", ["Ъ", "Оба знака", "Знак не нужен"], f"Разделительный Ь пишется внутри слова перед я, е, ё, ю, и: {full}."))
    return out


R_CONJ_II = ["строить", "говорить", "любить", "видеть", "слышать", "держать", "смотреть", "терпеть", "гнать", "дышать", "вертеть", "зависеть",
             "ненавидеть", "обидеть", "стоять", "спать", "лечить", "учить", "готовить", "красить"]
R_CONJ_I = ["читать", "писать", "думать", "играть", "работать", "ждать", "рисовать", "петь", "пить", "жить", "шить", "мыть", "дуть",
            "гулять", "знать", "решать", "стирать", "слушать", "рассказывать", "объяснять"]


def r_conj():
    out = []
    for i, v in enumerate(R_CONJ_II):
        r = _rng("c2" + v)
        others = R_CONJ_I[:]
        r.shuffle(others)
        out.append(C(2, "Найдите глагол II спряжения.", v, others[:3], f"«{v}» — II спряжение (-ишь, -ит, -им, -ите, -ат/-ят)."))
    for i, v in enumerate(R_CONJ_I):
        r = _rng("c1" + v)
        others = R_CONJ_II[:]
        r.shuffle(others)
        out.append(C(2, "Найдите глагол I спряжения.", v, others[:3], f"«{v}» — I спряжение (-ешь, -ет, -ем, -ете, -ут/-ют)."))
    return out


def russian_items(code):
    return {"R2": r_unstressed, "R4": r_signs, "R10": r_conj}.get(code, lambda: [])()


# ---------------------------------------------------------------- ONA TILI (imlo, sinonim-antonim)
TUTUQ = ["ma'no", "a'zo", "she'r", "sa'y", "ta'sir", "mas'ul", "e'lon", "ma'lumot", "mash'al", "jur'at", "qat'iy", "sur'at", "ta'lim", "ma'qul",
         "ma'ruza", "ma'mur", "san'at", "mas'uliyat", "ta'til", "ma'dan", "ta'm", "e'tibor", "e'tiqod", "sa'di", "mu'jiza", "ra'y", "do'st", "to'g'ri",
         "o'g'il", "bo'ldi", "g'oya", "g'alaba", "o'qituvchi", "qo'shiq", "bo'lim", "o'rdak", "ko'prik", "to'y", "yo'l", "ko'ngil", "tog'", "bog'", "sog'lik",
         "ko'z", "o'quvchi", "o'zbek", "mo'jiza"]


def _corrupt(w):
    out = []
    if "'" in w:
        i = w.index("'")
        out.append(w.replace("'", "", 1))
        if i > 1:
            out.append(w[:i - 1] + "'" + w[i - 1] + w[i + 1:])
        out.append(w.replace("'", "-", 1))
        out.append(w.replace("'", "h", 1))
    return [x for x in dict.fromkeys(out) if x != w]


def n_tutuq():
    out = []
    for w in TUTUQ:
        wr = _corrupt(w)
        if len(wr) < 3:
            continue
        out.append(C(1, "Qaysi so'z imlo qoidalariga muvofiq to'g'ri yozilgan?", w, wr[:3], f"To'g'ri yozilishi: {w}."))
        out.append(O(2, f"«{wr[0]}» so'zining to'g'ri imlosini yozing.", [w], f"To'g'ri yozilishi: {w}."))
    return out


N_ANT = [("katta", "kichik"), ("baland", "past"), ("yaxshi", "yomon"), ("issiq", "sovuq"), ("kun", "tun"), ("oq", "qora"), ("yengil", "og'ir"),
         ("qattiq", "yumshoq"), ("keng", "tor"), ("uzoq", "yaqin"), ("to'g'ri", "egri"), ("shirin", "achchiq"), ("boy", "kambag'al"), ("yosh", "qari"),
         ("tez", "sekin"), ("ochiq", "yopiq"), ("quruq", "ho'l"), ("toza", "iflos"), ("kuchli", "zaif"), ("sevinch", "g'am"), ("do'st", "dushman"),
         ("g'alaba", "mag'lubiyat"), ("ko'p", "oz"), ("kirmoq", "chiqmoq"), ("kelmoq", "ketmoq"), ("boshlamoq", "tugatmoq")]
N_SYN = [("go'zal", "chiroyli"), ("jasur", "botir"), ("aqlli", "dono"), ("vatan", "yurt"), ("kuch", "quvvat"), ("g'alaba", "zafar"), ("do'st", "o'rtoq"),
         ("qiyin", "mushkul"), ("sodiq", "vafodor"), ("tinchlik", "osoyishtalik"), ("baxt", "saodat"), ("katta", "ulkan")]


def n_synant():
    out = []
    pool = [x for p in N_ANT for x in p]
    for a, b in N_ANT:
        wr = _pick_wrong(b, [x for x in pool if x not in (a, b)], "na" + a)
        out.append(C(1, f"«{a}» so'ziga antonim (zid ma'noli) so'zni toping.", b, wr, f"{a} — {b} (antonimlar)."))
        out.append(O(2, f"«{a}» so'zining antonimini yozing (bitta so'z).", [b], f"{a} — {b} (antonimlar)."))
    sp = [x for p in N_SYN for x in p]
    for a, b in N_SYN:
        wr = _pick_wrong(b, [x for x in sp if x not in (a, b)], "ns" + a)
        out.append(C(2, f"«{a}» so'ziga sinonim (ma'nodosh) so'zni toping.", b, wr, f"{a} — {b} (sinonimlar)."))
    return out


def native_items(code):
    return {"N6.6": n_tutuq, "N5.4": n_synant}.get(code, lambda: [])()


# ---------------------------------------------------------------- BIRLASHTIRISH
def extend(packs):
    fn = {"history": history_items, "english": english_items, "russian": russian_items, "native": native_items}
    for pack in packs:
        f = fn.get(pack["subject"])
        if not f:
            continue
        by_code = {t["code"]: (t["name"], t["grade"], t.get("block", "")) for t in pack["topics"]}
        have = {q["question"].strip().lower() for q in pack["questions"]}
        codes = list(by_code)
        for code in codes:
            try:
                items = f(code)
            except Exception:  # noqa: BLE001
                continue
            if not items:
                continue
            name, grade, block = by_code[code]
            uniq, seen = [], set()
            for it in items:
                k = it["q"].strip().lower()
                if k in have or k in seen:
                    continue
                seen.add(k)
                uniq.append(it)
            if not uniq:
                continue
            pack["questions"].extend(expand(name, grade, uniq, block))
            have.update(seen)
    return packs
