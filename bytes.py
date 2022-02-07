values = [10,20,30,40]
b = bytes(values)
print(type(b))
for i in b:
    print(i, end=' ')
    #values = [10,20,30,400]-->error byte upto 0 to 256
