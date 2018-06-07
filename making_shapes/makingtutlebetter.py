import turtle

def draw_shapes() :
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()  

def draw_square() :
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    count = 0
    while(count < 4) :
        brad.forward(100)
        brad.right(90)
        count += 1

def draw_circle() :
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle() :
    fido = turtle.Turtle()
    fido.shape("turtle")
    fido.color("black")
    fido.speed(2)
    count = 0
    while(count < 3) :
        fido.forward(60)
        fido.left(120)
        count += 1

draw_shapes()



