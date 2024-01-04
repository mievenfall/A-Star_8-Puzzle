# ------------------------------------------------------------
#   Handle input between
#       (1) Generate a random 8-puzzle problem
#       (2) Enter a specific 8-puzzle configuration
# ------------------------------------------------------------

import random


class input_handler:

    # (1) Generate a random 8-puzzle problem
    def generate_random_puzzle():
        puzzle = list(range(9))
        random.shuffle(puzzle)
        return tuple(puzzle)
    
    
    # (2) Enter a specific 8-puzzle configuration
    def read_puzzle_input():
        print("\nEnter your 8-puzzle configuration row by row (use 0 for the empty tile):")
        puzzle = []
        for _ in range(3):
            row = input().strip().split()
            puzzle.extend([int(n) for n in row])
        return tuple(puzzle)
