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


def draw_board(dictionary): 
    columns = ['A','B','C','D','E','F','G','H']
    rows = [1,2,3,4,5,6,7,8] 
    flipped_dictionary = flip_dictionary(dictionary)
    final_string = ""
    row_index = 0
    for row in rows:
        row_string = ""
        column_index = 0
        for column in columns:
            #Format for position: 
            # print(f"{columns[column_index]} {rows[row_index]}")
            
            #Check flipped dictionary
            current_coordinate = f"{columns[column_index]}{rows[row_index]}"
            #Fill position
            position = ""
            if current_coordinate in flipped_dictionary:
                position = f"{flipped_dictionary[current_coordinate]} "
            else:
                position = f"{current_coordinate} "
            row_string += position
            column_index += 1
        row_string += "\n" #Will add a extra \n after last row unless if statement is implemented
        final_string += row_string
        row_index += 1
    return final_string


def validate_dictionary(dictionary):
    
    pass
####inner methods for validate dictionary STARTS here####
def max_piece_count(dictionary):
    max_pieces = {
        'PP': 16,
        'KI': 2,
        'QQ': 2,
        'RR': 2,
        'KN': 2,
        'BB': 2
    }
    for key, value in dictionary.items():
        print(f"{key} | {len(value)}")


####inner methods for validate dictionary ENDS here####
if __name__ == "__main__":
    main()
