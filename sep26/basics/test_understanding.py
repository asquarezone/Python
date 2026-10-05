def add(a,b):
    return a + b


if __name__ == "__main__":
    result = add(5,3)
    print(result)

    options = {
        'a': 5,
        'b': 3
    }
    result = add(**options)
    print(result)