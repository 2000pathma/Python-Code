# June3,2020
# + read and write
f= open("C:\\Users\\2000p\\Documents\\Java\\test1.txt","w+")
f.write("priya@tneducation.org\n")
for i in range(1,11):
    f.write("This is line %d\n" %(i))
f.close()
print ("output")
f= open("C:\\Users\\2000p\\Documents\\Java\\test1.txt","w+")   # opens in read mode
print (f.read())
f.close()

print ("\n")
print ("output")
f= open("C:\\Users\\2000p\\Documents\\Java\\test1.txt","w+")   
print (f.readline())
f.close()
print ("\n")
print ("output")
f= open("C:\\Users\\2000p\\Documents\\Java\\test1.txt","w+")  
print (f.readlines())
f.close()
f= open("C:\\Users\\2000p\\Documents\\Java\\test1.txt","w+") 
for x in f:
    print (x,end=' ')
f.close()
