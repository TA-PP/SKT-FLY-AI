import cv2

image = cv2.imread('OpenCV/images/flip_test.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception('영상 파일 오류 발생')

x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
rep_image = cv2.flip(image, 1, 2)
trans_image = cv2.flip(image)

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', 'rep_image', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)