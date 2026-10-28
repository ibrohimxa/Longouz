"""AI provayder xatolarini yodda saqlab, foydalanuvchiga tushunarli sabab ko'rsatadi."""

import logging
import time

logger = logging.getLogger(__name__)

_RECENT_SECONDS = 15 * 60
_PROVIDER_LABELS = {"claude": "Claude (Anthropic)", "gemini": "Gemini (Google)"}
_last_errors: dict[str, tuple[float, str, str]] = {}

_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("credit", ("credit balance", "billing", "insufficient")),
    ("auth", ("401", "403", "invalid x-api-key", "api key not valid", "permission_denied", "unauthenticated", "authentication")),
    ("quota", ("429", "quota", "rate limit", "resource_exhausted", "overloaded")),
    ("model", ("404", "not_found", "model")),
    ("network", ("connection", "timeout", "timed out", "tunnel", "ssl", "dns", "unreachable")),
)

_MESSAGES = {
    "credit": "{p} hisobida mablag' (kredit) tugagan. Hisobni to'ldiring yoki boshqa kalit qo'ying.",
    "auth": "{p} API kaliti noto'g'ri yoki ruxsati yo'q. .env faylidagi kalitni tekshiring.",
    "quota": "{p} so'rovlar limiti tugagan yoki band. Birozdan so'ng qayta urinib ko'ring.",
    "model": "{p} model nomi topilmadi. .env da CLAUDE_MODEL / GEMINI_MODEL qiymatini tekshiring.",
    "network": "{p} serveriga ulanib bo'lmadi (internet, proxy yoki firewall).",
    "unknown": "{p} kutilmagan xato qaytardi (server logiga qarang).",
}


def classify(error: object) -> str:
    text = str(error).lower()
    for kind, needles in _RULES:
        if any(n in text for n in needles):
            return kind
    return "unknown"


def record_error(provider: str, error: object) -> None:
    kind = classify(error)
    _last_errors[provider] = (time.time(), kind, str(error)[:300])
    logger.warning("AI xatosi [%s/%s]: %s", provider, kind, str(error)[:300])


def clear_error(provider: str) -> None:
    _last_errors.pop(provider, None)


def failure_hint() -> str:
    now = time.time()
    lines = [
        _MESSAGES[kind].format(p=_PROVIDER_LABELS.get(provider, provider))
        for provider, (ts, kind, _) in _last_errors.items()
        if now - ts <= _RECENT_SECONDS
    ]
    return " ".join(lines)
