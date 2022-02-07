#No. of lines, No. of words, No. of characters

import os
fname = input("Enter file name with location")
if os.path.isfile(fname):
    lcount = wcount = ccount = 0 
    print("File is Present")
    f=open(fname,'r')  # f - object 
    for line in f:  # 
        lcount=lcount+1
        words = line.split() #'This, is, Raja'
        wcount = wcount +len(words) #3
        ccount = ccount+len(line)  #15 
    print(lcount)
    print(wcount)
    print(ccount)
    print(
f.read
())
else:
    print('file not present')
