import json
import uuid
from pathlib import Path

FILE = Path("tasks.json")


def load_tasks() -> dict:
    """Loads tasks from the JSON file.

    Returns:
        dict: A dictionary containing the list of tasks. If the file does not
        exist, returns a default structure with an empty task list.
    """
    if not FILE.exists():
        return {
            "tasks": []
        }

    with open(FILE, 'r', encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks: dict) -> None:
    """Saves tasks to the JSON file.

    Args:
        tasks (dict): The task data to be written to the file.
    """
    with open(FILE, 'w', encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(task: str) -> str:
    """Adds a new task to the todo list file.

    Args:
        task (str): The task description to be added.

    Returns:
        str: The ID of the newly added task.
    """
    tasks = load_tasks()
    task_id = str(uuid.uuid4())
    completed = False

    tasks["tasks"].append(
        {
            "id": task_id,
            "task": task,
            "completed": completed
        }
    )
    save_tasks(tasks)
    return task_id


def list_tasks() -> None:
    """Lists all tasks in the task list.

    Prints:
        Displays each task with its completion status.
    """
    tasks = load_tasks()
    print("Task List:")
    for task in tasks["tasks"]:
        status = "✓" if task["completed"] else "○"
        print(f"{status} {task['task']}")


def complete_task(task_id: str) -> None:
    """Marks a task as completed.

    Args:
        task_id (str): The ID of the task to mark as completed.
    """
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(tasks)


def remove_task(task_id: str) -> None:
    """Removes a task from the task list.

    Args:
        task_id (str): The ID of the task to remove.
    """
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            tasks["tasks"].remove(task)
            break
    save_tasks(tasks)