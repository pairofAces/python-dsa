# Leetcode 121 - Best Time to Buy and Sell Stock

# say you have an array for which the (i)th element is the 
# price of a given stock on day (i)

# if you're only permitted to complete at most one transaction (
# i.e. buy one and sell one share of the stock), design an
# algorithm to find the max profit. 

# NOTE - cannot sell a stock before buying one

from typing import List

# Time Complexity: O(n) time, where (n) is the length of the input list
# Space Complexity: O(1) space, since no external data structures are being used other than
# creating 2 variables used as pointers
def maxProfit(prices: List[int]):
    # create 2 pointers to represent buying(left pointer) and selling(right pointer)
    l, r = 0, 1

    # initialize current max profit 
    maxP = 0

    # iterate through the array as long as the right pointer
    # index location is less than the length of the input array
    while r < len(prices):
        # is the opporunity profitable?
        if prices[l] < prices[r]:
            # calculate the current profit
            profit = prices[r] - prices[l]

            # update the max profit based if there's a new max
            maxP = max(maxP, profit)
        else:
            # else if the current price at the left pointer is larger than the price
            # at right pointer, update left pointer to equal the lower price at the right pointer.
            l = r
        # increment the right pointer by 1
        r += 1
    # return the final max profit value
    return maxP