"""Kimyo (DTM/BMBA va sertifikat): 8–11-sinf bo'yicha mavzular va tayyor savollar."""
from . import chem_8, chem_9, chem_10, chem_11, chem_x
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

# (kod, sinf, nom, tarif)
TOPICS = [
    ("K8.1", 8, "Mol, molyar massa va molyar hajm", "free"),
    ("K8.2", 8, "Kimyoviy formulalar, valentlik va massa ulush", "free"),
    ("K8.3", 8, "Massaning saqlanish qonuni va reaksiya turlari", "free"),
    ("K8.4", 8, "Kislorod, havo va yonish", "free"),
    ("K8.5", 8, "Vodorod va suv", "pro"),
    ("K8.6", 8, "Oksidlar, asoslar, kislotalar va tuzlar", "pro"),
    ("K8.7", 8, "Eritmalar: eruvchanlik va massa ulush", "free"),
    ("K8.8", 8, "Molyar konsentratsiya, mol qism va kristallogidratlar", "ultra"),
    ("K8.9", 8, "Atom tuzilishi va davriy qonun", "pro"),
    ("K8.10", 8, "Kimyoviy bog'lanish turlari", "pro"),
    ("K9.1", 9, "Elektrolitik dissotsiatsiya nazariyasi", "free"),
    ("K9.2", 9, "Ion almashinish reaksiyalari", "free"),
    ("K9.3", 9, "Suvning ion ko'paytmasi va pH", "free"),
    ("K9.4", 9, "Tuzlar gidrolizi", "pro"),
    ("K9.5", 9, "Galogenlar va xlor", "free"),
    ("K9.6", 9, "Xalkogenlar: ozon, oltingugurt va vodorod sulfid", "pro"),
    ("K9.7", 9, "Sulfat kislota va kontakt usuli", "pro"),
    ("K9.8", 9, "Azot va ammiak", "free"),
    ("K9.9", 9, "Nitrat kislota va zar suvi", "pro"),
    ("K9.10", 9, "Fosfor va fosforli o'g'itlar", "ultra"),
    ("K9.11", 9, "Uglerod va kremniy birikmalari", "pro"),
    ("K9.12", 9, "Metallarning umumiy xossalari va metallurgiya", "pro"),
    ("K9.13", 9, "Ishqoriy, ishqoriy-yer metallar va suv qattiqligi", "ultra"),
    ("K9.14", 9, "Alyuminiy va uning birikmalari", "ultra"),
    ("K9.15", 9, "Temir, xrom va marganets", "ultra"),
    ("K10.1", 10, "Butlerov nazariyasi va gibridlanish", "free"),
    ("K10.2", 10, "Izomeriya turlari", "free"),
    ("K10.3", 10, "Alkanlar: nomenklatura va radikallar", "free"),
    ("K10.4", 10, "Alkanlarning olinishi (Vyurs, Dyuma, Kolbe)", "pro"),
    ("K10.5", 10, "Alkanlarning kimyoviy xossalari", "pro"),
    ("K10.6", 10, "Alkenlar: olinishi va xossalari", "free"),
    ("K10.7", 10, "Alkadienlar va kauchuklar", "ultra"),
    ("K10.8", 10, "Alkinlar (atsetilen qatori)", "pro"),
    ("K10.9", 10, "Arenlar: benzol va toluol", "ultra"),
    ("K10.10", 10, "Uglevodorodlar bo'yicha hisoblash masalalari", "ultra"),
    ("K11.1", 11, "Spirtlar va fenol", "free"),
    ("K11.2", 11, "Aldegidlar va ketonlar", "pro"),
    ("K11.3", 11, "Karbon kislotalar", "pro"),
    ("K11.4", 11, "Murakkab efirlar, yog'lar va sovun", "ultra"),
    ("K11.5", 11, "Uglevodlar", "free"),
    ("K11.6", 11, "Aminlar va anilin", "ultra"),
    ("K11.7", 11, "Aminokislotalar va oqsillar", "pro"),
    ("K11.8", 11, "Polimerlar", "ultra"),
    ("K11.9", 11, "Reaksiya tezligi va kimyoviy muvozanat", "pro"),
    ("K11.10", 11, "Oksidlanish-qaytarilish va elektroliz", "ultra"),
    ("K11.11", 11, "Genetik bog'lanish va ketma-ket o'zgarishlar", "ultra"),
    ("K11.12", 11, "Aralashma, unum va tozalik bo'yicha masalalar", "pro"),
]

_MORE = [
    ("K8.11", 8, "Davriy jadval tuzilishi: davr va guruhlar", "free"), ("K8.12", 8, "Oksidlanish darajasi", "free"),
    ("K8.13", 8, "Kimyoviy tenglamalarni tenglashtirish", "free"), ("K8.14", 8, "Element nomlari va belgilari", "pro"),
    ("K8.15", 8, "Birikmalar turi va bog'lanishga qarab xossalari", "pro"),
    ("K9.16", 9, "Metallarning faollik qatori", "free"), ("K9.17", 9, "Korroziya va himoya", "pro"),
    ("K9.18", 9, "Kristall panjara turlari", "pro"), ("K9.19", 9, "Mineral o'g'itlar", "pro"),
    ("K9.20", 9, "Atrof-muhit kimyosi: kislotali yomg'ir, issiqxona effekti", "pro"),
    ("K10.11", 10, "Neft va tabiiy gaz", "free"), ("K10.12", 10, "Organik moddalar nomenklaturasi", "pro"),
    ("K10.13", 10, "Yonish reaksiyalari bo'yicha hisoblash", "pro"),
    ("K11.13", 11, "Vitaminlar, gormonlar va dori vositalari", "free"), ("K11.14", 11, "Gaz qonunlari va molyar hajm", "pro"),
    ("K11.15", 11, "Termokimyo: issiqlik effekti", "pro"),
]
TOPICS = sorted(TOPICS + _MORE, key=lambda t: t[1])

_BANKS = {}
for _m in (chem_8, chem_9, chem_10, chem_11, chem_x):
    _BANKS.update(_m.Q)


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Kimyo bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "chemistry", "modes": ["dtm", "certificate"], "topics": topics, "questions": questions}
