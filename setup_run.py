"""LongoUZ — o'rnatish va ishga tushirish (Windows / Linux / macOS).

Qadamlar: 1) .venv yaratadi  2) requirements.txt dagi kutubxonalarni BIR-BIRLAB
o'rnatadi (qaysi biri xato bersa, aniq ko'rinadi)  3) importlarni tekshiradi
4) .env ni tekshiradi  5) serverni ishga tushiradi (HTTP 6060, HTTPS 6600).
Faqat o'rnatish: python setup_run.py --no-run
"""
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
PY = VENV / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")

# pip nomi -> import nomi
IMPORT_NAMES = {
    "python-multipart": "multipart", "python-jose": "jose", "python-dotenv": "dotenv",
    "google-genai": "google.genai", "qrcode": "qrcode", "edge-tts": "edge_tts",
    "pypdf": "pypdf", "bcrypt": "bcrypt", "aiosqlite": "aiosqlite", "asyncpg": "asyncpg",
    "sqlalchemy": "sqlalchemy", "greenlet": "greenlet", "anthropic": "anthropic", "aiohttp": "aiohttp",
    "reportlab": "reportlab", "slowapi": "slowapi", "fastapi": "fastapi",
    "uvicorn": "uvicorn", "jinja2": "jinja2",
}


def run(cmd, **kw):
    return subprocess.run([str(c) for c in cmd], cwd=ROOT, **kw)


def requirements() -> list[str]:
    lines = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
    extra = ROOT / "requirements-local.txt"
    if extra.exists():
        lines += extra.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def pip_name(req: str) -> str:
    for sep in ("[", ">", "<", "=", "~", "!"):
        req = req.split(sep)[0]
    return req.strip().lower()


def main() -> int:
    if sys.version_info < (3, 10):
        print("XATO: Python 3.10 yoki yangisi kerak. https://www.python.org/downloads/")
        return 1
    if not PY.exists():
        print("[1/5] Virtual muhit (.venv) yaratilmoqda...")
        venv.create(VENV, with_pip=True)
    else:
        print("[1/5] .venv mavjud.")

    print("[2/5] pip yangilanmoqda...")
    run([PY, "-m", "pip", "install", "--upgrade", "pip", "-q"])

    reqs = requirements()
    failed = []
    print(f"[3/5] {len(reqs)} ta kutubxona birma-bir o'rnatilmoqda:")
    for i, req in enumerate(reqs, 1):
        print(f"   ({i}/{len(reqs)}) {req} ...", end=" ", flush=True)
        r = run([PY, "-m", "pip", "install", req, "-q", "--disable-pip-version-check"],
                capture_output=True, text=True)
        if r.returncode == 0:
            print("OK")
        else:
            print("XATO")
            failed.append((req, (r.stderr or r.stdout).strip().splitlines()[-1:]))
    if failed:
        print("\nO'rnatilmay qolganlar:")
        for req, err in failed:
            print(f"  - {req}: {' '.join(err)}")
        print("Internet aloqasini tekshirib, shu faylni qayta ishga tushiring.")
        return 1

    print("[4/5] Importlar tekshirilmoqda...")
    bad = []
    for req in reqs:
        mod = IMPORT_NAMES.get(pip_name(req), pip_name(req).replace("-", "_"))
        if run([PY, "-c", f"import {mod}"], capture_output=True).returncode != 0:
            bad.append(mod)
            print(f"   {mod}: XATO")
    if bad:
        return 1
    print("   Hammasi joyida.")

    env = ROOT / ".env"
    if not env.exists():
        print("\n[!] .env topilmadi. Ilova ishga tushadi, lekin AI, Google kirish va admin ishlamaydi.")
        print("    .env faylini main.py yoniga qo'ying (ADMIN_PASSWORD, GEMINI_API_KEY, ...).")
    else:
        text = env.read_text(encoding="utf-8")
        for key in ("ADMIN_PASSWORD", "GEMINI_API_KEY", "GOOGLE_CLIENT_ID", "TURNSTILE_SITE_KEY"):
            ok = any(ln.startswith(key + "=") and ln.split("=", 1)[1].strip() for ln in text.splitlines())
            print(f"   {key}: {'bor' if ok else 'BO`SH'}")

    if "--no-run" in sys.argv:
        print("[5/5] O'rnatish tugadi. Ishga tushirish: python main.py (.venv ichida).")
        return 0
    print("\n[5/5] Server ishga tushmoqda: http://localhost:6060  (to'xtatish: Ctrl+C)\n")
    return run([PY, "main.py"]).returncode


if __name__ == "__main__":
    sys.exit(main())
