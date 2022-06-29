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
# Standard Library import
# --------------------------------------------------------------------------------------------------

import sys
import os

# --------------------------------------------------------------------------------------------------
# Extra Library import
# --------------------------------------------------------------------------------------------------

from modules.parse_data import parse_input
from modules.pretty_board import pretty_board

# --------------------------------------------------------------------------------------------------
# Global variables
# --------------------------------------------------------------------------------------------------

# Variables that save operations for representing movements
UP    = [-1, 0]
DOWN  = [1, 0]
LEFT  = [0, -1]
RIGHT = [0, 1]

# Color variables
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

# --------------------------------------------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------------------------------------------

# This functions receives an input and with board size creates a map, then removes the
# occupied cells finally adding the tail of the snake since its a valid position
def procces_map(input):
    map = []
    for row in range(input[0][0]):
        for column in range(input[0][1]):
            map.append([row, column])

    for cell in input[1]:
        if cell in map:
            map.remove(cell)
    
    map.append(input[1][len(input[1])-1])

    return map

def move_snake():
    pass

# --------------------------------------------------------------------------------------------------
# Main routine
# --------------------------------------------------------------------------------------------------

def main():
    
    inputs = parse_input("resources/test_data.dat")
    
    for i in range(len(inputs)):
        print("\n" + OKGREEN + "--- [INFO] Test Case parsed [" + str(i+1) + "] ---" + ENDC)
        print("Board size: " + str(inputs[i][0]))
        print("Snake: " + str(inputs[i][1]))
        print("Depth: " + str(inputs[i][2]))
        print("Expected result: " + str(inputs[i][3]))
        print("Board state:")
        pretty_board(inputs[i][0], inputs[i][1])

    for input in inputs:
        empty_map = procces_map(input)


if __name__ == "__main__":
    main()