def create_playfair_matrix(key: str):
    key = key.upper().replace('J', 'I')
    seen = []
    for c in key:
        if c.isalpha() and c not in seen:
            seen.append(c)
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in seen:
            seen.append(c)
    return [seen[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(text: str, key: str) -> str:
    matrix = create_playfair_matrix(key)
    text = ''.join(c for c in text.upper() if c.isalpha()).replace('J', 'I')

    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i+1]:
            pairs.append(text[i] + 'X')
            i += 1
        else:
            pairs.append(text[i:i+2])
            i += 2

    result = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:  # même ligne
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # même colonne
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # rectangle
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def playfair_decrypt(text: str, key: str) -> str:
    matrix = create_playfair_matrix(key)
    text = ''.join(c for c in text.upper() if c.isalpha()).replace('J', 'I')
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]

    result = ""
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:  # même ligne → lettre à gauche
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # même colonne → lettre au-dessus
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # rectangle
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def process(option, text, key=None):
    if option == 0:  # Chiffrer
        return playfair_encrypt(text, key)
    else:            # Déchiffrer
        return playfair_decrypt(text, key)
