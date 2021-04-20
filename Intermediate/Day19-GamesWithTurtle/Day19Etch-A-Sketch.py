from turtle import Turtle, Screen
# import random

tim = Turtle()
screen = Screen()


def move_forwards():
    """Move forwards."""
    tim.forward(10)


def move_backwards():
    """Move Backwards."""
    tim.backward(10)


def move_counter_clockwise():
    """Move_counter_clockwise."""
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    """Move_counter_clockwise."""
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    """Clear drawing."""
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
