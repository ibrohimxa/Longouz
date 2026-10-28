"""Savollarni ixcham yozish uchun yordamchilar (faqat tayyor bank uchun).

    C(d, "savol", "to'g'ri javob", ["xato1", "xato2", "xato3"], "izoh", b="madaniyat")   — yopiq test
    O(d, "savol (yilni yozing)", ["1398", "1398-yil"], "izoh")                           — ochiq (yozma) javob
    M(d, [("chap1","o'ng1"), ("chap2","o'ng2"), ("chap3","o'ng3")], "izoh")             — moslashtirish

d: 1 oson, 2 o'rta, 3 qiyin. b: blok (siyosiy | ijtimoiy | madaniyat); moslashtirish har doim 'moslash'.
"""
import hashlib
import random


def _rng(text: str) -> random.Random:
    return random.Random(int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16))


def C(d, question, correct, wrong, expl="", b=None, fig=None):
    """fig — savol chizmasi: SVG matni (content/figs.py)."""
    return {"kind": "c", "d": d, "q": question, "a": correct, "w": list(wrong), "e": expl, "b": b, "fig": fig}


def O(d, question, accept, expl="", b=None):
    if isinstance(accept, str):
        accept = [accept]
    return {"kind": "o", "d": d, "q": question, "acc": list(accept), "e": expl, "b": b}


def M(d, pairs, expl="", b=None):
    return {"kind": "m", "d": d, "pairs": list(pairs), "e": expl, "b": "moslash"}


def T(code, items):
    return (code, items)


def _build_match(item):
    pairs = item["pairs"]
    n = len(pairs)
    rng = _rng("|".join(l for l, _ in pairs))
    rights = [r for _, r in pairs]
    order = list(range(n))
    rng.shuffle(order)
    if order == list(range(n)) and n > 1:
        order = order[1:] + order[:1]
    letters = "ABCDEF"[:n]
    # letter j shows rights[order[j]]
    left_lines = [f"{i + 1}. {pairs[i][0]}" for i in range(n)]
    right_lines = [f"{letters[j]}) {rights[order[j]]}" for j in range(n)]
    # correct mapping: left i -> letter j such that order[j] == i
    correct_map = [letters[order.index(i)] for i in range(n)]
    correct = ", ".join(f"{i + 1}-{correct_map[i]}" for i in range(n))
    # distractors: other distinct permutations of letters
    import itertools
    perms = [p for p in itertools.permutations(letters) if list(p) != correct_map]
    rng.shuffle(perms)
    wrong = []
    for p in perms:
        s = ", ".join(f"{i + 1}-{p[i]}" for i in range(n))
        if s != correct and s not in wrong:
            wrong.append(s)
        if len(wrong) == 3:
            break
    text = "Moslashtiring:\n" + "\n".join(left_lines) + "\n" + "\n".join(right_lines)
    return text, correct, wrong


def expand(topic_name, grade, items, default_block):
    """Yozuvlarni baza formatiga o'tkazadi va tarif darajasini (min_plan) belgilaydi."""
    out = []
    seen_d = {1: 0, 2: 0, 3: 0}
    for it in items:
        d = it["d"]
        seen_d[d] += 1
        n = seen_d[d]
        # oson -> hamma uchun; o'rtaning dastlabki 3 tasi -> hamma uchun, qolgani Pro;
        # qiyinning dastlabki 2 tasi -> Pro, qolgani Ultra
        if d == 1:
            plan = 0
        elif d == 2:
            plan = 0 if n <= 3 else 1
        else:
            plan = 1 if n <= 2 else 2
        if it.get("u"):
            plan = 2
        rec = {"topic": topic_name, "grade": grade, "difficulty": d, "explanation": it["e"], "min_plan": plan}
        if it["kind"] == "o":
            rec.update({"question": it["q"], "options": it["acc"], "correct_index": 0, "qtype": "open",
                        "block": it["b"] or default_block})
        else:
            if it["kind"] == "m":
                text, correct, wrong = _build_match(it)
                qtype, block = "match", "moslash"
            else:
                text, correct, wrong = it["q"], it["a"], it["w"]
                qtype, block = "closed", (it["b"] or default_block)
            opts = [correct] + list(wrong)
            r = _rng(text)
            order = list(range(len(opts)))
            r.shuffle(order)
            shuffled = [opts[i] for i in order]
            rec.update({"question": text, "options": shuffled, "correct_index": order.index(0),
                        "qtype": qtype, "block": block})
            if it.get("fig"):
                import json as _json
                rec["figure_json"] = _json.dumps({"q": {"type": "svg", "svg": it["fig"]}, "o": [None] * 4},
                                                 ensure_ascii=False, separators=(",", ":"))
        out.append(rec)
    return out


def validate(records):
    """Bank sifatini tekshiradi; muammolar ro'yxatini qaytaradi."""
    problems = []
    seen = set()
    for r in records:
        t = r["question"].strip()
        key = t.lower()
        if key in seen:
            problems.append(("takror savol", t[:70]))
        seen.add(key)
        if r["qtype"] == "open":
            if not r["options"] or any(not str(a).strip() for a in r["options"]):
                problems.append(("ochiq javob bo'sh", t[:70]))
            continue
        opts = r["options"]
        if len(opts) != 4:
            problems.append(("variantlar soni 4 emas", t[:70]))
        if len(set(o.strip().lower() for o in opts)) != len(opts):
            problems.append(("takror variant", t[:70]))
        if any(not o.strip() for o in opts):
            problems.append(("bo'sh variant", t[:70]))
        if not 0 <= r["correct_index"] < len(opts):
            problems.append(("kalit noto'g'ri", t[:70]))
        if len(t) > 1900 or any(len(o) > 600 for o in opts):
            problems.append(("matn uzun", t[:70]))
    return problems
