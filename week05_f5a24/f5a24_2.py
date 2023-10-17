print("f5a24 黎家暉")

print("""import四種範例介紹與用法：
    1.import 模組名稱
    2.import 模組名稱 as 模組別名
    3.from 模組名稱 import 模組名稱.模組成員名稱
    4.from 模組名稱 import *""")

print("範例1：import 模組名稱\n")
print("""import math
    print(math.pi)""")
import math
print(math.pi)

print("範例2：import 模組名稱 as 模組別名\n")
print("""import math as m
    print(m.pi)""")
import math as m
print(m.pi)

print("範例3：from 模組名稱 import 模組名稱.模組成員名稱")
print("""from math import pi
    print(pi)""")
from math import pi
print(pi)

print("範例4：from 模組名稱 import *")
print("""from math import *
    print(pi)
    print(math.factorial(5))""")
from math import *
print(pi)
print(math.factorial(5))