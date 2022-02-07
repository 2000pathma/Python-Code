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
         print(Total[list][member], end=' ')
         member+=1
    print()
    list+=1#PRINT ALL MEMBERS NAME
