"""LAN uchun o'z-o'zidan imzolangan HTTPS sertifikat (telefonda mikrofon ishlashi uchun)."""
from __future__ import annotations

import datetime
import ipaddress
import logging
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

logger = logging.getLogger(__name__)


def ensure_self_signed_cert(cert_dir: Path, lan_ips: list[str]) -> tuple[Path, Path]:
    """Sertifikat mavjud va barcha IP'larni qamrasa qayta ishlatadi, aks holda yangisini yaratadi."""
    cert_dir.mkdir(parents=True, exist_ok=True)
    cert_path = cert_dir / "longouz.crt"
    key_path = cert_dir / "longouz.key"
    ips_path = cert_dir / "ips.txt"
    wanted = ",".join(sorted(set(lan_ips)))

    if cert_path.exists() and key_path.exists() and ips_path.exists() and ips_path.read_text() == wanted:
        return cert_path, key_path

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "LongoUZ local")])
    alt_names: list[x509.GeneralName] = [x509.DNSName("localhost"), x509.IPAddress(ipaddress.ip_address("127.0.0.1"))]
    for ip in lan_ips:
        try:
            alt_names.append(x509.IPAddress(ipaddress.ip_address(ip)))
        except ValueError:
            logger.warning("Noto'g'ri IP o'tkazib yuborildi: %s", ip)
    now = datetime.datetime.now(datetime.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=1))
        .not_valid_after(now + datetime.timedelta(days=825))
        .add_extension(x509.SubjectAlternativeName(alt_names), critical=False)
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(key, hashes.SHA256())
    )
    key_path.write_bytes(key.private_bytes(
        serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()
    ))
    cert_path.write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    ips_path.write_text(wanted)
    return cert_path, key_path
