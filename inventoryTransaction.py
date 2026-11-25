
stock = {"pen": 10, "book": 5, "bag": 2}

transactions = [
    {"type": "receive", "item": "pen", "quantity": 4},
    {"type": "sell", "item": "book", "quantity": 3},
    {"type": "sell", "item": "bag", "quantity": 5},
    {"type": "receive", "item": "ruler", "quantity": 6},
    {"type": "sell", "item": "pen", "quantity": 8}
]

accepted = 0
rejected = 0

for transaction in transactions:
    item = transaction["item"]
    quantity = transaction["quantity"]

    if transaction["type"] == "receive":
        if item in stock:
            stock[item] += quantity
        else:
            stock[item] = quantity

        accepted += 1

    elif transaction["type"] == "sell":
        if item in stock and stock[item] >= quantity:
            stock[item] -= quantity
            accepted += 1
        else:
            print("Transaction rejected:", item, "not enough stock")
            rejected += 1

print("\nFinal Stock:")
print(stock)

print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)
