import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('input.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

blurred = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

titles = ['Original', 'Blurred', 'Gaussian', 'Median']

images = [img,  blurred, gaussian, median]

for i in range(len(titles)):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()