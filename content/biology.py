"""Biologiya (DTM/BMBA): 6–11-sinf bo'yicha mavzular va tayyor savollar (5–6-sinf Botanika 6-sinf bo'limida)."""
from . import bio_a, bio_b, bio_c
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

# (kod, sinf, nom, tarif)
TOPICS = [
    ("B6.1", 6, "Hujayra tuzilishi va mikroskopik kashfiyotlar", "free"),
    ("B6.2", 6, "Plastidalar va vakuola", "pro"),
    ("B6.3", 6, "O'simlik to'qimalari (gistologiya)", "free"),
    ("B6.4", 6, "Ildiz tizimi va ildiz zonalari", "pro"),
    ("B6.5", 6, "Poya, kurtak va barg", "ultra"),
    ("B6.6", 6, "Gul va qo'sh urug'lanish", "pro"),
    ("B6.7", 6, "O'simlik oilalari (taksonomiya)", "ultra"),
    ("B7.1", 7, "Bir hujayrali hayvonlar: amyoba va evglena", "free"),
    ("B7.2", 7, "Infuzoriya-tufelka va kon'yugatsiya", "ultra"),
    ("B7.3", 7, "Chuvalchanglar: gijjalar rivojlanish sikllari", "pro"),
    ("B7.4", 7, "Bo'g'imoyoqlilar tipi", "pro"),
    ("B7.5", 7, "Xordalilar: yurak va qon aylanishi", "free"),
    ("B7.6", 7, "Xordalilar: nafas, ayirish va boshqa belgilar", "ultra"),
    ("B8.1", 8, "Neyron, sinaps va refleks yoyi", "pro"),
    ("B8.2", 8, "Bosh miya bo'limlari", "free"),
    ("B8.3", 8, "Qon tarkibi va qon hujayralari", "free"),
    ("B8.4", 8, "Yurak sikli", "pro"),
    ("B8.5", 8, "Endokrin tizim va gormonlar", "ultra"),
    ("B9.1", 9, "Oqsillar va ularning tuzilmalari", "free"),
    ("B9.2", 9, "Nuklein kislotalar va komplementarlik", "free"),
    ("B9.3", 9, "Energiya almashinuvi (glyukoza parchalanishi)", "pro"),
    ("B9.4", 9, "Hujayra bo'linishi va organoidlar", "ultra"),
    ("B10.1", 10, "Allel bo'lmagan genlarning o'zaro ta'siri", "free"),
    ("B10.2", 10, "Jinsga birikkan irsiylanish", "pro"),
    ("B10.3", 10, "Evolyutsiyaning harakatlantiruvchi kuchlari", "ultra"),
    ("B10.4", 10, "Populyatsiya genetikasi (Xardi–Vaynberg)", "ultra"),
    ("B11.1", 11, "Arxey va Proterozoy (kriptozoy)", "free"),
    ("B11.2", 11, "Paleozoy: Kembriy, Ordovik, Silur", "ultra"),
    ("B11.3", 11, "Paleozoy: Devon, Toshko'mir, Perm", "ultra"),
    ("B11.4", 11, "Mezozoy va Kaynozoy", "ultra"),
    ("B11.5", 11, "Molekulyar biologiya masalalari va formulalar", "pro"),
]

_MORE = [
    ("B6.8", 6, "Meva va urug'lar", "free"), ("B6.9", 6, "O'simliklarning vegetativ ko'payishi", "free"),
    ("B6.10", 6, "Suv o'tlari", "free"), ("B6.11", 6, "Moxlar, qirqbo'g'imlar va paporotniklar", "pro"),
    ("B6.12", 6, "Yalang'ochurug'lilar (ignabarglilar)", "pro"), ("B6.13", 6, "Fotosintez (o'simliklarda)", "free"),
    ("B6.14", 6, "O'simliklarda nafas olish va transpiratsiya", "pro"), ("B6.15", 6, "Mineral oziqlanish va ildiz so'rishi", "pro"),
    ("B7.7", 7, "Bo'shliqichlilar: gidra va marjonlar", "free"), ("B7.8", 7, "Mollyuskalar tipi", "pro"),
    ("B7.9", 7, "Halqali chuvalchanglar", "free"), ("B7.10", 7, "Hasharotlar sinfi", "free"),
    ("B7.11", 7, "Baliqlar sinfi", "free"), ("B7.12", 7, "Amfibiyalar va reptiliyalar", "pro"),
    ("B7.13", 7, "Qushlar sinfi", "pro"), ("B7.14", 7, "Sutemizuvchilar sinfi", "free"),
    ("B8.6", 8, "Tayanch-harakat tizimi: suyaklar va bo'g'imlar", "free"), ("B8.7", 8, "Hazm tizimi va fermentlar", "free"),
    ("B8.8", 8, "Nafas tizimi va gaz almashinuvi", "free"), ("B8.9", 8, "Ayirish tizimi (buyrak, nefron)", "pro"),
    ("B8.10", 8, "Teri va termoregulyatsiya", "pro"), ("B8.11", 8, "Sezgi organlari: ko'rish va eshitish", "pro"),
    ("B8.12", 8, "Immunitet va emlash", "ultra"),
    ("B9.5", 9, "Fotosintez fazalari (yorug'lik va qorong'ilik)", "pro"), ("B9.6", 9, "Biosintez: transkripsiya va translyatsiya", "free"),
    ("B9.7", 9, "Vitaminlar", "free"), ("B9.8", 9, "Fermentlar va ularning xususiyatlari", "pro"),
    ("B9.9", 9, "Mitoz va meyoz bosqichlari", "ultra"),
    ("B10.5", 10, "Mendel qonunlari va chatishtirish masalalari", "free"), ("B10.6", 10, "Mutatsiya va modifikatsiya", "pro"),
    ("B10.7", 10, "Seleksiya asoslari", "pro"), ("B10.8", 10, "Ekotizim va ozuqa zanjirlari", "free"),
    ("B10.9", 10, "Biosfera va Vernadskiy ta'limoti", "ultra"),
]
TOPICS = sorted(TOPICS + _MORE, key=lambda t: t[1])

_BANKS = {}
_BANKS.update(bio_a.Q)
_BANKS.update(bio_b.Q)
_BANKS.update(bio_c.Q)


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Biologiya bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "biology", "modes": ["dtm"], "topics": topics, "questions": questions}
