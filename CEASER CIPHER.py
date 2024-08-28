def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
