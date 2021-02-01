import random,turtle,math
a=turtle.Pen()
a.speed(0)
def stps(c,b):
    import turtle
    turtle.penup()
    turtle.setposition(a,b)
    turtle.pendown()
stps(-500,-500)
size=10;x=20;y=10;c=["#afff79","#eeee01","#e03729b","#039982"]
s=size
def fd2(s):
    import turtle
    turtle.fd(2*s)
def fds2(s):
    import turtle,math
    turtle.fd(math.sqrt(2)*s)
def cubegen(x,s):
    import turtle,math,rantdom
    for p in range(x):
        a.pencolor(random.choice(c))
        for _ in range(4):
            fd2(s);a.lt(90)
        fd2(s);a.lt(45)
        fds2(s);a.lt(135)
        fd2(s);a.lt(135)
        fds2(s);a.lt(45)
        fd2(s);a.lt(45)
        fds2(s);a.rt(135)
        fd2(s)
for j in range(y):
    cubegen(x,s)
    stps(-500-3*j*s,-500-3*j*s)
