"""This module will have accounts
"""


class BankAccount:
    """Represents a bank account with basic transaction capabilities.

    Stores account holder information and supports deposits, withdrawals,
    and transfers between accounts.

    Attributes:
        account_id (str): Unique identifier for the bank account.
        name (str): Full name of the account holder.
        mobile_no (str): Mobile number of the account holder.
        email_id (str): Email address of the account holder.
        balance (float): Current account balance in USD.
        intrest_rate (float): Interest rate applied to the account. Defaults to 0.
    """

    def __init__(
            self,
            account_id: str,
            name: str,
            mobile_no: str,
            email_id: str,
            balance: float):
        self.account_id = account_id
        self.name = name
        self.mobile_no = mobile_no
        self.email_id = email_id
        self.balance = balance
        self.intrest_rate = 0

    def withdraw(self, amount: float) -> bool:
        """Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must not exceed current balance.

        Returns:
            bool: True if the withdrawal was successful, False if balance is insufficient.
        """
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

    def deposit(self, amount: float) -> None:
        """Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit into the account balance.
        """
        self.balance += amount

    def transfer(self, account, amount: float) -> bool:
        """Transfers a specified amount from this account to another account.

        Withdraws from the current account and deposits into the target account.
        The transfer only proceeds if sufficient funds are available.

        Args:
            account (BankAccount): The recipient account to transfer funds into.
            amount (float): The amount to transfer.

        Returns:
            bool: True if the transfer was successful, False if balance is insufficient.
        """
        if self.withdraw(amount):
            account.deposit(amount)
            return True
        return False


# Lets create a savings bank Account

class SavingsAccount(BankAccount):
    """A savings account with a default interest rate, extending BankAccount.

    Inherits all transaction capabilities from BankAccount and initializes
    with a configurable interest rate.

    Attributes:
        intrest_rate (int): Annual interest rate as a percentage. Defaults to 4.

    Example:
        >>> acc = SavingsAccount("SAV-001", "Alice", "9999999999", "alice@mail.com", 1000.0)
        >>> acc.intrest_rate
        4
    """

    def __init__(
        self,
        account_id,
        name,
        mobile_no,
        email_id,
        balance,
        intrest_rate=4
    ):
        """Initializes SavingsAccount with account details and an interest rate.

        Sets the interest rate before delegating remaining initialization
        to the parent BankAccount class.

        Args:
            account_id (str): Unique identifier for the savings account.
            name (str): Full name of the account holder.
            mobile_no (str): Mobile number of the account holder.
            email_id (str): Email address of the account holder.
            balance (float): Initial account balance.
            intrest_rate (int, optional): Annual interest rate as a percentage. Defaults to 4.
        """
        self.intrest_rate = intrest_rate
        super().__init__(account_id, name, mobile_no, email_id, balance)


class CurrentAccount(BankAccount):
    """A current account with no additional attributes or behavior.

    Inherits all transaction capabilities and attributes directly from
    BankAccount. Intended for use cases where no interest rate or
    additional features are required.

    Example:
        >>> acc = CurrentAccount("CUR-001", "Bob", "8888888888", "bob@mail.com", 5000.0)
        >>> acc.deposit(1000.0)
        >>> acc.balance
        6000.0
    """
