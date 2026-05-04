def is_even(n: int) -> bool:
    result = n%2
    if result == 0:
        return True
    return False

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_numeric_pallendrome(n: int) -> bool:
    
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    s = str(n)
    return s == s[::-1]