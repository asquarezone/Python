"""Sum of even Fibonacci numbers below a specified limit.

This module generates a Fibonacci sequence up to a given limit using the
`fibonacci_sequence` function and calculates the sum of all even numbers
in that sequence using the `is_even` function.

Example:
    $ python main.py
"""

from math_utils import fibonacci_sequence, is_even

sequence = fibonacci_sequence(
    first=1,
    second=2,
    limit=4000000)
result = 0
for number in sequence:
    if is_even(number):
        result += number
print(result)
