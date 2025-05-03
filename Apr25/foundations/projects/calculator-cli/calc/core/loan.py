"""This module contains the classes for different types of Loan Calculators
"""


from calc.core.calculator import BaseMonthlyCalculator


class LoanEmiCalculator(BaseMonthlyCalculator):
    """This class implements the Loan EMI Calculator
    
    """
    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        super().__init__(principal, monthly_intrest_rate, tenure_in_months)

    def calculate(self):
        """This method calculates the loan emi and Returns the Monthy emi value
        """

        result = (
            self._principal * self._monthly_intrest_rate * 
            ((1 + self._monthly_intrest_rate)**self._tenure_in_months)) / (
                ((1 + self._monthly_intrest_rate)**self._tenure_in_months)-1)
        return result

class TotalAmountOfLoanCalculator(LoanEmiCalculator):
    """This calculator will respond with a total amount you will be paying
    if the take the loan (principal + intrest)
    """
    def __init__(self, principal, monthly_intrest_rate, tenure_in_months):
        super().__init__(principal, monthly_intrest_rate, tenure_in_months)
    
    def calculate(self):
        """This method calculates the loan emi and Returns the Monthy emi value
        """
        monthly = super().calculate()
        total = self._tenure_in_months * monthly
        return total
        
        

