"""LongoUZ — bulutli (Neon/Supabase Postgres) bazani BIR MARTA tayyorlash va savollarni yuklash.

Ishlatish (kompyuteringizda, loyiha papkasida):
    python cloud_setup.py "postgresql://user:parol@host/db?sslmode=require"
yoki DATABASE_URL ni .env ga yozib:
    python cloud_setup.py

Nima qiladi: jadvallarni yaratadi, barcha tayyor mavzu va savollarni yuklaydi, hisobot beradi.
Qayta ishga tushirsangiz xavfsiz (mavjud savollar takrorlanmaydi, yangilari qo'shiladi).
"""
import asyncio
import os
import sys

if len(sys.argv) > 1 and sys.argv[1].strip():
    os.environ["DATABASE_URL"] = sys.argv[1].strip()

from dotenv import load_dotenv  # noqa: E402

load_dotenv()

if not os.getenv("DATABASE_URL"):
    print("XATO: DATABASE_URL yo'q. Misol: python cloud_setup.py \"postgresql://...\"")
    sys.exit(1)

import database as db  # noqa: E402
import exam_db  # noqa: E402


async def main():
    print("Baza:", "PostgreSQL" if not db.IS_SQLITE else "SQLite (!)")
    await db.init_web_db()
    # init_web_db Vercelda seed qilmaydi — bu yerda majburan
    await exam_db.seed_exam_content()
    async with db.async_session() as s:
        from sqlalchemy import select, func
        rows = (await s.execute(select(db.Question.subject, db.Question.mode, func.count()).group_by(db.Question.subject, db.Question.mode))).all()
    total = 0
    for subj, mode, n in sorted(rows):
        print(f"  {subj:10s} {mode:12s} {n:6d} savol")
        total += n
    print(f"JAMI: {total} savol. Tayyor!")


asyncio.run(main())
