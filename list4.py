#for loop used for edit the list
alpha = ['a','b','c','c']
numeric = [1,2,3,4]
both = [alpha, numeric]
print(both)
for i in range(len(both)):
    for j in range(len(both[i])):
        if i==1 and j==1:
            both[i][j]='check'
print(both)
