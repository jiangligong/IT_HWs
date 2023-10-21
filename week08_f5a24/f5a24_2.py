print("f5a24 黎家暉")

class initial_reward:
    def __init__(self):
        self.tree = 4
        self.stone = 2
        self.iron = 1
        self.gold = 0
        self.diamond = 0



class Backpack(initial_reward):
    def __init__(self):
        global backpack_quantity
        super().__init__()
        backpack_quantity = [self.tree, self.stone, self.iron, self.gold, self.diamond]


# 顯示背包內的物品
    def backpack(self):
        global backpack
        backpack = ["tree", "stone", "iron", "gold", "diamond"]
        print("\n你的背包中有：")
        for i in range(len(backpack)):
            print(f"{backpack[i]}:{backpack_quantity[i]}")
        print("\n", "=" * 30)
        start()



class Upgrade_tools:
    def tools_up(self):
        print(f"你手上的工具為{hand_tool}")
        print("""
            1.升為木鎬
            2.升為石鎬
            3.升為鐵鎬
            4.升為金鎬
            5.升為鑽鎬
            6.返回目錄
            """)
        
        tool = int(input("請輸入你想升級的工具編號："))
        if tool == 1:
            upgrade_tools.wood_pickaxe()
            
        elif tool == 2:
            upgrade_tools.stone_pickaxe()

        elif tool == 3:
            upgrade_tools.iron_pickaxe()

        elif tool == 4:
            upgrade_tools.gold_pickaxe()
        
        elif tool == 5:
            upgrade_tools.diamond_pickaxe()
        
        else:
            start()

# 升級成為木製工具
    def wood_pickaxe(self):
        global hand_tool
        print("升級成為木製工具需要tree*5")
        value = bool(input("確認合成？True/False: "))
        if hand_tool == "空手" and value == True:
            if backpack_quantity[0] >= 5:
                hand_tool = "木製工具"
                backpack_quantity[0] = backpack_quantity[0] - 5
                print(f"你手上的工具升級為{hand_tool}")
                start()

            else:
                print(f"你的{backpack[0]}不足5個")
                start()

        else:
            print("合成失敗原因：")
            print("你手上不是空手或你已取消升級")
            start()

# 升級成為石製工具
    def stone_pickaxe(self):
        global hand_tool
        print("升級成為石製工具需要tree*2及stone*3")
        value = bool(input("確認合成？True/False: "))
        if hand_tool == "木製工具" and value == True:
            if backpack_quantity[0] >= 2 and backpack_quantity[1] >= 3:
                hand_tool = "石製工具"
                backpack_quantity[0] = backpack_quantity[0] - 2
                backpack_quantity[1] = backpack_quantity[1] - 3
                print(f"你手上的工具升級為{hand_tool}")
                start()
            else:
                print(f"你的{backpack[0]}不足2個\n你的{backpack[1]}不足3個")
                start()

        else:
            print("合成失敗原因：")
            print("你手上不是木製工具或你已取消升級")
            start()

# 升級成為鐵製工具
    def iron_pickaxe(self):
        global hand_tool
        print("升級成為鐵製工具需要tree*2及iron*3")
        value = bool(input("確認合成？True/False: "))
        if hand_tool == "石製工具" and value == True:
            if backpack_quantity[0] >= 2 and backpack_quantity[2] >= 3:
                hand_tool = "鐵製工具"
                backpack_quantity[0] = backpack_quantity[0] - 2
                backpack_quantity[2] = backpack_quantity[2] - 3
                print(f"你手上的工具升級為{hand_tool}")
                start()
            else:
                print(f"你的{backpack[0]}不足2個\n你的{backpack[2]}不足3個")
                start()

        else:
            print("合成失敗原因：")
            print("你手上不是石製工具或你已取消升級")
            start()

# 升級成為金製工具
    def gold_pickaxe(self):
        global hand_tool
        print("升級成為金製工具需要tree*2及iron*3")
        value = bool(input("確認合成？True/False: "))
        if hand_tool == "鐵製工具" and value == True:
            if backpack_quantity[0] >= 2 and backpack_quantity[3] >= 3:
                hand_tool = "金製工具"
                backpack_quantity[0] = backpack_quantity[0] - 2
                backpack_quantity[3] = backpack_quantity[3] - 3
                print(f"你手上的工具升級為{hand_tool}")
                start()
            else:
                print(f"你的{backpack[0]}不足2個\n你的{backpack[3]}不足3個")
                start()

        else:
            print("合成失敗原因：")
            print("你手上不是鐵製工具或你已取消升級")
            start()

# 升級成為鑽製工具
    def diamond_pickaxe(self):
        global hand_tool
        print("升級成為鑽製工具需要tree*2及iron*3")
        value = bool(input("確認合成？True/False: "))
        if hand_tool == "金製工具" and value == True:
            if backpack_quantity[0] >= 2 and backpack_quantity[4] >= 3:
                hand_tool = "鑽製工具"
                backpack_quantity[0] = backpack_quantity[0] - 2
                backpack_quantity[4] = backpack_quantity[4] - 3
                print(f"你手上的工具升級為{hand_tool}")
                start()
            else:
                print(f"你的{backpack[0]}不足2個\n你的{backpack[4]}不足3個")
                start()

        else:
            print("合成失敗原因：")
            print("你手上不是金製工具或你已取消升級")
            start()



class Cut_tree:
    def selector(self):
        print(f"你手上的工具為{hand_tool}")
        if hand_tool == "空手":
            cut_tree.none_efficiency()

        elif hand_tool == "木製工具":
            cut_tree.wood_efficiency()

        elif hand_tool == "石製工具":
            cut_tree.stone_efficiency()

        elif hand_tool == "鐵製工具":
            cut_tree.iron_efficiency()

        elif hand_tool == "金製工具":
            cut_tree.gold_efficiency()

        elif hand_tool == "鑽製工具":
            cut_tree.diamond_efficiency()

    def none_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 16:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入16次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")

    def wood_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 14:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入14次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")

    def stone_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 12:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入12次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")

    def iron_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 8:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入8次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")

    def gold_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 6:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入6次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")

    def diamond_efficiency(self):
        cut_time = 0
        while True:
            if cut_time == 4:
                backpack_quantity[0] += 1
                print("伐木成功! tree+1")
                start()
            else :
                cut = str(input(f"伐木請輸入4次c 第{cut_time + 1}次:"))
                if cut == "c":
                    cut_time += 1
                else:
                    print("輸入c!!!")



class Break_stone:
    def selector(self):
        if hand_tool == "空手":
            print("空手挖不了石頭")
            upgrade_tools.tools_up()

        elif hand_tool == "木製工具":
            broke_stone.wood_efficiency()

        elif hand_tool == "石製工具":
            broke_stone.stone_efficiency()

        elif hand_tool == "鐵製工具":
            broke_stone.iron_efficiency()

        elif hand_tool == "金製工具":
            broke_stone.gold_efficiency()

        elif hand_tool == "鑽製工具":
            broke_stone.diamond_efficiency()

    def wood_efficiency(self):
        broke_time = 0
        while True:
            if broke_time == 14:
                backpack_quantity[1] += 1
                print("掘石成功! stone+1")
                start()
            else :
                bre = str(input(f"掘石請輸入14次b 第{broke_time + 1}次:"))
                if bre == "b":
                    broke_time += 1
                else:
                    print("輸入b!!!")

    def stone_efficiency(self):
        broke_time = 0
        while True:
            if broke_time == 12:
                backpack_quantity[1] += 1
                print("掘石成功! stone+1")
                start()
            else :
                bre = str(input(f"掘石請輸入12次b 第{broke_time + 1}次:"))
                if bre == "b":
                    broke_time += 1
                else:
                    print("輸入b!!!")

    def iron_efficiency(self):
        broke_time = 0
        while True:
            if broke_time == 8:
                backpack_quantity[1] += 1
                print("掘石成功! stone+1")
                start()
            else :
                bre = str(input(f"掘石請輸入8次b 第{broke_time + 1}次:"))
                if bre == "b":
                    broke_time += 1
                else:
                    print("輸入b!!!")

    def gold_efficiency(self):
        broke_time = 0
        while True:
            if broke_time == 6:
                backpack_quantity[1] += 1
                print("掘石成功! stone+1")
                start()
            else :
                bre = str(input(f"掘石請輸入6次b 第{broke_time + 1}次:"))
                if bre == "b":
                    broke_time += 1
                else:
                    print("輸入b!!!")

    def diamond_efficiency(self):
        broke_time = 0
        while True:
            if broke_time == 4:
                backpack_quantity[1] += 1
                print("掘石成功! stone+1")
                start()
            else :
                bre = str(input(f"掘石請輸入4次b 第{broke_time + 1}次:"))
                if bre == "b":
                    broke_time += 1
                else:
                    print("輸入b!!!")



class Craft:
    def selector(self):
        print("""
              1.stone_to_iron
              2.iron_to_gold
              3.gold_to_diamond
              4.返回
              """)
        change = input("請輸入你想轉換的編號：")
        if change == "1":
            craft.stone_to_iron()
        elif change == "2":
            craft.iron_to_gold()
        elif change == "3":
            craft.gold_to_diamond()
        else:
            start()

    def stone_to_iron(self):
        value = bool(input(f"確定由{backpack[1]}轉換為{backpack[2]}??True/False"))
        if value == True and backpack_quantity[2] >= 4:
            backpack_quantity[1] -= 4
            backpack_quantity[2] += 1
            print(f"你已經成功合成{backpack[2]}")
            start()
        else:
            print((f"你手上{backpack[2]}不足或你已取消合成"))

    def iron_to_gold(self):
        value = bool(input(f"確定由{backpack[2]}轉換為{backpack[3]}??True/False"))
        if value == True and backpack_quantity[2] >= 4:
            backpack_quantity[2] -= 4
            backpack_quantity[3] += 1
            print(f"你已經成功合成{backpack[3]}")
            start()
        else:
            print((f"你手上{backpack[2]}不足或你已取消合成"))

    def gold_to_diamond(self):
        value = bool(input(f"確定由{backpack[3]}轉換為{backpack[4]}??True/False"))
        if value == True and backpack_quantity[3] >= 4:
            backpack_quantity[3] -= 4
            backpack_quantity[4] += 1
            print(f"你已經成功合成{backpack[4]}")
            start()
        else:
            print((f"你手上{backpack[3]}不足或你已取消合成"))



def start():
    print("""
          1.離開遊戲
          2.查看背包
          3.升級工具
          4.砍伐樹木
          5.挖掘石頭
          6.資源合成
          """)
    want_to_do = input("請輸入你想進行動作的編號:")

    if want_to_do == "1":
        exit("拜拜")
    
    elif want_to_do == "2":
        backpack.backpack()

    elif want_to_do == "3":
        upgrade_tools.tools_up()

    elif want_to_do == "4":
        cut_tree.selector()

    elif want_to_do == "5":
        broke_stone.selector()

    elif want_to_do == "6":
        craft.selector()
    else:
        print("並不存在這個編號")
        start()



hand_tool = "空手"
backpack = Backpack()
upgrade_tools = Upgrade_tools()
cut_tree = Cut_tree()
broke_stone = Break_stone()
craft = Craft()
start()
