# While Loop = execute some code while some condition remains true
#              Continues executing until the condition is True
#              Exists the loop if the condition becomes false
#              if you don't have an escape sentence, the loops run infinity times

name = input("Enter your Name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your Age: "))

while age < 0:
    print("Enter a Valid Age")
    age = int(input("Enter your Age: "))

print(f"Your Age is: {age}")

# For Loop = execute a block of code for a fixed number of times
#            Programmer can decide how many times they want the block of code to loop
#            You can iterate over a range, string, sequence and many more

# Range = (Start, End, step)
#         whatever you enter in End is exclusive [Not included]

for i in range(1, 11):
    print(i)
print() # Outside the loop

# Reverse Counting = reversed()

for i in reversed(range(1, 11)):
    print(i)
print()

# Adding Step
# Always begins at Start

for i in range(1, 11, 3):
    print(i)
print()

# Iterating over String

cardNumber = "1234-1234-1234-1234"

for i in cardNumber:
    print(i)
print()

# Break In For Loop = Breaks the loop or exist the loop when the condition is True

for i in range(1, 11):
    if i == 5:
        break
    else:
        print(i)
print()

# Continue in For Loop = Skip the Value when the condition is True

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)
print()

# Nested Loop = A loop within another Loop [Outer, Inner]
#               Outer Loop
#                  Inner Loop
#               For Each iteration of Outer loop, the inner loop runs for all it's iterations

for i in range(3):
    for j in range(1, 11):
        print(j, end="")
    print()
print()

# Print a Rectangle using Nested Loops

rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))
print()
for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()
print()