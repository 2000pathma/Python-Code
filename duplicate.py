fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
#count function is used for determine the duplicate item in list
if fruits.count('apple') > 1:
    fruits.remove('apple')
print(fruits)
