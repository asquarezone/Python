"""
Project euler 2: Even Fibonacci Numbers
"""
from euler.math.basic import is_even


def solve(max=100):
    x = 1
    y = 2
    sum = 2
    while x + y < max:
        z = x + y
        if is_even(z):
            sum += z
        x = y
        y = z
    return sum
        