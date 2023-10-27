print("f5a24 黎家暉")

f = open("f5a24_2.txt", "w")
f.write("這是寫入模式\n")
f.write("它允許我們寫入一個指定檔案中\n")
f.write("你/妳可以在目錄中查看此新建立檔案")
f.close

print("已完成建立和寫入文字到檔案f5xxx_2.txt裡")

f = open("f5a24_2a.txt", "w")
f.write("這是寫入模式\n")
f.write("它允許我們寫入一個指定檔案中\n")
f.write("你/妳可以在目錄中查看此新建立檔案")
f.close

print("已完成建立和寫入文字到檔案f5xxx_2a.txt裡")

f = open("f5a24_2a.txt", "a")
f.write("\n這將會加入這一行")
f.close

print("已完成開啟和加入文字到檔案f5xxx_2a.txt裡")