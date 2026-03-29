"""
This module demonstrates composition by modeling a simple banking system.

It defines a Card class and a BankAccount class, where a BankAccount
composes a Card object to simulate card-based payments. This illustrates
how composition allows objects to delegate behavior to other objects
rather than relying solely on inheritance.

Classes:
    Card: Represents a payment card used for swiping transactions.
    BankAccount: Represents a bank account that holds account holder
        details, manages funds, and supports card-based payments.

Example:
    >>> card = Card("1234-5678-9012-3456")
    >>> account = BankAccount("ACC-001", "Alice", "9999999999", "alice@mail.com", 1000.0, card)
    >>> account.use_card(200.0)
    Card 1234-5678-9012-3456 use for ₹ 200.0
"""


class Card:
    """Represents a payment card that can be swiped for transactions.

    Attributes:
        card_number (str): Unique identifier number of the card.

    Example:
        >>> card = Card("1234-5678-9012-3456")
        >>> card.swipe(500.0)
        Card 1234-5678-9012-3456 used for ₹ 500.0
    """

    def __init__(self, card_number: str):
        """Initializes Card with a card number.

        Args:
            card_number (str): Unique identifier number of the card.
        """
        self.card_number = card_number

    def swipe(self, amount):
        """Simulates a card swipe for a given transaction amount.

        Args:
            amount (float): The transaction amount to be charged to the card.
        """
        print(f"Card {self.card_number} use for ₹ {amount}")


class BankAccount:
    """Represents a bank account with basic transaction capabilities.

    Stores account holder information and supports deposits, withdrawals,
    transfers, and card-based payments. Composes a Card object to delegate
    card swipe behavior.

    Attributes:
        account_id (str): Unique identifier for the bank account.
        name (str): Full name of the account holder.
        mobile_no (str): Mobile number of the account holder.
        email_id (str): Email address of the account holder.
        balance (float): Current account balance.
        intrest_rate (float): Interest rate applied to the account. Defaults to 0.
        card (Card): The payment card associated with this account.

    Example:
        >>> card = Card("1234-5678-9012-3456")
        >>> account = BankAccount("ACC-001", "Alice", "9999999999", "alice@mail.com", 1000.0, card)
        >>> account.deposit(500.0)
        >>> account.balance
        1500.0
    """

    def __init__(
            self,
            account_id: str,
            name: str,
            mobile_no: str,
            email_id: str,
            balance: float,
            card: Card):
        """Initializes BankAccount with account holder details and a linked card.

        Args:
            account_id (str): Unique identifier for the bank account.
            name (str): Full name of the account holder.
            mobile_no (str): Mobile number of the account holder.
            email_id (str): Email address of the account holder.
            balance (float): Initial account balance.
            card (Card): The payment card to associate with this account.
        """
        self.account_id = account_id
        self.name = name
        self.mobile_no = mobile_no
        self.email_id = email_id
        self.balance = balance
        self.intrest_rate = 0
        self.card = card

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

    def use_card(self, amount: float) -> None:
        """Withdraws funds and processes a card swipe for the given amount.

        Attempts to withdraw the specified amount from the account. If
        successful, delegates the swipe action to the associated Card object.
        Does nothing if the balance is insufficient.

        Args:
            amount (float): The amount to charge via card swipe.

        Example:
            >>> account.use_card(300.0)
            Card 1234-5678-9012-3456 use for ₹ 300.0
        """
        if self.withdraw(amount):
            self.card.swipe(amount)
