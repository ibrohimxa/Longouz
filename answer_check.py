"""LongoUZ — ochiq (yozma) javobni AQLLI tekshirish.

Qoida asosida (tez, bepul):
  * raqamlar: 2,5 = 2.5 = 5/2 = 2.5e0 = 25·10⁻¹; birlik yozilgan bo'lsa ham ("2nC", "2 nC", "20 m/s") raqam to'g'ri bo'lsa qabul;
    ikkala tomonda ham birlik bo'lib, ular boshqa-boshqa bo'lsa (nC ≠ mC) — noto'g'ri;
  * yaxlitlash: kasr javobda 0,5% gacha farq qabul (3,33 ≈ 10/3); butun javobda aniq moslik;
  * foiz/daraja belgisi: "25%", "30°";
  * matn: kichik/katta harf, apostrof turlari, tinish belgilari, qo'shimcha so'zlar ("Bu Amir Temur"), yil/asr qo'shimchalari;
  * chala yozilgan (kamida yarmi va aniq bir so'z) va 1-2 harfli imlo xatosi.
Qoida hal qila olmagan javoblar uchun AI (Claude/Gemini) hakamlik qiladi (ai_router.judge_open_answers) —
bu main.py submit ichida bir marta, barcha shubhali javoblar uchun bitta so'rov bilan amalga oshadi.
"""
from __future__ import annotations

import re
import unicodedata

_APOS = "'`´ʻʼ’‘ʹ"
_SUP = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-", "⁺": "+"}
_SUB = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9"}

_NUM = r"[-+]?(?:\d{1,3}(?:[  ]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?|[.,]\d+)"


def _prep(text) -> str:
    s = unicodedata.normalize("NFKC", str(text or "")).strip()
    s = s.replace("−", "-").replace("–", "-").replace("—", "-").replace(" ", " ")
    # yuqori indeks: 10⁻³ -> 10^-3
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        if ch in _SUP:
            j = i
            digits = ""
            while j < len(s) and s[j] in _SUP:
                digits += _SUP[s[j]]
                j += 1
            out.append("^" + digits)
            i = j
            continue
        out.append(_SUB.get(ch, ch))
        i += 1
    s = "".join(out)
    for ch in _APOS:
        s = s.replace(ch, "'")
    return s


def _to_float(num: str) -> float | None:
    n = num.replace(" ", "").replace(" ", "")
    if n.count(",") + n.count(".") > 1:
        # 1,234.5 yoki 1.234,5 — oxirgi belgi o'nli ajratgich
        last = max(n.rfind(","), n.rfind("."))
        n = n[:last].replace(",", "").replace(".", "") + "." + n[last + 1:]
    else:
        n = n.replace(",", ".")
    try:
        return float(n)
    except ValueError:
        return None


_SCI = re.compile(rf"^\s*({_NUM})\s*(?:[x×*·⋅]|\*)\s*10\s*(?:\^|\*\*)?\s*\(?\s*([-+]?\d+)\s*\)?\s*(.*)$", re.I)
_E = re.compile(rf"^\s*({_NUM})\s*[eE]\s*([-+]?\d+)\s*(.*)$")
_FRAC = re.compile(r"^\s*([-+]?\d+(?:[.,]\d+)?)\s*/\s*(\d+(?:[.,]\d+)?)\s*(.*)$")
_PLAIN = re.compile(rf"^\s*({_NUM})\s*(.*)$")
_POW10 = re.compile(r"^\s*10\s*\^\s*\(?\s*([-+]?\d+)\s*\)?\s*(.*)$")


def parse_quantity(text) -> tuple[float | None, str]:
    """(son, birlik_matni). Son topilmasa (None, '')."""
    s = _prep(text)
    if not s:
        return None, ""
    m = _SCI.match(s)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v * 10 ** int(m.group(2)), m.group(3).strip()
    m = _POW10.match(s)
    if m:
        return 10.0 ** int(m.group(1)), m.group(2).strip()
    m = _E.match(s)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v * 10 ** int(m.group(2)), m.group(3).strip()
    m = _FRAC.match(s)
    if m:
        a, b = _to_float(m.group(1)), _to_float(m.group(2))
        if a is not None and b:
            return a / b, m.group(3).strip()
    m = _PLAIN.match(s)
    if m:
        v = _to_float(m.group(1))
        if v is not None:
            return v, m.group(2).strip()
    return None, ""


def _unit_key(u: str) -> str:
    u = _prep(u).lower().replace(" ", "").replace("·", "*").replace("⋅", "*")
    u = u.strip(".,;:!?()=")
    u = u.replace("**", "^")
    return u


_UNIT_OK = re.compile(r"^[A-Za-zА-Яа-яЁёʻ'’°%µμΩ/*·⋅\^\-\+\d\.\s()]{0,24}$")


def _unit_tail_ok(u: str) -> bool:
    """Birlik qismi 'oddiy' bo'lishi kerak: harflar, /, ^, daraja raqami; ichida boshqa mustaqil son bo'lmasin."""
    if not u:
        return True
    if not _UNIT_OK.match(u):
        return False
    # "5 3" kabi ikkinchi mustaqil son — birlik emas
    stripped = re.sub(r"\^\s*[-+]?\d+", "", u)
    stripped = re.sub(r"(?<=[A-Za-zА-Яа-я])\d+", "", stripped)
    return not re.search(r"\d", stripped)


def numbers_match(user_text, accepted_text) -> bool | None:
    """True/False — ikkalasi ham son bo'lsa; None — taqqoslab bo'lmaydi (matn)."""
    uv, uu = parse_quantity(user_text)
    av, au = parse_quantity(accepted_text)
    if uv is None or av is None:
        return None
    if not _unit_tail_ok(uu) or not _unit_tail_ok(au):
        return None
    if au and uu and _unit_key(au) != _unit_key(uu):
        # ikkalasida ham birlik bor, lekin har xil (nC / mC, m / km) — "%"/"°"/nuqta farqlarini hisobga olmaymiz
        ak, uk = _unit_key(au).strip("%°"), _unit_key(uu).strip("%°")
        if ak != uk and ak and uk:
            return False
    if av == int(av) and abs(av) < 1e15:
        return abs(uv - av) <= 1e-9 + 1e-9 * abs(av)
    return abs(uv - av) <= 1e-12 + 0.005 * abs(av)  # kasr javobda 0,5% yaxlitlash


# ----------------------------------------------------------------- matn
def normalize_text(text) -> str:
    s = _prep(text).lower()
    s = s.replace("‑", "-")
    s = s.replace("^", "").replace("sqrt", "√").replace("->", "→").replace("<->", "⇌").replace("⇄", "⇌")
    s = re.sub(r"[\"“”«».,;:!?()\[\]{}]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _loose(s: str) -> str:
    s = normalize_text(s)
    s = re.sub(r"(?<=[\d\s-])(yil|yilda|yilgi|yillar|asr|asrda|asrning)\b", "", s)
    s = re.sub(r"(?<=\d)[-\s]*(chi|nchi|inchi)\b", "", s)
    return re.sub(r"[\s\-']+", "", s)


_FILLER = {"bu", "u", "bo'ladi", "boladi", "javob", "to'g'ri", "togri", "deb", "ekan", "edi", "ya'ni", "yani", "va", "ham", "dir", "-dir",
           "the", "is", "a", "это", "и"}


def _tokens(s: str) -> list[str]:
    return [t for t in re.split(r"[\s\-/]+", normalize_text(s)) if t]


def _lev(a: str, b: str, limit: int = 2) -> int:
    if abs(len(a) - len(b)) > limit:
        return limit + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > limit:
            return limit + 1
        prev = cur
    return prev[-1]


def _tok_eq(a: str, b: str) -> bool:
    if a == b:
        return True
    if len(a) >= 5 and len(b) >= 5:
        return _lev(a, b, 1 if min(len(a), len(b)) < 9 else 2) <= (1 if min(len(a), len(b)) < 9 else 2)
    return False


def text_match(user_text: str, accepted_text: str) -> bool:
    na, ua = normalize_text(accepted_text), normalize_text(user_text)
    if not na or not ua:
        return False
    if na == ua or _loose(accepted_text) == _loose(user_text):
        return True
    at = [t for t in _tokens(accepted_text)]
    ut = [t for t in _tokens(user_text) if t not in _FILLER]
    if not at or not ut:
        return False
    # barcha kerakli so'zlar (imlo xatosi bilan ham) mavjud, ortiqcha so'zlar kam
    covered = [any(_tok_eq(a, u) for u in ut) for a in at]
    extra_num = any(re.fullmatch(r"[-+]?\d+(?:[.,]\d+)?", u) and not any(_tok_eq(a, u) for a in at) for u in ut)
    if all(covered) and len(ut) <= len(at) + 3 and not extra_num:
        return True
    # chala yozilgan: foydalanuvchi so'zlari kerakli so'zlarning bir qismi (≥50% belgilar) va aniq bir so'z (≥4 harf)
    if len(at) >= 2 and all(any(_tok_eq(a, u) for a in at) for u in ut):
        part = sum(len(a) for a, c in zip(at, [any(_tok_eq(a, u) for u in ut) for a in at]) if c)
        if part >= 0.5 * sum(len(a) for a in at) and any(len(u) >= 4 for u in ut):
            return True
    return False


_EXPR_OK = re.compile(r"^[0-9.,+\-*/^()√π\s]+$")


def eval_expr(text) -> float | None:
    """Matematik ifodani xavfsiz hisoblaydi: √8, 2√2, sqrt(16), 3^2, 1 1/2, π/2, 'x = 3'. Birlik yoki harf bo'lsa — None."""
    import ast
    import math
    s = _prep(text).lower().strip()
    s = re.sub(r"^[a-z]\s*=\s*", "", s)                      # x = 3 -> 3
    s = s.replace("sqrt", "√").replace("pi", "π").replace("×", "*").replace("·", "*").replace(":", "/").replace("÷", "/")
    s = re.sub(r"(\d),(\d)", r"\1.\2", s)                      # 0,5 -> 0.5
    if not s or not _EXPR_OK.match(s):
        return None
    s = re.sub(r"^\s*(\d+)\s+(\d+)\s*/\s*(\d+)\s*$", r"(\1+\2/\3)", s)   # 1 1/2 aralash kasr
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"√\(", "sqrt(", s)
    s = re.sub(r"√([0-9.]+|π)", r"sqrt(\1)", s)
    s = s.replace("π", "pi").replace("^", "**")
    s = re.sub(r"(\d|\))(sqrt|pi|\()", r"\1*\2", s)           # 2√2 -> 2*sqrt(2)
    try:
        tree = ast.parse(s, mode="eval")
    except SyntaxError:
        return None
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        if isinstance(n, ast.Name) and n.id == "pi":
            return math.pi
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.UAdd, ast.USub)):
            v = ev(n.operand)
            return v if isinstance(n.op, ast.UAdd) else -v
        if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
            a, b = ev(n.left), ev(n.right)
            if isinstance(n.op, ast.Pow) and (abs(b) > 50 or abs(a) > 1e6):
                raise ValueError
            return {ast.Add: a + b, ast.Sub: a - b, ast.Mult: a * b}.get(type(n.op)) if not isinstance(n.op, (ast.Div, ast.Pow)) else (a / b if isinstance(n.op, ast.Div) else a ** b)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "sqrt" and len(n.args) == 1:
            v = ev(n.args[0])
            if v < 0:
                raise ValueError
            return math.sqrt(v)
        raise ValueError
    try:
        v = ev(tree)
        return v if isinstance(v, float) and math.isfinite(v) else None
    except (ValueError, ZeroDivisionError, OverflowError, TypeError):
        return None


def check_open_answer(user_answer, accepted: list[str]) -> bool:
    if user_answer is None:
        return False
    ua = str(user_answer)
    if not ua.strip():
        return False
    uv = eval_expr(ua)
    for acc in accepted or []:
        if uv is not None:
            av = eval_expr(acc)
            if av is not None and abs(uv - av) <= 1e-9 + 0.005 * abs(av):
                return True
    for acc in accepted or []:
        acc = str(acc)
        nm = numbers_match(ua, acc)
        if nm is True:
            return True
        if nm is False:
            continue
        if text_match(ua, acc):
            return True
    return False


def is_numeric_answer(accepted: list[str]) -> bool:
    return any(parse_quantity(a)[0] is not None for a in accepted or [])
