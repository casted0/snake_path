# --------------------------------------------------------------------------------------------------
# Function     : pretty_board
# Description  : This function prints board with snake for visual representation
# Arguments    : [list - board_size], [list - snake_position]
# Output       : None
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Function
# --------------------------------------------------------------------------------------------------

# This function prints board with snake for visual representation
def pretty_board(board_size, snake_position):
    print("")
    for i in range(board_size[1]):
        for j in range(board_size[0]):
            print("+---", end = "")
        print("+")
        for j in range(board_size[0]):
            pos_to_print = [j, i]
            if pos_to_print == snake_position[0]:
                print("| H ", end = "")
            elif pos_to_print == snake_position[len(snake_position) - 1]:
                print("| T ", end = "")
            elif pos_to_print in snake_position:
                print("| X ", end = "")
            else:
                print("|   ", end = "")
        print("|")
        for j in range(board_size[0]):
            print("+---", end = "")
        print("+")
    print("")
        