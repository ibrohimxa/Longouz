"""Tayyor savollar va mavzular bazasi (tarix: sinflar kesimida; biologiya, kimyo, fizika, matematika: DTM)."""


def load_packs():
    packs = []
    try:
        from . import sci_figq
        sci_figq.apply()
    except ImportError:
        pass
    try:
        from . import history
        packs.append(history.pack())
    except ImportError:
        pass
    try:
        from . import biology
        packs.append(biology.pack())
    except ImportError:
        pass
    try:
        from . import chemistry
        packs.append(chemistry.pack())
    except ImportError:
        pass
    try:
        from . import physics
        packs.append(physics.pack())
    except ImportError:
        pass
    try:
        from . import native
        packs.append(native.pack())
    except ImportError:
        pass
    # Matematika: asosiy nazariy (mathematics.py) + chizmali (math_fig.py) birlashtiriladi
    try:
        from . import mathematics
        packs.append(mathematics.pack())
    except ImportError:
        pass
    try:
        from . import math_fig
        packs.append(math_fig.pack())
    except ImportError:
        pass
    for mod in ("english", "russian", "ielts"):
        try:
            m = __import__(f"{__name__}.{mod}", fromlist=["pack"])
            packs.append(m.pack())
        except ImportError:
            pass
    # v215: hisoblanadigan (to'g'riligi kafolatlangan) qo'shimcha savollar
    try:
        from . import gen_v215
        gen_v215.extend(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("gen_v215 yuklanmadi: %s", e)
    try:
        from . import gen_v217
        gen_v217.extend(packs)
        from . import gen_v224
        gen_v224.extend(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("gen_v217 yuklanmadi: %s", e)
    try:
        from . import gen_v229
        gen_v229.extend(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("gen_v229 yuklanmadi: %s", e)
    try:
        sanitize_packs(packs)
    except Exception as e:  # pragma: no cover
        import logging
        logging.getLogger(__name__).warning("sanitize_packs ishlamadi: %s", e)
    apply_quota_tiers(packs)
    return packs


# ---------------------------------------------------------------------------
# v230: savollar sifati — javobni oshkor qiluvchi belgilar va kontekstsiz savollar
# ---------------------------------------------------------------------------
import re as _re

_PAREN = _re.compile(r"\s*\(([^()]{2,80})\)")
_LETTER_HINT = _re.compile(r"\s*\(\s*(?:[A-ZА-ЯЁЎҚҒҲ][a-zа-яёʼ'‘’]?\s*\.{2,3}\s*)+(?:[a-zа-яʼ']+\s*)?\)\s*\.?|\s*\(\s*[A-ZА-ЯЁЎҚҒҲ][a-zʼ'‘’]?\.{2,3}\s*$")
_MATHY = _re.compile(r"[=<>√^²³⁰¹⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉·×÷±∞π;]|\d\s*[,.]\s*\d|^\s*[\d\s,.;:+\-−/]+\s*$")
_CTX_START = _re.compile(r"^Shu\s+(?=\S)")


def _strip_giveaway_paren(opt: str) -> str | None:
    """'Monosemantik (bir ma'noli)' -> 'Monosemantik'. Matematik/kimyoviy ifodalarga tegmaydi."""
    m = _PAREN.search(opt)
    if not m:
        return None
    inner = m.group(1).strip()
    is_year = bool(_re.fullmatch(r"(?:mil\. avv\. )?\d{3,4}(?:[-–]\d{2,4})?(?:-yil)?", inner))
    if not is_year and (_MATHY.search(inner) or not _re.search(r"[A-Za-zА-Яа-яЎўҚқҒғҲҳʼ']{3,}", inner)):
        return None
    base = _PAREN.sub("", opt, count=1).strip(" ,;:-—")
    if len(_re.sub(r"[^\wʼ']", "", base)) < 2 or _MATHY.search(base) and not _re.search(r"[A-Za-zА-Яа-я]{3,}", base):
        return None
    return base


def _question_root(qs: list, i: int):
    """'Shu ...' savoli uchun shartni beradigan oldingi (o'zi 'Shu' bilan boshlanmagan) savol."""
    j = i - 1
    while j >= 0 and _CTX_START.match(qs[j]["question"]):
        j -= 1
    if j >= 0 and qs[j].get("topic") == qs[i].get("topic"):
        return qs[j]
    return None


def _context_of(root_text: str) -> str:
    t = root_text.strip()
    # oxirgi so'roq gapini olib tashlab, shart qismini qoldiramiz
    parts = _re.split(r"(?<=[.:])\s+", t)
    if len(parts) >= 2 and parts[-1].rstrip().endswith("?"):
        return " ".join(parts[:-1]).rstrip(" .:") + "."
    return "Shart: " + t.rstrip(" ?") + "."


def sanitize_packs(packs) -> dict:
    stats = {"paren": 0, "letter": 0, "ctx": 0}
    for pack in packs:
        qs = pack["questions"]
        for i, q in enumerate(qs):
            # 1) faqat to'g'ri variantda qavs ichidagi izoh bo'lsa — javobni oshkor qiladi
            opts = q.get("options") or []
            ci = q.get("correct_index", -1)
            if q.get("qtype", "closed") == "closed" and len(opts) >= 3 and isinstance(ci, int) and 0 <= ci < len(opts):
                has = ["(" in str(o) for o in opts]
                if has[ci] and sum(has) == 1 and str(opts[ci]).count("(") == 1:
                    base = _strip_giveaway_paren(str(opts[ci]))
                    if base and base.lower() not in {str(o).strip().lower() for k, o in enumerate(opts) if k != ci}:
                        extra = _PAREN.search(str(opts[ci])).group(1)
                        new_opts = list(opts)
                        new_opts[ci] = base
                        q["options"] = new_opts
                        exp = (q.get("explanation") or "").strip()
                        if extra.lower() not in exp.lower():
                            q["explanation"] = (f"{base} ({extra}). " + exp).strip()
                        stats["paren"] += 1
            # 2) ochiq savoldagi bosh harf ishorasi: "(Q...)" -> olib tashlanadi
            text = q["question"]
            new = _LETTER_HINT.sub("", text).rstrip()
            if new != text and len(new) > 15:
                if not new.endswith(("?", ".", ":")):
                    new += "."
                q["question"] = new
                stats["letter"] += 1
        # 3) "Shu jism ..." — oldingi savol shartiga bog'liq; shart savolning o'ziga qo'shiladi
        originals = [q["question"] for q in qs]
        for i, q in enumerate(qs):
            if not _CTX_START.match(originals[i]):
                continue
            if q.get("figure_json"):
                # chizma savolning o'zida bor — "Shu" so'zi ortiqcha
                rest = _CTX_START.sub("", originals[i])
                q["question"] = rest[:1].upper() + rest[1:]
                stats["ctx"] += 1
                continue
            root = _question_root([{"question": t, "topic": qq.get("topic")} for t, qq in zip(originals, qs)], i)
            if root is None:
                continue
            q["question"] = _context_of(root["question"]) + "\n" + originals[i]
            stats["ctx"] += 1
    return stats


# Mavzu bo'yicha savol kvotasi: Bepul 25, Pro jami 60 (≈2,4×), Ultra jami ~125 (≈5×)
QUOTA_FREE, QUOTA_PRO, QUOTA_ULTRA = 25, 60, 125


def apply_quota_tiers(packs):
    """Har mavzudagi savollarni qiyinlik va turi bo'yicha aralashtirib, tartib bo'yicha tarifga biriktiradi:
    birinchi 25 ta -> Bepul, keyingi 35 ta -> Pro, qolgani -> Ultra. Bepul to'plamda yozma/moslashtirish ham bo'ladi."""
    import hashlib
    from collections import defaultdict
    for pack in packs:
        by_topic = defaultdict(list)
        for q in pack["questions"]:
            by_topic[q.get("topic")].append(q)
        for items in by_topic.values():
            def h(q):
                return hashlib.md5(q["question"].strip().lower().encode()).hexdigest()
            groups = defaultdict(list)
            for q in sorted(items, key=h):
                kind = "c" if q.get("qtype", "closed") == "closed" else "x"
                groups[(q.get("difficulty", 2), kind)].append(q)
            order = [(1, "c"), (2, "c"), (3, "c"), (2, "x"), (1, "x"), (2, "c"), (3, "x")]
            seq = []
            while any(groups.values()):
                for k in order:
                    if groups.get(k):
                        seq.append(groups[k].pop(0))
                for k in list(groups):
                    if k not in order and groups[k]:
                        seq.append(groups[k].pop(0))
            for i, q in enumerate(seq):
                n = len(seq)
                # savol kam bo'lsa ham pullik tariflarda qo'shimcha savol qolishi uchun ulush ishlatiladi
                f_cut = min(QUOTA_FREE, max(4, round(n * 0.45)))
                p_cut = min(QUOTA_PRO, max(f_cut + 1, round(n * 0.75)))
                q["min_plan"] = 0 if i < f_cut else (1 if i < p_cut else 2)
    return packs
