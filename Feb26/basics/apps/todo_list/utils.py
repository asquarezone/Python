"""This module will have reusable functions
"""

def logger(func, *args, **kwargs):
    """This is a decorator to log function calls"""
    def inner(*args, **kwargs):
        print(f"Before function {func.__name__}")
        func(*args, **kwargs)
        print(f"After function {func.__name__}")
    return inner

def timer(func, *args, **kwargs):
    """This is a decorator to measure time taken by function to execute"""
    import time
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken {end-start}")
    return inner

    