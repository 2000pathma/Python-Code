alpha = ['a','b','c','c']
numeric = [1,2,3,4]
both = [alpha, numeric]
li=0
while li<len(both):
    item = 0
    while item < len(both[li]):
        if li==1 and item==1:
             both[li][item]='check'
        item+=1
    print()
    li+=1
print(both)
