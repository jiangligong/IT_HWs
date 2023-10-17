print("f5a24 黎家暉")

import turtle as t

screen = t.Screen()

t.pensize(5)
t.pencolor("#ff8888")

# 多邊形繪製
t.pu()
t.setx(-300)
t.sety(300)
t.pd()
side_length = int(input("請輸入多邊形的邊長數量："))
def hexagon() :
    t.fd(100)
    t.rt((360 / side_length))

for i in range(side_length) :
    hexagon()

# 圓形繪製
t.pu()
t.setx(0)
t.sety(300)
t.pd()
radius = float(input("請輸入圓的半徑："))
t.circle(radius * -10)

# 變色正方形繪製
t.pu()
t.setx(200)
t.sety(300)
t.pd()
for color in ("yellow", "red", "green", "blue") :
    t.color(color)
    t.fd(100)
    t.rt(90)

t.exitonclick()