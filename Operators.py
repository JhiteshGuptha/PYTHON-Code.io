# Arithmetic Operators

numberOne = int(input("Enter First number to perform Operations: "))
numberTwo = int(input("Enter Second number to perform Operations: "))

print()
print("|----Arithmetic----|")
print()
print(numberOne + numberTwo) # Addition
print(numberOne - numberTwo) # Subtraction
print(numberOne * numberTwo) # Multiplication
print(numberOne / numberTwo) # Division
print(numberOne % numberTwo) # Modulo / Reminder
print(numberOne ** numberTwo) # Power

# Assignment Operators / Augmented operator

print()
numberThree = int(input("Enter Third number to perform Operations: "))

print()
print("|----Assignment----|")
print()
numberThree += 2 #numberThree = numberThree + 2
print(numberThree)

numberThree -= 2 #numberThree = numberThree - 2
print(numberThree)

numberThree *= 2 #numberThree = numberThree * 2
print(numberThree)

numberThree /= 2 #numberThree = numberThree / 2
print(numberThree)

numberThree %= 2 #numberThree = numberThree % 2
print(numberThree)

numberThree **= 2 #numberThree = numberThree * numberThree
print(numberThree)

# Comparison Operator
# The result of Comparison operator is always boolean [True or False]

print()
print("|----Comparison----|")
print()
print(numberOne == numberTwo) # Equal to
print(numberOne != numberTwo) # Not Equal to
print(numberOne > numberTwo) # Greater than
print(numberOne < numberTwo) # Less than
print(numberOne >= numberTwo) # Greater than or Equal to
print(numberOne <= numberTwo) # Less than or Equal to

# Logical Operators = evaluate multiple conditions at once [Or, And, Not]
#                     And = Both conditions should be true
#                     Or  = At least one Condition must be true
#                     Not = Inverts the Condition [not False, not True]

# And Operator

print()
print("|----Logical----|")
print()
temperature = 30
isSunny = True
isRaining = True
isCold = False

if temperature > 28 and isSunny:
    print("It is Sunny☀️")
elif temperature <= 28 and not isSunny: # Not Operator
    print("It is Pleasant outside 🌥️")
elif 28 > temperature > 10 and isSunny:
    print("It is Warm outside ⛅️")
print()

# Or Operator

if temperature > 28 or isRaining:
    print("The event is cancelled ❎")
elif temperature < 28 or not isRaining: # Not Operator
    print("The Event is scheduled 😁")


# Membership Operator = used to test whether a value or variable is found in a sequence
#                     = (string, list, tuple, set or dictionary)
#                     = 1. in
#                     = 2. not in

print()
print("|----Membership----|")
print()
word = "ORANGE"
letter = input("Guess a letter in the secret word: ").upper()
if letter in word:
    print(f"There is {letter} in the Word 🥳")
else:
    print(f"{letter} is not in the word 😕")
print()

numbers = [1,2,3,4,5,6,7,8,9]
number = int(input("Guess a Number: "))
if number not in numbers:
    print(f"{number} is not in the List 😕")
else:
    print(f"{number} is in the List 🥳")