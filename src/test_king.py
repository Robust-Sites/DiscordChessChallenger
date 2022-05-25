import pytest
import piece

def test_possible_moves():
    test_king = King((2, 2), "black")
    assert (3, 1) in test_king.possible_moves()
    assert (3, 2) in test_king.possible_moves()
    assert (3, 3) in test_king.possible_moves()
    assert (2, 1) in test_king.possible_moves()
    assert (2, 3) in test_king.possible_moves()
    assert (1, 2) in test_king.possible_moves()
    assert (1, 1) in test_king.possible_moves()
    assert (1, 3) in test_king.possible_moves()

def test_left_border_possible_moves():
    pass

def test_right_border_possible_moves():
    pass

def test_bottom_border_possible_moves():
    pass

def test_top_border_possible_moves():
    pass
