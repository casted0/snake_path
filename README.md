**Snake path**

Description: Script that explores a map ocupping certain coordinates, and calculates all possible moves given a specific depth (Amount of total moves to do)

Input:
 - Map size as n * m meaning rows * columns
 - Snake coordinates as list of lists [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
 - Depth as total amount of final moves to count as valid solution

Output: 
 - Number of possible solutions
 - Each solution shall contain every direction followed (LLU meaning Left Left Up with a depth of 3)

Modules:
 - snake_path.py = Main routine
 - resources = .dat file containing all inputs and expected outputs
