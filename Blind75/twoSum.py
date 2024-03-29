from typing import List



def twoSum(nums: List[int], target: int):
    prevMap = {} # value : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i