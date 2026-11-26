
import pandas as pd

# Read the Excel file
file_path = r"C:\Users\DELL\Downloads\employee_data.xlsx"

df = pd.read_excel(file_path)

# (a) Display first five rows
print("First Five Rows:")
print(df.head())

# (b) Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# (c) Replace missing Department with Unknown
df["Department"] = df["Department"].fillna("Unknown")

# (d) Replace missing numerical values with their means
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df["Experience"] = df["Experience"].fillna(
    df["Experience"].mean()
)

# (e) Create Salary_Level column
def salary_level(salary):

    if salary >= 60000:
        return "High"

    elif salary >= 40000:
        return "Medium"

    else:
        return "Low"


df["Salary_Level"] = df["Salary"].apply(salary_level)

# (f) Remove completely duplicated rows
df = df.drop_duplicates()

# Display cleaned data
print("\nCleaned Employee Data:")
print(df)

# (g) Export cleaned data to Excel
df.to_excel("cleaned_employee_data.xlsx", index=False)

print("\nCleaned data exported successfully!")
