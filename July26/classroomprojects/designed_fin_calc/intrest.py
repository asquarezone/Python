"""Module for simple and compound interest calculations."""

from calc import BaseCalculation
from registry import register

class IntrestValidator:
    """Validates input arguments for interest calculations."""

    def validate(self, args):
        """Validates principal, rate, and years are non-negative.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.

        Raises:
            ValueError: If any value is negative.
        """
        if args["years"] < 0:
            raise ValueError("Years cannot be negative")
        if args["rate"] < 0:
            raise ValueError("Rate cannot be negative")
        if args["principal"] < 0:
            raise ValueError("Principal cannot be negative")

@register("Compound Interest")
class CompoundInterest(BaseCalculation):
    """Calculates compound interest using the standard formula."""

    params = ["principal", "rate", "years"]
    label = "Intrest Value"

    def __init__(self):
        self.validator = IntrestValidator()

    def validate(self, args):
        """Delegates validation to IntrestValidator.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.
        """
        return self.validator.validate(args)

    def compute(self, args):
        """Computes compound interest: P * (1 + r/100)^t - P.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.

        Returns:
            float: The compound interest earned.
        """
        p = args["principal"]
        r = args["rate"]
        t = args["years"]
        return p * (1 + r / 100) ** t - p

@register("Simple Interest")
class SimpleInterest(BaseCalculation):
    """Calculates simple interest using the standard formula."""

    params = ["principal", "rate", "years"]
    label = "Interest Value"

    def __init__(self):
            self.validator = IntrestValidator()

    def validate(self, args):
        """Delegates validation to IntrestValidator.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.
        """
        return self.validator.validate(args)

    def compute(self, args):
        """Computes simple interest: P * r * t / 100.

        Args:
            args (dict): Dictionary with keys 'principal', 'rate', and 'years'.

        Returns:
            float: The simple interest earned.
        """
        p = args["principal"]
        r = args["rate"]
        t = args["years"]
        return p * r * t / 100

