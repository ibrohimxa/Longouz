# LongoUZ — versiyalar tarixi

Har yuborilgan zip: `longouz_v<N>.zip`, versiya raqami `VERSION` faylida.

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
