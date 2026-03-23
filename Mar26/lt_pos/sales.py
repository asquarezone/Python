"""This module will have functions for sales and billing
"""
from inventory import get_item

CART: dict = {}

def add_item_to_cart(item_id:int, quantity:int) -> None:
    """Adds the items to the cart

    Args:
        item_id (int): item_id
        quantity (int): quantity
    """
    # todo: Add items to the cart only if quantity is less than or equal to 
    # what is available in inventory
    CART[item_id] = quantity

def remove_item_from_cart(item_id:int) -> None:
    """
    Removes the items from cart

    Args:
        item_id (int): item_id
    """
    del CART[item_id]

def generate_bill() -> int|float:
    total_amt = 0
    for item_id, quantity in CART.items():
        item = get_item(item_id)
        total_amt += item['price'] * quantity
    return total_amt

def finish_transaction():
    CART.clear()
