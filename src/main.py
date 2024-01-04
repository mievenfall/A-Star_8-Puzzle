# ----------------------------------------------------------------------------
#   CS4200 -- Project 1: 8-Puzzle
#
#   Solving 8-puzzle problem using A* search algorithm
#   There are two candidate heuristic functions: 
#       (1) h1 = the number of misplaced tiles;
#       (2) h2 = the sum of the distances of the tiles from their goal positions.
#   Input: 
#       (1) Generate a random 8-puzzle problem
#       (2) Enter a specific 8-puzzle configuration through the standard input, 
#           which contains the configuration for only one puzzle, in the following format:
#               1 2 4
#               0 5 6
#               8 3 7
#   The goal state is:
#               0 1 2
#               3 4 5
#               6 7 8
#       Where 0 represents the empty tile.
# ----------------------------------------------------------------------------


from test_choice import test_choice


def main(): 
    while True:
        
        # Selection for single/multiple test puzzle
        print("\nSelect:\n[1] Single Test Puzzle\n[2] Multi-Test Puzzle\n[3] Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            test_choice.single_test()
        elif choice == '2':
            test_choice.multiple_test()
        elif choice == '3':
            break
    

if __name__ == "__main__":
    main()
