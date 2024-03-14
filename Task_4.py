import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_resolution(image, block_size):
    # Calculate the dimensions of the image and the block size
    height, width = image.shape[:2]
    new_height = height // block_size
    new_width = width // block_size

    # Reshape the image into blocks
    blocks = image[:new_height * block_size, :new_width * block_size].reshape(new_height, block_size, new_width, block_size)

    # Take the average of each block
    reduced_blocks = blocks.mean(axis=(1, 3))

    # Repeat each block to the original size
    reduced_image = np.repeat(np.repeat(reduced_blocks, block_size, axis=1), block_size, axis=0)

    return reduced_image.astype(np.uint8)

# Load the image
image = cv2.imread('picture.jpg', cv2.IMREAD_GRAYSCALE)

# Reduce resolution for 3x3 blocks
reduced_image_3x3 = reduce_resolution(image, 3)

# Reduce resolution for 5x5 blocks
reduced_image_5x5 = reduce_resolution(image, 5)

# Reduce resolution for 7x7 blocks
reduced_image_7x7 = reduce_resolution(image, 7)

# Display the original and reduced resolution images
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(reduced_image_3x3, cmap='gray')
plt.title('Reduced Resolution 3x3')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(reduced_image_5x5, cmap='gray')
plt.title('Reduced Resolution 5x5')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(reduced_image_7x7, cmap='gray')
plt.title('Reduced Resolution 7x7')
plt.axis('off')

plt.show()
