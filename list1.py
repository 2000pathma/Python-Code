alpha = ['c','a','b','c']
numeric = [4,1,2,3]
both = [alpha, numeric]
print(both)
li=0
while li<len(both):  
    item = 0
    while item < len(both[li]): 
        print(both[li][item], end=' ')  
        item+=1
    print()
    li+=1
