from piece import Piece

class Rook(Piece):
    def __init__(self, coordinate, color):
        super().__init__(coordinate[0], coordinate[1], color)
        self.x = coordinate[0]
        self.y = coordinate[1]
        self.coordinate = coordinate
        self.if_moved = False

    def possible_moves(self):
        possible_moves = []
        rows = self.get_rows(self.coordinate[1])
        columns = self.get_columns(self.coordinate[0])
        for row in rows:
            possible_moves.append((row, self.coordinate[1]))
        for column in columns:
            possible_moves.append((self.coordinate[0], column))
        return possible_moves
        
    def get_rows(self, column):
        allowed_rows = []
        row = 0
        max_row = 7
        while row <= max_row:
            allowed_rows.append(row)
            row += 1
        return allowed_rows
    
    def get_columns(self, row):
        allowed_columns = []
        column = 0
        max_column = 7
        while column <= max_column:
            allowed_columns.append(column)
            column += 1
        return allowed_columns   
    

    
if __name__ == "__main__":
    main()
