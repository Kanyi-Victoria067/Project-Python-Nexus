from unittest import result


def calculator():
    print("This is a simple calculator.")
    print("Supported operations include: +, -, *, /")

    num1 = float(input("Enter the first digit: "))
    operator = input("Enter the operator: ")
    num2 = float(input("Enter the second digit: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        try:
            result = num1 / num2
            print(result)
        finally:
            print("Division by zero is not allowed")

    else:
        print("Enter valid values and operator.")

    print(num1, operator, num2, "=", result)

calculator()
