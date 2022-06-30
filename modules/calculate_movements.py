# --------------------------------------------------------------------------------------------------
# Function     : pretty_board
# Description  : This function prints board with snake for visual representation
# Arguments    : [list - board_size], [list - snake_position]
# Output       : None
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Global variables
# --------------------------------------------------------------------------------------------------

# Variables that save operations for representing movements
UP    = [0, -1]
DOWN  = [0, 1]
LEFT  = [-1, 0]
RIGHT = [1, 0]

# --------------------------------------------------------------------------------------------------
# Extra Library import
# --------------------------------------------------------------------------------------------------

from modules.pretty_board import pretty_board

# --------------------------------------------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------------------------------------------

# This functions receives an input and with board size creates a map, then removes the
# occupied cells finally adding the tail of the snake since its a valid position
def procces_map(board_size, snake):
    map = []
    for row in range(board_size[0]):
        for column in range(board_size[1]):
            map.append([row, column])

    for cell in snake:
        if cell in map:
            map.remove(cell)
    
    map.append(snake[len(snake)-1])

    return map

def snake_after_move(snake, move):
    for i in range(len(snake)-1):
        if i == 0:
            snake_copy_actual = snake[0]
            snake_copy_next   = snake[1]
            snake[0] = [snake[0][0] + move[0], snake[0][1] + move[1]]
        else:
            snake[i] = snake_copy_actual
            snake_copy_actual = snake_copy_next
            snake_copy_next = snake[i+1]

    snake[len(snake)-1] = snake_copy_actual
    return snake

# --------------------------------------------------------------------------------------------------
# Function
# --------------------------------------------------------------------------------------------------

# This function prints board with snake for visual representation
def calculate_movements(board_size, snake, depth, initial_map, list_of_moves = [], path = ""):

    if depth == 0:
        return path

    print("Moves left: " + str(depth))
    
    for i in range(depth):
        possible_move_up    = [snake[0][0] + UP[0], snake[0][1] + UP[1]]
        possible_move_down  = [snake[0][0] + DOWN[0], snake[0][1] + DOWN[1]]
        possible_move_left  = [snake[0][0] + LEFT[0], snake[0][1] + LEFT[1]]
        possible_move_right = [snake[0][0] + RIGHT[0], snake[0][1] + RIGHT[1]]

        lower_depth = depth - 1

        if possible_move_up in initial_map:
            pretty_board(board_size, snake)
            snake_up = snake_after_move(snake, UP).copy()
            empty_map_up = procces_map(board_size, snake_up)
            print(path + "U" + calculate_movements(board_size, snake_up, lower_depth, empty_map_up, list_of_moves, path))
            if len(path) == depth:
                print("Path: " + str(path))
                list_of_moves.append(path)
                path = ""
            else:
                return path + "U" + calculate_movements(board_size, snake_up, lower_depth, empty_map_up, list_of_moves, path)

        if possible_move_down in initial_map:
            pretty_board(board_size, snake)
            snake_down = snake_after_move(snake, DOWN).copy()
            empty_map_down = procces_map(board_size, snake_down)
            if len(path) == depth:
                print("Path: " + str(path))
                list_of_moves.append(path)
                path = ""
            else:
                return path + "D" + calculate_movements(board_size, snake_down, lower_depth, empty_map_down, list_of_moves, path)

        if possible_move_left in initial_map:
            pretty_board(board_size, snake)
            snake_left = snake_after_move(snake, LEFT).copy()
            empty_map_left = procces_map(board_size, snake_left)
            if len(path) == depth:
                print("Path: " + str(path))
                list_of_moves.append(path)
                path = ""
            else:
                return path + "L" + calculate_movements(board_size, snake_left, lower_depth, empty_map_left, list_of_moves, path)

        if possible_move_right in initial_map:
            pretty_board(board_size, snake)
            snake_right = snake_after_move(snake, RIGHT).copy()
            empty_map_right = procces_map(board_size, snake_right)
            if len(path) == depth:
                print("Path: " + str(path))
                list_of_moves.append(path)
                path = ""
            else:
                return path + "R" + calculate_movements(board_size, snake_right, lower_depth, empty_map_right, list_of_moves, path)

        return path

