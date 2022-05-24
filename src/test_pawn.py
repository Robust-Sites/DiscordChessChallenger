import pytest
from pawn import Pawn

def test_possible_moves_board_middle_not_first_turn_white():
    test_pawn = Pawn((3, 3), "white")
    assert (4,4) in test_pawn.possible_moves()
    assert (3,4) in test_pawn.possible_moves()
    assert (2,4) in test_pawn.possible_moves()


def test_possible_moves_left_edge_first_turn_white():
    test_pawn = Pawn((0, 1), "white")
    assert (0,3) in test_pawn.possible_moves()
    assert (0,2) in test_pawn.possible_moves()
    assert (1,2) in test_pawn.possible_moves()


def test_possible_moves():
    pass
