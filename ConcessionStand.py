# Concession Stand Program = Snack Stands available at Movie Theatre
# dictionary = {Key:value}

snacks = {"popcorn" : 1, "hot Dog" : 2, "pretzel" : 2, "candy" : 1, "soda" : 1, "water" : 1}

selection = []

total = 0

print("Snacks     Price")
for key, value in snacks.items():
    print("---------------")
    print(f"{key:10}: ${value}")

print("---------------")
print()

while True:
    userInput = input("Select Snacks [q to Quit]: ").lower()
    if userInput == "q":
        break
    elif snacks.get(userInput) is not None:
        selection.append(userInput)

for userInput in selection:
    total += snacks.get(userInput)

print("----------------------------------")
print(f"Food Items Selected: {selection}")
print(f"Amount to Pay: ${total}")