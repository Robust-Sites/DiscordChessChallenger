import chess_board_render as r
import pieces as p

# Validation for piece quantities
active_pieces = {
    "QQ": ['A1', 'B2', 'H7'], #Queen
    "RR": ['C3'],
    "BB": ['C4'],
    "KN": ['F2', 'G7'], #King
    "PP": ['C7'],
    "KI": ['H1']
}


def main():
   p.make_starting_pieces()


if __name__ == "__main__":
    main()