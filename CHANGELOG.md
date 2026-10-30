# LongoUZ — versiyalar tarixi

Har yuborilgan zip: `longouz_v<N>.zip`, versiya raqami `VERSION` faylida.

## v222 — xavfsizlik: koddagi admin paroli olib tashlandi
- `admin_auth.py`: ADMIN_PASSWORD berilmasa endi admin panel yopiq (avval ochiq GitHub reposida ko'rinadigan standart parol ishlardi).
- Vercel Environment Variables'ga kalitlar qo'shildi (WEB_SECRET_KEY, Google, Turnstile, WEB_COOKIE_SECURE, yangi ADMIN_PASSWORD).
- Oxirgi Vercel xatosi ("functions va builds birga ishlatib bo'lmaydi") v221 dagi `vercel.json` bilan tuzatiladi.

## v221 — Vercel konfiguratsiyasi va kalitlar ajratildi
- `vercel.json`: `builds` (`main.py` + `@vercel/python`) va `routes` (`/(.*)` → `main.py`) ko'rinishiga o'tkazildi; statik fayllarni ham FastAPI beradi (kesh sarlavhalari bilan).
- `.vercelignore` qo'shildi: `.env`, `.web_secret_key.local`, `*.db`, sertifikatlar va .bat fayllar Vercel'ga yuklanmaydi.
- `vercel_env_namuna.txt`: Vercel Environment Variables uchun kerakli nomlar (qiymatsiz).
- Baza manzili `DATABASE_URL`, `POSTGRES_URL` yoki `NEON_DATABASE_URL` dan olinadi.

## v220 — kabinetdagi tog'cha qaytarildi va yaxshilandi
- Kabinet (dashboard) yuqori kartasidagi kichik tog' rasmi joyiga qaytdi; kun/tun rejimi almashganda quyosh va oy almashadi.
- Kunduzgi rejim endi har doim yorug' kun: moviy osmon, quyosh (o'rni soatga qarab biroz siljiydi), oy va yulduzlar yo'q; kartaning chap qismi ham moviy (oldin to'q ko'k qolardi).
- Tunda shahar chiroqlari yonadi, kunduzi o'chadi; binolar, daraxtlar va "LONGO" yozuvi ikkala rejimda ham ko'rinadi.
- Planshetda oy sarlavha ustiga tushmaydi.
- Tema almashish animatsiyasi 2.3 s → 1.3 s (sahifa qotmasligi uchun).
- Bosh sahifa v219 dagidek fonsiz qoldi.

## v219 — oddiy fon, tezroq sayt
- **Bosh sahifa**: tog' manzarasi, quyosh va oy (tushib-chiqish animatsiyasi) butunlay olib tashlandi. Tungi rejim — to'q yashil-qora, kunduzgi — oq; tema almashganda faqat ranglar 0.35 soniyada yumshoq o'zgaradi. Barcha elementlar joyida qoldi.
- **Kabinet (dashboard)**: hero'dagi tog'/quyosh/oy va har soniyada qayta chiziladigan skript olib tashlandi — oddiy yashil karta.
- **Tezlik**: 3 soniyalik kirish (intro) ekrani olib tashlandi (bosh sahifa, kirish, ro'yxatdan o'tish darhol ochiladi); sahifalar gzip bilan siqiladi (bosh sahifa ~50 KB → ~11 KB); statik fayllar keshlanadi; og'ir blur (backdrop-filter) va telefonda doimiy animatsiyalar o'chirildi; Vercel'da fon yuklash bir instansni 12 soniyadan ortiq band qilmaydi.

## v224 — doimiy baza, admin, Pro qulfi, sayt tahlili, chizmali savollar
- **Login qayta so'ralishi tuzatildi**: foydalanuvchilar endi doimiy Postgres bazada (Supabase, Frankfurt) saqlanadi; Vercel serveri ham Frankfurt'ga (fra1) ko'chirildi. Yaroqsiz sessiya cookie'si avtomatik tozalanadi.
- **Header**: kichik "Kirish" / "Ro'yxatdan o'tish"; kirgan foydalanuvchiga faqat "Kabinet"; sarlavha foni to'liq yopiq.
- **Profil**: yuqoridagi avatar va ism bosilsa — Profil va sozlamalar.
- **AI repetitor**: bepul foydalanuvchi bossa sahifadan chiqmasdan Pro/Ultra tanlash oynasi (Bekor qilish / Sotib olish).
- **Yordam**: xabar turi (Savol / Shikoyat / Texnik xato / To'lov / Taklif) — admin "Xabarlar" bo'limiga boradi.
- **Admin**: login `neo` (katta-kichik harf farqsiz), parol faqat Vercel env'da; koddagi eski parol satrlari olib tashlandi. Yangi **Sayt tahlili** (`/neo/insights`): kunlik tashrifchilar, eng ko'p ochilgan sahifalar, ro'yxatdan o'tish/testlar, ochiq shikoyatlar va "Claude bilan tahlil qilish". Studio: avval mavzu nomi, keyin fayl yashigi.
- **Savollar**: 150+ yangi chizmali savol (richag, gidravlik press, qiya tekislik, elektr zanjirlari, v–t grafigi, Pifagor, yuzalar, parabola/to'g'ri chiziq grafiklari, diagrammalar, koordinatalar, aylana burchaklari, atom tuzilishi, Pennet katagi) — javoblar kod bilan hisoblangan. `CONTENT_VERSION=v224q`.
- `/api/health` — baza holatini tekshirish.

## v218 — katta ekranlar, mobil tuzatishlar, Turnstile zaxirasi, kalitlar sahifasi
- **Moslashuvchanlik**: 2K/4K/5K ekranlarda sayt zoom orqali butun ekranni to'ldiradi (max-width cheklovlari olib tashlandi); suzuvchi boyqush tugmasi telefonda skroll paytida yashirinadi va pastki kontentni yopmaydi; bosh sahifadagi osmon/oy telefonda sakramaydi (manzil satri o'zgarishi e'tiborga olinmaydi), hero matni planshetda markazlandi.
- **Fan nomi**: "Ona tili va adabiyot" hamma joyda bir xil.
- **Cloudflare Turnstile**: 9 soniyada yuklanmasa avtomatik zaxira rejimi (IP bo'yicha cheklov bilan), xato kodlari aniq; admin panelda `TURNSTILE_MODE` (o'chirish) va zaxira sozlamasi.
- **Ro'yxatdan o'tish → Pro**: mavjud email + to'g'ri parol bilan sotib olishda tarif yangilanadi va akkauntga kiriladi; sotib olish oynasida "Google bilan davom etish".
- **Admin → Kalitlar** (`/neo/keys`): Claude, Gemini, Turnstile, Google kalitlari saqlashdan oldin format va jonli tekshiriladi, bazada shifrlanadi (Fernet), maskalangan ko'rsatiladi.
- **GitHub/Vercel xavfsizligi**: `deploy_longouz.bat` `.env` ni indeksdan chiqaradi va kalit qoldig'i topilsa yuborishni to'xtatadi; `.gitignore` kengaytirildi.
- **Savollar**: tarix (sanalar, voqealar), ingliz tili (noto'g'ri fe'llar, lug'at, sinonim/antonim, sifat darajalari, predloglar), rus tili (urg'usiz unlilar, ъ/ь, tuslanish), ona tili (imlo, sinonim/antonim) bo'yicha jadvaldan tuzilgan yangi savollar; `CONTENT_VERSION=v217q`.

## v215 — ro'yxatdan o'tish oqimi, shikoyatlar, kalkulyator, Vercel mustahkamlandi
- **Ro'yxatdan o'tish/kirish**: bosh sahifada fan tanlansa (`?subject=` + `lz_subject` cookie) ro'yxatdan o'tgach fan va daraja QAYTA so'ralmaydi — to'g'ri panelga o'tadi. "Bepul/Boshlash" fansiz bosilsa — faqat fan so'raladi (daraja olib tashlandi). Pro/Ultra sotib olgach test boshlashda akkaunt qayta so'ralmaydi (redirect sarlavhasi xatosi tuzatildi, Vercel'da foydalanuvchi keshi o'chirildi).
- **Google**: "Google bilan davom etish" — akkaunt bor bo'lsa kiradi, yo'q bo'lsa ro'yxatdan o'tkazadi (login va register bir xil). Oddiy ro'yxatdan o'tishda email mavjud va parol to'g'ri bo'lsa ham kiradi.
- **Cloudflare Turnstile**: skript qayta-qayta yuklanadi, render qayta uriniladi, xato kodlari (110200 = domen ruxsat etilmagan) aniq ko'rsatiladi, CSP `child-src`/`worker-src` qo'shildi, token bo'lmasa yuborish bloklanadi.
- **Mavzular chiqmasligi (Vercel)**: bank bo'laklab, davom ettiriladigan tarzda yuklanadi (`/api/seed-step`, fon vazifa, sahifalardan ping, build paytida `cloud_setup.py`); mavzu ro'yxati bo'sh bo'lsa "tayyorlanmoqda" xabari va avtomatik qayta urinish.
- **Vercel**: `requirements.txt` ga `aiosqlite`, `vercel.json` build bosqichi mustahkamlandi.
- **AI kalitlari**: `ai_key_defaults.py` (qiymatlar qo'sh tirnoqda), tartib: env/.env → admin panel → `ai_key_defaults.py`; tirnoq, BOM va "KEY=" qo'shimchasi avtomatik tozalanadi.
- **Shikoyat**: test paytida tepada "Shikoyat" tugmasi → o'ng yon panel (10 ta sabab + izoh). Admin panelda yangi bo'lim `/neo/reports`: statistika, filtrlar, Claude tahlili (hukm, ishonch, tuzatish taklifi), tuzatishni tasdiqlash, rad etish, savolni yashirish, avtomatik rejim (ishonch ≥ chegara bo'lsa o'zi tuzatadi), shikoyat qilgan foydalanuvchiga xabar.
- **Kalkulyator** (matematika, fizika, kimyo, biologiya; tarix va tillarda yo'q): xavfsiz ifoda yechuvchi (`eval`siz), DEG/RAD, o'zgaruvchilar, tenglama yechish; matematika — formulalar yechuvchi, kvadrat tenglama va tizim, kombinatorika, foiz; fizika — formulalar, doimiylar, birlik o'zgartirgich; kimyo — molyar massa (maktab/aniq massalar), tenglashtirgich, mol hisobi; biologiya — DNK→iRNK→oqsil, Chargaff, Xardi–Vaynberg, Mendel.
- **Ochiq javob uchun belgilar klaviaturasi** (tarix, ona tili, ingliz, rus tillarida chiqmaydi): matematika (², √, π, ±, ≤…), fizika (10ⁿ, birliklar, yunon harflari), kimyo (indekslar, zaryadlar, →, ⇌), biologiya (genotip belgilari). Javob tekshiruvi `^`, `sqrt`, `->` yozuvlarini ham tushunadi.
- **Bank**: matematika, fizika, kimyo, biologiya va ingliz tili uchun kod orqali HISOBLANADIGAN ~1 100 ta yangi savol (`content/gen_v215.py`; to'g'ri javob xato bo'lishi mumkin emas), mavjud mavzularga qo'shildi. Jami ≈ 5 700 savol.
- **Telefon moslashuvi**: test oynasida savollar paneli gorizontal siljiydi, boyqush tugmasi kalkulyator ochilganda yashiriladi, kalkulyator/belgilar klaviaturasi kichik ekranga moslandi, ochiq javob maslahati fanga mos; admin pastki paneli gorizontal siljiydi va yorliqlar sig'adi; shikoyatlar sahifasi filtrlari tuzatildi.
- `CONTENT_VERSION = v215`: yangi savollar avtomatik yuklanadi.
- **DTM blok mock** (`/dtm-blok`, Pro/Ultra): haqiqiy DTM tuzilmasi — 90 savol / 180 daqiqa: majburiy 3 fan (ona tili, matematika, tarix; 30 savol, ×1,1), 1-ixtisoslik (30 savol, ×3,1), 2-ixtisoslik (30 savol, ×2,1); maksimum 189 ball, natija bloklar bo'yicha.
- **AI adaptiv test**: savol qiyinligi foydalanuvchi javobiga qarab o'zgaradi (to'g'ri → qiyinroq, xato → osonroq); mavzu sahifasida "AI adaptiv test" tugmasi.
- **Chuqur tahlil va prognoz** (`/analytics`): fan va mavzu statistikasi, kuchsiz/kuchli mavzular, haftalik progress, oxirgi natijalarga ko'ra DTM ball prognozi (189 dan).
- **Imtihon yo'riqnomasi** (`/guide`): DTM va Milliy sertifikat tuzilmasi, vaqt, ball, sinflar bo'yicha o'rganiladigan mavzular.
- **Mavzu kvotasi**: har mavzuda Bepul 25, Pro ~60 (2,4×), Ultra ~125 (5×) savol; urinishdagi savollar soni shunga mos (25/60/125). Savol kam mavzularda ulush bo'yicha taqsimlanadi (45%/75%/100%), shunda pullik tariflarda ham qo'shimcha savol qoladi.
- **Admin → Savol banki** (`/neo/bank`): har mavzu uchun Bepul/Pro/Ultra savollar soni va 125 gacha kamchilik.
- `CONTENT_VERSION = v215q`.

## v206 — Vercel + GitHub, Studio, kengaytirilgan bank
- **Vercel**: `api/index.py`, `vercel.json`, Neon/Postgres (NullPool), seans va avtosaqlash bazada, chizmalar bazada (`qfigures`), lazy init. Domen sotib olmasdan `*.vercel.app` da ishlaydi. `cloud_setup.py` — bazani bir marta tayyorlaydi. Joylash: `deploy_longouz.bat` (zipni ustiga tashlash → GitHub → Vercel avtomatik).
- **Google kirish** tuzatildi (sayt manzili avtomatik aniqlanadi), **Cloudflare Turnstile** kirish/ro'yxatdan o'tish/parol tiklashda ishlaydi; kalitlar admin panelda saqlanadi.
- **AI repetitor**: Claude birinchi, fan bo'yicha uslub va imtihon formatlari (`SUBJECT_GUIDE`), vaqt chegarasi va zaxira.
- **Ochiq javob tekshiruvi** (`answer_check.py`): "2 nC" / "2" / "2·10⁻⁹ C", o'nli/kasr, birlik va ortiqcha so'zlar; qoida yetmasa Claude hakam sifatida (faqat mazmunan to'g'ri bo'lsa qabul qiladi).
- **Admin Studio** (`/neo/studio`): hujjat → savollar (PDF/Word/Excel/JSON/CSV/rasm/ZIP; chizmalar saqlanadi, kenglik sozlanadi; AI bilan aniqlashtirish va skaner uchun AI ko'rish), mock yaratish (1–3 variant, o'zaro takrorlanmaydi; foydalanuvchida "Mock testlar" bo'limi), baza holati (fan/mavzu/tarif/tur/chizma kesimi, kam savolli mavzular), mavzuga AI savol yaratish, Claude yordamchi (bazani o'qiydi, tuzatish/o'chirish/qo'shishni TAKLIF qiladi, admin tasdiqlaydi), o'zgarishlar tarixi.
- **Bank**: biologiya 64 mavzu (590 savol), matematika 54 (404 + 75 chizmali), kimyo 63 (632), ona tili 60 (543), ingliz tili 40 (244; DTM), rus tili 30 (180; DTM va sertifikat). Pro jami ≥ 50 mavzu (biologiya, kimyo, matematika, ona tili, fizika), tarix 45/85/150.
- **Bazani yangilash**: versiya o'zgarganda tayyor bankdagi mavjud savollarning mavzusi/tarifi/javobi/chizmasi yangilanadi, paketdan chiqarilganlari nofaol bo'ladi (tarixdagi noto'g'ri biriktirilgan mavzular shu bilan tuzaladi).

## v204 — fizika, ona tili va adabiyot, chizmali savollar
- Fizika (sertifikat va DTM): 73 mavzu (mexanika, termodinamika, elektr-magnetizm, tebranish-to'lqin, optika, kvant va yadro), 677 tayyor savol (yopiq, ochiq hisoblash, moslashtirish). Sertifikat: 45 savol (№1–32 yopiq +1, №33–35 moslashtirish +2, №36–45 ochiq +3; xom ball 68 → 100), 150 daqiqa. DTM: 30 savol / 60 daqiqa.
- Ona tili va adabiyot (sertifikat va DTM): 55 mavzu (5–11-sinf: til bo'limlari, imlo, uslubiyat, adabiyot tarixi, asarlar tahlili), 508 savol. Sertifikat 45 savol / 90 daqiqa.
- Darajalar: A+ 86–100, A 76–85.9, B 66–75.9, C 56–65.9, D 46–55.9; imtiyozlar natija sahifasida.
- Ochiq javoblar raqamli tekshiriladi (vergul/nuqta, 10ⁿ).
- Chizmalar: fizika (grafiklar, sxemalar, qiya tekislik, linza, elektr zanjiri...), matematika (geometriya, grafiklar, diagramma, Venn; 9 mavzu / 75 savol), biologiya (hujayra, DNK, yurak, neyron, Pennet, mitoz), kimyo (atom modeli, spirt).
- Mavzu bo'yicha tariflar: Free / Pro / Ultra; Free mavzularda ham ochiq va moslashtirish savollari bor.

## v203 — kimyo (DTM va sertifikat)
- Kimyo: 8–11-sinf bo'yicha 47 mavzu va 517 tayyor savol (mol va stexiometriya, eritmalar, elektrolitlar va gidroliz, nometallar, metallar, organik kimya: alkanlardan aminokislota va polimerlargacha, reaksiya tezligi, elektroliz, hisoblash masalalari). Har mavzuda 11 savol: 3 oson, 5 o'rta (1 moslashtirish), 3 qiyin (1 ochiq hisoblash javobi).
- DTM (kimyo): 30 savol / 60 daqiqa, 1-fan 3.1 ball (93), 2-fan 2.1 ball (63); 9 oson / 15 o'rta / 6 qiyin; 24 yopiq + 3 moslashtirish + 3 ochiq. Quiz sahifasida 1-/2-fan tanlovi kimyo uchun ham ko'rinadi.
- Sertifikat rejimi: kimyo savollari umumiy sertifikat rejimida ham mavjud.
- Mavjud bazalarda yangi savollar avtomatik qo'shiladi (eskilari o'chmaydi).

## v202 — milliy sertifikat uslubidagi tarix va biologiya (DTM)
- Tarix: 6–11-sinf bo'yicha 150 mavzu va 1224 ta tayyor savol (yopiq, ochiq, moslashtirish, Amir Temur jang tartiblari kabi chizmali savollar). Sinf tablari, Bepul 45 / Pro 85 / Ultra 150 mavzu, qulf va tarifga o'tish oynasi, har 10 mavzudan keyin xatolar ustida ochiq "nazorat" testi.
- Milliy sertifikat: 45 savol / 90 daqiqa / 100 ball (siyosiy 29, ijtimoiy 7, moslashtirish 3, madaniyat 6; savol bali 1.3 / 2.2 / 3.2); daraja A+ ≥70, A 65, B+ 60, B 55, C+ 50, C 46; sertifikat egasiga majburiy blok uchun 11 ball.
- DTM tarix: majburiy 10 × 1.1 = 11 (15 daq) + mutaxassislik 30 × 3.1 = 93 (45 daq).
- Biologiya (DTM): 6–11-sinf bo'yicha 31 mavzu va 339 savol (botanika, zoologiya, odam, sitologiya, genetika, geoxronologiya, formulali masalalar); 1-fan 30 × 3.1 = 93, 2-fan 30 × 2.1 = 63; 9 oson / 15 o'rta / 6 qiyin, 24 yopiq + 3 moslashtirish + 3 ochiq.
- Ochiq (yozma) javoblar serverda tekshiriladi; natija sahifasida blok/qiyinlik bo'yicha tahlil, savollar paneli, ko'rib chiqishda ochiq javoblar.
- Kunduzgi rejimda bosh sahifa footeri ko'rinmay qolgan xato tuzatildi.

## v201 — savollar banki to'liq tozalandi
- Barcha tayyor savollar, mavzular, hisoblanadigan generatorlar ("Mashq: ...") va audit tuzatishlari olib tashlandi. Baza bo'sh boshlanadi.
- Mavjud bazalarda ham bir martalik avtomatik tozalash (savollar, mavzular, xatolar ro'yxati, mavzu progressi); foydalanuvchilar, tarif va sozlamalar saqlanadi.
- Savollar endi FAQAT admin paneldan: "Import (PDF / fayl)" yoki "Yangi savol".

## v200 — baholash, Google, admin, generatorlar (qo'shimcha)
- Baholash: DTM — asosiy fan 30 savol × 3.1 = maks. 93 ball; sertifikat — 100 ballik shkala va milliy daraja (A+ ≥70, A 65, B+ 60, B 55, C+ 50, C 46; 46 dan past — daraja yo'q).
- Reyting: foydalanuvchining jami to'g'ri javoblari yig'indisi bo'yicha.
- Dashboard: tong/kech quyosh ufqda yorug'lik va nurlar bilan, quyosh/oy yumshoq animatsiya.
- Google kirish: aniq xato xabarlari (/login, /register), redirect URI so'rov manzilidan olinadi, state imzolangan. Admin: "Tizim holati"da Google va Cloudflare Turnstile'ni haqiqiy tekshirish tugmasi.
- Admin savollar: to'g'ri javobni bitta bosish bilan belgilash, savollarni boshqa fan/mavzuga ko'chirish, "Tekshiruv" sahifasi.
- Hisoblanadigan savollar generatori (matematika, fizika, kimyo, ingliz tili — ~140 ta generator): javob formula bilan hisoblanadi; mavzularga "Mashq: ..." mavzulari qo'shildi.
- Tarif bo'yicha savollar soni: Bepul 20 / Pro 35 / Ultra 105 — mavzudagi tayyor savollar yetmasa generator va yaqin mavzulardan to'ldiriladi.
- Katta monitorlar (2K/4K) uchun shrift masshtabi; sertifikat rejimi tavsifi yangilandi.

## v200 — savollar bazasi auditi
- Barcha fanlar (biologiya, matematika, fizika, tarix, kimyo, ingliz, rus, ona tili) bo'yicha 318 ta savol tuzatildi: noto'g'ri javob kalitlari, bir nechta to'g'ri variantli savollar, bema'ni variantlar (masalan, "milodiy 22-asr"), 100% dan oshgan massa ulushlari, noto'g'ri fizik qiymatlar.
- 39 ta noaniq yoki tekshirib bo'lmaydigan savol olib tashlandi.
- Lotin/kirill harflari aralashgan so'zlar, "#", "e+14" kabi belgilar tozalandi.
- Test natijasi: yechilgan / xato / qoldirilgan savollar soni aniq ko'rsatiladi.
- Tuzatishlar mavjud bazaga ham bir martalik avtomatik qo'llanadi (`bank_audit_v200_r1`).

## v137
- Sertifikat kartalarida siz yuborgan qiz va yigit fotosi o'zgartirishsiz joylandi (faqat ikkiga ajratildi).

## v136
- Sertifikat kartalaridagi odam rasmlari tiniqlashtirildi (yigit rasmi yuz tiklash modeli bilan qayta ishlandi, qiz rasmi kattalashtirilib o'tkirlashtirildi).

## v135
- Sertifikat bo'limi: chizma juftlik olib tashlandi; ikki karta qaytarildi, ularda sizning maketingizdagi haqiqiy odam fotolari (qiz va yigit) turadi.
- Telefonda bosh sahifa sarlavhasi sig'dirildi (320–390 px).

## v134
- Sertifikat bo'limi: yigit va qiz bitta rasmda (kulib turgan, o'zbekcha doppi bilan, sertifikat ushlab), alohida portretlar olib tashlandi.
- Dashboardda rejim tugmasi: quyosh/oy almashuvi bilan birga butun ekran (fon, tog', kartalar) ~1 s ichida asta qorong'ilashadi yoki yorishadi; boshqa sahifalarda ham silliq o'tish.
- Telefonda bo'limlar pastki panelga (4 ta asosiy + "Yana" tugmasi, ochilganda yuqoriga chiqadigan darcha) ko'chdi; planshet/noutbukda yuqori panel + "3 chiziq" saqlandi.

## v133
- Tarif sotib olish oynasi referens rasm bo'yicha qayta qurildi (chap premium panel, o'ng "To'lov ma'lumotlari", UzCard kartasi, ko'k tugma). Bosh sahifa (mehmon) va /upgrade (a'zo) uchun bitta umumiy komponent; tugma "Tarifni tasdiqlash" — ro'yxatdan o'tish emas.
- Kirish va ro'yxatdan o'tish sahifalari referens rasmlar bo'yicha qayta qurildi (3 ustunli ro'yxat sahifasi, ikki bo'lakli kirish kartasi, yashil mavzu, kunduzgi rejim, 320–1920 px).
- Cloudflare Turnstile: kirish, ro'yxat, tarif oynasi va /upgrade da; serverda tekshiruv ham /upgrade ga qo'shildi; sahifada "Cloudflare Turnstile bilan himoyalangan" yozuvi.
- Yagona LongoUZ belgisi (3D boyqush + "Longo"+"UZ") barcha sahifalar, yon panel, admin, footer, favicon, chat tugmasida.

## v132
- Kunduzgi rejimda yon paneldagi "Pro'ga o'ting" kartasi o'qiladigan qilindi.

## v131
- Kontrast tuzatildi (kunduz va tun): xira yashil/to'q sariq/ko'k matnlar to'qroq qilindi, tugmalardagi matn rangi aniq ko'rinadi, bildirishnoma va "o'chirish" tugmalari, faol yorliqlar, tarif va balans tugmalari. Kunduzgi rejimda asosiy va ikkinchi darajali matn ranglari to'qlashtirildi.

## v130
(Eslatma: loyiha 2 oydan beri, jami 130 martaga yaqin tahrirlangan — versiya raqami 130.)
- Bosh sahifa: laptop burilgan holatda, atrofida 4 ta kichik so'z (tepa, pastki, chap, o'ng) sekin qimirlab qaytadi; kartalar ekranni yopmaydi.
- Bosh sahifa orqa foni — qadalgan (scroll qilganda joyida turadigan) real tog' manzarasi (qatlamli tizma, qor, nur sochuvchi yo'l, bayroq). Tema almashganda oy tog' ortiga tushadi, quyosh tong rangi bilan chiqadi va sayt ranglari kunduz/tunga o'tadi. Pastdagi tog' olib tashlandi.
- Haqiqiy odam rasmlari (`static/people/`, MUI docs, MIT) — hero va sertifikat kartalarida.
- Quyosh/oy surilma tugmasi (dumaloq surgich) — sayt headeri va dashboard tepasida.
- Dashboard: tog' rasmi asl holida; tema almashganda osmon, quyosh va oy ~1 soniyada almashadi.
- Telefon/planshet: yon panel yuqori panelga aylandi, sig'magan bo'limlar "3 chiziq" ortidagi darchaga yig'iladi; KPI, banner va tugmalar kichraytirildi.
- Reklama: haqiqiy ekranlar (dashboard, test, AI repetitor, kimyo, fizika), sichqoncha va ovoz to'lqini.

## v102
- Reklama (laptop ichida) endi haqiqiy ilova ekranlari: asosiy dashboard, test yechish, AI repetitor, kimyo va fizika. Sichqoncha AI repetitorga boradi, bosadi, ichiga kiradi; yozmasdan gaplashadi — ovoz to'lqinlari gapirganda ko'tarilib-pasayadi.
- Kartalar laptop ekranini yopmaydi; fan kartalaridagi pastki yozuvlar olib tashlandi; sertifikat bo'limidagi kartalar matn bilan to'qnashmaydi.
- Tog' bloki ochiq, osmonli fon bo'ldi. Tema almashganda oy tog' ortiga tushadi, quyosh asta chiqadi (tong rangi bilan) va teskarisi; dashboard'da ham xuddi shunday.
- Odam rasmlari uchun `static/people/` papkasi (rasm bo'lmasa, chizilgan portretlar ko'rinadi).
- `.env` zip ichiga qo'shildi (ADMIN_PASSWORD bo'sh).

## v101
(Eslatma: loyiha ~2 oydan beri ishlab chiqilgan, jami 100+ marta yangilangan — shu sababli raqam 101.)
- Bosh sahifa to'liq qayta qurildi (kunduz va tun rejimi): hero'da laptop ichida 4 ta aylanuvchi jonli reklama — test yechish, AI bilan IELTS suhbat, kimyo (formula + Mendeleyev jadvali, savol chapga siljib almashadi), fizika formulalari. "Qisqacha ko'ring" katta demo oynasini ochadi.
- Yangi bo'limlar: 3 qadam, AI yordamchisi, fanlar (rangli ikonkalar), sertifikat namunalari, tariflar, tog'li yakuniy blok (ortiqcha "Bepul boshlash" tugmasi olib tashlandi).
- Dashboard (kunduzgi rejim): quyosh tog' orqasidan asta chiqadi; osmon rangi va quyosh o'rni mahalliy soatga qarab o'zgaradi (sinash: ?hour=13.5).
- Admin import: bir nechta fayl, ZIP, PDF, Word (.docx), Excel (.xlsx), JSON/CSV/TXT/HTML; takrorlar bazadagi va fayllar orasidagilar bilan solishtiriladi (bittasi olinadi), hisobotda fayl nomi, sana va savol raqami; filtr, qidiruv, CSV hisobot.
- Savollar: Nashr / Private (qoralama) holati, ommaviy amallar (nashr, private, o'chirish), manba fayl bo'yicha filtr va fayl bo'yicha ommaviy boshqaruv.
- CSV/Excel importdagi kichik harfli A/B/C/D ustunlari xatosi tuzatildi.
- .env.example qo'shildi (bo'sh qiymatlar bilan).

## v71
- Admin: foydalanuvchilar sahifasi — tarif filtri, testlar soni va o'rtacha natija, CSV eksport (formula-injection himoyali), foydalanuvchi batafsil kartochkasi (oxirgi 30 test, tarif o'zgartirish).
- Admin dashboard: zaif mavzular rang darajalari to'g'rilandi; admin-dash.css qo'shimchalari.
- Xavfsizlik: /docs va /openapi.json sukut bo'yicha o'chirildi (EXPOSE_API_DOCS=true bilan yoqiladi); sarlavhalar, cookie bayroqlari, rate-limit va admin endpointlar jonli tekshirildi.

## v70
- O'rnatish skripti (`ornatish_va_ishga_tushir.bat`), `greenlet` tuzatildi.
- Google bilan kirish va Cloudflare Turnstile (kirish + ro'yxatdan o'tish) ulandi.
- Portlar: HTTP 6060, HTTPS 6600 (Chrome 6666 ni bloklaydi).
- Gemini asosiy AI repetitor, Claude zaxira; IELTS examiner uslubida qisqa gapirish.
- Dashboard rasmdagidek qayta yozildi.

## v1–v69
- Oldingi yuborilgan versiyalar (admin, savollar bazasi, formulalar paneli va h.k.).

## v200 (avval v138) — eski savollar banki qayta tiklandi (bir martalik)
- Savollar banki butunlay tozalandi; static_questions bilan avtomatik sinxronlash o'chirildi — savollar faqat admin orqali.
- Admin: yangi mavzu yaratish, "Test qo'shish" (bittalab / chizmali / JSON / fayl), savollar ro'yxati (o'chirish, tahrirlash, nashr/yopiq), mavzular sahifasi paginatsiyasi.
- Chizmalar: Dekart koordinatalari, funksiya grafiklari, geometrik shakllar, rasm, SVG — testda, natijada va tahrirlagichda.
- PDF/Word/ZIP importida chizmalar savol bilan birga olinadi (PyMuPDF).
- Test ko'rinishida tahrirlash: matn joyida, chizma paneli, o'zgargan savollar raqamlari, "Saved ✓" xabari.

## v205 — 2026-10-19

### Yangi
- **Matematika** to'liq qo'shildi: 8-9-10-11-sinf, 27 nazariy mavzu + 9 chizmali mavzu = 36 mavzu, 301 ta savol
  - `content/math_a.py` — 8-sinf (M8.1–M8.8) va 9-sinf (M9.1–M9.6)
  - `content/math_b.py` — 10-sinf (M10.1–M10.6) va 11-sinf (M11.1–M11.7)
  - `content/mathematics.py` — bosh modul, `pack()` qaytaradi
  - `exam_rules.py` — MATH_DTM (30q·3.1=93 ball) va MATH_CERT (raw68/100 ball) qo'shildi

### Tuzatildi
- **Katta ekran (1280px+)**: `app-content` da `max-width: 1200px`, `app-shell` da `max-width: 1440px; margin: auto` — keng monitorda kengayib ketmaydi
- **Test resume**: test jarayonida saytdan chiqib qayta kirganda dashboard da "Davom ettirish" banneri chiqadi (localStorage `lz_active_attempt`)
- **Google OAuth**: `next=` parametri saqlanadi — protected URL ga kirmoqchi bo'lib login sahifasiga tushgan foydalanuvchi, kirgandan keyin aynan o'sha sahifaga qaytadi
- **URL routing**: barcha 19 ta protected route redirect endi `?next=<url>` bilan — to'g'ridan URL yozib kirganda ham ishlaydi
