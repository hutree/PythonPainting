#SquareSpiral1.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")


my_name=turtle.textinput("输入你的姓名","你的名字？")
colors=["red","yellow","purple","blue"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(my_name,font=("Arial",int((x+4)/4),"bold"))
    t.left(92)


print("####结束####")
