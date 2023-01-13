import cv2
import matplotlib.pyplot as plt

img = cv2.imread('OpenCV/images/ots1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 128, 255, 0)

plt.subplot(131),
plt.imshow(imgRGB, cmap = 'gray'),
plt.title('Original Image'),
plt.axis('off')
plt.subplot(132),
plt.imshow(gray, cmap = 'gray'),
plt.title('Grayscale Image'),
plt.axis('off')
plt.subplot(133),
plt.imshow(thresh, cmap = 'gray'),
plt.title('Binary Image'),
plt.axis('off')

plt.show()