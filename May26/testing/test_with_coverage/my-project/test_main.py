from main import is_even, is_prime, is_numeric_pallendrome
import pytest

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(-5) == False


def test_is_numeric_pallendrome():
    assert is_numeric_pallendrome(121) == True
    assert is_numeric_pallendrome(123) == False
    # we are expecting an execption.
    with pytest.raises(ValueError):
        is_numeric_pallendrome('123')
