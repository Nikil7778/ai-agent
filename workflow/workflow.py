import json
from datetime import datetime

print("=== RULE-BASED WORKFLOW ===")

with open("data/tasks.json", "r") as file:
    tasks = json.load(file)

date_input = input("Show tasks due before (YYYY-MM-DD): ")

target_date = datetime.strptime(date_input, "%Y-%m-%d")

print("\nRules:")
print("1. Read private task data")
print("2. Compare due dates")
print("3. Select tasks before the given date")

print("\nResult:")

found = False

for task in tasks:

    due_date = datetime.strptime(
        task["due_date"],
        "%Y-%m-%d"
    )

    if due_date < target_date:
        print(
            task["task"],
            "-",
            task["due_date"],
            "-",
            task["status"]
        )
        found = True

if not found:
    print("No tasks found.")