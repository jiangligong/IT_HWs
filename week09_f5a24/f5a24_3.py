print("f5a24 黎家暉")

f = open("poem.txt", "w")
f.write("白日依山盡，黃河入海流。欲窮千里目，更上一層樓。")
f.close

f = open("math_score.txt", "w")
score = ["古同學：78分 \n", "何同學：83分 \n", "巫同學：87分"]
f.writelines(score)
f.close

f = open("poem.txt", "r")
print(f.read())
f.close

f = open("math_score.txt", "r", encoding="ANSI")
content = f.readlines()
print(content)
for i in content:
    print(i)
f.close