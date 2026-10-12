marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

valid_marks = []
grade_counts = {"A": 0, "B": 0, "C": 0, "F": 0}

for mark in marks:
    if mark < 0 or mark > 100:
        continue

    valid_marks.append(mark)

    if mark >= 80:
        grade_counts["A"] += 1
    elif mark >= 70:
        grade_counts["B"] += 1
    elif mark >= 60:
        grade_counts["C"] += 1
    else:
        grade_counts["F"] += 1

average = sum(valid_marks) / len(valid_marks)

print("Valid marks:", valid_marks)
print("Grade counts:", grade_counts)
print("Average: {:.2f}".format(average))