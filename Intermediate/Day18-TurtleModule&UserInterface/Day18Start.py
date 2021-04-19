from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("orange")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_a_figure(tim):
    count = 0
    tim.pendown()
    tim.pencolor(random.choice(color))
    while count < i:
        tim.forward(100)
        tim.right(360 / i)
        count += 1


for i in range(3, 10):
    draw_a_figure(tim)

screen = Screen()
screen.exitonclick()
