import pytest
from pawn import Pawn

def test_white_center_possible_moves():
    test_pawn = Pawn((3, 3), "white")
    assert (4,4) in test_pawn.possible_moves()
    assert (3,4) in test_pawn.possible_moves()
    assert (2,4) in test_pawn.possible_moves()


def test_white_left_border_first_turn_possible_moves():
    test_pawn = Pawn((0, 1), "white")
    assert (0,3) in test_pawn.possible_moves()
    assert (0,2) in test_pawn.possible_moves()
    assert (1,2) in test_pawn.possible_moves()


def test_white_right_border_first_turn_possible_moves():
    test_pawn = Pawn((7, 1), "white")
    assert (6,2) in test_pawn.possible_moves()
    assert (7,2) in test_pawn.possible_moves()
    assert (7,3) in test_pawn.possible_moves()

def test_black_right_border_first_turn_possible_moves():
    test_pawn = Pawn((0,6), "black")
    assert (0,4) in test_pawn.possible_moves()
    assert (0,5) in test_pawn.possible_moves()
    assert (1,5) in test_pawn.possible_moves()

def test_black_left_border_first_turn_possible_moves():
    test_pawn = Pawn((7,6), "black")
    assert (7,4) in test_pawn.possible_moves()
    assert (7,5) in test_pawn.possible_moves()
    assert (6,5) in test_pawn.possible_moves()

def test_black_center_possible_moves():
    test_pawn = Pawn((2,5), "black")
    assert (1,4) in test_pawn.possible_moves()
    assert (2,4) in test_pawn.possible_moves()
    assert (3,4) in test_pawn.possible_moves()
