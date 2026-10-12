
delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}

combined = delivery_1.copy()

for product in delivery_2:
    if product in combined:
        combined[product] += delivery_2[product]
    else:
        combined[product] = delivery_2[product]

print("Combined delivery:", combined)

total = sum(combined.values())
print("Grand total:", total)
