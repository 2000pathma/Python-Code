row=1
value=65
while row<=5:
    column=1
    while column<=row:
        print(chr(value),end='')#chr stand for character based on ASCII value
        column=column+1
    print()
    value=value+1
    row=row+1
