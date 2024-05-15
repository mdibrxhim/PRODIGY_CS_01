def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    
    while True:
        mode = input("Would you like to (e)ncrypt, (d)ecrypt, or (q)uit?: ").strip().lower()
        if mode == 'q' or mode == 'quit':
            print("Exiting the program. Goodbye!")
            break
        if mode not in ['e', 'encrypt', 'd', 'decrypt']:
            print("Invalid option. Please choose 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue
        
        text = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if mode.startswith('e'):
            result = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted text: {result}")
        elif mode.startswith('d'):
            result = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted text: {result}")
    
if __name__ == "__main__":
    main()
