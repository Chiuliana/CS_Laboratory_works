from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import padding
import os


def generate_user_key(username):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Save private key
    private_key_file = f"{username}_key.pem"
    with open(private_key_file, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    # Extract and save public key
    public_key_file = f"{username}_public_key.pem"
    public_key = private_key.public_key()
    with open(public_key_file, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    print(f"Keys generated: {private_key_file} (private), {public_key_file} (public)")
    return private_key_file, public_key_file


def create_test_file():
    file_to_sign = "document.txt"
    if not os.path.exists(file_to_sign):
        with open(file_to_sign, "w") as doc:
            doc.write("This is a test document for signing.")
        print(f"Test file created: {file_to_sign}")
    return file_to_sign


def sign_file(private_key_path, file_to_sign):
    # Load private key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    # Read file to sign
    with open(file_to_sign, "rb") as f:
        data = f.read()

    # Create signature
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        SHA256(),
    )

    # Save signature
    sig_file = f"{file_to_sign}.sig"
    with open(sig_file, "wb") as sig:
        sig.write(signature)
    print(f"Signature created: {sig_file}")


if __name__ == "__main__":
    # Generate keys
    username = "user1"
    private_key, public_key = generate_user_key(username)

    # Create a test document
    file_to_sign = create_test_file()

    # Sign the document
    sign_file(private_key, file_to_sign)
