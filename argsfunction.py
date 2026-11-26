
def student_result(name, *marks):

    if len(marks) == 0:
        print("No marks provided")
        return None

    total = sum(marks)
    average = total / len(marks)

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    result = {
        "name": name,
        "total": total,
        "average": average,
        "status": status
    }

    return result


print(student_result("Amina", 70, 80, 75))

print(student_result("Maya", 45, 38, 51, 42))

print(student_result("Nora"))
