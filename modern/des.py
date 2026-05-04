import base64

IP  = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
       62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
       57,49,41,33,25,17, 9,1,59,51,43,35,27,19,11,3,
       61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
 
IP_INV = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
          38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
          36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
          34,2,42,10,50,18,58,26,33,1,41, 9,49,17,57,25]
 
E  = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,
      12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,
      22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
 
P  = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
      2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
 
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,
       59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,
       31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,
       29,21,13,5,28,20,12,4]
 
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,
       26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,
       51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
 
SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
 
S_BOXES = [
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
]
 
def permute(block, table):
    return [block[i-1] for i in table]
 
def string_to_bits(text):
    bits = []
    for char in text:
        bits.extend([int(b) for b in bin(ord(char))[2:].zfill(8)])
    return bits
 
def bits_to_string(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        chars.append(chr(int(''.join(map(str, byte)), 2)))
    return ''.join(chars)
 
def generate_subkeys(key: str):
    key_bits = string_to_bits(key)[:64]
    key_bits = permute(key_bits, PC1)
    C, D = key_bits[:28], key_bits[28:]
    subkeys = []
    for shift in SHIFTS:
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]
        subkeys.append(permute(C + D, PC2))
    return subkeys
 
def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]
 
def des_round(block, subkey):
    L, R = block[:32], block[32:]
    expanded_R = permute(R, E)
    xored = xor(expanded_R, subkey)
    sbox_out = []
    for i in range(8):
        chunk = xored[i*6:(i+1)*6]
        row = (chunk[0] << 1) | chunk[5]
        col = int(''.join(map(str, chunk[1:5])), 2)
        if i < len(S_BOXES):
            val = S_BOXES[i % len(S_BOXES)][row][col]
        else:
            val = 0
        sbox_out.extend([int(b) for b in bin(val)[2:].zfill(4)])
    permuted = permute(sbox_out, P)
    new_L = xor(L, permuted)
    return R + new_L
import base64

def des_encrypt_manual(text: str, key: str) -> str:
    """Chiffrement DES manuel."""
    # Convertir le texte en bits
    text_bits = string_to_bits(text)

    # Ajouter du padding si nécessaire
    if len(text_bits) % 64 != 0:
        text_bits.extend([0] * (64 - (len(text_bits) % 64)))

    # Générer les sous-clés
    subkeys = generate_subkeys(key)

    # Chiffrer chaque bloc de 64 bits
    result_bits = []
    for i in range(0, len(text_bits), 64):
        block = text_bits[i:i+64]
        block = permute(block, IP)

        # 16 rounds
        for j in range(16):
            block = des_round(block, subkeys[j])
        block = block[32:] + block[:32]
        block = permute(block, IP_INV)
        result_bits.extend(block)

    # Convertir les bits en chaîne base64
    result_bytes = bytes([
        int(''.join(map(str, result_bits[i:i+8])), 2)
        for i in range(0, len(result_bits), 8)
    ])
    return base64.b64encode(result_bytes).decode()


def des_decrypt_manual(b64_text: str, key: str) -> str:
    """Déchiffrement DES manuel."""
    # Convertir le base64 en bits
    text_bytes = base64.b64decode(b64_text)
    text_bits = []
    for byte in text_bytes:
        text_bits.extend([int(bit) for bit in bin(byte)[2:].zfill(8)])

    # Générer les sous-clés
    subkeys = generate_subkeys(key)
    subkeys.reverse()

    # Déchiffrer chaque bloc de 64 bits
    result_bits = []
    for i in range(0, len(text_bits), 64):
        block = text_bits[i:i+64]
        block = permute(block, IP)

        # 16 rounds
        for j in range(16):
            block = des_round(block, subkeys[j])
        block = block[32:] + block[:32]
        block = permute(block, IP_INV)

        result_bits.extend(block)
    return bits_to_string(result_bits).rstrip('\x00')
def process(option, text, key=None):
    if option == 0:  # Chiffrer
        return des_encrypt_manual(text, key)
    else:            # Déchiffrer
        return des_decrypt_manual(text, key)
