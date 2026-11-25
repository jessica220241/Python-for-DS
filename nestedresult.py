
scores = {
    "Amina": {"python": 82, "statistics": 76, "calculus": 88},
    "Maya": {"python": 58, "statistics": 64, "calculus": 61},
    "Disha": {"python": 91, "statistics": 89, "calculus": 94},
    "Nora": {"python": 45, "statistics": 52, "calculus": 56}
}

results = {}

for student, marks in scores.items():
    average = sum(marks.values()) / len(marks)

    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"

    results[student] = {
        "average": round(average, 2),
        "status": status
    }

print("Student Results:")
print(results)

highest_student = max(results, key=lambda student: results[student]["average"])

print("\nStudent with the highest average:")
print(highest_student)
print("Highest Average:", results[highest_student]["average"])
