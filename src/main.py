import chess_board_render as r
import pawn as p
import knight as k

def main():
    print(r.render_board())
    pawn = p.Pawn((0, 1), 'white')
    print()
    print(pawn.possible_moves())


if __name__ == "__main__":
    main()
