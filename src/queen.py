from piece import Piece 

class Queen(Piece):
    def __init__(self, coordinate, color):
        x = coordinate[0]
        y = coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y

    def possible_moves():
        moves = []
        return moves
    
    

if __name__ == "__main__":
    main()
