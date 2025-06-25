# Temperature Conversion in Python
# Fahrenheit to Celsius and Vice Versa

temperature = float(input("Enter Temperature: "))
unit = input("Enter F if Fahrenheit or C if Celsius: ")
if unit == "F":
    celsius = (temperature - 32) * (5/9)
    print(f"{round(celsius, 1)}°C")
elif unit == "C":
    fahrenheit = (temperature * (9/5)) + 32
    print(f"{round(fahrenheit, 1)}°F")
else:
    print("Wrong Unit Selection, Please Select again")
