import pytest
from queen import Queen
from pytest_helpers import assert_array_of_tuples
from pytest_helpers import tuples_from_x_and_y_lists

def test_queen_possible_moves():
    test_queen = Queen((0, 0), "white")
    assert_array_of_tuples(test_queen, tuples_from_x_and_y_lists(
        21, 
        [0,0,0,0,0,0,0,1,2,3,4,5,6,7,1,2,3,4,5,6,7], 
        [1,2,3,4,5,6,7,1,2,3,4,5,6,7,0,0,0,0,0,0,0]
        ))
