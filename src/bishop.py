from piece import Piece

class Bishop(Piece):
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)

    def possible_moves(self):
        possible_moves = []
        y_equals_x_set = self.y_equals_x_moves()
        possible_moves.append(y_equals_x_set)
        y_equals_negative_x_set = self.y_equals_negative_x_moves()
        possible_moves.append(y_equals_negative_x_set)
        return possible_moves
        

    def y_equals_x_moves(self):
        allowed_moves = []
        min_value = 0
        max_value = 7
        coordinate_copy = [self.coordinate[0], self.coordinate[1]]
        while coordinate_copy[0] > min_value or coordinate_copy[1] > min_value:
            coordinate_copy[0] -= 1
            coordinate_copy[1] -= 1
        while coordinate_copy[0] <= max_value or coordinate_copy[1] <= max_value:
            if coordinate_copy[0] != self.coordinate[0] and coordinate_copy[1] != self.coordinate[1]:
                allowed_moves.append((coordinate_copy[0], coordinate_copy[1]))
            coordinate_copy[0] += 1
            coordinate_copy[1] += 1
        return allowed_moves

    def y_equals_negative_x_moves(self):
        allowed_moves = []
        min_value = 0
        max_value = 7
        coordinate_copy = [self.coordinate[0], self.coordinate[1]]
        while coordinate_copy[0] > min_value or coordinate_copy[1] < max_value:
            coordinate_copy[0] -= 1
            coordinate_copy[1] += 1
        while coordinate_copy[0] <= max_value or coordinate_copy[1] >= min_value:
            if coordinate_copy[0] != self.coordinate[0] and coordinate_copy[1] != self.coordinate[1]:
                allowed_moves.append((coordinate_copy[0], coordinate_copy[1]))
            coordinate_copy[0] += 1
            coordinate_copy[1] -= 1
        return allowed_moves

if __name__ == "__main__":
    main()

