def create_playfair_matrix(key):
    # Romanian alphabet with specific characters included
    alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSTȘTUVXYZ"

    # Remove duplicate letters from the key and convert to uppercase
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))

    # Initialize the 6x6 matrix for the Romanian alphabet
    matrix = [['' for _ in range(6)] for _ in range(6)]

    # Fill the matrix with the key and the remaining letters
    row, col = 0, 0
    for char in key:
        if char in alphabet:
            matrix[row][col] = char
            col += 1
            if col == 6:
                col = 0
                row += 1

    # Fill the remaining cells with unused letters
    for char in alphabet:
        if char not in key:
            matrix[row][col] = char
            col += 1
            if col == 6:
                col = 0
                row += 1

    return matrix


def format_plaintext(plaintext):
    # Formats plaintext to split into pairs and insert 'X' between duplicate letters
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
    # Encrypts the plaintext using the Playfair cipher with the given key

    # Remove non-alphabetic characters and convert to uppercase
    plaintext = ''.join(char.upper() for char in plaintext if char.isalpha())
    plaintext = format_plaintext(plaintext)

    # Create the Playfair matrix
    matrix = create_playfair_matrix(key)

    # Split the plaintext into pairs
    pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
    ciphertext = ''

    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i in range(6):
            for j in range(6):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i][j] == pair[1]:
                    row2, col2 = i, j
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 6][col1] + matrix[(row2 + 1) % 6][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext


def decrypt_playfair(ciphertext, key):
    # Decrypts the ciphertext using the Playfair cipher with the given key

    # Create the Playfair matrix
    matrix = create_playfair_matrix(key)

    # Split the ciphertext into pairs
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ''

    for pair in pairs:
        row1, col1 = None, None
        row2, col2 = None, None
        for i in range(6):
            for j in range(6):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i][j] == pair[1]:
                    row2, col2 = i, j
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 6][col1] + matrix[(row2 - 1) % 6][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext.replace('X', '')