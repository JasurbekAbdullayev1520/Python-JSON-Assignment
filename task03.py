import json
with open("students.json", "r") as f:
    lines = json.loads(f.read())

with open("students.json", 'w') as jsonfile:
    jsonfile.write(json.dumps(lines, indent=4))

