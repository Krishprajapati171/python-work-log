
def encrypt(plaintext, key):
    """Encrypt the plaintext."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext.lower():
        if char in alphabet:
            ciphertext += key[alphabet.index(char)]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for char in ciphertext.lower():
        if char in key:
            plaintext += alphabet[key.index(char)]
        else:
            plaintext += char
    return plaintext

# User input for the substitution key and plaintext
key = input("Enter a 26-letter key (e.g., qwertyuiopasdfghjklzxcvbnm): ")
if len(key) != 26:
    print("Error: The key must have exactly 26 unique letters.")
else:
    plaintext = input("Enter plaintext to encrypt: ")
    ciphertext = encrypt(plaintext, key)
    print("Encrypted Text:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
