from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):

    img = Image.open(image_path)
    img_array = np.array(img)

    encrypted_array = img_array ^ key

    encrypted_img = Image.fromarray(encrypted_array)
    
    encrypted_img.save(os.path.dirname(image_path) + '\encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")


def decrypt_image(image_path, key):

    img = Image.open(image_path)
    img_array = np.array(img)
    
    decrypted_array = img_array ^ key
    
    decrypted_img = Image.fromarray(decrypted_array)
    
    decrypted_img.save(os.path.dirname(image_path) + '\decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")



if __name__ == "__main__":
    print("Image Encryption/Decryption Tool")
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    image_path = input("Enter the image file path: ")
    key = int(input("Enter the encryption key (integer): "))
    if key > 255:
        key = key %255
    
    if mode == 'encrypt':
        encrypt_image(image_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, key)
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
