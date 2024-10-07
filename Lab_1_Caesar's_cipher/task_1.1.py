def caesar_cipher(text, key, mode='encrypt'):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "").strip()

    for char in text:
        if char in alphabet:  # Only process valid characters
            idx = alphabet.index(char)
            if mode == 'encrypt':
                new_idx = (idx + key) % 26  # Encryption formula
            else:
                new_idx = (idx - key) % 26  # Decryption formula
            result += alphabet[new_idx]
        # Ignore non-alphabet characters as per the instructions

    return result


# User input
if __name__ == "__main__":
    while True:
        text = input("Enter the text (or 'q' to exit): ")
        if text.lower() == 'q':
            break

        # Get a valid key
        while True:
            try:
                key = int(input("Enter the key (1-25): "))
                if 1 <= key <= 25:
                    break
                else:
                    print("Invalid key. Please enter a value between 1 and 25.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 25.")

        # Get the operation mode
        while True:
            mode_input = input("Enter 'encrypt' (or 'en') or 'decrypt' (or 'de'): ").strip().lower()
            if mode_input in ['encrypt', 'en']:
                mode = 'encrypt'
                break
            elif mode_input in ['decrypt', 'de']:
                mode = 'decrypt'
                break
            else:
                print("Invalid mode selected. Please enter 'encrypt' (or 'en') or 'decrypt' (or 'de').")

        # Get the result
        output = caesar_cipher(text, key, mode)
        print(f"Output: {output}")
