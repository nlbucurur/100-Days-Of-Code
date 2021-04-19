import random
from turtle import Turtle, Screen


def go_to_start(participant, i, color):
    participant.color(color)
    participant.penup()
    participant.goto(x=-230, y=-150 + i)


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race (red, orange, yellow, green,"
                                                           "cyan, blue or violet)? Enter a color: ")
is_race_on = False

red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
cyan = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
violet = Turtle(shape="turtle")
i = 0
turtles = [red, orange, yellow, green, cyan, blue, violet]
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

for j in range(len(colors)):
    go_to_start(turtles[j], i, colors[j])
    i += 50

l = 0

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
