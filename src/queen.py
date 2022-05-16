from piece import Piece 

class Queen(Piece):
    move_set = [] 
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)

    def possible_moves():
        # this may return an array of all possible target
        # coordinates
        pass

if __name__ == "__main__":
    main()
