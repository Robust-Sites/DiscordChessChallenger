from piece import Piece
from piece_helpers import filter_moves_out_of_bounds

class King(Piece):
    def __init__(self, coordinate, color):
        x = coordinate[0]
        y = coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y
    
    def possible_moves(self):
        moves = [
            *self.vertical_moves(),
            *self.horizontal_moves(),
            *self.diagonal_moves(),
        ]
        return filter_moves_out_of_bounds(moves)

    def vertical_moves(self):
        x, y = self.x, self.y
        moves = [(x, y + 1), (x, y - 1)]
        return moves 
    
    def horizontal_moves(self):
        x, y = self.x, self.y
        moves = [(x + 1, y), (x - 1, y)]
        return moves

    def diagonal_moves(self):
        x, y = self.x, self.y
        moves = [
            (x + 1, y + 1), 
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1)
        ]
        return moves


if __name__ == "__main__":
    main()
