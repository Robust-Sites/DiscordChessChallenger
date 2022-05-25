import pytest
from pytest_helpers import assert_array_of_tuples
from pytest_helpers import tuples_from_x_and_y_lists 
from king import King

def test_possible_moves():
    test_king = King((3, 3), "white")
    assert_array_of_tuples(test_king, tuples_from_x_and_y_lists(8, [4, 4, 4, 3, 3, 2, 2, 2], [4, 3, 2, 4, 2, 4, 3, 2]))

def test_left_border_possible_moves():
    test_king = King((0, 1), "black")
    assert_array_of_tuples(test_king, tuples_from_x_and_y_lists(5, [0, 0, 1, 1, 1], [2, 0, 2, 1, 0]))

def test_right_border_possible_moves():
    test_king = King((5, 1), "black")
    assert_array_of_tuples(test_king, tuples_from_x_and_y_lists(5, [4, 4, 4, 5, 5], [2, 1, 0, 2, 0]))

def test_bottom_border_possible_moves():
    test_king = King((2, 0), "black")
    assert_array_of_tuples(test_king, tuples_from_x_and_y_lists(5, [1, 1, 2, 3, 3], [1, 0, 1, 1, 0]))

def test_top_right_corner_possible_moves():
    test_king = King((7, 7), "black")
    assert_array_of_tuples(test_king, tuples_from_x_and_y_lists(3, [6, 6, 7], [7, 6, 6]))
