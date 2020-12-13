import cv2
import matplotlib.pyplot as plt

monkey = cv2.imread('sample.jpg', 1)
monkey = cv2.cvtColor(monkey, cv2.COLOR_BGR2RGB)

building = cv2.imread('building.jpg',1)
building = cv2.cvtColor(building, cv2.COLOR_BGR2RGB)

butterfly = cv2.imread('butterfly.jpg',1)
butterfly = cv2.cvtColor(butterfly, cv2.COLOR_BGR2RGB)

fruits = cv2.imread('fruits.jpg',1)
fruits = cv2.cvtColor(fruits, cv2.COLOR_BGR2RGB)

home  = cv2.imread('home.jpg', 1)
home = cv2.cvtColor(home, cv2.COLOR_BGR2RGB)

fish  = cv2.imread('HappyFish.jpg', 1)
fish = cv2.cvtColor(fish, cv2.COLOR_BGR2RGB)

images = [monkey, building, butterfly, home, fish, fruits]
for i in range(len(images)):
    plt.subplot(3,2, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(images[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
