#calculator program
repeat = 'Y'  #Yes 
print('Basic Calculator')
 
while repeat == 'Y':
    num1 = float(input('Enter first number: '))#user should give us first number
    operator = input('''Enter your choice 
                        + -> addition,
                        - -> subtraction,
                        * -> multiplication,
                        / -> division,
                        // -> floor division
                        % -> modulus and
                        ** -> power operator
                        ''')#user enters operation(+-*%)
 
    num2 = float(input('Enter the second number: '))#user presses second number
    if operator == '+':
        answer = num1 + num2
        print(num1,' + ', num2, ' = ', answer)
    elif operator == '-':
        answer = num1 - num2
        print(num1,' - ', num2, ' = ', answer)
    elif operator == '*':
        answer = num1 * num2
        print(num1,' * ', num2, ' = ', answer)
    elif operator == '/':
        answer = num1 / num2
        print(num1,' / ', num2, ' = ', answer)
    elif operator == '//':
        answer = num1 // num2
        print(num1,' // ', num2, ' = ', answer)   
    elif operator == '%':
        answer = num1 % num2
        print(num1,' % ', num2, ' = ', answer)
    elif operator == '**':
        answer = num1 ** num2
        print(num1,' ** ', num2, ' = ', answer)#User presses equal operator
    else:
        print('Invalid, Please enter valid operator')
    y_or_n = input("Press 'Y' for another calculation")
    repeat = y_or_n.upper()  #No -> repeat = No
 
    if repeat != 'Y':
        print('Thank you')
