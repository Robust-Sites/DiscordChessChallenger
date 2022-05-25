def assert_array_of_tuples(piece, array_of_tuples):
    for tuple in array_of_tuples:
        assert tuple in piece.possible_moves()
