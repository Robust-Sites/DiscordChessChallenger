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

def test_right_possible_moves():
    test_rook = Rook((0,4), "white")
    test_values = []
    array_of_row_values = return_array_of_numbers_except(0)
    for number in array_of_row_values:
        test_values.append((number, 4)) 
    assert_array_of_tuples(test_rook, test_values)

def test_up_possible_moves():
    test_rook = Rook((6,0), "black")
    test_values = []
    array_of_column_values = return_array_of_numbers_except(0)
    for number in array_of_column_values:
        test_values.append((6, number))
    assert_array_of_tuples(test_rook, test_values)
    
def test_down_possible_moves():
    test_rook = Rook((2,7), "white")
    test_values = []
    array_of_column_values = return_array_of_numbers_except(7)
    for number in array_of_column_values:
        test_values.append((2,number))
    assert_array_of_tuples(test_rook, test_values)

def test_up_and_right_possible_moves():
    test_rook = Rook((0,0), "white")
    test_values = []
    array_of_values = return_array_of_numbers_except(0)
    for number in array_of_values:
        test_values.append((0,number))
        test_values.append((number,0))
    assert_array_of_tuples(test_rook, test_values)