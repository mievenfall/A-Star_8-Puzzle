# ------------------------------------------------------------
#   Handle output printing:
#       (1) If there is a soluton/result, print out steps and search cost
#       (2) If there is no solution, notify user and print out search cost
# ------------------------------------------------------------

class output_handler:
    def print_solution(solution_state, search_cost):

        # (1) If there is a soluton/result, print out steps and search cost
        if solution_state:
            print("\nSolution found")
            path = []

            while solution_state:
                path.append(solution_state)
                solution_state = solution_state.prev_state

            for state in reversed(path):
                print("Step:", state.moves)
                for i in range(0, 9, 3):
                    print(' '.join(map(str, state.board[i:i+3])))
                print() 

        # (2) If there is no solution, notify user and print out search cost
        else:
            print("\nNo solution found")
        print("Search Cost:", search_cost)
        print()
