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

def format_plaintext(plaintext):
    # Formats plaintext to split into pairs and insert 'X' between duplicate letters.
    formatted = ''
    i = 0
    while i < len(plaintext):
        formatted += plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            formatted += 'X'
        elif i + 1 < len(plaintext):
            formatted += plaintext[i + 1]
            i += 1
        i += 1
    if len(formatted) % 2 != 0:
        formatted += 'X'
    return formatted

def encrypt_playfair(plaintext, key):
    # Encrypts the plaintext using the Playfair cipher with the given key.

    # Remove non-alphabetic characters and convert to uppercase
    plaintext = ''.join(char.upper() for char in plaintext if char.isalpha())
    plaintext = format_plaintext(plaintext)

    # Create the Playfair matrix
    matrix = create_playfair_matrix(key)

    # Split the plaintext into pairs
    pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    plaintext = ''

    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i][j] == pair[1]:
                    row2, col2 = i, j
        if row1 == row2:
            plaintext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext

def decrypt_playfair(ciphertext, key):
    # Decrypts the ciphertext using the Playfair cipher with the given key.

    # Create the Playfair matrix
    matrix = create_playfair_matrix(key)

    # Split the ciphertext into pairs
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''

    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i][j] == pair[1]:
                    row2, col2 = i, j
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext.replace('X', '')