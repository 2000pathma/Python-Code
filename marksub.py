no_of_subjects=int(input("enter no.of subjects"))
total=0
mark_got=0
while mark_got<no_of_subjects:
    mark=int(input("tell your mark"))
    total=total+mark
    mark_got=mark_got+1
print("your total is",total)
print("your percentage is",round((total/no_of_subjects),2))#round the value use round()&use this 2 to print after point 2 values
