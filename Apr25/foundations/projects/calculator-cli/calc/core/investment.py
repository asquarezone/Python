"""This module contains the classes for different types of Investment Calculators
"""
from calc.core.calculator import BaseCalculator,BaseMonthlyCalculator

class SIPCalculator(BaseMonthlyCalculator):
    def __init__(self, principal, monthly_return_rate, tenure_in_months):
        return super().__init__(principal,monthly_return_rate, tenure_in_months)

    def calculate(self):
        """This method will return the total amount after investment
        """
        maturity_amount = self._principal * (
            (((1+self._monthly_intrest_rate) ** self._tenure_in_months) - 1) /self._monthly_intrest_rate) * ( 
                1+self._monthly_intrest_rate )
        return maturity_amount

class LumpsumInvestmentCalculator(BaseCalculator):
    def __init__(self, principal, yearly_return_rate, tenure_in_years,intrest_compounding_frequency=1):
        self._principal = principal
        self._yearly_return_rate = yearly_return_rate
        self._tenure_in_years = tenure_in_years
        self._intrest_compounding_frequency = intrest_compounding_frequency
    
    def calculate(self):
        pass
        