from piece import Piece
from piece_helpers import chess_line

class Queen(Piece):
    def __init__(self, coordinate, color):
        x, y = coordinate[0], coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y

    def possible_moves(self):
        moves = [
            *self.vertical_moves(),
            *self.horizontal_moves(),
            *self.diagonal_moves()
        ]
        return moves

    def vertical_moves(self):
        x, y  = self.x, self.y
        moves = []
        y_coordinates = chess_line(y)
        for num in y_coordinates: 
            moves.append((x, num))
        return moves 

    def horizontal_moves(self):
        x, y  = self.x, self.y
        moves = []
        x_coordinates = chess_line(x)
        for num in x_coordinates: 
            moves.append((num, y))
        return moves

    def diagonal_moves(self):
        x, y  = self.x, self.y
        moves = []
        diagonal_coordinates = chess_line(x)
        for num in diagonal_coordinates:
            moves.append((num,num))
        return moves 


    
    

if __name__ == "__main__":
    main()
