import struct

def rotl(x, y):
    return ((x << (y & 31)) | (x >> (32 - (y & 31)))) & 0xffffffff

def rotr(x, y):
    return ((x >> (y & 31)) | (x << (32 - (y & 31)))) & 0xffffffff

def rc6_key_schedule(key: bytes, w=32, r=20):
    u = w // 8
    c = max(1, len(key) // u)
    L = [0] * c
    for i in range(len(key)-1, -1, -1):
        L[i // u] = (L[i // u] << 8) + key[i]

    Pw, Qw = 0xB7E15163, 0x9E3779B9
    S = [0] * (2*r + 4)
    S[0] = Pw
    for i in range(1, 2*r+4):
        S[i] = (S[i-1] + Qw) & 0xffffffff

    A = B = i = j = 0
    for k in range(3 * max(c, len(S))):
        A = S[i] = rotl((S[i] + A + B) & 0xffffffff, 3)
        B = L[j] = rotl((L[j] + A + B) & 0xffffffff, (A + B) & 31)
        i = (i + 1) % len(S)
        j = (j + 1) % c
    return S

def rc6_encrypt_block(block, S, r=20):
    A, B, C, D = block
    B = (B + S[0]) & 0xffffffff
    D = (D + S[1]) & 0xffffffff
    for i in range(1, r+1):
        t = rotl(B * (2*B + 1) & 0xffffffff, 5)
        u = rotl(D * (2*D + 1) & 0xffffffff, 5)
        A = (rotl(A ^ t, u) + S[2*i]) & 0xffffffff
        C = (rotl(C ^ u, t) + S[2*i+1]) & 0xffffffff
        A, B, C, D = B, C, D, A
    A = (A + S[2*r+2]) & 0xffffffff
    C = (C + S[2*r+3]) & 0xffffffff
    return A, B, C, D

def rc6_decrypt_block(block, S, r=20):
    A, B, C, D = block
    C = (C - S[2*r+3]) & 0xffffffff
    A = (A - S[2*r+2]) & 0xffffffff
    for i in range(r, 0, -1):
        A, B, C, D = D, A, B, C
        t = rotl(B * (2*B + 1) & 0xffffffff, 5)
        u = rotl(D * (2*D + 1) & 0xffffffff, 5)
        C = rotr((C - S[2*i+1]) & 0xffffffff, t) ^ u
        A = rotr((A - S[2*i]) & 0xffffffff, u) ^ t
    D = (D - S[1]) & 0xffffffff
    B = (B - S[0]) & 0xffffffff
    return A, B, C, D

def process(option, text, key: str):
    S = rc6_key_schedule(key.encode("utf-8"))

    if option == 0:  # Chiffrer
        data = text.encode("utf-8")
        data = data.ljust(16, b"\0")  # padding
        block = struct.unpack("<4I", data)
        encrypted = rc6_encrypt_block(block, S)
        return struct.pack("<4I", *encrypted).hex()

    else:  # Déchiffrer
        data = bytes.fromhex(text)
        block = struct.unpack("<4I", data)
        decrypted = rc6_decrypt_block(block, S)
        result = struct.pack("<4I", *decrypted)
        return result.rstrip(b"\0").decode("utf-8", errors="ignore")
