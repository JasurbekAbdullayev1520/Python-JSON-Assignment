import json
with open("students.json", "r") as f:
    r = json.loads(f.read())

    print(r)