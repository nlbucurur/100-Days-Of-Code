# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_a = name1.lower()
name_b = name2.lower()

T = name_a.count("t") + name_b.count("t")
R = name_a.count("r") + name_b.count("r")
U = name_a.count("u") + name_b.count("u")
E = name_a.count("e") + name_b.count("e")

L = name_a.count("l") + name_b.count("l")
O = name_a.count("o") + name_b.count("o")
V = name_a.count("v") + name_b.count("v")
E = name_a.count("e") + name_b.count("e")

TRUE_LOVE = int(str(T + R + U + E) + str(L + O + V + E))

if TRUE_LOVE <= 10 or TRUE_LOVE >= 90:
  print(f"Your score is {TRUE_LOVE}, you go together like coke and mentos.")
elif TRUE_LOVE >= 40 and TRUE_LOVE <= 50:
  print(f"Your score is {TRUE_LOVE}, you are alright together.")
else:
  print(f"Your score is {TRUE_LOVE}.")
