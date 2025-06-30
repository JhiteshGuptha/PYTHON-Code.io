# Dictionary = collection of {key:value} pairs
#            = ordered and changeable. NO Duplicates
#            = Each key:value pair is seperated with a comma
#            = {Key:Value} pair can be of any datatype

# Dictionary

currency = {"USA" : "Dollar", "Europe" : "Euro", "India" : "Rupee"}
print(currency)
print()

price = {"Pizza": 10, "Cheese" : 3, "Milk" : 2.50}
print(price)
print()

# Iterating over a Dictionary to display all the Keys using a loop
# You can also Display all the keys using Keys() method

for i in currency:
    print(i)
print()

for j in price:
    print(j)
print()

# Length of a Dictionary

print(f"{len(currency)} elements")
print(f"{len(price)} elements")
print()

# To check if a Key is in a Dictionary = in operator
# Returns a Boolean value = True or False

print("USA" in currency)
print("Bread" in price)
print()

# Dictionary Methods

# Getting the value using a key = variable.get(key)
# Returns "None" if a key does not exist

print(currency.get("USA"))
print(currency.get("Europe"))
print(currency.get("India"))
print()
print(price.get("Pizza"))
print(price.get("Cheese"))
print(price.get("Milk"))
print()

# Updating a Dictionary = variable.update({key:value})
# You can Either inset a new Key:Value pair
# You can also update an existing Key:Value pair

currency.update({"Japan" : "Yen"})
print(currency)
print()

# Remove a Key:Value pair from a dictionary = variable.pop(key)

currency.pop("Japan")
print(currency)
print()

# Display all the Keys in a dictionary = variable.keys()
# Returns a dictionary object with list of keys

print(currency.keys())
print()

# Display all the values in a dictionary = variable.values()
# Returns a dictionary object with List of values

print(currency.values())
print()

# To view the values outside a List = using a for loop

for values in currency.values():
    print(values)
print()

# To display all the Key:Value pairs = variable.items()
# Returns a dictionary object with a 2d list of tuples
# items = [(), (), ()]

print(price.items())
print()

# To view each Key:value pair individually

for key, value in price.items():
    print(f"{key} : {value}")
print()
 