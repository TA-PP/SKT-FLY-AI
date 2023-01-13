import numpy as np
import cv2

area = 0

def setLabelCir(img, pts, text): # 정확한 출력을 위한 좌표 수정
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y) 
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 0), 1)
    cv2.putText(img, text, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

image = cv2.imread('OpenCV/images/yejin.png')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower = np.array([0,30,30], dtype="uint8") # 전체
# upper = np.array([255, 255, 255], dtype="uint8")
lower_b = np.array([100, 100, 120], dtype="uint8") # blue
upper_b = np.array([150, 255, 255], dtype="uint8")
lower_g = np.array([50, 150, 50], dtype="uint8") # green
upper_g = np.array([80, 255, 255], dtype="uint8")
lower_r = np.array([0, 240, 240], dtype="uint8") # red
upper_r = np.array([10, 255, 255], dtype="uint8")
mask_b = cv2.inRange(image, lower_b, upper_b)
mask_g = cv2.inRange(image, lower_g, upper_g)
mask_r = cv2.inRange(image, lower_r, upper_r)

def hs_sw(mask, text):
    global area
    count = 0
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1] # 인자 중 contours만 받아옴(이미지, 계층 구조 x)

    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        if len(approx) > 5:
            setLabelCir(original, c, text)
            count += 1
            area += cv2.contourArea(c)
    print("%s 색상의 공 개수 : %d" % (text, count))

hs_sw(mask_b, 'blue')
hs_sw(mask_g, 'green')
hs_sw(mask_r, 'red')

print("총 공의 비율 : %.4f" % (area/(original.shape[0]*original.shape[1])))

cv2.imshow('original', original)
cv2.waitKey(0)