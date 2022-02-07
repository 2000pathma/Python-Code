Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try: 
    file = open("C:\\Users\\91759\\Documents\\Python\\pincodes.txt")
    for each_line in file:
        try:
            (city, pincode) = each_line.split("-")
            print('pincode of ', city, end='')
            print('is ', pincode,end='')
        except:
            pass
	
    file.close()
except:
    print('Please check file location')

    
Please check file location
>>> try: 
    file=open("C:\\Users\\2000p\\Documents\\Java\\pincides.txt")
    for each_line in file:
        try:
            (city, pincode) = each_line.split("-")
            print('pincode of ', city, end='')
            print('is ', pincode,end='')
        except:
            pass
	
    file.close()
except:
    print('Please check file location')

    
Please check file location
>>> try: 
    file=open("C:\\Users\\2000p\\Documents\\Java\\pincodes.txt")
    for each_line in file:
        try:
            (city, pincode) = each_line.split("-")
            print('pincode of ', city, end='')
            print('is ', pincode,end='')
        except:
            pass
	
    file.close()
except:
    print('Please check file location')

    
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except ZeroDivisionError:
    print("Please check y value ")
except ValueError:
	print("Please enter valid number")
except:
	print("Something went wrong")

	
Enter no 5
Enter no 0
Please check y value 
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except ZeroDivisionError:
    print("Please check y value ")
except ValueError:
	print("Please enter valid number")
except:
	print("Something went wrong")

	
Enter no 5
Enter no hf
Please enter valid number
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
finally:
	print("Check finally ")

	
Enter no 5
Enter no 4
1.25
Check finally 
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
finally:
	print("Check finally ")

	
Enter no 7
Enter no 0
division by zero
Check finally 
>>> #finally usage--->DB cleanng,connection closing
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
finally:
	pass

Enter no 4
Enter no 0
division by zero
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
finally:
	pass

Enter no gg
invalid literal for int() with base 10: 'gg'
>>> try:
    x = int(input("Enter no "))
    y = int(input("Enter no ")) #0, ten
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)

    
Enter no 7
Enter no 9
0.7777777777777778
>>> import sys

inputList = ['a', 0, 2,8,10,False]

for entry in inputList:
    try:
        print("The entry is ", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[1], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of ", entry, "is", r)
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
inputList = ['a', 0, 2,8,10,False]
for entry in inputList:
    try:
        print("The entry is ", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[1], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of ", entry, "is", r)
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
inputList = ['a', 0, 2,8,10,False]
for entry in inputList:
	try:
		print("The entry is ", entry)
		r = 1/int(entry)
		break
	except:
		print("Oops!", sys.exc_info()[1], "occurred.")
		print("Next entry.")
		print()
print("The reciprocal of ", entry, "is", r)
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
inputList = ['a', 0, 2,8,10,False]
for entry in inputList:
	try:
		print("The entry is ", entry)
		r = 1/int(entry)
		break
	except:
		print("Oops!", sys.exc_info()[1], "occurred.")
		print("Next entry.")
		print()print("The reciprocal of ", entry, "is", r)
		
SyntaxError: multiple statements found while compiling a single statement
>>> import sys
inputList = ['a', 0, 2,8,10,False]
for entry in inputList:
	try:
		print("The entry is ", entry)
		r = 1/int(entry)
		break
	except:
		print("Oops!", sys.exc_info()[1], "occurred.")
		print("Next entry.")
		print()
		
SyntaxError: multiple statements found while compiling a single statement
>>> import system
inputList = ['a', 0, 2,8,10,False]
for entry in inputList:
	try:
		print("The entry is ", entry)
		r = 1/int(entry)
		break
	except:
		print("Oops!", system.exc_info()[1], "occurred.")
		print("Next entry.")
		print()
print("The reciprocal of ", entry, "is", r)
SyntaxError: multiple statements found while compiling a single statement
>>> try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
        except (AttributeError, TypeError) as e:
    #print("Error occurred:", e)
	#print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>
		
SyntaxError: invalid syntax
>>> try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
except (AttributeError, TypeError) as e:
	print("Error occurred:", e)
	print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>

	
Enter no4
Enter no5
Error occurred: can only concatenate str (not "int") to str
Error occurred  <class 'TypeError'>
>>> try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
except (AttributeError, TypeError) as e:
	print("Error occurred:", e)
	print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>

	
Enter no5
Enter noht
Traceback (most recent call last):
  File "<pyshell#46>", line 3, in <module>
    y = int(input("Enter no"))
ValueError: invalid literal for int() with base 10: 'ht'
>>>  try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
except (AttributeError, TypeError) as e:
	print("Error occurred:", e)
	print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>
	
SyntaxError: unexpected indent
>>> 
>>>  try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
except (AttributeError, TypeError) as e:
	print("Error occurred:", e)
	print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>

	
SyntaxError: unexpected indent
>>> try:
    x = int(input("Enter no"))
    y = int(input("Enter no"))
    if x > y:
        result = 5
        result.append("hello")  # throws AttributeError
    else:
        print("Hi " + 5)  # throws TypeError
except (AttributeError, TypeError) as e:
	print("Error occurred:", e)
	print("Error occurred ", type(e)) #Error occurred  <class 'AttributeError'>

	
Enter no5
Enter no4
Error occurred: 'int' object has no attribute 'append'
Error occurred  <class 'AttributeError'>
>>> 