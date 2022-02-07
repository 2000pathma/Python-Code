##def மொத்தவிலை(விற்கும்விலை, வாங்கும்விலை,**வரி): 
##    print(விற்கும்விலை)
##    print(வாங்கும்விலை)
##    for key, value in வரி.items(): 
##        print (key, type(key))
##        print (value, type(value))
##
##	
##மொத்தவிலை(100,90,sgst=5,cgst=5)
def mrp(sellingprice,buyingprice, **tax):
	print(sellingprice)
	print(buyingprice)
	for key, value in tax.items():
		print(key, type(key))
		print(value, type(value))
	
		
mrp(100,90,sgst=5,cgst=6)
