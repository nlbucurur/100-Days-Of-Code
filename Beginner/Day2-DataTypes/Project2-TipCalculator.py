"""This program calculates the total amount of a bill."""
print("Welcome to the Tip Calculator")

Bill = float(input("What was the total bill? $"))

Tip = int(input("What percentage tip wpuld you like to tip? 10, 12 or 15? "))

People = int(input("How many people to split the bill? "))

Tip1 = Bill * float(Tip) / 100

Bill += Tip1
Bill /= int(People)

# Bill1 = round(Bill, 2)
Bill1 = "{:.2f}".format(Bill)

print(f"Each person should pay: ${Bill1}")
