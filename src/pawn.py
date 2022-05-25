from piece import Piece 
from piece_helpers import filter_moves_out_of_bounds

class Pawn(Piece):
    def __init__(self, coordinate, color):
        x = coordinate[0]
        y = coordinate[1]
        super().__init__(x, y, color)
        self.x = x
        self.y = y


    def possible_moves(self):
        moves = []
        at_start = self.at_start()

        moves.append(self.forward())
        moves.append(self.take_left())
        moves.append(self.take_right())
        if at_start:  
            moves.append(self.forward(2))
        return filter_moves_out_of_bounds(moves)

    def at_start(self):
        x, y = self.x, self.y
        if self.white():
            return y == 1 
        else:
            return y == 6 

    def white(self):
        return self.color == 'white'

    def forward(self, counter=1):
        x, y = self.x, self.y
        if self.white():
            return (x,  y + counter)
        else: 
            return (x,  y - counter)

    def left(self, counter=1):
        x, y = self.x, self.y
        if self.white():
            return (x,  y + counter)
        else: 
            return (x,  y - counter)

    def right(self, counter=1):
        x, y = self.x, self.y
        if self.white():
            return (x,  y + counter)
        else: 
            return (x,  y - counter)

    def take_left(self, counter=1):
        x, y = self.x, self.y
        if self.white():
            return (x - counter, y + counter)
        else:
            return (x + counter, y - counter)

    def take_right(self, counter=1):
        x, y = self.x, self.y
        if self.white():
            return (x + counter, y + counter)
        else:
            return (x - counter, y - counter)

        


if __name__ == "__main__":
    main()
