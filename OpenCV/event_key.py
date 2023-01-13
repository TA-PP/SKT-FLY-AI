import numpy as np
import cv2

## switch case 문을 사전(dictionary)으로 구현
switch_case = {
    ord('a'): "a키 입력",
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력", # 16진수인 0x42를 10진수로 변환하면 66임
    2424832: "왼쪽 화살표키 입력", # 0x250000
    2490368: "윗쪽 화살표키 입력", # 0x260000
    2555904: "오른쪽 화살표키 입력", # 0x270000
    2621440: "아래쪽 화살표키 입력" # 0x280000
}

image = np.ones((200, 300), np.float64)
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', image)

while True:
    key = 