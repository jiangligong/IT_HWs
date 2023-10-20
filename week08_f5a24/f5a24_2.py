print("f5a24 黎家暉")

class Employee :
    def __init__(self) :
        self.cut_tree = 3

class Andy(Employee) :
    def __init__(self , get_gold) :
        super().__init__()
        self.get_gold = get_gold

    def getDetails(self) :
        print("===getDetails===")
        print(f"tree:{self.cut_tree}")
        print(f"gold:{self.get_gold}")

andy = Andy(1)
andy.getDetails()
