# if = Do something only if Condition is True
#      else = Do something else
#      Take care of the indentation when you are working with if statements

age = int(input("Enter Your Age to verify Sign-up Info: "))

if age >= 16:
    print("You have successfully signed up, Continue Browsing!")
else:
    print("Age limit: Greater than or equal to 16")
print()

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
print()

# Boolean with If Statements

isActive = True

if isActive:
    print("The user is Active")
else:
    print("The user is Not active")
print()

# Ternary Operator: Short form of If Else

result = "The user is Active" if isActive else "The user is Not active"
print(result)
print()

# Switch = An alternative to using many "elif" statements
#        = Execute some code if a value matches a "case"
#        = cleaner and syntax is more readable

def week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "No Day Found 🗓️"

day = int(input("Enter a number [1-7] to find Day: "))
print(week(day))
