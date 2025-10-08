"""Calculate the sum of all numbers below a maximum that are multiples of 3 or 5.

This module demonstrates a simple program that iterates through numbers
from 1 up to a specified maximum and sums those that are multiples
of 3 or 5 using the `is_multiple_of` utility function.
"""

from math_utils import is_multiple_of

MAX = 1000
result = 0
for number in range(1,MAX):
    if is_multiple_of(number,3) or is_multiple_of(number,5):
        result += number

print(result)
