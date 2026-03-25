class BankAccount:
    def __init__(self, balance:float, number:str, name: str):
        self.balance = balance
        self.number = number
        self.name = name

    def withdraw(self, amount: float):
        self.balance -= amount

    def deposit(self, amount: float):
        self.balance += amount

    def transfer(self, account, amount:float):
        self.withdraw(amount)
        account.deposit(amount)


if __name__ == "__main__":
    ram_account  = BankAccount(balance=1000000, number="99999", name="RAM")
    shyam_account  = BankAccount(balance=1000, number="11111", name="SHYAM")
    print("Before donation")
    print(f"Ram's balance {ram_account.balance} Shyam's balance {shyam_account.balance}")
    ram_account.transfer(shyam_account, 10000)
    print("After donation")
    print(f"Ram's balance {ram_account.balance} Shyam's balance {shyam_account.balance}")
