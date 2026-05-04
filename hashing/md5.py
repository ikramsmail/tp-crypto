import hashlib

def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

def process(option, text, key=None):
    return md5_hash(text)
