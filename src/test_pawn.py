import pytest
from pawn import Pawn

def assert_tuples(piece, array_of_tuples):
    for tuple in array_of_tuples:
        assert tuple in piece.possible_moves()

def test_white_center_possible_moves():
    test_pawn = Pawn((3, 3), "white")
    assert_tuples(test_pawn, [(4, 4), (3, 4), (2, 4)])


def test_white_left_border_first_turn_possible_moves():
    test_pawn = Pawn((0, 1), "white")
    assert_tuples(test_pawn, [(0, 3), (0, 2), (1, 2)])

def test_white_right_border_first_turn_possible_moves():
    test_pawn = Pawn((7, 1), "white")
    assert_tuples(test_pawn, [(6, 2), (7, 2), (7, 3)])

def test_black_right_border_first_turn_possible_moves():
    test_pawn = Pawn((0,6), "black")
    assert_tuples(test_pawn, [(0, 4), (0, 5), (1, 5)])

def test_black_left_border_first_turn_possible_moves():
    test_pawn = Pawn((7,6), "black")
    assert_tuples(test_pawn, [(7, 4), (7, 5), (6, 5)])

def test_black_center_possible_moves():
    test_pawn = Pawn((2,5), "black")
    assert_tuples(test_pawn, [(1, 4), (2, 4), (3, 4)])
    assert (1,4) in test_pawn.possible_moves()
    assert (2,4) in test_pawn.possible_moves()
    assert (3,4) in test_pawn.possible_moves()
