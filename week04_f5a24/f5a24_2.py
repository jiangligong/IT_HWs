print("f5a24 黎家暉")

def circle_area(r) :
    pi = 3.14
    return pi * r**2

def circle_circum(r) :
    pi = 3.14
    return pi * r * 2

def circle_calculator(r, is_area = True) :
    pi = 3.14
    if is_area == True :
        return pi * r**2
    elif is_area == False :
        return pi * r * 2

def circle_calculator2(r) :
    pi = 3.14
    area = pi * r**2
    circum = pi * r * 2
    return area, circum

r = float(input("請輸入圓半徑："))
print("\n計算出圓面積")
print(f"圓面積為:{circle_area(r)}\n")

print("-" * 30)
print("\n計算出圓周長")
print(f"圓周長為:{circle_circum(r)}\n")

print("-" * 30)
is_area = bool(input("\n計算面積輸入1/計算周長輸入0:"))
r = float(input("請輸入圓半徑："))
if is_area == True :
    print(f"利用參數is_area決定回傳面積為：{circle_calculator(r, is_area = True)}\n")
elif is_area == False :
    print(f"利用參數is_area決定回傳周長為：{circle_calculator(r, is_area = False)}\n")

print("-" * 30)
r = float(input("請輸入圓半徑："))
print(f"圓面積為{circle_calculator2(r)[0]}，圓周長為{circle_calculator2(r)[1]}")