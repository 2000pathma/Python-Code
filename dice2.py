from random import randint
min=1
max=6
repeat = 'Y'  #Yes 
while repeat == 'Y':
    print("Dice value now: ", randint(min, max))
    another_roll = input("Press 'y' if you want to roll the dice again ")
    y_or_n = input()
    repeat = y_or_n.upper()  #No -> repeat = No
    if repeat != 'y':
        print('Thank you')
