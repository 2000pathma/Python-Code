Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import csv
>>> with open('students.csv','w') as f:
	w = csv.writer(f)
	w.writerow(['Name','No','Percentage','Address'])
	while True:
		name = input("Enter name ")
		no = int(input("Enter no "))
		percentage = int(input("Enter percentage "))
		address = input("Enter address ")
		w.writerow([name,no,percentage, address])
		option = input('Continue? Yes | No ')
		if option.lower() == 'no':
			break

		
28
Enter name priya
Enter no 65
Enter percentage 90
Enter address gdhjdfhud
23
Continue? Yes | No yes
Enter name oriy
Enter no 9
Enter percentage 098
Enter address jl,hfd
20
Continue? Yes | No no
>>> import csv
>>> f = open('students.csv','r')
>>> w = csv.writer(f)
>>> r = csv.reader(f)
>>> data = list(r)
>>> print(data)
[['Name', 'No', 'Percentage', 'Address'], [], ['priya', '65', '90', 'gdhjdfhud'], [], ['oriy', '9', '98', 'jl,hfd'], []]
>>> for row in data:
	print (row)

	
['Name', 'No', 'Percentage', 'Address']
[]
['priya', '65', '90', 'gdhjdfhud']
[]
['oriy', '9', '98', 'jl,hfd']
[]
>>> for column in data:
	print (column)

	
['Name', 'No', 'Percentage', 'Address']
[]
['priya', '65', '90', 'gdhjdfhud']
[]
['oriy', '9', '98', 'jl,hfd']
[]
>>> #recursive function
>>> def fact(number):
	if n ==0:
		return 1
	else:
		return n * fact(n-1)
	print(fact(0))
	print(fact(5))

	
>>> 
>>> 
KeyboardInterrupt
>>> def fact(n):
	if n ==0:
		return 1
	else:
		return n * fact(n-1)
    print(fact(0))
    print(fact(5))
    
SyntaxError: unindent does not match any outer indentation level
>>> def fact(n):
	if n ==0:
		return 1
	else:
		return n * fact(n-1)
        print(fact(0))
        print(fact(5))
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
============== RESTART: C:/Users/2000p/Desktop/PRIYA/recursion.py ==============
1
120
>>> def fact(n):
	if n ==0:
		return 1
	else:
		return n * fact(n-1)
     print(fact(0))
     print(fact(5))
     
SyntaxError: unindent does not match any outer indentation level
>>> def fact(n):
	if n ==0:
		return 1
	else:
		return n * fact(n-1)
     print(fact(0))
     print(fact(5))
     
SyntaxError: unindent does not match any outer indentation level
>>> for no in range(5):
	print(no+1)

	
1
2
3
4
5
>>> 