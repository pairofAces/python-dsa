# Out of Boundary Paths - Leetcode

# there is an (m * n) grid with a ball. The ball is initially at the position
# [startRow, startColumn]. You're allowed to move the ball to one of the four
# adjacent cells in the grid.
    # note, you might move the ball out of the grid
    # note, you can apply at most (maxMove) moves to the ball

# Given five integers (m, n, maxMove, startRow, startColumn), return
# the number of paths to move the ball out of the grid boundary. 
    # the answer can be large, so return it in modulo (10^9 + 7).

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # create a memo variable as a dictionary
        memo = {}

        # create recursive function to be invoked
        def rec(r, c, M):
            if (r, c, M) in memo: 
                return memo[(r, c, M)]
            if r<0 or c<0 or r>=m or c>=n:
                return 1
            if M == 0:
                return 0
            
            # create a variable to represent the number of moves
            moves = 0

            # initate for loop to traverse through potential grid coordinates
            for x,y in [(1,0), (-1, 0), (0,1), (0, -1)]:
                # invoke recursion of the function (rec) to be incremented into
                # (moves)
                moves += rec(r+x, c+y, M-1)
            memo[(r, c, M)] = moves

            # return the value of (moves)
            return moves
        
        # return the recursive function
        return rec(startRow, startColumn, maxMove)