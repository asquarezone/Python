from calc.core.investment import SIPCalculator

def test_sip():
    p = 5000
    r = 0.01
    n = 24
    expected_value = 136216
    calc = SIPCalculator(principal=p, monthly_return_rate=r, tenure_in_months=n)
    actual_value =round(calc.calculate())
    assert expected_value == actual_value