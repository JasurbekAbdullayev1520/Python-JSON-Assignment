import json


with open("students.json", "r") as f:
    students = json.loads(f.read())

older_students = [s for s in students if s["age"] > 20]

print("20 yoshdan katta talabalar:")
for s in older_students:
    print(f"{s['name']} - {s['age']} yosh")

with open("students_over20.json", "w") as f:
    f.write(json.dumps(older_students, indent=4))