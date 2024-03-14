import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('picture.jpg')

# Rotate the image by 45 degrees
rows, cols = image.shape[:2]
rotation_matrix_45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))

# Rotate the image by 90 degrees
rotation_matrix_90 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))

# Display the original image
plt.figure()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Display the rotated images
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(rotated_image_45, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image 45 Degrees')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(rotated_image_90, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image 90 Degrees')

plt.show()