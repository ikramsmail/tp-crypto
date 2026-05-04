import random
import hashlib

def generer_cles_dsa_simple(p=None, q=None, g=None):
    """Génération de clés DSA simplifiée."""
    if p is None:
        p = 23
        q = 11
        g = 2
    x = random.randint(1, q-1)   # Clé privée
    y = pow(g, x, p)             # Clé publique
    return (p, q, g, x), (p, q, g, y)

def signer_dsa_simple(message: str, private_key) -> tuple:
    """Signature DSA simplifiée."""
    p, q, g, x = private_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    while True:
        k = random.randint(1, q-1)
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = pow(k, -1, q)
        s = (k_inv * (h + x * r)) % q
        if s != 0:
            break
    return r, s

def verifier_dsa_simple(message: str, signature: tuple, public_key) -> bool:
    """Vérification DSA simplifiée."""
    p, q, g, y = public_key
    r, s = signature
    if not (0 < r < q and 0 < s < q):
        return False
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    w = pow(s, -1, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q
    return v == r

def process(option, text, key=None):
    """
    option = 0 → Signer
    option = 1 → Vérifier
    """
    if option == 0:  # Signer
        priv, pub = generer_cles_dsa_simple()
        signature = signer_dsa_simple(text, priv)
        return {"signature": signature, "public_key": pub}

    else:  # Vérifier
        try:
            signature = key["signature"]
            public_key = key["public_key"]
            valid = verifier_dsa_simple(text, signature, public_key)
            return "Signature valide ✅" if valid else "Signature invalide ❌"
        except Exception as e:
            return f"Erreur vérification : {e}"
