##def தள்ளுபடி_கண்டுபிடி(விலை, சதவீதம்=10):
##	தள்ளுபடி = விலை * (சதவீதம்/100)
##	புதுவிலை = விலை - தள்ளுபடி
##	print(புதுவிலை)
##
##தள்ளுபடி_கண்டுபிடி(100)
##தள்ளுபடி_கண்டுபிடி(100, 25)
##Default arguement
def find_discount(mrp,perc=10):
	discount = mrp ** (perc/100)
	arp = mrp - discount
	print(arp) 

find_discount(mrp=100,perc=25)
find_discount(perc=25,mrp=100)
