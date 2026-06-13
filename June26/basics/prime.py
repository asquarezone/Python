"""
This module contains is prime implementation
"""

number = int(input("Enter the number: "))
is_prime= True
index = 2
while index <= number // 2:
    if number % index == 0:
        is_prime = False
        break
    index += 1

if is_prime:
    print("prime")
else:
    print("Not Prime")