
# Grocery Shop Billing System
# Available products
prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

print("Available Products:")
for item, price in prices.items():
    print(item, ":", price)

order = {}

n = int(input("\nHow many order entries? "))

for i in range(n):
    item = input("\nEnter product " + str(i + 1) + ": ").lower()
    quantity = int(input("Enter quantity: "))

    if item not in prices:
        print(item, "is not available.")

    elif quantity <= 0:
        print("Quantity must be positive.")

    else:
        order[item] = order.get(item, 0) + quantity

print("\nFinal Order:")
print(order)

bill = {}

subtotal = 0

for item, quantity in order.items():
    unit_price = prices[item]
    total = quantity * unit_price

    bill[item] = {
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    subtotal += total

if subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

vat = (subtotal - discount) * 0.02

final_amount = subtotal - discount + vat

print("\nBill Dictionary:")
print(bill)

print("\n============== GROCERY SHOP BILL ==============")
print()

print("{:<12}{:>10}{:>14}{:>12}".format(
    "Item", "Quantity", "Unit Price", "Total"
))

print("-" * 48)

for item, details in bill.items():
    print("{:<12}{:>10}{:>14.2f}{:>12.2f}".format(
        item,
        details["quantity"],
        details["unit_price"],
        details["total"]
    ))

print("-" * 48)

print("{:<30}Tk {:>10.2f}".format("Subtotal:", subtotal))
print("{:<30}Tk {:>10.2f}".format("Discount (5%):", discount))
print("{:<30}Tk {:>10.2f}".format("VAT (2%):", vat))

print("-" * 48)

print("{:<30}Tk {:>10.2f}".format("Final Amount:", final_amount))

print("=" * 48)
