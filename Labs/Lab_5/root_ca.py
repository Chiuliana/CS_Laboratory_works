from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509 import (
    CertificateBuilder, Name, NameAttribute, random_serial_number,
    BasicConstraints
)
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta, timezone


def generate_root_ca():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )

    # Save private key
    with open("root_ca_key.pem", "wb") as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    # Build certificate
    subject = issuer = Name([
        NameAttribute(NameOID.COUNTRY_NAME, "MD"),
        NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Chisinau"),
        NameAttribute(NameOID.LOCALITY_NAME, "Chisinau"),
        NameAttribute(NameOID.ORGANIZATION_NAME, "Lab5PKI"),
        NameAttribute(NameOID.COMMON_NAME, "Lab5 Root CA"),
    ])

    certificate = (
        CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(random_serial_number())
        .not_valid_before(datetime.now(timezone.utc))
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=3650))
        .add_extension(
            BasicConstraints(ca=True, path_length=None),
            critical=True,
        )
        .sign(private_key, SHA256(), default_backend())
    )

    # Save certificate
    with open("root_ca_cert.pem", "wb") as cert_file:
        cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))


if __name__ == "__main__":
    generate_root_ca()
