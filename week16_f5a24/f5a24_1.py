print('f5a24黎家暉\n')

#導入庫
import cv2
import numpy as np

#建立畫布並指定三角形的座標：
# 建立畫布
img = np.zeros((512, 512, 3), np.uint8)

# 定義三角形的三點
pts = np.array([[100, 100], [400, 100], [250, 400]], np.int32)
# 資料型別必須為 int32
pts = pts.reshape((-1, 1, 2))
#將pts變數轉換為三維數組，其中第一維的大小由原始數組中的元素數量自動計算，
#第二維和第三維的大小分別為1 和2

#在畫布上繪製三角形：
# 繪製三角形
cv2.polylines(img, [pts], True, (0, 255, 255), 3)
#polylines()函數繪製一個多邊形，[pts]參數指定繪製的多邊形的點(這裡是一個三角形)，
#True表示繪製閉合的多邊形，(0, 255, 255)指定繪製的顏色，3表示繪製的線條粗細為3。

#顯示繪製結果：
cv2.imshow("f5a24_1aa", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#=========================================
#b. 繪製尖角向上三角形

import cv2
import numpy as np

#建立畫布並指定三角形的座標：
# 建立畫布
img = np.zeros((512, 512, 3), np.uint8)

# 定義三角形的三點
pts = np.array([[250, 100], [100, 400], [400, 400]], np.int32)
# 資料型別必須為 int32
pts = pts.reshape((-1, 1, 2))
#將pts變數轉換為三維數組，其中第一維的大小由原始數組中的元素數量自動計算，
#第二維和第三維的大小分別為1 和2

#在畫布上繪製三角形：
# 繪製三角形
cv2.polylines(img, [pts], True, (0, 255, 255), 3)
#polylines()函數繪製一個多邊形，[pts]參數指定繪製的多邊形的點(這裡是一個三角形)，
#True表示繪製閉合的多邊形，(0, 255, 255)指定繪製的顏色，3表示繪製的線條粗細為3。

#顯示繪製結果：
cv2.imshow("f5a24_1bb", img)
cv2.waitKey(0)
cv2.destroyAllWindows()