# Collection = single "variable" used to store multiple values

# Tuple = () ordered and unchangeable. Duplicates are Okay
#       = You CANNOT add or remove element like List and Sets
#       = Faster compared to List and Set

# Tuple = ("element1", "element2", element3")
# index =     0            1          2

# Tuple

fruits = ("apple", "mango", "banana")
print(fruits)
print()

numbers = (22, 33, 44)
print(numbers)
print()

# Accessing Single Element inside a Tuple

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

# Reversing the tuple using Step

print(fruits[::-1])
print()

# Iterating over a Tuple using for loop

for fruit in fruits:
    print(fruit)
print()

for number in numbers:
    print(number)
print()

# Length of a Tuple

print(f"{len(fruits)} elements")
print(f"{len(numbers)} elements")
print()

# To check if a value is in a tuple = in operator
# Returns a Boolean value = True or False

print("mango" in fruits)
print("55" in numbers)
print()

# fruits[0] = "orange" ERROR

# Tuple Methods

# To get the Index of an element = variable.index(element)

print(f"Index of \"mango\": {fruits.index("mango")}")
print()

# Count the number of occurrence of a single element = variable.count(element)

print(f"Occurrence of \"mango\": {fruits.count("mango")}")
print()

# fruits.clear() ERROR
