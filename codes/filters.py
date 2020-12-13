import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('input.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5) , np.float32)/25

filtered = cv2.filter2D(img, -1, kernel)
blurred = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)

titles = ['Original', 'Filtered', 'Blurred', 'Gausssian', 'Median']

images = [img, filtered, blurred, gaussian, median]

for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()