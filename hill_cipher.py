import numpy as np

def get_matrix(key):
    """Convert the key string into a matrix."""
    key_matrix = []
    for i in range(0, len(key), 2):
        key_matrix.append([ord(key[i]) - 65, ord(key[i + 1]) - 65])
    return np.array(key_matrix)


def encrypt(plaintext, key):
    """Encrypt the plaintext using the Hill cipher."""
    key_matrix = get_matrix(key)
    plaintext_vector = [ord(char) - 65 for char in plaintext]

    # Pad plaintext if necessary
    while len(plaintext_vector) % 2 != 0:
        plaintext_vector.append(ord('X') - 65)  # Padding with 'X'

    ciphertext = []
    for i in range(0, len(plaintext_vector), 2):
        vector = np.array(plaintext_vector[i:i + 2])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        ciphertext.extend(encrypted_vector)

    return ''.join(chr(num + 65) for num in ciphertext)


def main():
    plaintext = input("Enter the plaintext (uppercase letters only): ").upper()
    key = input("Enter the key (4 uppercase letters): ").upper()

    if len(key) != 4 or not all(char.isalpha() for char in key):
        print("Key must be 4 uppercase letters.")
        return

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)


if __name__ == "__main__":
    main()