"""
LongoUZ — savollarni fayldan (JSON / CSV / TXT / PDF) bazaga yuklash skripti.

Misollar:
  python import_questions.py yangi.pdf --mode dtm --subject auto --dry-run
  python import_questions.py yangi.json --mode certificate --subject math
  python import_questions.py test.pdf --mode dtm --subject chemistry --topic "Eritmalar - massa ulushi"

--subject auto : fan va mavzu savol matniga qarab, savoli KAM mavzularga ustuvorlik bilan aniqlanadi.
--dry-run      : hech narsa yozmasdan faqat nima bo'lishini ko'rsatadi.
--no-notify    : foydalanuvchilarga bildirishnoma yubormaydi.
JSON format: [{"question": "...", "options": ["a","b","c","d"], "correct_index": 1, "explanation": "...", "topic": "ixtiyoriy"}]
"""
import argparse
import asyncio
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import database as db  # noqa: E402
import question_import as qi  # noqa: E402


async def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--mode", required=True, choices=["dtm", "certificate", "ielts", "cefr"])
    ap.add_argument("--subject", default="auto", help="fan kodi yoki auto")
    ap.add_argument("--topic", default="", help="barcha savollar uchun bitta mavzu (ixtiyoriy)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-notify", action="store_true")
    args = ap.parse_args()

    if args.subject != "auto" and args.subject not in db.SUBJECT_CODES:
        print("Noma'lum fan. Mumkin:", ", ".join(sorted(db.SUBJECT_CODES)), "yoki auto")
        return 2
    with open(args.file, "rb") as fh:
        items, warn = qi.parse_upload(os.path.basename(args.file), fh.read())
    if warn:
        print("Ogohlantirish:", warn)
    if not items:
        print("Hech qanday savol topilmadi.")
        return 1

    await db.init_web_db()
    matcher = await qi.build_matcher(args.mode, None if args.subject == "auto" else [args.subject])
    qi.auto_assign(items, matcher, args.subject, args.topic or None)

    ready = [it for it in items if it["correct_index"] is not None and it.get("subject")]
    no_answer = len(items) - len([it for it in items if it["correct_index"] is not None])
    print(f"Topildi: {len(items)} ta savol; to'g'ri javobi yo'q: {no_answer} ta (ular o'tkazib yuboriladi).")
    dist = collections.Counter((it["subject"], it["topic"]) for it in ready)
    for (s, t), n in dist.most_common():
        print(f"  +{n:3d}  {db.SUBJECT_NAMES.get(s, s)} / {t}")
    if args.dry_run:
        print("--dry-run: bazaga yozilmadi.")
        return 0

    for it in ready:
        it["mode"] = args.mode
    result = await db.admin_bulk_create_questions(ready, mock_test="Import")
    print(f"Qo'shildi: {len(result['added'])}, takror/o'tkazib yuborildi: {result['skipped']}")

    if not args.no_notify and result["added"]:
        groups = collections.defaultdict(list)
        for it in result["added"]:
            groups[it["subject"]].append(it["topic"])
        for subject, topics in groups.items():
            n = await db.notify_question_change(subject, args.mode, "questions_added", topics, len(topics))
            print(f"  Bildirishnoma: {db.SUBJECT_NAMES.get(subject, subject)} — {n} foydalanuvchi")
    await db.log_admin_action("script", "question_import", f"{args.file}: +{len(result['added'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
