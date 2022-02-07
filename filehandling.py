Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f= open("C:\\Users\\2000p\\Documents\\Java\\test.txt","w+")
>>> f.write('Miranda@gmail.com')
17
>>> print(f.readable())
True
>>> print(f.writeable())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(f.writeable())
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeable'
>>> print(f.name)
C:\Users\2000p\Documents\Java\test.txt
>>> f.close()
>>> f.write('abcd')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f.write('abcd')
ValueError: I/O operation on closed file.
>>> f= open("C:\\Users\\2000p\\Documents\\Java\\test2.txt","w+")
>>> f.write('abcd')
4
>>> print ('file closed ',f.closed)
file closed  False
>>> print(f.closed)
False
>>> with open("d:\\temp\\test2.txt","a")   as f:
    f.write('abcd')
    print ('file closed ',f.closed)
print (f.closed)
SyntaxError: invalid syntax
>>>  with open("d:\\temp\\test2.txt","a")   as f:
	 
SyntaxError: unexpected indent
>>> with open("d:\\temp\\test2.txt","a")   as f:
	f.write('abcd')
	print ('file closed ',f.closed)
	print (f.closed)

	
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    with open("d:\\temp\\test2.txt","a")   as f:
FileNotFoundError: [Errno 2] No such file or directory: 'd:\\temp\\test2.txt'
>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/file4.py ================
Enter file name with location\\Users\\2000p\\Documents\\Java\\test2.txt
file not present

\
>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/file4.py ================
Enter file name with location\Users\\2000p\\Documents\\Java\\test2.txt
File is Present

>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/file5.py ================
Enter file name with location\\Users\\2000p\\Documents\\Java\\test2.txt
file not present



>>> 
================ RESTART: C:/Users/2000p/Desktop/PRIYA/file5.py ================
Enter file name with location\Users\\2000p\\Documents\\Java\\test2.txt
File is Present
r

>>> 