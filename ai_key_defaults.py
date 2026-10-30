"""Zaxira kalitlar (FAQAT agar muhit o'zgaruvchisida / .env da / admin panelda kalit BO'LMASA ishlatiladi).

Tartib: 1) muhit o'zgaruvchisi (Vercel Environment Variables yoki .env)  ->  2) admin paneldagi saqlangan kalit
        ->  3) shu fayldagi qiymat.
Shu fayl ichiga yozsangiz, qiymatni ALBATTA qo'sh tirnoq ichida yozing (tirnoqsiz yoki ortiqcha matn bilan yozilsa,
dastur chalg'ib qolishi mumkin). Tirnoq, bo'sh joy va ortiqcha belgilar avtomatik tozalanadi.

DIQQAT: bu faylni GitHub'ga yuklashdan oldin kalitni olib tashlang — ochiq repoda kalit o'g'irlanadi.
Eng xavfsiz yo'l: kalitlarni Vercel → Settings → Environment Variables ga yoki admin panelga (/neo → AI) kiriting.
"""

DEFAULT_KEYS = {
    "ANTHROPIC_API_KEY": "",   # misol: "sk-ant-...."
    "GEMINI_API_KEY": "",      # misol: "AIza...."
}
