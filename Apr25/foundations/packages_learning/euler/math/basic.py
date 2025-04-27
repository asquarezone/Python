"""This module contains basic math functions

"""

def is_even(number):
    """This function checks if the number is even or not

    Args:
       number(int): number to be checked

    Returns (bool): True if even false otherwise
    """
    return number % 2 == 0

def is_odd(number):
    """Checks if the number is odd or not

    Args:
        number (int): number to be checked

    Returns:
        bool: True if odd, false otherwise
    """
    return number % 2 == 1