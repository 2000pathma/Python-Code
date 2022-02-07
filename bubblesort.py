#Bubble sorting
#finding biggest number first
arr = [2,18,16,11,7,4,6]  
n = len(arr)-1 #6
print("Before for loop ", arr)
for i in range(n):
    print("Inside for loop ", arr)
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
print("After for loop ", arr)
print(arr[6])#print(arr[-1])
#Skip the biggest number balance numbers are short
#print second biggest print(arr[-1]) or print(arr[6])
n = n-1 #5
print('*******')
print("Before for loop ", arr)
for i in range(n):
    print("Inside for loop ", arr)
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
print("After for loop ", arr)
print(arr[5])#print(arr[-2])
#After finding second biggest balance numbers are shorted
#print second biggest print(arr[-2]) or print(arr[5])
n = n-1 #4
print('*******')
print("Before for loop ", arr)
for i in range(n):
    print("Inside for loop ", arr)
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
print("After for loop ", arr)
print(arr[4])#print(arr[-3])
n = n-1 #3
print('*******')
print("Before for loop ", arr)
for i in range(n):
    print("Inside for loop ", arr)
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
print("After for loop ", arr)
print(arr[5])#print(arr[-4])


