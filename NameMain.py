# if __name__ == "__main__" = Code inside this will only execute if we run the file directly
#                           = If we import this file and run, the code inside will not execute
#                           = It's not necessary to name your file as main for it to run
#                           = Mostly used to write some hidden code / test code which is not executed when imported

def greet(name):
    print(f"Hello {name}")

def square(number):
    return number * number

print("This print statement is outside (if __name__ == \"__main__\"), hence it will always execute even if i import this file")
print()

# 1

def main():
    print("----------------------------------------------------")
    print("Running (if __name__ == \"__main__\") in NameMain.py")
    print("--------------------------------------------------\n")
    print(f"The value of __name__ is {__name__}")
    greet("Code.io")
    print(square(5))

if __name__ == "__main__":
    main()

# 2
# 1 and 2 are the same, just used function in 1

# if __name__ == "__main__":
#     print("This is running because i executed the file directly instead of importing")
#     print(f"The value of __name__ is {__name__}")
#     print("\n----Running Functions-----\n")
#     greet("Code.io")
#     print(square(5))


