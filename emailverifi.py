email=input("enter your email id")
length=len(email)
countofalphabets=0
countofnumbers=0
countofspecialcharacters=0
if length<20:
    print("please enter a valid email id")
else:
    for no in range(length):
        if((email[no]>='A' and email[no]<='Z') or (email[no]>='a' and email[no]<='z')):
             countofalphabets=countofalphabets+1
        elif(email[no]>='0' and email[no]<='9'):
            countofnumbers=countofnumbers+1
        else:
            countofspecialcharacters+=1
    print(countofalphabets,"alphabets are present")
    print(countofnumbers,"numbers are present")
    print(countofspecialcharacters,"special char are present")
    #instead using isdigit() and isalpha()
