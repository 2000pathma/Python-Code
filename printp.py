HRNames=['priya','sathya','nithya']
TestersNames=['pavi','suthan','kumar']
DeveloperNames=['puvana','arjun','pooja']
AdminNames=['paramu','bheem','krishna']
Total=[HRNames,TestersNames,DeveloperNames,AdminNames]
print("Total names:")
list=0
while list<len(Total):
    member = 0
    while member < len(Total[list]):
        if(Total[list][member][0]=="p" or Total[list][member][0]=="p"):
            print(Total[list][member], end=' ')
        member+=1
    print()
    list+=1 #print only starting with p names
