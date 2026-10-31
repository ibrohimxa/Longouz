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
ANTHROPIC_API_KEY = ai_keys.get("ANTHROPIC_API_KEY")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
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
GEMINI_API_KEY = ai_keys.get("GEMINI_API_KEY")
# v233: eng yangi BEPUL Gemini modeli (2026-yil sentabr, GA). gemini-4-argon bepul tarifda yo'q.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
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
# v222: kalitlarning O'ZI emas, SHA-256 xeshi saqlanadi (ochiq repoda kalit ko'rinmasin).
_KNOWN_LEAKED_SHA256 = {
    "81ce2485882bf3dc4505f82468f9b0a93dbe532fbb7ebff59f4a9a563e6d2869",
    "2768ab05c836d13905f6ec648195fefc0d0dc37e475f501acb556d58ef7bd5a5",
    "830ea18979df118cc7bdb81a6ea9c956f52667f1c45264b1c13f48d4379279b0",
    "7300fe020c7e45b0c78726f3742c04602703b7b7cb702a4e62e15c32cef783ac",
    "907345a4bc7dc0f0d1e20bae525d3c61077fe7492cd079a35fe16de160ca19b5",
    "c53bcc50689492a7c8ef2df599c4a530bdf281e37e7a1fa31e5d91e6158c6f4f",
}
import hashlib as _hl
for _cand in (ANTHROPIC_API_KEY, GEMINI_API_KEY):
    if _cand and _hl.sha256(_cand.strip().encode()).hexdigest() in _KNOWN_LEAKED_SHA256:
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
