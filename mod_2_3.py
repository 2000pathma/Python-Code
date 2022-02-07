no=1
last_no=int(input("enter range"))
while no<=last_no:
    if(no%2==0 and no%3==0):
        print(no)
    no=no+1
