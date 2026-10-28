# LongoUZ — Vercel + GitHub orqali joylash (qadamma-qadam)

Domen sotib olish shart emas: sayt `https://<loyiha>.vercel.app` manzilida ishlaydi.

## 1. Baza (Neon, bepul)
1. https://neon.tech → Google bilan kiring (iborgimxa6@gmail.com) → **Create project** → nom: `longouz`.
2. **Connection string** ni nusxalang (`postgresql://...neon.tech/neondb?sslmode=require`). Bu — `DATABASE_URL`.
3. Kompyuteringizda (loyiha papkasida, bir marta):
   ```
   pip install -r requirements.txt
   python cloud_setup.py "postgresql://...sizning-neon-manzilingiz..."
   ```
   Jadvallar yaratiladi va barcha tayyor savollar yuklanadi.

## 2. GitHub repo
1. https://github.com/new → nom: **Longouz** (Private tavsiya) → Create.
2. `deploy_longouz.bat` ni oching, kerak bo'lsa yuqoridagi `TARGET` papkani o'zgartiring (standart: `C:\Users\Usmon\Documents\LongoUZ`).
3. Yangi zipni (`longouz_v206.zip`) `deploy_longouz.bat` ustiga **sudrab tashlang**. Birinchi marta repo manzilini so'raydi (`https://github.com/<login>/Longouz.git`) va GitHub'ga kirishni (brauzer oynasi) so'raydi.
   - `.env`, `.git`, `*.db` GitHub'ga **yuborilmaydi** (kalitlar xavfsiz).

## 3. Vercel
1. https://vercel.com → **Continue with GitHub** → **Add New → Project** → `Longouz` repo → **Import**.
2. Framework: *Other*. Build sozlamalari `vercel.json` da tayyor — o'zgartirmang.
3. **Environment Variables** (Settings → Environment Variables) ga quyidagilarni kiriting:

| Nom | Qiymat |
|---|---|
| `DATABASE_URL` | Neon connection string |
| `WEB_SECRET_KEY` | tasodifiy 64 belgi (`python -c "import secrets;print(secrets.token_hex(32))"`) |
| `WEB_COOKIE_SECURE` | `true` |
| `ADMIN_PASSWORD` | admin panel paroli (kamida 12 belgi) |
| `ANTHROPIC_API_KEY` | Claude kaliti (repetitor, javob tekshiruvi, Studio) |
| `GEMINI_API_KEY` | ixtiyoriy zaxira |
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | 4-bo'limdan |
| `TURNSTILE_SITE_KEY`, `TURNSTILE_SECRET_KEY` | 5-bo'limdan |

   Keyin **Deployments → Redeploy**. Sayt manzili Vercel panelida ko'rinadi.
4. Bundan keyin: yangi zipni `deploy_longouz.bat` ga tashlasangiz — GitHub yangilanadi, Vercel 1–3 daqiqada o'zi qayta joylaydi.

> Kalitlarni admin paneldan ham kiritish mumkin: `/neo` → **AI holati / Sozlamalar** (bazada saqlanadi).

## 4. Google bilan kirish
1. https://console.cloud.google.com → loyiha yarating → **APIs & Services → OAuth consent screen**: *External*, ilova nomi `LongoUZ`, email. *Testing* holatida bo'lsa — **Test users** ga o'z Gmail manzillaringizni qo'shing (yoki **Publish app**).
2. **Credentials → Create credentials → OAuth client ID → Web application**.
3. **Authorized redirect URIs** ga aynan shu manzilni qo'shing:
   `https://<loyihangiz>.vercel.app/auth/google/callback`
   (lokal test uchun: `http://localhost:6060/auth/google/callback`)
4. Client ID va Secret ni Vercel o'zgaruvchilariga kiriting → Redeploy.

## 5. Cloudflare Turnstile (bot himoyasi)
1. https://dash.cloudflare.com → **Turnstile → Add widget**.
2. **Hostname** ga qo'shing: `<loyihangiz>.vercel.app` (va keyin domen olsangiz — uni ham).
3. Widget turi: *Managed*. **Site key** va **Secret key** ni Vercelga kiriting.
4. Kirish, ro'yxatdan o'tish va parolni tiklash formalari tekshiruvsiz yuborilmaydi.

## 6. Admin Studio
`https://<sayt>/neo` → **Studio (AI)**:
- **Hujjat → savollar**: PDF/Word/Excel/JSON/CSV/rasm/ZIP yuklang → "O'qish" → kerak bo'lsa "AI bilan aniqlashtirish" (skaner/rasm uchun "AI ko'rish") → savollarni tahrirlang (variant, javob, mavzu, tarif, chizma kengligi) → "Bazaga qo'shish". Vercelda bitta so'rov 4,5 MB dan oshmasligi kerak (katta PDF ni bo'lib yuklang yoki lokal ishga tushiring).
- **Mock yaratish**: fan + rejim + 1–3 variant; foydalanuvchilar test tanlashda "Mock testlar" ni ko'radi.
- **Baza holati**: fan/mavzu kesimida savol soni; "AI: +8 savol" tugmasi mavzuga yangi savol yaratadi (siz tekshirib qo'shasiz).
- **Claude yordamchi**: bazani tekshiradi, xato savollarni topadi va tuzatishni **taklif** qiladi — siz "Qo'llash" tugmasini bosmaguncha hech narsa o'zgarmaydi.
- **Tayyor bazani yangilash**: yangi versiyadan keyin bir marta bosing (yoki `python cloud_setup.py`).

## Muammolar
- *Google "redirect_uri_mismatch"*: 4-bo'limdagi URI aynan Vercel manzili bilan bir xilmi tekshiring.
- *Turnstile "invalid domain"*: hostname ro'yxatida Vercel manzili bormi.
- *Sayt sekin ochilsa*: birinchi so'rov (cold start) 2–4 soniya olishi mumkin.
- *Savollar chiqmasa*: `cloud_setup.py` ishlaganini va `DATABASE_URL` to'g'riligini tekshiring.
