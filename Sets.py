# Collection = single "variable" used to store multiple values

# Set = {} unordered and immutable [cannot change], NO Duplicates
#     = We can add and remove values
#     = The input will not have the same order as we have declared the elements in a set
#     = Sets do not have Index as they are unordered

# Set

fruits = {"apple", "mango", "banana"}
print(fruits)
print()

numbers = {22, 33, 44}
print(numbers)
print()

# print(fruits[0]) ERROR

# Iterating over a list using for loop
# The output changes everytime you run the program as it is unordered

for fruit in fruits:
    print(fruit)
print()

for number in numbers:
    print(number)
print()

# Length of a Set

print(f"{len(fruits)} elements")
print(f"{len(numbers)} elements")
print()

# To check if a value is in a set = in Operator
# Returns a Boolean value = True or False

print("mango" in fruits)
print("55" in numbers)
print()

# Set Methods

# Add an Element to the Set = variable.add(element)

fruits.add("pineapple")

# remove an element from the set = variable.remove(element)

fruits.remove("apple")

for fruit in fruits:
    print(fruit)
print()

# To remove the first element from the set = variable.pop()
# The element that would be removed is RANDOM because it's unordered

fruits.pop()
for fruit in fruits:
    print(fruit)
print()

# To clear a set = variable.clear()

fruits.clear()
print(fruits)