from utils import is_prime

if __name__ == "__main__":
    # get the number from user
    number = int(input("Enter any number: "))
    if is_prime(number):
        print("Prime Number")
    else:
        print("Not a Prime Number")
   