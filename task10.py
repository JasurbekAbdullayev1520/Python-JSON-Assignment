import json

with open("students.json", "r") as f:
    students = json.loads(f.read())


sorted_students = sorted(students, key=lambda r: r["age"])

print("Yosh bo`yicha tartiblangan talabalar:")
for i in sorted_students:
    print(f"{i['name']} - {i['age']} yosh")

with open("students_sorted.json", "w") as f:
    f.write(json.dumps(sorted_students, indent=4))