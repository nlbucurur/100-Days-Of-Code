MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough (water, water_sol, milk, milk_sol, coffee, coffee_sol):
    """Verify if resources are enough."""
    are_enough = True
    if water_sol <= water and milk_sol <= milk and coffee_sol <= coffee:
        return are_enough
    else:
        are_enough = False
        return are_enough


def payment():
    """Ask for payment."""
    print('Please insert coins')
    quarters = int(input('How many quarters?: ')) * 0.25
    dimes = int(input('How many dimes?: ')) * 0.1
    nickles = int(input('How many nickles?: ')) * 0.05
    pennies = int(input('How many pennies?: ')) * 0.01
    total = quarters + dimes + nickles + pennies

    return total


gain = 0

the_end = False

while not the_end:

    # TODO: 1. Ask the user what kind of coffee would like
    command = input("What would you like? (espresso $1.5 /latte $2.5 /cappuccino $3.0): ").lower()

    if command == 'report':
        print(f"Water: {resources['water']} \nmilk: {resources['milk']} \nCoffee: {resources['coffee']}"
              f"\nMoney: {gain} \nCost of espresso: ${MENU['espresso']['cost']}"
              f"\nCost of latte: ${MENU['latte']['cost']} \nCost of cappuccino: ${MENU['cappuccino']['cost']}")
    elif command == 'espresso' or command == 'latte' or command == 'cappuccino':
        # Verify if all resources are enough
        enough_all = enough(resources['water'], MENU[command]['ingredients']['water'],
                            resources['milk'], MENU[command]['ingredients']['milk'],
                            resources['coffee'], MENU[command]['ingredients']['coffee'])
        if enough_all:
            pay = payment()

            if pay >= MENU[command]['cost']:
                balance = pay - MENU[command]['cost']
                print(f"Here is ${balance} in change.\nHere is your espresso ☕️. Enjoy!")
                resources["water"] -= MENU[command]["ingredients"]["water"]
                resources["milk"] -= MENU[command]["ingredients"]["milk"]
                resources["coffee"] -= MENU[command]["ingredients"]["coffee"]
                gain += MENU[command]['cost']
            else:
                print("Sorry that's not enough money. Money refunded.")
                the_end = True

        else:
            if MENU[command]['ingredients']['water'] < resources['water']:
                print("Sorry there is not enough water.")
            if MENU[command]['ingredients']['milk'] < resources['milk']:
                print("Sorry there is not enough milk.")
            if MENU[command]['ingredients']['coffee'] < resources['coffee']:
                print("Sorry there is not enough coffee.")
            the_end = True

    elif command == "off":
        the_end = True
