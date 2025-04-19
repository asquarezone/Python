a = 1
b = 2
sum = 2
while a + b < 100:
    c = a + b
    if c % 2 == 0:
        sum = sum + c
    a = b
    b = c
print(sum)