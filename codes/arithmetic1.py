import cv2
def get_coordinates(event, x,y, flags, params):
    font = cv2.FONT_HERSHEY_DUPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, str(x)+','+str(y), (x,y), font, 1, (255,0,0), 2)
        cv2.imshow('image', img)

img = cv2.imread('sample.jpg', 1)
img = cv2.resize(img, (512, 512))
eye = img[127:250, 43:87]
img[300:423, 383:427] = eye
cv2.imshow('image', img)
cv2.setMouseCallback('image', get_coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()
