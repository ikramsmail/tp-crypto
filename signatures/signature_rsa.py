import hashlib

def generer_cles_rsa_simple(p=61, q=53, e=17):
    n = p * q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    public = (n, e)      # clé publique = 2 valeurs
    private = (n, d)     # clé privée
    return public, private

def signer_rsa_simple(message, private_key):
    n, d = private_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    return pow(h, d, n)

def verifier_rsa_simple(message, signature, public_key):
    n, e = public_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    h_check = pow(signature, e, n)
    # Comparer modulo n
    return (h % n) == h_check

def process(option, text, key=None):
    if option == 0:  # Signer
        public, private = generer_cles_rsa_simple()
        signature = signer_rsa_simple(text, private)
        return {"signature": signature, "public_key": public}
    elif option == 1:  # Vérifier
        signature = key["signature"]
        public_key = key["public_key"]
        return "Signature valide ✅" if verifier_rsa_simple(text, signature, public_key) else "Signature invalide ❌"

