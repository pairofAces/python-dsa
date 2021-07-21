# SPIRAL TRAVERSE

# Create a function that takes in an (n) * (m) two-dimensional array (that
# can be square-shaped when n == m) and returns a one-dimensional array
# of all the array's elements in spiral order.

    # Note:
    # Sprial order starts at the top left corner of the two-dimensional array,
    # then goes to the right, and proceeds in a spiral pattern until all the
    # elements have been visited.

# Complexity Analysis
    # Time: O(n) time, where (n) is the number of elements in the input array

    # Space: O(n) space, where (n) is the number of elements in the array that
    # was created within the spiralTraverse function -> (result)
class Solution:
    def spiralTraverse(array):
        # create results array
        result = []

        # initiate variables to represent the starting and ending rows
        startRow, endRow = 0, len(array) - 1

        # initiate variables to represent the starting and ending columns
        startCol, endCol = 0, len(array[0] - 1)

        # start conditional statement
            # while he starting row is less than or equal to ending row
            # AND the starting column is less than or equal to ending column
                # proceed to inner conditionals
        while startRow <= endRow and startCol <= endCol:
            #  use for loops for inner logic
                # 4 cases
            for col in range(startCol, endCol + 1):
                # append the element at the starting row and column
                # to the result array -> startingRow -> and initial
                # column value
                result.append(array[startRow][col])
            
            for row in range(startRow, endRow + 1):
                # append the element at the initial row value and the
                # ending colum -> row -> ending column value
                result.append(array[row][endCol])
            
            for col in reversed(range(startCol, endCol)):
                # edge case - row
                    # when there is only a single row in the matrix
                    # we don't want to double count the values since
                    # we've already counted it during the initial
                    # for loop above
                
                # if the starting row is equal to the ending row
                if startRow == endRow:
                    break
                
                # if the starting row and ending row are not equal
                result.append(array[endRow][col])
            
            for row in reversed(range(startRow + 1, endRow)):
                # edge case - column
                    # when there is only a single column in the matrix
                    # we don't want to double count the values since
                    # they have already been accounted for in the second
                    # nested for loop above
                
                # if the starting and ending columns are equal
                if startCol == endCol:
                    break
                
                # if they aren't equal
                result.append(array[row][startCol])
            
            # increment the start rows and columns
            # decrement the end rows and columns
            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
        
        # return the results array
        return result

class Solution2:
    def spiralTraversal(array):
        # create results array
        results = []

        # using a helper function
        spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, results)

        # return the results array
        return results
    
    # create helper function
    def spiralFill(array, rowStart, rowEnd, colStart, colEnd, result):
        # if the starting row or column is larger than it's respected
        # ending row/column
        if rowStart > rowEnd or colStart > colEnd:
            # return a blank statement
            return
        
        # initiate for loops
        for col in range(colStart, colEnd + 1):
            # result
            result.append(array[rowStart][col])
        
        for row in range(rowStart + 1, rowEnd + 1):
            # result
        
        for col in reversed(range(colStart, colEnd)):
            # result
        
        for row in reversed(range(rowStart + 1, rowEnd)):
            # result