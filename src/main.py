import chess_board_render as r
import pawn as p
import knight as k

def main():
   
    knight = k.Knight((2,1), 'Black')
    print(knight.possible_moves(2,0))


if __name__ == "__main__":
    main()
