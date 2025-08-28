import cv2

# Load image
img = cv2.imread("sample_image.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
canny = cv2.Canny(gray, 50, 150)

# Save result
cv2.imwrite("canny_edges.png", canny)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Canny Edges", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canny edge detection completed! Saved as canny_edges.png")
