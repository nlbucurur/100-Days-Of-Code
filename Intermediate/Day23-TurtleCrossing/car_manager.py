from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.new_vel = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.new_vel)

    def level_up(self):
        self.new_vel += MOVE_INCREMENT
