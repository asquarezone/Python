"""This module contains the classes for different types of Loan Calculators
"""


from calc.core.calculator import BaseCalculator


class LoanEmiCalculator(BaseCalculator):
    """This class implements the Loan EMI Calculator
    """
    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        self._principal = principal
        self._monthly_intrest_rate = monthly_intrest_rate
        self._tenure_in_months = tenure_in_months

    def calculate(self):
        """This method calculates the loan emi and Returns the Monthy emi value
        """
        pass

class TotalAmountOfLoanCalculator(BaseCalculator):
    """This calculator will respond with a total amount you will be paying
    if the take the loan (principal + intrest)
    """
    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        self._principal = principal
        self._monthly_intrest_rate = monthly_intrest_rate
        self._tenure_in_months = tenure_in_months
    
    def calculate(self):
        """This method calculates the loan emi and Returns the Monthy emi value
        """
        pass
        
        

