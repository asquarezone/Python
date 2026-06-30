class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def transfer(self, target, amount):
        self.balance -= amount
        target.balance += amount

ram_account = BankAccount(12345, 50000)
shyam_account = BankAccount(23456, 0)

ram_account.transfer(shyam_account, 10000)