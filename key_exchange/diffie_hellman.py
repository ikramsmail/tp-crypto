import random

def generate_keys(p=23, g=5):
    a = random.randint(2, p-2)  # secret de A
    b = random.randint(2, p-2)  # secret de B
    A = pow(g, a, p)            # clé publique de A
    B = pow(g, b, p)            # clé publique de B
    return (p, g, A, B), (a, b)

def compute_shared_secret(public_params, private_secrets):
    p, g, A, B = public_params
    a, b = private_secrets
    secret_a = pow(B, a, p)
    secret_b = pow(A, b, p)
    return secret_a if secret_a == secret_b else None

def process(option, text, key=None):
    p = 23
    g = 5
    public_params, private_secrets = generate_keys(p, g)
    shared_secret = compute_shared_secret(public_params, private_secrets)
    if shared_secret is None:
        return "Erreur : les secrets ne correspondent pas."
    return str(shared_secret)  # retourne juste la clé partagée
