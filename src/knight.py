from piece import Piece 

class Knight(Piece):
    def __init__(self, coordinate, color):
        self.coordinate = coordinate
        self.color = color

    def possible_moves(self, row_index, column_index):
        rows = ['A','B','C','D','E','F','G','H']
        columns = ['1','2','3','4','5','6','7','8']
        allowed_moves = []
        
        row = row_index - 2

        while (row - row_index < 3):
            if (row >= 0 and row <= 7):
                column = column_index - 2
                while (column - column_index < 3):
                    if (column >= 0 and column <= 7):
                        if (abs(row - row_index) + abs(column - column_index) == 3):
                            allowed_moves.append(f'{rows[row]}{columns[column]}')
                    column += 1
            row += 1
        return allowed_moves

if __name__ == "__main__":
    main()