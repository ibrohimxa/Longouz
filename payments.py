"""LongoUZ — tarif xaridi (v244).

Narxlar (yagona manba — barcha sahifalar shu yerdan oladi):
  Pro   — 25 000 so'm/oy, yillik 2% chegirma
  Ultra — 40 000 so'm/oy, yillik 5% chegirma

Hozircha to'lov provayderi (Click/Payme) ulanmagan: karta kiritilib «sotib olinganda» PUL YECHILMAYDI,
lekin xarid bazaga yoziladi va tanlangan tarif darhol ochiladi.

XAVFSIZLIK: karta to'liq raqami va CVV hech qachon saqlanmaydi (bu qonunan taqiqlangan — PCI DSS).
Bazaga faqat: karta turi (UzCard/HUMO/Visa/Mastercard), niqoblangan raqam (8600 •••• •••• 1234), amal muddati, karta egasi ismi.
"""
from __future__ import annotations

import re
from datetime import date, datetime, timedelta

from sqlalchemy import Date, DateTime, Integer, String, desc, func, select
from sqlalchemy.orm import Mapped, mapped_column

import database as db

PRICES = {"pro": 25000, "ultra": 40000}
YEARLY_DISCOUNT = {"pro": 2, "ultra": 5}
PLAN_NAMES = {"free": "Bepul", "pro": "Pro", "ultra": "Ultra"}


def fmt_sum(n: int) -> str:
    return f"{int(n):,}".replace(",", " ")


def yearly_price(plan: str) -> int:
    return int(round(PRICES[plan] * 12 * (100 - YEARLY_DISCOUNT[plan]) / 100))


def price_info() -> dict:
    """Shablonlar uchun: plan_prices.pro.monthly_label va hokazo."""
    out = {}
    for p, m in PRICES.items():
        y = yearly_price(p)
        out[p] = {"monthly": m, "yearly": y, "discount": YEARLY_DISCOUNT[p], "full_year": m * 12,
                  "monthly_label": f"{fmt_sum(m)} so'm/oy", "yearly_label": f"{fmt_sum(y)} so'm/yil",
                  "monthly_num": fmt_sum(m), "yearly_num": fmt_sum(y), "save": fmt_sum(m * 12 - y)}
    out["max_discount"] = max(YEARLY_DISCOUNT.values())
    return out


class PlanPurchase(db.Base):
    __tablename__ = "plan_purchases"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    plan: Mapped[str] = mapped_column(String(10))
    cycle: Mapped[str] = mapped_column(String(10), default="monthly")      # monthly | yearly
    amount: Mapped[int] = mapped_column(Integer, default=0)                # so'm
    card_brand: Mapped[str] = mapped_column(String(20), default="")
    card_mask: Mapped[str] = mapped_column(String(32), default="")         # 8600 •••• •••• 1234
    card_exp: Mapped[str] = mapped_column(String(5), default="")           # MM/YY
    card_holder: Mapped[str] = mapped_column(String(80), default="")
    status: Mapped[str] = mapped_column(String(16), default="demo")        # demo = pul yechilmagan
    valid_until: Mapped[date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)


_ready = False


async def _ensure() -> None:
    global _ready
    if not _ready:
        async with db.engine.begin() as conn:
            await conn.run_sync(lambda c: db.Base.metadata.create_all(c, tables=[PlanPurchase.__table__]))
        _ready = True


def card_brand(d: str) -> str:
    if d.startswith("8600") or d.startswith("5614"):
        return "UzCard"
    if d.startswith("9860"):
        return "HUMO"
    if d.startswith("4"):
        return "Visa"
    if re.match(r"^(5[1-5]|2(2[2-9]|[3-6]\d|7[01]|720))", d):
        return "Mastercard"
    return "Karta"


def _luhn_ok(d: str) -> bool:
    total, alt = 0, False
    for ch in reversed(d):
        n = int(ch)
        if alt:
            n *= 2
            if n > 9:
                n -= 9
        total += n
        alt = not alt
    return total % 10 == 0


def validate_card(number: str, exp: str) -> tuple[str, str, str]:
    """(raqam, MM/YY, xato). Xato bo'sh bo'lsa — karta yaroqli. UzCard/HUMO Luhn'ga bo'ysunmasligi mumkin."""
    d = re.sub(r"\D", "", number or "")
    if len(d) != 16:
        return d, "", "Karta raqami 16 ta raqamdan iborat bo'lishi kerak."
    brand = card_brand(d)
    if brand in ("Visa", "Mastercard") and not _luhn_ok(d):
        return d, "", "Karta raqami noto'g'ri. Tekshirib qayta kiriting."
    if brand == "Karta":
        return d, "", "Faqat UzCard, HUMO, Visa yoki Mastercard kartalari qabul qilinadi."
    m = re.match(r"^\s*(\d{2})\s*/\s*(\d{2})\s*$", exp or "")
    if not m or not 1 <= int(m.group(1)) <= 12:
        return d, "", "Amal muddatini OO/YY ko'rinishida kiriting (masalan 08/28)."
    mm, yy = int(m.group(1)), 2000 + int(m.group(2))
    today = date.today()
    if (yy, mm) < (today.year, today.month) or yy > today.year + 15:
        return d, "", "Karta amal muddati o'tgan yoki noto'g'ri."
    return d, f"{mm:02d}/{m.group(2)}", ""


def mask(d: str) -> str:
    return f"{d[:4]} •••• •••• {d[-4:]}"


async def record_purchase(user_id: int, plan: str, cycle: str, card_number: str, card_exp: str, holder: str) -> PlanPurchase:
    """Xaridni yozadi va tarifni ochadi. Pul YECHILMAYDI (to'lov provayderi hali ulanmagan)."""
    await _ensure()
    cycle = "yearly" if cycle == "yearly" else "monthly"
    amount = yearly_price(plan) if cycle == "yearly" else PRICES[plan]
    until = date.today() + timedelta(days=365 if cycle == "yearly" else 30)
    p = PlanPurchase(user_id=user_id, plan=plan, cycle=cycle, amount=amount, card_brand=card_brand(card_number),
                     card_mask=mask(card_number), card_exp=card_exp, card_holder=(holder or "").strip()[:80],
                     status="demo", valid_until=until)
    async with db.async_session() as s:
        s.add(p)
        await s.commit()
        await s.refresh(p)
    await db.admin_set_user_plan(user_id, plan)
    try:
        await db.create_notification(user_id, "plan", title=f"{PLAN_NAMES[plan]} tarifi ochildi",
                                     body=f"{PLAN_NAMES[plan]} ({'yillik' if cycle == 'yearly' else 'oylik'}) tarifingiz faollashdi. "
                                          f"Karta: {p.card_mask}. Hozircha kartadan pul yechilmadi.")
    except Exception:  # noqa: BLE001
        pass
    return p


async def list_purchases(limit: int = 200) -> dict:
    await _ensure()
    async with db.async_session() as s:
        rows = (await s.execute(select(PlanPurchase, db.WebUser.first_name, db.WebUser.email)
                                .join(db.WebUser, db.WebUser.id == PlanPurchase.user_id, isouter=True)
                                .order_by(desc(PlanPurchase.id)).limit(limit))).all()
        totals = dict((await s.execute(select(PlanPurchase.plan, func.count()).group_by(PlanPurchase.plan))).all())
        summ = int((await s.execute(select(func.coalesce(func.sum(PlanPurchase.amount), 0)))).scalar() or 0)
    return {"items": [{"p": p, "name": n or "", "email": e or ""} for p, n, e in rows], "totals": totals, "sum": summ}
