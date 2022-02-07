##def மாற்றவேண்டியது(பணம்):
##	பணம் = 2000  #local variable
##        print("சில்லரை மாற்றவேண்டியது ", பணம்)
##
##
##பணம் = 10000  #global variable 
##print("செலவழிக்க வேண்டிய பணம் ",பணம் )
##மாற்றவேண்டியது(பணம்)
##print("சில்லரை மாற்றிய பிறகு கையில் இருப்பது ",பணம் )
def change(amount): #argument 
	amount = 2000 #local variable
	print("Change needed for ", amount)
	
amount = 10000#global variable
print("To be spent ", amount)
change(amount)  #function calling - parameter 
print("After getting change ", amount)
