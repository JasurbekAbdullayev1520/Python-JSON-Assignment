import json

with open("students.json", "r") as f:
    students = json.loads(f.read())

total_age = sum(s["age"] for s in students)
average_age = total_age / len(students)

print(f"Talabalarning o`rtacha yoshi: {average_age:.1f}")


with open("average_age.txt", "w") as f:
    f.write(f"O`rtacha yosh: {average_age:.1f}")