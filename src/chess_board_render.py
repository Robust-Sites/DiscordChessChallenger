import main
starting_board = {
    'A1': 'KI',
    'B1': 'KI'}


def render_board(active_pieces={}):
    # active pieces will auto fill with empty dict. 
    # { "coordinate": "Piece"}
    # just convert active pieces to what player will see.

    #rows horizontal - columns vertical
    #list(active_pieces.values()).__contains__()
    rows = ['A', 'B','C','D','E','F','G','H']
    columns = ['1','2','3','4','5','6','7','8']
    board = ''
    for row in rows:
        line = ''
        for column in columns:
            coordinate = f'{row}{column}'
            if coordinate in active_pieces:
               line += f'{active_pieces[coordinate]} '
            else:
                line += f'{coordinate} '
        line += '\n'
        board += line
    return board

####inner methods for validate dictionary ENDS here####
if __name__ == "__main__":
    main.main()
