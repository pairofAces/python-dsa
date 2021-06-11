# Can Place Flowers - LeetCode 605

# Given a flowerbed in which some plots are planted, and some are not.
    # Flowers cannot be planted in adjacent plots

# Given an integer array (flowerbed) containing 0s and 1s,
# where 0 means empty and 1 means not empty, and an integer (n).

# return true if (n) new flowers can be planted in the flowerbed without
# violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # initiate tracking variable and variable for the length of input array
        count = 0
        f = len(flowerbed)

        # for loop to traverse through the flowerbed input array
        for i in range(f):
            # if statements for edge cases
            if i - 1 >= 0 and flowerbed[i -1] == 1:
                continue
            if flowerbed[i] == 1:
                continue
            if i + 1 < f and flowerbed[i + 1] == 1:
                continue
             