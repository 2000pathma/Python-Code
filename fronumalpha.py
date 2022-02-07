word=input("enter your word")
length=len(word)
countofalphabets=0
countofnumbers=0
countofspecialcharacters=0
for no in range(length):
    if((word[no]>='A' and word[no]<='Z') or (word[no]>='a' and word[no]<='z')):
        countofalphabets=countofalphabets+1
    elif(word[no]>='0' and word[no]<='9'):
        countofnumbers=countofnumbers+1
    else:
        countofspecialcharacters+=1
print(countofalphabets,"alphabets are present")
print(countofnumbers,"numbers are present")
print(countofspecialcharacters,"special char are present")
