# HackerRank
# Subarray Division a.k.a. Birthday Chocolate

# Prompt

# Lily and Ron want to share a choclate bar. Each square has an integer on
# it. 

# Lily decides to share a contiguous segment of the bar such that:
    # the length of the segment matches Ron's birthday Month
    # the sum of the integers on the squares is equal to Ron's birthdyay

# Determine how many ways Lily can divide the bar

class Solution:
    def birthdays(s, d, m):
        # initate pointer and total variables
        i = 0
        total = 0

        # initiate while loop for as long as (i) is less than the
        # length of (s)
        while i < len(s):
            