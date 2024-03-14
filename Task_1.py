import cv2
import matplotlib.pyplot as plt

def reduce_intensity_levels(image, levels):
    reduced_image = (image // (256 // levels)) * (256 // levels)
    return reduced_image

# Load the image
image = cv2.imread('picture.jpg', cv2.IMREAD_GRAYSCALE)

desired_levels = int(input("Enter the desired number of intensity levels (power of 2, between 2 and 256): "))

# Validate the user input
if not (desired_levels and desired_levels >= 2 and desired_levels <= 256 and desired_levels & (desired_levels - 1) == 0):
    print("Please enter a valid number of intensity levels (a power of 2 between 2 and 256).")
    exit()

# Display the original image
plt.figure(figsize=(6, 6))
plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Reduce the intensity levels and display the image with the reduced levels
reduced_image = reduce_intensity_levels(image, desired_levels)
plt.subplot(2, 1, 2)
plt.imshow(reduced_image, cmap='gray')
plt.title('Reduced Image ({} intensity levels)'.format(desired_levels))
plt.axis('off')

plt.show()
