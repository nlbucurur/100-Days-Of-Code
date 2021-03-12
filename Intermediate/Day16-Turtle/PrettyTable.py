"""import another module."""

# from turtle import turtle, screen

# timmy = turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "gold1")
# timmy.forward(100)
#
# my_screen = screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclic()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("pokemon name", ["pikachu", "squirtle", "charmander"])
table.add_column("type", ["electric", "water", "fire"])
table.align = "l"

print(table)