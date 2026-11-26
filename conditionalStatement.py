
mark = int(input("Enter the mark: "))

if mark < 0 or mark > 100:
    print("Invalid mark")

else:
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if mark >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
