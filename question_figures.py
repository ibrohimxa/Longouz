"""Import paytida chizmalarni ajratib olish: PDF (sahifadan kesib olish), DOCX (ichki rasmlar),
ZIP ichidagi rasmlar. Rasmlar static/qfig/ ga xavfsiz (qayta kodlangan) holda saqlanadi."""
from __future__ import annotations

import hashlib
import io
import logging
import re
from pathlib import Path

import figures

logger = logging.getLogger("longouz.qfig")

QFIG_DIR = Path(__file__).parent / "static" / "qfig"
PENDING: dict[str, bytes] = {}  # hali bazaga yozilmagan rasmlar: nom -> PNG bayt
MAX_IMAGE_PIXELS = 24_000_000
MAX_SIDE = 1600
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif")
MARKER_RE = re.compile(r"\[\[IMG:([0-9a-f]{16})\]\]")


def save_image_bytes(data: bytes) -> str | None:
    """Rasmni tekshiradi (Pillow), kattaligini cheklaydi, PNG qilib saqlaydi. '/static/qfig/..' qaytaradi."""
    try:
        from PIL import Image
        img = Image.open(io.BytesIO(data))
        if img.width * img.height > MAX_IMAGE_PIXELS:
            return None
        img.load()
        if img.mode not in ("RGB", "RGBA", "L"):
            img = img.convert("RGBA" if "A" in img.mode else "RGB")
        if max(img.size) > MAX_SIDE:
            img.thumbnail((MAX_SIDE, MAX_SIDE))
        buf = io.BytesIO()
        img.save(buf, "PNG", optimize=True)
        png = buf.getvalue()
    except Exception as exc:  # noqa: BLE001
        logger.warning("Rasm yaroqsiz: %s", exc)
        return None
    name = hashlib.sha1(png).hexdigest()[:16] + ".png"
    PENDING[name] = png  # bazaga yoziladi (main.py middleware -> db.save_qfigs); Vercel'da disk yo'q
    try:
        QFIG_DIR.mkdir(parents=True, exist_ok=True)
        path = QFIG_DIR / name
        if not path.exists():
            path.write_bytes(png)
    except OSError:
        pass  # faqat-o'qish fayl tizimi — baza yetarli
    return f"/static/qfig/{name}"


def image_figure(src: str, alt: str = "") -> dict:
    return {"type": "image", "src": src, "alt": alt}


# ---------------------------------------------------------------- PDF
_Q_LINE = re.compile(r"^\s*(\d{1,3})\s*[\.\)]\s+\S")


def _overlaps(r, region) -> bool:
    """Bo'sh (qalinligi 0) to'g'ri to'rtburchaklar uchun ham ishlaydigan kesishish tekshiruvi."""
    return r.x0 <= region.x1 and r.x1 >= region.x0 and r.y0 <= region.y1 and r.y1 >= region.y0


def pdf_question_figures(data: bytes, max_pages: int = 300, max_figs: int = 400) -> list[tuple[int, dict | None]]:
    """PDF dagi har bir savol boshi uchun (raqam, chizma|None) ro'yxati (hujjat tartibida).
    Savol hududida rasm yoki vektor chizma bo'lsa, o'sha qism PNG qilib kesib olinadi."""
    try:
        import pymupdf
    except ImportError:
        return []
    out: list[tuple[int, dict | None]] = []
    made = 0
    try:
        doc = pymupdf.open(stream=data, filetype="pdf")
    except Exception:  # noqa: BLE001
        return []
    with doc:
        for pno in range(min(len(doc), max_pages)):
            page = doc[pno]
            starts: list[tuple[int, float]] = []
            for block in page.get_text("dict").get("blocks", []):
                for line in block.get("lines", []):
                    text = "".join(sp["text"] for sp in line.get("spans", []))
                    m = _Q_LINE.match(text)
                    if m:
                        starts.append((int(m.group(1)), line["bbox"][1]))
            if not starts:
                continue
            starts.sort(key=lambda s: s[1])
            rects = []
            for img in page.get_images(full=True):
                try:
                    for r in page.get_image_rects(img[0]):
                        if r.width > 24 and r.height > 24:
                            rects.append(("img", r))
                except Exception:  # noqa: BLE001
                    pass
            drawings = []
            try:
                for d in page.get_drawings():
                    r = d.get("rect")
                    if r is None or (r.width < 1.5 and r.height < 1.5):
                        continue
                    if r.width > page.rect.width * 0.92 and r.height < 3:  # uzun chiziq (ajratgich)
                        continue
                    drawings.append(r)
            except Exception:  # noqa: BLE001
                pass
            for idx, (num, y0) in enumerate(starts):
                y1 = starts[idx + 1][1] if idx + 1 < len(starts) else page.rect.height
                region = pymupdf.Rect(0, y0 - 2, page.rect.width, y1 - 1)
                inside_img = [r for k, r in rects if _overlaps(r, region)]
                inside_dr = [r for r in drawings if _overlaps(r, region) and r.y0 >= y0 - 4 and r.y1 <= y1 + 4]
                fig = None
                if (inside_img or len(inside_dr) >= 6) and made < max_figs:
                    union = pymupdf.Rect()
                    for r in inside_img + (inside_dr if len(inside_dr) >= 6 else []):
                        union |= r
                    union &= region
                    union = pymupdf.Rect(union.x0 - 6, union.y0 - 6, union.x1 + 6, union.y1 + 6) & page.rect
                    if union.width >= 28 and union.height >= 28:
                        try:
                            pix = page.get_pixmap(clip=union, dpi=170, alpha=False)
                            src = save_image_bytes(pix.tobytes("png"))
                            if src:
                                fig = image_figure(src, f"{num}-savol chizmasi")
                                made += 1
                        except Exception as exc:  # noqa: BLE001
                            logger.warning("PDF chizma kesilmadi: %s", exc)
                out.append((num, fig))
    return out


def attach_pdf_figures(items: list[dict], found: list[tuple[int, dict | None]]) -> int:
    """Savollar tartibida (raqam bo'yicha oldinga qarab) chizmalarni biriktiradi."""
    ptr, attached = 0, 0
    for it in items:
        no = it.get("no")
        j = ptr
        while j < len(found) and found[j][0] != no:
            j += 1
        if j >= len(found):
            continue
        ptr = j + 1
        fig = found[j][1]
        if fig:
            it["figure"] = {"q": fig, "o": [None] * 4}
            it["question"] = re.sub(r"(?<=[.?!:])(\s+\S{1,2}){1,8}\s*$", "", it["question"]).strip() or it["question"]
            attached += 1
    return attached


# ---------------------------------------------------------------- DOCX
def docx_marker_text(run_element, part) -> str:
    """Run ichidagi rasmlarni saqlaydi va matnga [[IMG:hash]] belgisini qo'yadi."""
    marks = []
    for blip in run_element.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}blip"):
        rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
        if not rid:
            continue
        try:
            blob = part.related_parts[rid].blob
        except Exception:  # noqa: BLE001
            continue
        src = save_image_bytes(blob)
        if src:
            marks.append(f"[[IMG:{Path(src).stem}]]")
    return " ".join(marks)


def resolve_markers(items: list[dict]) -> int:
    """Savol/variant matnidagi [[IMG:..]] belgilarini chizma hujjatiga aylantiradi."""
    n = 0
    for it in items:
        fig = {"q": None, "o": [None] * 4}
        found = False

        def strip(text: str):
            hits = MARKER_RE.findall(text or "")
            return MARKER_RE.sub("", text or "").strip(), hits

        it["question"], hits = strip(it.get("question", ""))
        if hits:
            fig["q"] = image_figure(f"/static/qfig/{hits[0]}.png", "Savol chizmasi")
            found = True
        for i, opt in enumerate(it.get("options", [])):
            clean, hits = strip(opt)
            it["options"][i] = clean
            if hits:
                fig["o"][i] = image_figure(f"/static/qfig/{hits[0]}.png", f"{'ABCD'[i]} variant")
                found = True
        if found:
            it["figure"] = fig
            n += 1
    return n


# ---------------------------------------------------------------- ZIP rasmlari
def zip_image_index(entries: list[tuple[str, bytes]]) -> dict[str, str]:
    """{kichik harfli fayl nomi (kengaytmasiz) -> '/static/qfig/..'} (barcha rasmlar saqlanadi)."""
    index: dict[str, str] = {}
    for name, blob in entries:
        low = name.lower()
        if not low.endswith(IMAGE_EXT):
            continue
        src = save_image_bytes(blob)
        if src:
            base = low.replace("\\", "/").split("/")[-1]
            index[base] = src
            index[base.rsplit(".", 1)[0]] = src
    return index


def attach_zip_images(items: list[dict], index: dict[str, str]) -> int:
    """1) JSON dagi figure.src fayl nomi bo'lsa, saqlangan yo'lga almashtiradi.
       2) Rasm nomi savol raqami bo'lsa (1.png, q1.jpg, savol_1.png) shu savolga biriktiradi."""
    if not index:
        return 0
    n = 0
    by_no: dict[int, str] = {}
    for key, src in index.items():
        m = re.fullmatch(r"(?:q|savol|question|rasm|img|image|fig)?[_\- ]*0*(\d{1,3})", key)
        if m:
            by_no.setdefault(int(m.group(1)), src)

    def fix(f):
        if isinstance(f, dict) and f.get("type") == "image":
            s = str(f.get("src") or "").replace("\\", "/")
            if s.startswith("/static/qfig/"):
                return f
            key = s.lower().split("/")[-1]
            hit = index.get(key) or index.get(key.rsplit(".", 1)[0])
            return image_figure(hit, f.get("alt", "")) if hit else None
        return f

    for it in items:
        doc = it.get("figure")
        if isinstance(doc, dict):
            doc["q"] = fix(doc.get("q"))
            doc["o"] = [fix(x) for x in (doc.get("o") or [None] * 4)]
            n += 1
        elif it.get("no") in by_no:
            it["figure"] = {"q": image_figure(by_no[it["no"]], "Savol chizmasi"), "o": [None] * 4}
            n += 1
    return n


def clean_figure_doc(doc) -> dict:
    return figures.sanitize_figures_doc(doc)
