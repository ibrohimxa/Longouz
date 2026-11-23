"""v248: QIDIRUV TIZIMLARI VA SUN'IY INTELLEKTLAR UCHUN (SEO + AEO).

- /robots.txt       — Google, Bing, Yandex va AI botlariga (GPTBot, Google-Extended, ClaudeBot, PerplexityBot …)
                      ochiq sahifalarni o'qishga ruxsat; shaxsiy sahifalar va API yopiq.
- /sitemap.xml      — barcha ochiq sahifalar ro'yxati.
- /llms.txt         — sun'iy intellektlar uchun sayt haqida qisqa, aniq ma'lumot (llmstxt.org standarti).
- /llms-full.txt    — fanlar va mavzular bilan to'liq ma'lumot.
- /<KEY>.txt        — IndexNow kaliti: Bing, Yandex (va ular orqali ChatGPT/Copilot qidiruvi) yangi sahifani
                      darhol biladi. Domen sotib olish shart emas.
- /subjects, /subjects/<fan>, /about — qidiruvda chiqadigan ochiq sahifalar (mavzular ro'yxati bilan).
- Google / Bing / Yandex tasdiqlash kodi admin paneldan kiritiladi (Sozlamalar → Qidiruv tizimlari).
"""
from __future__ import annotations

import asyncio
import html
import json
import logging
import os
import re
import time
from datetime import date
from functools import lru_cache

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, Response

logger = logging.getLogger(__name__)
router = APIRouter()

# IndexNow kaliti ochiq bo'lishi kerak (sayt ildizida /<kalit>.txt sifatida turadi) — maxfiy emas.
INDEXNOW_KEY = "lz8c41f7e29b3d4a6e9f05c2b71d8e3a46"
LASTMOD = "2026-11-22"

SLUGS = {
    "mathematics": "math", "uzbek-language": "native", "english": "english", "russian": "russian",
    "history": "history", "chemistry": "chemistry", "biology": "biology", "physics": "physics",
}
# v250: eski o'zbekcha manzillar yangisiga doimiy yo'naltiriladi
OLD_SLUGS = {
    "matematika": "mathematics", "ona-tili": "uzbek-language", "ingliz-tili": "english", "rus-tili": "russian",
    "tarix": "history", "kimyo": "chemistry", "biologiya": "biology", "fizika": "physics",
}
CODE2SLUG = {v: k for k, v in SLUGS.items()}

SUBJECT_INFO = {
    "math": ("Matematika", "Algebra, geometriya, funksiyalar, tenglama va tengsizliklar, trigonometriya, logarifm, hosila va integral — 5–11-sinf dasturi bo'yicha DTM va milliy sertifikat testlari, chizmali masalalar bilan."),
    "native": ("Ona tili va adabiyot", "Fonetika, leksika, morfologiya, sintaksis, imlo va tinish belgilari hamda o'zbek mumtoz va zamonaviy adabiyoti — DTM va milliy sertifikat uchun testlar."),
    "english": ("Ingliz tili", "Grammatika (zamonlar, modal fe'llar, shart gaplar, passive voice), lug'at, reading va CEFR/milliy sertifikat, DTM va IELTS Reading, Writing, Speaking tayyorgarligi."),
    "russian": ("Rus tili", "Fonetika, orfoepiya, morfologiya, sintaksis, punktuatsiya va rus adabiyoti — DTM va milliy sertifikat testlari."),
    "history": ("Tarix", "O'zbekiston va jahon tarixi: qadimgi davrdan mustaqillik yillarigacha, 6–11-sinf darsliklari bo'yicha DTM va milliy sertifikat testlari."),
    "chemistry": ("Kimyo", "Umumiy, anorganik va organik kimyo: davriy jadval, kimyoviy bog'lanish, reaksiyalar, eritmalar, hisoblash masalalari — DTM va milliy sertifikat testlari."),
    "biology": ("Biologiya", "Botanika, zoologiya, odam anatomiyasi, sitologiya, genetika, evolyutsiya va ekologiya — DTM va milliy sertifikat testlari."),
    "physics": ("Fizika", "Mexanika, molekulyar fizika, termodinamika, elektr va magnetizm, optika, atom va yadro fizikasi — formulali va chizmali DTM va sertifikat masalalari."),
}

AI_BOTS = [
    "Googlebot", "Google-Extended", "Bingbot", "YandexBot", "Applebot", "Applebot-Extended", "DuckDuckBot",
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "anthropic-ai",
    "PerplexityBot", "Perplexity-User", "CCBot", "cohere-ai", "Meta-ExternalAgent", "Amazonbot", "YouBot",
]
PRIVATE = ["/api/", "/dashboard", "/profile", "/billing", "/tests", "/tutor", "/onboarding", "/analytics",
           "/logout", "/auth/", "/certificate/", "/ielts/", "/block-test", "/guide", "/support/"]


def site() -> str:
    u = (os.getenv("SITE_BASE_URL") or "").strip().rstrip("/")
    return u if u.startswith("http") else "https://longouz.vercel.app"


# ---------------------------------------------------------------------------
# Tasdiqlash kodlari (admin paneldan) — 5 daqiqa keshlanadi
# ---------------------------------------------------------------------------
_VERIFY = {"t": 0.0, "v": {"google": "", "bing": "", "yandex": ""}}
_META_RE = re.compile(r'content\s*=\s*["\']([^"\']+)["\']', re.I)


def clean_code(raw: str) -> str:
    """'<meta name="google-site-verification" content="abc" />' yoki 'abc' -> 'abc'."""
    raw = (raw or "").strip()
    m = _META_RE.search(raw)
    if m:
        raw = m.group(1)
    raw = re.sub(r"^google-site-verification[:=]\s*", "", raw, flags=re.I)
    return re.sub(r"[^A-Za-z0-9_\-.]", "", raw)[:120]


async def refresh_verify(force: bool = False) -> dict:
    if not force and time.time() - _VERIFY["t"] < 300:
        return _VERIFY["v"]
    try:
        import database as db
        v = {k: clean_code(await db.get_setting("seo_verify_" + k, "") or os.getenv(f"SEO_{k.upper()}_VERIFY", ""))
             for k in ("google", "bing", "yandex")}
        _VERIFY.update(t=time.time(), v=v)
    except Exception:  # noqa: BLE001
        logger.debug("SEO tasdiqlash kodlari o'qilmadi", exc_info=True)
    return _VERIFY["v"]


def meta() -> dict:
    """Shablonlar uchun (sinxron): sayt manzili va tasdiqlash kodlari."""
    return {"site": site(), **_VERIFY["v"]}


# ---------------------------------------------------------------------------
# Fanlar katalogi (content paketlaridan — bazaga murojaat qilmaydi)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=1)
def catalog() -> dict:
    import content
    out: dict = {}
    for pk in content.load_packs():
        code = pk.get("subject")
        if code not in SUBJECT_INFO:
            continue
        item = out.setdefault(code, {"questions": set(), "topics": {}, "modes": set()})
        item["modes"].update(pk.get("modes") or [])
        counts: dict = {}
        for q in pk["questions"]:
            item["questions"].add(q["question"].strip().lower())
            counts[q["topic"]] = counts.get(q["topic"], 0) + 1
        for t in pk["topics"]:
            name = t["name"]
            g = int(t.get("grade") or 0)
            if name not in item["topics"]:
                item["topics"][name] = {"name": name, "grade": g, "count": counts.get(name, 0)}
            else:
                item["topics"][name]["count"] += counts.get(name, 0)
    res = {}
    for code, it in out.items():
        topics = sorted(it["topics"].values(), key=lambda x: (x["grade"] or 99,))
        by_grade: dict = {}
        for t in topics:
            by_grade.setdefault(t["grade"], []).append(t)
        res[code] = {"code": code, "slug": CODE2SLUG[code], "name": SUBJECT_INFO[code][0], "desc": SUBJECT_INFO[code][1],
                     "q": len(it["questions"]), "t": len(topics), "by_grade": sorted(by_grade.items(), key=lambda kv: kv[0] or 99),
                     "ielts": code == "english"}
    return res


def totals() -> tuple[int, int]:
    c = catalog()
    return sum(v["q"] for v in c.values()), sum(v["t"] for v in c.values())


# ---------------------------------------------------------------------------
# robots.txt / sitemap.xml / llms.txt / IndexNow kaliti
# ---------------------------------------------------------------------------
@router.get("/robots.txt", include_in_schema=False)
async def robots_txt():
    pub = ["Allow: /api/news", "Allow: /api/public/", "Allow: /api/site-stats"]   # bosh sahifa shularni yuklaydi — Google to'liq ko'rsin
    lines = ["# LongoUz — DTM 2026, milliy sertifikat va IELTS'ga onlayn tayyorgarlik platformasi", ""]
    for bot in AI_BOTS:
        lines += [f"User-agent: {bot}", "Allow: /"] + pub + [f"Disallow: {p}" for p in PRIVATE] + [""]
    lines += ["User-agent: *", "Allow: /"] + pub + [f"Disallow: {p}" for p in PRIVATE] + [
        "", f"Sitemap: {site()}/sitemap.xml", f"# AI uchun qisqa ma'lumot: {site()}/llms.txt", ""]
    return PlainTextResponse("\n".join(lines), headers={"Cache-Control": "public, max-age=3600"})


def public_urls() -> list[tuple[str, str, str]]:
    """(yo'l, changefreq, priority)"""
    urls = [("/", "daily", "1.0"), ("/subjects", "weekly", "0.9"), ("/about", "monthly", "0.8")]
    urls += [(f"/subjects/{s}", "weekly", "0.8") for s in SLUGS]
    urls += [("/register", "monthly", "0.6"), ("/login", "monthly", "0.4"),
             ("/verify", "monthly", "0.4"), ("/terms", "yearly", "0.2"), ("/privacy", "yearly", "0.2"),
             ("/llms.txt", "weekly", "0.3")]
    return urls


@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap_xml():
    base = site()
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, freq, pr in public_urls():
        body.append(f"  <url><loc>{base}{path}</loc><lastmod>{LASTMOD}</lastmod><changefreq>{freq}</changefreq><priority>{pr}</priority></url>")
    body.append("</urlset>")
    return Response("\n".join(body), media_type="application/xml", headers={"Cache-Control": "public, max-age=3600"})


def _llms(full: bool) -> str:
    base = site()
    q, t = totals()
    c = catalog()
    out = [
        "# LongoUz",
        "",
        "> LongoUz (longouz) — O'zbekistondagi o'quvchi va abituriyentlar uchun DTM 2026 test sinovlari, milliy sertifikat "
        "va IELTS imtihonlariga onlayn, bepul tayyorlanish platformasi. Sun'iy intellekt (AI) repetitor, 8 ta fan bo'yicha "
        f"{q:,} dan ortiq test savoli va {t} ta mavzu, DTM blok mock (189 ball tizimi), xatolar tahlili va sertifikatlar.".replace(f"{q:,}", f"{q:,}".replace(",", " ")),
        "",
        f"Sayt: {base}",
        "Til: o'zbek (lotin), ingliz va rus tili fanlari o'z tilida",
        "Narx: bepul tarif mavjud; Pro — 25 000 so'm/oy, Ultra — 40 000 so'm/oy (yillik to'lovda chegirma)",
        "Kimlar uchun: 9–11-sinf o'quvchilari, abituriyentlar, milliy sertifikat va IELTS topshiruvchilar",
        "",
        "## Asosiy imkoniyatlar",
        "- Mavzuli testlar: har bir fan sinflar (5–11) va mavzular bo'yicha tartiblangan, har bir savolda izoh bor",
        "- DTM blok mock: 90 savol — majburiy fanlar 3×10 (×1,1), 1-ixtisoslik 30 (×3,1), 2-ixtisoslik 30 (×2,1); maksimal 189 ball",
        "- AI repetitor (LongoAI): xatoni bosqichma-bosqich tushuntiradi, formulalar va chizmalar bilan javob beradi",
        "- IELTS: Reading, Writing va Speaking mashqlari, AI baholash",
        "- Natijalar tahlili, kunlik reja, QR kodli sertifikat",
        "",
        "## Fanlar",
    ]
    for code in ("native", "math", "history", "english", "russian", "chemistry", "biology", "physics"):
        s = c.get(code)
        if not s:
            continue
        out.append(f"- [{s['name']}]({base}/subjects/{s['slug']}): {s['q']} savol, {s['t']} mavzu. {s['desc']}")
    out += ["", "## Sahifalar",
            f"- [Bosh sahifa]({base}/)", f"- [Barcha fanlar]({base}/subjects)", f"- [Platforma haqida]({base}/about)",
            f"- [Ro'yxatdan o'tish (bepul)]({base}/register)",
            f"- [Sertifikatni tekshirish]({base}/verify)", ""]
    if full:
        out += ["## Mavzular (fan va sinf bo'yicha)", ""]
        for code in ("native", "math", "history", "english", "russian", "chemistry", "biology", "physics"):
            s = c.get(code)
            if not s:
                continue
            out.append(f"### {s['name']}")
            for g, items in s["by_grade"]:
                label = f"{g}-sinf" if g else "Umumiy"
                out.append(f"- {label}: " + "; ".join(f"{x['name']} ({x['count']})" for x in items))
            out.append("")
    return "\n".join(out) + "\n"


@router.get("/llms.txt", include_in_schema=False)
async def llms_txt():
    return PlainTextResponse(_llms(False), headers={"Cache-Control": "public, max-age=3600"})


@router.get("/llms-full.txt", include_in_schema=False)
async def llms_full_txt():
    return PlainTextResponse(_llms(True), headers={"Cache-Control": "public, max-age=3600"})


@router.get(f"/{INDEXNOW_KEY}.txt", include_in_schema=False)
async def indexnow_key():
    return PlainTextResponse(INDEXNOW_KEY)


@router.get("/google{code}.html", include_in_schema=False)
async def google_html_file(code: str):
    """Google Search Console «HTML fayl» usuli: googleXXXX.html. Kod admin paneldagi Google kodi bilan bir xil bo'lsa."""
    v = (await refresh_verify()).get("google", "")
    code = re.sub(r"[^A-Za-z0-9_\-]", "", code)
    if v and ("google" + code) == v.removesuffix(".html"):
        return PlainTextResponse(f"google-site-verification: google{code}.html")
    return PlainTextResponse("Not found", status_code=404)


async def ping_indexnow(paths: list[str] | None = None) -> dict:
    """Bing, Yandex, Seznam, Naver … — IndexNow orqali sahifalarni darhol yuboradi."""
    import aiohttp
    base = site()
    host = base.split("//", 1)[-1].split("/")[0]
    urls = [base + p for p in (paths or [u[0] for u in public_urls()])]
    payload = {"host": host, "key": INDEXNOW_KEY, "keyLocation": f"{base}/{INDEXNOW_KEY}.txt", "urlList": urls}
    res: dict = {}
    timeout = aiohttp.ClientTimeout(total=8)
    async with aiohttp.ClientSession(timeout=timeout) as s:
        for ep in ("https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow", "https://yandex.com/indexnow"):
            try:
                async with s.post(ep, json=payload, headers={"Content-Type": "application/json; charset=utf-8"}) as r:
                    res[ep.split("/")[2]] = r.status
            except Exception as e:  # noqa: BLE001
                res[ep.split("/")[2]] = f"xato: {type(e).__name__}"
    return {"urls": len(urls), "result": res}


async def auto_ping_once(version: str) -> None:
    """Har yangi versiyada bir marta (birinchi tashrifda) qidiruv tizimlariga xabar beradi."""
    try:
        import database as db
        if not os.getenv("VERCEL"):
            return
        if await db.get_setting("seo_pinged_version", "") == version:
            return
        await db.set_setting("seo_pinged_version", version)
        r = await asyncio.wait_for(ping_indexnow(), timeout=9)
        await db.set_setting("seo_last_ping", json.dumps({"at": int(time.time()), **r}, ensure_ascii=False))
        logger.info("IndexNow: %s", r)
    except Exception:  # noqa: BLE001
        logger.debug("IndexNow yuborilmadi", exc_info=True)


# ---------------------------------------------------------------------------
# JSON-LD (Google va AI uchun tuzilgan ma'lumot)
# ---------------------------------------------------------------------------
HOME_FAQ = [
    ("LongoUz nima?", "LongoUz — DTM 2026 test sinovlari, milliy sertifikat va IELTS imtihonlariga onlayn tayyorlanish platformasi. 8 ta fan bo'yicha minglab test savollari, AI repetitor va DTM blok mock bor."),
    ("LongoUz bepulmi?", "Ha. Ro'yxatdan o'tib, har bir mavzu bo'yicha bepul testlarni yechish mumkin. Pro (25 000 so'm/oy) va Ultra (40 000 so'm/oy) tariflarida savollar soni ko'payadi, AI repetitor va to'liq blok mock ochiladi."),
    ("Qaysi fanlar bor?", "Ona tili va adabiyot, matematika, tarix, ingliz tili, rus tili, kimyo, biologiya va fizika. Ingliz tilida IELTS Reading, Writing va Speaking ham bor."),
    ("Savollar haqiqiy imtihonga mosmi?", "Savollar DTM test sinovlari va milliy sertifikat dasturi (5–11-sinf darsliklari) asosida tuzilgan, har bir savolda izoh bor. Fizika, matematika va kimyoda chizmali masalalar ham mavjud."),
    ("DTM blok mock qanday hisoblanadi?", "90 ta savol: majburiy fanlar (ona tili, matematika, O'zbekiston tarixi) — har biri 10 tadan, ball ×1,1; 1-ixtisoslik fani 30 ta (×3,1); 2-ixtisoslik fani 30 ta (×2,1). Maksimal ball — 189."),
    ("AI repetitor nima qiladi?", "Xato qilingan savolni bosqichma-bosqich tushuntiradi, formulalar va chizmalar bilan javob beradi, mavzu bo'yicha qo'shimcha mashq tavsiya qiladi."),
]


def ld_json(obj) -> str:
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def home_ld() -> str:
    base = site()
    q, t = totals()
    org = {
        "@context": "https://schema.org", "@type": "EducationalOrganization", "@id": base + "/#org",
        "name": "LongoUz", "alternateName": ["LongoUz", "Longo UZ", "longouz", "Longo"], "url": base + "/",
        "logo": base + "/static/logo-owl.png", "image": base + "/static/logo-owl3d.png",
        "description": f"DTM 2026, milliy sertifikat va IELTS'ga AI yordamida bepul onlayn tayyorgarlik: 8 fan, {q} dan ortiq test savoli, {t} mavzu.",
        "areaServed": {"@type": "Country", "name": "Uzbekistan"}, "inLanguage": "uz",
        "knowsAbout": [v[0] for v in SUBJECT_INFO.values()] + ["DTM", "Milliy sertifikat", "IELTS", "Abituriyent"],
    }
    web = {"@context": "https://schema.org", "@type": "WebSite", "@id": base + "/#site", "name": "LongoUz",
           "alternateName": ["Longo UZ", "longouz"], "url": base + "/", "inLanguage": "uz", "publisher": {"@id": base + "/#org"}}
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "LongoUz", "url": base + "/",
           "applicationCategory": "EducationalApplication", "operatingSystem": "Web",
           "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "UZS", "name": "Bepul"},
                      {"@type": "Offer", "price": "25000", "priceCurrency": "UZS", "name": "Pro (oylik)"},
                      {"@type": "Offer", "price": "40000", "priceCurrency": "UZS", "name": "Ultra (oylik)"}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in HOME_FAQ]}
    return "\n".join(ld_json(x) for x in (org, web, app, faq))


def _crumbs(items: list[tuple[str, str]]) -> dict:
    base = site()
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": base + p} for i, (n, p) in enumerate(items)]}


# ---------------------------------------------------------------------------
# Ochiq sahifalar: /subjects, /subjects/<fan>, /about
# ---------------------------------------------------------------------------
def _templates():
    import main
    return main.templates


@router.get("/subjects", response_class=HTMLResponse)
async def fanlar_page(request: Request):
    await refresh_verify()
    c = catalog()
    q, t = totals()
    order = ("native", "math", "history", "english", "russian", "chemistry", "biology", "physics")
    subjects = [c[k] for k in order if k in c]
    ld = ld_json(_crumbs([("Bosh sahifa", "/"), ("Fanlar", "/subjects")])) + ld_json({
        "@context": "https://schema.org", "@type": "ItemList", "name": "LongoUz fanlari",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{site()}/subjects/{s['slug']}", "name": s["name"]} for i, s in enumerate(subjects)]})
    return _templates().TemplateResponse(request, "seo_page.html", {
        "kind": "fanlar", "subjects": subjects, "q_total": q, "t_total": t, "ld": ld,
        "page_title": "Fanlar | LongoUz",
        "page_desc": f"8 ta fan bo'yicha {q} dan ortiq bepul test savoli: ona tili, matematika, tarix, ingliz tili, rus tili, kimyo, biologiya, fizika. DTM 2026 va milliy sertifikatga onlayn tayyorgarlik.",
        "canonical": "/subjects",
    })


@router.get("/subjects/{slug}", response_class=HTMLResponse)
async def fan_page(request: Request, slug: str):
    if slug in OLD_SLUGS:
        return RedirectResponse(f"/subjects/{OLD_SLUGS[slug]}", status_code=301)
    code = SLUGS.get(slug) or ""
    if not code:
        return HTMLResponse("<h1>Sahifa topilmadi</h1><p><a href='/subjects'>Barcha fanlar</a></p>", status_code=404)
    await refresh_verify()
    s = catalog().get(code)
    if not s:
        return HTMLResponse("<h1>Sahifa topilmadi</h1>", status_code=404)
    others = [v for k, v in catalog().items() if k != code]
    course = {"@context": "https://schema.org", "@type": "Course", "name": f"{s['name']} — DTM 2026 va milliy sertifikatga tayyorgarlik",
              "description": s["desc"], "inLanguage": "uz", "isAccessibleForFree": True,
              "provider": {"@type": "EducationalOrganization", "name": "LongoUz", "url": site() + "/"},
              "numberOfCredits": s["t"], "educationalLevel": "5–11-sinf, abituriyent",
              "teaches": [t["name"] for _, items in s["by_grade"] for t in items][:40]}
    ld = ld_json(_crumbs([("Bosh sahifa", "/"), ("Fanlar", "/subjects"), (s["name"], f"/subjects/{s['slug']}")])) + ld_json(course)
    return _templates().TemplateResponse(request, "seo_page.html", {
        "kind": "fan", "s": s, "others": others, "ld": ld,
        "page_title": f"{s['name']} | LongoUz",
        "page_desc": f"{s['name']}: {s['q']} ta test savoli, {s['t']} ta mavzu, har bir savolda izoh. {s['desc'][:150]}",
        "canonical": f"/subjects/{s['slug']}",
    })


@router.get("/about", response_class=HTMLResponse)
async def haqida_page(request: Request):
    await refresh_verify()
    q, t = totals()
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in HOME_FAQ]}
    ld = ld_json(_crumbs([("Bosh sahifa", "/"), ("Platforma haqida", "/about")])) + ld_json(faq)
    return _templates().TemplateResponse(request, "seo_page.html", {
        "kind": "haqida", "faq": HOME_FAQ, "q_total": q, "t_total": t, "subjects": list(catalog().values()), "ld": ld,
        "page_title": "Haqida | LongoUz",
        "page_desc": "LongoUz nima, kimlar uchun, qanday ishlaydi: mavzuli testlar, DTM blok mock (189 ball), AI repetitor, IELTS, tariflar va savol-javoblar.",
        "canonical": "/about",
    })


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def today() -> str:
    return date.today().isoformat()
