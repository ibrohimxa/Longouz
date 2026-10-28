"""Savollar banki BO'SH: savollar va mavzular faqat admin panel orqali (Import yoki "Yangi savol") qo'shiladi."""

QUESTION_BANK: dict = {}
TOPIC_REMAP: dict = {}


def get_static_questions(subject: str, mode: str = "dtm", count: int = 0, topic=None, exclude_keys=None) -> list:
    return []


def list_topics(subject: str, mode: str = "dtm") -> list:
    return []
