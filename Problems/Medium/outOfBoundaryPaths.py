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
        