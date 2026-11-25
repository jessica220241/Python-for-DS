
sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}
]

revenue_by_product = {}
total_revenue = 0
high_revenue_transactions = []
invalid_records = 0

for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    price = sale["price"]

    if quantity <= 0 or price < 0:
        invalid_records += 1
        continue

    revenue = quantity * price

    if product in revenue_by_product:
        revenue_by_product[product] += revenue
    else:
        revenue_by_product[product] = revenue

    total_revenue += revenue

    if revenue >= 200:
        high_revenue_transactions.append(sale)

highest_product = max(revenue_by_product, key=revenue_by_product.get)

print("Revenue by Product:")
print(revenue_by_product)

print("\nTotal Revenue:")
print("Tk", total_revenue)

print("\nProduct with Highest Revenue:")
print(highest_product, "- Tk", revenue_by_product[highest_product])

print("\nTransactions with Revenue >= Tk 200:")
print(high_revenue_transactions)

print("\nNumber of Invalid Records:")
print(invalid_records)
