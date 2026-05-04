from numpy import gcd

def inverse_modulaire(a: int, m: int):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text: str, a: int, b: int) -> str:
    """Chiffrement affine E(x) = (ax + b) mod 26."""
    if gcd(a, 26) != 1:
        raise ValueError("La valeur de 'a' doit être première avec 26")

    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            x = ord(char) - ascii_offset
            y = (a * x + b) % 26
            result += chr(y + ascii_offset)
        else:
            result += char
    return result

def affine_decrypt(text: str, a: int, b: int) -> str:
    """Déchiffrement affine D(y) = a^(-1) * (y - b) mod 26."""
    a_inv = inverse_modulaire(a, 26)
    if a_inv is None:
        raise ValueError("La valeur de 'a' doit être première avec 26")

    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            y = ord(char) - ascii_offset
            x = (a_inv * (y - b)) % 26
            result += chr(x + ascii_offset)
        else:
            result += char
    return result

def process(option, text, key=None):
    #Ici key peut être un tuple (a,b) ou une chaîne "a,b"
    if isinstance(key, tuple):
        a, b = key
    else:
        a, b = map(int, key.split(","))

    if option == 0:  # Chiffrer
        return affine_encrypt(text, a, b)
    else:            # Déchiffrer
        return affine_decrypt(text, a, b)
