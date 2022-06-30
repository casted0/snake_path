# --------------------------------------------------------------------------------------------------
# File         : snake_paths.py
# Author       : Pablo Castedo Sanjuan for DAMAVIS HR Interview
# Language     : Python
# Inputs       :
#   - Map size          -> n * m cells
#   - Snake coordinates -> Array of 2-dimensional vectors representing snake coordinates
#   - Depth             -> Quantitiy of moves that have to be processed
# Synopsis     : This script receives a map, a snake and an amount of moves, and generates 
#              : a list of possible sequences of moves
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Module import
# --------------------------------------------------------------------------------------------------

from modules.parse_data import parse_input
from modules.pretty_board import pretty_board
from modules.tree_move import tree_move

# --------------------------------------------------------------------------------------------------
# Global variables
# --------------------------------------------------------------------------------------------------

# Color variables
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

# --------------------------------------------------------------------------------------------------
# Main routine
# Description: Parses test cases, executes recursion to get paths and represent test results
# --------------------------------------------------------------------------------------------------

def main():
    
    # Test data is located on resources folder
    inputs = parse_input("resources/test_data.dat")
    
    # Loops around all test cases read on test_data
    for i in range(3):

        # Variable used for representing test number at the end of the main routine
        test_count = i + 1

        # Save variables parsed for better understanding
        board_size = inputs[i][0]
        snake      = inputs[i][1]
        depth      = inputs[i][2]
        expected_r = inputs[i][3]

        # Tells user test cases have been parsed correctly and gives information
        print("\n" + WARNING + "--- [INFO] Test Case parsed [" + str(i+1) + "] ---" + ENDC)
        print("Board size: " + str(board_size))
        print("Snake: " + str(snake))
        print("Depth: " + str(depth))
        print("Expected result: " + str(expected_r))
        print("Board state:")
        print("\n ----------------- INITIAL STATE ----------------- \n")
        # This function is located at modules/pretty board and gives visual info about board and snake
        pretty_board(board_size, snake)
        print("\n ----------------- START EXECUTION ----------------- \n")

        # Moves are retrived as a long string, every x (depth) movement a new sequence is created and kept
        string_of_moves = tree_move(board_size, snake, depth)
        move = ""
        list_of_moves = []

        for i in range(len(string_of_moves)):
            move = move + string_of_moves[i]
            # When (depth) moves have been parsed a new move is appended to final list
            if len(move) == depth:
                list_of_moves.append(move)
                move = ""

        # Print list of moves to see final results
        print("\nList of moves: ")
        for move in list_of_moves:
            print(move)

        # Check number of results on each test for debuging issues
        # If len of moves is different from expected output result is wrong
        if len(list_of_moves) == int(expected_r):
            print("\n" + OKGREEN + "--- [INFO] SUCCESS on Test case [" + str(test_count) + "] ---\n" + ENDC)
            print("Calculated result: " + str(len(list_of_moves)))
            print("Expected output: " + str(expected_r))
        else:
            print("\n" + FAIL + "--- [INFO] FAILURE on Test case [" + str(test_count) + "] ---\n" + ENDC)
            print("Calculated result: " + str(len(list_of_moves)))
            print("Expected output: " + str(expected_r))

if __name__ == "__main__":
    main()