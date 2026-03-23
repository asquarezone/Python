"""
This module is an entrypoint for the lt_pos Application
"""
from inventory import (
    print_sales_menu, 
    print_inventory_menu,
    add_item,
    delete_item,
    update_item,
    search_item_by_name
)

from sales import (
    add_item_to_cart, 
    remove_item_from_cart, 
    finish_transaction, 
    generate_bill
)

def inventory_menu() -> None:
    """Inventory menu
    """
    while True:
        print_inventory_menu()
        name = input("Enter name: ")
        description = input("Enter description: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        add_item(name, description, price, quantity)
        choice = input("Do you want to continue adding items. Enter Y for yes and N for no: ")
        if choice.lower() == 'n':
            print_inventory_menu()
            break



def sale_menu() -> None:
    """Sales menu
    """
    while True:
        print_sales_menu()
        item_id = int(input("Enter the item_id: "))
        quantity = int(input("Enter number of items: "))
        add_item_to_cart(item_id, quantity)
        choice = input("Do you want to continue adding items. Enter Y for yes and N for no: ")
        if choice.lower() == 'n':
            total_amount = generate_bill()
            print(f"Your bill is {total_amount}")
            input("Enter to confirm payment. ")
            finish_transaction()
            break
        


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
                sale_menu()
            elif option == "2":
                print("You have selected Inventory")
                inventory_menu()
            elif option == "3":
                print("Goodbye")
                break
            else:
                print("Invalid option")
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_menu()
