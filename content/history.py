"""Tarix paketi: 150 ta mavzu (6–11-sinf) va tayyor savollar. Milliy sertifikat va DTM rejimlari uchun bir xil bank."""
from . import h6, h7, h8, h9, h10, h11
from ._dsl import expand, validate
from .history_topics import all_topics

_BANKS = {6: h6.Q, 7: h7.Q, 8: h8.Q, 9: h9.Q, 10: h10.Q, 11: h11.Q}


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, block, tier in all_topics():
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": block})
        items = _BANKS[grade].get(code, [])
        questions.extend(expand(name, grade, items, block))
    problems = validate(questions)
    if problems:
        # Bank sifati muammolari ishga tushirishni to'xtatmaydi, lekin logda ko'rinadi
        import logging
        logging.getLogger(__name__).warning("Tarix bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "history", "modes": ["certificate", "dtm"], "topics": topics, "questions": questions}
