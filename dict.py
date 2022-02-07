Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={10,20,30,40}
>>> f=frozenset()
>>> type(f)
<class 'frozenset'>
>>> results={'muthu':67,'kathir':90}
>>> results
{'muthu': 67, 'kathir': 90}
>>> results['muthu']=90
>>> results
{'muthu': 90, 'kathir': 90}
>>> results['kavin'=98
	
SyntaxError: invalid syntax
>>> results['kain']=98
>>> results
{'muthu': 90, 'kathir': 90, 'kain': 98}
>>> del results['arjun']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    del results['arjun']
KeyError: 'arjun'
>>> del results['kathir']
>>> results
{'muthu': 90, 'kain': 98}
>>> list(results)#convert dict to list
['muthu', 'kain']
>>> results
{'muthu': 90, 'kain': 98}
>>> set(results)
{'muthu', 'kain'}
>>> tuple(results)
('muthu', 'kain')
>>> results.keys()_
SyntaxError: invalid syntax
>>> results.keys()
dict_keys(['muthu', 'kain'])
>>> results.values()
dict_values([90, 98])
>>> [*results.values()]
[90, 98]
>>> [*results.keys()]
['muthu', 'kain']
>>> details={'name':'mukil','age':22}
>>> details.get('age')
22
>>> print(details.popitem())
('age', 22)
>>> print(details)
{'name': 'mukil'}
>>> print(details.get('city'))
None
>>> https://docs.python.org/3/library/functions.html#id

https://docs.python.org/3/glossary.html#term-immutable
SyntaxError: invalid syntax
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
>>> print(details.pop('city'))
tirunelveli
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
print(details)
for key in details:
    print(key)
    
SyntaxError: multiple statements found while compiling a single statement
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
    print(details)
    for key in details:print(key)
    
SyntaxError: multiple statements found while compiling a single statement
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
    print(details)
    for key in details:print(key)
    
SyntaxError: multiple statements found while compiling a single statement
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
    print(details)
    for key in details:
         print(key)details
         
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/2000p/Desktop/PRIYA/dict1.py
{'name': 'Mukil', 'age': 22, 'city': 'tirunelveli', 'state': 'tamil nadu'}
name
age
city
state
>>> 
= RESTART: C:/Users/2000p/Desktop/PRIYA/dict1.py
{'name': 'Mukil', 'age': 22, 'city': 'tirunelveli', 'state': 'tamil nadu'}
name
age
city
state
>>> type(key)
<class 'str'>
>>> print(key, '-->',details[key] )
state --> tamil nadu
>>> details = {'name': 'Mukil', 'age': 22, 'city':'tirunelveli','state':'tamil nadu'}
print(details)
for item in details.items():
    print(item)
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
= RESTART: C:/Users/2000p/Desktop/PRIYA/dict2.py
{'name': 'Mukil', 'age': 22, 'city': 'tirunelveli', 'state': 'tamil nadu'}
('name', 'Mukil')
('age', 22)
('city', 'tirunelveli')
('state', 'tamil nadu')
>>> type(item)
<class 'tuple'>
>>> 