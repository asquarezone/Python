"""Entry point for the application.

This module serves as the main entry point of the program. It initializes
core components, coordinates high-level application flow, and triggers
execution of the primary logic.

Typical usage example:
    $ python main.py
"""

from math_utils import factors, prime_factors


if __name__ == '__main__':
    result = factors(100)
    print(result)
    result = prime_factors(100)
    print(result)
