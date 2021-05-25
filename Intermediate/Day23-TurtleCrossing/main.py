import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# TODO Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the
#  turtle north. If you get stuck, check the video walkthrough in Step 3.

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Arrival at the goal?
    if player.on_top():
        player.go_home()
        car_manager.level_up()
        scoreboard.update_score()

    # There is a collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game()


screen.exitonclick()
