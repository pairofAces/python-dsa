# roman to int Leetcode

class Solution:

    def romanToInt(self, s : str):
        # create a dictionary for the roman numerals and the values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        _res = 0

        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                _res = _res - roman_map[s[i]]
            else:
                _res = _res + roman_map[s[i]]
        
        return _res + roman_map[s[len(s) - 1]]
