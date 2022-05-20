import chess_board_render as r
import pawn as p
import knight as n
import rook as r

def main():
   
    rook = r.Rook('00', 'black')
    print(rook.possible_moves(0,0))


if __name__ == "__main__":
    main()
