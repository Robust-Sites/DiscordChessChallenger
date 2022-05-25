def assert_array_of_tuples(piece, array_of_tuples):
    for tuple in array_of_tuples:
        assert tuple in piece.possible_moves()

def tuples_from_x_and_y_lists(number_of_tuples, list_of_x_values, list_of_y_values):
    tuples = []
    count = 0
    while count < number_of_tuples:
        tuples.append((list_of_x_values[count], list_of_y_values[count])) 
        count += 1
    return tuples

