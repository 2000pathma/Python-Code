# how many students 
studentCount = int(input("Enter the number of students":)
report = {} #dictionary
subjects = ('Tamil', 'English', 'Maths', 'Science', 'Social') 
for student in range(studentCount): 
	#student = 1 
    name = input('Enter the name of the student %d: ' % (student + 1))
	#name = input('Enter the name of the student ')
	#print(student +1) 
    marks = []  #empty list 
    for subject in subjects:
		mark = int(input('Enter your mark for %s'  %subject)
		marks.append(mark) 
        #marks.append(int(input('Enter marks of %s: ' % #subject)))
    report[name] = marks


for name, marks in report.items():
    total =  sum(marks)
	print('Student Name ', name)
	print('Total is ', total) 
   # print("%s 's  total marks %d" % (name, total))
    if total < 120:
        print("%s failed :",% name)
    else:
        print("%s passed :",% name)
