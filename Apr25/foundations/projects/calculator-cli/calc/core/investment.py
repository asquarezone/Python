"""This module contains the classes for different types of Investment Calculators
"""
from calc.core.calculator import BaseCalculator,BaseMonthlyCalculator
from calc.core.exceptions import ZeroInvestmentError


class SIPCalculator(BaseMonthlyCalculator):
    """This is SIP (Systematic Investment Calculator) with monthly investments
    

    Usage:

    from calc.core.investment import SIPCalculator
    p = 5000
    r = 0.01
    n = 24
    calc = SIPCalculator(principal=p, monthly_return_rate=r, tenure_in_months=n)
    future_value = calc.calculate()

    """
    def __init__(
            self, 
            principal: int|float, 
            monthly_return_rate: float, 
            tenure_in_months: int):
        """Initializer

        Args:
            principal (int | float): monthly investment 
            monthly_return_rate (float): average monthly return rate
            tenure_in_months (int): number of months

        """
        return super().__init__(principal,monthly_return_rate, tenure_in_months)

    def calculate(self) -> float:
        """Returns the future value of investment

        Returns:
            float: future value
        """
        if self._principal == 0:
            raise ZeroInvestmentError()

        maturity_amount = self._principal * (
            (((1+self._monthly_intrest_rate) ** self._tenure_in_months) - 1) /self._monthly_intrest_rate) * ( 
                1+self._monthly_intrest_rate )
        return maturity_amount

class LumpsumInvestmentCalculator(BaseCalculator):
    
    def __init__(
            self, 
            principal : int|float, 
            yearly_return_rate: float, 
            tenure_in_years: int,
            intrest_compounding_frequency:int =1
        ):
        """Intializer for Lumpsum investments

        Args:
            principal (int | float): Total lumpsum investment
            yearly_return_rate (float): yearly return rate
            tenure_in_years (int): tenure in years
            intrest_compounding_frequency (int, optional): compounding frequency in a year. Defaults to 1.
        """
        self._principal = principal
        self._yearly_return_rate = yearly_return_rate
        self._tenure_in_years = tenure_in_years
        self._intrest_compounding_frequency = intrest_compounding_frequency
    
    def calculate(self) -> float:
        """Future value of lumpsum investment

        Returns:
            float: Future value
        """
        future_value = self._principal * ( 
            (1 + (self._yearly_return_rate/self._intrest_compounding_frequency)) ** 
                (self._tenure_in_years * self._intrest_compounding_frequency)
        )
        return future_value
        