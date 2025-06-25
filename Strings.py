# Strings        = Series of characters

# Index of a String = S t r i n g...
#                     0 1 2 3 4 5...

# Negative Index =  S  t  r  i  n  g
#                  -6 -5 -4 -3 -2 -1

# String Methods = Built-in functions that help to perform operations on Strings

name = input("Enter your Name: ")

# Length of a String = len(variable)
#                      Whitespaces are also considered as length

result = len(name)
print(f"The length of Your name is {result}.")

# First Occurrence of a given character = variable.find("character")

result = name.find("h")
print(f"The First Occurrence of character is {result}.")

# Last Occurrence of a given character = variable.rfind("character")
# r                                    = Reverse

result = name.rfind("h")
print(f"The Last Occurrence of character is {result}.")

# If a given character is not located = -1

result = name.find("$")
print(f"$ not found: {result}")

# Capitalize the first letter in a string = variable.capitalize()

result = name.capitalize()
print(f"Capitalized First Letter: {result}")

# Upper case all characters in a string = variable.upper()

result = name.upper()
print(f"Upper cased: {result}")

# Lower case all characters in a string = variable.lower()

result = name.lower()
print(f"Lower cased: {result}")

# To check if a String has a digit = variable.isdigit()
# Returns "True" if the string is ONLY digits [abc123 would return false]

result = name.isdigit()
print(f"Is there a digit: {result}")

# To check if a String has only alphabets = variable.isalpha()
# Special characters, Spaces, numbers return False

result = name.isalpha()
print(f"Only Alphabet: {result}")

# To count the number of a single character in a string = variable.count("character")

result = name.count("h")
print(f"Count: {result}")

# Replace any Occurrence with another character = variable.replace("old char", "new char")
# Very Useful Method

result = name.replace("h", " ")
print(f"Replace: {result}")

# To find all the String Methods = help(datatype)

print(help(str))

# Indexing = Accessing elements of a sequence using [] [indexing operator]
#            [Start : end : step]

# [Start] # First Element

print(name[0])

# [Start : End] # First 4 Elements
# Ending index is exclusive i.e., not included

print(name[0 : 4])

# [Start:] # 3rd element to end

print(name[2:])

# Negative Index # Last Element

print(name[-1])

# [Step] # 1st element and 2 elements after the 1st element

print(name[::2])



