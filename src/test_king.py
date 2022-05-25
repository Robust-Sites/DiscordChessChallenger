import pytest
from pytest_helpers import assert_array_of_tuples
from king import King

def test_possible_moves():
    test_king = King((3, 3), "white")
    assert_array_of_tuples(test_king, [(4, 4),(4, 3),(4, 2),(3, 4),(3, 2),(2, 4),(2, 3),(2, 2)])

def test_left_border_possible_moves():
    pass

def test_right_border_possible_moves():
    pass

def test_bottom_border_possible_moves():
    pass

def test_top_border_possible_moves():
    pass
