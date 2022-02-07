mind=5
guess=int(input("enter your guess"))
if guess==mind:
    print("guess is correct")
elif guess>mind:
    print("guess is higher")
elif guess<mind:
    print("guess is less")
