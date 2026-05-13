import random, hashlib

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def generer_cles_elgamal_simple(p=467, g=2):
    x = random.randint(1, p-2)
    y = pow(g, x, p)
    public = (p, g, y)
    private = (p, g, x)
    return private, public

def signer_elgamal_simple(message, private_key):
    p, g, x = private_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % (p-1)
    while True:
        k = random.randint(1, p-2)
        if gcd(k, p-1) != 1: continue
        r = pow(g, k, p)
        k_inv = pow(k, -1, p-1)
        s = (k_inv * (h - x*r)) % (p-1)
        if s != 0: break
    return r, s

def verifier_elgamal_simple(message, signature, public_key):
    p, g, y = public_key
    r, s = signature
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % (p-1)
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, h, p) % p
    return v1 == v2

def process(option, text, key=None):
    if option == 0:  # Signer
        priv, pub = generer_cles_elgamal_simple()
        signature = signer_elgamal_simple(text, priv)
        return {"signature": signature, "public_key": pub}
    elif option == 1:  # Vérifier
        signature = key["signature"]
        public_key = key["public_key"]
        return "Signature valide ✅" if verifier_elgamal_simple(text, signature, public_key) else "Signature invalide ❌"
