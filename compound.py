Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> squares=[1,4,9,16,25]
>>> marks=[94,98,97,90,95]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3]
9
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares+[36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares.append(120)
>>> squares()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    squares()
TypeError: 'list' object is not callable
>>> print(squares)
[1, 4, 9, 16, 25, 120]
>>> squares.append(12*2*)
SyntaxError: invalid syntax
>>> squares.append(12**2)
>>> print(squares)
[1, 4, 9, 16, 25, 120, 144]
>>> squares.append([8])
>>> print(squares)
[1, 4, 9, 16, 25, 120, 144, [8]]
>>> leters=['a','b','c','d','e','f','g']
>>> letters
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    letters
NameError: name 'letters' is not defined
>>> letters=['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]
['c', 'd', 'e']
>>> letters[2:5]=[]
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:]=[]
>>> letters
[]
>>> len(letters)
0
>>>  letters=['a','b','c','d','e','f','g']
 
SyntaxError: unexpected indent
>>> letters=['a','b','c','d','e','f','g']
>>> len(letters)
7
>>> alpha=['a','b','c']
>>> numbers=[1,2,3]alpha[0]
SyntaxError: invalid syntax
>>> numbers=[1,2,3]
>>> alpha[0]
'a'
>>> numbers[0]
1
>>> both=[alpha,numbers]
>>> print(both)
[['a', 'b', 'c'], [1, 2, 3]]
>>> type(numbers[0])
<class 'int'>
>>> type(alpha[0])
<class 'str'>
>>> type(numbers)
<class 'list'>
>>> type(alpha)
<class 'list'>
>>> len(both)
2
>>> len(numbers)
3
>>> len(alpha)
3
>>> type('a')
<class 'str'>
>>> type(0)
<class 'int'>
>>> both[0]
['a', 'b', 'c']
>>> both[1]
[1, 2, 3]
>>> both[2]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    both[2]
IndexError: list index out of range
>>> both[0][0]
'a'
>>> both[0][1]
'b'
>>> both[1][0]
1
>>> both[2][2]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    both[2][2]
IndexError: list index out of range
>>> both[1][3]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    both[1][3]
IndexError: list index out of range
>>> both[1][2]
3
>>> list=['a','b','c','d']
>>> for item in list:
	print(item,end=' ')

	
a b c d 
>>> list=['a','e','i','o','b']
>>> for item in list=="a" or "e" or "i" or "o" or "u":
	print(item,end=' ')

	
e 
>>> list=['a','e','i','o','b']
>>> if item in list['a','e','i','o','u']:
	print(item,end=' ')
	
SyntaxError: multiple statements found while compiling a single statement
>>> list=['a','e','i','o','b']
>>> for item in list:
       if item in list['a','e','i','o','u']:
	print(item,end=' ')
	
SyntaxError: multiple statements found while compiling a single statement
>>> for inner_list in both:
	for list_item in inner_list:
		print(list_item,end='')

		
abc123
>>> for inner_list in both:
	for list_item in inner_list:
		if list_item,isalpha():
		print(list_item,end='')
		
SyntaxError: invalid syntax
>>> 
>>> for inner_list in both:
	for list_item in inner_list:
		if list_item.isalpha():
		print(list_item,end='')
		
SyntaxError: expected an indented block
>>> 
>>> for inner_list in both:
	for list_item in inner_list:
		if list_item.isalpha()
		    print(list_item,end='')
		    
SyntaxError: invalid syntax
>>> 
>>> for inner_list in both:
	for list_item in inner_list:
		if list_item.isalpha():
		    print(list_item,end='')

		    
abcTraceback (most recent call last):
  File "<pyshell#74>", line 3, in <module>
    if list_item.isalpha():
AttributeError: 'int' object has no attribute 'isalpha'
>>> for inner_list in both:
	for list_item in inner_list:
		if type(list_item)==str and items.isalpha():
		print(list_item,end='')
		
SyntaxError: expected an indented block
>>>  for inner_list in both:
	for list_item in inner_list:
		if type(list_item)==str and items.isalpha():
		     print(list_item,end='')
		     
SyntaxError: unexpected indent
>>> 
>>> for inner_list in both:
	for list_item in inner_list:
		if type(list_item)==str and items.isalpha():
		    print(list_item,end='')

		    
Traceback (most recent call last):
  File "<pyshell#79>", line 3, in <module>
    if type(list_item)==str and items.isalpha():
NameError: name 'items' is not defined
>>> for inner_list in both:
	for list_item in inner_list:
		if type(list_item)==str and list_item.isalpha():
		     print(list_item,end='')

		     
abc
>>> for inner_list in both:  
		for list_item in inner_list:
			print(list_item," belongs to ", type(list_item), end =' ')

			
a  belongs to  <class 'str'> b  belongs to  <class 'str'> c  belongs to  <class 'str'> 1  belongs to  <class 'int'> 2  belongs to  <class 'int'> 3  belongs to  <class 'int'> 
>>> 