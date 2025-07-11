# Collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates are okay
#      = You cannot add or remove element

# List = ["element1", "element2", element3"]
# index =     0            1          2

# List

fruits = ["apple", "mango", "banana"]
print(fruits)
print()

numbers = [22, 33, 44]
print(numbers)
print()

# Accessing Single Element inside a List

print(fruits[0])
print(fruits[1])
print(fruits[2])
print()

# Accessing with Range: [Start, end , Step]

# [start: end]

print(fruits[0:3])
print()

# [Step]

print(fruits[::2])
print()

# Reversing the list using Step

print(fruits[::-1])
print()

# Iterating over a list using for loop

for fruit in fruits:
    print(fruit)
print()

for number in numbers:
    print(number)
print()

# Length of a list

print(f"{len(fruits)} elements")
print(f"{len(numbers)} elements")
print()

# To check if a value is in a list = in operator
# Returns a Boolean value = True or False

print("mango" in fruits)
print("55" in numbers)
print()

# Changing an element value inside the list

fruits[0] = "orange"
for fruit in fruits:
    print(fruit)
print()

# List Methods

# To get the Index of an element = variable.index(element)

print(f"Index of \"mango\": {fruits.index("mango")}")
print()

# Add or Append an element at the end of the list = variable.append(element)

fruits.append("pineapple")

# Remove an element from the list = variable.remove(element)

fruits.remove("orange")

# Inserting an element at a given index = variable.insert(index, element)

fruits.insert(0, "orange")

# Sorting all the elements in a list = variable.sort()
# Arranges in alphabetical order with low to high order

fruits.sort()

for fruit in fruits:
    print(fruit)
print()

# Count the number of occurrence of a single element = variable.count(element)

print(f"Occurrence of \"mango\": {fruits.count("mango")}")
print()

# To clear a list = variable.clear()

fruits.clear()
print(fruits)
print()

# A 2D List = A List inside a List
#           = Single list should be created before creating a 2d list
#           = Think of it like a matrix with rows and columns

# Individual Lists

fruit = ["apple", "orange", "banana"]
vegetables = ["tomato", "carrot", "onion"]
dairy = ["milk", "cheese", "bread"]

# 2D List

groceries = [fruit, vegetables, dairy]

# Printing 2D List
# Prints each list seperated with a comma

print("----2D List----")
print()
print(groceries)
print()

# Accessing each list inside a 2d list using index

print(groceries[0])
print(groceries[1])
print(groceries[2])
print()

# Accessing elements inside each list from a 2d list

print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])
print()

# Iterating over each list inside a 2D List

for lists in groceries:
    print(lists)
print()

# Iterating over each element inside a list in a 2D List

for lists in groceries:
    for elements in lists:
        print(elements)
print()

# List Comprehension = A concise way to create Lists in Python
#                    = Compact and easier to read than Traditional Loops
#                    = [expression for value in iterable if condition]
#                    = Expression is returned/added inside the list

# Basic List Creation

square = []
for i in range(1, 11):
    square.append(i * i)
print(square)
print()

# Using List Comprehension

square = [i * i for i in range(1, 11)]
print(square)
print()

fruits = [fruit.capitalize() for fruit in ["apple", "orange", "banana", "mango"]]
print(fruits)
print()

# Using List Comprehension with condition

positiveNumbers = [num for num in range(-5, 6) if num >= 0]
negativeNumbers = [num for num in range(-5, 6) if num < 0]
print(positiveNumbers)
print(negativeNumbers)
print()