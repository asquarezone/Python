a = 1
b = 2
print(a, end=",")
print(b, end=",")
max = 100
while True:
    c = a + b
    print(c, end=",")
    if c > 100:
        break
    a = b
    b = c

