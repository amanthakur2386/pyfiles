import turtle
t=turtle
t.position()
t.speed(0)
i=1
while i<=300:
    t.bgcolor('black')
    t.pencolor('blue')
    t.fd(50+i)
    t.rt(120.999)
    i=i+1



turtle.exitonclick()