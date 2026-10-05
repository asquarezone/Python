if __name__ == "__main__":
    number = int(input("Enter your number: "))
    reverse = 0
    while number > 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = number // 10
    print(reverse)
