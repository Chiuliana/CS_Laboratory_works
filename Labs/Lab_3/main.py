from playfair_cipher import encrypt_playfair, decrypt_playfair

if __name__ == "__main__":
    while True:
        print("Playfair Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key (at least 7 characters): ")
            if len(key) < 7:
                print("Key must be at least 7 characters long.")
                continue
            ciphertext = encrypt_playfair(plaintext, key)
            print("Ciphertext:", ciphertext)
        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            key = input("Enter the key (at least 7 characters): ")
            if len(key) < 7:
                print("Key must be at least 7 characters long.")
                continue
            plaintext = decrypt_playfair(ciphertext, key)
            print("Plaintext:", plaintext)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
