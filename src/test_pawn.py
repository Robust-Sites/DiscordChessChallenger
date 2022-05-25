import pytest
from pytest_helpers import assert_array_of_tuples
from pawn import Pawn

def test_white_center_possible_moves():
    test_pawn = Pawn((3, 3), "white")
    assert_array_of_tuples(test_pawn, [(4, 4), (3, 4), (2, 4)])


def test_white_left_border_first_turn_possible_moves():
    test_pawn = Pawn((0, 1), "white")
    assert_array_of_tuples(test_pawn, [(0, 3), (0, 2), (1, 2)])

def test_white_right_border_first_turn_possible_moves():
    test_pawn = Pawn((7, 1), "white")
    assert_array_of_tuples(test_pawn, [(6, 2), (7, 2), (7, 3)])

def test_black_right_border_first_turn_possible_moves():
    test_pawn = Pawn((0,6), "black")
    assert_array_of_tuples(test_pawn, [(0, 4), (0, 5), (1, 5)])

def test_black_left_border_first_turn_possible_moves():
    test_pawn = Pawn((7,6), "black")
    assert_array_of_tuples(test_pawn, [(7, 4), (7, 5), (6, 5)])

def test_black_center_possible_moves():
    test_pawn = Pawn((2,5), "black")
    assert_array_of_tuples(test_pawn, [(1, 4), (2, 4), (3, 4)])
