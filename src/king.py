from piece import Piece

class King(Piece):
    def __init__(self, coordinate, color):
        x = coordinate[0]
        y = coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y
    
    def possible_moves(self):
        pass

    def move_vertically(self):
        pass
    
    def move_horizontally(self):
        pass

    def move_diagonally(self):
        pass

    def
if __name__ == "__main__":
    main()
