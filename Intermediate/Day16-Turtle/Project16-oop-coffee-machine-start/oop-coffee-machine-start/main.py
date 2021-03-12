from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = Menu()
coffeeMK = CoffeeMaker()
money = MoneyMachine()

# print(choice.find_drink(command))

end = False

while not end:
    command = input(f"What would you like? {choice.get_items()}: ").lower()

    if command == 'report':
        coffeeMK.report()
        money.report()
    elif command == 'off':
        end = True
    else:
        drink = choice.find_drink(command)
        enough = coffeeMK.is_resource_sufficient(drink)

        if enough and money.make_payment(drink.cost):
            coffeeMK.make_coffee(drink)