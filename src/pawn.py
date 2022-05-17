from piece import Piece 

class Pawn(Piece):
    move_set = []
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)

    def possible_moves(self):
        possible_moves = []
        white = self.white() 
        x = self.coordinate[0]
        y = self.coordinate[1]
        at_start = self.at_start()
        if white: 
            if at_start: 
                possible_moves.append(self.forward())
        else:
            if at_start:
                possible_moves.append(self.forward())
        return possible_moves

    def at_start(self):
        if self.white():
            return self.coordinate[1] == 1 
        else:
            return self.coordinate[1] == 6 

    def white(self):
        return self.color == 'white'

    def forward(self):
        if self.white():
            return (self.coordinate[0],  self.coordinate[1] + 1)
        else: 
            return (self.coordinate[0],  self.coordinate[1] - 1)

        


if __name__ == "__main__":
    main()
