import chess_board_render as r
import pawn as p
import knight as n
import rook as r
import bishop as b

def main():
   
    bishop = b.Bishop((1,1), 'Black')
    print(bishop.possible_moves())


if __name__ == "__main__":
    main()
