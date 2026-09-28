import pandas as pd

data = pd.read_csv("students.csv")

print("Student Data:")
print(data)

print("\nAverage Marks:")
print(data["Marks"].mean())

print("\nHighest Marks:")
print(data["Marks"].max())

print("\nLowest Marks:")
print(data["Marks"].min())