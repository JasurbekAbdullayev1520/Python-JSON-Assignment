import json

with open("students.json", "r") as f:
    students = json.loads(f.read())

count = len(students)
print(f"Umumiy talabalar soni: {count}")

with open("student_count.txt", "w") as f:
    f.write(f"Talabalar soni: {count}")