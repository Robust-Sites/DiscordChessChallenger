from piece import Piece 

class Pawn(Piece):
    move_set = []
    def __init__(self, coordinate, color, first_move):
        super().__init__(coordinate, color)
        self.first_move = first_move

    def possible_moves(self):
        possible_moves = []
        if self.color == 'white': 
            if self.coordinate[1] == 1: 
                possible_moves.append((self.coordinate[0],2)) 
                possible_moves.append((self.coordinate[0],3)) 
            if 
        elif self.color is 'black':
            if self.coordinate[1] == 6:
                possible_moves.append((self.coordinate[0],5)) 
                possible_moves.append((self.coordinate[0],4)) 


        

        

if __name__ == "__main__":
    main()
