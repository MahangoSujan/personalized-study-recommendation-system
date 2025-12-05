import pandas as pd

data = pd.read_csv("dataset/students.csv")

print("Student Dataset:\n")
print(data)



print("\nOnly Student Names:")
print(data["name"])

print("\nOnly Student Marks:")
print(data["marks"])

print("\nOnly Student Interest:")
print(data["interest"])



print("\nBasic Recommendation Logic:")

for index, row in data.iterrows():
    if row["marks"] >= 80:
        print(row["name"], "=> Recommended: Advanced Studies")
    else:
        print(row["name"], "=> Recommended: Basic Studies")

