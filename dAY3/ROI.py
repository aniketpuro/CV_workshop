#resume of interest
import cv2 as cv
import numpy as np
img = cv.imread("image.png")  # Go up one directory to find image.png
roi = img[84:308,717:890]
img[84:308,457:630] = roi  # Moved 100px left, adjusted width to match ROI (457+173=630)


# img = cv.putText(img, "ROI", (300, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv.imshow("ROI", roi)
cv.waitKey(0)  # Wait until any key is pressed
cv.destroyAllWindows()