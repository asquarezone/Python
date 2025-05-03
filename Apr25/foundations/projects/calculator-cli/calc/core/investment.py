"""This module contains the classes for different types of Investment Calculators
"""
from calc.core.calculator import BaseCalculator

class SIPCalculator(BaseCalculator):
    def __init__(self, principal, monthly_return_rate, tenure_in_months):
        self._principal = principal
        self._monthly_return_rate = monthly_return_rate
        self._tenure_in_months = tenure_in_months

    def calculate(self):
        """This method will return the total amount after investment
        """
        pass

class LumpsumInvestmentCalculator(BaseCalculator):
    def __init__(self, principal, yearly_return_rate, tenure_in_years,intrest_compounding_frequency=1):
        self._principal = principal
        self._yearly_return_rate = yearly_return_rate
        self._tenure_in_years = tenure_in_years
        self._intrest_compounding_frequency = intrest_compounding_frequency
    
    def calculate(self):
        pass
        