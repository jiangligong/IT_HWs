print("f5a24 黎家暉")

f = open("students.txt", "r")
num = int(input("請輸入你的學號："))

if num >=1 and num <= 26:
    f.seek((num-1)*15, 0)
    print(f"你的姓名是{f.readline()[7:]}")
    
else: print(f"並沒有{num}這個學號")
