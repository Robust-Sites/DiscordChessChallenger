from piece import Piece
from piece_helpers import chess_line

class Queen(Piece):
    def __init__(self, coordinate, color):
        x, y = coordinate[0], coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y

    def possible_moves():
        moves = [
            *self.vertical_moves(),
            *self.horizontal_moves(),
            *self.diagonal_moves()
        ]
        return moves

    def vertical_moves():
        x, y  = self.x, self.y
        moves = []
        for each in chess_line(self.y):
            moves.append(())
            
        return moves 

    def horizontal_moves():
        x, y  = self.x, self.y
        moves = []
        return moves

    def diagonal_moves():
        x, y  = self.x, self.y
        moves = []
        return moves 


    
    

if __name__ == "__main__":
    main()
