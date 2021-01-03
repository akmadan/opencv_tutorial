import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('smarties.png', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
_, threshold = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(threshold, kernel, iterations=1)
erosion = cv2.erode(threshold,kernel,iterations = 1)
gradient = cv2.morphologyEx(threshold, cv2.MORPH_GRADIENT, kernel)

plt.subplot(3,2,1)
plt.imshow(img)
plt.subplot(3,2,2)
plt.imshow(threshold)
plt.subplot(3,2,3)
plt.imshow(erosion)
plt.subplot(3,2,4)
plt.imshow(dilation)
plt.subplot(3,2,5)
plt.imshow(gradient)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()