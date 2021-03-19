import random,turtle,math
print("input create number(row),num(line),num(size)")
x=10
y=5
s=20
print("input start position(x,y),using enter to separate two numbers")
stx=-200
sty=-180
print("input pensize")
psz=8
def stps(c,b):
	import turtle
	turtle.penup()
	turtle.setposition(c,b)
	turtle.pendown()
	
def fd2(s):
    turtle.fd(2*s)
    
def fds2(s):
    turtle.fd(math.sqrt(2)*s)
    
def cubegen(x,s):
    for __ in range(x):
        turtle.pencolor(random.choice(col))
        for _ in range(4):
            fd2(s);turtle.lt(90)
        fd2(s);turtle.lt(45)
        fds2(s);turtle.lt(135)
        fd2(s);turtle.lt(45)
        fds2(s);turtle.rt(135)
        fd2(s);turtle.rt(45)
        fds2(s);turtle.rt(45)
        fd2(s)
        
turtle.speed(0)
turtle.pensize(10)

stps(stx,sty)
col=["#afff79","#81efa8","#8ade70","#8eefac","#eeee01","#e0729b","#039982"]
for j in range(1,1+y):
    cubegen(x,s)
    stps(stx+3*j*s,sty+j*s)
