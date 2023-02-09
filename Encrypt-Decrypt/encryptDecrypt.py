import base64
def encrypt(key, plaintext):
    plaintext = plaintext.encode()
    encoded_text = base64.b64encode(plaintext)
    return encoded_text
def decrypt(key, ciphertext):
    decoded_text = base64.b64decode(ciphertext)
    plaintext = decoded_text.decode()
    return plaintext
def main():
    key = input("Enter a key: ")
    plaintext = input("Enter the message to encrypt: ")
    encrypted_message = encrypt(key, plaintext)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = decrypt(key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
main()
