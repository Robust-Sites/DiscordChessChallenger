import chess_board_render as r

active_pieces = {
    "QQ": ['A1', 'B2'], #Queen
    "LL": ['C2'],
    "MM": ['C3'],
    "EE": ['C4'],
    "KK": ['F2', 'G7'], #King
}
print(r.flip_dictionary(active_pieces))