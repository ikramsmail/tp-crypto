def cesar_encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def cesar_decrypt(text: str, shift: int) -> str:
    return cesar_encrypt(text, -shift)

def process(option, text, key=None):
    shift = int(key) if key else 3
    if option == 0:  # Chiffrer
        return cesar_encrypt(text, shift)
    else:            # Déchiffrer
        return cesar_decrypt(text, shift)
