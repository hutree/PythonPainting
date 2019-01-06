import turtle as t
import math as m 

t.pensize(4) # 设置画笔的大小
t.colormode(255) # 设置GBK颜色范围为0-255
t.color((0,0,255),"blue") # 设置画笔颜色和填充颜色(pink)
t.setup(800,600) # 设置主窗口的大小为840*500
t.speed(10) # 设置画笔速度为10
#头部
t.hideturtle()
t.pu() # 提笔
t.goto(-50,0) # 画笔前往坐标(0,0)
t.seth(150)
t.pd() # 下笔
t.begin_fill()
t.color(0,0,255)
for i in range(300):
  t.rt(1)
  t.forward(2*m.pi*100/360)
t.seth(0)
t.backward(10)

t.seth(30)
for i in range(300):
  t.lt(1)
  t.forward(2*m.pi*80/360)
t.seth(0)
t.backward(10)
t.end_fill()
#眼睛
t.pu()
t.begin_fill()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(-15,40*m.sqrt(3)+60)
t.pd()
t.circle(15)
t.color(255,255,255)
t.end_fill()

t.pu()
t.begin_fill()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(-15,40*m.sqrt(3)+60)
t.pd()
t.circle(5)
t.color(0,0,0)
t.end_fill()

t.pu()
t.begin_fill()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(15,40*m.sqrt(3)+60)
t.pd()
t.circle(15)
t.color(255,255,255)
t.end_fill()

t.pu()
t.begin_fill()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(15,40*m.sqrt(3)+60)
t.pd()
t.circle(5)
t.color(0,0,0)
t.end_fill()


#鼻子
t.pu()
t.pensize(3)
t.pencolor(255,0,0)
t.goto(0,40*m.sqrt(3)+40)
t.pd()
t.begin_fill()
t.color(255,0,0)
t.circle(10)
t.end_fill()
#嘴巴
t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(0,40*m.sqrt(3)+40)
t.pd()
t.seth(-90)
t.forward(50)
t.pu()
t.goto(-50,90-10*m.sqrt(3))
t.seth(-30)
t.pd()
for i in range(60):
 t.lt(1)
 t.forward(2*m.pi*100/360)
 
 
#胡须
t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(-30,40*m.sqrt(3)+25)
t.seth(0)
t.pd()
t.backward(40)

t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(-30,40*m.sqrt(3)+15)
t.pd()
t.seth(30)
t.backward(40)

t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(-30,40*m.sqrt(3)+35)
t.pd()
t.seth(-30)
t.backward(40)

t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(30,40*m.sqrt(3)+25)
t.seth(0)
t.pd()
t.forward(40)



t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(30,40*m.sqrt(3)+35)
t.pd()
t.seth(30)
t.forward(40)

t.pu()
t.pensize(3)
t.pencolor(0,0,0)
t.goto(30,40*m.sqrt(3)+15)
t.pd()
t.seth(-30)
t.forward(40)


# a=0.4
# for i in range(360):
   # if 0<=i<90 or 180<=i<270:
       # a=a+0.008
       # t.lt(1) #向左转3度
       # t.fd(a) #向前走a的步长
   # else:
       # a=a-0.008
       # t.lt(1)
       # t.fd(a)
t.done()
