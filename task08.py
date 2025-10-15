import json

with open("students.json", "r") as f:
    students = json.loads(f.read())

top_student = max(students, key=lambda r: r["age"])
print(f"Eng katta yoshli talaba: {top_student['name']} - {top_student['age']} yosh")


with open("top_student.json", "w") as f:
    f.write(json.dumps(top_student, indent=4))