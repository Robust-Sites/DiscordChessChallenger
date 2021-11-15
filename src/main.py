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
print(draw_board(
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