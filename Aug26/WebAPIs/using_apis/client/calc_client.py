import requests

def create_request(operation="add", a=0, b=0):
    response = requests.get(f"http://localhost:8000/{operation}?a={a}&b={b}")
    if response.status_code == 200:
        return response.json()



if __name__ == "__main__":
    while True:
        operation = input("Operation: ")
        a = int(input("A: "))
        b = int(input("B: "))
        print(create_request(operation, a, b))
        choice = input("Do you want to continue? Enter y for yes anything else to quit")
        if choice != "y":
            break

        
        
