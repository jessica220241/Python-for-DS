
import pandas as pd

data = {
    "Name": ["Amina", "Maya", "Lina", "Nora", "Sara"],
    "Quiz": [18, 12, 16, 9, 15],
    "Midterm": [25, 19, 28, 15, 22],
    "Final": [45, 31, 40, 25, 38]
}

# (a) Create and display DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# (b) Add Total column
df["Total"] = df["Quiz"] + df["Midterm"] + df["Final"]

# (c) Add Average column
df["Average"] = df["Total"] / 3

# (d) Add Status column
df["Status"] = df["Total"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print("\nCompleted DataFrame:")
print(df)

# (e) Display students who passed
print("\nStudents who passed:")
print(df[df["Status"] == "Pass"])

# (f) Sort by Total in descending order
df = df.sort_values(by="Total", ascending=False)

print("\nSorted DataFrame:")
print(df)

# (g) Export to Excel
df.to_excel("student_results.xlsx", index=False)

print("\nData exported successfully!")
