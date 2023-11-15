print("f5a24黎家暉")

import cv2
cap = cv2.VideoCapture(0)

while(1):
    # 获得图片
    # 參數ret的值為True或False，代表有沒有讀到圖片
    # 參數是frame，是目前截取一格的圖片。
    ret, frame = cap.read()
    # 展示图片
    cv2.imshow("neighbor capture", frame)
    if cv2.waitKey(1) == ord('c'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # 存储图片
        cv2.imwrite("neighbor capture.jpg", frame)
    # 按下 q 結束
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
