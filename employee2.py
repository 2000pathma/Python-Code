#specific conditions of value is print value>=1800
employees = {'kathir':1000, 'kavin':2000, 'arul':3000, 'viyan': 1800,'kathir':2010 }
new_employees={}  #new dictionary
for key, value in employees.items():
    if value >= 1800:
        new_employees[key] = value
print(new_employees)
