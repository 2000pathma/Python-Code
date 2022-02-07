studentDetails = []
studentCount = int(input("Good Morning sir," 
                         "Please tell me student count in your class"))
for student in range(studentCount):
    name, age, percentage = input("Enter your name, Age, Percentage separated by space: ").split()
    #print("User Details: ", name, age, percentage)
    studentDetails.append(name)
    studentDetails.append(age)
    studentDetails.append(percentage)
print(studentDetails)
count = 1
print("Student Name ", "Student Age ", "Student Mark ", end=' ')
print()
print("---------------------------------------",end = ' ')
print()
for percentage in studentDetails:
    if count%3 == 0:
        if int(percentage)>75:
            print(studentDetails[count-3], ":", studentDetails[count-2])
count+=1
