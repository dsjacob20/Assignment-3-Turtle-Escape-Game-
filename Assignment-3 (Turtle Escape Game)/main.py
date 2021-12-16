
 #BEGINS PROGRAM
# Welcome screen
print()
print("      !WELCOME!")
print()
input("Click ENTER to begin ")
print()


print()
print("Their will be 2 turtles in this bet.")
print("Give both of them a name and colour...")

# input info for turtle 1
print()
loop = True
while loop==True:
    t1= input("Name of turtle 1, ")
    print("Please DO NOT select GREY, GREEN, or WHITE")
    c1= input("Colour for turtle 1, ")

    if c1 in ('grey','Grey','GREY','green','Green','GREEN,''white','White','WHITE'):
        print()
        print("Please DO NOT choose this colour")
        print("Reinput the turtle-1 information")
        loop = True
        print()
        
    else:
        print(t1, "=", c1)
        loop = False


# input info for turtle 2
print()
loop = True
while loop==True:
    t2= input("Name of turtle 2, ")
    print("Please DO NOT select GREY, GREEN, or WHITE")
    c2= input("Colour for turtle 2, ")

    if c2 in ('grey','Grey','GREY','green','Green','GREEN,''white','White','WHITE'):
        print()
        print("Please DO NOT choose this colour")
        print("Reinput the turtle-2 information")
        loop = True
        print()
    elif t2 == t1:
        print()
        print("This NAME is alredy taken")
        print("Reinput the turtle-2 information")
        loop = True
        print()   
    else:
        print(t2, "=", c2)
        loop = False

print()
print ("Name", '\t', "Colour")
print ("-----", '\t', "-----")
print (t1.upper(), '\t', c1.lower())
print (t2.upper(), '\t', c2.lower())

t1=t1.upper()
t2=t2.upper()

print()
print("ALL SET")
input("Click ENTER to begin ")

print()
print()

# GAME BEGINS!!!!
def still_in_screen(t1, t2, r):

    turtleX = t1.xcor()
    turtleY = t1.ycor()
    tX = t2.xcor()
    tY = t2.ycor()
 
    loop = True
    if turtleX > 300 or turtleX <-300:
        loop = False
        r.goto(0,0)
        r.write("STOP", move=False, align="left", font=("Arial", 40, "bold"))
        wn.exitonclick()
        print("And the Winner is...")
        print(t1," - ", c1)
    if turtleY > 300 or turtleY <-300:
        loop = False
        r.goto(0,0)
        r.write("STOP", move=False, align="left", font=("Arial", 40, "bold"))
        wn.exitonclick()
        print("And the Winner is...")
        print(t1," - ", c1)
    if tX > 300 or tX <-300:
        loop = False
        r.goto(0,0)
        r.write("STOP", move=False, align="left", font=("Arial", 40, "bold"))
        wn.exitonclick()
        print("And the Winner is...")
        print(t2," - ", c2)
    if tY > 300 or tY < -300:
        loop = False
        r.goto(0,0)
        r.write("STOP", move=False, align="left", font=("Arial", 40, "bold"))
        wn.exitonclick()
        print("And the Winner is...")
        print(t2," - ", c2)

    return loop


import turtle
wn = turtle.Screen()  
wn.bgcolor("green")


# Referee
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

#players
import random

t1 = turtle.Turtle() 
t1.shape("turtle") 
t1.color(c1)
t1.pensize(2)
t1.right(90)
t1.forward(10)

t2 = turtle.Turtle() 
t2.shape("turtle") 
t2.color(c2)
t2.pensize(2)
t2.left(90)
t2.forward(10)

win = turtle.Screen()

loop = True
while still_in_screen(t1,t2,r):
    coin1 = random.randrange (0,2)
    if coin1 == 0:
        t1.left(90)
        t1.forward(50)
    else:
        t1.right(90)
        t1.forward(50)
    

    coin2 = random.randrange (0,2)
    if coin2 == 0:
        t2.left(90)
        t2.forward(50)
    else:
        t2.right(90)
        t2.forward(50)


print()
print()











