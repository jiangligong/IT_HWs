print("f5a24 黎家暉")

def even_list() :
    global even_list
    even_list = []
    even_list.append(list[::2])
    return even_list

integer = int(input("請輸入一個正整數："))
list = []

for i in range(integer + 1) :
    list.append(i)

even_list()
print(f"列印 0~{integer}內的所有偶數(包括0)組成的列表\n{even_list}")
