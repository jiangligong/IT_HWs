print("f5a24 黎家暉")

print("計算華氏(F)與攝氏(C)溫度的轉換")
print("C = (F - 32) / 1.8")
print("F = 1.8 * C + 32\n")

temp = input("輸入溫度值，例如30C 或 80F: ")

if temp[-1] in ["f", "F"] :
    print(f"{temp} 轉換華氏溫度是: {1.8 * float(temp[:-1]) + 32}C\n")

elif temp[-1] in ["c", "C"] :
    print(f"{temp} 轉換攝氏溫度是: {(float(temp[:-1]) - 32) / 1.8}F\n")

else :
    print("格式錯誤")