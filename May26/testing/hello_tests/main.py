"""This module contains 
simple python functions
"""

def is_even(number: int) -> bool:
    """Checks if the number is even or not

    Args:
        number (int): number passed

    Returns:
        bool: Returns true if even false otherwise
    """

    if not isinstance(number, int):
        return False
    return number % 2 == 0


def reverse(number: int) -> int:
    """Reverses the digits

    Args:
        number (int): Number to be reversed

    Returns:
        int: returns reversed number
    """

    reverse_number = 0
    while number > 0:
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10
    return reverse_number

