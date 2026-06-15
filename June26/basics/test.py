def is_pallendrome(number):
    """Checks if the number is pallendrome or not

    Args:
        number (_type_): number

    Returns:
       True if pallendrome False otherwise
    """
    return str(number) == str(number)[::-1]

x = 99
y = 99
largest_pallendrome = 0
result_x = 0
result_y = 0
while x >= 10:
    while y >= 10:
        number = x * y
        # check if number is divisible by 11
        if is_pallendrome(number) and number > largest_pallendrome:
            largest_pallendrome = number
            result_x = x
            result_y = y
        y -= 1
    x -= 11
print(f"largest pallendrom is {largest_pallendrome} => {result_x} * {result_y}")