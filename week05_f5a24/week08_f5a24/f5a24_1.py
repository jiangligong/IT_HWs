print("f5a24 黎家暉")

class Employee :
    def __init__(self) :
        self.working_hour = 0

    def work(self) :
        self.working_hour += 1
        print(f"working: {self.working_hour}")

class this_test_class :
    getName = "Max"
    
    def __init__(self) :
        self.getNameFrominit = "Max__init__"
        pass

andy = Employee()
andy.work()
print(andy.working_hour, "\n")

print("=" * 20)

task = this_test_class()
task.sendName = "Max_sendName"

print("方法一：把屬性定義寫在init外面")
print(task.getName)

print("方法二：把屬性定義寫在init內")
print(task.getNameFrominit)

print("方法三：自己給屬性與參數")
print(task.sendName)