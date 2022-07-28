import turtle
t=turtle
t.position()
t.bgcolor('black')
t.speed(0)
t.pencolor('cyan')
i=1
while i<=300:
    t.fd(25+i)
    t.rt(45)
    t.rt(170)
    i=i+1



t.exitonclick()