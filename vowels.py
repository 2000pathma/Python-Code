#determine and count vowels(aeiou) from the given name
word=input("enter your name")
no=0
count=0
while no<len(word):
#if word[no] is equal to 'a' or 'e'or'i' or 'o' or 'u' then print(word[no])
#instead of using word[no]=='a' or word[no]=='e' or word[no]=='i' or word[no]=='o' or word[no]=='u' by
    if word[no] in ['a','e','i','o','u'] or word[no] in ['A','E','I','O','U']:  #or ['A','E','I','O','U']:
        print(word[no])
        count=count+1
    no=no+1
print("no.of vowels",count)
