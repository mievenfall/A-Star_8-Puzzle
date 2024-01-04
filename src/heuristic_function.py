# ------------------------------------------------------------
#   Two candidate heuristic functions:
#       (1) h1 = the number of misplaced tiles;
#       (2) h2 = the sum of the distances of the tiles from their goal positions.
# ------------------------------------------------------------

class heuristic_function:
    
    # (1) Calculate number of misplaced tiles
    def h1(board, goal):
        total = 0
        for i in range(8):
            if board[i] != goal[i]:
                total = total +1
        return total


    # (2) Calculate sum of the distances of the tiles from their goal positions
    def h2(board, goal):
        distance = 0
        for i in range(8):
            a = board.index(i) // 3
            b = board.index(i) % 3
            x = goal.index(i) // 3
            y = goal.index(i) % 3
            distance = distance + abs(a - x) + abs(b - y)
        return distance