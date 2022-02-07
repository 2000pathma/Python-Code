row=1
#value=65
while row<=5:
    column=1
    value=65
    while column<=row:
        print(chr(value),end='')#chr stand for character based on ASCII value
        value=value+1
        column=column+1
    print()
    row=row+1
