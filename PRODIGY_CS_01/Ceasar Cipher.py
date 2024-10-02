def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:

        if char.isalpha():
            shift_base = 65 if char.isupper() else 97 

            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
            
        else:
            result += char
    
    return result


if __name__ == "__main__":
    print("Caesar Cipher Algorithm")
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    
    if mode in ['encrypt', 'decrypt']:
        if shift > 26:
            shift = shift % 26
        output = caesar_cipher(text, shift, mode)
        print(f"Result ({mode}ed): {output}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
