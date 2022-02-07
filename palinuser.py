#palindrome user input
word1=input("enter any word")
word2=word1[::-1]
if word1==word2:
    print("palindrome")
else:
    print("not palindrome")
