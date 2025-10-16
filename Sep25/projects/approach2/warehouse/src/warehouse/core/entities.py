"""This module will have entities defined used for the package
"""

from dataclasses import dataclass


@dataclass
class Product:
    """Represents a generic product.

    Attributes:
        id: A unique identifier for the product.
        name: The name of the product.
        price: The selling price of the product.
    """
    id: str
    name: str
    price: float


@dataclass
class WarehouseItem(Product):
    """Represents an item stored in a warehouse.

    Inherits attributes from :class:`Product` and adds inventory information.

    Attributes:
        quantity: The current stock quantity of the item in the warehouse.
    """
    quantity: int
