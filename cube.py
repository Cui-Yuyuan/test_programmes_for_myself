import random,turtle,math
a=turtle.Pen()
a.speed(0)
def stps(a,b):
    turtle.penup()
    turtle.setposition(a,b)
    turtle.pendown()
a.stps(-500,-500)
size=10;x=20;y=10;c=["#afff79","#eeee01","#e03729b","#039982"]
def fd2(size):
    turtle.fd(2*size)
def fds2(size):
    turtle.fd(math.sqrt(2)*size)
def cubegen(n,size):
    for ii in range(n):
        a.pencolor(random.choice(c[]))
        for iii in range
    
