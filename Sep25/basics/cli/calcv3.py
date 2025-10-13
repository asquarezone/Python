"""Simple command-line calculator using argparse.

This module provides a basic command-line interface (CLI) calculator that
supports arithmetic operations like addition, subtraction, multiplication,
division, and modulus. Currently, only addition is implemented.
"""

import argparse
from argparse import Namespace


def main(args: Namespace) -> None:
    """Executes the calculator operation based on parsed command-line arguments.

    Args:
        args (Namespace): Parsed arguments containing the operation type and
            two integer operands. Expected attributes are:
                operation (str): The arithmetic operation to perform.
                number1 (int): The first operand.
                number2 (int): The second operand.

    Returns:
        None: Prints the result directly to standard output.

    Raises:
        NotImplementedError: If the operation is not yet supported.
    """
    if args.operation == "add":
        result = args.number1 + args.number2
        print(result)


if __name__ == "__main__":
    # create argument parser
    parser = argparse.ArgumentParser(
        "calcv3",
        description="This is a basic calculator CLI that performs arithmetic operations."
    )
    parser.add_argument(
        "operation",
        choices=["add", "sub", "div", "mod", "mul"],
        help="Arithmetic operation to perform."
    )
    parser.add_argument("-a","--number1", type=int)
    parser.add_argument("-b","--number2", type=int)
    args = parser.parse_args()
    main(args)
