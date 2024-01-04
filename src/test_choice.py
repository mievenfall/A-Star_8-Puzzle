from puzzle import puzzle
from heuristic_function import heuristic_function
from a_star_search import a_star_search
from input_handler import input_handler
from output_handler import output_handler


class test_choice():
    def single_test():

        # Selection for randomly generated/user input puzzle
        print("\nSelect Input Method:\n[1] Random\n[2] File")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            initial_board = input_handler.generate_random_puzzle()
            print("\nRandomly generated puzzle:")
            for i in range(0, 9, 3):
                print(' '.join(map(str, initial_board[i:i+3])))
        else:
            initial_board = input_handler.read_puzzle_input()
    
        # Choose heuristic function
        heuristic_func = get_heuristic()

        # Initialize puzzle
        initial_state = puzzle(initial_board, 0, heuristic_func)

        # Choose a solution depth
        max_depth = int(input("\nEnter Solution Depth (2-20): "))

        # Perform A* search to get the result and search cost
        result, search_cost = a_star_search.a_star_search(initial_state, heuristic_func, max_depth)

        # Print the result
        output_handler.print_solution(result, search_cost)


    def multiple_test():

        # Choose a number of test cases
        test_cases = int(input("Number of test cases: "))

        while test_cases > 0:
            row = input().strip().split()
            initial_board = tuple(int(num) for num in row)
            
            # Choose heuristic function
            heuristic_func = get_heuristic()

            # Initialize puzzle
            initial_state = puzzle(initial_board, 0, heuristic_func)

            # Choose a solution depth
            max_depth = int(input("\nEnter Solution Depth (2-20): "))

            # Perform A* search to get the result and search cost
            result, search_cost = a_star_search.a_star_search(initial_state, heuristic_func, max_depth)

            # Print the result
            output_handler.print_solution(result, search_cost)

            test_cases = test_cases - 1


# Choose between:
#   (1) h1 = the number of misplaced tiles;
#   (2) h2 = the sum of the distances of the tiles from their goal positions.
def get_heuristic():
    heuristic_choice = input("\nSelect H Function: \n[1] H1\n[2] H2\n ").strip()
    return heuristic_function.h1 if heuristic_choice == '1' else heuristic_function.h2
