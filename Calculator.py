# Calculator Program in Python

numberOne = float(input("Enter the First Number: "))
operation = input("Enter the Operation to perform [+, -, *, /, %, **]: ")
numberTwo = float(input("Enter the Second Number: "))

if operation == "":
    print("Please enter which operation to perform")

if operation == "+":
    result = numberOne + numberTwo
    print(round(result, 1))
elif operation == "-":
    result = numberOne - numberTwo
    print(round(result, 1))
elif operation == "*":
    result = numberOne * numberTwo
    print(round(result, 1))
elif operation == "/":
    result = numberOne / numberTwo
    print(round(result, 1))
elif operation == "%":
    result = numberOne % numberTwo
    print(round(result, 1))
elif operation == "**":
    result = numberOne ** numberTwo
    print(round(result, 1))
else:
    print("Please enter a valid operator")



