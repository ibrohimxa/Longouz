"""Rus tili (DTM va milliy sertifikat): fonetika, orfografiya, morfologiya, sintaksis, leksika, adabiyot."""
from . import ru_a
from ._dsl import expand, validate

BLOCK = "mutaxassislik"

TOPICS = [
    ("R1", 5, "Фонетика: звуки и буквы", "free"), ("R2", 5, "Безударные гласные в корне", "free"),
    ("R3", 5, "Правописание согласных", "free"), ("R4", 5, "Разделительные Ь и Ъ", "free"),
    ("R5", 5, "Имя существительное: род, число, падеж", "free"), ("R6", 5, "Склонение существительных", "free"),
    ("R7", 6, "Имя прилагательное", "free"), ("R9", 6, "Местоимение", "free"),
    ("R10", 6, "Глагол: спряжение", "free"), ("R15", 6, "Предлоги, союзы и частицы", "free"),
    ("R19", 7, "Простое предложение: члены предложения", "free"), ("R25", 7, "Лексика: синонимы, антонимы, омонимы", "free"),
    ("R28", 7, "Чтение: главная мысль текста", "free"),
    ("R8", 6, "Имя числительное", "pro"), ("R11", 7, "Глагол: время и вид", "pro"),
    ("R12", 8, "Причастие", "pro"), ("R13", 8, "Деепричастие", "pro"), ("R14", 8, "Наречие", "pro"),
    ("R16", 8, "Частицы НЕ и НИ", "pro"), ("R17", 8, "Правописание Н и НН", "pro"),
    ("R18", 8, "Словосочетание", "pro"), ("R20", 9, "Однородные члены и знаки препинания", "pro"),
    ("R21", 9, "Обращение и вводные слова", "pro"), ("R22", 9, "Сложносочинённое предложение", "pro"),
    ("R23", 9, "Сложноподчинённое предложение", "pro"), ("R24", 9, "Прямая речь и диалог", "pro"),
    ("R26", 9, "Фразеологизмы", "pro"),
    ("R27", 10, "Стили и типы речи", "ultra"), ("R29", 10, "Литература: А. С. Пушкин", "ultra"),
    ("R30", 11, "Литература: Лермонтов и Гоголь", "ultra"),
]

_BANKS = dict(ru_a.Q)


def pack() -> dict:
    topics, questions = [], []
    for code, grade, name, tier in TOPICS:
        topics.append({"code": code, "grade": grade, "name": name, "tier": tier, "block": BLOCK})
        questions.extend(expand(name, grade, _BANKS.get(code, []), BLOCK))
    problems = validate(questions)
    if problems:
        import logging
        logging.getLogger(__name__).warning("Rus tili bankida %s ta muammo: %s", len(problems), problems[:5])
    return {"subject": "russian", "modes": ["dtm", "certificate"], "topics": topics, "questions": questions}
