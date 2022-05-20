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
            invalid_column = self.coordinate[1]           
            if column != invalid_column:
                possible_moves.append((self.coordinate[0], column))

        while row_index <= max_value:
            append_row(row_index)
            row_index += 1
        while column_index <= max_value:
            append_column(column_index)
            column_index += 1
        return possible_moves