import json
from datetime import datetime


def read_tasks():

    with open("../data/tasks.json", "r") as file:
        return json.load(file)


def find_tasks_before(date):

    tasks = read_tasks()

    target_date = datetime.strptime(
        date,
        "%Y-%m-%d"
    )

    result = []

    for task in tasks:

        due_date = datetime.strptime(
            task["due_date"],
            "%Y-%m-%d"
        )

        if due_date < target_date:
            result.append(task)

    return result


def check_task_status(task_name):

    tasks = read_tasks()

    for task in tasks:

        if task["task"].lower() == task_name.lower():
            return task["status"]

    return "Task not found"