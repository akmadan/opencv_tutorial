import cv2
img = cv2.imread('gradient.png')


_, thresh_binary = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
_, thresh_binary_inverse = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
_, thresh_trunc = cv2.threshold(img, 79, 255, cv2.THRESH_TRUNC)
_, thresh_tozero = cv2.threshold(img, 79, 255, cv2.THRESH_TOZERO)
_, thresh_tozero_inv = cv2.threshold(img, 79, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('image', img)
cv2.imshow('thresh_binary', thresh_binary)
cv2.imshow('thresh_binary_inverse', thresh_binary_inverse)
cv2.imshow('thresh_trunc', thresh_trunc)
cv2.imshow('thresh_tozero', thresh_tozero)
cv2.imshow('thresh_tozero_inv', thresh_tozero_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()