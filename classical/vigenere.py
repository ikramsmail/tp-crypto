def vigenere_encrypt(text: str, key: str) -> str:
    """Chiffrement de Vigenère."""
    result = ""
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(k) - ord('A') for k in key]

    for i, char in enumerate(text):
        if char.isalpha():
            key_index = i % key_length
            key_shift = key_as_int[key_index]
            if char.isupper():
                result += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
        else:
            result += char
    return result

def vigenere_decrypt(text: str, key: str) -> str:
    """Déchiffrement de Vigenère."""
    result = ""
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(k) - ord('A') for k in key]

    for i, char in enumerate(text):
        if char.isalpha():
            key_index = i % key_length
            key_shift = key_as_int[key_index]
            if char.isupper():
                result += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
        else:
            result += char
    return result

def process(option, text, key=None):
    if option == 0:  # Chiffrer
        return vigenere_encrypt(text, key)
    else:            # Déchiffrer
        return vigenere_decrypt(text, key)
