#printing no of words 
sentence = "Today is Saturday. Today's Date is 16th"
noofwords = 1
for letter in sentence:
    if letter == ' ':
        noofwords += 1
print ("No of words ",noofwords)
