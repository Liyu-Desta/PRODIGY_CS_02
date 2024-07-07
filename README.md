This Python script allows for encryption and decryption of images using pixel manipulation techniques.
By shuffling pixel positions based on a user-provided key, the script encrypts the image by applying 
a basic mathematical operation to each pixel. The shuffled indices are saved alongside the encrypted image. 
During decryption, the script retrieves the shuffled indices, unshuffles the pixels, and reverses the 
encryption process to restore the original image. Ensure that both the encrypted image and the corresponding
_indices.npy file are present in the directory for successful decryption.
