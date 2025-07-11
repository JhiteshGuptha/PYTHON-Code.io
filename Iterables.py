# Iterables = An Object/Collection that can return its element once at a time
#           = Iterates over a loop
#           = Python uses an inbuilt iter() function to iterate over a list
#           = NOT THE INDEX

# List

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
print()

for number in reversed(numbers):
    print(number)
print()

# Tuple

years = (2022, 2023, 2024, 2025)
for year in years:
    print(year)
print()

for year in reversed(years):
    print(year)
print()

# Sets = We can Iterate over a Set using a Loop
#      = How Can you iterate over a Set if there are no index inside a set? [Research]
#      = NOT Reversible

fruits = {"Mango", "Apple", "Banana", "Orange"}
for fruit in fruits:
    print(fruit)
print()

# String

name = "Code.io"
for character in name:
    print(character, end=" ")
print("\n")

# Dictionary

currency = {"USA" : "Dollar", "Europe" : "Euro", "India" : "Rupee"}
for key, value in currency.items():
    print(f"{key}: {value}")
print()