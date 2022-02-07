f= open("C:\\Users\\2000p\\Documents\\Java\\test3.txt","w+")
import os
fname = input("Enter file name with location")
if os.path.isfile(fname):
    print("File is Present")
    f=open(fname,'r')
    print(
    f.read())
else:
    print('file not present')
