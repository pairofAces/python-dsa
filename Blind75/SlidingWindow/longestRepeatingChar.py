# Leetcode 424 Longest Repeating Character Replacement

# Given a string (s) and an integer (k), choose any character
# in the string and change it to any other uppercase English
# character. You can perform this AT MOST (k) times.

# Return the length of the longest substring containing the same
# letter you can get after peforming the above operations.

# example input: s = "ABAB", k = 2
# example output: 4
# explanation: replace the 2 'A's with 2 'B's or vice versa

def charaterReplacement(s: str, k: int ):
    count = {}
    res = 0

    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l +=1

        res = max(res, r - l + 1)
    return res