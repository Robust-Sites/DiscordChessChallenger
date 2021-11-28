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

