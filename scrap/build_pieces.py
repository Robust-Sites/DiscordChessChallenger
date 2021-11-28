#11/12/2021

#Visual repr. of chess board
# if piece is empty
# 8x8 grid
from typing import KeysView


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
    "QQ": ['A1', 'B2'], #Queen
    "LL": ['C2'],
    "MM": ['C3'],
    "EE": ['C4'],
    "KK": ['F2', 'G7'], #King
}

#Pass a dictionary to same draw function that makes coordinates
#If dictionary contains specific values, ""QQ,'KK', looks in array,
#if array has value, it will have at least one coordinate, instead of coordinate

#Thinking of making a position string to check in key values
def make_coordinate_string(column_i, row_i):
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8] 

    current_column = (columns[column_i])
    current_row = str(rows[row_i]) #Refactor to only work with integers
    coordinate = current_column + current_row
    return coordinate
def fill_current_position(coordinate_found_test, coordinate):
    if coordinate_found_test:
        correct_key = "-- "
        # print(key)
    else:
        correct_key = f"{coordinate} "   
    return correct_key

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

            coordinate = make_coordinate_string(column_index, row_index)
            position = "" #value which will be put to line

            bucket_index = 1
            bucket = ""
            for key, value in dictionary.items(): #in this loop, we are accessing EACH key
                #Make coordinate found work
                value_string = key + ''.join(value)
                coordinate_found = coordinate in value_string
                #print(coordinate_found)
                position = fill_current_position(coordinate_found, coordinate)
                
                if bucket_index <= 9:
                    bucket += f"{position} "
                else:
                    bucket += f"\n{position}"
                    bucket_index = 1
            print(bucket)
            
            line += position
            column_index += 1
        line += "\n"    
        final_string += line
        row_index += 1
    return final_string
#print(new_board(active_pieces))

def new_board2(dictionary):
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8] 
    final_string = ""
    #######Access variable keys
    coordinates = {}
    test = {
        2: "GAY"
    }
    key = test[2]
    coordinates
    #######
    row_index = 0
    for row in rows:
        # Working with a horizontal row
        line = ""
        column_index = 0
        for column in columns:
            #Accessing each position on board
            current_marker = ""
            

def flip_dictionary(dictionary):
    fliptionary = {}
    for key, values in dictionary.items():
        key_index = 0
        keys = []
        keys.append(key)
        for value in values:
             #Save value as a key
            current_key = value 
            #Place key as value
            current_value = keys[key_index]
            current_dictionary_pair = {current_key: current_value}
            fliptionary.update(current_dictionary_pair)
        key_index += 1
    return fliptionary
