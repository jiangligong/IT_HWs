print("f5a24黎家暉")

import cv2
img = cv2.imread('AsianGames.jpg')   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imshow('coffee Studio', img)     # 使用名為 ChanTaiManstudio 的視窗開啟圖片
cv2.waitKey(0)                       # 按下任意鍵停止
cv2.destroyAllWindows()              # 結束所有圖片視窗

#BGR 彩色圖像，圖像尺寸減小 1/4

img = cv2.imread('AsianGames.jpg', cv2.IMREAD_REDUCED_COLOR_4)   # 開啟圖片，使用 cv2.IMREAD_COLOR_4 模式
cv2.imshow('coffee Studio', img)                                 # 使用名為 ChanTaiManstudio 的視窗開啟圖片
cv2.waitKey(0)                                                   # 按下任意鍵停止
cv2.destroyAllWindows()                                          # 結束所有圖片視窗