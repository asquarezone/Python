"""Calculator with basic operations.

This module provides simple arithmetic functions such as addition,
subtraction, and multiplication. Each function accepts two integers
and returns an integer result.
"""

def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of `a` and `b`.
    """
    return a + b


def sub(a: int, b: int) -> int:
    """Subtract one integer from another.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The result of `a - b`.
    """
    return a - b


def mul(a: int, b: int) -> int:
    """Multiply two integers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of `a` and `b`.
    """
    return a * b

# result = add(5,6)
# print(result)
