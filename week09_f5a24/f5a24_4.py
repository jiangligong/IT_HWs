print("f5a24 黎家暉")

f = open("poem.txt", "r+")
f.write("白日依山盡，黃河入海流。欲窮千里目，更上一層樓。")
f.seek(4, 0)
print(f.readline(12))
f.close