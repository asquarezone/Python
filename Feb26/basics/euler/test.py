a = 1
b = 2
print(a, end=",")
print(b, end=",")
max = 100
while True:
    if a + b > 100:
        break
    c = a + b
    print(c, end=",")
    
    a = b
    b = c
