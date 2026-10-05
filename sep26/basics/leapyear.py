if __name__ == "__main__":
    year = int(input("Enter your year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is leap year")
            else:
                print(f"{year} is not leap year")
        else:
            print(f"{year} is leap year")


    else:
        print(f"{year} is not leap year")
    