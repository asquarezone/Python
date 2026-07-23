def simple_intrest(
    principal: float,
    periods: int,
    rate: float):
    return principal * periods * rate / 100


def compound_interest(
    principal: float,
    periods: int,
    rate: float):
    return principal * (1 + rate / 100) ** periods

