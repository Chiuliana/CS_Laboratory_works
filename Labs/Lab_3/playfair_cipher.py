def create_playfair_matrix(key):
    # Creates the Playfair cipher matrix from the given key.

    # Remove duplicate letters from the key
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))

    # Initialize the 5x5 matrix
    matrix = [['' for _ in range(5)] for _ in range(5)]

    # Fill the matrix with the key and the remaining letters
    row, col = 0, 0
    for char in key:
        if char == 'J':
            char = 'I'
        matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1

    # Fill the remaining cells with the unused letters
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in key:
            matrix[row][col] = char
            col += 1
            if col == 5:
                col = 0
                row += 1

    return matrix
    pass

def encrypt_playfair(plaintext, key):
    # Encrypts the plaintext using the Playfair cipher with the given key.

    pass

def decrypt_playfair(ciphertext, key):
    # Decrypts the ciphertext using the Playfair cipher with the given key.

    pass