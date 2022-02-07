details={'Gokul':5000,'Rahul':4000,'Ashok':3000,'Pranesh':4000}
for key in sorted(details):
	print('Prints Defaul Asc Order ',key,':',details[key])
#Try in Different way this is For By Default Ascending Order Muthu sir Code , just added Reverse Function near to sort

details={'Gokul':5000,'Rahul':4000,'Ashok':3000,'Pranesh':4000}
for key in sorted(details,reverse=False):
	print('Prints Defaul Asc Order ',key,':',details[key])
#Try in Different way this is For By Descending Order Muthu Sir Assignment used Reverse function in sort just added Reverse function-True:
for key in sorted(details,reverse=True):
	print('Muthu Sir Assignment Descending Order ',key,':',details[key])
