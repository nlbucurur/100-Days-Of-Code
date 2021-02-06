"""Practice your Rock, paper, scissors skills."""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# options
ops = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

pc = random.randint(0, 2)

if choice == 0:
    print("Your choose:\n" + ops[0])
    if pc == 1:
        print("Computer choice:\n" + ops[1] + "\nYou lose!")
    elif pc == 2:
        print("Computer choice:\n" + ops[2] + "\nYou win!")
    else:
        print("Computer choice:\n" + ops[0] + "\n" + "Draw!")

elif choice == 1:
    print("Your choose:\n" + ops[1])
    if pc == 2:
        print("Computer choice:\n" + ops[2] + "\nYou  lose!")
    elif pc == 0:
        print("Computer choice:\n" + ops[0] + "\nYou win!")
    else:
        print("Computer choice:\n" + ops[1] + "\n" + "draw")

elif choice == 2:
    print("Your choice:\n" + ops[2])
    if pc == 0:
        print("Computer choice:\n" + ops[0] + "\nYou lose!")
    elif pc == 1:
        print("Computer choice:\n" + ops[1] + "\nYou win!")
    else:
        print("Computer choice:\n" + ops[2] + "\n" + "draw")

else:
    print("Try again! There is an error in your choice")
