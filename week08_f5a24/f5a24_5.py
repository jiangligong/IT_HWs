print("f5a24 黎家暉")

student_list = ["F5A:01 何曉婷",
                "F5A:02 阮麗燕",
                "F5A:03 林思琪",
                "F5A:04 林森麗",
                "F5A:05 梁倚心",
                "F5A:06 陳安妮",
                "F5A:07 廖昭穎",
                "F5A:08 何一平",
                "F5A:09 岑柏健",
                "F5A:10 李俊宇",
                "F5A:11 李健豪",
                "F5A:12 李景霖",
                "F5A:13 林宇洋",
                "F5A:14 林  峰",
                "F5A:15 林晉琪",
                "F5A:16 唐俊賢",
                "F5A:17 夏德忠",
                "F5A:18 容梓薺",
                "F5A:19 徐瑋伸",
                "F5A:20 陳  宏",
                "F5A:21 楊堉棋",
                "F5A:22 劉嘉樂",
                "F5A:23 鄧嘉琛",
                "F5A:24 黎家暉",
                "F5A:25 蕭振祐",
                "F5A:26 蘇子健"]

subjuct_list = ["1.中文" , "2.英文" , "3.數學" , "4.物理" , "5.化學" , "6.生物" ,
                "7.體育" , "8.資訊" , "9.美術" , "10.宗品" , "11.音樂" , "12.會話"]



class student :
    def __init__(self , name , subject , score) :
        self.name = name
        self.subject = subject
        self.score = score

    def speak(self) :
        print(f"{self.name} {self.subject}考了{self.score}分")

for i in range(26) :
    print(student_list[i])

while True :

    stu = int(input("請輸入你的學號:"))

    if stu in range(1 , 27) :

        stu = student_list[stu - 1]
        stu = stu[7:]

        for i in range(12) :
            print(subjuct_list[i])

        while True :
            sub = int(input("請輸入你的科目:"))

            if sub in range(1 , 13) :

                sub = subjuct_list[sub - 1]
                sub = sub[-2:]

                while True :

                    sco = float(input("請輸入你的分數:"))

                    if sco in range(101) :

                        break

                    else :
                        print("這不在0-100分的範圍内")

            else :
                print("沒有這個科目")
            
            break

    else :
        print("這并不是你的學號")

    break

student = student(stu , sub , sco)
student.speak()