import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(1000,900)

polygon=turtle.Turtle()
for i in range(7):
    polygon.forward(90)
    polygon.right(50)

turtle.done()