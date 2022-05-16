import chess_board_render as r
import pawn as p
import knight as k

def main():
    print(r.render_board())
    pawn = p.Pawn("C2", "Black")
    knight = k.Knight("C2", "Black")
    knight.possible_moves(1,2)
    pass 


if __name__ == "__main__":
    main()
