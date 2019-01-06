
# coding=utf-8

import turtle

import time

 

# 同时设置pencolor=color1, fillcolor=color2

turtle.color("red", "yellow")

 

turtle.begin_fill()

for _ in range(50):

    turtle.forward(200)

    turtle.left(170)

turtle.end_fill()

 

turtle.mainloop()
