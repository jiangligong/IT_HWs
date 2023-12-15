print('f5a24黎家暉\n')

#偵測眼睛、鼻子和嘴巴 
# 例子執行後，會偵測圖片中人的眼睛、鼻子和嘴巴，並透過繪製形狀的方式，
# 使用方框標記偵測到的人臉，通常鼻子和嘴巴的準確度較低，容易偵測到其他類似的形狀，
# 至於眼睛的準確度則較高。

import cv2
img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('f5a24_2aa', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()



#=========================================
#b.利用方框和圓形把2~30.png圖片偵測影像中的眼睛、鼻子和嘴巴

import cv2
img = cv2.imread('3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.circle(img, (x + w // 2, y + h // 2), min(w, h) // 2, (255, 0, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('f5a24_2bb', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()



#=========================================
#c.利用方框、圓形和三角形把2~30.png圖片偵測影像中的眼睛、鼻子和嘴巴。

import cv2
import numpy as np
img = cv2.imread('30.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.circle(img, (x + w // 2, y + h // 2), min(w, h) // 2, (0, 255, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.polylines(img, [np.array([[x + w // 2, y], [x, y + h], [x + w, y + h]], np.int32).reshape(-1, 1, 2)], True, (255, 0, 0), 2)# 標記藍色方框

cv2.imshow('f5a24_2cc', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()