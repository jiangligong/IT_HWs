print("f5a24 黎家暉")

class Employee() :
    def work(self) :
        print("Employee work")

class Andy(Employee) :
    def work(self) :
        print("Andy work")

class Joy(Employee) :
    def work(self) :
        print("Joy work")

w = Employee()
w1 = Andy()
w2 = Joy()

w.work()
w1.work()
w2.work()