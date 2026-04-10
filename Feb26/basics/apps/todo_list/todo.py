"""
This module will be entry point for todo list cli
"""

import sys
import task


def print_usage():
    """Prints the usage instructions for the todo CLI application.

    Displays available commands and examples, then exits the program
    with a non-zero status code.

    Returns:
        None
    """
    print("Usage: python todo.py [add|list|remove]", end="\n\n\n")
    print("Examples")
    print("python todo.py add 'task description'")
    print('python todo.py remove task-index')
    print('python todo.py list')
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    command = sys.argv[1]

    if command == "add":
        task.add_task(sys.argv[2])
    elif command == "list":
        task.list_tasks()
    elif command == "remove":
        task.remove_task(int(sys.argv[2]))
    else:
        print_usage()
