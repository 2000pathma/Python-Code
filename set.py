Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/tuple3.py ===============
>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/tuple3.py ===============

>>> tuple=1,2,3
>>> n1,n2,n3=tuple
>>> print(n1,"and",n2,"and",n3)
SyntaxError: multiple statements found while compiling a single statement
>>> tuple=(1,2,3)
>>> n1,n2,n3=tuple
>>> rint(n1,"and",n2,"and",n3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    rint(n1,"and",n2,"and",n3)
NameError: name 'rint' is not defined
>>> print(n1,"and",n2,"and",n3)
1 and 2 and 3
>>> set
<class 'set'>
>>> set={1,2,3,1}
>>> set
{1, 2, 3}
>>> #it have no duplicate values
>>> set.remove('2')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set.remove('2')
KeyError: '2'
>>> set.add(6)
>>> set
{1, 2, 3, 6}
>>> set.remove(2)
>>> set
{1, 3, 6}
>>> set.pop()
1
>>> alphaDuplicate=('a','b','c')
>>> alpha=('a','b','c')
>>> id(alpha)
53801512
>>> id(alphaDuplicate)
62695688
>>> #pop()---->first value displayed
>>> for i in values:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    for i in values:
NameError: name 'values' is not defined
>>> for i in setprint(i)
SyntaxError: invalid syntax
>>> for i in set:
	print(i)

	
3
6
>>> set{}
SyntaxError: invalid syntax
>>> set={}
>>> print(type(set))
<class 'dict'>
>>> values=set{}
SyntaxError: invalid syntax
>>> values={}
>>> type(values)
<class 'dict'>
>>> values=set{}
SyntaxError: invalid syntax
>>> values=set()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    values=set()
TypeError: 'dict' object is not callable
>>> values=set()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    values=set()
TypeError: 'dict' object is not callable
>>> 