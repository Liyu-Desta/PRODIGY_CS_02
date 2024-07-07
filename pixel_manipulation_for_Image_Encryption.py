from PIL import Image
import numpy as np

def shuffle_pixels(image_array, key):
    np.random.seed(key)
    indices = np.arange(image_array.size)
    np.random.shuffle(indices)
    flat_image_array = image_array.flatten()
    shuffled_array = flat_image_array[indices]
    return shuffled_array.reshape(image_array.shape), indices

def unshuffle_pixels(shuffled_array, indices):
    unshuffled_array = np.zeros_like(shuffled_array)
    flat_shuffled_array = shuffled_array.flatten()
    flat_unshuffled_array = np.zeros_like(flat_shuffled_array)
    flat_unshuffled_array[indices] = flat_shuffled_array
    return flat_unshuffled_array.reshape(shuffled_array.shape)

def encrypt(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    image_array = np.array(image)

    # Shuffle pixels
    shuffled_array, indices = shuffle_pixels(image_array, key)

    # Apply the encryption (basic mathematical operation)
    encrypted_array = (shuffled_array.astype(np.uint16) + key) % 256
    encrypted_array = encrypted_array.astype(np.uint8)

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array)

    # Save the encrypted image and indices
    encrypted_image.save(output_path)
    np.save(output_path + '_indices.npy', indices)
    print(f'Image encrypted and saved to {output_path}')

def decrypt(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    image_array = np.array(image)

    # Apply the decryption (reverse the encryption operation)
    decrypted_array = (image_array.astype(np.uint16) - key) % 256
    decrypted_array = decrypted_array.astype(np.uint8)

    # Load the indices
    indices = np.load(image_path + '_indices.npy')

    # Unshuffle pixels
    unshuffled_array = unshuffle_pixels(decrypted_array, indices)

    # Convert the unshuffled array back to an image
    decrypted_image = Image.fromarray(unshuffled_array)

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f'Image decrypted and saved to {output_path}')

def main():
    choice = input('What do you want to do?\n1. Encrypt\n2. Decrypt\n')
    if choice == '1':
        image_path = input('Provide the path to the image to encrypt: ')
        output_path = input('Provide the complete path to save the encrypted image (including file name and extension): ')
        key = int(input('Provide the encryption key (an integer): '))
        encrypt(image_path, output_path, key)
    elif choice == '2':
        image_path = input('Provide the path to the image to decrypt: ')
        output_path = input('Provide the complete path to save the decrypted image (including file name and extension): ')
        key = int(input('Provide the decryption key (an integer): '))
        decrypt(image_path, output_path, key)
    else:
        print('Invalid choice. Please enter 1 to encrypt or 2 to decrypt.')

if __name__ == "__main__":
    main()
