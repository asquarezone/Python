"""
This module serves as the entry point for the todo list CLI.
"""

import sys
import argparse
import task_structured
from utils import logger, timer


def build_parser() -> argparse.ArgumentParser:
    """Builds and returns the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: Configured argument parser with subcommands.
    """
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command line to-do list manager"
    )

    sub_parser = parser.add_subparsers(
        dest="action",
        help="Action to be performed",
        description="Supported operations on the todo list"
    )

    add_parser = sub_parser.add_parser("add", help="Add a new task")
    add_parser.add_argument(
        "-i", "--item",
        type=str,
        help="Todo item description",
        required=True
    )

    remove_parser = sub_parser.add_parser("remove", help="Remove an existing task")
    remove_parser.add_argument(
        "-i", "--identifier",
        type=str,
        help="Task identifier",
        required=True
    )

    list_parser = sub_parser.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose mode"
    )

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()


    if args.action == "add":
        task_structured.add_task(args.item)
    elif args.action == "list":
        task_structured.list_tasks()
    elif args.action == "remove":
        task_structured.remove_task(args.identifier)