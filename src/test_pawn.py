import pytest
from pawn import Pawn

def test_possible_moves():
    test_pawn = Pawn((3, 3), "white")
    assert test_pawn.possible_moves() == [(3, 4), (2, 4), (4, 4)] 

def test_possible_moves_at_edge():
    test_pawn = Pawn((0, 1), "white")
    assert test_pawn.possible_moves() == [(0, 2), (1, 2), (0, 3)]  


