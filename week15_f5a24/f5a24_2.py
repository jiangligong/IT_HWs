print("f5a24黎家暉")

# 人臉加上馬賽克 
# 將「人臉偵測」和「馬賽克效果」兩篇文章的範例結合，當影像中偵測到人臉時，
# 透過 x、y 坐標和 w、h 長寬，就能定義馬賽克的位置和大小，下面的程式執行後，
# 會自動將蒙娜麗莎的臉加上馬賽克。

import cv2
img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # 載入人臉偵測模型
faces = face_cascade.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('f5a24_2a', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()

#=========================================
#b.把The_Queen_of_News圖片的人臉加上馬賽克。




import cv2
img = cv2.imread('The_Queen_of_News.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # 載入人臉偵測模型
faces = face_cascade.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('f5a24_2b', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()





#=========================================
#c.把自己或與同學表情包相片(4合1/6合1)的人臉加上馬賽克(加分題)

import cv2
img = cv2.imread('classphoto.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # 載入人臉偵測模型
faces = face_cascade.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('f5a24_2c', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()