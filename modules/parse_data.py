# --------------------------------------------------------------------------------------------------
# Function     : parse_input
# Description  : This function parses data to test functionality as well as expected result
# Arguments    : [string - filename]
# Output       : List containing lists containing
#                    map size,
#                    snake coordinates,
#                    depth,
#                    expected result
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Extra Library import
# --------------------------------------------------------------------------------------------------

import json

# --------------------------------------------------------------------------------------------------
# Function
# --------------------------------------------------------------------------------------------------

def parse_input(filename):
    list_parsed = []
    data_parsed = []
    # Open data file
    data_file = open(filename, "r")
    # Iterate over data saving parsed data
    for line in data_file:
        # Split raw data with ":" separator
        line_parsed = line.split(":")
        # Parse line and add it to list, list of lists has to be parsed with json module
        if "board" in line_parsed[0]:
            # List parsed will be list of strings, map it to int
            line_parsed_to_list = json.loads(line_parsed[1])
            line_parsed_int = [int(item) for item in line_parsed_to_list]
            data_parsed.append(line_parsed_int)
        elif "snake" in line_parsed[0]:
            # List parsed will be list of lists of strings, use comprehension for lists of ints
            line_parsed_to_list = json.loads(line_parsed[1])
            line_parsed_int = [[int(item) for item in sub_list] for sub_list in line_parsed_to_list]
            data_parsed.append(line_parsed_int)
        elif "depth" in line_parsed[0]:
            # Parse depth to int
            data_parsed.append(int(line_parsed[1]))
        elif "result" in line_parsed[0]:
            # Parse depth to int
            data_parsed.append(int(line_parsed[1]))
        else:
            pass
        
        # Before end of iteration, if data_parsed size is 3 items, append it to list_parsed
        # and clear all values of data_parsed since it's a temp list
        if len(data_parsed) == 4:
            list_parsed.append(data_parsed.copy())
            data_parsed.clear()

    return list_parsed