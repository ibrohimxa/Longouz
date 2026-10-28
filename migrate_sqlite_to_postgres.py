"""
LongoUZ — SQLite'dan PostgreSQL'ga ma'lumotlarni ko'chirish.

Ishlatish:
  1) PostgreSQL'da bo'sh baza yarating:   createdb longouz
  2) python migrate_sqlite_to_postgres.py --source longouz_web.db \
         --target postgresql+asyncpg://user:parol@localhost:5432/longouz
  3) .env faylga qo'shing:  DATABASE_URL=postgresql+asyncpg://user:parol@localhost:5432/longouz
  4) Serverni qayta ishga tushiring.

Skript jadvallarni yaratadi, barcha qatorlarni (foydalanuvchilar, natijalar, savollar,
bildirishnomalar va h.k.) ko'chiradi va id ketma-ketliklarini to'g'rilaydi. Maqsadli
baza BO'SH bo'lishi kerak (aks holda --force bilan jadvallar tozalanadi).
"""
import argparse
import asyncio
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text  # noqa: E402
from sqlalchemy.ext.asyncio import create_async_engine  # noqa: E402

CHUNK = 2000


async def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="SQLite fayl yo'li (longouz_web.db)")
    ap.add_argument("--target", required=True, help="postgresql+asyncpg://... manzil")
    ap.add_argument("--force", action="store_true", help="maqsadli bazadagi jadvallarni tozalaydi")
    args = ap.parse_args()

    if not os.path.exists(args.source):
        print("Manba fayl topilmadi:", args.source)
        return 2
    if not args.target.startswith("postgresql"):
        print("--target postgresql+asyncpg://... bo'lishi kerak")
        return 2

    # database.py muhit o'zgaruvchisidan engine yaratadi — metadata olish uchun SQLite rejimida import qilamiz
    os.environ.pop("DATABASE_URL", None)
    import database as db  # noqa: E402

    tables = list(db.Base.metadata.sorted_tables)  # tashqi kalitlar tartibida
    engine = create_async_engine(args.target)
    src = sqlite3.connect(args.source)
    src.row_factory = sqlite3.Row
    src_tables = {r[0] for r in src.execute("select name from sqlite_master where type='table'")}

    async with engine.begin() as conn:
        await conn.run_sync(db.Base.metadata.create_all)
        if args.force:
            names = ", ".join(f'"{t.name}"' for t in tables)
            await conn.execute(text(f"TRUNCATE {names} RESTART IDENTITY CASCADE"))
        else:
            for t in tables:
                n = (await conn.execute(text(f'select count(*) from "{t.name}"'))).scalar_one()
                if n:
                    print(f"Maqsadli baza bo'sh emas ({t.name}: {n} qator). --force bilan tozalang.")
                    await engine.dispose()
                    return 3

    total = 0
    for t in tables:
        if t.name not in src_tables:
            continue
        cols = [c.name for c in t.columns]
        src_cols = {r[1] for r in src.execute(f'pragma table_info("{t.name}")')}
        use = [c for c in cols if c in src_cols]
        rows = src.execute(f'select {", ".join(chr(34) + c + chr(34) for c in use)} from "{t.name}"').fetchall()
        if not rows:
            print(f"  {t.name}: 0")
            continue
        bool_cols = {c.name for c in t.columns if c.type.__class__.__name__ == "Boolean"}
        dt_cols = {c.name for c in t.columns if c.type.__class__.__name__ in ("DateTime", "Date")}
        from datetime import datetime, date

        def conv(name, v):
            if v is None:
                return None
            if name in bool_cols:
                return bool(v)
            if name in dt_cols and isinstance(v, str):
                try:
                    if t.c[name].type.__class__.__name__ == "Date":
                        return date.fromisoformat(v[:10])
                    return datetime.fromisoformat(v)
                except ValueError:
                    return None
            return v

        data = [{c: conv(c, r[c]) for c in use} for r in rows]
        async with engine.begin() as conn:
            for i in range(0, len(data), CHUNK):
                await conn.execute(t.insert(), data[i:i + CHUNK])
            if "id" in cols:
                await conn.execute(text(
                    f"select setval(pg_get_serial_sequence('\"{t.name}\"', 'id'), coalesce((select max(id) from \"{t.name}\"), 1))"
                ))
        total += len(data)
        print(f"  {t.name}: {len(data)}")
    await engine.dispose()
    print(f"Tayyor. Jami {total} qator ko'chirildi. Endi .env ga DATABASE_URL ni qo'shing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
