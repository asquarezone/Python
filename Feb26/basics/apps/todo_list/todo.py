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
    parser.add_argument("action", choices=["add", "list", "remove"],help="action to be performed")
    parser.add_argument("-i", "--item", help="todo item")
    parser.add_argument("--index", help="index of todo item", type=int)
    return parser



if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    if args.action == "add":
        task.add_task(args.item)
    elif args.action == "list":
        task.list_tasks()
    elif args.action == "remove":
        task.remove_task(args.index)
    
