from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encrypt by adding the key to each pixel value
    encrypted_array = (img_array + key) % 256  # Ensuring pixel values remain in the range [0, 255]

    # Create and save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Decrypt by subtracting the key from each pixel value
    decrypted_array = (img_array - key) % 256  # Ensuring pixel values remain in the range [0, 255]

    # Create and save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

# Main program
if __name__ == "__main__":
    print("Image Encryption/Decryption Program")
    
    # User input
    mode = input("Would you like to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    image_path = input("Enter the path of the image file: ")
    key = int(input("Enter the key (a number) for encryption/decryption: "))
    
    # Perform the chosen operation
    if mode == 'encrypt':
        encrypt_image(image_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
