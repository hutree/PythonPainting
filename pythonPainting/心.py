import turtle
import time
Name=['L','J']
def draw_circle():
    for i in range (200):
        turtle.right(1)
        turtle.forward(1)
def draw_love():
    turtle.color('red','pink')
    turtle.pensize(2)
    turtle.speed(1000)
    turtle.goto(0,0)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(112)
    draw_circle()
    turtle.left(120)
    draw_circle()
    turtle.forward(112)
    turtle.end_fill()
def draw_name():
    turtle.pensize(5)
    turtle.up()
    turtle.goto(-50,142.7)
    if Name[0]=='L':
        turtle.left(50)
        turtle.down()
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(25)
    turtle.up()
    turtle.goto(37.5,142.7)
    if Name[1]=='J':
        turtle.down()
        turtle.forward(25)
        turtle.up()
        turtle.goto(50,142.7)
        turtle.right(90)
        turtle.down()
        turtle.forward(60)
        for i in range (20):
            turtle.right(7.8)
            turtle.forward(0.3)
        turtle.forward(8)
        turtle.up()
    turtle.goto(100,-10)
    turtle.write("happy birthday")


draw_love()
draw_name()
