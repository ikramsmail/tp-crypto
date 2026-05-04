def rc4_init(key):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def rc4_crypt(text, key):
    S = rc4_init(key)
    i = j = 0
    result = []

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ K))

    return ''.join(result)

def process(option, text, key=None):
    return rc4_crypt(text, key)

