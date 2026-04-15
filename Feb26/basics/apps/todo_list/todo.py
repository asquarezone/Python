"""
This module will be entry point for todo list cli
"""

import sys
import task
from utils import logger, timer
import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command line to-do list manager"
    )
    sub_parser = parser.add_subparsers(
        dest="action",
        help="action to be performed",
        description="This is supported operations on todo list"

    )

    add_parser = sub_parser.add_parser("add", help="add a new task")
    add_parser.add_argument(
        "-i", "--item",
        type=str,
        help="todo item",
        required=True
    )

    remove_parser = sub_parser.add_parser("remove", help="remove an existing task") 
    remove_parser.add_argument(
        "-i", "--index",
        type=int,
        help="index of todo item",
        required=True
    )

    list_parser = sub_parser.add_parser("list", help="list all tasks")
    list_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="enable verbose mode"
    )

    # export_parser = sub_parser.add_parser("export", help="export tasks")
    # export_parser.add_argument(
    #     "-f", "--file-name",
    #     type=str,
    #     help="export file name",
    #     required=True
    # )

    # parser.add_argument("action", choices=["add", "list", "remove"],help="action to be performed")
    # parser.add_argument("-i", "--item", help="todo item")
    # parser.add_argument("--index", help="index of todo item", type=int)
    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    print(args)
    if args.action == "add":
        task.add_task(args.item)
    elif args.action == "list":
        task.list_tasks()
    elif args.action == "remove":
        task.remove_task(args.index)
    