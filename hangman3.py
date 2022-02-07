name = input("What is your name? ")
print("Welcome, " + name)
word = "laptop"
guesses = ''

turns = 10
while turns > 0:         
    failed = 0                
    for char in word:      
        if char in guesses:    
            print(char, end=' ')  
        else:
            print("_ ",end=' ')    
            failed += 1    

    if failed == 0:        
        print("\nYou won")
        break              

    print()
    guess = input("guess a character:")
    guesses += guess   
	# guesses = 'za'                 

    if guess not in word:  #if 'a' not in 'laptop'
        turns -= 1        #9  
        print("Wrong")  
        print("You have", + turns, 'more guesses') 
        if turns == 0:           
            print("You Lose")
