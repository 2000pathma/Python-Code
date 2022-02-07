word='payilagam'
count=len(word)
for terms in range(len(word)):#terms---->row
    for letter in range(count):#letter--->column
       print(' ',end=' ')
    for hashval in range(terms+1):
       print(chr(terms+65),end=' ')
    print()
    count=count-1
    #terms0-1
