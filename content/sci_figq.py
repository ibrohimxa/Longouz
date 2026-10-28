"""Biologiya va kimyo banklariga chizmali savollar qo'shadi (import qilinganda bir marta)."""
from . import bio_a, bio_b, chem_8, chem_10, figs_sci as S
from ._dsl import C

_done = False


def apply():
    global _done
    if _done:
        return
    _done = True
    bio_a.Q["B6.1"] += [
        C(1, "Hayvon hujayrasi chizmasida 1-raqam bilan belgilangan organoid nima?", "Yadro", ["Mitoxondriya", "Endoplazmatik to'r", "Hujayra membranasi"], "1 — yadro (irsiy axborot saqlanadi).", fig=S.animal_cell()),
        C(1, "Chizmada 2-raqam bilan ko'rsatilgan organoid vazifasi nima?", "Hujayrani energiya (ATF) bilan ta'minlash", ["Oqsil sintezi", "Irsiy axborotni saqlash", "Moddalarni hujayraga kiritmaslik"], "2 — mitoxondriya: «hujayraning energiya stansiyasi».", fig=S.animal_cell()),
        C(2, "Chizmada 4-raqam bilan belgilangan struktura qaysi?", "Hujayra membranasi", ["Yadro", "Mitoxondriya", "Hujayra devori"], "Hayvon hujayrasi tashqi tomondan faqat membrana bilan o'ralgan.", fig=S.animal_cell()),
    ]
    bio_b.Q["B8.1"] += [
        C(1, "Neyron chizmasida 3-raqam bilan belgilangan qism nima?", "Akson", ["Dendrit", "Neyron tanasi", "Sinaptik uch"], "Akson — impulsni hujayra tanasidan uzoqlashtiradi.", fig=S.neuron()),
        C(2, "Chizmada 1-raqam bilan ko'rsatilgan o'simtalar vazifasi?", "Impulsni qabul qilib, tanaga olib keladi", ["Impulsni tanadan uzatadi", "Mielin qobig'ini hosil qiladi", "Faqat oziqlantiradi"], "Dendritlar — qabul qiluvchi qisqa shoxlangan o'simtalar.", fig=S.neuron()),
        C(2, "Chizmada 4-raqam bilan belgilangan joyda nima sodir bo'ladi?", "Impuls keyingi hujayraga uzatiladi (sinaps)", ["Impuls hosil bo'ladi", "Yadro bo'linadi", "Oqsil sintezlanadi"], "Sinaptik uchlarda mediator ajraladi.", fig=S.neuron()),
    ]
    bio_b.Q["B8.4"] += [
        C(1, "Yurak chizmasida 4-raqam bilan belgilangan kamera qaysi?", "Chap qorincha", ["O'ng qorincha", "Chap bo'lmacha", "O'ng bo'lmacha"], "Chap qorincha katta qon aylanish doirasini boshlaydi.", fig=S.heart_diagram()),
        C(2, "Chizmada 2-raqamli kameradan qon qayerga chiqadi?", "O'pka arteriyasiga", ["Aortaga", "O'pka venasiga", "Kovak venaga"], "O'ng qorincha → o'pka arteriyasi (kichik doira).", fig=S.heart_diagram()),
        C(2, "Chizmada 1-raqamli kameraga qaysi tomirlar qon quyadi?", "Yuqori va pastki kovak venalar", ["O'pka venalari", "Aorta", "O'pka arteriyasi"], "O'ng bo'lmachaga venoz qon kovak venalardan keladi.", fig=S.heart_diagram()),
    ]
    bio_b.Q["B9.2"] += [
        C(1, "DNK chizmasida «?» o'rnida qaysi azot asosi bo'lishi kerak (1-zanjirda T)?", "A", ["G", "C", "U"], "T komplementar A ga.", fig=S.dna_ladder()),
        C(2, "Chizmadagi DNK qismida 1-zanjirda nechta A–T va G–C jufti bor (yashirin asos hisobga olingan holda)?", "2 ta A–T va 2 ta G–C", ["3 ta A–T va 1 ta G–C", "1 ta A–T va 3 ta G–C", "4 ta G–C"], "A–T, T–A, G–C, C–G.", fig=S.dna_ladder()),
        C(2, "Chizmadagi G–C jufti orasida nechta vodorod bog'i bor?", "3 ta", ["2 ta", "1 ta", "4 ta"], "G≡C — 3 ta, A=T — 2 ta vodorod bog'i.", fig=S.dna_ladder()),
    ]
    bio_b.Q["B9.4"] += [
        C(2, "Mitoz chizmasida xromosomalar hujayra ekvatorida joylashgan bosqich qaysi?", "B (metafaza)", ["A (profaza)", "C (anafaza)", "D (telofaza)"], "Metafazada xromosomalar ekvator tekisligida.", fig=S.mitosis_phases()),
        C(2, "Chizmada xromatidalar qutblarga tortilayotgan bosqich qaysi?", "C (anafaza)", ["A (profaza)", "B (metafaza)", "D (telofaza)"], "Anafazada xromatidalar ajraladi.", fig=S.mitosis_phases()),
        C(3, "Chizmada hujayra bo'linish to'sig'i hosil bo'lgan va ikki yadro shakllangan bosqich qaysi?", "D (telofaza)", ["A (profaza)", "B (metafaza)", "C (anafaza)"], "Telofazada yadro qayta tiklanadi, sitokinez boshlanadi.", fig=S.mitosis_phases()),
    ]
    bio_b.Q["B10.1"] += [
        C(1, "Pennet katagi Aa × Aa chizmasida AA genotipli nasllar ulushi?", "1/4", ["1/2", "3/4", "1"], "AA : Aa : aa = 1 : 2 : 1.", fig=S.punnett()),
        C(2, "Chizmadagi Aa × Aa chatishtirishda fenotip bo'yicha (to'liq dominantlik) nisbat?", "3 : 1", ["1 : 1", "1 : 2 : 1", "9 : 3 : 3 : 1"], "A_ : aa = 3 : 1.", fig=S.punnett()),
        C(2, "Chizmadagi chatishtirishda geterozigota nasllar foizi?", "50%", ["25%", "75%", "100%"], "Aa — 2/4.", fig=S.punnett()),
    ]
    chem_8.Q["K8.9"] += [
        C(1, "Chizmada atom modelida nechta elektron qavat bor (Na)?", "3 ta", ["2 ta", "1 ta", "4 ta"], "Qavatlar: 2, 8, 1.", fig=S.bohr_atom([2, 8, 1], "Na")),
        C(2, "Chizmadagi Na atomining tashqi qavatida nechta elektron bor?", "1 ta", ["2 ta", "8 ta", "11 ta"], "Elektron konfiguratsiya 2e, 8e, 1e.", fig=S.bohr_atom([2, 8, 1], "Na")),
        C(2, "Chizmadagi atom (Cl) tashqi qavatida nechta elektron bor?", "7 ta", ["8 ta", "17 ta", "1 ta"], "Cl: 2, 8, 7 — VII A guruh.", fig=S.bohr_atom([2, 8, 7], "Cl")),
        C(2, "Chizmadagi atom (Cl) qanday ion hosil qilishga moyil?", "Cl⁻ (1 ta elektron biriktiradi)", ["Cl⁺", "Cl²⁻", "Cl⁷⁺"], "Oktet uchun 1 e⁻ yetishmaydi.", fig=S.bohr_atom([2, 8, 7], "Cl")),
    ]
    chem_10.Q["K10.1"] += [
        C(1, "Chizmada tasvirlangan zanjir oxirida qaysi funksional guruh bor?", "Gidroksil –OH", ["Karboksil –COOH", "Aldegid –CHO", "Amino –NH₂"], "–OH guruhi spirtlarga xos.", fig=S.alcohol(2)),
        C(2, "Chizmadagi modda (ikki uglerodli zanjir + OH) qaysi sinfga kiradi?", "Spirtlar (etanol)", ["Kislotalar", "Efirlar", "Alkenlar"], "C₂H₅OH — etanol.", fig=S.alcohol(2)),
    ]
