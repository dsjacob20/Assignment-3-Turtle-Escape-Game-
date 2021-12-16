

import turtle
wn = turtle.Screen()  
wn.bgcolor("green")

r = turtle.Turtle() 
r.shape("turtle") 
r.color("grey")
r.pensize(4)

r.penup()
r.goto(-300,300)
r.left(180)

r.pendown()
r.begin_fill()
for x in range(4):
    r.left(90)
    r.forward(600)
r.end_fill()

r.color("white")
r.penup()
r.goto(-320,315)
r.left(150)

