# --------------------------------------------------------------------------------------------------
# Function     : tree_move
# Description  : This module creates a tree structure and uses it to check all possible paths 
#                snake can follow through the board
# Arguments    : [list - board_size], [list - snake], [int - depth]
# Output       : [String - Whole sum of paths]
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

# Library for representing the board on stdout 
from modules.pretty_board import pretty_board

# --------------------------------------------------------------------------------------------------
# Auxiliar functions
# --------------------------------------------------------------------------------------------------

# This functions receives an input and with board size creates a map, then removes the
# occupied cells finally adding the tail of the snake since its a valid position
def update_map(board_size, snake):
    map = []
    for row in range(board_size[0]):
        for column in range(board_size[1]):
            map.append([row, column])

    for cell in snake:
        if cell in map:
            map.remove(cell)
    
    map.append(snake[len(snake)-1])

    return map

# This function receives the snake coordinates and creates a copy of it
# after doing a move to another cell, returning the copied snake
def snake_after_move(snake, move):
    snake_copy = []
    # First cell changes manually, then other ones just copy the old coordinates +1 position
    snake_copy.append([snake[0][0] + move[0], snake[0][1] + move[1]])
    for i in range(len(snake)-1):
        snake_copy.append(snake[i].copy())
    
    return snake_copy


# --------------------------------------------------------------------------------------------------
# Class Tree for resolving board paths with recursion
# --------------------------------------------------------------------------------------------------

class Tree:

    # This class stores a move (Can be anything but in this script is used as a string)
    # and also all the leafs, in this case moves that can derived from last one
    def __init__(self, move):
        self.move  = move
        self.history = move
        self.leafs = []

    # Every new move in explore_leafs is store as a new tree since tree depth and width depends
    # on script parameters and not a limitation here in the class
    def append_move(self, move):
        new_leaf = Tree(move)
        new_leaf.history = self.history + move
        self.leafs.append(new_leaf)
        return new_leaf

    # For debugging reasons this function does the same as return_tree but printing result in
    # standard output
    def show_tree(self, tree):
        print("Move: " + str(tree.move))
        print("Available moves: ")
        for leaf in tree.leafs:
            print(leaf.move, end="")
        print()

    # History attribute is used to represent paths, keeping from-coming nodes in it and returning them when
    # no more leafs are found
    def return_tree_rec(self, tree):
        path = ""
        if len(tree.leafs) == 0:
            return tree.history
        else:
            for leaf in tree.leafs:
                path = path + tree.return_tree_rec(leaf)
        return path


    # This method uses recursion to retrieve 1. move in root -> 2. move in all leafs
    # Since leafs are also trees this will continue untill no more leafs are found
    def return_tree(self, tree):
        path = ""
        for leaf in tree.leafs:
            path = path + tree.return_tree_rec(leaf)
        return path

# --------------------------------------------------------------------------------------------------
# Function 
# Name:        explore_leafs
# Description: After main trees are created leaf exploring starts, untill depth is 0
#              this function will be called recursively finding all possible paths by
#              saving last move's state
# Arguments:   [Tree - tree], [int - depth], [list - snake], [list - board_size], [list - empty-map]
# Output:      Whole string of sub-moves pending from each main-tree   
# --------------------------------------------------------------------------------------------------

def explore_leafs(tree, depth, snake, board_size, empty_map):

    # Every recursive step depth is called sustracting 1, at last step this value will be 0
    if not depth:
        return tree

    move_UP = False
    move_DOWN = False
    move_LEFT = False
    move_RIGHT = False
    

    # This 4 ifs are the same, if any move is possible (cell is empty) append that move to 
    # main tree, update snake coordinates and board, and call recursion untill depth is 0
    # It's not necessary to return here explore_leafs since before recursion move is already
    # introduced in tree
    if [snake[0][0] + UP[0], snake[0][1] + UP[1]] in empty_map:
        move_UP = True

    if [snake[0][0] + DOWN[0], snake[0][1] + DOWN[1]] in empty_map:
        move_DOWN = True
        
        
    if [snake[0][0] + LEFT[0], snake[0][1] + LEFT[1]] in empty_map:
        move_LEFT = True
        

    if [snake[0][0] + RIGHT[0], snake[0][1] + RIGHT[1]] in empty_map:
        move_RIGHT = True
    

    if move_UP:
        sub_tree = tree.append_move("U")
        snake_UP = snake_after_move(snake, UP)
        explore_leafs(sub_tree, depth-1, snake_UP, board_size, update_map(board_size, snake_UP))
    if move_DOWN:
        sub_tree = tree.append_move("D")
        snake_DOWN = snake_after_move(snake, DOWN)
        explore_leafs(sub_tree, depth-1, snake_DOWN, board_size,  update_map(board_size, snake_DOWN))
    if move_LEFT:
        sub_tree = tree.append_move("L")
        snake_LEFT = snake_after_move(snake, LEFT)
        explore_leafs(sub_tree, depth-1, snake_LEFT, board_size,  update_map(board_size, snake_LEFT))
    if move_RIGHT:
        sub_tree = tree.append_move("R")
        snake_RIGHT = snake_after_move(snake, RIGHT)
        explore_leafs(sub_tree, depth-1, snake_RIGHT, board_size,  update_map(board_size, snake_RIGHT))


    # return tree that in main function will be translated to string of moves with class method
    return tree

# --------------------------------------------------------------------------------------------------
# Function 
# Name:        tree_move
# Description: Main method that creates starting trees from initial position and calls recursion
# Arguments:   [list - board_size], [list - snake], [int - depth]
# Output:      Whole string of moves   
# --------------------------------------------------------------------------------------------------

def tree_move(board_size, snake, depth):

    # Initialize strings that will be returned at the end just in case some moves are unavailable
    # at begining
    moves_UP    = ""
    moves_DOWN  = ""
    moves_LEFT  = ""
    moves_RIGHT = ""

    # Use auxiliar function to get actual empty cells
    empty_map = update_map(board_size, snake)

    # This 4 ifs are the same, if any move is possible (cell is empty) append that move to 
    # main tree, update snake coordinates and board, and call recursion untill depth is 0
    if [snake[0][0] + UP[0], snake[0][1] + UP[1]] in empty_map:
        tree_UP  = Tree("U")
        snake_UP = snake_after_move(snake, UP)
        moves_UP = tree_UP.return_tree(explore_leafs(tree_UP, depth-1, snake_UP, board_size, update_map(board_size, snake_UP)))
        #empty_map = update_map(board_size, snake_UP)

    if [snake[0][0] + DOWN[0], snake[0][1] + DOWN[1]] in empty_map:
        tree_DOWN  = Tree("D")
        snake_DOWN = snake_after_move(snake, DOWN)
        moves_DOWN = tree_DOWN.return_tree(explore_leafs(tree_DOWN, depth-1, snake_DOWN, board_size,  update_map(board_size, snake_DOWN)))
        #empty_map = update_map(board_size, snake_DOWN)

    if [snake[0][0] + LEFT[0], snake[0][1] + LEFT[1]] in empty_map:
        tree_LEFT  = Tree("L")
        snake_LEFT = snake_after_move(snake, LEFT)
        moves_LEFT = tree_LEFT.return_tree(explore_leafs(tree_LEFT, depth-1, snake_LEFT, board_size,  update_map(board_size, snake_LEFT)))
        #empty_map = update_map(board_size, snake_LEFT)

    if [snake[0][0] + RIGHT[0], snake[0][1] + RIGHT[1]] in empty_map:
        tree_RIGHT  = Tree("R")
        snake_RIGHT = snake_after_move(snake, RIGHT)
        moves_RIGHT = tree_RIGHT.return_tree(explore_leafs(tree_RIGHT, depth-1, snake_RIGHT, board_size,  update_map(board_size, snake_RIGHT)))
        #empty_map = update_map(board_size, snake_RIGHT)

    # Returns concatenation of all strings of moves
    return moves_UP + moves_DOWN + moves_LEFT + moves_RIGHT

    

