# Variable Scope = Where a variable is Visible and Accessible
# Scope Order = Local -> Enclosed -> Global -> Built in

# Local Variables = Variables declared within a function
#                 = Name is local in Function1 and cannot be accessed by Function2
#                 = year is local in Function2 and cannot be accessed by Function1
#                 = You can use the same Variable Name in both the Functions

def function1():
    name = "Code.io"
    print(name)

def function2():
    year = 2025
    print(year)
    print()

function1()
function2()

# Enclosed Variables = Local Variable inside one Function used within another Function

def function1():
    name = "Code.io"
    def function2():
        print(name)
        print()
    function2()

function1()

# Global Variables = Variable that can be used anywhere
#                  = Can be used within or outside the function

quantity = 3

def function1():
    print(quantity)

def function2():
    print(quantity)
    print()

function1()
function2()

# Built-in Variables = Variables Pre-Defined inside Python
#                    = Math Module Variables

import math

def function1():
    print(math.pi)

def function2():
    print(math.e)
    print()

function1()
function2()