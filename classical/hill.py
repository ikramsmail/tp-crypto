import numpy as np

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det = det % modulus
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("La matrice n'est pas inversible modulo {}".format(modulus))

    n = matrix.shape[0]
    cofactors = np.zeros((n, n), dtype=int)
    for r in range(n):
        for c in range(n):
            minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
            cofactors[r, c] = ((-1) ** (r + c)) * int(round(np.linalg.det(minor)))
    adjugate = cofactors.T

    return (det_inv * adjugate) % modulus

def hill_encrypt(text: str, key_matrix: np.ndarray) -> str:
    n = key_matrix.shape[0]
    text = ''.join(c for c in text if c.isalpha()).lower()
    while len(text) % n != 0:
        text += 'x'

    result = ""
    for i in range(0, len(text), n):
        vector = [ord(text[i+j]) - ord('a') for j in range(n)]
        encrypted_vector = np.dot(key_matrix, vector) % 26
        result += ''.join(chr(int(num) + ord('a')) for num in encrypted_vector)
    return result

def hill_decrypt(text: str, key_matrix: np.ndarray) -> str:
    n = key_matrix.shape[0]
    inv_matrix = matrix_mod_inv(key_matrix, 26)
    text = ''.join(c for c in text if c.isalpha()).lower()
    while len(text) % n != 0:
        text += 'x'

    result = ""
    for i in range(0, len(text), n):
        vector = [ord(text[i+j]) - ord('a') for j in range(n)]
        decrypted_vector = np.dot(inv_matrix, vector) % 26
        result += ''.join(chr(int(num) + ord('a')) for num in decrypted_vector)

    # Supprimer le padding éventuel
    return result.rstrip("x")

def process(option, text, key=None):
    # Clé peut être une chaîne "3,2,5,7" ou une matrice [[3,2],[5,7]]
    if isinstance(key, str):
        numbers = list(map(int, key.split(",")))
        n = int(len(numbers) ** 0.5)
        key_matrix = np.array(numbers).reshape(n, n)
    elif isinstance(key, (list, np.ndarray)):
        key_matrix = np.array(key)
    else:
        raise ValueError("Format de clé non reconnu")

    if option == 0:  # Chiffrer
        return hill_encrypt(text, key_matrix)
    else:            # Déchiffrer
        return hill_decrypt(text, key_matrix)
