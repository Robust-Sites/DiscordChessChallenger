def filter_moves_out_of_bounds(array_of_possible_moves):
    valid_moves = []
    for coordinate in array_of_possible_moves:
        x, y = coordinate[0], coordinate[1]
        if (x > 7 or x < 0) or (y > 7 or y < 0):
            continue
        else:
            valid_moves.append(coordinate)
    return valid_moves

