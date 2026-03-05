def is_prime(number:int) -> bool:
    """Checks if the number is prime or not

    Args:
        number (int): number to be checked

    Returns:
        bool: Returns True if prime False otherwise
    """
    is_prime_result = True
    if number < 2:
        is_prime_result = False
    else:
        index = 2
        while index < number:
            if number % index == 0:
                is_prime_result = False
                break
            index += 1
    return is_prime_result