from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 240)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)