import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime


def generate_user_key(username):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    filename = f"{username}_key.pem"
    with open(filename, "wb") as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    return filename


def sign_file(private_key_path, file_to_sign):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    with open(file_to_sign, "rb") as f:
        data = f.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        SHA256(),
    )

    sig_file = f"{file_to_sign}.sig"
    with open(sig_file, "wb") as sig:
        sig.write(signature)

    print(f"Signature saved to {sig_file}")


if __name__ == "__main__":
    user_key = generate_user_key("user1")
    print(f"Generated user key: {user_key}")

    file_to_sign = "document.txt"
    if not os.path.exists(file_to_sign):
        with open(file_to_sign, "w") as doc:
            doc.write("This is a test document.")

    sign_file(user_key, file_to_sign)
