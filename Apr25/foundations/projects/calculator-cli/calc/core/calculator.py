"""This module has base implementations for calculator


Usage
>>> from calc.core.calculator import BaseCalculator

"""
from abc import abstractmethod, ABC

class BaseCalculator(ABC):
    """Calculator Base.

    All the Calculators should be derived from this Base Implementation
    """
    
    @abstractmethod
    def calculate(self):
        """This method will perform calculations and respond 
        with a result
        """


class BaseMonthlyCalculator(BaseCalculator):

    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        """This is intializer for monthly Calculaions

        Args:
            principal (int|float): _description_
            monthly_intrest_rate (float): _description_
            tenure_in_months (int): _description_
        """
        self._principal = principal
        self._monthly_intrest_rate = monthly_intrest_rate
        self._tenure_in_months = tenure_in_months

    @abstractmethod
    def calculate(self):
        """This method will perform calculations and respond 
        with a result
        """
