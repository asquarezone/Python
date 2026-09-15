def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal = item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal, customer_type):
    discount = 0

    if customer_type == "premium":
        discount = subtotal * 0.20
    elif customer_type == "regular":
        discount = subtotal * 0.10

    return discount


def calculate_tax(amount):
    tax_rate = 0.18
    return amount * tax_rate


def generate_bill(items, customer_type):
    subtotal = calculate_subtotal(items)

    discount = calculate_discount(
        subtotal,
        customer_type
    )

    amount_after_discount = subtotal - discount

    tax = calculate_tax(subtotal)

    total = amount_after_discount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total
    }


def print_bill(customer_name, bill):
    print(f"Customer: {customer_name}")
    print(f"Subtotal: ₹{bill['subtotal']:.2f}")
    print(f"Discount: ₹{bill['discount']:.2f}")
    print(f"Tax: ₹{bill['tax']:.2f}")
    print(f"Total: ₹{bill['total']:.2f}")


def main():
    customer_name = "Khaja"
    customer_type = "premium"

    items = [
        {"name": "Laptop", "price": 50000, "quantity": 1},
        {"name": "Mouse", "price": 1000, "quantity": 2},
        {"name": "Keyboard", "price": 2000, "quantity": 1}
    ]

    bill = generate_bill(items, customer_type)

    print_bill(customer_name, bill)


if __name__ == "__main__":
    main()