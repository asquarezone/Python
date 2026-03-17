"""This module will have necessary functions to handle inventory
"""

# ITEMS: list[dict[str, object]] = []
ITEMS: list[dict] = []


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

def delete_item(item_id:int) -> bool:
    """Delete item from inventory

    Args:
        item_id (int): item id

    Returns:
        bool: True if deleted False otherwise
    """
    pass
