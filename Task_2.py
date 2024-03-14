import cv2
import numpy as np
import matplotlib.pyplot as plt

def spatial_average(image, neighborhood_size):
    # Define the kernel for averaging
    kernel = np.ones((neighborhood_size, neighborhood_size), dtype=np.float32) / (neighborhood_size ** 2)

    # Apply the filter
    averaged_image = cv2.filter2D(image, -1, kernel)

    return averaged_image

# Load the image
image = cv2.imread('picture.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform spatial averaging for different neighborhood sizes
neighborhood_sizes = [3, 10, 20]
fig, axs = plt.subplots(1, len(neighborhood_sizes), figsize=(15, 5))

for i, size in enumerate(neighborhood_sizes):
    averaged_image = spatial_average(gray_image, size)
    axs[i].imshow(averaged_image, cmap='gray')
    axs[i].set_title(f'Averaged Image {size}x{size}')
    axs[i].axis('off')

plt.show()
