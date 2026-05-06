import turtle

turtle.color("green")
speed=0

i=0
j=0
while i<4:
    turtle.forward(100)
    turtle.right(90)
    i+=1

turtle.setheading(60)
turtle.forward(100)
turtle.setheading(-60)
turtle.forward(100)

turtle.done()