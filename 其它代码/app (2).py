import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x - width/2, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(color, size, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_birthday_cake():
    turtle.speed(2)
    turtle.bgcolor("lightblue")

    # Draw cake base
    draw_rectangle("chocolate", 200, 100, 0, -150)

    # Draw candles
    for x in range(-90, 110, 50):
        draw_rectangle("pink", 10, 40, x, -50)
        draw_triangle("red", 20, x, -10)

    # Draw flame
    draw_circle("yellow", 5, 20, 30)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_birthday_cake()
    