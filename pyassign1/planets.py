import math
from turtle import* 
speed(0)
colors=['blue', 'yellow', 'green', 'red', 'orange',
        'purple']

setup(800,800,0,0)
up()
goto(-75,350)
down()
bgcolor('black')
color('red')
write('太阳系模拟图',font=(64))

Mercury=Turtle()
Venus=Turtle()
Earth=Turtle()
Mars=Turtle()
Jupiter=Turtle()
Saturn=Turtle()                      #定义行星
up()
goto(50,-25)
down()
fillcolor('red')
begin_fill()
circle(25)
end_fill()
ht()                                # 画出太阳

def firstplace(planet,a,m):
      planet.shape('circle') 
      planet.up()
      planet.fd(a)
      planet.down()
      planet.color(colors[m])       # 行星的初始位置

def planet(planet,a,i):
      b=(a**2-50**2)**0.5
      x=a*math.cos(i*0.01)
      y=b*math.sin(i*0.01)
      planet.goto(x,y)
      planet.pensize(2)             # 行星的运动方程
      
firstplace(Mercury,100,0)
firstplace(Venus,140,1)
firstplace(Earth,180,2)
firstplace(Mars,220,3)
firstplace(Jupiter,260,4)
firstplace(Saturn,300,5)

for i in range(1000):
      planet(Mercury,100,18*i)
      planet(Venus,140,16*i)
      planet(Earth,180,14*i)
      planet(Mars,220,12*i)
      planet(Jupiter,260,10*i)
      planet(Saturn,300,8*i)
done()
