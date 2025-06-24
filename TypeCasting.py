# Typecasting = Converting a variable from one datatype to another
#               str(), int(), float(), bool() functions

brandName = "code.io"
blankName = ""
brandYear = 2025
brandPrice = 3.2
isNew = True

# To find the Type of variable's declared

print(type(brandName))
print(type(brandYear))
print(type(brandPrice))
print(type(isNew))

# Converting Float to Integer

brandPrice = int(brandPrice)
print(f"Float to Integer: {brandPrice}")
print(type(brandPrice))

# Converting Integer to Float

brandYear = float(brandYear)
print(f"Integer to FLoat: {brandYear}")
print(type(brandYear))

# Converting Integer to String

brandPrice = str(brandPrice)
print(f"Integer to String: {brandPrice}")
print(type(brandPrice))

# String Concatenation

brandPrice = brandPrice + "1"
print(f"String Concatenation: {brandPrice}")

# Converting String to Bool

# When we convert a String with 1 or more character to bool, it returns true

brandName = bool(brandName)
print(f"String to Bool with >= 1 characters: {brandName}")
print(type(brandName))

# When we convert a String with 0 characters, it returns false
# This can be used to check if user enters a input or not

blankName = bool(blankName)
print(f"String to Bool with 0 characters: {blankName}")
print(type(blankName))