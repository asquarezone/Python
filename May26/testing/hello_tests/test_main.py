from main import is_even, reverse


def test_is_even_postive():
    """This function tests is even with postive cases
    """
    assert is_even(4) == True, "4 is an even number"
    assert is_even(3) == False, "3 is an odd number"
    assert is_even(0) == True, "0 is an even number"
    assert is_even(-10) == True, "0 is an even number"
    assert is_even(-3) == False, "3 is an odd number"

def test_is_even_negative():
    """This function tests is even with negative cases
    """
    assert is_even("4") == False, "string is not even"
    assert is_even("4.1") == False, "string is not even"


def test_reverse_basic():
    """This function will test basic functionality of reverse
    """

    assert reverse(123) == 321, "Reverse is not working"
    assert reverse(121) == 121, "Reverse is not working"


