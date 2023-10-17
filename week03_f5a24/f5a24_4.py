print("f5a24 黎家暉")

import random

randomNo = random.randint(1,100)

print("請猜1-100中的隨機的年齡是多少，你共有5次機會\n")

chance = 5

while True :

    if chance == 0 :
        exit("好遺憾你沒有機會了")
    else :
        guess = int(input("請輸入你猜測的年齡："))

    try :
        if guess == randomNo :
            print("你猜對了\n")
            break
            
        elif guess < randomNo :
            chance -= 1
            print(f"你猜小了,還有{chance}次機會\n")
        
        elif guess > randomNo :
            chance -= 1
            print(f"你猜大了,還有{chance}次機會\n")
    except :
        break

print(f"隨機年齡是{randomNo}")