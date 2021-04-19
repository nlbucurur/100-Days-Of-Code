import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    """Choose a rgb color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(size_of_gap, radius):
    """Make a spirograph."""
    for _ in range(0, 361, size_of_gap):
        tim.color(random_color())
        tim.setheading(_)
        tim.circle(radius)


spirograph(20, 100)

screen = t.Screen()
screen.exitonclick()
