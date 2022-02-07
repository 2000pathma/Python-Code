Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name='priya'
>>> name.capitalize()
'Priya'
>>> name='priya'
>>> name.casefold()
'priya'
>>> name='PRIYA'
>>> name.casefold()
'priya'
>>> name='Basic Calculator'
>>> name.center(30,'*')
'*******Basic Calculator*******'
>>> sentence="Hi Everyone"
>>> word='is'
>>> sentece.count(word)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sentece.count(word)
NameError: name 'sentece' is not defined
>>> sentence.count(word)
0
>>> sentence="Hi Everyone"
>>> word="is"
>>> sentence.count(word)
0
>>> word="Hi"
>>> sentence.count(word)
1
>>> sentence="Hi Everyone"
>>> sentence.endsWith("correct")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sentence.endsWith("correct")
AttributeError: 'str' object has no attribute 'endsWith'
>>> sentence.endswith("correct")
False
>>> 