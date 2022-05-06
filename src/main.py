import chess_board_render as r

# Validation for piece quantities
# active_pieces = {
#     "QQ": ['A1', 'B2', 'H7'], #Queen
#     "RR": ['C3'],
#     "BB": ['C4'],
#     "KN": ['F2', 'G7'], #King
#     "PP": ['C7'],
#     "KI": ['H1']
# }
starting_board = {
    'A1': 'KI',
    'B1': 'KI'}

def main():
    print(r.render_board(starting_board))
    pass 


if __name__ == "__main__":
    main()