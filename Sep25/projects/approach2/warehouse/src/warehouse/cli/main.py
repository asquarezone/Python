from warehouse.core.warehouse import WareHouse
from warehouse.core.entities import WarehouseItem

def get_item_id() -> str:
    """Prompts the user to enter a product ID.

    Returns:
        str: The product ID entered by the user.
    """
    wid = input("Enter the product id: ")
    return wid

def get_item_quantity() -> int:
    """Prompts the user to enter the number of items (quantity).

    Returns:
        int: The quantity entered by the user.
    """
    quantity = int(input("Enter number of items: "))
    return quantity

def get_item_name() -> str:
    """Prompts the user to enter a product name.

    Returns:
        str: The product name entered by the user.
    """
    name = input("Enter the product name: ")
    return name

def get_item_details() -> tuple[str, str, float, int]:
    """Collects all necessary details for a new or existing warehouse item
    from the user: ID, name, price, and quantity.

    Returns:
        tuple: A tuple containing the item ID (str), name (str), price (float),
            and quantity (int).
    """
    wid: str = get_item_id()
    name: str = get_item_name()
    price: float = float(input("Enter the price of product: "))
    quantity: int = get_item_quantity()
    return wid,name,price,quantity

def main() -> None:
    """Main function to run the warehouse management application.

    Initializes a warehouse and runs a command-line interface loop
    to allow the user to add, procure, sell, and search for products.
    """
    print("Welcome to warehouse")
    warehouse: WareHouse = WareHouse(
        wid="w1001",
        name="Hyd warehouse 1",
        location="Ameerpet")
    while True:
        print("1. Add a new product to Warehouse")
        print("2. Procure existing products")
        print("3. Sell Products")
        print("4. Get item by id")
        print("5. Get items by name")
        print("6. quit")
        choice: str = input("Enter your choice: ")
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid entry")
        elif choice == "1":
            wid: str
            name: str
            price: float
            quantity: int
            wid, name, price, quantity = get_item_details()
            warehouse.add_new_item(item_id= wid, name=name, price=price, quantity=quantity)
        elif choice == "2":
            wid: str = get_item_id()
            quantity: int = get_item_quantity()
            warehouse.procure_item(item_id=wid, quantity=quantity)
        elif choice == "3":
            wid: str = get_item_id()
            quantity: int = get_item_quantity()
            warehouse.sell_item(item_id=wid, quantity=quantity)
        elif choice == "4":
            wid: str = get_item_id()
            item: WarehouseItem | None = warehouse.find_item_by_id(item_id=wid)
            if item:
                print(item)
            else:
                print("Item not found")
        elif choice == "5":
            name: str = get_item_name()
            # Assuming find_item_by_name returns an iterable of WarehouseItem
            for item in warehouse.find_item_by_name(name=name):
                print(item)
        elif choice == "6":
            print("Bye................")
            break

if __name__ == "__main__":
    main()