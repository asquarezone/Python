"""This module is only for testing functions
"""
from inventory import add_item, ITEMS, update_item, delete_item

def test_delete_products():
    if len(ITEMS) == 1:
        print("Pre condition is working")
    delete_item(item_id=1)
    if len(ITEMS) == 0:
        print("delete works correctly")


def test_update_products():
    if len(ITEMS) == 1:
        print("Pre condition is working")
    update_item(
        item_id=1,
        name="Tajmahal Tea",
        description= "Tajmahal Tea", 
        price=110, 
        quantity=10
    )
    if len(ITEMS) == 1:
        print("update worked correctly")
    if ITEMS[0]['price'] == 110:
        print("update worked correctly")

def test_add_products():
    if len(ITEMS) == 0:
        print("its working correctly")
    add_item(
        name="Tajmahal Tea",
        description= "Tajmahal Tea", 
        price=100, 
        quantity=10)
    # lets verify the count
    if len(ITEMS) == 1:
        print("its working correctly")

if __name__ == "__main__":
    # lets test adding products
    test_add_products()
    test_update_products()
    test_delete_products()
    