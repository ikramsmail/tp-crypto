import random, base64
from sympy import randprime

def text_to_int(message: str) -> int:
    return int.from_bytes(message.encode('utf-8'), 'big')

def int_to_text(n: int) -> str:
    length = (n.bit_length() + 7) // 8
    return n.to_bytes(length, 'big').decode('utf-8')

def generate_rsa_keys(bits=128):  # petite taille pour tester rapidement
    p = randprime(2**(bits//2 - 1), 2**(bits//2))
    q = randprime(2**(bits//2 - 1), 2**(bits//2))
    while p == q:
        q = randprime(2**(bits//2 - 1), 2**(bits//2))
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi_n)
    return (n, d), (n, e)

def encrypt_text(message, public_key):
    n, e = public_key
    m_int = text_to_int(message)
    c = pow(m_int, e, n)
    return base64.b64encode(c.to_bytes((c.bit_length() + 7) // 8, 'big')).decode('utf-8')

def decrypt_text(cipher_b64, private_key):
    n, d = private_key
    c_bytes = base64.b64decode(cipher_b64)
    c_int = int.from_bytes(c_bytes, 'big')
    m_int = pow(c_int, d, n)
    return int_to_text(m_int)

# 🔹 Génération des clés une seule fois
private_key, public_key = generate_rsa_keys(bits=128)

def process(option, text, key=None):
    global private_key, public_key
    if option == 0:  # Chiffrer
        return encrypt_text(text, public_key)
    else:            # Déchiffrer
        return decrypt_text(text, private_key)
