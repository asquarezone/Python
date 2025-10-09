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
        limit (int, optional): The upper bound for numbers in the sequence. Defaults to 10.

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


def factors(number: int) -> list[int]:
    """Return a list of factors for the given number.

    This function computes all the factors of the specified integer,
    excluding 1 and the number itself.

    Args:
        number (int): The integer whose factors are to be found.

    Returns:
        list[int]: A list containing all factors of the given number.
    """
    result = []
    for index in range(2, number):
        if number % index == 0:
            result.append(index)
    return result


def is_prime(number) -> bool:
    """Check if a number is a prime number.

    This function determines whether the given number has any factors
    other than 1 and itself by using the `factors` function.

    Args:
        number (int): The integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    result = True
    for index in range(2, number):
        if number % index == 0:
            result = False
            break
    return result

def prime_factors(number) -> bool:
    """Return all prime factors of a given number.

    This function finds all the factors of the specified number
    and filters them to include only the prime ones.

    Args:
        number (int): The integer whose prime factors are to be found.

    Returns:
        list[int]: A list containing all prime factors of the given number.
    """
    factors_number = factors(number)
    result = []
    for factor in factors_number:
        if is_prime(factor):
            result.append(factor)
    return result
