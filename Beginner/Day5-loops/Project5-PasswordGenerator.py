"""Password Generator Project."""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

let = []
sym = []
num = []

for n in range(nr_letters):
    let.append(random.choice(letters))

for p in range(nr_symbols):
    sym.append(random.choice(symbols))

for k in range(nr_numbers):
    num.append(random.choice(numbers))

# Basic Level
# print("".join(let + sym + num))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

basic_pasword = let + sym + num

password = "".join(random.sample(basic_pasword, k=len(basic_pasword)))

print(password)


# Metodo básico alternativo:
"""
basic_password = ""

for n in range(nr_letters):
  basic_password += random.choice(letters)

for l in range(nr_symbols):
  basic_password += random.choice(symbols)

for k in range(nr_numbers):
  basic_password += random.choice(numbers)

# Basic Level
# print("".join(let + sym + num))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = "".join(random.sample(basic_password, k=len(basic_password)))

print(password)
"""


def lole():
    """fghjkl."""
    print("lole")
