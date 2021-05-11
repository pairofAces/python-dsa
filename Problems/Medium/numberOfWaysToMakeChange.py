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