"""
Project euler 1: Multiples of 3 or 5
"""

def solve(max=10):
    sum = 0
    for index in range(1,max):
        if index % 3 == 0 or index % 5 == 0:
            sum += index
    return sum