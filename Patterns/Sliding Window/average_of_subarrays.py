# Given an array, find he average of all subarrays of 'k' 
# contiguous elements in it

# array = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5

# first 5 numbers (subarray from index 0 - 4), average: (1 + 3 + 2 + 6 -1)/ 5 => 2.2
# next 5 numbers (subarray from index 1 - 5), average: (3 + 2 + 6 - 1 + 4)/ 5 => 2.8
# next 5 numbers (subarray from index 2 - 6), average: (2 + 6 -1 + 4 + 1)/ 5 => 2.4

# expected output : [2.2, 2.8, 2.4, 3.6, 2.8]

# BRUTE FORCE SOLUTION
    # calculate the sum of every k-element subarray of the given array
    # and divide the sum by k

def find_averages_of_subarrays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        # find the sum of the next 'k' elements
        _sum = 0.0
        for j in range(i, i + k):
            _sum+= arr[j]
        result.append(_sum/k) # calculate the average and append to the (result) array
    
    # return the result
    return result

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of the subarrays of size k: " + str(result))

main()