def find_largest(numbers):
    largest = 0

    for number in numbers:
        if number < largest:
            largest = number
    return largest

values = [10,20,30,40,50]
result = find_largest(values)
print(result)