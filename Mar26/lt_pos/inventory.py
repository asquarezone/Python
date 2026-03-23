"""This module will have necessary functions to handle inventory
"""

# ITEMS: list[dict[str, object]] = []
ITEMS: list[dict] = [
    {
        "id": 1,
        "name": "HP Wireless Mouse",
        "description": "Ergonomic wireless mouse with USB receiver",
        "price": 799.0,
        "quantity": 500
    },
    {
        "id": 2,
        "name": "HP Keyboard",
        "description": "Full-size wired keyboard with numeric keypad",
        "price": 1199,
        "quantity": 300
    }
]


def add_item(
        name: str,
        description: str,
        price: int | float,
        quantity: int) -> bool:
    """Adds item to the inventory

    Args:
        name (str): name of product
        description (str): description
        price (int | float): price
        quantity (int): quantity

    Returns:
        bool: Returns True when all values are valid False otherwise
    """
    # validate
    # Todo: As of now we are sending only True or False but not the reason
    #       when values are invalid. This needs to be fixed
    if price < 1 and quantity < 1:
        return False

    unique_id = len(ITEMS) + 1
    ITEMS.append({
        "id": unique_id,
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity
    })
    return True

def get_item(item_id:int) -> dict|None:
    """Get item

    Args:
        item_id (int): item item Id

    Returns:
        dict: _description_
    """
    index = find_item(item_id)
    if index is None:
        return None
    return ITEMS[index]


def find_item(item_id:int) -> int|None:
    """This method will find item id in list

    Args:
        item_id (int): item_id to be found

    Returns:
        dict|None: Returns index if found None Otherwise
    """
    index = None
    for id, item in enumerate(ITEMS):
        if item['id'] == item_id:
            index = id
            break
    return index

def delete_item(item_id:int) -> bool:
    """Delete item from inventory

    Args:
        item_id (int): item id

    Returns:
        bool: True if deleted False otherwise
    """
    index = find_item(item_id)
    if index == None:
        return False
    del ITEMS[index]
    return True

def update_item(
        item_id:int,
        name: str,
        description: str,
        price: int | float,
        quantity: int) -> bool:
    """Updates item to the inventory

    Args:
        item_id(int): id of the product
        name (str): name of product
        description (str): description
        price (int | float): price
        quantity (int): quantity

    Returns:
        bool: Returns True when all values are valid False otherwise
    """
    if price < 1 and quantity < 1:
        return False
    index = find_item(item_id)
    if index == None:
        return False
        
    ITEMS[index] = {
        "id": item_id,
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity
    }

def search_item_by_name(name: str) -> list[dict]:
    """This method is used to search items by name

    Args:
        name (str): name of the product

    Returns:
        list[dict] | None: items found
    """
    results = []
    for item in ITEMS:
        if name.lower() in item['name'].lower():
            results.append(item)
    return results

def print_inventory_menu():
    """This method will print all the items with its item id and item details
    """
    print("id\tname\tprice\tquantity")
    for item in ITEMS:
        print(f"{item['id']}\t{item['name']}\t{item['price']}\t{item['quantity']}")

def print_sales_menu():
    """This method will print all the items with its item id and item details
    """
    print("id\tname\tprice")
    for item in ITEMS:
        print(f"{item['id']}\t{item['name']}\t{item['price']}")
