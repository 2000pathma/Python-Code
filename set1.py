Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> values = {True, 'arul', 50, 'mukil', 123}
>>> del values[50]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    del values[50]
TypeError: 'set' object doesn't support item deletion
>>> name1={'muthu','rama','priya'}
>>> name2={'lingam','arjun','ramesh'}
>>> print(name1-name2)
{'muthu', 'priya', 'rama'}
>>> print(name1|name2)
{'lingam', 'ramesh', 'rama', 'muthu', 'priya', 'arjun'}
>>> print(name1&name2)
set()
>>> print(name1^name2)
{'lingam', 'arjun', 'ramesh', 'rama', 'muthu', 'priya'}
>>> values={'lingam','arjun','ramesh'}
>>> for i in values:
	if isinstance(i,int):
		if type(i) is int:
			print(i)

			
>>> 


>>> 

>>> 


>>> 


>>> 


>>> 


>>> 

>>> 

>>> for i in values:
	#if isinstance(i,int):
	if type(i) is int:
		print(i)

		
>>> 