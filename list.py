marks = [50, -100, -90, 200, 70, 99, 89, 80]

for mark in marks:

    if mark < 0 or mark > 100:
        print(mark, "is invalid")
        continue

    if mark >= 97:
        print(mark, "A+")
    elif mark >= 93:
        print(mark, "A")
    elif mark >= 90:
        print(mark, "A-")
    elif mark >= 87:
        print(mark, "B+")
    elif mark >= 83:
        print(mark, "B")
    elif mark >= 80:
        print(mark, "B-")
    elif mark >= 77:
        print(mark, "C+")
    elif mark >= 73:
        print(mark, "C")
    elif mark >= 70:
        print(mark, "C-")
    elif mark >= 67:
        print(mark, "D+")
    elif mark >= 60:
        print(mark, "D")
    else:
        print(mark, "F")