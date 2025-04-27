
def calculate_two_numbers():
    print("Calculating two numbers")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    calculate = input("Enter the operation (+, -, *, /): ")

    if calculate == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif calculate == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif calculate == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif calculate == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif calculate == '%':
        if num2 == 0:
            print("Error: Modulo by zero")
        else:
            print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Invalid operation")

calculate_two_numbers()
