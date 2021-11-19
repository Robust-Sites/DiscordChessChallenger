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
#New test table to print 
active_pieces = {
    "QQ": ['A1'], #Queen
    "KK": ['F2'], #King
}

#Pass a dictionary to same draw function that makes coordinates
#If dictionary contains specific values, ""QQ,'KK', looks in array,
#if array has value, it will have at least one coordinate, instead of coordinate

#Thinking of making a position string to check in key values

def new_board(dictionary):
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8] 
    final_string = ""
    row_index = 0
    for row in rows:
        # Working with a horizontal row
        line = ""
        column_index = 0
        for column in columns:
            #Accessing each piece in a row!
            #Functionality here
            current_column = (columns[column_index])
            current_row = str(rows[row_index]) #Refactor to only work with integers
            coordinate = current_column + current_row
            
            #Accessing positions in keys
            coordinate_string = ""
            for key in dictionary:
                coordinate_values = ""
                for value in dictionary[key]:
                    coordinate_values += value
                #Fill key_values with each value in key
                position = ""
                coordinate_found = coordinate_values.find(coordinate) > -1
                if coordinate_found:
                    position += key + " "
                else:
                    position += f"{coordinate} "

            column_index += 1
            line += position
        line += "\n"    
        final_string += line
        row_index += 1
    return final_string
print(new_board(active_pieces))