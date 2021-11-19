#11/12/2021

#Visual repr. of chess board
# if piece is empty
# 8x8 grid
def make_board(object):
    grid = [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

def get_value_in_position(grid):   
    for y in range(len(grid)): #Goes through each row
        for x in range(len(grid[y])): #Goes through each column
            value = grid[y][x] #gets value in y-row, x-column
    return value

def draw_board():
    index = 1
    row = ""
    while index < 9:
        if index == 3 or index == 1 or index == 7:
            row += str(index)
        else:
            row += "#"
        index += 1
    print(row)
#draw_board()
def draw_row(n):
    #n is string
    values = []
    for num in n:
        values.append(int(num))
    index = 1
    row = ""
    while index < 9:
        if index in values:
            row += str(index)
        else:
            row += "#"
        index += 1
    return row

#print(draw_row("128"))
#any amount of rows, and positions within specific rows
def draw_row_array(a):
    #a is array
    row = ""
    index = 1
    while index < 9:
        if index in a:
            row += str(index)
        else:
            row += "#"
        index += 1
    return row
#print(draw_row_array([3,4,7]))

#Have it draw 8 rows, if dictionary has one of rows as key
#Pass it value of array, what is in array, call draw row array
def eight_rows(dictionary={}, char="#",row_count=8):
    rows = 1
    final = "" 
    while rows <= row_count:
        #This loop deals with each row
        index = 1
        while index < 9:
            #Making a row
            if index in dictionary[rows]:
                final += str(index)
            else:
                final += char
            index += 1
        final +="\n"
        rows += 1  
    return final

#    HashTable key value 
#    keys will be 1-8
# dictionary = {
#    "Manny": True
# }
# print(dictionary["Manny"])
def new_board(dictionary):
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8]
    test_table = {
    1: [1,2,3,4,5,6,7,8],
    2: [1,2,3,4,5,6,7,8],
    3: False,
    4: False,
    5: False,
    6: False,
    7: [1,2,3,4,5,6,7,8],
    8: [1,2,3,4,5,6,7,8]
    }