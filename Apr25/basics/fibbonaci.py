a = 1
b = 2
c = 0
sum = 2
while c < 100:
    c = a + b
    if c % 2 == 0:
        sum = sum + c
    a = b
    b = c
print(sum)