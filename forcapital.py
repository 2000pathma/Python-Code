#print capital numbers
word=input("enter your word")
length=len(word)
for no in range(length):
    if(word[no]>='A' and word[no]<='Z'):
      print(word[no])
