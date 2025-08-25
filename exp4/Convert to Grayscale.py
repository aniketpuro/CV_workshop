import cv2

# Read the color image
color_img = cv2.imread('sample_image.png')

# Convert the BGR image to grayscale
# cv2.cvtColor() is the function for color space conversions
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('grayscale_image.png', gray_img)
print("Grayscale image saved.")

# Display both images
cv2.imshow('Color Image', color_img)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()