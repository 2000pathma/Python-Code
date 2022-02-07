Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> no=123
>>> no
123
>>> type(no)
<class 'int'>
>>> id(no)
1452343120
>>> value=0b1111
>>> print(value)
15
>>> value=0B1010
>>> print(value)
10
>>> value2=0o12345
>>> print(value2)
5349

>>> value=0X123
>>> value
291
>>> value=0Xabc
>>> value
2748
>>> value=0XABC
>>> value
2748
>>> value=0xface
>>> value
64206
>>> value=0xace
>>> value
2766
>>> value=oxbad
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    value=oxbad
NameError: name 'oxbad' is not defined
>>> value=0xbad
>>> value
2989
>>> value=0xbeef
>>> value
48879
>>> print(bin(10))
0b1010
>>> print(oct(10))
0o12
>>> print(hex(100))
0x64
>>> print(bin(0xbeef))
0b1011111011101111
>>> no=1.123
>>> no=0x123.11
SyntaxError: invalid syntax
>>> no=5.6e3
>>> no
5600.0
>>> type(no)
<class 'float'>
>>> id(no)
47103888
>>> 5+6j
(5+6j)
>>> value=5+6j
>>> print(value.real)
5.0
>>> print(value.imag)
6.0
>>> bool->True False
SyntaxError: invalid syntax
>>> mark=98
>>> mark1=65
>>> print(mark>mark1)
True
>>> print(mark<mark1)
False
>>> print(mark==mark1)
False
>>> print(True+False)
1
>>> print(True+True)
2
>>> print(False+False)
0
>>> name='priya'
>>> name
'priya'
>>> name="priya"
>>> name
'priya'
>>> name='"priya"'
>>> name
'"priya"'
>>> name='''priya
m'''
>>> name
'priya\nm'
>>> print(name)
priya
m
>>> name="""priya
m
pathma priya"""
>>> name
'priya\nm\npathma priya'
>>> print(name)
priya
m
pathma priya
>>> no=5
>>> no2='5'
>>> type(no)
<class 'int'>
>>> type(no2)
<class 'str'>
>>> doorno=120/2B
SyntaxError: invalid syntax
>>> doorno=120/2
>>> doorno
60.0
>>> doorno='120/2'
>>> doorno
'120/2'
>>> sentence="'thiruvalluvar' wrote 'tirukural'"
>>> print(sentence)
'thiruvalluvar' wrote 'tirukural'
>>> sent="'thiruvalluvar' wrote"thirukural""
SyntaxError: invalid syntax
>>> sent=''''tiruvalluvar' wrote "thirukural"'''
>>> sent
'\'tiruvalluvar\' wrote "thirukural"'
>>> print(sent)
'tiruvalluvar' wrote "thirukural"
>>> 