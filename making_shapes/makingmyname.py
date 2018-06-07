import turtle

def draw_myname() :
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.speed(1)

    brad.pu()
    brad.setpos(-50, 0)
    brad.pd()
    brad.left(90)
    brad.forward(100)
    brad.setpos(-50, -5)
    brad.right(60)
    brad.forward(60)

    window.exitonclick()

draw_myname()
