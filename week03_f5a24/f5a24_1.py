print("f5a24 黎家暉")

print("計算梯形的面積(公式: 上底加下底乘高除二)\n")

upperb = float(input("輸入梯形中上底(upperb)的長度(cm): "))
underb = float(input("輸入梯形中下底(underb)的長度(cm): "))
height = float(input("輸入梯形中高(height)的長度(cm): "))

trapezoid = ((upperb + underb) * height) / 2

print(f"梯形的面積是: {trapezoid}")