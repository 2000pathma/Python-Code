#random dice roller
from random import randint
min=1
max=6
#random integer-randint(min,max)---two arguements--int
again = True
while again:
    print("Dice value now: ", randint(min, max))
    another_roll = input("Press 'y' if you want to roll the dice again ")
    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':
        again = True
    else:
        again = False
        print("Thank you")
