#variable argument
def mrp(*amount):
	for price in amount:
		print(price)
	
mrp(100,90)
mrp(100,90,5)
