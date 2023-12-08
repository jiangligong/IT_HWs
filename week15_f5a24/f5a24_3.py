print("f5a24黎家暉")
'''
#即時偵測影片中的人臉
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#faces = face_cascade.detectMultiScale(gray)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(480,300))              # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
    faces = face_cascade.detectMultiScale(gray)      # 偵測人臉
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)   # 標記人臉
    cv2.imshow('f5a24_3a', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''
# #=========================================
#b. 即時偵測影片中的人臉，自動加馬賽克
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(480,300))              # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
    faces = face_cascade.detectMultiScale(gray)      # 偵測人臉

    for (x, y, w, h) in faces:
        
        face_roi = frame[y:y+h, x:x+w]                      # 提取人臉區域
        face_roi = cv2.resize(face_roi, (w//10, h//10))     # 對人臉區域進行馬賽克處理
        face_roi = cv2.resize(face_roi, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h, x:x+w] = face_roi                      # 將馬賽克區域放回原圖

    cv2.imshow('f5a24_3b', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
