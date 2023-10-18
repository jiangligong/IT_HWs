print("f5a24 黎家暉")

class student :
    def __init__(self , name , subject , score) :
        self.name = name
        self.subject = subject
        self.score = score

    def speak(self) :
        print(f"{self.name} {self.subject}考了{self.score}分")

s = student(str(input("请输入你的名字")) ,
           str(input("请输入你的科目")) ,
           float(input("你的科目考了多少分")))
s.speak()