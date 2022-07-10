import pytest
from pytest_helpers import assert_array_of_tuples
from pytest_helpers import return_array_of_numbers_except
from rook import Rook

def test_left_possible_moves():
    test_rook = Rook((7,3), "black")
    test_values = []
    array_of_row_values = return_array_of_numbers_except(7)
    for number in array_of_row_values:
        test_values.append((number, 3))
    assert_array_of_tuples(test_rook, test_values)