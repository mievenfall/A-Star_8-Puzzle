import heapq
from puzzle import puzzle 


class a_star_search:
    def a_star_search(start_state, heuristic_func, max_depth):
        
        # Initialize frontier as a priority queue using heapq
        frontier = []
        heapq.heappush(frontier, (0, start_state))

        # Keep track of explored states
        explored = set()

        # Keep track of search cost
        search_cost = 0 

        while frontier:

            # Get the state with lowest estimated total cost
            _, current_state = heapq.heappop(frontier)

            # Increment search cost for each state explored
            search_cost += 1  

             # Check if we have reached the solution state
            if current_state.is_solved():
                return current_state, search_cost  # Return solution and search cost

            # Prune if max depth exceeded
            if current_state.moves > max_depth:
                continue

            # Add current state to explored set
            explored.add(current_state.board)

            # Expand current state
            for state in current_state.next_states():

                # Check if successor is already explored
                if state.board not in explored:
                    # Create a new state object
                    new_state = puzzle(state.board, state.moves, heuristic_func, prev_state=current_state)
                    
                    # Calculate total estimated cost
                    total_cost = new_state.heuristic(heuristic_func)

                    # Add state to frontier with calculated cost
                    heapq.heappush(frontier, (total_cost, new_state))
                else:
                    search_cost += 1
        
        # If no solution found, return search cost anyway
        return None, search_cost  # No solution found, return search cost anyway

