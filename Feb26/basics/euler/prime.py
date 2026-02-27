number = 7
is_prime = True
index = 1
while index < number:
    if number % index == 0:
        is_prime = False
    index += 1

if is_prime:
    print("prime number")
else:
    print("not a prime number")
