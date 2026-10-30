@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul
title LONGOUZ - yangi versiyani GitHub va Vercel ga joylash

rem ============================================================
rem  FOYDALANISH: yangi versiya ZIP faylini (yoki ochilgan
rem  longouz papkasini) shu faylning USTIGA sudrab tashlang.
rem  Skript: 1) loyiha papkasidagi fayllarni almashtiradi,
rem          2) git commit + git push qiladi,
rem          3) Vercel GitHub'dagi o'zgarishni ko'rib, saytni
rem             o'zi qayta joylaydi (1-3 daqiqa).
rem  .env, .git, .vercel, *.db fayllariga TEGILMAYDI.
rem ============================================================

rem --- SOZLAMALAR (kerak bo'lsa o'zgartiring) ---
set "TARGET=C:\Users\Usmon\Documents\LongoUZ"
set "REPO_URL="
rem  REPO_URL bo'sh bo'lsa, birinchi ishga tushirishda so'raladi (masalan https://github.com/SIZNING-NOMINGIZ/Longouz.git)
set "BRANCH=main"
rem ------------------------------------------------

set "SRC=%~1"
set "VER=%~n1"
set "TMPDIR="

if "!SRC!"=="" (
  echo.
  echo  Yangi versiya ZIP faylini yoki longouz papkasini shu fayl ustiga sudrab tashlang.
  echo.
  pause
  exit /b 1
)

where git >nul 2>nul
if errorlevel 1 (
  echo.
  echo  XATO: git topilmadi. "Git for Windows" ni o'rnating: https://git-scm.com/download/win
  echo.
  pause
  exit /b 1
)

if not exist "%TARGET%\" (
  echo  Loyiha papkasi yo'q, yangi yaratilmoqda: %TARGET%
  mkdir "%TARGET%"
)

rem --- ZIP bo'lsa avval ochamiz ---
if /i "%~x1"==".zip" (
  set "TMPDIR=%TEMP%\longouz-deploy-%RANDOM%%RANDOM%"
  echo  ZIP ochilmoqda...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '!SRC!' -DestinationPath '!TMPDIR!' -Force"
  if errorlevel 1 (
    echo  XATO: ZIP faylni ochib bo'lmadi.
    pause
    exit /b 1
  )
  set "SRC=!TMPDIR!"
)

if "!SRC:~-1!"=="\" set "SRC=!SRC:~0,-1!"

rem --- main.py topilgan papkani qidiramiz (ZIP ichida bitta papka bo'lishi mumkin) ---
if not exist "!SRC!\main.py" (
  for /d %%d in ("!SRC!\*") do (
    if exist "%%d\main.py" set "SRC=%%d"
  )
)

if not exist "!SRC!\main.py" (
  echo.
  echo  XATO: bu LongoUZ loyihasiga o'xshamaydi ^(main.py topilmadi^).
  echo  Tekshirilgan joy: !SRC!
  echo.
  if defined TMPDIR rmdir /s /q "!TMPDIR!" >nul 2>nul
  pause
  exit /b 1
)
if not exist "!SRC!\vercel.json" (
  echo.
  echo  OGOHLANTIRISH: vercel.json yo'q - bu eski versiya, Vercelda ishlamasligi mumkin.
  echo.
)

echo.
echo  Manba : !SRC!
echo  Maqsad: %TARGET%
echo.
echo  Fayllar almashtirilmoqda...

rem  /MIR - yangi versiyada yo'q fayllarni ham o'chiradi; .git/.env/.vercel/*.db ga tegilmaydi
robocopy "!SRC!" "%TARGET%" /MIR /XD .git .venv .vercel node_modules __pycache__ certs public /XF .env .env.* *.db *.pyc .web_secret_key.local /NFL /NDL /NJH /NJS /NP >nul
if errorlevel 8 (
  echo.
  echo  XATO: fayllarni ko'chirishda muammo chiqdi.
  if defined TMPDIR rmdir /s /q "!TMPDIR!" >nul 2>nul
  pause
  exit /b 1
)

if defined TMPDIR rmdir /s /q "!TMPDIR!" >nul 2>nul

rem --- git: birinchi marta bo'lsa ulaymiz ---
if not exist "%TARGET%\.git\" (
  echo  Git repozitoriysi yaratilmoqda va GitHub'ga ulanmoqda...
  if "!REPO_URL!"=="" (
    echo.
    echo  GitHub repozitoriy manzilini kiriting ^(masalan: https://github.com/SIZNING-NOMINGIZ/Longouz.git^)
    set /p "REPO_URL=  Manzil: "
  )
  if "!REPO_URL!"=="" (
    echo  XATO: repozitoriy manzili kiritilmadi.
    pause
    exit /b 1
  )
  git -C "%TARGET%" init
  git -C "%TARGET%" branch -M %BRANCH%
  git -C "%TARGET%" remote add origin "!REPO_URL!"
)

set "ROOT=%TARGET%"
echo  Git papkasi: !ROOT!
echo.

set "CHANGED="
for /f "delims=" %%i in ('git -C "!ROOT!" status --porcelain') do set "CHANGED=1"
if not defined CHANGED (
  echo  Hech narsa o'zgarmadi - bu versiya allaqachon joylangan.
  echo.
  pause
  exit /b 0
)

if "!VER!"=="" set "VER=yangilash"
git -C "!ROOT!" add -A
rem --- XAVFSIZLIK: .env va kalitlar GitHub'ga HECH QACHON ketmasin ---
git -C "!ROOT!" rm --cached -q --ignore-unmatch .env .env.local .web_secret_key.local deploy_config.txt >nul 2>nul
set "LEAK="
for /f "delims=" %%i in ('git -C "!ROOT!" diff --cached -U0 ^| findstr /R /C:"sk-ant-api[0-9A-Za-z_-][0-9A-Za-z_-]*" /C:"GOCSPX-[0-9A-Za-z_-][0-9A-Za-z_-]*" /C:"AIzaSy[0-9A-Za-z_-][0-9A-Za-z_-]*"') do set "LEAK=1"
if defined LEAK (
  git -C "!ROOT!" reset -q
  echo.
  echo  TO'XTATILDI: o'zgarishlar ichida KALIT ko'rindi ^(sk-ant-... / AIza... / GOCSPX-...^).
  echo  Kalitni fayldan olib tashlang va kalitlarni admin panel ^(/neo/keys^) yoki Vercel Environment Variables orqali kiriting.
  echo  GitHub'ga hech narsa yuborilmadi.
  pause
  exit /b 1
)
git -C "!ROOT!" commit -m "Yangilash: !VER!"
if errorlevel 1 (
  echo.
  echo  XATO: commit bajarilmadi. Git'da ism/email sozlanmagan bo'lishi mumkin. Quyidagilarni bir marta bajaring:
  echo    git config --global user.name "Ismingiz"
  echo    git config --global user.email "iborgimxa6@gmail.com"
  pause
  exit /b 1
)

echo.
echo  GitHub'ga yuborilmoqda...
git -C "!ROOT!" push -u origin %BRANCH%
if errorlevel 1 (
  echo.
  echo  Push rad etildi. Agar repo'da boshqa tarix bo'lsa, "yangi versiya bilan almashtirish" kerak.
  choice /C YN /M "  Majburan almashtirilsinmi (git push --force)?"
  if errorlevel 2 (
    echo  Bekor qilindi.
    pause
    exit /b 1
  )
  git -C "!ROOT!" push -u --force origin %BRANCH%
  if errorlevel 1 (
    echo.
    echo  XATO: push bajarilmadi. Yuqoridagi xabarni o'qing ^(GitHub login yoki internet muammosi^).
    pause
    exit /b 1
  )
)

echo.
echo  ================================================
echo   TAYYOR! Kod GitHub'ga yuborildi.
echo   Vercel saytni avtomatik yangilaydi
echo   ^(1-3 daqiqa; Vercel panelida "Ready" ni kuting^).
echo  ================================================
echo.
pause
