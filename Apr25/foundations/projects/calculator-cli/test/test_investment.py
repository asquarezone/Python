from calc.core.investment import SIPCalculator, LumpsumInvestmentCalculator

def test_sip():
    """This test case tests the positive testing of sip returns
    """
    p = 5000
    r = 0.01
    n = 24
    expected_value = 136216
    calc = SIPCalculator(principal=p, monthly_return_rate=r, tenure_in_months=n)
    actual_value =round(calc.calculate())
    assert expected_value == actual_value


def test_lumpsum():
    p = 100000
    r = 0.1
    t = 20

    calc = LumpsumInvestmentCalculator(
        principal=p,
        yearly_return_rate=r,
        tenure_in_years=t
    )
    calculated = round(calc.calculate())
    expected = 672750
    assert expected == calculated
