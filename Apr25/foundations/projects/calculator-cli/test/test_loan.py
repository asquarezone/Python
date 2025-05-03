from calc.core.loan import LoanEmiCalculator,TotalAmountOfLoanCalculator

def test_loanemi():
    """This test case checks loan
    """
    p = 1000000
    r = 0.006
    t = 120
    calc = LoanEmiCalculator(principal=p,monthly_intrest_rate=r,tenure_in_months=t)
    what_we_got = calc.calculate()
    answer = 11714
    assert int(what_we_got) == answer


def test_total_loan():
    """This test case tests the total amount that will be paid 
    """
    p = 1000000
    r = 0.006
    t = 120
    calc = TotalAmountOfLoanCalculator(principal=p, monthly_intrest_rate=r,tenure_in_months=t)
    total = calc.calculate()
    assert total > p


