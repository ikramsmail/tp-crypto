def F(right, key):
    return (right ^ key)  # version simplifiée

def feistel_encrypt(block, keys):
    L, R = block

    for k in keys:
        L, R = R, (L ^ F(R, k))

    return L, R

def feistel_decrypt(block, keys):
    L, R = block

    for k in reversed(keys):
        L, R = (R ^ F(L, k)), L

    return L, R