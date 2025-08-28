import cv2

# Read the image
img = cv2.imread('sample_image.png')

# --- Method 1: Resize to specific dimensions ---
# Specify the new width and height
new_width = 200
new_height = 150
resized_img_specific = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
cv2.imwrite('resized_specific_dims.png', resized_img_specific)
print("Image resized to 200x150 and saved.")


# --- Method 2: Resize by a scaling factor ---
# Specify scaling factors for width (fx) and height (fy)
scale_x = 0.5  # 50% of original width
scale_y = 0.5  # 50% of original height
resized_img_scaled = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('resized_scaled.png', resized_img_scaled)
print("Image scaled by 50% and saved.")

# Display original and resized images
cv2.imshow('Original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()