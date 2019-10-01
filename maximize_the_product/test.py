import pytest
from find_maximum_product import find_maximum_product


def test_typeerror():
    with pytest.raises(TypeError):
        assert find_maximum_product([.1])


def test_all_positive():
    assert find_maximum_product([1, 10, 2, 6, 5, 3]) == 300, "Result should be 300."


def test_single_negative():
    assert find_maximum_product([1, -10, 2, 6, 5, 3]) == 90, "Result should be 90."


def test_double_negative():
    assert find_maximum_product([1, 10, 2, -6, -5, 3]) == 300, "Result should be 300."


def test_negative():
    assert find_maximum_product([1, -10, 2, -6, -5, 3]) == 180, "Result should be 180."


def test_all_negative():
    assert find_maximum_product([-1, -10, -2, -6, -5, -3]) == -6, "Result should be -6."


def test_single_zero():
    assert find_maximum_product([0, 1, 10, 2, 6, 5, 3]) == 300, "Result should be 300."


def test_all_zeros():
    assert find_maximum_product([0, 0, 0, 0, 0]) == 0, "Result should be -6."


def test_empty():
    assert find_maximum_product([]) == 0, "Result should be 0."
