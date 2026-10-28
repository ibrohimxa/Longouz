"""Ingliz tili (DTM va milliy sertifikat): grammatika, lug'at, o'qish — tarif tizimi bilan."""
from . import en_a, en_b
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

# (kod, sinf, nom, tarif)
TOPICS = [
    ("E1", 5, "Present Simple va Present Continuous", "free"), ("E2", 5, "Past Simple va Past Continuous", "free"),
    ("E3", 6, "Present Perfect va Past Simple", "free"), ("E4", 6, "Future: will / going to / Present Continuous", "free"),
    ("E5", 5, "Artikllar: a / an / the / zero", "free"), ("E6", 5, "Predloglar: vaqt va joy", "free"),
    ("E7", 6, "Comparatives va superlatives", "free"), ("E8", 6, "Modal fe'llar", "free"),
    ("E9", 6, "Sanaladigan/sanalmaydigan otlar va quantifiers", "free"), ("E35", 5, "Olmoshlar va egalik shakllari", "free"),
    ("E36", 5, "Son, sana va vaqt ifodalari", "free"), ("E21", 5, "Lug'at: oila va kundalik hayot", "free"),
    ("E22", 6, "Lug'at: sayohat va transport", "free"), ("E23", 6, "Lug'at: salomatlik va tana", "free"),
    ("E28", 6, "Reading: asosiy fikr va tafsilot (matn)", "free"),
    ("E10", 7, "Savol shakllari va question tags", "pro"), ("E11", 7, "Passive Voice", "pro"),
    ("E12", 8, "Conditionals 0, 1, 2", "pro"), ("E14", 8, "Reported Speech", "pro"),
    ("E15", 8, "Relative clauses", "pro"), ("E16", 8, "Gerund va Infinitive", "pro"),
    ("E17", 9, "Past Perfect va Perfect Continuous", "pro"), ("E18", 9, "Phrasal verbs", "pro"),
    ("E19", 9, "So'z yasalishi: prefiks va suffikslar", "pro"), ("E20", 9, "Bog'lovchi so'zlar (linking words)", "pro"),
    ("E24", 7, "Lug'at: ta'lim va kasblar", "pro"), ("E25", 7, "Lug'at: ekologiya", "pro"),
    ("E26", 8, "Lug'at: texnologiya", "pro"), ("E29", 9, "Reading: xulosa va kontekstdan ma'no (matn)", "pro"),
    ("E30", 9, "Sinonim va antonimlar", "pro"), ("E34", 9, "Ega va kesim moslashuvi", "pro"),
    ("E37", 10, "Gap to'ldirish: zamon tanlash (matn)", "pro"), ("E38", 10, "Imlo va tinish belgilari", "pro"),
    ("E13", 10, "Conditionals 3 va mixed", "ultra"), ("E27", 10, "Idiomalar va kollokatsiyalar", "ultra"),
    ("E31", 11, "Adashtiriladigan so'zlar", "ultra"), ("E32", 11, "Inversiya va ta'kid", "ultra"),
    ("E33", 11, "Wishes va If only", "ultra"), ("E39", 11, "Sabab, natija va maqsad", "ultra"),
    ("E40", 11, "Participle clauses", "ultra"),
]

_BANKS = {}
_BANKS.update(en_a.Q)
_BANKS.update(en_b.Q)


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Ingliz tili bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "english", "modes": ["dtm"], "topics": topics, "questions": questions}
