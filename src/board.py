class Board:
    def create_board(): 
        board = {}
        x, y = 0, 0
        rows, columns = 7, 7
        while x <= columns:
            while y <= rows:
                board[f'{x},{y}'] = None
                y += 1
            y = 0
            x += 1
        return board
