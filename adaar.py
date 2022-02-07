age=int(input("enter your age"))
if age>5:
    nationality=input("enter your nationality")
    if nationality.upper()=='INDIAN':
        print("eligible for adhaar card")
    else:
        print("not for other nationalities")
else:
    print("age criteria not met")
