import main

# example_active_pieces= {
#     'A1': 'KI',
#     'B1': 'P'
# }

def render_board(active_pieces={}):
    rows = ['H','G','F','E','D','C','B','A']
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

if __name__ == "__main__":
    main.main()
