import requests


def get_all_products():
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code == 200:
        return response.json()


if __name__ == "__main__":
    products = get_all_products()
    for product in products:
        print("-" * 25)
        for name, value in product.items():
            print(f"{name}: {value}")
        print()