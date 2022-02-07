employees = {'kathir':500, 'kavin':2000, 'arul':3000, 'viyan': 1800,'kabil':1010 }
new_employees={}  #new dictionary
for key, value in employees.items():
    if value <= 1800:
        new_employees[key] = value
print(new_employees)
