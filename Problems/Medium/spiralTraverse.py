# SPIRAL TRAVERSE

# Create a function that takes in an (n) * (m) two-dimensional array (that
# can be square-shaped when n == m) and returns a one-dimensional array
# of all the array's elements in spiral order.

    # Note:
    # Sprial order starts at the top left corner of the two-dimensional array,
    # then goes to the right, and proceeds in a spiral pattern until all the
    # elements have been visited.

class Solution:
    def spiralTraverse(array):
        # create results array
        result = []

        # initiate variables to represent the starting and ending rows
        startRow, endRow = 0, len(array) - 1

        # initiate variables to represent the starting and ending columns
        startCol, endCol = 0, len(array[0] - 1)