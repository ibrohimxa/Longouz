"""Ona tili va adabiyot (milliy sertifikat va DTM): 5–11-sinf leksikologiya, fonetika, morfologiya, sintaksis, orfografiya, poetika va asarlar."""
from . import nat_a, nat_b, nat_c, nat_d
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

TOPICS = [
    # --- 5-sinf: leksikologiya ---
    ("N5.1", 5, "So'zning ma'nolari: monosemiya va polisemiya", "free"),
    ("N5.2", 5, "Ma'no ko'chishi: metafora, metonimiya, sinekdoxa", "free"),
    ("N5.3", 5, "Omonimlar, gomofonlar va gomograflar", "free"),
    ("N5.4", 5, "Sinonimlar va antonimlar", "free"),
    ("N5.5", 5, "Paronimlar (talaffuzdosh so'zlar)", "pro"),
    ("N5.6", 5, "Leksika qatlamlari: o'z va o'zlashgan so'zlar", "free"),
    ("N5.7", 5, "Arxaizm, istorizm, neologizm, tabu va evfemizm", "pro"),
    ("N5.8", 5, "Frazeologizmlar va maqollar", "free"),
    ("N5.9", 5, "Xalq og'zaki ijodi janrlari", "free"),
    # --- 6-sinf: fonetika, orfografiya, morfemika ---
    ("N6.1", 6, "Unli tovushlar tasnifi va nutq a'zolari", "free"),
    ("N6.2", 6, "Undosh tovushlar tasnifi", "free"),
    ("N6.3", 6, "Fonetik hodisalar: eliziya, epenteza, assimilyatsiya", "pro"),
    ("N6.4", 6, "Bo'g'in va urg'u", "free"),
    ("N6.5", 6, "Imlo: bosh harf, qo'shib, ajratib va chiziqcha bilan yozish", "free"),
    ("N6.6", 6, "Imlo: tutuq belgisi, h–x, o'–g' harflari", "pro"),
    ("N6.7", 6, "Morfemika va so'z yasalishi", "pro"),
    ("N6.8", 6, "«Alpomish» va «Go'ro'g'li» dostonlari", "free"),
    # --- 7-sinf: ot, sifat, son, olmosh, ravish ---
    ("N7.1", 7, "Ot turkumi", "free"),
    ("N7.2", 7, "Kelishik, egalik va son qo'shimchalari", "free"),
    ("N7.3", 7, "Sifat va sifat darajalari", "free"),
    ("N7.4", 7, "Son turkumi", "pro"),
    ("N7.5", 7, "Olmosh turkumi", "pro"),
    ("N7.6", 7, "Ravish turkumi", "pro"),
    ("N7.7", 7, "«Qutadg'u bilig» va qadimgi adabiy yodgorliklar", "pro"),
    # --- 8-sinf: fe'l, yordamchi so'zlar, sintaksis asoslari ---
    ("N8.1", 8, "Fe'l turkumi va fe'l nisbatlari", "free"),
    ("N8.2", 8, "Fe'lning vazifa shakllari: harakat nomi, sifatdosh, ravishdosh", "pro"),
    ("N8.3", 8, "Fe'l mayllari va zamonlari", "pro"),
    ("N8.4", 8, "Ko'makchi, bog'lovchi va yuklama", "free"),
    ("N8.5", 8, "Modal, undov va taqlid so'zlar", "pro"),
    ("N8.6", 8, "So'z birikmasi va sintaktik aloqa", "free"),
    ("N8.7", 8, "Ega, kesim va ular orasidagi tire", "pro"),
    ("N8.8", 8, "Alisher Navoiy hayoti va ijodi", "free"),
    ("N8.9", 8, "Zahiriddin Muhammad Bobur va «Boburnoma»", "pro"),
    # --- 9-sinf: sintaksis, uslublar, asarlar ---
    ("N9.1", 9, "Ikkinchi darajali bo'laklar", "free"),
    ("N9.2", 9, "Bir tarkibli gaplar", "pro"),
    ("N9.3", 9, "Undalma, kiritma va ajratilgan bo'lakli gaplar", "pro"),
    ("N9.4", 9, "Teng bog'langan qo'shma gaplar", "pro"),
    ("N9.5", 9, "Ergash gapli qo'shma gaplar", "free"),
    ("N9.6", 9, "Bog'lovchisiz qo'shma gaplar va tinish belgilari", "ultra"),
    ("N9.7", 9, "Ko'chirma va o'zlashtirma gap, nutq uslublari", "pro"),
    ("N9.8", 9, "Behbudiy va «Padarkush» dramasi", "pro"),
    ("N9.9", 9, "Abdulla Qodiriy va «O'tkan kunlar»", "free"),
    ("N9.10", 9, "Cho'lpon: lirikasi va «Kecha va kunduz»", "ultra"),
    # --- 10–11-sinf: matn, poetika, yirik asarlar ---
    ("N10.1", 10, "Matn va uning bog'lanish vositalari", "ultra"),
    ("N10.2", 10, "Aruz vazni", "ultra"),
    ("N10.3", 10, "Barmoq vazni, qofiya va radif", "pro"),
    ("N10.4", 10, "Badiiy san'atlar", "pro"),
    ("N10.5", 10, "Abdulla Qahhor: hikoyalar va «Sinchalak»", "pro"),
    ("N10.6", 10, "Maqsud Shayxzoda: «Mirzo Ulug'bek» fojiasi", "ultra"),
    ("N10.7", 10, "Said Ahmad: «Ufq» trilogiyasi", "ultra"),
    ("N10.8", 10, "Odil Yoqubov: «Ulug'bek xazinasi»", "ultra"),
    ("N10.9", 10, "Pirimqul Qodirov: «Yulduzli tunlar»", "pro"),
    ("N10.10", 11, "Erkin Vohidov va Abdulla Oripov ijodi", "ultra"),
    ("N10.11", 11, "Tog'ay Murod ijodi", "ultra"),
    ("N10.12", 10, "Adabiyot nazariyasi: tur, janr va obraz", "free"),
]

_MORE = [
    ("N6.9", 6, "So'z ko'chirish qoidalari", "free"), ("N7.8", 7, "Ot yasovchi qo'shimchalar", "pro"),
    ("N8.10", 8, "Gap turlari: maqsad va ohangga ko'ra", "free"), ("N9.11", 9, "Tinish belgilari qoidalari", "pro"),
    ("N10.13", 10, "Oybek ijodi: «Navoiy» va «Qutlug' qon»", "pro"),
]
TOPICS = sorted(TOPICS + _MORE, key=lambda t: t[1])

_BANKS = {}
for _m in (nat_a, nat_b, nat_c, nat_d):
    _BANKS.update(_m.Q)


def _prepare(items, tier):
    """Bepul mavzularda birinchi ochiq va moslashtirish savoli ham bepul tarifga tushishi uchun."""
    items = list(items)
    if tier != "free":
        return items
    for kind in ("o", "m"):
        for i, it in enumerate(items):
            if it["kind"] == kind:
                it = dict(it)
                it["d"] = 2
                items.pop(i)
                items.insert(0, it)
                break
    return items


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _prepare(_BANKS.get(code, []), tier), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Ona tili bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "native", "modes": ["certificate", "dtm"], "topics": topics, "questions": questions}
