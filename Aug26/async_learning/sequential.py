import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"{func.__name__} took {elapsed_time:.4f} seconds")

        return result

    return wrapper

@measure_time
def compute_intensive(max=1000):
    """
    Perform a compute-intensive operation by finding
    all prime numbers up to max.
    """
    primes = []

    for num in range(2, max + 1):
        is_prime = True

        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

import random
from pathlib import Path


def io_intensive(max=1000):
    """
    This method does I/O intensive operations
    by randomly reading files from a directory.
    """

    files = list(Path("data").glob("*.txt"))

    if not files:
        raise FileNotFoundError("No .txt files found in data directory")

    total_bytes = 0

    for _ in range(max):
        filename = random.choice(files)

        with open(filename, "r") as file:
            data = file.read()

        total_bytes += len(data)

    return total_bytes

@measure_time
def cpu(compute_intensive):
    for attempt in range(1, 11):
        print(f"Starting compute intensive task... - {attempt}")
        result = compute_intensive(10000)
        print(f"Found {len(result)} prime numbers.- {attempt}")

        
@measure_time
def io_bound(io_intensive):
    for attempt in range(1, 11):
        print(f"Starting I/O intensive task... - {attempt}")
        result = io_intensive(1000)
        print(f"Read {result} bytes.- {attempt}")

if __name__ == "__main__":
    #cpu(compute_intensive)
    io_bound(io_intensive)

