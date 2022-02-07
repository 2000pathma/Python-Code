#Binary Search: 
# Bi - 2 
# ordered list - ascending, descending 
#input() -> int
# how many numbers 
# append()
#sort
# creating list with user given values

arr = [1,10,20,30,40,50]
#index 0 1  2  3  4  5  length = 6
x = 10
start =0
end = len(arr)-1  #5
while end >= start:  # 0>=1 False    
    mid = start + (end- start)//2   #1 + (0-1)//2
      # If element is present at the middle
    if arr[mid] == x:  #if  1 == 5
        result = mid  #4
        break
      # If element is smaller than mid
    elif arr[mid] > x:  # 1 > 5 True 
        end = mid -1   #end = 0
      # Else the element greator than mid
    else:
        start = mid+1  # 1  start =1 end = 0 
else:
      # Element is not found in the list
    result= -1


if result != -1:  # 4 != -1 
   print ("Element is present at index ", result)
else:
   print ("Element is not present in array")
