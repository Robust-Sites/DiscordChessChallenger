from unicodedata import name
from piece import Piece

class King(Piece):
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)
    
    def possible_moves():
        # this may return an array of all possible target
        # coordinates
        pass
if __name__ == "__main__":
    main()