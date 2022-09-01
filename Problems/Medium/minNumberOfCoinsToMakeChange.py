# Minimum Number of Coins to Make Change 

# Given an array of positive integers representing coin denominations
# and a single non-negative integer, n, representing a target amount of money. 

# Write a function that returns the smallest number of coins required to make the 
# target amount of money, using the given coin denominations. 

# Note, you have an unlimited amount of coins to use at your disposal.

# If it's impossible to make change for the target amount, return -1.

def minNumberOfCoinsToMakeChange(n, denoms):
    numOfCoins = [float('inf') for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
    return numOfCoins[n] if numOfCoins[n] is not float('inf') else -1

n = 7
denoms = [1, 5, 10]

print(minNumberOfCoinsToMakeChange(n, denoms))