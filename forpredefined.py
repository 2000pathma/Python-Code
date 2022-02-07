word=input("enter your word")
length=len(word)
countofalphabets=0
countofnumbers=0
countofspecialcharacters=0
if length<8:
    print("no,please enter more characters")
else:
    for no in range(length):
         if(word[no].isalpha()):
            countofalphabets=countofalphabets+1
         elif(word[no].isdigit()):
            countofnumbers=countofnumbers+1
         else:
            countofspecialcharacters+=1
    print(countofalphabets,"alphabets are present")
    print(countofnumbers,"numbers are present")
    print(countofspecialcharacters,"special char are present")

