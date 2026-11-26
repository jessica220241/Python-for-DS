
numbers = [12, 7, -4, 12, 18, 5, -3, 8, 18]

non_negative = []
unique_numbers = []

negative_count = 0
even_sum = 0

for num in numbers:

    if num < 0:
        negative_count += 1
        continue

    non_negative.append(num)

    if num not in unique_numbers:
        unique_numbers.append(num)

    if num % 2 == 0:
        even_sum += num

# Elements at indices 1, 3, 5 and 7
selected = numbers[1:8:2]

print("Non-negative numbers:", non_negative)
print("Unique non-negative numbers:", unique_numbers)
print("Sum of even non-negative numbers:", even_sum)
print("Number of negative numbers:", negative_count)
print("Elements at indices 1, 3, 5 and 7:", selected)
