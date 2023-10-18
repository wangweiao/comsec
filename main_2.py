def encrypt_by_add_mod(text, key):
    cipher = ''
    for ch in text:
        cipher += chr((ord(ch) + key) % 256)
    return cipher

