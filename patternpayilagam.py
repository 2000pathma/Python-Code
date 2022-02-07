word='payilagam'
count=len(word)
for terms in range(len(word)):#terms---->row
    for letter in range(count):#letter--->column
       print(word[letter],end='')
    print()
    count=count-1
