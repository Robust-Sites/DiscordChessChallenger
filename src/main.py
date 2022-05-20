import chess_board_render as r
import pawn as p
import knight as n
import rook as r

def main():
   
    rook = r.Rook('55', 'black')
    print(rook.possible_moves())


if __name__ == "__main__":
    main()
