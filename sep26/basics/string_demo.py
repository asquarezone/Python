def main():
    text = input("Enter text: ")
    print(f"Characters Count: {len(text)}")
    vowels = 'aeiou'
    # count = 0

    # for char in text:
    #     if char in vowels:
    #         count += 1
    count = sum(char.lower() in "aeiou" for char in text)
    
    print(f"Vowels: {count}")
    # count = 0
    # for char in text:
    #     if char.isdigit():
    #         count += 1
    count = sum(char.isdigit()  for char in text)
    print(f"Digits: {count}")

if __name__ == "__main__":
    main()