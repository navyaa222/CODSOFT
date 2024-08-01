def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation: ")
    
    if operation == '1' or operation == '+':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2' or operation == '-':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3' or operation == '*':
        result = num2 * num2
        operation_symbol = '*'
    elif operation == '4' or operation == '/':
        if num2 != 0:
            result = num1 / num2
            operation_symbol = '/'
        else:
            result = "undefined (cannot divide by zero)"
            operation_symbol = '/'
    else:
        print("Invalid input! Please enter a valid operation.")
        return

    print(f"The result of {num1} {operation_symbol} {num2} is: {result}")

calculator()
