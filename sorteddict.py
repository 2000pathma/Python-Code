employees = {'kathir':1000, 'mathi':2000, 'arul':3000, 'viyan': 1800,'kathir':2010 }
for key in sorted(employees):
    print(key, ':', employees[key])
for value in sorted(employees.values()):
    print(value)
for item in sorted(employees.items()):
    print(item)
