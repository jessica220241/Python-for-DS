students = [
    {"name": "Amina", "major": "AMDS"},
    {"name": "Maya", "major": "Economics"},
    {"name": "Disha", "major": "AMDS"},
    {"name": "Nora", "major": "Public Health"},
    {"name": "Lina", "major": "Economics"}
]

groups = {}

for student in students:
    major = student["major"]
    name = student["name"]

    if major not in groups:
        groups[major] = []

    groups[major].append(name)

counts = {}

for major in groups:
    counts[major] = len(groups[major])

print("Groups:", groups)
print("Counts:", counts)