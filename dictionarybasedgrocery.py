
products = {
    "rice": 75,
    "milk": 90,
    "bread": 55,
    "egg": 15,
    "apple": 180,
    "oil": 190,
    "sugar": 130,
    "salt": 45,
    "soap": 60,
    "tea": 220
}

order = {}

print("Available Products:")

for item, price in products.items():
    print(item, ":", price)

while True:
    item = input("\nEnter product name (or done): ").lower()

    if item == "done":
        break

    if item not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be positive")
        continue

    order[item] = order.get(item, 0) + quantity

print("\nItemised Bill")

grand_total = 0

print("{:<12}{:>10}{:>12}{:>12}".format(
    "Product", "Price", "Quantity", "Total"
))

for item, quantity in order.items():

    price = products[item]
    total = price * quantity

    grand_total += total

    print("{:<12}{:>10}{:>12}{:>12}".format(
        item, price, quantity, total
    ))

print("\nGrand Total: Tk", grand_total)
