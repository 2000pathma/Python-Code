f= open("C:\\Users\\2000p\\Documents\\Java\\test4.txt","w+")
import os
fname = input("Enter file name with location")
if os.path.isfile(fname):
    print("File is Present")
    f=open(fname,'r')
    print(f.mode)
    print(
f.read
())
else:
    print('file not present')
