max = 10
index = 1
sum = 0
while index < max:
    if index % 3 == 0 or index % 5 == 0:
        sum = sum + index
    index = index + 1
print(sum)