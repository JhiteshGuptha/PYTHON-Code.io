# Shipping Label using Arbitrary Arguments

def label(*args, **kwargs):
    print("Customer Name: " , end="")
    for i in args:
        print(i, end="")
    print("\n\n-------------------------------")
    print("Customer Address: \n")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("-----------------------------------")


print("--------Shipping Label--------------\n")
print("--------Customer Details------------\n")
title = input("Title [Mr, Ms, Mrs, Miss, Dr]: ").capitalize()
firstName = input("First Name: ").capitalize()
lastName = input("Last Name: ").capitalize()
print("\n--------Address Details------------\n")
unitNumber = int(input("Unit Number: "))
apartmentNumber = int(input("Apartment Number: "))
streetName = input("Street: ").capitalize()
cityName = input("City: ").capitalize()
stateName = input("State: ").capitalize()
zipCode = int(input("Zip Code: "))
print("\n-------------Label---------------\n")
label(title, firstName, lastName,
      Unit=unitNumber,
      Apartment=apartmentNumber,
      Street=streetName,
      City=cityName,
      State=stateName,
      Zip=zipCode)