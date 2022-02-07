#Linear Search: 
items = [15, 8, 1, 10, 13]  #list 
 
print("list of items: ", items)
 
searchingNo = int(input("enter item to search"))

#if items[0] == searchingNo:  #15==13
#	print("Your no. is present")
#elif items[1]== searchingNo:  #8 == 13
#	print("Your no. is present")
#elif items[2]== searchingNo:  #8 == 13
#	print("Your no. is present")
#elif items[3]== searchingNo:  #8 == 13
#	print("Your no. is present")
	
i = 0
numbergot =False
while i < len(items):
        if items[i] == searchingNo:  #15 == 15
                numbergot= True
		break
	i = i + 1
if numbergot== True:
	print("item found at position:", i + 1)
else:
	print("item not found")
