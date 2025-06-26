# Compound Interest calculator Program in Python

import math

principal = float(input("Enter the Initial Deposit or Loan Amount: "))
rate = (float(input("Enter Annual Interest Rate: ")))/100
numberTimes= int(input("Enter the Number of Times that Interest is compounded per Year: "))
time = int(input("Enter the Number of Years the Money is Invested: "))

while principal <= 0:
    print("Principal Cannot be -ve or 0")
    principal = float(input("Enter the Initial Deposit or Loan Amount: "))

while rate <= 0:
    print("rate Cannot be -ve or 0")
    rate = (float(input("Enter Annual Interest Rate: ")))/100

while numberTimes <= 0:
    print("Number of Times Cannot be -ve or 0")
    numberTimes= int(input("Enter the Number of Times that Interest is compounded per Year: "))

while time <= 0:
    print("Time Cannot be -ve or 0")
    time = int(input("Enter the Number of Years the Money is Invested: "))


userInput = input("Do you wanna calculate the Future Value or Compound Interest [A or CI]: ")

totalAmount = principal * pow((1 + (rate / numberTimes)), (numberTimes * time))

if userInput == "A":
    print(f"Future Value (A): ${totalAmount:.2f}")
elif userInput == "CI":
    compoundInterest = totalAmount - principal
    print(f"Compound Interest(CI): ${compoundInterest:.2f}")
else:
    print("Invalid Input Selection")



