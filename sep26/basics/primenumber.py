number = int(input("Enter any number: "))
is_prime_number = True
index = 2
while index < number:
    if number % index == 0:
        is_prime_number = False
        # After this no need to be in while loop
        break
    index = index + 1
if is_prime_number:
    print("Prime")
else:
    print("Not Prime")