"""
LongoUZ — rasmiy PDF sertifikat generatori.

Muvaffaqiyatli yakunlangan DTM/Sertifikat/IELTS/CEFR testi uchun O'zbekiston
milliy sertifikat andozasiga yaqin ("Umumta'lim fanini bilish darajasi
to'g'risida sertifikat" uslubida), tekshirish QR kodi bilan PDF hujjat
yaratadi. Hech qanday tashqi shrift talab qilinmaydi — faqat reportlab'ning
ichki shriftlaridan foydalanadi, shuning uchun har qanday serverda ishlaydi.
"""

import io

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import qrcode

from ai_config import SITE_BASE_URL

BRAND_BLUE = HexColor("#1A5FE0")
BRAND_BLUE_LIGHT = HexColor("#4FA8FF")
INK = HexColor("#12213E")
INK_SOFT = HexColor("#5A6B8C")
GOLD = HexColor("#D9A441")
GOLD_LIGHT = HexColor("#F3E3BE")


def _verification_url(verification_id: str) -> str:
    return f"{SITE_BASE_URL}/certificate/{verification_id}"


def _make_qr_image(verification_id: str) -> io.BytesIO:
    qr = qrcode.QRCode(border=1, box_size=6)
    qr.add_data(_verification_url(verification_id))
    qr.make(fit=True)
    img = qr.make_image(fill_color="#12213E", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def _grade_letter(percent: int) -> str:
    """Rasmdagi namunaga o'xshab (masalan 'A+'), foizni harfli darajaga aylantiradi."""
    if percent >= 95:
        return "A+"
    if percent >= 85:
        return "A"
    if percent >= 75:
        return "B+"
    if percent >= 60:
        return "B"
    if percent >= 45:
        return "C+"
    if percent >= 30:
        return "C"
    return "D"


def _draw_ornate_background(c, width: float, height: float, margin: float):
    """
    Rasmiy davlat hujjatlariga o'xshagan nozik, takrorlanuvchi bezak
    naqshini (guilloche uslubi) chizadi — och oltin rangda, matnga
    xalaqit bermaydigan darajada shaffof. Bunday naqsh haqiqiy
    sertifikatlarga xos "soxtalashtirish qiyin" ko'rinishni beradi.
    """
    c.saveState()
    # Naqsh faqat ramka ICHIDA chizilishi uchun shu to'rtburchak bilan
    # kesib (clip) qo'yamiz — shunda diagonal chiziqlar chetdan chiqib
    # ketmaydi.
    clip_path = c.beginPath()
    clip_path.rect(margin, margin, width - 2 * margin, height - 2 * margin)
    c.clipPath(clip_path, stroke=0, fill=0)

    c.setStrokeColor(HexColor("#EEE3C4"))
    c.setLineWidth(0.35)
    step = 7 * mm
    diag = width + height  # diagonalning to'liq uzunligidan kattaroq oraliq
    i = -diag
    while i < diag:
        c.line(margin + i, margin, margin + i + (height - 2 * margin), height - margin)
        i += step
    c.restoreState()

    # To'rt burchakda kichik romb-bezak (rasmiy hujjatlarga xos burchak belgisi)
    corner_size = 7 * mm
    corners = [
        (margin + 6 * mm, height - margin - 6 * mm),
        (width - margin - 6 * mm, height - margin - 6 * mm),
        (margin + 6 * mm, margin + 6 * mm),
        (width - margin - 6 * mm, margin + 6 * mm),
    ]
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.9)
    for cx, cy in corners:
        c.line(cx - corner_size / 2, cy, cx + corner_size / 2, cy)
        c.line(cx, cy - corner_size / 2, cx, cy + corner_size / 2)
        c.circle(cx, cy, corner_size / 2, fill=0, stroke=1)


def _draw_field_row(c, x: float, y: float, label: str, value: str, label_width: float = 62 * mm):
    """Rasmdagi kabi 'Yorliq: Qiymat' formatidagi bitta qatorni chizadi."""
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica", 10)
    c.drawString(x, y, label)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + label_width, y, value)


def _draw_answer_grid(c, x: float, top_y: float, width: float, answer_grid: list[dict]) -> float:
    """
    Rasmiy DTM javob varag'iga o'xshagan ko'p ustunli javoblar ro'yxatini
    chizadi ("1. A" to'g'ri bo'lsa yashil, xato bo'lsa qizil rangda). Qolgan
    balandlikni tejash uchun savollar soniga qarab ustunlar sonini
    moslashtiradi. Chizishni tugatgan Y koordinatasini qaytaradi.
    """
    if not answer_grid:
        return top_y

    total = len(answer_grid)
    columns = 4 if total > 20 else (3 if total > 10 else 2)
    rows = -(-total // columns)  # ceil division
    row_h = 5.2 * mm
    col_w = width / columns

    c.setFont("Helvetica", 8)
    for i, item in enumerate(answer_grid):
        col = i // rows
        row = i % rows
        cx = x + col * col_w
        cy = top_y - row * row_h
        color = HexColor("#1E8E5A") if item["is_correct"] else (INK_SOFT if item["letter"] == "—" else HexColor("#C0392B"))
        c.setFillColor(color)
        mark = "✓" if item["is_correct"] else ("—" if item["letter"] == "—" else "✗")
        c.drawString(cx, cy, f"{item['num']}. {item['letter']}  {mark}")

    return top_y - rows * row_h


def generate_certificate_pdf(
    full_name: str,
    subject_name: str,
    score_label: str,
    mode_name: str,
    issued_date: str,
    verification_id: str,
    correct_count: int = 0,
    total_count: int = 0,
    percent: int = 0,
    valid_until_date: str = "",
    mode_code: str = "dtm",
    answer_grid: list[dict] | None = None,
    topic_breakdown: list[dict] | None = None,
    student_id: str = "",
    grade_override: str = "",
) -> bytes:
    """
    Rasmiy sertifikat PDF'ini generatsiya qiladi va bayt sifatida qaytaradi
    (diskka yozmaydi — to'g'ridan-to'g'ri HTTP javobida yuborish uchun).

    Andoza foydalanuvchi taqdim etgan O'zbekiston Respublikasi Umumta'lim
    fanini bilish darajasi to'g'risidagi rasmiy sertifikatning MAYDON
    TUZILISHI va UMUMIY KO'RINISHIGA (yozuv joylashuvi, ranglar, bezak
    ramka) yaqinlashtirilgan.

    MUHIM, ATAYLAB QILINGAN FARQ: bu yerda hech qachon HAQIQIY davlat
    idorasi nomi (masalan "...Bilim va Malakalarni Baholash Agentligi")
    ishlatilmaydi va rasmiy davlat gerbi chizilmaydi — faqat "LongoUZ
    ta'lim platformasi" issuer sifatida ko'rsatiladi, va pastda aniq
    "rasmiy davlat hujjati emas" degan izoh doim chiqadi. Buning sababi:
    xatti-harakati/ko'rinishi rasmiy davlat idorasi tomonidan berilgandek
    ko'rinadigan, ammo aslida shunday bo'lmagan hujjat yaratish — bu
    real hayotda ishga joylashish yoki boshqa joyларда soxta imtiyoz
    olish uchun suiiste'mol qilinishi mumkin bo'lgan hujjat firibgarligi
    hisoblanadi. Vizual o'xshashlik (ramka, joylashuv, ranglar) — bezash
    maqsadida; lekin KIM bergani va bu RASMIY EMASLIGI har doim aniq
    bo'lib qoladi.
    """
    buf = io.BytesIO()
    page_size = A4  # rasmdagi namunaga mos — vertikal (portrait) format
    c = canvas.Canvas(buf, pagesize=page_size)
    width, height = page_size

    grade = grade_override or _grade_letter(percent)

    # --- Fon va bezakli ramka ---
    c.setFillColor(HexColor("#FBF8F0"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    margin = 12 * mm
    _draw_ornate_background(c, width, height, margin)

    c.setStrokeColor(GOLD)
    c.setLineWidth(2.4)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin, fill=0, stroke=1)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.rect(margin + 2 * mm, margin + 2 * mm, width - 2 * margin - 4 * mm, height - 2 * margin - 4 * mm, fill=0, stroke=1)
    c.setStrokeColor(BRAND_BLUE)
    c.setLineWidth(0.5)
    c.rect(margin + 3.5 * mm, margin + 3.5 * mm, width - 2 * margin - 7 * mm, height - 2 * margin - 7 * mm, fill=0, stroke=1)

    top = height - margin

    # --- Issuer — ATAYLAB "LongoUZ ta'lim platformasi", HECH QACHON haqiqiy
    #     davlat idorasi nomi emas (batafsil izoh yuqorida) ---
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica", 8)
    c.drawCentredString(width / 2, top - 10 * mm, "LONGOUZ TA'LIM PLATFORMASI")
    c.setFont("Helvetica-Oblique", 6.5)
    c.drawCentredString(width / 2, top - 14 * mm, "(norasmiy, onlayn platforma sertifikati — davlat hujjati emas)")

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width / 2, top - 23 * mm, "UMUMTA'LIM FANINI BILISH DARAJASI")
    c.drawCentredString(width / 2, top - 29.5 * mm, "TO'G'RISIDA SERTIFIKAT")

    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(width / 2 - 45 * mm, top - 33 * mm, width / 2 + 45 * mm, top - 33 * mm)

    # --- MA'LUMOTLAR BLOKI — rasmdagi kabi, chapga tekislangan
    #     "Yorliq: Qiymat" qatorlari (bezakli quti o'rniga) ---
    field_x = margin + 14 * mm
    y = top - 44 * mm
    line_h = 7.2 * mm

    _draw_field_row(c, field_x, y, "Sertifikat raqami:", f"LU{verification_id}"); y -= line_h
    if student_id:
        _draw_field_row(c, field_x, y, "Talabaning ID raqami:", student_id); y -= line_h
    _draw_field_row(c, field_x, y, "F.I.Sh.:", full_name or "LongoUZ foydalanuvchisi"); y -= line_h
    _draw_field_row(c, field_x, y, "Test fani:", subject_name); y -= line_h
    _draw_field_row(c, field_x, y, "Test turi:", mode_name); y -= line_h * 1.3

    _draw_field_row(c, field_x, y, "Umumiy to'plagan ball:", score_label); y -= line_h
    _draw_field_row(c, field_x, y, "To'g'ri javoblar soni:", f"{correct_count} / {total_count}"); y -= line_h
    _draw_field_row(c, field_x, y, "Umumiy ball nisbiy foizi:", f"{percent}%"); y -= line_h

    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica", 10)
    c.drawString(field_x, y, "Sertifikat darajasi:")
    c.setFillColor(BRAND_BLUE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(field_x + 62 * mm, y - 1 * mm, grade if percent else score_label)
    y -= line_h * 1.6

    # --- Bo'limlar (mavzular) bo'yicha natijalari — rasmdagi kabi ---
    if topic_breakdown:
        c.setFillColor(INK_SOFT)
        c.setFont("Helvetica", 10)
        c.drawString(field_x, y, "Bo'limlar bo'yicha natijalari:")
        y -= line_h
        c.setFont("Helvetica", 9.5)
        for item in topic_breakdown[:6]:  # joy yetarli bo'lishi uchun cheklaymiz
            c.setFillColor(INK)
            c.drawString(field_x + 6 * mm, y, f"{item['topic']}:")
            c.drawRightString(field_x + 62 * mm + 20 * mm, y, f"{item['correct']}/{item['total']}")
            y -= line_h * 0.85
        y -= line_h * 0.4

    # --- Foydalanuvchi ismi (katta, markazda) — vizual urg'u sifatida ---
    y -= 2 * mm
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.6)
    c.line(field_x, y, width - field_x, y)
    y -= 8 * mm
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width / 2, y, "Muvaffaqiyatli tayyorlagan LongoUZ o'quvchisi:")
    y -= 8 * mm
    c.setFillColor(BRAND_BLUE)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, y, full_name or "LongoUZ foydalanuvchisi")

    # --- DTM rejimida — javoblar xulosasi (agar joy qolsa) ---
    y -= 14 * mm
    if mode_code == "dtm" and answer_grid and y > margin + 42 * mm:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(INK)
        c.drawCentredString(width / 2, y, "JAVOBLAR XULOSASI")
        y -= 6 * mm
        grid_width = width - 2 * margin - 24 * mm
        y = _draw_answer_grid(c, margin + 12 * mm, y, grid_width, answer_grid)

    # --- Pastki qism: sana, amal qilish muddati, imzo, QR, halollik izohi ---
    bottom_y = margin + 20 * mm

    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica", 9)
    c.drawString(margin + 14 * mm, bottom_y + 22 * mm, f"Berilgan sana: {issued_date}")
    if valid_until_date:
        c.drawString(margin + 14 * mm, bottom_y + 17 * mm, f"Amal qilish muddati: {valid_until_date}")
    c.drawString(margin + 14 * mm, bottom_y + 12 * mm, f"Tekshirish ID: {verification_id}")

    # Direktor imzosi joyi (rasmdagi kabi — chiziq + lavozim, shaxs ismisiz,
    # chunki bu haqiqiy shaxs emas)
    c.setStrokeColor(INK_SOFT)
    c.line(margin + 14 * mm, bottom_y, margin + 62 * mm, bottom_y)
    c.setFont("Helvetica", 8.5)
    c.drawString(margin + 14 * mm, bottom_y - 5 * mm, "Direktor")

    # QR kod — o'ng pastda, tekshirish sahifasiga olib boradi
    qr_buf = _make_qr_image(verification_id)
    qr_size = 22 * mm
    c.drawImage(
        ImageReader(qr_buf),
        width - margin - qr_size - 12 * mm, bottom_y - 4 * mm,
        width=qr_size, height=qr_size, mask="auto",
    )
    c.setFont("Helvetica", 7)
    c.setFillColor(INK_SOFT)
    c.drawCentredString(
        width - margin - qr_size / 2 - 12 * mm, bottom_y - 8 * mm, "Tekshirish uchun skanerlang",
    )

    # Halollik izohi — HAR DOIM, barcha rejimlarda ko'rinadi (batafsil izoh
    # yuqoridagi funksiya docstringida)
    c.setFont("Helvetica-Oblique", 6.5)
    c.setFillColor(INK_SOFT)
    c.drawCentredString(
        width / 2, margin + 6 * mm,
        "Ushbu sertifikat LongoUZ ta'lim platformasida o'tkazilgan onlayn test natijasi asosida avtomatik berilgan — rasmiy davlat hujjati emas.",
    )

    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()
