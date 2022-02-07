#Saa Boo Three Game: 

from random import randint

#create a list of play options
choices = ["Saa", "Boo", "Three"]

#assign a random play to the computer
value = randint(0,2)
computer = choices[value]  # Saa, Boo, Three 

#set player to False
repeat = True

while repeat == True:
#set player to True
    player = input(" Saa, Boo, Three? ")
    if player == computer:
        print("Tie!")
    elif player == "Saa":
        if computer == "Boo":
            print("You lose!", computer, "won", player)
        else:
            print("You win!", player, "won ", computer)
    elif player == "Boo":
        if computer == "Three":
            print("You lose!", computer, "won ", player)
        else:
            print("Great!  You win", player, "won ", computer)
    elif player == "Three":
        if computer == "Saa":
            print("You lose...", computer, "won ", player)
        else:
            print("You win!", player, "won ", computer)
    else:
        print("Please check your spelling!")
    y_or_n = input("Press 'Y' for continuing")
    repeat = y_or_n.upper()  #No -> repeat = No
    computer = choices[value]
