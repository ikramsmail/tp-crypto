import hashlib
import struct

INITIAL_HASH = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

def sha256(message: bytes) -> str:
    # Pré-traitement (pédagogique, mais incomplet)
    message_byte_len = len(message)
    message_bit_len = message_byte_len * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += struct.pack('>Q', message_bit_len)
    h = INITIAL_HASH.copy()

    return ''.join(f'{value:08x}' for value in h)

def process(option, text, key=None):
    return hashlib.sha256(text.encode()).hexdigest()
