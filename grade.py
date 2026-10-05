while True:
    marks = input("Enter your marks: ")

    if marks.isdigit():
        marks = int(marks)
        break
    else:
        print("Please enter an integer.")
        continue

if marks >= 97 and marks<=100:
    print("A+")
elif marks >= 93:
    print("A")
elif marks >= 90:
    print("A-")
elif marks >= 87:
    print("B+")
elif marks >= 83:
    print("B")
elif marks >= 80:
    print("B-")
elif marks >= 77:
    print("C+")
elif marks >= 73:
    print("C")
elif marks >= 70:
    print("C-")
elif marks >= 67:
    print("D+")
elif marks >= 60:
    print("D")
else:
    print("F")