import random

def generate_keys(p=23):
    g = 5
    x = random.randint(2, p-2)  # clé privée
    y = pow(g, x, p)            # clé publique
    return (p, g, y), x

def elgamal_encrypt(m_int, public_key):
    p, g, y = public_key
    k = random.randint(2, p-2)
    c1 = pow(g, k, p)
    c2 = (m_int * pow(y, k, p)) % p
    return (c1, c2)

def elgamal_decrypt(cipher, private_key, p):
    c1, c2 = cipher
    s = pow(c1, private_key, p)
    m_int = (c2 * pow(s, -1, p)) % p
    return m_int

p = 23
public_key, private_key = generate_keys(p)

def process(option, text, key=None):
    if option == 0:  # Chiffrer
        m_int = int.from_bytes(text.encode(), "big")
        cipher = elgamal_encrypt(m_int, public_key)
        return str(cipher)  

    else:  # Déchiffrer
        try:
            c1, c2 = eval(text)  # texte sous forme "(c1, c2)"
            m_int = elgamal_decrypt((c1, c2), private_key, p)
            return m_int.to_bytes((m_int.bit_length() + 7) // 8, "big").decode()
        except Exception as e:
            return f"Erreur déchiffrement : {e}"
