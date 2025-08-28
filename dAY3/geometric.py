import cv2
import numpy as np

# Load the image
try:
    image = cv2.imread('image.png')
    if image is None:
        raise FileNotFoundError("Error: 'sample_image.jpg' not found. Make sure it's in the same folder as the script.")
    height, width = image.shape[:2]
except FileNotFoundError as e:
    print(e)
    exit()
s
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))


center = (width // 2, height // 2)
angle = 45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
affine_matrix = cv2.getAffineTransform(pts1, pts2)
affine_image = cv2.warpAffine(image, affine_matrix, (width, height))


# --- Display all the results ---
cv2.imshow('Original', image)
cv2.imshow('1. Translated', translated_image)
cv2.imshow('2. Rotated', rotated_image)
cv2.imshow('3. Scaled', scaled_image)
cv2.imshow('4. Affine', affine_image)

print("Displaying transformations. Press any key to close all windows.")
cv2.waitKey(0)
cv2.destroyAllWindows()
