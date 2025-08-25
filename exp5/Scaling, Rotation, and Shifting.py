import cv2
import numpy as np

# Read the image
img = cv2.imread('sample_image.png')
(height, width) = img.shape[:2]

# --- 1. Scaling ---
# This is the same as resizing, covered in point 4.
# We'll just use the cv2.resize() function.
scaled_img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imwrite('transformed_scaled.png', scaled_img)
print("Scaling operation complete.")

# --- 2. Rotation ---
# To rotate, we need a center of rotation, angle (in degrees), and scale
center = (width // 2, height // 2)
angle = 45  # Rotate by 45 degrees
scale = 1.0   # No scaling

# Get the 2x3 rotation matrix
M_rotate = cv2.getRotationMatrix2D(center, angle, scale)

# Apply the rotation using cv2.warpAffine
rotated_img = cv2.warpAffine(img, M_rotate, (width, height))
cv2.imwrite('transformed_rotated.png', rotated_img)
print("Rotation operation complete.")

# --- 3. Shifting (Translation) ---
# To shift, we create a translation matrix M = [[1, 0, tx], [0, 1, ty]]
# tx is the shift along the x-axis, ty is the shift along the y-axis
tx = 50   # Shift 50 pixels to the right
ty = 100  # Shift 100 pixels down

# Define the translation matrix as a NumPy array
M_shift = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation using cv2.warpAffine
shifted_img = cv2.warpAffine(img, M_shift, (width, height))
cv2.imwrite('transformed_shifted.png', shifted_img)
print("Shifting operation complete.")

# Display all transformed images
cv2.imshow('Original', img)
cv2.imshow('Rotated 45 Degrees', rotated_img)
cv2.imshow('Shifted Right and Down', shifted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()