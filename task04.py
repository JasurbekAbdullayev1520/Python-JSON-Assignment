import json
with open('students.json') as f:
    students = json.loads(f.read())

name = input("Ism: ")
surname = input("Familiya: ")
age = int(input("Yosh: "))
new_text = {
    "name": name,
    "surname": surname,
    "age": age
} 

students.append(new_text)

with open("students.json", "w") as f:
    f.write(json.dumps(students, indent=4))



