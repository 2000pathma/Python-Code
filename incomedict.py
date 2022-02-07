employees = {'kathir':1000, 'kavin':2000, 'arul':3000, 'viyan': 1800,'kabil':2010 }
total_income = 0
for key in sorted(employees):
    print(key, ':', employees[key])
    total_income += employees[key] 
print(total_income)
for value in employees.values():
    total_income += value
