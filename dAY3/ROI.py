import cv2
import numpy as np

#read image
img = cv2.imread("image.png")
img = cv2.resize(img,(800,800))

roi = img[50:250,320:450]
img[50:250,190:320] = roi
img[50:250,450:580] = roi
img[330:530,560:690] = roi

# Save the generated image
cv2.imwrite("generated_roi_image.png", img)
print("Image saved as 'generated_roi_image.png'")

cv2.imshow("ironman",img)
# cv2.imshow('ROI',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()