import cv2
import numpy as np

def something():
    pass


img = np.zeros((250,500,3), np.uint8)
cv2.namedWindow('trackbar')
cv2.createTrackbar('B', 'trackbar', 0,255 , something)
cv2.createTrackbar('G', 'trackbar', 0,255 , something)
cv2.createTrackbar('R', 'trackbar', 0,255 , something)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    b = cv2.getTrackbarPos('B', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    r = cv2.getTrackbarPos('R', 'trackbar')
    img[:] = [b,g,r]
cv2.destroyAllWindows()