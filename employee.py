employees = {'kathir':101, 'kavin':105, 'arul':103, 'viyan': 104,'kathir':201 }
new_employees={}  #empty dictionary 
for key, value in employees.items():
    new_employees[value] = key
print(new_employees)
#output old key order {201: 'kathir'}
#{201: 'kathir', 105: 'kavin'}
#{201: 'kathir', 105: 'kavin', 103: 'arul'}
#{201: 'kathir', 105: 'kavin', 103: 'arul', 104: 'viyan'}
