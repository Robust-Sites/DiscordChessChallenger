from piece import Piece 

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
        return self.filter_moves_out_of_bounds(moves)

    #checks for out of bounds not collisions
    @staticmethod
    def filter_moves_out_of_bounds(array_of_possible_moves):
        valid_moves = []
        for coordinate in array_of_possible_moves:
            x, y = coordinate[0], coordinate[1]
            if (x > 7 or x < 0) or (y > 7 or y < 0):
                continue
            else:
                valid_moves.append(coordinate)
        return valid_moves

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
