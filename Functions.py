# Function = A block of Reusable Code
#          = place () after the function name to invoke it

# Define and Declare the Function

def message():
    print("Welcome to Code.io")
    print("We are learning Python")
    print()

# Call the Function

message()

# Send Values / Variables to a Function
# Parameter = Inside Function Declaration
#           = The DATATYPE of Arguments and Parameter should be same
#           = Position of Parameter Matters

def greeting(name):
    print(f"Hi {name}, Thankyou for Referring to Code.io")
    print()

inputName = input("Enter Your Name: ")

# Send the Input to the function
# Argument = Inside Function Call
#          = Position of Argument Matters

greeting(inputName)

# Sending 2 Argument

def total(i, j):
    print(f"{i} + {j} = {i + j}")
    print()

x = int(input("Enter First Number to find Sum: "))
y = int(input("Enter Second Number to find Sum: "))

total(x, y)

# Sending 3 Arguments

def invoice(username, amount, date):
    print(f"Hello {username}")
    print(f"Your Bill of ${amount:.2f} is due on: {date}")
    print()

invoice("Code.io", 45.90, "01/01/2001")

# Return = Statement used to end a function
#        = Send a result back to the caller

def multiply(p, q):
    z = p * q
    return z

x = int(input("Enter First Number to find Product: "))
y = int(input("Enter Second Number to find Product: "))
print(f"{x} x {y} = {multiply(x, y)}")
print()

def fullname(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

firstName = input("Enter Your First Name: ")
lastName = input("Enter Your Last Name: ")
print(f"Your Full Name: {fullname(firstName, lastName)}")
print()
