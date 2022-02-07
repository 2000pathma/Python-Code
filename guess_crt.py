mind=5
match_not_found=True
while match_not_found==True:
     guess=int(input("enter your guess between 1 and 10"))
     if guess==mind:
         print("guess is correct")
         match_not_found=False
     elif guess>=mind:
         print("guess is higher")
     elif guess<=mind:
         print("guess is less")
        
