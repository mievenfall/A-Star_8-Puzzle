class puzzle:
    def __init__(self, board, moves = 0, heuristic_func = None, prev_state= None, goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)):
        
        # The current state of the board
        self.board = board

        # Number of moves so far (depth of node)
        self.moves = moves

        # Heuristic function 
        self.heuristic_func = heuristic_func

        # Previous state for tracing path 
        self.prev_state = prev_state

        # Goal state
        self.goal = goal


    # Check if current board matches goal board
    def is_solved(self):
        return self.board == self.goal


    def next_states(self):
        # List to store successor states
        moves = []

        # Get position of blank tile
        zero_pos = self.board.index(0)  
        row = zero_pos // 3
        col = zero_pos % 3

        # Possible slide directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir_row, dir_col in directions:

            # Check if slide is legal
            new_row = row + dir_row
            new_col = col + dir_col

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                # Swap blank tile and update board
                new_pos = new_row * 3 + new_col
                new_board = list(self.board)
                new_board[zero_pos], new_board[new_pos] = new_board[new_pos], new_board[zero_pos]
                
                # Add new state
                moves.append(puzzle(tuple(new_board), self.moves + 1, prev_state=self))

        return moves


    def __lt__(self, other):
        return self.heuristic(self.heuristic_func) < other.heuristic(other.heuristic_func)


    def heuristic(self, func):
        return func(self.board, self.goal) + self.moves
    