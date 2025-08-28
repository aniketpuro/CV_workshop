import cv2
import numpy as np

# Load the image and convert it to grayscale
try:
    image = cv2.imread('image.png')
    if image is None:
        raise FileNotFoundError("Error: 'sample_image.jpg' not found.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
except FileNotFoundError as e:
    print(e)
    exit()

edges = cv2.Canny(gray, threshold1=100, threshold2=200)


lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
lines_image = image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(lines_image, (x1, y1), (x2, y2), (0, 0, 255), 2) # Draw red lines

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners = np.int0(corners)
corners_image = image.copy()
for i in corners:
    x, y = i.ravel()
    cv2.circle(corners_image, (x, y), 3, (0, 255, 0), -1) # Draw green circles


# --- Display all the results ---
cv2.imshow('Original', image)
cv2.imshow('1. Canny Edges', edges)
cv2.imshow('2. Detected Lines', lines_image)
cv2.imshow('3. Detected Corners (Shi-Tomasi)', corners_image)

print("Displaying feature detection results. Press any key to close all windows.")
cv2.waitKey(0)
cv2.destroyAllWindows()
