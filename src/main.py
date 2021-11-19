def draw_board(dictionary):
    #Dictionary with 8 keys 1-8
    #if row no pieces, will be false
    row = 1
    final = ""
    while row < 9:
        index = 1
        while index < 9:
            if dictionary[row] == False:
                final += "#"
            else:
                if index in dictionary[row]:
                    final += str(index)
                else:
                    final += "#"
            index += 1
        final += "\n"
        row += 1
    return final

#print actual coordinate

def draw_coordinates():
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8]

    final = ""
    for row in rows:
        line = ""
        for column in columns:
            position = f"{column}{row} "
            line += position  
        line += "\n"
        final += line
    return final

print(draw_board2(
    {
    1: [1,2,3,4,5,6,7,8],
    2: [1,2,3,4,5,6,7,8],
    3: False,
    4: False,
    5: False,
    6: False,
    7: [1,2,3,4,5,6,7,8],
    8: [1,2,3,4,5,6,7,8]
    }
))