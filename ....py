import turtle,random
a=turtle.Pen();a.speed(0)
col=["#acad28","#626382","#b01fff"    \
,"#272872"]
for _ in range(0,2000,25):
    for __ in range(0,3000,25):
        a.penup();a.setpos(-600+_,-500+__);a.pendown()
        a.dot(random.randint(2,20),random.choice(col))
