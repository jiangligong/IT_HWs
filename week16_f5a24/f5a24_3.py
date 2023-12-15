print('f5a24黎家暉\n')

#即時偵測影片中的五官
import cv2
cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")          # 使用眼睛模型
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(540,320))
    gray = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    eyes = eye_cascade.detectMultiScale(gray)      # 偵測眼睛
    for (x, y, w, h) in eyes:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(img, (x+int(w/2), y+int(h/2)), int(w/2), (0, 255, 0), 2)

    mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴
    for (x, y, w, h) in mouths:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    noses = nose_cascade.detectMultiScale(gray)    # 偵測鼻子
    for (x, y, w, h) in noses:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('f5a24_3aa', img)
    if cv2.waitKey(1) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()


#=========================================
#b.利用方框、圓形和倒尖角三角形把即時偵測影片中的五官

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")          # 使用眼睛模型
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(540,320))
    gray = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    eyes = eye_cascade.detectMultiScale(gray)      # 偵測眼睛
    for (x, y, w, h) in eyes:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(img, (x+int(w/2), y+int(h/2)), int(w/2), (0, 255, 0), 2)

    mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴
    for (x, y, w, h) in mouths:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    noses = nose_cascade.detectMultiScale(gray)    # 偵測鼻子
    for (x, y, w, h) in noses:
        cv2.polylines(img, [np.array([[x, y], [x + w, y], [x + w // 2, y + h]], np.int32).reshape(-1, 1, 2)], True, (255, 0, 0), 2)

    cv2.imshow('f5a24_3bb', img)
    if cv2.waitKey(1) == ord('q'):
        break     # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()