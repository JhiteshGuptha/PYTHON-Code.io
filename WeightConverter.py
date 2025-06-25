# Weight Converter Program in Python
# Pounds to Kilogram and Vice Versa

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds Input? [Kg or Lbs]: ")
if unit == "Kg":
    pounds = weight * 2.20462
    print(f"{round(pounds, 1)} Lbs")
elif unit == "Lbs":
    kilograms = weight * 0.453592
    print(f"{round(kilograms, 1)} Kg")
else:
    print("Wrong Unit Selection, Please Select again")