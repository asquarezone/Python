# LT_POS – Simple Point of Sale (POS)

## Overview

**LT_POS** is a very basic **Point of Sale (POS)** project created for learning fundamental Python programming concepts.

The goal of this project is **not to build a production POS**, but to practice core programming constructs such as:

* Data Types
* Loops
* Conditional Statements
* Functions
* List Comprehensions
* Dictionary Comprehensions

The system runs entirely in memory and **does not store any data permanently**.

---

## Features

### 1. Sale

Allows a user to simulate selling products.

Typical flow:

1. Display available products
2. Select a product
3. Enter quantity
4. Calculate total price
5. Show bill summary

Example output:

```
Available Products
1. Milk - ₹50
2. Bread - ₹40
3. Eggs - ₹6

Select product: 1
Enter quantity: 2

Total = ₹100
```

---

### 2. Inventory

Displays available products and their details.

Example:

```
Product Inventory

Milk   - Price: ₹50
Bread  - Price: ₹40
Eggs   - Price: ₹6
```

Inventory will be stored using **Python dictionaries**.

Example structure:

```python
inventory = {
    "milk": 50,
    "bread": 40,
    "eggs": 6
}
```

---

## Learning Objectives

This project demonstrates the following Python concepts:

### Data Types

* `int`
* `float`
* `str`
* `list`
* `dict`

---

### Loops

Used for:

* Iterating through inventory
* Displaying product lists
* Handling repeated menu operations

Example:

```python
for item in inventory:
    print(item)
```

---

### Conditional Statements

Used to control program flow.

Example:

```python
if option == "sale":
    process_sale()
elif option == "inventory":
    show_inventory()
else:
    print("Invalid option")
```

---

### Functions

Functions will be used to organize the program.

Example functions:

```
show_menu()
show_inventory()
process_sale()
calculate_total()
```

Example:

```python
def show_inventory():
    for item, price in inventory.items():
        print(item, price)
```

---

### List Comprehensions

Used for creating lists efficiently.

Example:

```python
product_names = [item for item in inventory]
```

---

### Dictionary Comprehensions

Used to transform dictionaries.

Example:

```python
discount_prices = {item: price * 0.9 for item, price in inventory.items()}
```

---

## Project Structure

```
lt_pos/
│
├── main.py
├── inventory.py
├── sale.py
└── README.md
```

---

## Running the Project

1. Clone the repository

```bash
git clone https://github.com/asquarezone/Python.git
```

2. Navigate to the project

```bash
cd Mar26/lt_pos
```

3. Run the program

```bash
python main.py
```

---

## Example Menu

```
===== LT POS =====

1. Sale
2. Inventory
3. Exit

Select an option:
```

---

## Limitations

This project intentionally keeps things simple:

* No database
* No file storage
* No authentication
* No GUI
* Runs only in terminal

---

## Future Improvements

Possible upgrades:

* File storage using JSON
* SQLite database
* Barcode scanning
* Receipt generation
* Web or GUI interface

---

## Purpose of the Project

This project is designed for **beginners learning Python**, especially to understand how multiple programming concepts work together in a small real-world style application.

---

## Author

Khaja
