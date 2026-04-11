"""
This module deals with Task functionality in todo list
"""
from utils import logger, timer

FILE_NAME = "todo.txt"

@timer
#@logger
def add_task(task: str) -> None:
    """Adds a new task to the todo list file.

    Args:
        task (str): The task description to be added.

    Returns:
        None
    """
    with open(FILE_NAME, 'a', encoding="utf-8") as todolist:
        todolist.write(task + "\n")
    print("Task added")

@timer
#@logger
def list_tasks() -> None:
    """Lists all tasks stored in the todo list file.

    Reads tasks from the file and prints them with their index.

    Returns:
        None
    """
    with open(FILE_NAME, 'r', encoding="utf-8") as todolist:
        tasks = todolist.readlines()

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

@timer
def remove_task(index: int) -> None:
    """Removes a task from the todo list based on its index.

    Args:
        index (int): The 1-based index of the task to remove.

    Returns:
        None
    """
    with open(FILE_NAME, 'r', encoding="utf-8") as todolist:
        tasks = todolist.readlines()
    
    #todo: ensure index is valid
    removed = tasks.pop(index - 1)

    with open(FILE_NAME, 'w', encoding="utf-8") as todolist:
        todolist.writelines(tasks)
    
    print(f"Removed {removed.strip()}")