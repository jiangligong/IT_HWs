print("f5a24黎家暉")

#兩張圖片進行半透明漸層合成 
#準備兩張長寬尺寸相同的圖片(如果不同可用 resize 或裁切方式轉換成相同尺寸)，
# 使用 for 迴圈，讀取水平方向從左而右的像素，根據位置的比例，混合該像素的顏色，
# 就能做到半透明漸層合成的效果。

import cv2

img1 = cv2.imread('mona.jpg')
img2 = cv2.imread('girl.jpg')
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # 藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # 紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # 綠色按照比例混合

cv2.imwrite('f5a24_2aa.png',img1)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('f5a24_2aa.png', show)

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()

#=========================================
#b.利用2位小學同學的相片進行半透明漸層合成

import cv2

img1 = cv2.imread('10.png')
img2 = cv2.imread('25.png')
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # B藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # R紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # G綠色按照比例混合

cv2.imwrite('f5a24_2bb.png',img1)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('f5a24_2bb.png', show)

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()





#=========================================
#c.利用2位同學的相片進行半透明漸層合成(例如：1號和2號、3號和4號.........)(加分題)

import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # B藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # R紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # G綠色按照比例混合

cv2.imwrite('f5a24_2cc.png',img1)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('f5a24_2cc.png', show)

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()