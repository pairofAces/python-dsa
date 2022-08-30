# Number of ways to make change

# Given an array of distinct positive integers representing coin denominations
# and a single non-negative integer, n, representing a target amount of money, 
# write a funciton that returns the number of ways to make change for that target
# amount using the given coin denominations. 

# Note, an unlimited amount of coins at your disposal. 

def numberOfWaysToMakeChange(n, denoms):
    # initialize an array where the number of ways to create change will be stored
    ways = [0 for amount in range(n + 1)]

    # base case where the amount is 0
        # only 1 way to make change of $0, and that's by using nothing
    ways[0] = 1
    
    # iterate through array of denoms
    for denom in denoms:
        # create a for loop to iterate through various consecutive amounts
        # from 1 to the target amount, n.
        for amount in range(1, n + 1):
            # check if the denom is less than the amount
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    # return the amount of ways to make the target integer, n. Which will be the 
    # value assigned to location ways[n]
    return ways[n]