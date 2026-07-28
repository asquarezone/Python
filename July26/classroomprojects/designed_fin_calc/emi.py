"""Module for EMI (Equated Monthly Installment) calculations."""

from calc import BaseCalculation
from intrest import IntrestValidator
from registry import register

@register("Monthly EMI")
class MonthlyEMICalculation(BaseCalculation):
    """Calculates the monthly EMI for a loan using the standard amortization formula."""
    params = ["principal", "rate", "years"]
    label = "Monthly EMI"

    def __init__(self):
        self._validator = IntrestValidator()

    def validate(self, args):
        """Delegates validation to IntrestValidator.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.
        """
        return self._validator.validate(args)

    def compute(self, args):
        """Computes monthly EMI: [P * r * (1+r)^n] / [(1+r)^n - 1].

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.

        Returns:
            float: The monthly EMI amount.
        """
        total = args["principal"]
        rate = args["rate"] / 12 / 100
        months = args["years"] * 12
        return (total * rate * (1 + rate) ** months) / ((1 + rate) ** months - 1)
        
@register("Yearly EMI")
class YearlyEmiCalculation(BaseCalculation):
    """Calculates the yearly EMI for a loan."""
    params = ["principal", "rate", "years"]
    label = "Yearly EMI"

    def __init__(self):
        self._validator = IntrestValidator()

    def validate(self, args):
        """Delegates validation to IntrestValidator.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.
        """
        return self._validator.validate(args)

    def compute(self, args):
        """Computes yearly EMI.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.

        Returns:
            float: The yearly EMI amount.
        """
        monthly_emi = MonthlyEMICalculation()
        monthly_emi.validate(args)
        return monthly_emi.compute(args) * 12

    