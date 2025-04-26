def is_prime(number):
    if number < 2:
        return False
    result = True
    index = 2
    while index < number:
        if number % index == 0:
            result = False
            break
        index = index + 1
    return result

# number = 100
# for index in range(2, number):
#     if number%index == 0:
#         if is_prime(index):
#             print(index)

result = is_prime(7)
print(result)

