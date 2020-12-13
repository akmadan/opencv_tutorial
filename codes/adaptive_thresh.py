import cv2
img = cv2.imread('sample1.jpg',0)
#a_,threshold = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
adaptive_threshold = cv2.adaptiveThreshold(img, 255,
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 11,2);

#cv2.imshow('thresh', threshold)
cv2.imshow('adaptive', adaptive_threshold)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()