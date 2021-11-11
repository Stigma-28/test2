import turtle as t
import ModuleStar2
import math

t.shape('turtle')
t.title('중국 국기')
t.penup()



t.setup(600,400) #중국 국기의 비율은 가로:세로 = 3:2 
t.bgcolor("red")

t.goto(-260,120)
r1 = 2*(60*math.sin(math.pi/180*72)) #큰 별의 선 하나 길이
ModuleStar2.Star(r1,'yellow')

def GoandRight():
    t.forward(20)
    t.right(180-18)
    

t.goto(-100,160)
t.right(90 + math.degrees(math.acos(3/34**0.5)))
GoandRight()
r2 = 2*(20*math.sin(math.pi/180*72)) #작은 별의 선 하나 길이
ModuleStar2.Star(r2,'yellow')

t.home()
t.goto(-60,120)
t.right(90 + math.degrees(math.atan(7)))
GoandRight()
ModuleStar2.Star(r2,'yellow')

t.home()
t.goto(-60,60)
t.left(90 + math.degrees(math.acos(2/7)))
GoandRight()
ModuleStar2.Star(r2,'yellow')

t.home()
t.goto(-100,20)
t.left(90 + math.degrees(math.atan(5/4)))
GoandRight()
ModuleStar2.Star(r2,'yellow')

t.hideturtle()
t.done()












