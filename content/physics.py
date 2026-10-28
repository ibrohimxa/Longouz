"""Fizika (milliy sertifikat va DTM): 6–11-sinf mexanika, issiqlik, elektr, optika, kvant va yadro fizikasi."""
from . import phys_a, phys_b, phys_c, phys_d
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

TOPICS = [
    # --- MEXANIKA (6–7-sinf asoslari) ---
    ("P6.1", 6, "Fizik kattaliklar, SI birliklari va o'lchash", "free"),
    ("P6.2", 6, "Moddaning tuzilishi, diffuziya va zichlik", "free"),
    ("P7.1", 7, "Mexanik harakat: yo'l va ko'chish", "free"),
    ("P7.2", 7, "Tekis harakat va o'rtacha tezlik", "free"),
    ("P7.3", 7, "Kuch va teng ta'sir etuvchi kuch", "free"),
    ("P7.4", 7, "Og'irlik, Guk qonuni va ishqalanish", "free"),
    ("P7.5", 7, "Bosim, Paskal qonuni va gidrostatika", "free"),
    ("P7.6", 7, "Arximed kuchi va jismlarning suzishi", "pro"),
    ("P7.7", 7, "Richag, bloklar, qiya tekislik va FIK", "pro"),
    ("P7.8", 7, "Mexanik ish, quvvat va energiya", "free"),
    # --- KINEMATIKA VA DINAMIKA (9-sinf) ---
    ("P9.1", 9, "Tekis tezlanuvchan harakat", "free"),
    ("P9.2", 9, "Harakat grafiklari (v–t, x–t)", "pro"),
    ("P9.3", 9, "Erkin tushish va vertikal otilish", "free"),
    ("P9.4", 9, "Gorizontal va burchak ostida otilgan jism", "pro"),
    ("P9.5", 9, "Aylana bo'ylab tekis harakat", "pro"),
    ("P9.6", 9, "Nyuton qonunlari", "free"),
    ("P9.7", 9, "Qiya tekislikdagi harakat dinamikasi", "pro"),
    ("P9.8", 9, "Bloklar va bog'langan yuklar tizimi", "ultra"),
    ("P9.9", 9, "Butun olam tortishish va kosmik tezliklar", "pro"),
    ("P9.10", 9, "Vaznsizlik va o'ta og'irlik (lift masalalari)", "ultra"),
    ("P9.11", 9, "Impuls va impulsning saqlanish qonuni", "pro"),
    ("P9.12", 9, "Ish-energiya teoremasi va energiyaning saqlanishi", "pro"),
    ("P9.13", 9, "Zarbalar: elastik va noelastik to'qnashuvlar", "ultra"),
    ("P9.14", 9, "Harakatning nisbiyligi (daryo va kema masalalari)", "ultra"),
    ("P9.15", 9, "Gidrodinamika: uzluksizlik va Bernulli tenglamasi", "ultra"),
    ("P9.16", 9, "Prujinalar tizimi va statika", "ultra"),
    # --- ISSIQLIK VA MOLEKULYAR FIZIKA ---
    ("P8.1", 8, "Temperatura va issiqlik uzatish turlari", "free"),
    ("P8.2", 8, "Issiqlik miqdori va issiqlik balansi", "free"),
    ("P8.3", 8, "Yonish, erish va bug'lanish issiqliklari", "free"),
    ("P8.4", 8, "Issiqlik dvigatellari va FIK", "pro"),
    ("P10.1", 10, "MKT asoslari, mol va Avogadro doimiysi", "free"),
    ("P10.2", 10, "MKT asosiy tenglamasi va temperatura", "pro"),
    ("P10.3", 10, "Ideal gaz holat tenglamasi", "free"),
    ("P10.4", 10, "Izojarayonlar va gaz qonunlari", "free"),
    ("P10.5", 10, "Siklik jarayonlar va grafik transformatsiya", "ultra"),
    ("P10.6", 10, "Gazlar aralashmasi va Dalton qonuni", "ultra"),
    ("P10.7", 10, "To'yingan bug', namlik va qaynash", "pro"),
    ("P10.8", 10, "Sirt taranglik, kapillyarlik va Laplas bosimi", "ultra"),
    ("P10.9", 10, "Qattiq jismlarning mexanik xossalari", "ultra"),
    ("P10.10", 10, "Ichki energiya va termodinamikaning birinchi qonuni", "pro"),
    ("P10.11", 10, "Adiabata, ikkinchi qonun va Karno sikli", "ultra"),
    ("P10.12", 10, "Murakkab issiqlik balansi masalalari", "pro"),
    # --- ELEKTRODINAMIKA ---
    ("P11.1", 10, "Elektr zaryadi va Kulon qonuni", "free"),
    ("P11.2", 10, "Elektr maydon kuchlanganligi", "pro"),
    ("P11.3", 10, "Potensial, kuchlanish va maydon ishi", "pro"),
    ("P11.4", 10, "Kondensatorlar va ularni ulash", "pro"),
    ("P11.5", 8, "Om qonuni va rezistorlarni ulash", "free"),
    ("P11.6", 10, "To'liq zanjir: EYK va ichki qarshilik", "pro"),
    ("P11.7", 10, "Kirxgof qonunlari va Uitston ko'prigi", "ultra"),
    ("P11.8", 8, "Joul–Lens qonuni va elektr quvvati", "free"),
    ("P11.9", 10, "Suyuqlik, gaz va yarimo'tkazgichlarda tok", "pro"),
    ("P11.10", 11, "Magnit maydon: Amper va Lorens kuchlari", "pro"),
    ("P11.11", 11, "Elektromagnit induksiya", "pro"),
    ("P11.12", 11, "O'zinduksiya va magnit maydon energiyasi", "ultra"),
    # --- TEBRANISH, TO'LQIN, OPTIKA ---
    ("P11.13", 11, "Elektromagnit tebranishlar (LC kontur)", "pro"),
    ("P11.14", 11, "O'zgaruvchan tok", "pro"),
    ("P11.15", 11, "RLC zanjir, rezonans va transformator", "ultra"),
    ("P11.16", 9, "Mexanik tebranishlar va to'lqinlar", "free"),
    ("P11.17", 9, "Tovush", "free"),
    ("P11.18", 11, "Elektromagnit to'lqinlar", "pro"),
    ("P11.19", 9, "Geometrik optika: qaytish va sinish", "free"),
    ("P11.20", 9, "Yupqa linzalar", "pro"),
    ("P11.21", 11, "Interferensiya, difraksiya va panjara", "ultra"),
    ("P11.22", 11, "Dispersiya va qutblanish", "pro"),
    ("P11.23", 11, "Maxsus nisbiylik nazariyasi", "ultra"),
    # --- KVANT, ATOM VA YADRO ---
    ("P11.24", 11, "Issiqlik nurlanishi va Plank gipotezasi", "pro"),
    ("P11.25", 11, "Fotoeffekt", "pro"),
    ("P11.26", 11, "Foton, Kompton effekti va de Broyl to'lqinlari", "ultra"),
    ("P11.27", 11, "Atom modellari va Bor postulatlari", "pro"),
    ("P11.28", 11, "Atom yadrosi va bog'lanish energiyasi", "pro"),
    ("P11.29", 11, "Radioaktivlik va yemirilish qonuni", "pro"),
    ("P11.30", 11, "Yadro reaksiyalari, bo'linish va sintez", "ultra"),
    ("P11.31", 11, "Elementar zarralar va kvarklar", "ultra"),
]

_BANKS = {}
for _m in (phys_a, phys_b, phys_c, phys_d):
    _BANKS.update(_m.Q)


def _prepare(items, tier):
    """Bepul mavzularda birinchi ochiq va moslashtirish savoli ham bepul tarifga tushishi uchun (haqiqiy imtihon tarkibi)."""
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
        logging.getLogger(__name__).warning("Fizika bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "physics", "modes": ["certificate", "dtm"], "topics": topics, "questions": questions}
