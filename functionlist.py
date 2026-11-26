
def analyse_marks(marks):

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    passed = 0
    failed = 0

    for mark in marks:

        if mark >= 50:
            passed += 1
        else:
            failed += 1

    return highest, lowest, average, passed, failed


student_marks = [78, 45, 82, 39, 67, 50, 91]

highest, lowest, average, passed, failed = analyse_marks(student_marks)

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
print("Number of students passed:", passed)
print("Number of students failed:", failed)
