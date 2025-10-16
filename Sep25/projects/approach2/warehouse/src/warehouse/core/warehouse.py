"""
Core business logic and domain model for the warehouse management system.

This module defines the central `WareHouse` class responsible for inventory
management, including procuring, selling, and searching for items.
It depends on the entity definitions from `warehouse.core.entities`.
"""
from warehouse.core.entities import WarehouseItem


class WareHouse:
    """Manages the inventory and operations of a physical warehouse.

    This class provides methods for adding, removing, and finding items
    based on their unique identifiers or names.

    Attributes:
        wid: A unique identifier for the warehouse.
        name: The human-readable name of the warehouse.
        location: The physical address or location of the warehouse.
        items: A dictionary mapping product IDs (str) to :class:`WarehouseItem` objects
               currently in stock.
    """

    def __init__(self, wid: str, name: str, location: str):
        """Initializes a new WareHouse instance.

        Args:
            wid: A unique identifier for the warehouse (e.g., 'WH-001').
            name: The human-readable name of the warehouse (e.g., 'Central Depot').
            location: The physical address or location of the warehouse.
        """
        self.wid = wid
        self.name = name
        self.location = location
        self.items: dict[str, WarehouseItem] = {}

    def add_new_item(self, item_id: str, name: str, price: float, quantity: int):
        """Creates and registers a brand new item in the warehouse inventory.

        This method should only be used for items that are not yet tracked.

        Args:
            item_id: The unique identifier for the new product.
            name: The name of the new product.
            price: The selling price of the new product.
            quantity: The initial stock quantity of the new product.

        Raises:
            KeyError: If an item with the given `item_id` already exists in the inventory.
        """
        if item_id in self.items:
            # throw error
            print(f"item with {item_id} already exists")
        else:
            self.items[item_id] = WarehouseItem(
                id=item_id,
                name=name,
                price=price,
                quantity=quantity
            )

    def procure_item(self, item_id: str, quantity: int):
        """Increases the stock quantity of an existing item in the inventory.

        This method is used when purchasing or receiving stock. For adding
        a completely new product, use :meth:`add_new_item`.

        Args:
            item_id: The ID of the existing item to increase stock for.
            quantity: The amount to add to the current stock.

        Raises:
            KeyError: If the `item_id` is not found in the inventory.
            ValueError: If the `quantity` is less than or equal to zero.
        """
        if item_id in self.items:
            self.items[item_id].quantity += quantity
        else:
            print(f"item with {item_id} does not exist")

    def sell_item(self, item_id: str, quantity: int):
        """Reduces the stock of a specified item.

        Raises:
            ValueError: If the `item_id` is not found or if the requested
                        `quantity` is greater than the available stock.

        Args:
            item_id: The ID of the item to be sold.
            quantity: The amount to subtract from the stock.
        """
        if item_id in self.items:
            self.items[item_id].quantity -= quantity
        else:
            print(f"item with {item_id} does not exist")

    def find_item_by_id(self, item_id: str) -> WarehouseItem | None:
        """Retrieves an item from the inventory using its unique ID.

        Args:
            item_id: The unique identifier of the item to find.

        Returns:
            The matching :class:`WarehouseItem` object, or None if the item is not found.
        """
        pass

    def find_item_by_name(self, name: str) -> list[WarehouseItem]:
        """Finds items in the inventory that match the given name.

        This method supports partial or case-insensitive matching.

        Args:
            name: The name or partial name of the item to search for.

        Returns:
            A list of matching :class:`WarehouseItem` objects. Returns an empty list
            if no matches are found.
        """
        pass