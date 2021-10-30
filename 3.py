#Assignment 5
import turtle

turtle.speed(1)
turtle.bgcolor('black')

turtle.pensize(1)
turtle.color("black")
turtle.pos()
x = 0
y = 0
n = 3
f = 9
while True:
    for i in ['red', 'yellow', 'purple', 'blue', 'green', 'orange', 'white']:    
        for j in range(n):
            turtle.forward(f)
            turtle.left(360/n)
        turtle.color(i)
        n += 1
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        x -= 7
        y -= 7
        f += 10
