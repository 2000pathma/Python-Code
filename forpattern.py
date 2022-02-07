word='payilagam'
count=len(word)
for terms in range(len(word)):#terms---->row
    for letter in range(count):#letter--->column
       print(chr(letter+65),end='')#instead use terms
    print()
    count=count-1
