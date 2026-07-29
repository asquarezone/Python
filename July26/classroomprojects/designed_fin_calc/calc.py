"""This module contains calcutions related classes and functions
"""


from abc import ABC, abstractmethod
from store import InMemoryStore, CacluatorStore, JsonMemoryStore

class BaseCalculation(ABC):
    """This class represents the Base Calculation
    """
    params: list[str] = []
    label: str = "Result"
    currency: str  = "Rs"
    store: CacluatorStore = JsonMemoryStore()

    def run(self, args: dict) -> str:
        """This method runs the calculation

        Args:
            args (dict): The arguments for the calculation

        Returns:
            str: The result of the calculation
        """
        self.validate(args)
        value = self.compute(args)
        self.store.append(self.__class__.__name__, args, value)
        return self.present(value)

    def validate(self, args: dict) -> bool:
        """This method validates the arguments

        Args:
            args (dict): The arguments to be validated

        Returns:
            bool: True if the arguments are valid

        Raises:
           ValueError: For missing or invalid arguments
        """
        return True

    @abstractmethod
    def compute(self, args: dict) -> str:
        """This method computes the calculation

        Args:
            args (dict): The arguments for the calculation

        Returns:
            str: The result of the calculation
        """

    def present(self, value: float) -> str:
        """This method presents the value

        Args:
            value (float): The value to be presented

        Returns:
            str: The formatted value
        """
        return f"{self.label} = {self.currency} {value:.2f}"

