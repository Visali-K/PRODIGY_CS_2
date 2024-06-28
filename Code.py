from PIL import Image

def encrypt_image(image_path, key, output_path):
    
    image = Image.open(image_path)
    encrypted_image = image.copy()
    pixels = encrypted_image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    
    image = Image.open(image_path)
    decrypted_image = image.copy()
    pixels = decrypted_image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")
  
encrypt_image('input_image.png', 10, 'encrypted_image.png')
decrypt_image('encrypted_image.png', 10, 'decrypted_image.png')
