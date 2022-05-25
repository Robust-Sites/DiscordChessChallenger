from piece import Piece
from pytest_helpers import filter_moves_out_of_bounds

class King(Piece):
    def __init__(self, coordinate, color):
        x = coordinate[0]
        y = coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y
    
    def possible_moves(self):
        moves = []
        self.move_vertically()
        self.move_horizontally()
        self.move_diagonally()
        return filter_moves_out_of_bounds(moves)

    def vertical_moves(self):
        pass
    
    def horizontal_moves(self):
        pass

    def diagonal_moves(self):
        pass

if __name__ == "__main__":
    main()
