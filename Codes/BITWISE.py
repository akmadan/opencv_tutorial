import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
img2 = np.zeros((512,512,3), np.uint8)

img2 = cv2.rectangle(img2, (256,0), (512,512), (255,255,255), -1)

bit_and_result = cv2.bitwise_and(img1, img2)
bit_or_result = cv2.bitwise_or(img1, img2)
bit_not_result = cv2.bitwise_not(img1)
bit_xor_result = cv2.bitwise_xor(img2, img1)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('result', bit_xor_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
