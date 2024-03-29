import turtle as t
import turtle
import random

tim = t.Turtle()
turtle.colormode(255)


def random_color():
    """Choose a rgb color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(10)

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

