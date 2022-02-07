பெயர் = input("உங்கள் பெயர் ")
print( பெயர் + " அவர்களே வருக! வருக! ")
வார்த்தை = "laptop"
கணிப்புகள் = ''

முயற்சிகள் = 10
while முயற்சிகள் > 0:         
    தோல்வி = 0                
    for எழுத்து in வார்த்தை:      
        if எழுத்து in கணிப்புகள்:    
            print(எழுத்து, end=' ')  
        else:
            print("_ ",end=' ')
            
            தோல்வி += 1    

    if தோல்வி == 0:        
        print("\nவெற்றி வெற்றி!")
        break              

    print()
    கணிப்பு = input("ஏதாவது ஓர் எழுத்து சொல்லுங்கள்!  ")    
    கணிப்புகள் += கணிப்பு                    

    if கணிப்பு not in வார்த்தை:  
        முயற்சிகள் -= 1         
        print("தப்பு, ")  
        print("நீங்கள் இன்னும் ", + முயற்சிகள், ' தடவை தொடரலாம்') 
        if  முயற்சிகள் == 0:           
            print("அடடா!  கொஞ்சம் முயன்றிருக்கலாமே")
##from random import randint
##
##list_keywords=['false', 'none', 'true', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
## 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
## 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
##
##r=randint(0, len(list_keywords) - 1)
##
##turns=len(list_keywords[r]) # no of chances for user is based on size of a key word
##
##if len(list_keywords[r])>2: # this if and else part is to define how many missing letters in b/w keywords
##    space=list_keywords[r]
##    print('Find a keyword in python with',len(list_keywords[r]),'characters..','Keyword starts with :',list_keywords[r][0],' _ '*(len(list_keywords[r])-2),list_keywords[r][-1])
##else:
##    print('Find a keyword in python with', len(list_keywords[r]), 'characters..', 'Keyword starts with :',list_keywords[r][0], '_ ' * (len(list_keywords[r]) - 1))
##
##print('You only have',turns ,'chances..')
##
##while True:
##
##    USER = input('Now enter your guess to find the right keyword : ')
##
##    if USER.lower() == list_keywords[r]:
##        print('Congratulations..!\nYou remember most keywords list in python..')
##        print('THANKS FOR USING MY APPLICATION')
##        break
##    elif turns == 1:
##        print('The correct keyword is :',list_keywords[r])
##        print('you have used all chances..\nKeep trying..')
##        break
##    else:
##        print('Please try again')
##    turns -=1
