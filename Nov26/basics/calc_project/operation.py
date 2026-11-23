from abc import ABC, abstractmethod


class Operation(ABC):
    """Abstract base class for mathematical and financial operations.

    All concrete operations must implement the calculate() method.
    """

    @abstractmethod
    def calculate(self, **kwargs) -> float:
        """Perform a calculation.

        Args:
            **kwargs: Arguments required by the specific operation.

        Returns:
            float: Result of the calculation.
        """
        pass


class Addition(Operation):
    """Perform addition of two numbers."""

    def calculate(self, **kwargs) -> float:
        """Add two numbers.

        Args:
            **kwargs: Must contain `a` and `b`.

        Returns:
            float: Sum of a and b.

        Example:
            >>> Addition().calculate(a=10, b=5)
            15
        """
        return kwargs["a"] + kwargs["b"]


class Subtraction(Operation):
    """Perform subtraction of two numbers."""

    def calculate(self, **kwargs) -> float:
        """Subtract b from a.

        Args:
            **kwargs: Must contain `a` and `b`.

        Returns:
            float: Difference between a and b.

        Example:
            >>> Subtraction().calculate(a=10, b=5)
            5
        """
        return kwargs["a"] - kwargs["b"]


class Multiplication(Operation):
    """Perform multiplication of two numbers."""

    def calculate(self, **kwargs) -> float:
        """Multiply two numbers.

        Args:
            **kwargs: Must contain `a` and `b`.

        Returns:
            float: Product of a and b.

        Example:
            >>> Multiplication().calculate(a=10, b=5)
            50
        """
        return kwargs["a"] * kwargs["b"]


class Division(Operation):
    """Perform division of two numbers."""

    def calculate(self, **kwargs) -> float:
        """Divide a by b.

        Args:
            **kwargs: Must contain `a` and `b`.

        Returns:
            float: Quotient of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.

        Example:
            >>> Division().calculate(a=10, b=5)
            2.0
        """
        return kwargs["a"] / kwargs["b"]


class Modulus(Operation):
    """Perform modulus (remainder) operation on two numbers."""

    def calculate(self, **kwargs) -> float:
        """Calculate the remainder of a divided by b.

        Args:
            **kwargs: Must contain `a` and `b`.

        Returns:
            float: Remainder of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.

        Example:
            >>> Modulus().calculate(a=10, b=3)
            1
        """
        return kwargs["a"] % kwargs["b"]


class SimpleInterest(Operation):
    """Calculate simple interest."""

    def calculate(self, **kwargs) -> float:
        """Calculate simple interest on a principal amount.

        Formula:
            SI = (P * R * T) / 100

        Args:
            **kwargs:
                p (float): Principal amount.
                r (float): Annual interest rate in percentage.
                t (float): Time period in years.

        Returns:
            float: Simple interest earned or payable.

        Example:
            >>> SimpleInterest().calculate(p=10000, r=5, t=2)
            1000.0
        """
        return kwargs["p"] * kwargs["t"] * kwargs["r"] / 100


class CompoundInterest(Operation):
    """Calculate compound interest compounded annually."""

    def calculate(self, **kwargs) -> float:
        """Calculate compound interest.

        Formula:
            A = P * (1 + R / 100) ** T
            CI = A - P

        Args:
            **kwargs:
                p (float): Principal amount.
                r (float): Annual interest rate in percentage.
                t (float): Time period in years.

        Returns:
            float: Compound interest earned or payable, excluding principal.

        Example:
            >>> CompoundInterest().calculate(p=10000, r=5, t=2)
            1025.0
        """
        p = kwargs["p"]
        r = kwargs["r"]
        t = kwargs["t"]

        amount = p * (1 + r / 100) ** t
        return amount - p


class EMI(Operation):
    """Calculate the Equated Monthly Instalment for a loan."""

    def calculate(self, **kwargs) -> float:
        """Calculate monthly loan repayment (EMI).

        Formula:
            EMI = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

        Args:
            **kwargs:
                p (float): Loan principal amount.
                r (float): Annual interest rate in percentage.
                t (float): Loan tenure in years.

        Returns:
            float: Monthly EMI amount.

        Example:
            >>> EMI().calculate(p=500000, r=8.5, t=5)
            102...  # Approximate monthly EMI
        """
        p = kwargs["p"]
        annual_rate = kwargs["r"]
        t = kwargs["t"]

        # Convert annual interest rate into monthly decimal rate.
        monthly_rate = annual_rate / (12 * 100)

        # Convert loan tenure from years to months.
        months = t * 12

        # Handle zero-interest loans.
        if monthly_rate == 0:
            return p / months

        emi = (
            p
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        return emi

class CircleArea(Operation):
    def calculate(self, **kwargs):
        radius = kwargs['r']
        import math
        return math.pi * radius * radius