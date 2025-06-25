# if = Do something only if Condition is True
#      else = Do something else
#      Take care of the indentation when you are working with if statements

age = int(input("Enter Your Age to verify Sign-up Info: "))

if age >= 16:
    print("You have successfully signed up, Continue Browsing!")
else:
    print("Age limit: Greater than or equal to 16")

# else if = check multiple if conditions when the initial condition is False
#           The Elif block of code is executed only if the previous condition is false

if age >= 100:
    print("Invalid Age, Please enter Correct Age")
elif age <= 0:
    print("Invalid Age, Please enter Correct Age")
elif age >= 16:
    print("You have successfully signed up, Continue Browsing!")
else:
    print("Age limit: Greater than or equal to 16")

# Boolean with If Statements

isActive = True

if isActive:
    print("The user is Active")
else:
    print("The user is Not active")

# Ternary Operator: Short form of If Else

result = "The user is Active" if isActive else "The user is Not active"
print(result)

