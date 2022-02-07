fruits_dict = {'apple': 100, 'banana': 40,'orange': 60,  'papaya': 30}
for nameKey, priceValue in fruits_dict.items():#key-namekey,price-pricevalue
    fruits_dict[nameKey] = round(priceValue * 1.1, 2)
    print(fruits_dict)
#print(fruits_dict)---->last value only print
#fruitsNamesList = list(fruits_dict.keys())
#for name in fruitsNamesList:
#	print(name)
#print keys in list
fruitsNamesList = list(fruits_dict.keys())
for key in fruitsNamesList:
    if key=='apple':
        del fruits_dict[key]#delete key,value
print(fruits_dict)
	

