print("f5a24黎家暉")

# 偵測影像中的人臉 
# OpenCV 裡的 CascadeClassifier() 方法(級聯分類器)，
# 可以根據所提供的模型檔案，判斷某個事件是否屬於某種結果，
# *例如偵測人臉，如果影像中符合模型所定義的人臉屬性，
# 就會出現這個人臉對應的屬性 ( 座標、尺寸...等 )*。
# 使用 CascadeClassifier() 後，會再*透過 detectMultiScale() 進行偵測，
# 如果偵測到臉，就會將偵測到的屬性輸出 ( 串列與字典形式 )*，相關用法如下：

import cv2
img = cv2.imread('mona.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
# 設定集聯分類器為人臉的模型 ( haarcascade_frontalface_default.xml )
faces = face_cascade.detectMultiScale(gray)    # 偵測人臉
# 偵測並取出相關屬性
# img 來源影像，建議使用灰階影像
# scaleFactor 前後兩次掃瞄偵測畫面的比例係數，預設 1.1
# minNeighbors 構成檢測目標的相鄰矩形的最小個數，預設 3
# flags 通常不用設定，若設定 CV_HAAR_DO_CANNY_PRUNING 會使用 Canny 邊緣偵測，排除邊緣過多或過少的區域
# minSize, maxSize 限制目標區域的範圍，通常不用設定

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('f5a_1a', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()





#=========================================
#b.利用綠方框把p1/p2/p3圖片偵測影像中的多個人臉。





import cv2
img = cv2.imread('p2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
# 設定集聯分類器為人臉的模型 ( haarcascade_frontalface_default.xml )
faces = face_cascade.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('f5a_1b', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()





#=========================================
#c.利用藍色圓圈把p1/p2/p3圖片偵測影像中的多個人臉





import cv2
img = cv2.imread('p3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
# 設定集聯分類器為人臉的模型 ( haarcascade_frontalface_default.xml )
faces = face_cascade.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    center_x = x + w // 2
    center_y = y + h // 2
    radius = min(w, h) // 2
    cv2.circle(img, (center_x, center_y), radius, (255, 0, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製圓圈

cv2.imshow('f5a_1c', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()





#=========================================
#d.利用自己或與同學表情包相片(4合1/6合1)偵測影像中的多個人臉(加分題)





import cv2
img = cv2.imread('classphoto.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
# 設定集聯分類器為人臉的模型 ( haarcascade_frontalface_default.xml )
faces = face_cascade.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('f5a_1c', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()