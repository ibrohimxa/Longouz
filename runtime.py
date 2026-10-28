"""LongoUZ — ishlash muhiti (lokal kompyuter yoki Vercel serverless) haqida yagona joy."""
import os
import hashlib

IS_VERCEL = bool(os.getenv("VERCEL") or os.getenv("VERCEL_ENV") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"))


def _is_local_url(url: str) -> bool:
    u = (url or "").lower()
    return not u or any(h in u for h in ("localhost", "127.0.0.1", "0.0.0.0", "192.168.", "10.0.", "172.16."))


def site_base_url() -> str:
    """Sayt asosiy manzili: SITE_BASE_URL (agar haqiqiy bo'lsa) -> Vercel domeni -> lokal."""
    configured = (os.getenv("SITE_BASE_URL") or "").strip().rstrip("/")
    if IS_VERCEL and _is_local_url(configured):
        host = os.getenv("VERCEL_PROJECT_PRODUCTION_URL") or os.getenv("VERCEL_URL") or ""
        if host:
            return "https://" + host.replace("https://", "").rstrip("/")
    return configured or "http://127.0.0.1:6060"


def stable_secret_seed() -> str:
    """WEB_SECRET_KEY berilmagan serverless holat uchun barqaror (har instansda bir xil) kalit manbai."""
    raw = (os.getenv("DATABASE_URL", "") + os.getenv("ADMIN_PASSWORD", "") + os.getenv("VERCEL_PROJECT_ID", "longouz"))
    return hashlib.sha256(("longouz-secret|" + raw).encode()).hexdigest()
