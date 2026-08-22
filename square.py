import turtle

turtle.Screen().bgcolor("purple")
turtle.Screen().setup(300,400)

square = turtle.Turtle()
for i in range(4):
    square.forward(100)
    square.right(90)

turtle.done()