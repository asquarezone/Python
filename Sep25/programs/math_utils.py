"""Math utilities module.

This module provides helper functions for performing mathematical
checks and calculations.
"""

def is_multiple_of(number: int, multiple: int) -> bool:
    """Check if a number is a multiple of another.

    Args:
        number (int): The number to check.
        multiple (int): The potential multiple.

    Returns:
        bool: True if `number` is a multiple of `multiple`, otherwise False.
    """
    return number % multiple == 0


def fibonacci_sequence(first: int = 1, second: int = 2, limit: int = 10) -> list[int]:
    """Generate a Fibonacci sequence up to a given limit.

    The sequence starts with `first` and `second` values, and each subsequent
    number is the sum of the previous two. Numbers are included in the
    sequence only if they are less than `limit`.

    Args:
        first (int, optional): The first number in the sequence. Defaults to 1.
        second (int, optional): The second number in the sequence. Defaults to 2.
        limit (int, optional): The upper bound (exclusive) for numbers in the sequence. Defaults to 10.

    Returns:
        list[int]: A list containing the Fibonacci sequence up to `limit`.
    """
    sequence = [first, second]

    while first + second < limit:
        next_in_sequence = first + second
        sequence.append(next_in_sequence)
        first, second = second, next_in_sequence

    return sequence

def is_even(number: int) -> bool:
    """Check if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if `number` is even, False otherwise.
    """
    return number % 2 == 0
