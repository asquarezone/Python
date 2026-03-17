"""
This module is an entrypoint for the lt_pos Application
"""

def main_menu() -> None:
    """This function will display menu to the user
    
    return: None
    """
    while True:
        print("===== LT POS =====", end="\n\n")
        print("1. Sale")
        print("2. Inventory")
        print("3. Exit", end="\n\n")
        option = input("Select an option ")
        if option.isnumeric():
            if option == "1":
                print("You have selected Sale")
            elif option == "2":
                print("You have selected Inventory")
            elif option == "3":
                print("Goodbye")
                break
            else:
                print("Invalid option")
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_menu()
