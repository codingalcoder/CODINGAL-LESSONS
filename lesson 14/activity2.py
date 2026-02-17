import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen(). setup(300,400)
polygon = turtle.Turtle()

forward_length = 100
turtle.forward(forward_length)
turtle.left (120)
turtle.forward(forward_length)
turtle.left(120)
turtle.forward(forward_length)

turtle.penup()
turtle.right(150)
turtle.forward(50)

turtle.pendown()
turtle.right(90)
turtle.forward(forward_length)

turtle.right(120)
turtle.forward(forward_length)

turtle.right(120)
turtle.forward(forward_length)

turtle.done()