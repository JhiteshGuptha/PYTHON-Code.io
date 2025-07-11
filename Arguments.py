# Positional Arguments = Declaring Each Argument prior in the function call
#                      = Mandatory for a function to run, if not provided it's a TYPE ERROR

def total(i, j):
    print(f"{i} + {j} = {i + j}")
    print()

x = int(input("Enter First Number to find Sum: "))
y = int(input("Enter Second Number to find Sum: "))

total(x, y)

# Default Arguments = Default Value for certain Parameters
#                   = Default is used when that certain parameters are same for different inputs
#                   = Makes your function more flexible, reduces # of arguments
#                   = Placed AFTER Positional Arguments

def total_price(item_price, discount = 0.0, tax = 0.05):
    return item_price * (1 - discount) * (1 + tax)

itemCost = float(input("Enter Item Cost: "))
print(f"Item Total Price: {total_price(itemCost)}")
print()

# Using Arguments to Change the default function parameter
# Value assigned inside Argument is considered First, even if there is a Default Value

itemDiscount = float(input("Enter Discount: "))
print(f"Item Total Price: {total_price(itemCost, itemDiscount)}")
print()

# Keyword Arguments = Using Parameter Name in Argument as a Keyword
#                   = Helps with Readability
#                   = Order of Argument Does not matter
#                   = Placed AFTER Positional Arguments

def greeting(greet, title, first, last):
    print(f"{greet} {title}{first} {last}")
    print()

greeting("Hello", first="Abc", last="Def", title="Mr.")

# Arbitrary Arguments = Varying amount of Arguments
# *args               = Allows us to pass multiple non-keyword arguments
#                     = Each of this argument is stored in a tuple and send as a parameter
#                     = * Unpacking Operator

def add(*args):
    sum = 0
    print(type(args))
    for i in args:
        print(i, end=" ")
        sum += i
    return sum

print(f"\nTotal: {add(1, 2, 3, 4, 5)}")
print()

# Arbitrary Arguments = Varying amount of Arguments
# **kwargs            = Allows us to pass multiple keyword arguments
#                     = Each of this argument is stored in a dictionary and send as a parameter
#                     = * Unpacking Operator

def address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} {value}")

address(unit="1x", apartment="1234", street="abc", city="xyz", state="pqr", zip="67890")
