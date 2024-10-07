def generate_permuted_alphabet(keyword):
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create a set of unique characters from the keyword
    unique_chars = []
    for char in keyword:
        if char not in unique_chars and char in alphabet:
            unique_chars.append(char)

    # Create the permuted alphabet
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)

    return ''.join(unique_chars)


def caesar_cipher_with_two_keys(text, key1, key2, mode='encrypt'):
    # Generate the permuted alphabet from key2
    permuted_alphabet = generate_permuted_alphabet(key2)

    result = ""
    text = text.upper().replace(" ", "").strip()  # Normalize input text

    for char in text:
        if char in permuted_alphabet:  # Only process valid characters
            idx = permuted_alphabet.index(char)
            if mode == 'encrypt':
                new_idx = (idx + key1) % 26  # Encryption formula
            else:
                new_idx = (idx - key1) % 26  # Decryption formula
            result += permuted_alphabet[new_idx]
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


# User input
if __name__ == "__main__":
    while True:
        text = input("Enter the text (or 'q' to exit): ")
        if text.lower() == 'q':
            break

        # Get a valid key 1
        while True:
            try:
                key1 = int(input("Enter the key (1-25): "))
                if 1 <= key1 <= 25:
                    break
                else:
                    print("Invalid key. Please enter a value between 1 and 25.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 25.")

        # Get a valid key 2
        while True:
            key2 = input("Enter the keyword (at least 7 letters): ").strip()
            if len(key2) >= 7 and key2.isalpha():
                break
            else:
                print("Invalid keyword. Please enter a valid keyword of at least 7 letters.")

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
        output = caesar_cipher_with_two_keys(text, key1, key2, mode)
        print(f"Output: {output}")
