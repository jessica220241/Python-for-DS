stock={"pen": 12, "book": 3, "bag": 2, "ruler": 9, "calculator": 1}

total= 0
low_stock= {}

for product, quantity in stock.items():
    total+= quantity

    if quantity<5:
        low_stock[product]= quantity
print("Total units", total)
print("Low stock", low_stock)