from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key


def verify_signature(public_key_path, file_to_verify, signature_file):
    with open(public_key_path, "rb") as pub_key_file:
        public_key = load_pem_public_key(pub_key_file.read())

    with open(file_to_verify, "rb") as f:
        data = f.read()

    with open(signature_file, "rb") as sig_file:
        signature = sig_file.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            SHA256(),
        )
        print("Signature is valid.")
    except Exception as e:
        print(f"Invalid signature: {e}")


if __name__ == "__main__":
    # Update these paths if needed
    public_key_path = "user1_public_key.pem"  # Public key file
    file_to_verify = "document.txt"          # Original document
    signature_file = "document.txt.sig"      # Signature file

    verify_signature(public_key_path, file_to_verify, signature_file)
