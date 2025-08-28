import cv2 as cv
import numpy as np
img = np.ones([512,512,3],np.uint8)*255 #white
cv.imshow('Image', img)

img = np.ones([512,512,3],np.uint8)*0 #black


img = cv.imread("sample_image.png")
img = cv.resize(img, (512, 512))

img = cv.line(img, (288,158), (531,158), (255,0,0), 5)
img = cv.arrowedLine(img, (288,158), (531,158), (0,255,0), 5)
img = cv.rectangle(img, (168,400), (200,400), (0,0,255), 5)
img = cv.circle(img, (300,300), 10, (0,0,0), -1)
#polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
print(pts)
cv.polylines(img, [np.array(pts,np.int32)], True, (255,0,255), 5)

#create self input array
pts = np.array([[0,0],[0,512],[512,512],[512,0]], np.int32)
img = cv.polylines(img,[pts],False,(0,255,255),5)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
