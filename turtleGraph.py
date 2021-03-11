import turtle as tk
import random
tk.speed(10)
line = tk.Turtle()
line.pensize(5)
a = 5
color1 = ["#980654","#123456","#234567","#654321","#987678","#456372"]
# tk.bgcolor("black")
a = 0
aa = 0
i = 10
r = 250
for j in range(15):
    line.penup()
    line.goto(0,0)
    line.left(aa)
    line.forward(r+a)
    line.left(90)
    line.pendown()
    line.forward(r+a)
    line.left(90)
    line.forward(2*r+a)
    line.left(90)
    line.forward(2*r+a)
    line.left(90)
    line.forward(2*r+a)
    line.left(90)
    line.forward(r+a)
    aa =360/30
    # a += 10
tk.done()
