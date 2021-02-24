"""Silent Auction."""

from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.

print(logo)

should_continue = True

participants = []

max = 0

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    participants.append(
        {
            "name": name,
            "bid": bid
        },
    )

    contin = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if contin == "no":
        should_continue = False
    elif contin == "yes":
        clear()

for key in range(len(participants)):
    if participants[key]["bid"] >= max:
        max = participants[key]["bid"]
        winner = participants[key]["name"]

clear()

print("The winner is " + winner + f" with a bit of {max}")
