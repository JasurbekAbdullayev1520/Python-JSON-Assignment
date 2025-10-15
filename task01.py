import json
students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

with open('students.json', 'w') as f:
    content = json.dumps(students, indent=4)
    f.write(content)