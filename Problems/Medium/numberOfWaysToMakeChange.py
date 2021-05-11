# NUMBER OF WAYS TO MAKE CHANGE 

# THE PROMPT

# Given an array of unique positive integers, each representing coin
# denominations and a single non-negative integer, (n), representing a
# target amount of money, write a function that returns the number of WAYS
# to make change for that target amount using the given coin denominations.

# Note, you have an unlimited amount of coins

# Solution 1

# create a function that takes in an integer, (n), and an array of integers, (array)
class Solution:
    def numberOfWaysToMakeChange(n, denoms):
        # create another array with 1 more element than the input array
        ways = [0 for amount in range(n + 1)]

        # set the first element in the new array to 1
        ways[0] = 1

        # use a for loop, to traverse through the denoms array
        for denom in denoms:

            # use a nested for loop to act as index pointers
            for amount in range(1, n + 1):

                # now use an if statement to check if (denom)'s value is 
                # less than or equal to the value of (amount)
                if denom <= amount:
                    
                    # if it is, then incrememnt the element at the index of (amount), in
                    # the (ways) array, by the element located at the index of 
                    # (amount - denom)
                    ways[amount] += ways[amount - denom]
        
        # once getting out of the complete for loop, return the element at the 
        # (n)th position in (ways)
        return ways[n]