"""LongoUZ — Gemini «agent» dvigateli (v243).

* `run_agent(...)` — Gemini'ga VOSITALAR (function calling) beriladi: u o'zi bazadan savol qidiradi, shikoyatni ochadi,
  internetdan (Google Search) ma'lumot topadi, xotiraga yozadi va hokazo — keyin yakuniy javob qaytaradi.
* `web_search(query)` — Gemini + Google Search grounding: internetdan qidirib, qisqa xulosa va manbalarni qaytaradi.

Bepul Gemini kaliti bilan ishlaydi (karta talab qilinmaydi). Model band bo'lsa — keyingi modelga o'tiladi.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

import ai_gemini
import ai_keys

logger = logging.getLogger("longouz.agent")

AGENT_MODELS = ("gemini-3.6-flash", "gemini-3.8-flash", "gemini-3.5-flash-lite")
SEARCH_MODELS = ("gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.8-flash")


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    fn: Callable[[dict], Awaitable[Any]]
    label: str = ""          # admin oynasida ko'rinadigan nom («Savollar qidirilmoqda»)

    def decl(self) -> dict:
        return {"name": self.name, "description": self.description, "parameters_json_schema": self.parameters}


@dataclass
class AgentResult:
    text: str = ""
    steps: list = field(default_factory=list)   # [{"tool": name, "label": .., "args": {..}, "ok": bool, "ms": int}]
    model: str = ""
    ok: bool = False


def _models() -> list[str]:
    first = (ai_keys.get("GEMINI_MODEL", "") or "").strip()
    order = [first] if first else []
    now = time.time()
    rest = [m for m in AGENT_MODELS if m != first]
    rest.sort(key=lambda m: 1 if ai_gemini._BUSY_UNTIL.get(m, 0) > now else 0)
    return order + rest


def _is_busy(exc: Exception) -> bool:
    t = str(exc)
    code = getattr(exc, "code", None)
    return code in (429, 500, 503, 504) or "UNAVAILABLE" in t or "RESOURCE_EXHAUSTED" in t or "overloaded" in t.lower()


def _to_contents(history: list[dict]) -> list[dict]:
    out = []
    for m in history:
        text = str(m.get("text") or m.get("content") or "").strip()
        if not text:
            continue
        out.append({"role": "model" if m.get("role") in ("assistant", "model") else "user", "parts": [{"text": text}]})
    # Gemini birinchi xabar foydalanuvchidan bo'lishini kutadi
    while out and out[0]["role"] != "user":
        out.pop(0)
    return out


async def run_agent(system: str, history: list[dict], tools: list[Tool], *, deadline: float = 50.0, max_steps: int = 8,
                    thinking: str = "low", max_tokens: int = 6000, json_final: bool = False) -> AgentResult:
    """Vosita chaqiruvlari bilan Gemini suhbati. history: [{"role": "user"|"assistant", "text": "..."}]."""
    res = AgentResult()
    client = ai_gemini._get_client()
    if client is None:
        res.text = "Gemini kaliti sozlanmagan (admin → Kalitlar)."
        return res
    from google.genai import types

    by_name = {t.name: t for t in tools}
    started = time.monotonic()
    base_contents = _to_contents(history)
    if not base_contents:
        res.text = "Savol yozing."
        return res
    sys_text = system + ("\n\nYAKUNIY JAVOBNI FAQAT JSON KO'RINISHIDA QAYTARING." if json_final else "")
    last_err: Exception | None = None
    for model in _models():
        contents = list(base_contents)
        res.steps = []
        try:
            for _step in range(max_steps + 1):
                left = deadline - (time.monotonic() - started)
                if left < 3:
                    raise asyncio.TimeoutError()
                cfg: dict = {
                    "system_instruction": sys_text, "max_output_tokens": max_tokens,
                    "automatic_function_calling": {"disable": True},
                    "thinking_config": {"thinking_level": thinking},
                }
                if tools and _step < max_steps:
                    cfg["tools"] = [{"function_declarations": [t.decl() for t in tools]}]
                resp = await asyncio.wait_for(client.aio.models.generate_content(model=model, contents=contents, config=cfg),
                                              timeout=min(left, 40))
                calls = list(resp.function_calls or [])
                if not calls:
                    res.text = (resp.text or "").strip()
                    res.model, res.ok = model, bool(res.text)
                    ai_gemini._BUSY_UNTIL.pop(model, None)
                    if res.ok:
                        return res
                    break
                cand = resp.candidates[0] if resp.candidates else None
                if cand is not None and cand.content is not None:
                    contents.append(cand.content)   # o'ylash imzolari (thought signatures) saqlanadi
                parts = []
                for fc in calls[:6]:
                    tool = by_name.get(fc.name or "")
                    t0 = time.monotonic()
                    args = dict(fc.args or {})
                    if tool is None:
                        out: Any = {"error": f"'{fc.name}' degan vosita yo'q"}
                        ok = False
                    else:
                        try:
                            out = await asyncio.wait_for(tool.fn(args), timeout=max(3.0, min(30.0, deadline - (time.monotonic() - started) - 2)))
                            ok = True
                        except Exception as exc:  # noqa: BLE001
                            logger.info("Vosita %s xatosi: %s", fc.name, exc)
                            out, ok = {"error": str(exc)[:300]}, False
                    res.steps.append({"tool": fc.name, "label": (tool.label if tool else fc.name), "args": _short(args),
                                      "ok": ok, "ms": int((time.monotonic() - t0) * 1000)})
                    payload = out if isinstance(out, dict) else {"result": out}
                    blob = json.dumps(payload, ensure_ascii=False, default=str)
                    if len(blob) > 14000:
                        payload = {"result_truncated": blob[:14000]}
                    parts.append(types.Part(function_response=types.FunctionResponse(id=getattr(fc, "id", None), name=fc.name, response=payload)))
                contents.append(types.Content(role="user", parts=parts))
        except asyncio.TimeoutError as exc:
            last_err = exc
            logger.warning("Agent %s: vaqt tugadi", model)
            if res.steps and time.monotonic() - started > deadline - 3:
                break
            ai_gemini._BUSY_UNTIL[model] = time.time() + 90
            continue
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            logger.warning("Agent %s xatosi: %s", model, str(exc)[:300])
            if _is_busy(exc) or getattr(exc, "code", None) in (400, 404):
                ai_gemini._BUSY_UNTIL[model] = time.time() + 120
                continue
            break
    if not res.text:
        res.text = ("Gemini hozir band yoki limit tugadi — bir daqiqadan so'ng qayta urinib ko'ring."
                    if last_err is not None else "Javob olinmadi.")
    return res


def _short(args: dict) -> dict:
    out = {}
    for k, v in list(args.items())[:6]:
        s = v if isinstance(v, (int, float, bool)) else str(v)
        out[k] = s[:80] if isinstance(s, str) else s
    return out


def parse_json(text: str) -> dict | None:
    t = (text or "").strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t.lower().startswith("json"):
            t = t[4:]
    try:
        v = json.loads(t)
        return v if isinstance(v, dict) else None
    except ValueError:
        pass
    i, j = t.find("{"), t.rfind("}")
    if 0 <= i < j:
        try:
            v = json.loads(t[i:j + 1])
            return v if isinstance(v, dict) else None
        except ValueError:
            return None
    return None


# ------------------------------------------------------------------ internet qidiruv
_SEARCH_CACHE: dict[str, tuple[float, dict]] = {}


async def web_search(query: str, focus: str = "") -> dict:
    """Google qidiruvi orqali Gemini javobi: {"text": "...", "sources": [{"title", "url"}]}."""
    query = (query or "").strip()[:400]
    if not query:
        return {"text": "", "sources": []}
    key = (focus + "|" + query).lower()
    hit = _SEARCH_CACHE.get(key)
    if hit and time.time() - hit[0] < 3600:
        return hit[1]
    client = ai_gemini._get_client()
    if client is None:
        return {"text": "", "sources": [], "error": "Gemini kaliti yo'q"}
    prompt = ("Google'da qidirib, quyidagi savolga ANIQ faktlar bilan qisqa (5-8 gap) javob ber. Sana, raqam, nomlarni aniq yoz. "
              "Ishonchli manbalarni (rasmiy saytlar, ensiklopediyalar, darsliklar) afzal ko'r. O'zbek tilida yoz.\n"
              + (f"Kontekst: {focus}\n" if focus else "") + f"Savol: {query}")
    last = ""
    for model in SEARCH_MODELS:
        if ai_gemini._BUSY_UNTIL.get(model, 0) > time.time():
            continue
        try:
            resp = await asyncio.wait_for(client.aio.models.generate_content(
                model=model, contents=prompt,
                config={"tools": [{"google_search": {}}], "max_output_tokens": 2500,
                        "thinking_config": {"thinking_level": "low"}}), timeout=28)
            sources = []
            try:
                gm = resp.candidates[0].grounding_metadata
                for ch in (gm.grounding_chunks or [])[:8] if gm else []:
                    w = getattr(ch, "web", None)
                    if w and getattr(w, "uri", None):
                        sources.append({"title": (w.title or "")[:120], "url": w.uri})
            except Exception:  # noqa: BLE001
                pass
            out = {"text": (resp.text or "").strip()[:4000], "sources": sources}
            if out["text"]:
                _SEARCH_CACHE[key] = (time.time(), out)
                if len(_SEARCH_CACHE) > 200:
                    for k in sorted(_SEARCH_CACHE, key=lambda k: _SEARCH_CACHE[k][0])[:100]:
                        _SEARCH_CACHE.pop(k, None)
                return out
        except Exception as exc:  # noqa: BLE001
            last = str(exc)[:200]
            logger.info("web_search %s: %s", model, last)
            if _is_busy(exc):
                ai_gemini._BUSY_UNTIL[model] = time.time() + 90
    return {"text": "", "sources": [], "error": last or "qidiruv natija bermadi"}
