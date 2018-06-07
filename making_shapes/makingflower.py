import turtle

def draw_flower() :
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(3)

    brad.pu()
    brad.setpos(-200,0)
    brad.pd()
    
    for i in range(1,37) :
        brad.left(35)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(145)
        brad.forward(50)
        brad.right(35)
        brad.forward(50)
        brad.right(10)
    brad.seth(270)
    brad.forward(200)
    
    window.exitonclick()

draw_flower()
