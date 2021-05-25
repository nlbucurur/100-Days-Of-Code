from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.setheading(90)
        self.go_home()

    def go_home(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def on_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
