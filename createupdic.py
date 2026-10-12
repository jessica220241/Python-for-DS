student={"name": "Amina", "age": 20, "score": 78}
student["score"]= 85
student["major"]= "AMDS"
removed_age= student.pop("age")
print("updated student: ", student)
print("removed age: ", removed_age)