from piece import Piece 

class Pawn(Piece):
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)

    def possible_moves(self):
        possible_moves = []
        at_start = self.at_start()

        possible_moves.append(self.forward())
        possible_moves.append(self.take_left())
        possible_moves.append(self.take_right())
        if at_start:  
            possible_moves.append(self.forward(2))
        return self.filter_moves_out_of_bounds(possible_moves)

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
        if self.white():
            return self.coordinate[1] == 1 
        else:
            return self.coordinate[1] == 6 

    def white(self):
        return self.color == 'white'

    def forward(self, counter=1):
        if self.white():
            return (self.coordinate[0],  self.coordinate[1] + counter)
        else: 
            return (self.coordinate[0],  self.coordinate[1] - counter)

    def left(self, counter=1):
        if self.white():
            return (self.coordinate[0],  self.coordinate[1] + counter)
        else: 
            return (self.coordinate[0],  self.coordinate[1] - counter)

    def right(self, counter=1):
        if self.white():
            return (self.coordinate[0],  self.coordinate[1] + counter)
        else: 
            return (self.coordinate[0],  self.coordinate[1] - counter)

    def take_left(self, counter=1):
        if self.white():
            return (self.coordinate[0] - counter, self.coordinate[1] + counter)
        else:
            return (self.coordinate[0] + counter, self.coordinate[1] - counter)

    def take_right(self, counter=1):
        if self.white():
            return (self.coordinate[0] + counter, self.coordinate[1] + counter)
        else:
            return (self.coordinate[0] - counter, self.coordinate[1] - counter)

        


if __name__ == "__main__":
    main()
