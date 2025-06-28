# Shopping cart program to practice List, Tuples and Sets

foods = []
prices = []
totalPrice = 0

while True:
    item = input("Add Items or q to exit: ")
    if item.lower() == "q":
        print("Thankyou for adding the Products")
        print()
        break
    else:
        price = float(input(f"Enter Price of {item}: $"))
        foods.append(item)
        prices.append(price)

print("----Your Cart----")
print(f"Products Purchased: {foods}")

for price in prices:
    totalPrice = totalPrice + price

print(f"Total Price of all Products: ${totalPrice}")




