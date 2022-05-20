from piece import Piece

class Rook(Piece):
    def __init__(self, coordinate, color):
        super().__init__(coordinate, color)
        self.if_moved = False

    def possible_moves(self):
        possible_moves = []
        at_start = self.at_start()
        max_value = 7

        row_index = 0
        column_index = 0

        def append_row(row):
            invalid_row = self.coordinate[0]
            if row != invalid_row:
                possible_moves.append((row, self.coordinate[1]))
        
        def append_column(column):
            

        while row_index <= max_value:
            append_row(row_index)