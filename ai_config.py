"""
LongoUZ WEBSAYT uchun sozlamalar (bot config.py'ga o'xshab, lekin alohida).

Kalitlarni muhit o'zgaruvchisi orqali bering:
  Windows PowerShell:
    $env:ANTHROPIC_API_KEY="sk-ant-..."
    $env:GEMINI_API_KEY="AIza..."
    uvicorn web.main:app --reload

Kalit qo'yilmagunicha /ask va /quiz komandalari "AI hali sozlanmagan" deb
xushmuomalalik bilan javob beradi - sayt buzilmaydi.
"""

import os

import ai_keys
ai_keys.reload_env()

# --- Anthropic (Claude) — test generatsiya, murakkab tushuntirish, baholash ---
# XAVFSIZLIK, MUHIM: bu yerda ILGARI haqiqiy API kalit ochiq matnda yozilgan
# edi (standart qiymat sifatida). Bu JIDDIY xavfsizlik teshigi edi — kod
# GitHub'ga yuklansa yoki boshqa birov ko'rsa, kalit darhol o'g'irlanadi va
# SIZNING HISOBINGIZ hisobidan kimdir cheksiz so'rov yubora oladi (aynan
# shuning uchun "credit balance too low" xatosi chiqqan bo'lishi ehtimoli
# katta — kalit allaqachon oshkor bo'lgan va boshqa birov ishlatgan bo'lishi
# mumkin). Endi standart qiymat yo'q — kalit FAQAT muhit o'zgaruvchisi orqali
# (yoki .env fayldan) olinadi, kodning hech bir joyida yozilmagan.
# ANTHROPIC_API_KEY: .env yoki Vercel Environment Variables ichida (qo'shtirnoqsiz).
# .env bo'lmagan holat uchun: CONFIG_ANTHROPIC_API_KEY ga to'g'ridan-to'g'ri yozsangiz bo'ladi,
# lekin bu XAVFSIZ EMAS — git'ga tushurib yubormaslik uchun .env usulini ishlating.
CONFIG_ANTHROPIC_API_KEY = ""  # <-- faqat test/lokal uchun; .env ustunlik qiladi
ANTHROPIC_API_KEY = ai_keys.get("ANTHROPIC_API_KEY") or CONFIG_ANTHROPIC_API_KEY.strip().strip("\"'")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")  # claude-sonnet-4-6 — tezkor va iqtisodiy
CLAUDE_MAX_TOKENS = 2000

# Ba'zi Anthropic kalitlari (ayniqsa tashkilot/Console hisobidagi "umumiy"
# kalitlar) BITTA workspace'ga bog'lanmagan bo'ladi — bunday kalit bilan
# so'rov yuborilganda API "anthropic-workspace-id header talab qilinadi"
# deb xato beradi. Agar sizda ham shunday xato chiqsa: Anthropic Console'da
# Settings -> Workspaces bo'limidan workspace ID'ni oling (masalan
# "wrkspc_01AbCdEfGh...") va shu o'zgaruvchiga qo'ying:
#   $env:ANTHROPIC_WORKSPACE_ID="wrkspc_..."
# Kalitingiz allaqachon bitta workspace'ga bog'langan bo'lsa, buni bo'sh
# qoldiring — hech narsa o'zgarmaydi.
ANTHROPIC_WORKSPACE_ID = os.getenv("ANTHROPIC_WORKSPACE_ID", "")

# --- Gemini — tezkor, oddiy darajadagi repetitor chat ---
# XAVFSIZLIK: xuddi yuqoridagidek — standart qiymatda haqiqiy kalit YO'Q.
# GEMINI_API_KEY: .env yoki Vercel Environment Variables ichida "GEMINI_API_KEY" nomli
# kalit (qo'shtirnoqsiz, to'g'ridan-to'g'ri kalit qiymatini yozing).
# .env'da bo'lmasa, pastdagi CONFIG_GEMINI_API_KEY o'zgaruvchisiga bevosita
# yozishingiz mumkin — ammo bu XAVFSIZ EMAS va git'ga tushmasm uchun avval
# .env usulini sinab ko'ring.
CONFIG_GEMINI_API_KEY = ""  # <-- .env bo'lmagan holda bu yerga yozsa bo'ladi (faqat test uchun)
GEMINI_API_KEY = ai_keys.get("GEMINI_API_KEY") or CONFIG_GEMINI_API_KEY.strip().strip("\"'")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")  # gemini-2.5-flash — eng so'nggi tezkor model
GEMINI_MAX_TOKENS = 1000

# --- Qaysi daraja qaysi AI'ga yo'naltirilsin ---
# "boshlangich" -> Gemini (tez, arzon, oddiy tushuntirish yetarli)
# "ortacha" / "yuqori" -> Claude (chuqurroq tushuntirish kerak)
GEMINI_LEVELS = {"boshlangich"}
CLAUDE_LEVELS = {"ortacha", "yuqori"}

# Test generatsiyasi va yakuniy baholash HAR DOIM Claude orqali bo'ladi
# (daraja qanday bo'lishidan qat'iy nazar) - chunki aniq JSON struktura va
# barqaror baholash mantiqi kerak.

# --- Sayt manzili — sertifikat PDF'idagi QR kod shu manzilga olib boradi ---
# Production'da o'zingizning domeningizga o'zgartiring, masalan:
#   $env:SITE_BASE_URL="https://longouz.uz"
import runtime as _rt
SITE_BASE_URL = _rt.site_base_url()

# --- DOIMIY XAVFSIZLIK QO'RIQCHISI ---
# Bu loyihada avval ikki marta (Anthropic va Gemini) haqiqiy API kalitlari
# koddagi standart qiymat sifatida ochiq qolib ketgan va GitHub/zip orqali
# tarqalgan edi. Bu funksiya har safar server ishga tushganda ishlaydi va
# agar o'sha ANIQ oshkor bo'lgan kalitlar yana qaysidir joyda (env, .env,
# yoki kod) paydo bo'lsa — serverni ATAYLAB ishga tushirmaydi, chunki bu
# degani kimdir eski, buzilgan nusxadan hali ham foydalanyapti.
_KNOWN_LEAKED_VALUES = [
   
]
for _leaked in _KNOWN_LEAKED_VALUES:
    if _leaked and (_leaked in ANTHROPIC_API_KEY or _leaked in GEMINI_API_KEY):
        raise RuntimeError(
            "XAVFSIZLIK TO'XTATUVI: Bu API kalit ILGARI oshkor bo'lgan "
            "(GitHub/zip orqali tarqalgan) va ENDI ISHLATIB BO'LMAYDI. "
            "Anthropic/Google konsolida bu kalitni bekor qiling (revoke) "
            "va YANGI kalit yarating, so'ng uni faqat `.env` fayliga yozing. "
            "Server xavfsizlik uchun ataylab ishga tushmadi."
        )


def anthropic_key() -> str:
    return ai_keys.get("ANTHROPIC_API_KEY")


def gemini_key() -> str:
    return ai_keys.get("GEMINI_API_KEY")
