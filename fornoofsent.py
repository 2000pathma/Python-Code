# printing no of  sentences
sentence = "Today is Saturday. Today's Date is 16th"
noofsentences = 1
for letter in sentence:
    if letter == '.':
        noofsentences += 1
print ("No of sentences  ",noofsentences)
