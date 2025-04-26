"""This module contains utility functions

The function which we have in this are
   is_even
   is_prime
"""

def is_even(number):
    """This function checks if the number is even or not

    Args:
       number(int): number to be checked
    
    Returns (bool): True if even false otherwise   
    """
    result = number % 2 == 0
    return result


def is_odd(number):
    result = number % 2 == 1
    return result

print(__name__)
