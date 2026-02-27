number = 151
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10  + digit
    number = number // 10

if number == reverse:
    print("pallendrome")
else:
    print("not a pallendrome")
