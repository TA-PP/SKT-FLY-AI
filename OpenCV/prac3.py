import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception('카메라 연결결 안됨')

fps = 15
delay = round(1000/fps)
size = (600, 480)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

while True:
    ret, frame = capture.read()
    if not ret or cv2.waitKey(delay) >= 0: break

    cv2.flip()

    x, y, w, h = (200, 100, 100, 200)
    cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 3)

    blue, green, red = cv2.split(frame)
    tmp = green[y:y+h, x:x+w]
    cv2.add(tmp, 50, tmp)
    frame = cv2.merge([blue, green, red])

    if cv2.waitKey(delay) >= 0: break
    cv2.imshow('Read Video File', frame)

capture.release()