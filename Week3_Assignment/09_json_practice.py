import json

students = [
    {
        "name": "Laxmi",
        "age": 19,
        "marks": 85
    },
    {
        "name": "Anu",
        "age": 20,
        "marks": 90
    },
    {
        "name": "Sita",
        "age": 19,
        "marks": 78
    }
]

# Create JSON file
with open("practice_students.json", "w") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully!")

# Read JSON file
with open("practice_students.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")

for student in data:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])
    print("--------------------")