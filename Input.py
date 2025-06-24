# input() = Built in function that prompts the user to enter data
#           Returns the entered data as a string
#           Input is entered in the console

language = input("What's Your Favorite Programming Language?: ")
print(f"Language Selected: {language}")

# Converting Input into Integer using Type Casting

number = int(input("Enter an integer to increment by 1: "))
number = number + 1
print(f"Final Value: {number}")

# Area of Square Problem to understand Float Conversion of input

side = float(input("Enter Side of Square: "))
area = side * side
print(f"Area of Square is: {area}cm²")

