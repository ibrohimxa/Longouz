# Tez boshlash

Windows: `ornatish_va_ishga_tushir.bat` ni ikki marta bosing (Linux/Mac: `./ornatish_va_ishga_tushir.sh`).
U `.venv` yaratadi, kutubxonalarni birma-bir o'rnatadi, tekshiradi va serverni ishga tushiradi (http://localhost:6060). `.env` ni `main.py` yoniga qo'ying.

# LongoUZ — admin va ma'lumotlar bazasi qo'llanmasi

## 1. O'rnatish
    pip install -r requirements.txt     # pypdf (PDF import) ham shu yerda
    python main.py                      # HTTP 6060 + HTTPS 6600

`.env` da `ADMIN_PASSWORD=` ni **albatta** to'ldiring. Admin manzili: `/neo` (foydalanuvchi: NEO).

## 2. Yangi savollarni qo'shish (ikki yo'l)
### a) Admin panel → "Import" (`/neo/import`)
PDF / JSON / CSV / TXT faylni tashlang. Dastur:
1. savollarni ajratadi (A-D variantlar, "Javoblar: 1-B ..." kalitlari);
2. fan va mavzuni o'zi aniqlaydi (TF-IDF o'xshashlik + **savoli kam mavzularga ustuvorlik**);
3. oldindan ko'rsatadi — mavzuni qo'lda o'zgartirish mumkin;
4. "Tasdiqlash" bosilganda bazaga yozadi (takrorlar o'tkazib yuboriladi) va fan foydalanuvchilariga bildirishnoma yuboradi.
Skanerlangan (rasm) PDF qo'llab-quvvatlanmaydi — matnli PDF kerak.

### b) Skript
    python import_questions.py FAYL --mode dtm|certificate|ielts|cefr [--subject auto|physics|...] [--topic "Mavzu"] [--dry-run] [--no-notify]
JSON formati: `[{"subject":"physics","topic":"Dinamika","question":"...","options":["A","B","C","D"],"correct_index":0,"explanation":"..."}]`
`topic` bo'lmasa avtomatik tanlanadi.

## 3. Doimiylik
Admin panelda qo'shilgan/tahrirlangan/o'chirilgan hamma narsa bazada saqlanadi — boshqa qurilma yoki qayta kirishda ham o'sha holat.
O'chirilgan savol bazadan olib tashlanadi, xatolar ro'yxatidan tozalanadi va qayta ishga tushganda
`static_questions.py` dan **qaytib kelmaydi** (`deleted_questions` jadvali). Bildirishnoma FAQAT yangi savol/mavzu qo'shilganda (katak orqali), import tasdiqlanganda, e'lon va support javobida ketadi.
Tahrirlash va o'chirish o'quvchilarga hech qanday bildirishnoma yubormaydi.

## 4. PostgreSQL'ga o'tish
    createdb longouz
    # .env:  DATABASE_URL=postgresql+asyncpg://user:parol@localhost:5432/longouz
    python migrate_sqlite_to_postgres.py --source longouz_web.db --target postgresql+asyncpg://user:parol@localhost:5432/longouz
    python main.py
Skript jadvallarni bog'liqlik tartibida ko'chiradi va ketma-ketliklarni (sequence) tiklaydi. `--force` — mavjud nishon jadvallarni tozalab qayta yozadi.

## 5. HTTPS va telefonda mikrofon (AI repetitor jonli suhbati)
Brauzer mikrofonni faqat **HTTPS** yoki `localhost` da beradi. Telefondan `http://192.168.x.x:6060` orqali kirsangiz mikrofon ISHLAMAYDI.
Yechim: `start_server_https.bat` ni ishga tushiring (yoki `HTTPS=1 python main.py`). Dastur o'zi `certs/` papkasida
o'z-o'zidan imzolangan sertifikat yaratadi. Telefonda "Xavfsiz emas" ogohlantirishi chiqadi — "Batafsil → Davom etish" ni bosing,
shundan keyin mikrofon ishlaydi. Haqiqiy domen bo'lsa — Cloudflare Tunnel yoki nginx + Let's Encrypt ishlating.
Nutq tanish Chrome/Edge/Safari'da internet orqali ishlaydi (brauzer xizmati); Firefox qo'llamaydi — u yerda savolni yozing.

## 6. AI holati (admin → "AI holati")
Claude, Gemini va ovoz (edge-tts) sozlanganmi va ishlayaptimi — "Hozir tekshirish" tugmasi haqiqiy so'rov yuboradi va aniq sababni ko'rsatadi
(kalit noto'g'ri / kredit tugagan / limit / tarmoq). AI ishlamasa, avval shu sahifaga qarang. Kalitlar `.env` da: `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`.
AI repetitor faqat Pro/Ultra tarifda: sinash uchun admin → Foydalanuvchilar → tarifni "Pro/Ultra" qiling.

## 7. Mavzular markazi va savol tahrirlagich
`/neo/topics` — mavzular ro'yxati (fan/rejim chiplari, qidiruv, har mavzu bitta qatorda; ochilganda statistika).
"Tahrirlash" → `/neo/topics/edit?...` 1-savoldan boshlanadi:
- **Ko'rish / Tahrirlash** — Tahrirlashda o'ng panel: *Matn* (savol, variantlar, to'g'ri javob, izoh, faol/yashirin, qo'shish/o'chirish),
  *Ko'rinish* (shu savolning matn o'lchami, qalinligi, joylashuvi, masofalari, surilishi, rangi), *Test oynasi* (butun mavzu uchun: soat ko'rinishi/joyi/o'lchami,
  sarlavha, progress, kenglik, tugmalar joyi).
- **Saqlash [N]** — N = haqiqatan o'zgartirilgan (yoki yangi/o'chirilgan) savollar soni; teginilmagan savollar sanalmaydi. O'zgargan savollar raqamlar qatorida
  sariq nuqta bilan, yangilari yashil, o'chiriladiganlari qizil ko'rinadi. Ctrl+S ham ishlaydi.
- Saqlangach o'zgarishlar DARHOL saytdagi test yechishda ko'rinadi, bildirishnoma YUBORILMAYDI.

## 8. Manzillar va portlar (eslab qolish oson)
- Barcha qurilmada port bir xil: **6060** (HTTP) va **6600** (HTTPS) — faqat 6 va 0 raqamlari (Chrome 6666 portini xavfsizlik uchun bloklagani sababli 6060 va 6600 tanlandi).
- Kompyuterda: `http://localhost:6060`. Telefon/planshet (bir xil Wi-Fi): `http://<kompyuter-IP>:6060`; mikrofon uchun `https://<kompyuter-IP>:6600`.
- Portlarni o'zgartirish: `.env` yoki muhitda `SERVER_PORT=...`, `HTTPS_PORT=...`; HTTPS'ni o'chirish: `HTTPS=0`.
- **Boshqa Wi-Fi yoki mobil internet** (kompyuter bilan bir tarmoqda bo'lmagan qurilmalar): `start_online.bat` (yoki `TUNNEL=1 python main.py`) —
  Cloudflare tunnel (`cloudflared` o'rnatilgan bo'lishi kerak) ommaviy HTTPS manzil beradi, u istalgan tarmoqda ishlaydi va mikrofon ham ishlaydi.
  Manzil har ishga tushirishda yangi bo'ladi; doimiy manzil uchun o'z domeningizni Cloudflare Tunnel'ga ulang.
- `.env` dagi `SITE_BASE_URL` sertifikat QR-kodi va Google kirishi uchun ishlatiladi: uni tunnel yoki domen manziliga qo'ying (IP o'zgarib turadi).
