print("f5a24 黎家暉")

f = open("f5a24_1.txt", "r", encoding="utf-8")
print(f"進行讀檔\n{f.read()}")
f.close()

print("=" * 30)

f = open("f5a24_1.txt", "r", encoding="utf-8")
print(f"讀出檔案一定字數{f.read(7)}")
f.close

print("=" * 30)

f = open("f5a24_1.txt", "r", encoding="utf-8")
print("讀出檔案每一行")
for each in f:
    print(each)
f.close