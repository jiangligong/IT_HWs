print("f5a24黎家暉")

#圖片去背，加上其他背景圖 
#下方的程式碼運用同樣的原理，將背景單純的物體去背(去除背景)，
#然後再與其他圖片進行重疊合成。
'''
import cv2
bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA


img = cv2.imread('goku.jpg', cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 轉換成 BGRA

h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if 20<=r<=80 and 110<=g<=190 and 60<=b<=150:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.imwrite('f5a24_1aa.png', img)
img = cv2.imread('f5a24_1aa.png')
cv2.imshow('f5a24_1aa', img)

cv2.waitKey(0)
cv2.destroyAllWindows()





#=========================================
#b.利用三眼仔圖片(白色背景)去背，加上其他背景圖

import cv2
bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA


img = cv2.imread('Toy_Story01.jpg', cv2.IMREAD_UNCHANGED)  # 開啟三眼仔公仔圖
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 轉換成 BGRA

h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if 250<=r<=255 and 250<=g<=255 and 250<=b<=255:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.imwrite('f5a24_1bb.png', img)
img = cv2.imread('f5a24_1bb.png')
cv2.imshow('f5a24_1bb', img)

cv2.waitKey(0)
cv2.destroyAllWindows()





#=========================================
#c.利用三眼仔圖片(綠色背景)去背，加上其他背景圖

import cv2
bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA


img = cv2.imread('Toy_Story01a.jpg', cv2.IMREAD_UNCHANGED)  # 開啟三眼仔公仔圖
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 轉換成 BGRA

h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if 20<=r<=80 and 110<=g<=190 and 60<=b<=150:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.imwrite('f5a24_1cc.png', img)
img = cv2.imread('f5a24_1cc.png')
cv2.imshow('f5a24_1cc', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''




#=========================================
#d.利用自己相片(白色/綠色背景)去背，加上其他背景圖(加分題)

import cv2
bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA


img = cv2.imread('IMG-0977.png', cv2.IMREAD_UNCHANGED)  # 開啟自拍照
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)             # 轉換成 BGRA

# 将自拍照马赛克
x, y, cw, ch = 50, 80, 200, 160
mosaic = img[y:y+ch, x:x+cw]
level = 15
h, w = int(ch/level), int(cw/level) 
mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_LINEAR)
mosaic = cv2.resize(mosaic, (cw,ch), interpolation=cv2.INTER_NEAREST)
img[y:y+ch, x:x+cw] = mosaic


h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if 250<=r<=255 and 250<=g<=255 and 250<=b<=255:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.imwrite('f5a24_1dd.png', img)
img = cv2.imread('f5a24_1dd.png')
cv2.imshow('f5a24_1dd', img)

cv2.waitKey(0)
cv2.destroyAllWindows()