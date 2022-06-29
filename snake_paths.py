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

from parse_data import parse_input


def main():
    
    inputs = parse_input("resources/test_data.dat")
    
    for i in range(len(inputs)):
        print("\n--- Test Case parsed [" + str(i+1) + "] ---")
        print("Board size: " + str(inputs[i][0]))
        print("Snake: " + str(inputs[i][1]))
        print("Depth: " + str(inputs[i][2]))
        print("Expected result: " + str(inputs[i][3]))

if __name__ == "__main__":
    main()