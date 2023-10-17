print("f5a24 黎家暉")

import turtle as t

def forward_100() :
    t.pensize(5)
    t.pencolor("#069")
    t.fd(100)

def right_90( ) :
    t.rt(90)

for i in range(4) :
    forward_100()
    right_90()

t.exitonclick()