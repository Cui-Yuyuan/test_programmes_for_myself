import random,turtle,math
print("please notice that all the nums should be integers",end="")
print("or\n the program may run incorrectly")
print("input create num(row),num(line),num(size)")
r=int(input())
l=int(input())
s=int(input())
print("input start position(x,y),using enter to separate two numbers")
x=int(input())
y=int(input())
print("input pensize&speed")
sz=int(input())
v=int(input())
def stps(a,b):
	turtle.penup()
	turtle.setpos(a,b)
	turtle.pendown()
	
def fd2(s):
    turtle.fd(2*s)
    
def fds2(s):
    turtle.fd(math.sqrt(2)*s)
    
def cubegen(r,s):
	for __ in range(r):
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
        
turtle.speed(v)
turtle.pensize(sz)

stps(x,y)
col=["#afff79","#81efa8","#8ade70","#8eefac","#eeee01","#e0729b","#039982","#a7890b"] #need updating
for j in range(1,1+l):
    cubegen(r,s)
    stps(stx+3*j*s,sty+j*s)
